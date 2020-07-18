# open in ths sintax wil overide everything on the file
file_builder = open('logger.txt', 'w+')

for i in range(100):
    file_builder.write(f'Im on line {i + 1}\n')
# file_builder.write('Hey, Im in a file!')

file_builder.close()