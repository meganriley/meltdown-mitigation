""" Meltdown Mitigation exercise """
import math

def is_criticality_balanced(temperature, neutrons_emitted):
    return True if (temperature < 800) and (neutrons_emitted > 500) and (temperature * neutrons_emitted < 500000) else False



def reactor_efficiency(voltage, current, theoretical_max_power):
    percentage = ((voltage * current)/theoretical_max_power) *100
    percent = math.floor(percentage)
    

    if percent < 30:
        return 'black'
    elif percent >= 30 and percent < 60:
        return 'red'
    elif percent >=60 and percent < 80:
        return 'orange'
    else:
        return 'green'



def fail_safe(temperature, neutrons_produced_per_second, threshold):
    value = temperature * neutrons_produced_per_second
    if value < (.9 * threshold):
        return 'LOW'
    elif value >= (.9 * threshold) and value <= (1.1 * threshold):
        return 'NORMAL'
    else:
        return 'DANGER'
