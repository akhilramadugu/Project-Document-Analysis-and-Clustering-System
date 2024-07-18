import matplotlib.pyplot as mtl

no_of_files = [10, 20, 40, 80, 100, 200, 300, 400, 502]
ms = [115, 190, 380, 799, 938, 1984, 4200, 10558, 16364]

mtl.plot(no_of_files, ms)

mtl.title('Line Plot')
mtl.xlabel('Number of Files')
mtl.ylabel('Time taken in ms')

mtl.savefig("Performance Graph")
