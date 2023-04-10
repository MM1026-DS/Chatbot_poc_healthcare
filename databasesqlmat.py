import sqlite3
conn = sqlite3.connect("sql1.db")
cur = conn.cursor()
import reverse_geocoder as rf



class respond:
    def sql_answer(input_query):
        input_query = input_query.lower()
        conn = sqlite3.connect("sql1.db")
        cur = conn.cursor()
        if(input_query == "who are the best doctors for heart disease"):
            mycur = cur.execute("SELECT Doctor_Name FROM DOCTOR WHERE Speciality = 'Cardiologist' ")
            for i in mycur:
                print("{} is best doctor for heart disease".format(i[0]))
        elif(input_query == "who are the best doctors for cardiovascular disease"):
            mycur = cur.execute("SELECT Doctor_Name FROM DOCTOR WHERE Speciality = 'Cardiologist' ")
            for i in mycur:
                print("{} is the best doctor for cardiovasular disease".format(i[0]))
        elif(input_query == "who are the best doctors for skin"):
            mycur = cur.execute("SELECT Doctor_Name FROM DOCTOR WHERE Speciality = 'Dermatologist' ")
            for i in mycur:
                print("{} is the best doctor for skin".format(i[0]))
        elif(input_query == "best doctors for dermatology"):
            mycur = cur.execute("SELECT Doctor_Name FROM DOCTOR WHERE Speciality = 'Dermatologist' ")
            for i in mycur:
                print("{} is the best doctor for Dermatology".format(i[0]))
        elif(input_query == "best physician"):
            mycur = cur.execute("SELECT Doctor_Name FROM DOCTOR WHERE Speciality = 'Physician' ")
            for i in mycur:
                print("{} is the best Physician".format(i[0]))
        elif(input_query == "what is the clinic location of doctor mayank"):
            position = reversegeocoding.reversegeocoding_loc(input_query)
            print("Clinic location of Doctor Mayank is {}".format(position))
            
        elif(input_query == "what is the clinic location of doctor piyush"):
            position = reversegeocoding.reversegeocoding_loc(input_query)
            print("Clinic location of Doctor Piyush is {}".format(position))
            
        elif(input_query == "what is the clinic location of doctor soumya"):
            position = reversegeocoding.reversegeocoding_loc(input_query)
            print("Clinic location of Doctor Soumya is {}".format(position))   
            
        elif(input_query == "what is the clinic location of doctor deepshikha"):
            position = reversegeocoding.reversegeocoding_loc(input_query)
            print("Clinic location of Doctor Deepshikha is {}".format(position))   
            
            
        elif(input_query == "best doctor near my location for cardiology"):
            mycur = cur.execute("SELECT Doctor_Name FROM DOCTOR WHERE Speciality = 'Cardiologist' ")
            for i in mycur:
                print("Best Doctor for Cardiology is {}".format(i[0]))    
    
        elif(input_query == "Please provide the name of the doctors which have fees less than 500 rupees"):
            mycur = cur.execute("SELECT Doctor_Name FROM DOCTOR WHERE Fees <=500 ")
            for i in mycur:
                print("Doctor with fees less than aur equal to 500 is/are {}".format(i[0]))   
            
        elif(input_query == "what is timing for doctor soumya"):
            print("currently we are unavaiable to provide time schedule")
            
        elif(input_query == "which is the best dental clinic"):
            print("currently we have no data for dental clinic")
            
        elif(input_query == "what is the fees of doctor rishabh"):
            mycur = cur.execute("SELECT Fees FROM DOCTOR WHERE Doctor_Name = 'Rishabh Yadav'")
            for i in mycur:
                print("consultation charge of the Doctor Rishabh is {}".format(i[0]))    
        
        elif(input_query == "doctor with fees more than 1000 rupees"):
            mycur = cur.execute("SELECT Doctor_Name FROM DOCTOR WHERE Fees >= 1000")
            for i in mycur:
                for j in range(len(i)):
                    print("Doctor with consultation charges more than 1000 rupees is {}".format(i[j]))
    
        elif(input_query == "what is the speciliatity of doctor piyush"):
            mycur = cur.execute("SELECT Speciality FROM DOCTOR WHERE Doctor_Name = 'Piyush Singh' ")
            for i in mycur:
                print("Specilization of Doctor Piyush is {}".fomat(i[0]))
                
        elif(input_query =="what is the rating of doctor piyush singh"):
            mycur = cur.execute("SELECT Rating FROM DOCTOR WHERE Doctor_Name = 'Piyush Singh' ")
            for i in mycur:
                print("Rating of Doctor Piyush is {}".format(i[0]))        
                
                
        elif(input_query == "what is the speciliatity of doctor mayank"):
            mycur = cur.execute("SELECT Speciality FROM DOCTOR WHERE Doctor_Name = 'Mayank Mishra' ")
            for i in mycur:
                print("Specilization of Doctor Mayank is {}".format(i[0]))
                
        elif(input_query == "what is the rating of doctor mayank mishra"):
            mycur = cur.execute("SELECT Rating FROM DOCTOR WHERE Doctor_Name = 'Mayank Mishra' ")
            for i in mycur:
                print("Rating of Doctor Mayank is {}".format(i[0]))        
                
                
        elif(input_query == "what is the speciliatity of doctor soumya"):
            mycur = cur.execute("SELECT Speciality FROM DOCTOR WHERE Doctor_Name = 'Soumya' ")
            for i in mycur:
                print("Specilization of Doctor Soumya is {}".format(i[0]))
                
        elif(input_query == "what is the rating of doctor soumya"):
            mycur = cur.execute("SELECT Rating FROM DOCTOR WHERE Doctor_Name = 'Soumya' ")
            for i in mycur:
                print("Rating of Doctor Soumya is {}".format(i[0]))        
                
                
        elif(input_query == "what is the speciliatity of doctor rishabh"):
            mycur = cur.execute("SELECT Speciality FROM DOCTOR WHERE Doctor_Name = 'Rishabh Yadav' ")
            for i in mycur:
                print("Specilization of Doctor Rishabh is {}" .format(i[0]))
                
        elif(input_query == "what is the rating of doctor rishabh yadav"):
            mycur = cur.execute("SELECT Rating FROM DOCTOR WHERE Doctor_Name = 'Rishabh Yadav'")
            for i in mycur:
                print("Rating of Doctor Rishabh is {}" .format(i[0]))        
                
                
        elif(input_query == "what is the speciliatity of doctor deepshikha"):
            mycur = cur.execute("SELECT Speciality FROM DOCTOR WHERE Doctor_Name = 'Deepshikha Mishra' ")
            for i in mycur:
                print("Specilization of Doctor Deepshikha is {}".format(i[0]))
                
        elif(input_query == "what is the rating of doctor deepshikha"):
            mycur = cur.execute("SELECT Rating FROM DOCTOR WHERE Doctor_Name = 'Deepshikha Mishra' ")
            for i in mycur:
                print("Rating of Doctor Deepshikha is {}".format(i[0]))        
                
                
        elif(input_query == "what is the fees of doctor piyush"):
            mycur = cur.execute("SELECT Fees FROM DOCTOR WHERE Doctor_Name = 'Piyush Singh' ")
            for i in mycur:
                print("consultation charges of Doctor Piyush is {}  Rupees".format(i[0]))         
                
                
        elif(input_query == "what is the fees of doctor mayank"):
            mycur = cur.execute("SELECT Fees FROM DOCTOR WHERE Doctor_Name = 'Mayank Mishra' ")
            for i in mycur:
                print("consultation charges of Doctor Mayank is {} Rupees" .format(i[0]))
                
                
        elif(input_query == "what is the fees of doctor soumya"):
            mycur = cur.execute("SELECT Fees FROM DOCTOR WHERE Doctor_Name = 'Soumya' ")
            for i in mycur:
                print("consultation charges of Doctor Soumya is {} Rupees".format(i[0]))  
                
                
        elif(input_query == "what is the fees of doctor deepshikha"):
            mycur = cur.execute("SELECT Fees FROM DOCTOR WHERE Doctor_Name = 'Deepshikha Mishra' ")
            for i in mycur:
                print("consultation charges of Doctor Deepshikha is {} Rupees".format(i[0]))
                
                
        elif(input_query == "who is the doctor of patient aditya"):
            mycur = cur.execute("SELECT Doctor_Name FROM Doctor WHERE Pat_id=(SELECT Patient_id FROM Patient WHERE Patient_Name = 'Aditya Sonkar')")
            for i in mycur:
                print("{} is the Doctor of patient Aditya".format(i[0]))
                
                
        elif(input_query == "who is the doctor of patient harsh"):
            mycur = cur.execute("SELECT Doctor_Name FROM Doctor WHERE Pat_id=(SELECT Patient_id FROM Patient WHERE Patient_Name = 'Harsh Mishra')")
            for i in mycur:
                print("{} is the Doctor of patient Harsh".format(i[0]))
                
                
        elif(input_query == "who is the doctor of patient yuvraj"):
            mycur = cur.execute("SELECT Doctor_Name FROM Doctor WHERE Pat_id=(SELECT Patient_id FROM Patient WHERE Patient_Name = 'Yuvraj Sinha')")
            for i in mycur:
                print("{} is the Doctor of patient Yuvraj".format(i[0]))
                
                
        elif(input_query == "who is the doctor of patient amit"):
            mycur = cur.execute("SELECT Doctor_Name FROM Doctor WHERE Pat_id=(SELECT Patient_id FROM Patient WHERE Patient_Name = 'Amit')")
            for i in mycur:
                print("{} is the Doctor of patient Amit".format(i[0]))
                
        elif(input_query == "who is the doctor of patient garima"):
            mycur = cur.execute("SELECT Doctor_Name FROM Doctor WHERE Pat_id=(SELECT Patient_id FROM Patient WHERE Patient_Name = 'Garima')")
            for i in mycur:
                print("{} is the Doctor of patient garima".format(i[0]))
                
                
        elif(input_query == "what is the minium age of the patient of doctor mayank"):
            mycur = cur.execute("SELECT min(Age) FROM Patient WHERE Patient_id =(SELECT Pat_id from Doctor WHERE Doctor_Name='Mayank Mishra')")
            for i in mycur:
                print("Minimum age of the Patient under Doctor Mayank Is {} years".format(i[0]))
                
                
        elif(input_query == "what is the sickness reason of devashree gupta"):
            print("Data for Devashree is not available")
            
        elif(input_query == "what is the sickness reason for aditya sonkar"):
            mycur = cur.execute("SELECT Issue from Patient WHERE Patient_Name = 'Aditya Sonkar' ")    
            for i in mycur:
                print("{} is the Health issue with patient Aditya sonkar".format(i[0]))
                
                      
        elif(input_query == "what is the sickness reason for amit patel"):
            mycur = cur.execute("SELECT Issue from Patient WHERE Patient_Name = 'Amit' ")    
            for i in mycur:
                print("{} is the health issue with patient Amit".format(i[0]))      
                
                
        elif(input_query == "how many girls are sick from last year"):
            mycur = cur.execute("SELECT count(Gender) FROM Patient WHERE Gender = 'F' ")    
            for i in mycur:
                print("{} is the total count  for sick girls".format(i[0]))
                
        elif(input_query == "what is the maximum age of the patient"):
            mycur = cur.execute("SELECT max(Age) FROM Patient ")    
            for i in mycur:
                print(i[0])        
       
        elif(input_query == "what is the reason of sickness of alok patel"):
            print("Currently No Data Available for the Patient Name Alok")
            
        elif(input_query == "most sick patiet"):
            mycur = cur.execute("SELECT Patient_Name FROM patient GROUP BY(Issue) HAVING Age = max(Age) AND Issue = 'Heart Attack'  ")    
            for i in mycur:
                print(i[0])     
            
        elif(input_query == "what is the age and gender of minimun age patient"):
            mycur = cur.execute("SELECT min(Age),Gender FROM Patient")    
            for i in mycur:
                print(i)
                
                
        elif(input_query == "what is the reason of sickness of maximum age patient"):
            mycur = cur.execute("SELECT Issue FROM Patient WHERE Patient_Name = (SELECT Patient_Name FROM Patient GROUP By(Age) HAVING Age=(Select max(Age) FROM Patient))")    
            for i in mycur:
                print(i[0])        
            
        elif(input_query == "what is the health issue with aditya sonkar"):
            mycur = cur.execute("SELECT Issue FROM Patient WHERE Patient_Name = 'Aditya Sonkar' ")    
            for i in mycur:
                print("{} is the Health issue with  Aditya Sonkar".format(i[0]))
                
        elif(input_query == "health issue with patient id 1 patient aditya sonkar"):
            mycur = cur.execute("SELECT Issue FROM Patient Where Patient_id=1")
            for i in mycur:
                print("{} is the Health issue with  Aditya Sonkar".format(i[0]))
                
        
        elif(input_query == "disease name of patient aditya sonkar"):
            mycur = cur.execute("SELECT Issue FROM Patient WHERE Patient_Name = 'Aditya Sonkar' ")    
            for i in mycur:
                print("{} is the Health issue with  Aditya Sonkar".format(i[0]))
  
    
    
    
                
        elif(input_query == "what is the health issue with harsh"):
            mycur = cur.execute("SELECT Issue FROM Patient WHERE Patient_Name = 'Harsh Mishra' ")    
            for i in mycur:
                print("{} is the Health issue with  Patient Harsh Mishra".format(i[0]))
                
                
        elif(input_query == "health issue with patient id 2 patient harsh"):
            mycur = cur.execute("SELECT Issue FROM Patient Where Patient_id=2")
            for i in mycur:
                print("{} is the Health issue with  Patient Harsh Mishra".format(i[0]))
                
                
                
        elif(input_query == "disease name of patient harsh mishra"):
            mycur = cur.execute("SELECT Issue FROM Patient WHERE Patient_Name = 'Harsh Mishra' ")    
            for i in mycur:
                print("{} is the Health issue with  Patient Harsh Mishra".format(i[0]))        
                
                
                
        elif(input_query == "what is the health issue with yuvraj"):
            mycur = cur.execute("SELECT Issue FROM Patient WHERE Patient_Name = 'Yuvraj Sinha' ")    
            for i in mycur:
                print("{} is the Health issue with  Patient Yuvraj Sinha".format(i[0]))
                
                
        elif(input_query == "health issue with patient id 3 patient yuvraj"):
            mycur = cur.execute("SELECT Issue FROM Patient Where Patient_id=3")
            for i in mycur:
                print("{} is the Health issue with  Patient Yuvraj Sinha".format(i[0]))
                
                
                
        elif(input_query == "disease name of patient yuvraj sinha"):
            mycur = cur.execute("SELECT Issue FROM Patient WHERE Patient_Name = 'Yuvraj Sinha' ")    
            for i in mycur:
                print("{} is the Health issue with  Patient Yuvraj Sinha".format(i[0]))        
                
                
        elif(input_query == "what is the health issue with amit"):
            mycur = cur.execute("SELECT Issue FROM Patient WHERE Patient_Name = 'Amit' ")    
            for i in mycur:
                print("{} is the Health issue with  Patient Amit".format(i[0]))
                
        elif(input_query == "health issue with patient id 4 patient amit"):
            mycur = cur.execute("SELECT Issue FROM Patient Where Patient_id=4")
            for i in mycur:
                print("{} is the Health issue with  Patient Amit".format(i[0]))
                
                
        
        elif(input_query == "disease name of patient amit"):
            mycur = cur.execute("SELECT Issue FROM Patient WHERE Patient_Name = 'Amit' ")    
            for i in mycur:
                print("{} is the Health issue with  Patient Amit".format(i[0]))
                
                
        elif(input_query == "what is the health issue with garima"):
            mycur = cur.execute("SELECT Issue FROM Patient WHERE Patient_Name = 'Garima' ")    
            for i in mycur:
                print("{} is the Health issue with  Patient Garima".format(i[0]))
                
                
        elif(input_query == "health issue with patient id 5 patient garima"):
            mycur = cur.execute("SELECT Issue FROM Patient Where Patient_id=5")
            for i in mycur:
                print("{} is the Health issue with  Patient Garima".format(i[0]))
            
                
                
        
        elif(input_query == "disease name of patient yuvraj sinha"):
            mycur = cur.execute("SELECT Issue FROM Patient WHERE Patient_Name = 'Garima' ")    
            for i in mycur:
                print("{} is the Health issue with  Patient Garima".format(i[0]))        
                
                
        elif(input_query == "maximum age patient name"):
            mycur = cur.execute("SELECT Patient_Name FROM Patient GROUP BY(Age) HAVING Age = (SELECT max(Age) FROM Patient) ")    
            for i in mycur:
                print(i[0])
                
        elif(input_query == "minimum age patient name"):
            mycur = cur.execute("SELECT Patient_Name FROM Patient GROUP BY(Age) HAVING Age = (SELECT min(Age) FROM Patient) ")    
            for i in mycur:
                print(i[0])
                
        elif(input_query == "average age of patients"):
            mycur = cur.execute("SELECT avg(Age) FROM Patient")    
            for i in mycur:
                print(i[0])
                
        elif(input_query == "best rating doctor"):
            mycur = cur.execute("SELECT Doctor_Name FROM Doctor WHERE Rating = (SELECT max(Rating) FROM Doctor)")    
            for i in mycur:
                for j in range(len(i)):
                    print("Highest rating Doctors are {}".format(i[j]))
                    
        elif(input_query == "worst rating doctor"):
            mycur = cur.execute("SELECT Doctor_Name FROM Doctor WHERE Rating = (SELECT min(Rating) FROM Doctor)")    
            for i in mycur:
                for j in range(len(i)):
                    print("lowest rating Doctors is {}".format(i[j]))   
                    
        elif(input_query == "highesst rating doctor"):
            mycur = cur.execute("SELECT Doctor_Name FROM Doctor WHERE Rating = (SELECT max(Rating) FROM Doctor)")    
            for i in mycur:
                for j in range(len(i)):
                    print("Highest rating Doctors are {}".format(i[j]))
                    
        elif(input_query == "lowest rating doctor"):
            mycur = cur.execute("SELECT Doctor_Name FROM Doctor WHERE Rating = (SELECT min(Rating) FROM Doctor)")    
            for i in mycur:
                for j in range(len(i)):
                    print("lowest rating Doctors is {}".format(i[j]))            
                
                
            
            
class reversegeocoding:
    def reversegeocoding_loc(input_query):
        con = sqlite3.connect("sql1.db")
        cur = con.cursor()
        
        if(input_query == "what is the clinic location of doctor mayank"):
            mycur = cur.execute("SELECT Clinic_lat,Clinic_long FROM Doctor WHERE Doctor_Name='Mayank Mishra' ")
            for i in mycur:
                lat = i[0]
                long = i[1]
            latitude = float(lat)
            longititude = float(long)
            coordinates = (latitude,longititude)
            location = rf.search(coordinates)
           
            
        elif(input_query == "what is the clinic location of doctor piyush"):
            mycur = cur.execute("SELECT Clinic_lat,Clinic_long FROM Doctor WHERE Doctor_Name='Piyush Singh' ")
            for i in mycur:
                lat = i[0]
                long = i[1]
            latitude = float(lat)
            longititude = float(long)
            coordinates = (latitude,longititude)
            location = rf.search(coordinates)
        
            
        elif(input_query == "what is the clinic location of doctor soumya"):
            mycur = cur.execute("SELECT Clinic_lat,Clinic_long FROM Doctor WHERE Doctor_Name='Soumya' ")
            for i in mycur:
                lat = i[0]
                long = i[1]
            latitude = float(lat)
            longititude = float(long)
            coordinates = (latitude,longititude)
            location = rf.search(coordinates)
           
            
        elif(input_query == "what is the clinic location of doctor deepshikha"):
            mycur = cur.execute("SELECT Clinic_lat,Clinic_long FROM Doctor WHERE Doctor_Name='Deepshikha Mishra' ")
            for i in mycur:
                lat = i[0]
                long = i[1]
            latitude = float(lat)
            longititude = float(long)
            coordinates = (latitude,longititude)
            location = rf.search(coordinates)
        
        
        elif(input_query == "what is the clinic location of doctor rishabh"):
            mycur = cur.execute("SELECT Clinic_lat,Clinic_long FROM Doctor WHERE Doctor_Name='Rishabh Yadav' ")
            for i in mycur:
                lat = i[0]
                long = i[1]
            latitude = float(lat)
            longititude = float(long)
            coordinates = (latitude,longititude)
            location = rf.search(coordinates)

        return location[0]['name']