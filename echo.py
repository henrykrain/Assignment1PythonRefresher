def echo(text: str, repetitions: int = 3) -> str:
    """imitate a real world echo."""
    str_len: int = repetitions
    for x in range(repetitions):
        print(text[len(text)-str_len:])
        str_len = str_len - 1
    print('.')

if __name__ == "__main__": 
    text = input("Yell something at a mountain: ")
    print(echo(text))

#    Yell something at a mountain: Helloooo
#    ooo
#    oo
#    o
#    .
    
#    Yell something at a mountain: echo 123
#    123
#    23
#    3
#    .