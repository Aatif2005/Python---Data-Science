'''code = 20000
match code:
    case 200:
        print("Response ok")
        print("Good Job!")
    case 500:
        print("Bad response")
    case 2000:
        print("Worst response")
    case __:
        print("Nothing matched ")

print("End of the program")'''

'''def http_status(code):
    match code:
        case 200:
            return "OK"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

print(http_status(200))  # Output: OK
print(http_status(404))  # Output: Not Found'''

point = (3,4)
match point:
    case(0,0):
        print("Origin")
    case(x,0):
        print(f"x-axis at {x}")
    case(0,y):
        print((f"y-axis at {y}"))
    case(x,y):
        print((f"Point at ({x},{y})"))