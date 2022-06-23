import csv 
# field names 
fields = ['Ngay', 'Nhan vien', 'Trang thai den', 'Thoi gian den', 'Trang thai di', 'Thoi gian di'] 
filename = "log.csv"
def update_file(staff):
    csv_writer = csv.writer(open(filename, 'a'))
    csv_writer.writerow(staff)
staff = [['manh', 'bkhn'], ['atrung', 'maj'], ['manh', 'bkhn'], ['atrung', 'maj'], ['manh', 'bkhn'], ['atrung', 'maj']]

