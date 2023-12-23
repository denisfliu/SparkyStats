#!/usr/bin/env python
import xlrd
from src.sqbs import Matches

if __name__ == "__main__":
    # C:\\Users\\denis\\code\\python\\QBStats\\stats.xlsx
    print("Input File Location: ")
    path = input()
    wb = xlrd.open_workbook(path)
    obj = Matches(wb)
    with open("sqbs.sqbs", "w") as writer:
        sqbs = obj.create_sqbs_string()
        writer.write(sqbs)
