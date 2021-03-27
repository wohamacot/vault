import argparse
from openpyxl import Workbook, load_workbook
from datetime import datetime, date, time
from pathlib import Path
from sys import exit

parser = argparse.ArgumentParser()
parser.add_argument("command", help="command for mngr trk")
parser.add_argument("name", help="name of work for tracking")

args = parser.parse_args()

workbook_name = 'table_trk.xlsx'
current_mounth = datetime.date(datetime.now()).strftime("%b")
def create_workbook():
    headers = ['name', 'start_time', 'stop_time', 'total_time']
    wb = Workbook()
    page = wb.active

    page.title = current_mounth 
    page.append(headers)
    wb.save(workbook_name)


def start():    
    start_time = datetime.now().strftime("%H:%M:%S")
    new_data = [[args.name, start_time]]
        
    try:
        
        wb_load = load_workbook(workbook_name)
        source = wb_load[current_mounth]
        values = {} # dict key - values from name; vals - values from start_time 
        for i in range(1,len(source['A'])):
            values[source['A'][i].value] = source['B'][i].value
        
        print(values)
        page = wb_load.active
        exit()
        for d in new_data:
            page.append(d)
        wb_load.save(workbook_name)
    
    except FileNotFoundError:
        print("File not found =( try create_book command")

if args.command == "create_book":
    create_workbook()
if args.command == "start":
    start()
if args.command == "stop":
    print("stop time")


