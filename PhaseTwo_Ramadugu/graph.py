import matplotlib.pyplot as mtl

no_of_files = [10, 20, 40, 80, 100, 200, 300, 400, 503]
ms = [122, 194, 364, 744, 810, 1502, 3051, 6484, 10282]

mtl.plot(no_of_files, ms)

mtl.title('Line Plot')
mtl.xlabel('Number of Files')
mtl.ylabel('Time taken in ms')

mtl.savefig("Performance Graph")
