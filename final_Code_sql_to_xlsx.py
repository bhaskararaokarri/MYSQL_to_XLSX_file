########### reading the data from xl files

import pandas as pd
from sqlalchemy import create_engine
import pymysql

# # Create dataframe
# TestBed_129288_R62020180.xlsx
# file =(r"E:pranay/practice1.xlsx")
# file =(r"E:pranay/test_case_code/test_base.xlsx")
file =(r"E:pranay/test_case_code/modify_data.xlsx")

xl = pd.ExcelFile(file)
for s_name in xl.sheet_names:
    dff = pd.read_excel(file,sheet_name = s_name)
#     print(s_name)
#     print(df)
# # Create SQLAlchemy engine to connect to MySQL Database
    engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                    .format(host="localhost", db="Testdata", user="root", pw="Bhaskar@1296"))
    # Convert dataframe to sql table                                   
    dff.to_sql('bhaskar'+'_'+s_name,engine,index=False)
	
	
########### reading the data from xl files up to here


########### reading the data from mysql data base and stored in csv files

import mysql.connector as sql
import pandas as pd
db_name='db1'
 
db_connection = sql.connect(host='localhost', database=db_name, user='root', password='Bhaskar@1296')
db_cursor = db_connection.cursor()
# based on no tables this one will iterate
db_cursor.execute("show tables")
All_Tables = db_cursor.fetchall()
print(All_Tables)

writer = pd.ExcelWriter('E:/pranay/test_case_code/'+ db_name +'.xlsx', engine='xlsxwriter')

for i,j in enumerate(All_Tables):
    print()
    db_cursor.execute('SELECT * FROM {}'.format(j[0]))

    var_1  = db_cursor.description
    # print(var_1)
    # print(type(var_1))
    list_1 = []
    for k in var_1:
        list_1.append(k[0])
        
    table_rows = db_cursor.fetchall()
    # print(table_rows)
    
    # df = pd.DataFrame(list_1)
    # print(df)
    data_frame = pd.DataFrame(table_rows,columns=list_1)
    data_frame.to_excel(writer, sheet_name='{}'.format(j[0]))
    print('{}'.format(j[0]))
    print(data_frame)

writer.save()