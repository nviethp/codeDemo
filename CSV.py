import csv 
# with open(r'F:\FPT_COOKING\Python\csv_demo.csv','rt')as f: # r no chuyen doi chuoi thuong thành chuoi tho de su dung
#   data = csv.reader(f)
#   for row in data:
#         print(row)


with open(r'F:\FPT_COOKING\Python\csv_demo.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|') #delimiter là bỏ khoảng trắng,quotechar bỏ dấu ngoặc
    for row in spamreader:
       print(', '.join(row))
# with open(r'C:\Users\nviet\csv_demo.csv', newline='') as csv_file:      
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Tên các cột là: {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} làm việc trong {row[1]}, và được sinh ra tháng {row[2]}.')
#             line_count += 1
#     print(f'Đã đọc {line_count} lines.')

# with open('.\csv_demo.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})