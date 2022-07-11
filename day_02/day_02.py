import os
import sys

import test_to_import_1 as t1

#Here we are trying to import something (test_to_import_2.py) which is not in the same location folder of this file (day_02.py). 
#Because of this, we can't just import it with one line of code (differently to what we did with 'import test_to_import_1 as t1' where 
#test_to_import_1.py is actually in the same folder of this file 'day_02.py')

#So, we need first to 'point' to the folder that containts 'test_to_import_1.py' (line 17), then we have sys.path.append(directoryofthefilewewanttoimport), 
#then import the file (line 21). 
#To move back and forth we'll use os.path.dirname(foldersuccessiva), os.path.join(folderpresente, 'folderincuivoglioentrare') 

current_directory = os.path.dirname(os.path.realpath(__file__))
print (current_directory)

final_directory = os.path.join(current_directory, 'test_folder')
print (final_directory)
sys.path.append(final_directory)

import test_to_import_2 as t2

#In this case see this way 'to go back'

parent_directory = os.path.dirname(current_directory)
print (parent_directory)