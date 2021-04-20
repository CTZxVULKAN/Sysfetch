#!/usr/bin/python3
import curses
import time
import os
import sysfetch_functions

#OUTPUT

def output(stdscr):
    while True:

        """
        fetch all the data required using the functions in sysfetch_functions.py 
        convert the fetched values to strings and display them 
        apply an infinite loop to keep fetching and refreshing the values every 1 sec.
        """

        cpu_freqz = ' CPU frequency : {} MHz'.format(sysfetch_functions.get_cpu_frequency())
        cpu_useage_pct = ' CPU usage : {}%'.format(sysfetch_functions.get_cpu_usage_pct())
        cpu_temp = ' CPU temperature : {}°C'.format(sysfetch_functions.get_cpu_temp())

        ram_used = ' System RAM used : {} MB'.format(int(sysfetch_functions.get_ram_usage() / 1024 / 1024))
        ram_total = ' Total available RAM : {} MB'.format(int(sysfetch_functions.get_ram_total() / 1024 / 1024))
        ram_useage_pct=' RAM usage : {}%'.format(sysfetch_functions.get_ram_usage_pct())

        swap_used = ' SWAP used : {} MB'.format(int(sysfetch_functions.get_swap_usage() / 1024 / 1024))
        swap_total = ' Total available SWAP : {} MB'.format(int(sysfetch_functions.get_swap_total() / 1024 / 1024))
        swap_useage_pct = ' Swap usage : {}%'.format(sysfetch_functions.get_swap_usage_pct())

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
        
        #Window Decorations
        
        #Do not use any color scheme ,follow the default color scheme
        curses.use_default_colors()
        #We do not need to show the cursor when the program is running
        curses.curs_set(0) 

        stdscr.refresh()
        time.sleep(1)



def main():
    curses.wrapper(output)

if __name__ == "__main__":
    main()


