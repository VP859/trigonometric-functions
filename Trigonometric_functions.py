import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from time import process_time
import csv

class Trigonometric:
    def __init__(self, file_path = '') -> None:
        self.file_path = file_path

        if self.file_path:
            self.initialise(self.file_path)
        else:
            self.generate()


    def sin(self):
        data = np.sort(self.data)

        values = np.sin(data)

        fig, ax = plt.subplots()
        ax.plot(data, values)

        ax.set_title('Sin function')
        ax.set_xlabel('Values')
        ax.set_ylabel('Sin values')

        plt.title('Sin function')

        plt.savefig('figures/sin_function.png', format='png', dpi=300)


    def cos(self):
        data = np.sort(self.data)

        values = np.cos(data)

        fig, ax = plt.subplots()
        ax.plot(data, values)

        ax.set_title('Cos function')
        ax.set_xlabel('Values')
        ax.set_ylabel('Cos values')

        plt.title('Cos function')

        plt.savefig('figures/cos_function.png', format='png', dpi=300)


    def tan(self):
        data = np.sort(self.data)

        values = np.tan(data)

        fig, ax = plt.subplots()
        ax.plot(data, values)

        ax.set_title('Tan function')
        ax.set_xlabel('Values')
        ax.set_ylabel('Tan values')

        plt.title('Tan function')

        plt.savefig('figures/tan_function.png', format='png', dpi=300)


    def arctan(self):
        data = np.sort(self.data)

        values = np.arctan(data)

        fig, ax = plt.subplots()
        ax.plot(data, values)

        ax.set_title('Arctan function')
        ax.set_xlabel('Values')
        ax.set_ylabel('Arctan values')

        plt.title('Arctan function')

        plt.savefig('figures/arctan_function.png', format='png', dpi=300)
    

    
    def arcsin(self):
        data = np.sort(self.data)

        values = np.arcsin(data)

        fig, ax = plt.subplots()
        ax.plot(data, values)

        ax.set_title('Arcsin function')
        ax.set_xlabel('Values')
        ax.set_ylabel('Arcsin values')

        plt.title('Arcsin function')

        plt.savefig('figures/arcsin_function.png', format='png', dpi=300)

    
    def arccos(self):
        data = np.sort(self.data)

        values = np.arccos(data)

        fig, ax = plt.subplots()
        ax.plot(data, values)

        ax.set_title('Arccos function')
        ax.set_xlabel('Values')
        ax.set_ylabel('Arccos values')

        plt.title('Arccos function')

        plt.savefig('figures/arccos_function.png', format='png', dpi=300)


    def display(self):
        plt.show()


    def initialise(self, file_path):
        data = []
        with open(file_path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                for element in row:
                    data.append(float(element))

        self.data = np.array(data)
    

    def generate(self, size = 1000):
        self.data = np.random.randint(0, 90, size)

        self.data = np.radians(self.data)

        

    



if __name__ == '__main__':
    start = process_time()

    functions = Trigonometric()

    functions.sin()
    functions.cos()
    functions.tan()
    functions.arctan()
    functions.arcsin()
    functions.arccos()

    end = process_time()

    print(f'Time taken: {end - start}')