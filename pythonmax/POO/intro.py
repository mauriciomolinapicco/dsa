class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"This {self.model} is driving")

    def stop(self):
        print('The car is stopped')


def main():
    car1 = Car('chevy', 2003, 'blue')
    car1.drive()

if __name__ == '__main__':
    main()