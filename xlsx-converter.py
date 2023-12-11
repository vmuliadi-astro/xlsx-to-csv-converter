#!/usr/bin/python3
import pandas as pd
from sys import argv, exit

try:
  excel_file = pd.read_excel(argv[1], None)
  for sheet_name in excel_file.keys():
    blacklisted_keywords = ["DONE", "NEED FIX"]
    if all(keyword not in sheet_name for keyword in blacklisted_keywords):
      excel_sheet = pd.read_excel(argv[1], sheet_name)
      sheet_name = sheet_name.split()[-1]
      print("{}.csv contains {:d} data".format(sheet_name, len(excel_sheet.index.tolist())))
      with open("{}.csv".format(sheet_name), "w") as csv_file:
        csv_file.write(excel_sheet.to_csv())
except Exception as err:
  print(err)
  exit(1)
