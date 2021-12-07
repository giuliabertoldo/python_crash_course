# 8.2 PASSING ARGUMENTS
## EXERCISE 8-4

def make_shirt(text = 'I love Python', size = 'L'):
    print(f"The T-shirt size is {size} with text {text}.")

make_shirt()
make_shirt(size = 'M')
make_shirt(size ='S', text = "Hello" )
