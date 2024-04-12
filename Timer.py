import time


def countdown_timer():
    def divisor_f(seconds, divisor):
        quotient = seconds // divisor
        remainder = seconds % divisor
        return quotient, remainder

    def input_time():
        while True:
            try:
                time_input = input("Insert time to count down (h:m:s) ")
                hs, ms, ss = map(int, time_input.split(':'))
                total_s = hs * 3600 + ms * 60 + ss
                if total_s < 0:
                    raise ValueError("Please enter a non-negative time.")
                return total_s
            except ValueError as e:
                print("Invalid input:", e)

    total_seconds = input_time()
    while total_seconds:
        h, r = divisor_f(total_seconds, 3600)
        m, s = divisor_f(r, 60)
        timer_display = f"{h:02d}:{m:02d}:{s:02d}"
        print(timer_display)
        time.sleep(1)
        total_seconds -= 1
    print("Time's up!")


countdown_timer()
