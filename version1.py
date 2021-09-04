# => System Information Dsiplayer
# => Python Tool
# => importing required python modules
import psutil
import platform
import os
import sys
import time
from os import system
from datetime import datetime


# => setting window title 
system("title " + "InfoSIMP")


# => banner function 
# => prints simple banner made for this program
def banner():
    time.sleep(3)
    
    print('\n')
    print("""
          __      ___________  __ ____  
(_)_ __  / _| ___/ ___|_ _|  \/  |  _ \ 
| | '_ \| |_ / _ \___ \| || |\/| | |_) |
| | | | |  _| (_) |__) | || |  | |  __/ 
|_|_| |_|_|  \___/____/___|_|  |_|_|    
                            Version 1.0
                                    by naqviO7
""")          
    print('\n')
    
    time.sleep(3)
 
    
# => table of contents
# => menu of program/tool
def menu():
    print("="*40, "M E N U", "="*40)
    print("-> Press 1 for System Information!")
    print("-> Press 2 for CPU Information!")
    print("-> Press 3 for Memory Usage Information!")
    print("-> Press 4 for Disk Usage Information!")
    print("-> Press 5 for Network Information!")
  
    
# => function that converts large number of bytes into a scaled format (e.g in kilo, mega, giga, etc.)    
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return (f"{bytes:.2f}{unit}{suffix}")
        bytes /= factor
 
  
# => using platform module displaying system details    
def system_information():
    print("="*40, "System Information", "="*40)
    uname = platform.uname()
    print(f"-> System: {uname.system}")
    print(f"-> Node Name: {uname.node}")
    print(f"-> Release: {uname.release}")
    print(f"-> Version: {uname.version}")
    print(f"-> Machine: {uname.machine}")
    print(f"-> Processor: {uname.processor}")    
 
    
# => displaying number of cores and usage of CPU
def cpu_information():
    print("="*40, "CPU Information", "="*40)
    
    # => number of cores
    print("-> Physical cores:", psutil.cpu_count(logical=False))
    print("-> Total cores:", psutil.cpu_count(logical=True))
    
    # => CPU frequencies
    cpufreq = psutil.cpu_freq()
    print(f"-> Max Frequency: {cpufreq.max:.2f} Mhz")
    print(f"-> Min Frequency: {cpufreq.min:.2f} Mhz")
    print(f"-> Current Frequency: {cpufreq.current:.2f} Mhz")
    
    # => CPU usage
    print("-> CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"-> Core {i}: {percentage} %")
    print(f"-> Total CPU Usage: {psutil.cpu_percent()} %")


# => displaying memory usages
def memory_information():
    print("="*40, "Memory Information", "="*40)
    
    # => get the memory details
    svmem = psutil.virtual_memory()
    print(f"-> Total: {get_size(svmem.total)}")
    print(f"-> Available: {get_size(svmem.available)}")
    print(f"-> Used: {get_size(svmem.used)}")
    print(f"-> Percentage: {svmem.percent}%")
    print("="*20, "SWAP", "="*20)
    
    # => get the swap memory details (if exists)
    swap = psutil.swap_memory()
    print(f"-> Total: {get_size(swap.total)}")
    print(f"-> Free: {get_size(swap.free)}")
    print(f"-> Used: {get_size(swap.used)}")
    print(f"-> Percentage: {swap.percent}%")
      

      
def disk_information():
    print("="*40, "Disk Information", "="*40)
    print("Partitions and Usage:")
    
    # => get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f" === Device: {partition.device} ===")
        print(f" -> Mountpoint: {partition.mountpoint}")
        print(f" -> File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # => this can be catched due to the disk that
            continue
        
        print(f" -> Total Size: {get_size(partition_usage.total)}")
        print(f" -> Used: {get_size(partition_usage.used)}")
        print(f" -> Free: {get_size(partition_usage.free)}")
        print(f" -> Percentage: {partition_usage.percent}%")
    
    # => get IO statistics
    disk_io = psutil.disk_io_counters()
    print(f"-> Total read: {get_size(disk_io.read_bytes)}")
    print(f"-> Total write: {get_size(disk_io.write_bytes)}")  


def network_information():
    print("="*40, "Network Information", "="*40)
    
    # => get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f" -> IP Address: {address.address}")
                print(f" -> Netmask: {address.netmask}")
                print(f" -> Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f" -> MAC Address: {address.address}")
                print(f" -> Netmask: {address.netmask}")
                print(f" -> Broadcast MAC: {address.broadcast}")
    
    # => get IO statistics 
    net_io = psutil.net_io_counters()
    print(f"-> Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"-> Total Bytes Received: {get_size(net_io.bytes_recv)}")


# => main body of code
# => execution of code starts from here
# => all functions are called inthis part of code    
def main_function():
    # => clearing screen of previous output in windows
    os.system('cls')
    
    # clearing screen of previous output in linux
    os.system('clear')
    
    # => displaying banner
    banner()
    
    time.sleep(2)
    
    print("="*40, "W E L C O M E", "="*40)
    print("Options to USE:\n -> Press 1 to Default Run.\n -> Press 2 to Custom Run\n -> Press 0 to Quit")
    
    key=int(input('Enter Key to Run: '))
    if key==0:
        print('\nQuitting... InfoSimp\n')
        
        time.sleep(1)
        sys.exit()
            
    elif key==1:
        print("\nRunning Infosimp in Default Mode!\n")
        time.sleep(1.5)
        system_information()
        
        time.sleep(1.5)
        cpu_information()
        
        time.sleep(1.5)
        memory_information()
        
        time.sleep(1.5)
        disk_information()
        
        time.sleep(1.5)
        network_information()
        
        print("\n")
        print("="*30, "E X I T I N G", "="*30)
        print("\n")
        
            
    elif key==2:
        print("\nRunning Infosimp in Custom Mode!\n")
        menu()
        num=int(input("Enter Operation to Perform: "))
        if num==1:
            time.sleep(1.5)
            system_information()
            
            print("\n")
            print("="*30, "E X I T I N G", "="*30)
            print("\n")
        
        elif num==2:
            time.sleep(1.5)
            cpu_information()
            print("\n")
            print("="*30, "E X I T I N G", "="*30)
            print("\n")

        elif num==3:
            time.sleep(1.5)
            memory_information()

            print("\n")
            print("="*30, "E X I T I N G", "="*30)
            print("\n")
                    
        elif num==4:
            time.sleep(1.5)
            disk_information()
        
            print("\n")
            print("="*30, "E X I T I N G", "="*30)
            print("\n")
            
        elif num==5:
            time.sleep(1.5)
            network_information()

            print("\n")
            print("="*30, "E X I T I N G", "="*30)
            print("\n")
        
        else:
            print("-> Invalid Option!")
            print("\n")
            print("="*30, "E X I T I N G", "="*30)
            print("\n")
    
    else:
        print("-> Invalid Option!")
        print("\n")
        print("="*30, "E X I T I N G", "="*30)
        print("\n")    
 
  
#manaing importing for other files  
if __name__ == "__main__":        
    
    # => Calling main function
    main_function()
    
    time.sleep(1)
    input()
    

# => END OF CODE
