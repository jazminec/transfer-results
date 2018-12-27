import re
import xlsxwriter

# open input file
f = open("p4_collatz.869631", "r")
content = f.read()

# extract runtimes from input file (in the format #.###)
match = re.findall("[0-9][.][0-9]{3}", content)

# create excel file
workbook = xlsxwriter.Workbook("results_collatz.xlsx")
worksheet = workbook.add_worksheet()

# set titles for each column
worksheet.write(0, 1, "None")
worksheet.write(0, 2, "schedule(static, 1)")
worksheet.write(0, 3, "schedule(static, 100)")
worksheet.write(0, 4, "schedule(dynamic, 1)")
worksheet.write(0, 5, "schedule(dynamic, 100)")
worksheet.write(0, 6, "schedule(guided, 1)")
worksheet.write(0, 7, "schedule(guided, 100")

# initialize cell variables
row = 1
col = 1
threads = 1

# this column lists the number of threads
for i in range(19):
    worksheet.write(i+1, 0, i+1)

# write runtimes to cells
for item in match:
    worksheet.write(row, col, item)
    row += 1
    threads = (threads + 1) % 20
    if threads == 0:
        row = 1
        col += 1
        threads += 1

workbook.close()
f.close()
