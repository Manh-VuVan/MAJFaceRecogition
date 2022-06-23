import xlsxwriter
import time
day_id = 0
name_before, day_before = "", "19:06:2022"
workbook = xlsxwriter.Workbook("log.xlsx")
def createlogfile(workbook, staff):
    # setup this file
    global day_id, name_before, day_before
    worksheet = workbook.add_worksheet('Chamcong1')
    # workbook = xlsxwriter.Workbook("log.xlsx")
    # worksheet = workbook.add_worksheet('Chamcong')
    worksheet.write('A1', "STT")
    worksheet.write('B1', "Ngay")
    worksheet.write('C1', "Nhan vien")
    worksheet.merge_range('D1:G1', 'Tinh trang')
    worksheet.merge_range('D2:E2', 'Den')
    worksheet.merge_range('F2:G2', 'Di')
    worksheet.write('D3', "Trang thai")
    worksheet.write('E3', "Thoi gian")
    worksheet.write('F3', "Trang thai")
    worksheet.write('G3', "Thoi gian")
        
    for i in range(0, len(staff)):
        # if staff[i][1] != day_before:
        day_id = day_id + 1
        worksheet.write('A'+str(day_id + 3), day_id)
        worksheet.write('B'+str(day_id + 3), staff[i][1])
        worksheet.write('C'+str(day_id + 3), staff[i][0])
        worksheet.write('D'+str(day_id + 3), staff[i][2])
        worksheet.write('E'+str(day_id + 3), staff[i][3])
        worksheet.write('F'+str(day_id + 3), staff[i][4])
        worksheet.write('G'+str(day_id + 3), staff[i][5])
    day_before = staff[1]
staff = [['loan', '2022-06-22', 'Som', '6:26:59.480016', 'Muon', ' 2:33:00.337762'], ['manh', '2022-06-22', 'Som', '6:27:21.724556', 'Muon', ' 2:32:37.162758'], ['loan', '2022-06-23', 'Som', '6:26:59.480016', 'Muon', ' 2:33:00.337762'], ['manh', '2022-06-23', 'Som', '6:26:59.480016', 'Muon', ' 2:33:00.337762']]
createlogfile(workbook, staff)
time.sleep(1)
staff = []
staff = [['loan', '2022-06-22', 'Som', '6:26:59.480016', 'Muon', ' 2:33:00.337762'], ['manh', '2022-06-22', 'Som', '6:27:21.724556', 'Muon', ' 2:32:37.162758'], ['loan', '2022-06-23', 'Som', '6:26:59.480016', 'Muon', ' 2:33:00.337762'], ['manh', '2022-06-23', 'Som', '6:26:59.480016', 'Muon', ' 2:33:00.337762']]
createlogfile(workbook, staff)
# time.sleep(20)
workbook.close()
print("Done1")
workbook1 = xlsxwriter.Workbook("log.xlsx")
# worksheet = workbook1.add_worksheet('Chamcong')
staff = [['loan', '2022-06-22', 'Som', '6:26:59.480016', 'Muon', ' 2:33:00.337762'], ['manh', '2022-06-22', 'Som', '6:27:21.724556', 'Muon', ' 2:32:37.162758'], ['loan', '2022-06-23', 'Som', '6:26:59.480016', 'Muon', ' 2:33:00.337762'], ['manh', '2022-06-23', 'Som', '6:26:59.480016', 'Muon', ' 2:33:00.337762']]
createlogfile(workbook1,staff)
workbook1.close()
print("Done")


