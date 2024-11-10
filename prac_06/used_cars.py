from prac_06.car import Car


def main():
    my_car = Car(name="My Car", fuel=180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # Create a new car object called "limo" and perform operations on it
    limo = Car(name="Limo", fuel=100)
    limo.add_fuel(20)
    print(f"Limo has fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)


main()
