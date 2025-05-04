class Logger:
    def __init__(self):
        print("Logger created")  # Constructor message
    
    def __del__(self):
        print("Logger destroyed")  # Destructor message

print("Creating objects:")
obj1 = Logger()
obj2 = Logger()
obj3 = Logger()
obj4 = Logger()
obj5 = Logger()

print("\nDeleting one object:")
del obj1
del obj3
print("\nProgram ending - remaining objects will be destroyed:")