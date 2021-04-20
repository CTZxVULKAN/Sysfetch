#!/usr/bin/python3
import curses
import time
import psutil
import os

#CPU FUNCTIONS

def get_cpu_usage_pct():
    """
    Obtains the system's average CPU load as measured over a period of 500 milliseconds.
    :returns: System CPU load as a percentage.
    :rtype: float
    """
    return psutil.cpu_percent(interval=0.5)

def get_cpu_frequency():
    """
    Obtains the real-time value of the current CPU frequency.
    :returns: Current CPU frequency in MHz.
    :rtype: int
    """
    return int(psutil.cpu_freq().current)

def get_cpu_temp():
    """
    Obtains the current value of the CPU temperature.
    :returns: Current value of the CPU temperature if successful, zero value otherwise.
    :rtype: float
    """
    # Initialize the result.
    result = 0.0
    # The first line in this file holds the CPU temperature as an integer times 1000.
    # Read the first line and remove the newline character at the end of the string.
    if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            line = f.readline().strip()
        # Test if the string is an integer as expected.
        if line.isdigit():
            # Convert the string with the CPU temperature to a float in degrees Celsius.
            result = float(line) / 1000
    # Give the result back to the caller.
    return result





#RAM FUNCTIONS

def get_ram_total():
    """
    Obtains the total amount of RAM in bytes available to the system.
    :returns: Total system RAM in bytes.
    :rtype: int
    """
    return int(psutil.virtual_memory().total)

def get_ram_usage_pct():
    """
    Obtains the system's current RAM usage.
    :returns: System RAM usage as a percentage.
    :rtype: float
    """
    return psutil.virtual_memory().percent

def get_ram_usage():
    """
    Obtains the absolute number of RAM bytes currently in use by the system.
    :returns: System RAM usage in bytes.
    :rtype: int
    """
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)

#SWAP FUNCTIONS

def get_swap_usage():
    """
    Obtains the absolute number of Swap bytes currently in use by the system.
    :returns: System Swap usage in bytes.
    :rtype: int
    """
    return int(psutil.swap_memory().used)

def get_swap_total():
    """
    Obtains the total amount of Swap in bytes available to the system.
    :returns: Total system Swap in bytes.
    :rtype: int
    """
    return int(psutil.swap_memory().total)

def get_swap_usage_pct():
    """
    Obtains the system's current Swap usage.
    :returns: System Swap usage as a percentage.
    :rtype: float
    """
    return psutil.swap_memory().percent



#OUTPUT

def main(stdscr):

    cpu_freqz = ' CPU frequency : {} MHz'.format(get_cpu_frequency())
    cpu_useage_pct = ' CPU usage : {}%'.format(get_cpu_usage_pct())
    cpu_temp = ' CPU temperature : {}°C'.format(get_cpu_temp())

    ram_used = ' System RAM used : {} MB'.format(int(get_ram_usage() / 1024 / 1024))
    ram_total = ' Total available RAM : {} MB'.format(int(get_ram_total() / 1024 / 1024))
    ram_useage_pct=' RAM usage : {}%'.format(get_ram_usage_pct())

    swap_used = ' SWAP used : {} MB'.format(int(get_swap_usage() / 1024 / 1024))
    swap_total = ' Total available SWAP : {} MB'.format(int(get_swap_total() / 1024 / 1024))
    swap_useage_pct = ' Swap usage : {}%'.format(get_swap_usage_pct())

    stdscr.addstr(0,1,"CPU Status")
    stdscr.addstr(1,1,cpu_freqz)
    if os.path.exists("/sys/class/thermal/thermal_zone0"):
            stdscr.addstr(2,1,cpu_temp)
    stdscr.addstr(3,1,cpu_useage_pct)

    stdscr.addstr(4,1,"")

    stdscr.addstr(5,1,"RAM Status")
    stdscr.addstr(6,1,ram_used)
    stdscr.addstr(7,1,ram_total)
    stdscr.addstr(8,1,ram_useage_pct)


    stdscr.addstr(9,1,"")

    stdscr.addstr(10,1,"SWAP Status")
    stdscr.addstr(11,1,swap_used)
    stdscr.addstr(12,1,swap_total)
    stdscr.addstr(13,1,swap_useage_pct)



    stdscr.refresh()
    time.sleep(10)

curses.wrapper(main)


