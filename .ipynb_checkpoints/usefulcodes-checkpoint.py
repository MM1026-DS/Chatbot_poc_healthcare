
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