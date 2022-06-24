import csv

from sklearn.datasets import load_files 
# field names 
fields = ['Ngay', 'Nhan vien', 'Trang thai den', 'Thoi gian den', 'Trang thai di', 'Thoi gian di'] 
filename = "log.csv"
load_first = False
def update_file(staff):
    global load_first
    csv_writer = csv.writer(open(filename, 'a'))
    if load_first == False:
        load_first = True
        csv_writer.writerow(fields)
    csv_writer.writerow(staff)
# staff = [['manh', 'bkhn'], ['atrung', 'maj'], ['manh', 'bkhn'], ['atrung', 'maj'], ['manh', 'bkhn'], ['atrung', 'maj']]

