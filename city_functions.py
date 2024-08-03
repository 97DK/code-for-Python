def city_country(city,country,population=''):
    if population:
        C_c=f"{city},{country}-{population}"
    else:
        C_c=f"{city},{country}"
    return C_c
a=city_country('beijing',"China")
print(a)