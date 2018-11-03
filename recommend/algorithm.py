from .models import Smartphone 

#TODO: budget
def calculate(main, system, size):
    smartphones = Smartphone.objects.all().filter(system=system)
    calculated = []

    for smartphone in smartphones:
        fit = 0
        if main == 'camera':
            fit += smartphone.camera_rate * 5
        elif main == 'efficient':
            fit += smartphone.eficient_rate * 5
        elif main == 'battery':
            fit += smartphone.battery_rate * 5
        elif main == 'display':
            fit += smartphone.display_rate * 5
        
        if smartphone.size == size:
            fit += 20

        smartphone.fit = fit
        calculated.append(smartphone)
    
    return calculated

    # for smartphone in smartphones:
    #     if smartphone.screen_size < 4.5:
    #         smartphone.size = 'small'
    #     elif smartphone.screen_size <= 6:
    #         smartphone.size = 'medium'
    #     else:
    #         smartphone.size = 'huge'
    #     smartphone.save()
    
    