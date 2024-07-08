import os
path=input("enter path name")
print("only dicritories")
print([name for name in os.listdir(path)if os.path.isdir(os.path.join(path,name))])
print("\n only files:")
print([name for name in os.listdir(path)if not os.path.isdir(os.path.join(path,name))])
print("\n all dictories and files")
print([names for names in os.listdir(path)])

