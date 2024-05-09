import gradio as gr
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
task = Tasks.token_classification
#模型导入
model = 'damo/mgeo_geographic_elements_tagging_chinese_base'
pipeline_ins = pipeline(
    task=task, model=model)

#地址提取
def gn(inputs):
    '''
    输入：一个字符串，表示需要提取地址的语句
    输出：一个字典，表示地址提取结果
    例：
    输入：'解析并提取快递单据中的文本信息，广东省清远市清城区石角镇美林湖大东路口佰仹公司标准规范的输出结构化信息，包含姓名、电话、地址，帮助快递或电商企业提高单据处理效率 郑万顺 15345785872'
    输出：{'poi': '美林湖大东路佰仹公司', 'prov': '广东省', 'city': '清远市', 'district': '清城区', 'town': '石角镇'}
    '''
    res = pipeline_ins(input=inputs)
    length = len(inputs)
    print(res)
    output = {'poi':''}
    lis = ['prov','city','district','town']
    lf = length
    rg = 0
    for x in res['output']:
        if x['type'] in lis:
            output[x['type']] = x['span']
            lf = length
            rg = 0
        else:
            if lf == length:
                lf = x['start']
                rg = x['end']
            elif x['start'] - rg < 7:
                rg = x['end']
    output['poi'] = inputs[lf:rg]
    return output


#gradio框架封装
def text(input):
    out=gn(input)
    output = ""
    if 'prov' in out:
        output += out['prov']
    else:
        output += ' '
    if 'city' in out:
        output += ", "
        output += out['city']
    else:
        output += ",  "
    if 'district' in out:
        output += ", "
        output += out['district']
    else:
        output += ",  "
    if 'town' in out:
        output += ", "
        output += out['town']
    else:
        output += ",  "
    if 'poi' in out:
        output += ", "
        output += out['poi']
    else:
        output += ",  "
    return [output.split(',') for _ in output.split('\n')]


with gr.Blocks() as demo:
    with gr.Column():
        text1 = gr.Textbox(label="请输入一段想分析的文本：", lines=10)
        but = gr.Button("开始分析")
    with gr.Row():
        output = gr.DataFrame(label='地址',
                              headers=["省", "市", "区", "镇","具体地址"],
                              datatype=["str", "str", "str", "str", "str"],
                              interactive=True, wrap=True,row_count=(1, "fixed"),col_count=(5, "fixed"))
        but.click(fn=text,inputs=text1,outputs=output)

demo.launch(server_name="0.0.0.0", server_port=7864)

