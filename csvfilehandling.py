import csv
import os
path = r"C:\Users\DELL\PycharmProjects\python_vidyamaam_notes\files\csv_files"
os.chdir(path)
# with open("sample.csv") as file:
#     reader_obj = csv.reader(file)
#     for data in reader_obj:
#         print(data)
#
# with open("sample.csv") as file:
#     reader1 = csv.DictReader(file)
#     for datas in reader1:
#         print(datas)
##############################################################################################################
# to write data into csv file
# with open("sample.csv","w") as file:
#     write_obj = csv.writer(file)
#
#     write single row
    # write_obj.writerow((["emp",'emp_no']))
    # write_obj.writerow(["abd",123])
    # writing multiple rows
    # write_obj.writerows(["dsg",234],['qwert',7689])
    ########################################################################################################
# fieldname = ['emp','emp_id']
# with open("sample.csv","w") as file:
#     write_obj =csv.DictWriter(file,['emp','emp_id'])
#     write_obj.writeheader()
    #single row
    # write_obj.writerow({"emp":"abc"  ,"emp_id": 234})
    #multiple rows
    # write_obj.writerows([{"emp":"abc"  ,"emp_id": 234},{"emp":"ytu"  ,"emp_id": 898}])
######################################################################################################3
