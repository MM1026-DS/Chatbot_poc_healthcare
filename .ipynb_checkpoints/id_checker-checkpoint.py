import sqlite3
conn = sqlite3.connect("sql1.db")
cur = conn.cursor()

pat_id = cur.execute("SELECT Patient_id FROM Patient")


class pat_id_lst:
    def id_checker_lst(pat_id):
        pat_id_lst = []
        for i in pat_id:
            for j in range(len(i)):
                pat_id_lst.append(i[j])
                
        return pat_id_lst


class pat_id_checker:
    def id_checker(query):
        name  = None
        pat_id = cur.execute("SELECT Patient_id FROM Patient")
        lst = pat_id_lst.id_checker_lst(pat_id)
        for i in lst:
            if i==query:
                if i==1:
                    name = "Aditya Sonkar"
                elif i==2:
                    name = "Harsh Mishra"
                elif i==3:
                    name = "Yuvraj Sinha"
                elif i==4:
                    name ="Amit"
                elif i==5:
                    name  = "Garima"
            
            else:
                print("Please Provide the Right Id")
                break
        return name        
        
        
