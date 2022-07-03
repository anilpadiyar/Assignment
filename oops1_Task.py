import logging
logging.basicConfig(filename='loginfo.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s  %(message)s')

class string_task:

# Extract string
        def string_extract(self,ext_string):
            logging.info("WE are about to extact string from index one to index 300 with a jump of 3")
            self.ext_string = ext_string
            try:
                if len(ext_string) == 0:
                    raise ValueError("empty string")
                    logging.error("empty string")
                else:
                    str = ext_string[::3]
                    logging.info("Extracted string is %s: " , str)
                    return str
            except Exception as e:
                logging.exception(e)

#Reverse string
        def string_reverse(self,rev_string):
            logging.info("WE are about to reverse string")
            self.rev_string = rev_string
            try:
                if len(rev_string) == 0:
                    raise ValueError("empty string")
                    logging.error("empty string")
                else:
                    str = rev_string[::-1]
                    logging.info("reversed string is %s: ", str)
                    return str
            except Exception as e:
                logging.exception(e)

#Split string
        def string_split(self,_string):
            logging.info("WE are about to split string")
            self._string = _string
            try:
                if len(_string) == 0:
                    raise ValueError("empty string")
                    logging.error("empty string")
                else:
                    str = _string.upper()
                    str1 = str.split()
                    logging.info("Split string is %s: ", str1)
                    return str1
            except Exception as e:
                logging.exception(e)

#Lower string
        def string_lower(self,_Lstring):
            logging.info("WE are about to lower string")
            self._Lstring = _Lstring
            try:
                if len(_Lstring) == 0:
                    raise ValueError("empty string")
                    logging.error("empty string")
                else:
                    str = _Lstring.lower()
                    logging.info("lower string is %s: ", str)
                    return str
            except Exception as e:
                logging.exception(e)

#Captilize string
        def string_split(self,_Cstring):
            logging.info("WE are about to captilize string")
            self._Cstring = _Cstring
            try:
                if len(_Cstring) == 0:
                    raise ValueError("empty string")
                    logging.error("empty string")
                else:
                    str = _Cstring.title()
                    logging.info("Title  string is %s: ", str)
                    return str
            except Exception as e:
                logging.exception(e)


###class  for list
class List_task:
        logging.info("log for List Class ")
# Reverse List
        def List_reverse(self,List_rev):
            logging.info("WE are about to reverse list ")
            self.List_rev = List_rev
            try:
                if len(List_rev) == 0:
                    raise ValueError("list is empty ")
                    logging.error("List is empty")
                else:
                    List_rev.reverse()
                    logging.info("revesre List is %s: " , List_rev)
                    return List_rev
            except Exception as e:
                logging.exception(e)


#extract numberfrom lisst
        def extact_int_list(self, l1, num):
            logging.info("we are about find the number")
            self.l1 = l1
            self.num = num
            try:
                if len(l1)== 0 or num == 0:
                    raise ValueError("list is empty or number is 0 ")
                    logging.error("List is empty or number is 0")
                elif type(num) != int:
                    raise TypeError("Number is not integer ")
                    logging.error("umber is not is 0")
                else:
                    for i in l1:
                        if i==num:
                            logging.info("the deseirded number is found %s ", i)
                            return i
                    else:
                        logging.info("number not found")
            except Exception as e:
                logging.exception(e)

#extrat sstring forn list
        def ext_Str_list(self,str_l1,fndstr):
            logging.info("WE are about to fiind string e list ")
            self.str_l1 = str_l1
            try:
                if len(str_l1) == 0:
                    raise ValueError("list is empty ")
                    logging.error("List is empty")
                else:
                    for i in str_l1:
                        if i == fndstr and type(i) ==str :
                            logging.info("string in list found and is %s: " , i)
                            return i
                    else:
                        logging.info("Sting not found")
            except Exception as e:
                logging.exception(e)


#extract list frm lisst
        def extact_list(self, lst1):
            logging.info("we are about ectract the list")
            self.lst1 = lst1
            try:
                if len(lst1)== 0:
                    raise ValueError("list is empty  ")
                    logging.error("List is empty")
                else:
                    for i in lst1:
                        if type(i) == list:
                            logging.info("the list is with in list  %s ", i)
                            return i
            except Exception as e:
                logging.exception(e)

#extract key of dict in lisst
        def extact_Keylist(self, list1_key):
            logging.info("we are about ectract the list")
            self.list1_key = list1_key
            try:
                if len(list1_key)== 0:
                    raise ValueError("list is empty  ")
                    logging.error("lit is empty")
                else:
                    l = []
                    for i in list1_key:
                        if type(i) == dict:
                            for k in i.keys():
                                logging.info("the key in list is %s ", k)
                                l.append(k)
                return l
            except Exception as e:
                logging.exception(e)

#extract VALUE of dict in list
        def extact_valuelist(self, list1_value):
            logging.info("we are about ectract the list")
            self.list1_value = list1_value
            try:
                if len(list1_value)== 0:
                    raise ValueError("list is empty  ")
                    logging.error("lit is empty")
                else:
                    l = []
                    for i in list1_value:
                         if type(i) == dict:
                            for k in i:
                                logging.info("the value in list is %s ", i[k])
                                l.append(i[k])
                return l
            except Exception as e:
                logging.exception(e)

#extract all the integer fron the list
        def ext_allint_list(self, list1):
            logging.info("we are about ectract the list")
            self.list1 = list1
            try:
                if len(list1)== 0:
                    raise ValueError("list is empty  ")
                    logging.error("list is empty")
                else:
                    l = []
                    for i in list1:
                        if type(i) == tuple or type(i) == list or type(i) == set:
                            for j in i:
                                if type(j) == int:
                                    logging.info("the int value is %s ", j)
                                    l.append(j)
                        if type(i) == dict:
                            logging.info("the value dict")
                            for k, v in i.items():
                                if type(k) == int or type(v) == int:
                                    l.append(k)
                                    l.append(v)
                return l
            except Exception as e:
                logging.exception(e)


#extract all sum of the integer fron the list
        def ext_sum_list(self, list1):
            logging.info("we are about ectract the list")
            self.list1 = list1
            try:
                if len(list1)== 0:
                    raise ValueError("list is empty  ")
                    logging.error("list is empty")
                else:
                    l = []
                    for i in list1:
                        if type(i) == tuple or type(i) == list or type(i) == set:
                            for j in i:
                                if type(j) == int:
                                    logging.info("the int value is %s ", j)
                                    l.append(j)
                        if type(i) == dict:
                            logging.info("the value dict")
                            for k, v in i.items():
                                if type(k) == int or type(v) == int:
                                    l.append(k)
                                    l.append(v)
                return sum(l)
            except Exception as e:
                logging.exception(e)

#extract all oddnumber   fron the list
        def ext_odd_num(self, list1):
            logging.info("we are about ectract the list")
            self.list1 = list1
            try:
                if len(list1)== 0:
                    raise ValueError("list is empty  ")
                    logging.error("list is empty")
                else:
                    l = []
                    for i in list1:
                        if type(i) == tuple or type(i) == list or type(i) == set:
                            for j in i:
                                if type(j) == int:
                                    if (j % 2) != 0:
                                        logging.info("the int value is %s ", j)
                                        l.append(j)
                        if type(i) == dict:
                            logging.info("the value dict")
                            for k, v in i.items():
                                if type(k) == int or type(v) == int:
                                    if (k % 2) != 0 or (v % 2) != 0:
                                        logging.info("the int value is %s ", j)
                                        l.append(k)
                                        l.append(v)
                return l
            except Exception as e:
                logging.exception(e)

#extract numbe of occurarne of indiviualnumber  fron the list
        def ext_occ_num(self, list1):
            logging.info("we are about ectract the list")
            self.list1 = list1
            try:
                if len(list1)== 0:
                    raise ValueError("list is empty  ")
                    logging.error("list is empty")
                else:
                    l = []
                    for i in list1:
                        if type(i) == tuple or type(i) == list or type(i) == set:
                            for j in i:
                                if type(j) == int:
                                    logging.info("the int value is %s ", j)
                                    l.append(j)
                        if type(i) == dict:
                            logging.info("the value dict")
                            for k, v in i.items():
                                if type(k) == int or type(v) == int:
                                    logging.info("the int value is %s ", j)
                                    l.append(k)
                                    l.append(v)
                count ={}
                for b in l:
                    if b in count:
                        count[b] = l.count(b)
                    else:
                        count[b] = l.count(b)
                return count
            except Exception as e:
                logging.exception(e)

######################### Tuple##########################################

class tuple_task:
    logging.info("class for tuple task")

#extract the tuples from list
    def ext_tuple(self,list_):
        logging.info("this is the extactring tupple from list ")
        self.list_ = list_
        try:
            if len(list_) ==0:
                raise Exception("list is empty  ")
                logging.error("list is empty")
            else:
                for i in list_:
                    if type(i) ==tuple:
                        logging.info("found tple in list ", i)
                        return i
                    else:
                        logging.error("no tuple in list withi in ist")
        except Exception as e:
            logging.exception(e)


######################################################Class for Dict
class dict_task:
    logging.info("class for dict task")

#extract the dictfrom list
    def ext_dict(self,list_):
        logging.info("this is the extact dict from list ")
        self.list_ = list_
        try:
            if len(list_) ==0:
                raise Exception("list is empty  ")
                logging.error("list is empty")
            else:
                for i in list_:
                    if type(i) ==dict:
                        logging.info("found dict in list ", i)
                        for j in i.items():
                            logging.info("found dict in list %s ", j)
                            return j
                else:
                    logging.error("no dictin list withi in ist")
        except Exception as e:
            logging.exception(e)



nu1 = List_task()
l1= [[1,2,3,4],{'mae':'anil'},[12,3,4],{100:121} ,(2,4,5,6,7,4)]
l2=[]
nl = nu1.ext_occ_num(l1)
print(nl)


'''

nu1 = List_task()
l1= [1,2,3,4,'anil']
nl = nu1.ext_Str_list(l1 ,'anil')

print(nl)

nu1 = List_task()
l1= [1,2,3,4]
nl = nu1.List_reverse(l1)

e_string = string_task()
output_str =e_string.string_extract("this is My First Python programming class and i am learNING python string and its function")
print(output_str)

e_string = string_task()
output_str =e_string.string_extract("")
print(output_str)

r_string = string_task()
rev_St = r_string.string_reverse("this is My First Python programming class and i am learNING python string and its function")
print(rev_St)

s_string = string_task()
split_St = s_string.string_split("this is My First Python programming class and i am learNING python string and its function")
print(split_St)
'''
