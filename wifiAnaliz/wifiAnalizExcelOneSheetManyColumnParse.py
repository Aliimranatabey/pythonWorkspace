from openpyxl.styles import Font
from openpyxl import Workbook

#read_log_file methodu içerisinde "file_path" parametresi alır. Aldığı log dosyasını okur ve lines adında bir listeeye atar.
#Ardından lines içerisindeki her bir satırı içerisindeki boşlukları yok ederek dönderir .
def read_log_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

#create_master_excel methodu içerisinde "log_data","output_file" adında iki girdi alır . Bir workbook nesnesi oluşturur .
#Excel dosyasını açar verileri yazar ve kapatır .
def create_master_excel(log_data, output_file):
    workbook = Workbook()
    total_sheet = workbook.create_sheet("All Sheets")
    # total_sheet.append(["Time", "State","Signal","Receive Rate","Transmit Rate","Channel","Protocol"])
    
    for line in log_data[1:]:
        parts = line.split("|")
        if len(parts) >= 2:
            time = parts[0].strip()
            values = parts[1].strip().split(", ")
            
            if "connected" in values[1]:
                state = "connected"
                value = 1
            elif "disconnected" in values[1]:
                state = "disconnected"
                value = 0
            else:
                state = "different"
                value = 2

            state_status=value
            signal_status = values[2].split("%")[0].strip()
            for i in range(1,101):
                if signal_status==f"{i}":
                    signal_status=i
            receive_rate_status = values[3].strip()
            for i in range(1,1001):
                if receive_rate_status==f"{i}":
                    receive_rate_status=i
            transmit_rate_status = values[4].strip()
            for i in range(1,1001):
                if transmit_rate_status==f"{i}":
                    transmit_rate_status=i
            channel_status = values[5].strip()
            for i in range(1,25):
                if channel_status==f"{i}":
                    channel_status=i
            protocol = values[6].strip()
            if protocol == "802.11ax":
                value = 5
            elif protocol == "802.11ac":
                value = 4
            elif protocol == "802.11n":
                value = 3
            elif protocol == "802.11g":
                value = 2
            elif protocol == "802.11b":
                value = 1
            else:
                value = 0
            protocol_status=value
            total_sheet.append([time.replace('-----',''), values[1],state_status, signal_status,receive_rate_status,transmit_rate_status,channel_status,values[6],protocol_status])
    total_sheet.column_dimensions['A'].width = 27
    total_sheet.column_dimensions['B'].width = 10
    total_sheet.column_dimensions['C'].width = 11
    total_sheet.column_dimensions['D'].width = 11
    total_sheet.column_dimensions['E'].width = 12
    total_sheet.column_dimensions['F'].width = 12
    total_sheet.column_dimensions['G'].width = 10
    total_sheet.column_dimensions['H'].width = 10
    total_sheet.column_dimensions['I'].width = 13
    bold_font = Font(bold=True)
    total_sheet['C1']="State Value"    
    total_sheet['I1']="Protocol Value"
    total_sheet['A1'].font = bold_font
    total_sheet['B1'].font = bold_font
    total_sheet['C1'].font = bold_font
    total_sheet['D1'].font = bold_font
    total_sheet['E1'].font = bold_font
    total_sheet['F1'].font = bold_font
    total_sheet['G1'].font = bold_font
    total_sheet['H1'].font = bold_font
    total_sheet['I1'].font = bold_font
    
    
    workbook.remove(workbook.active)
    workbook.save(output_file)

log_data = read_log_file('wifiAnaliz_arcadyan_wifi6vdsl_20230815_54000sn_log.txt')

create_master_excel(log_data, "onesheet_master_sheet.xlsx")
