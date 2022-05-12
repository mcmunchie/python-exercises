import car

def test_init():
    honda = car.Car('2012', 'Honda')
    assert honda.get_speed() == 0
    assert honda.get_make() == 'Honda'
    assert honda.get_year_model() == '2012'

def test_accelerate():
    # setup / arrange
    honda = car.Car('2012', 'Honda')
    # execution / act
    honda.accelerate()
    # verify / assert
    assert honda.get_speed() == 5

def test_brake_when_speed_is_zero():
    # setup / arrange
    honda = car.Car('2012', 'Honda')
    # execution / act
    honda.brake()
    # verify / assert
    assert honda.get_speed == 0

def test_brake_when_speed_is_5():
    # setup / arrange
    honda = car.Car('2012', 'Honda')
    # execution / act
    honda.accelerate()
    honda.brake()
    # verify / assert
    assert honda.get_speed() == 0

def test_brake_when_speed_is_greater_than_5():
    # setup / arrange
    honda = car.Car('2012', 'Honda')
    # execution / act
    honda.accelerate()
    honda.accelerate()
    honda.brake()
    # verify / assert
    assert honda.get_speed() == 5

def test_string_method():
    honda = car.Car('2012', 'Honda')

    print(honda)

def test_string_method_2(capsys):
    honda = car.Car('2012', 'Honda')
    honda.accelerate()
    print(honda)

    captured = capsys.readouterr()
    assert captured.out == "The year model is 2012, make is Honda, current speed is 5\n"
    