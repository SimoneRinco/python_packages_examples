from mypkg import bar

def print_me():
    print(f"I am mypkg.sub1.sub1one ({__file__})")
    print(f"Here is my friend bar: ")
    bar.print_me()