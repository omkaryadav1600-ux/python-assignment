import sys
import shutil

source = sys.argv[1]

shutil.copy(source, "Demo.txt")

print("File copied successfully into Demo.txt")