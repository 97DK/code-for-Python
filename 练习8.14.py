def make_car(maker,type,**info):
    car_info={
        'maker':maker,
        'model':type
    }
    car_info.update(info)
    for k,v in car_info.items():
        print(f"There have some informations about this car:{k}:{v}")
    return car_info
car = make_car('subaru', 'outback', color='blue',tow_package='True')
print(car)

