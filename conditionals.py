""" Meltdown Mitigation exercise """
import math

def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: temperature value (integer or float)
    :param neutrons_emitted: number of neutrons emitted per second (integer or float)
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
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

    pass
