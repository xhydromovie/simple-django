from .models import Smartphone 
import operator

def calculate(d):
    my_d = d.dict()
    helper = {}
    diffrence = 0

    smartphones = Smartphone.objects.all().filter(price__range=(0, my_d.get('price')), system=my_d.get('system'))
    print(smartphones)

    for smartphone in smartphones:
        num = 0
        fit = 0

        for q in d.getlist('main'):
            if q == 'camera':
                fit += smartphone.camera_rate * 8
            elif q == 'efficient':
                fit += smartphone.efficient_rate * 8
            elif q == 'battery':
                fit += smartphone.battery_rate * 8
            elif q == 'display':
                fit += smartphone.display_rate * 8
            num += 1

        fit = fit/num

        if smartphone.size == d.getlist('size')[0]:
            fit += 20

        smartphone.fit = int(fit) #modify fit

        helper.update({smartphone.name: smartphone.fit})


    for smartphone in smartphones:
        if smartphone.name == max(helper, key=helper.get):
            diffrence = 100 - smartphone.fit

    for smartphone in smartphones:
        smartphone.fit += diffrence - 2

    for smartphone in smartphones:
        if smartphone.id == 1:
            print(smartphone.name, smartphone.fit)

    print (helper)
    print (max(helper, key=helper.get))

    return smartphones

    # for smartphone in smartphones:
    #     if smartphone.screen_size < 4.5:
    #         smartphone.size = 'small'
    #     elif smartphone.screen_size <= 6:
    #         smartphone.size = 'medium'
    #     else:
    #         smartphone.size = 'huge'
    #     smartphone.save()
    
    