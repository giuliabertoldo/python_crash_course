# 8.5 PASSING AN ARBITRARY NUMBER OF ARGUMENTS
## EXERCISE 8-12

def sandwiches(*items):
    """Summarize the sandwich we are about to make"""
    print("\nMaking a sandwich with the following ingredients:")
    for item in items:
        print(f"- {item}")

sandwiches('ham')

sandwiches('ham', 'mushrooms')

sandwiches('ham', 'mushrooms', 'mayo')
