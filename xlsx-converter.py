#!/usr/bin/python3
import pandas as pd
from sys import argv, exit

try:
  total_data=0
  excel_file = pd.read_excel(argv[1], None)
  for sheet_name in excel_file.keys():
    blacklisted_keywords = ["DONE", "NEED FIX"]
    blacklisted_worksheet = ["fix", "DATA", "2"]
    if (all(keyword not in sheet_name for keyword in blacklisted_keywords)) and (all(keyword not in sheet_name for keyword in blacklisted_worksheet)):
      excel_sheet = pd.read_excel(argv[1], sheet_name)
      sheet_name = sheet_name.split()[-1]
      total_data = total_data + len(excel_sheet.index.tolist())
      print("{}.csv contains {:d} data".format(sheet_name, len(excel_sheet.index.tolist())))
      excel_sheet.to_csv("{}.csv".format(sheet_name), index=False)

  data_counting = "Total data in this XLSX: {:d} data".format(total_data)

  print()
  print("= " + "=" * len(data_counting) + " =")
  print("= " + data_counting + " =")
  print("= " + "=" * len(data_counting) + " =")
  print()
except Exception as err:
  print(err)
  exit(1)
