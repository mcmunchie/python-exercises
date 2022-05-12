import car 

def main():
    ford = car.Car('2013', 'Focus')
    hyundai = car.Car('2020', 'Tucsun')

    # do something with the car object 
    make_car_go_fast(ford)
    make_car_go_fast(hyundai)

    print(ford)
    print(hyundai)

def make_car_go_fast(a_car):
    a_car.accelerate()
    a_car.accelerate()
    a_car.accelerate()
    a_car.accelerate()
    a_car.accelerate()
    a_car.accelerate()
    a_car.accelerate()

if __name__ == '__main__':
    main()
