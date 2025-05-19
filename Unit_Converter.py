def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    while True:
        print("\nUnit Converter")
        print("[1] Meters ↔ Feet")
        print("[2] Kilograms ↔ Pounds")
        print("[3] Celsius ↔ Fahrenheit")
        print("[4] Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            m = float(input("Enter meters: "))
            print(f"{m} meters = {meters_to_feet(m):.2f} feet")
            f = float(input("Enter feet: "))
            print(f"{f} feet = {feet_to_meters(f):.2f} meters")
        elif choice == "2":
            kg = float(input("Enter kilograms: "))
            print(f"{kg} kg = {kg_to_pounds(kg):.2f} lbs")
            lbs = float(input("Enter pounds: "))
            print(f"{lbs} lbs = {pounds_to_kg(lbs):.2f} kg")
        elif choice == "3":
            c = float(input("Enter Celsius: "))
            print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
            f = float(input("Enter Fahrenheit: "))
            print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()