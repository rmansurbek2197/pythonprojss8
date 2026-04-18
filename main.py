def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    n = int(input("Fibonacci ketma-ketligining uzunligini kiriting: "))
    print(fibonacci(n))

def validate_input(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n <= 0:
                print("Iltimos, haqiqiy musbat son kiriting.")
            else:
                return n
        except ValueError:
            print("Iltimos, haqiqiy son kiriting.")

def print_fibonacci(n):
    fib_sequence = fibonacci(n)
    print(f"Fibonacci ketma-ketligi: {fib_sequence}")

def get_user_choice():
    while True:
        choice = input("Fibonacci ketma-ketligini kiritishni davom ettirmoqchimisiz? (ha/yo'q): ")
        if choice.lower() == "ha":
            return True
        elif choice.lower() == "yo'q":
            return False
        else:
            print("Iltimos, ha yoki yo'q deb javob bering.")

def main_loop():
    while True:
        n = validate_input("Fibonacci ketma-ketligining uzunligini kiriting: ")
        print_fibonacci(n)
        if not get_user_choice():
            break

main_loop()