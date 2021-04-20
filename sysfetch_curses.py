#!/usr/bin/python3
import curses
import time
import os
import sysfetch_functions

#OUTPUT
col=1
def output(stdscr):
    while True:

        row=0

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

        stdscr.addstr(row,col,"CPU Status")
        if os.path.exists("/sys/class/thermal/thermal_zone0"):
            stdscr.addstr(row+1,col,cpu_temp)
        else :
            row=row-1
        stdscr.addstr(row+2,col,cpu_freqz)

        stdscr.addstr(row+3,col,cpu_useage_pct)

        stdscr.addstr(row+4,col,"")

        stdscr.addstr(row+5,col,"RAM Status")
        stdscr.addstr(row+6,col,ram_used)
        stdscr.addstr(row+7,col,ram_total)
        stdscr.addstr(row+8,col,ram_useage_pct)


        stdscr.addstr(row+9,col,"")

        stdscr.addstr(row+10,col,"SWAP Status")
        stdscr.addstr(row+11,col,swap_used)
        stdscr.addstr(row+12,col,swap_total)
        stdscr.addstr(row+13,col,swap_useage_pct)
        
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


