
##Best recommendation
from fuzzywuzzy import fuzz
class bestrecommend1:
    def getContext_bestrecommend(input_query):
        input_query = input_query.lower()
        unsortedfuzz_lst = []
        unsortedstarement_lst = []
        lst_old = []
        idx = []
        sortedstaement_list = []
        for i in range(len(wx)):
            fuz_ratio = fuzz.ratio(wx[i],input_query)
            if fuz_ratio >=40:  
                unsortedfuzz_lst.append(fuz_ratio)
                unsortedstarement_lst.append(wx[i])
            
        for j in unsortedfuzz_lst:
            lst_old.append(j)
        unsortedfuzz_lst.sort(reverse = True)

        for j in unsortedfuzz_lst:
            idx.append(lst_old.index(j))
            
            
        for index in idx:
            sortedstaement_list.append(unsortedstarement_lst[index])
        return sortedstaement_list[:3],unsortedfuzz_lst,unsortedstarement_lst
print("--------------------------------------------------------------------------------------------------------------")    
    
##Best recommendation2
import operatorclass bestrecommend2:
    def getContext_bestrecommend(input_query):
        input_query = input_query.lower()
        unsortedfuzz_lst = []
        unsortedstarement_lst = []
        lst_old = []
        idx = []
        sortedstaement_list = []
        for i in range(len(wx)):
            fuz_ratio = fuzz.ratio(wx[i].replace(' ',''),input_query.replace(' ',''))
            if fuz_ratio >=40:  
                unsortedfuzz_lst.append(fuz_ratio)
                unsortedstarement_lst.append(wx[i])
        
        
        res = {} 
        for key in unsortedstarement_lst: 
            for value in unsortedfuzz_lst: 
                res[key] = value 
                unsortedfuzz_lst.remove(value)
                break  
        

        import operator
        from collections import OrderedDict

        
        sorted_tuples = sorted(res.items(), key=operator.itemgetter(1))
        print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]

        sorted_dict = OrderedDict()
        for k, v in sorted_tuples:
            sorted_dict[k] = v
            
        list_keys = list(sorted_dict.keys())
    
        for j in range(0,6):
            print(list_keys[len(list_keys)-1-j])
            

#        print(unsortedstarement_lst)
#         for j in unsortedfuzz_lst:
#             lst_old.append(j)
#         unsortedfuzz_lst.sort(reverse = True)

#         for j in unsortedfuzz_lst:
#             idx.append(lst_old.index(j))
            
            
#         for index in idx:
#             sortedstaement_list.append(unsortedstarement_lst[index])
#         return sortedstaement_list[:3],unsortedfuzz_lst,unsortedstarement_lst
print("----------------------------------------------------------------------------------------------------------------------------------------")

##Database connection

# mycur = cur.execute("SELECT Clinic_lat,Clinic_long FROM Doctor WHERE Doctor_Name='Piyush Singh' ")

# long = [i[1] for i in mycur]



# lat = [i[0] for i in mycur]



# for i in mycur:
#     latitiude = i[0]
#     longititude = i[1]


print("----------------------------------------------------------------------------------------------------------------------------------------------------")



def sent(sentence):
    for j in range(2):
        for i in sentence[j]:
            phrase_1 = re.sub(r"won\'t", "will not", i)
            phrase_2 = re.sub(r"can\'t","can not",phrase_1)
            phrase_3 = re.sub(r"n\'t", "not", phrase_2)
            phrase_4 = re.sub(r"\'re", "are", phrase_3)
            phrase_5 = re.sub(r"\'s", "is", phrase_4)
            
            phrase_6 = re.sub(r"\'d", "would", phrase_5)
            phrase_7 = re.sub(r"\'ll", "will", phrase_6)
            phrase_8 = re.sub(r"\'t", "not", phrase_7)
            phrase_9 = re.sub(r"\'ve", "have", phrase_8)
            phrase_10 = re.sub(r"\'m", "am", phrase_9)
            
            sent = re.sub("[?]+","",phrase_10)
               
            print(sent)          
                
wg = sent(data_frame["utterances"])
print(wg)


print("--------------------------------------------------------------------------------------------------")


def sent(sentence):
        for i in range(len(sentence)):
            phrase_1 = re.sub(r"won\'t", "will not", sentence[i])
            phrase_2 = re.sub(r"can\'t","can not",phrase_1)
            phrase_3 = re.sub(r"n\'t", "not", phrase_2)
            phrase_4 = re.sub(r"\'re", "are", phrase_3)
            phrase_5 = re.sub(r"\'s", "is", phrase_4)
            
            phrase_6 = re.sub(r"\'d", "would", phrase_5)
            phrase_7 = re.sub(r"\'ll", "will", phrase_6)
            phrase_8 = re.sub(r"\'t", "not", phrase_7)
            phrase_9 = re.sub(r"\'ve", "have", phrase_8)
            phrase_10 = re.sub(r"\'m", "am", phrase_9)
            
            sent = re.sub("[?]+","",phrase_10)
            print(sent)        
            
print("---------------------------------------------------------------------------------------------------------------------------------------------")

class bestrecommend:
    def getContext_bestrecommend(input_query):
        input_query = input_query.lower()
        input_query_vector = vectorizer.transform([input_query])
        unsorted_score = []
        unsorted_match = []
        recommedation_dict = {}
        best_recommend = []
        lst_old = []
        idx = []

        for ind, vector in enumerate(count_dense):
            sim_score = cosine_similarity(input_query_vector, count_dense[ind,:])[0][0]
            if sim_score>=0.4:
                unsorted_score.append(sim_score)
                unsorted_match.append(wx[ind])
        print(unsorted_score)
        print(unsorted_match)
                
        for j in unsorted_score:
            lst_old.append(j)
        unsorted_score.sort(reverse = True)
        
        for j in unsorted_score:
            idx.append(lst_old.index(j))
            
        
        for index in idx:
            best_recommend.append(unsorted_match[index])  
            
        return best_recommend[:3]

            
print("_______________________________________________________________________________________________________________________")

# import reverse_geocoder as rf
# import pprint

# class reversegeocoding:
#     def reversegeocoding_loc(lat,long):# mycur = cur.execute("SELECT Clinic_lat,Clinic_long FROM Doctor WHERE Doctor_Name='Piyush Singh' ")

# long = [i[1] for i in mycur]



# lat = [i[0] for i in mycur]



# for i in mycur:
#     latitiude = i[0]
#     longititude = i[1]

print("______________________________________________________________________________________________________________________________________")
#         location = []
#         latitude = float(lat)
#         longititude = float(long)
#         coordinates = (latitude,longititude)
#         location.append(rf.search(coordinates))
# #         pprint.pprint(location)
#         return location[0][0]["name"]
    
    
print("------------------------------------------------------------------------------------------------------------------------------------------")

###Chatbot first layout


flag = True
context = None
Bestmatch = None
reply = None


while flag:
    query =input("User >")

    score,_,context = getContext_details(query)
    
    if len(query)==0:
        print("Bot > Please provide the Input")
    elif query=="exit":
        flag=False
    
    else:
        if(score<0.4):
            print("Bot >Hello, I am a bot design for Specific Purpose How can I help you?")
        elif(score>=0.4 and context == "Doctor"):
            print("Bot > You want to check Information about Doctor Database Yes or No")
            query =input("User > ")
            if (query=="Yes"):
                print("Bot > Please provide your search query again")
                query =input("User >")
                Bestmatch = bestrecommend.getContext_bestrecommend(query)
                for response in Bestmatch:
                    print("Bot > {} ".format(response))
                print("Bot > Above are the matching query,Select the suitable query")
                print("Bot > Enter the best suitable query")
                query = input("User >")
                respond.sql_answer(query)
                
                
                
             
            else:
                print("bot > Sorry, I am currently unavailable to find query")
                
        elif(score>=0.4 and context=="Patient"):
            print("Bot > You want to check Information about Patient Database Yes or No")   
            query = input("User >")
            if (query=="Yes"):
                print("Bot > Please provide your Search query again")
                query = input("User >")
                Bestmatch_1 = bestrecommend.getContext_bestrecommend(query)
                for response in Bestmatch_1:
                    print("Bot > {}".format(response))
                print("Bot > Above are the matching query,Select the suitable query")
                print("Bot > Enter the best suitable query")
                query = input("User >")
                answer = respond.sql_answer(query)
                
              
            elif (query == "No" or "NO" or "no"):
                print("bot > Sorry, I am currently unavailable to find query")
            
            

print("__________________________________________________________________________________________________________________________________________________________")    
flag = True
context = None
Bestmatch = None
reply = None

while flag:
    query =input("User >")
    query = regrex(query)
    print("Bot > Hello, I am a bot design for Specific Purpose How can I help you?")
    time.sleep(1)
    print("Bot > I can help you to provide information about Doctor Speciliaty,Doctor Fees,Clinic Location")
    time.sleep(1)
    print("Bot > I can also help you to provide the information about the Patient Health Issue,Patient Doctor")
    time.sleep(1)
    print("Bot > Here is the list of Doctors {}".format(Doctors))
    time.sleep(1)
    print("Bot > Here is the list of Patients {}".format(Patients))
    time.sleep(1)
    print("Bot > Please Provide your Query for Search")
    query = input("User >")
    query = regrex(query)

    score,_,context = getContext_details(query)
    
    if len(query)==0:
        print("Bot > Please provide the Input")
    elif query=="exit":
        flag=False
    
    else:
        if(score<0.4):
            print("Bot > I am a bot design for Database related issues, Please Provide Suitable Qury")
            
        elif(score>=1.0):
            _,best_match,_ = getContext_details(query)
            
            answer = respond.sql_answer(best_match)
            
            break
            
            
        elif(score>=0.4 and context == "Doctor"):
            print("Bot > You want to check Detail Information about Doctor {} Yes or No" .format(get_name(nlp(query))))
            query =input("User > ")
            query = regrex(query)
            if(query == "exit"):
                flag = False
            if (query=="Yes"):
                print("Bot > Please provide your search query again for confirmation")
                query =input("User >")
                query = regrex(query)
                if(query == "exit"):
                    flag = False
                else:
                    Bestmatch = bestrecommend.getContext_bestrecommend(query)
                    for response in Bestmatch:
                        print("Bot > {} ".format(response))
                        print(" ")
                    print("Bot > None of the Above")
                    print(" ")
                    print("Bot > Above are the matching query,Select the suitable query")
                    print("Bot > Enter the best suitable query")
                    query = input("User >")
                    query = regrex(query)
                    if (query=="exit"):
                        flag=False
                    elif(query == "None of the Above"):
                        print("Bot > I am unable to  find this query this time,I am Design for Specific Purpose, I will help you after some time")
                        break
                    else:
                        respond.sql_answer(query)
                        time.sleep(2)
                        flag = False
                
                
            else:
                print("bot > Sorry, I am currently unavailable to find query")
                flag = False
                
        elif(score>=0.4 and context=="Patient"):
            print("Bot > Paient Informations are very Sensitive Information to check the information \n Please Provide the Patient id")
            time.sleep(2)
            
            query = int(input("User > "))
            
            print("Bot > You want to check Detail Information about Patient {} Yes or No" .format(patient_name(query)))   
            query = input("User >")
            query = regrex(query)
            if (query=="exit"):
                flag = False
            if (query=="Yes"):
                print("Bot > Please provide your Search query again for confirmation")
                query = input("User >")
                query = regrex(query)
                if (query == "exit"):
                    flag = False
                else:
                    Bestmatch_1 = bestrecommend.getContext_bestrecommend(query)
                    for response in Bestmatch_1:
                        print("Bot > {}".format(response))
                        print(" ")
                    print("Bot > None of the Above") 
                    print(" ")
                    print("Bot > Above are the matching query,Select the suitable query")
                    print("Bot > Enter the best suitable query")
                    query = input("User >")
                    query = regrex(query)
                    if (query=="exit"):
                        flag = False
                    
                    elif(query == "None of the Above"):
                        print("Bot > I am unable to  find this query this time,I am Design for Specific Purpose, I will help you after some time")
                        break
                    
                    else:
                        answer = respond.sql_answer(query)
                    print("Please provide query to search again or type exit to end the Conversation")    
                
              
            elif (query == "No"):
                print("bot > Sorry, I am currently unavailable to find query")
                print("Please provide query to search again or type exit to end the Conversation")
                query = input("User >")
                query = regrex(query)
                if (query=="exit"):
                    flag = False
            
            
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
def patient_name(query):
    name = None
    if query == 1:
        name = "Aditya Sonkar"
    elif query == 2:
        name = "Harsh Mishra"
    elif query == 3:
        name = "Yuvraj Sinha"
    elif query == 4:
        name = "Amit"
    elif query == 5:
        name = "Garima"
    else:
        name = "None"
        
    return name    
    