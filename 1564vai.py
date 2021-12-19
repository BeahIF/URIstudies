while True:
    try:
        i=int(input())
        if(i>1):
            print("vai ter duas!")
        else:
            print("vai ter copa")
    except EOFError:
        break