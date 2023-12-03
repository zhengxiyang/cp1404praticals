import random

NUM_QUICK_PICKS = 5
NUM_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUM_PER_LINE))

def display_quick_picks(quick_picks):
    for line in quick_picks:
        print(" ".join(map(str, line)))

def main():
    num_quick_picks = int(input("How many quick picks? "))

    quick_picks = []
    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        quick_picks.append(quick_pick)

    display_quick_picks(quick_picks)

if __name__ == "__main__":
    main()
