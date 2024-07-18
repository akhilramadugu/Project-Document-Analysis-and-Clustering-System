import matplotlib.pyplot as mtl

no_of_files = [10, 20, 40, 80, 100, 200, 300, 400, 502]
kb = [81, 143, 293, 575, 655, 2011, 2238, 6310, 8093]

mtl.plot(no_of_files, kb)

mtl.title('Line Plot')
mtl.xlabel('Number of Files')
mtl.ylabel('Memory of Postings+Dictionary')

mtl.savefig("Memory Graph")
