import random

'''
function changes the Unit status depending on the thresholds
'''
def unit_status(temperature):
    THRESHOLD = 75
    if temperature >= THRESHOLD:
        return "Unit ON"
    else:
        return "Unit OFF"


if __name__ == '__main__':

    # output 20 results of unit_status depending on random temperature
    for count in range(1, 21):
        temperature = random.randrange(0, 100)
        print("{}. Temperature now is {}. {}".
              format(count, temperature, unit_status(temperature)))


