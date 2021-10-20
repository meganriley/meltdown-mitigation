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
    """Assess and return status code for the reactor.

    :param temperature: value of the temperature (integer or float)
    :param neutrons_produced_per_second: neutron flux (integer or float)
    :param threshold: threshold (integer or float)
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 90% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutrons per second` is not in the above-stated ranges ==  'DANGER'
    """

    value = temperature * neutrons_produced_per_second
    minus_ten = threshold - (threshold * .10)
    print(minus_ten)
    plus_ten = threshold + (threshold * .10)
    print(plus_ten)
    if value < (.9 * threshold):
        return 'LOW'
    elif value >= (.9 * threshold) and value <= (1.1 * threshold):
        return 'NORMAL'
    else:
        return 'DANGER'
