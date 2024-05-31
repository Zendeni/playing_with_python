import sys
import time
import sevseg  # Ensure you have the sevseg.py module in the same directory.

# Change this to any number of seconds:
SECONDS_LEFT = 30

def clear_screen():
    """Clear the console screen in a cross-platform way."""
    if sys.platform.startswith('win'):
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def format_time(seconds_left):
    """Convert seconds to hours, minutes, and seconds."""
    hours = str(seconds_left // 3600).zfill(2)
    minutes = str((seconds_left % 3600) // 60).zfill(2)
    seconds = str(seconds_left % 60).zfill(2)
    return hours, minutes, seconds

def display_countdown(hours, minutes, seconds):
    """Get the digit strings from sevseg module and display them."""
    h_digits = sevseg.getSevSegStr(hours, 2)
    h_top, h_middle, h_bottom = h_digits.splitlines()

    m_digits = sevseg.getSevSegStr(minutes, 2)
    m_top, m_middle, m_bottom = m_digits.splitlines()

    s_digits = sevseg.getSevSegStr(seconds, 2)
    s_top, s_middle, s_bottom = s_digits.splitlines()

    # Display the digits:
    print(f"{h_top} {m_top} {s_top}")
    print(f"{h_middle} * {m_middle} * {s_middle}")
    print(f"{h_bottom} * {m_bottom} * {s_bottom}")

def main():
    """Main program loop."""
    seconds_left = SECONDS_LEFT

    try:
        while True:
            clear_screen()
            hours, minutes, seconds = format_time(seconds_left)
            display_countdown(hours, minutes, seconds)

            if seconds_left == 0:
                print()
                break

            print()
            print('Press Ctrl-C to quit.')

            time.sleep(1)  # Insert a one-second pause.
            seconds_left -= 1
    except KeyboardInterrupt:
        print('\nCountdown interrupted.')
        sys.exit()

if __name__ == "__main__":
    main()
