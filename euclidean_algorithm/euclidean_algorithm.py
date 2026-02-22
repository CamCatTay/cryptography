# assumptions and equations
# s1 = 1, s2 = 0
# t1 = 0, t2 = 1
# s = s1 - s2 * q
# t = t1 - t2 * q

# just repeat (b, a % b) for gcd
def basic_euclidean(a, b):
    if b == 0:
        return a
    else:
        return basic_euclidean(b, a % b)

def extended_euclidean(a, b):
    orig_a, orig_b = a, b

    # can't divide by zero so set defaults and return original values
    if b == 0:
        d = abs(a)
        t = 1 if a > 0 else -1
        s = 0
        return orig_a, orig_b, d, s, t

    swapped = False
    if abs(a) < abs(b):
        a, b = b, a
        swapped = True

    # set assumptions
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    # perform calculations
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    d = old_r
    s_coef = old_s
    t_coef = old_t

    # ensure results are positive
    if d < 0:
        d = -d
        s_coef = -s_coef
        t_coef = -t_coef

    if swapped:
        s_coef, t_coef = t_coef, s_coef

    return orig_a, orig_b, d, s_coef, t_coef

# helper to make sure input is valid
def convert_to_int(num):
    negative = False
    if num[0] == "-":
        negative = True
        num = num.replace("-", "")

    if not num.isdigit():
        return False

    num = int(num)

    if negative:
        return -num
    else:
        return num

def main():
    # colors for output
    ORANGE = "\033[38;2;255;165;0m"
    RESET = "\033[0m"

    print(f"{ORANGE}\nCtrl + C to end loop\n{RESET}")

    while True:
        try:
            str_a = input("Enter a: ").strip()
            str_b = input("Enter b: ").strip()

            int_a = convert_to_int(str_a)
            int_b = convert_to_int(str_b)

            if (int_a is False or int_b is False):
                print("\nInvalid Input\n")
                continue

            print(f"\nGCD({int_a}, {int_b})")

            a,b,d,s,t = extended_euclidean(int_a, int_b)
            print(f"a = {a} b = {b} d = {d} s = {s} t = {t}\n")

        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled")
            break

# initialize
main()