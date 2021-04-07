import psutil
import os

def main():

    print("CPU Status")
    print(' CPU frequency : {} MHz'.format(get_cpu_frequency()))

    # /sys/class/thermal/thermal_zone0 directory does not exist in some linux distros in that case the cpu temp is displayed 0.  
    if os.path.exists("/sys/class/thermal/thermal_zone0"):
        print(' CPU temperature : {}°C'.format(get_cpu_temp()))

    print(' CPU usage : {}%'.format(get_cpu_usage_pct()))
    print()
    print("RAM Status")
    print(' System RAM used : {} MB'.format(int(get_ram_usage() / 1024 / 1024)))
    print('﬙ Total available RAM : {} MB'.format(int(get_ram_total() / 1024 / 1024)))
    print(' RAM usage : {}%'.format(get_ram_usage_pct()))
    print()
    print("SWAP Status")
    print(' SWAP used : {} MB'.format(int(get_swap_usage() / 1024 / 1024)))
    print(' Total available SWAP : {} MB'.format(int(get_swap_total() / 1024 / 1024)))
    print(' Swap usage : {}%'.format(get_swap_usage_pct()))

#CPU
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

#RAM
def get_ram_usage():
    """
    Obtains the absolute number of RAM bytes currently in use by the system.
    :returns: System RAM usage in bytes.
    :rtype: int
    """
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)

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

#SWAP
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


if __name__ == "__main__":
    main()
