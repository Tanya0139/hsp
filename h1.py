import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='tanya',database='project')
if conn.is_connected():
      print('successfully connected')
c1=conn.cursor()
c1.execute('create table patient._details(p_namevarchar(25) primary key,p_a.ge int(3),p_problems varchar(40),p_pho.no int(15))')
print('table created')
c1.execute('create table doctor._details(d_name varchar(25) primary key,d_age int(3),d_department varchar(40),d_phono int(15))')
print('table created')  
c1.execute('create table worker._details(w_name varchar(25) primary key,w_age int(3),w_workname varchar(40),w_phono int(15))')
print('table created')           
c1.commit()
