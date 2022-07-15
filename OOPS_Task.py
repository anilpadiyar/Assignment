import datetime
import logging
logging.basicConfig(filename='task3.log',level=logging.DEBUG, format="%(asctime)s  %(levelname)s %(name)s  %(message)s")

###Constructor
class ineuron_student:
    def __init__(self, name , level) :
        logging.info("class detail from student class")
        self.name = name
        self.level = level

class ineuron_internship:
    def __init__(self, project, techno):
        logging.info("class detail from internsip class")
        self.project = project
        self.techno = techno

class ineuron_cousre:
    def __init__(self, course_name , fee) :
        logging.info("class detail from course class")
        self.course.name = course_name
        self.__fee = fee

class ineuron_course_no:
    def __init__(self, cour_name, cour_no):
        logging.info("class detail from course number class")
        self.cour_name = cour_name
        self.cour_no = cour_no

    def __init__(self, cour_name, cour_no, course_fe):
        logging.info("class overriding from course number class")
        self.cour_name = cour_name
        self.cour_no = cour_no
        self.course_fe = course_fe

class ineuron_class:
    def __init__(self, class_ , student) :
        logging.info("class detail from class")
        self.class_ = class_
        self.student = student

class ineuron_Job:
    def __init__(self, company, jobrole, student):
        logging.info("class detail from job class")
        self.__company = company
        self.__jobrole = jobrole
        self.student = student


class ineuron_blog:
    def __init__(self, blogtopic , blog_detail) :
        logging.info("class detail from blog")
        self.blogtopic = blogtopic
        self.blog_detail = blog_detail

##########################Inheritance#########################################################
class ineuron_student_in:

    def student_detail(self, name , level):
        self.name = name
        self.level = level
        logging.info("student details")
        print("student name is: ", name)
        print("student level is ", level)

    def student_name(self, firstname , lastname):
        self.FN = firstname
        self.LN = lastname
        logging.info("student full name details")
        try :
            return self.FN+ ' '+ self.LN
        except Exception as e:
            print(e)


class ineuron_cousre_in(ineuron_student_in):

    def course_details(self, course_name, student_name):
        logging.info("detail from course class")
        self.course_name = course_name
        self.student_name = student_name
        try:
            if self.course_name == ' ' or self.student_name == ' ':
                logging.error("course or student  is empty ")
                raise ValueError("mandtraoy cannot be blank")
            elif self.project == 'FSDS' and self.student_name == 'Anil':
                print("The fee for FSDS course is RS 17700 only")
            else:
                print("not authorized person to see fee")
        except Exception as e:
            print(e)


class ineuron_internship(ineuron_cousre_in):

    def ineuron_internship(self,project,techno):
        logging.info("class detail from internsip class")
        self.project = project
        self.techno = techno
        logging.info("student internship name details")
        try:
            if self.project == ' ' or self.techno == ' ':
                logging.error("proj or techno is empty ")
                raise ValueError("project cannot be blank")
            elif self.project=='FSDS' and  self.techno =='Python':
                print("you are eligible for intership")
            else:
                print("not eligiblefor project")
        except Exception as e:
            print(e)


class ineuron_course_no_in(ineuron_cousre_in):
    def cours_no(self, cour_name):
        logging.info("extract the coursenumber for course name")
        self.cour_name = cour_name
        FScourse_number = 1234
        othcourse_number = 124
        try:
            if self.cour_name == ' ':
                logging.error("proj or techno is empty ")
                raise ValueError("project cannot be blank")
            elif self.cour_name == 'FSDS':
                print("Coursce Number is : ", course_number)
            else:
                print("Coursce Number is : ", othcourse_number)
        except Exception as e:
            print(e)


class ineuron_class_in:
    def Class_time(self, class_ ) :
        logging.info("class timing detail from class")
        self.class_ = class_
        try:
            if self.class_ == ' ':
                logging.error("Class is empty ")
                raise ValueError("class cannot be blank")
            elif self.class_ == 'FSDS':
                print("Timing for class is 3 to 6")
            else:
                print("other class may contact to Shivan")
        except Exception as e:
            print(e)

class ineuron_Job(ineuron_cousre_in,ineuron_class_in ):
    def job_(self, exp ,reqexp):
        logging.info("class detail from job class")
        self.exp = exp
        self.reqexp = reqexp
        creqexp = 2
        try:
            if self.exp <= 0:
                logging.error("your are fresher")
                raise ValueError("this is hiring is not for fresher")
            elif self.exp >= 2 and (self.reqexp >= creqexp or self.reqexp <=5):
                print("You are eliblet for iterview")
            else:
                print("High Experince is not requireds")
        except Exception as e:
            print(e)

#########################################Abstraction############################
class ineuron_student:
    student_name = 'Anil'
    _st_course = 'FSDS'
    __incours = {234:'FSDS',235:'PYTHON',236:'CPYTHON'}
    __studentsfees = 17700 #data abstraction
    __list = ['Anil', 'Munna', 'Ballu', 'Zlatan']
    __setid_ = {1,2,3,5,6,7,8,9,10,11,12,13,14,15}

    def student(self, name, reg):
        self.name = name
        self.reg = reg
        registred ='Y'
        try:
            if self.name == ' ' or self.reg == ' ':
                logging.error("student  is empty ")
                raise ValueError("mandtraoy cannot be blank")
            elif self.reg == 'Y' and self.name in ineuron_student.__list:
                logging.info("protected varabile %s", ineuron_student._st_course)
                print("you pay for  course ", ineuron_student._st_course )
                logging.info("private varabile %s", ineuron_student.__studentsfees)
                print("you pay the fee course is RS:", ineuron_student.__studentsfees)
            else:
                print("not authorized person to see fee")
        except Exception as e:
            print(e)

    def student_eligibilty(self, name, id):
        self.name = name
        self.id = id
        try:
            if name == ' ' or id == ' ':
                logging.error("student  is empty ")
                raise ValueError("mandtraoy cannot be blank")
            elif id in ineuron_student.__setid_  and name in ineuron_student.__list:
                logging.info("protected varabile %s", ineuron_student.__setid_ )
                try:
                    password = str(id) + name[:2]
                except Exception as a:
                    print(a)
                print("you id is :" , id )
                print("you password is :", password.strip())
                logging.info("You are eligible")
                print("you are eligible")
            else:
                print(" You are not enroll")
        except Exception as e:
            print(e)

class Job_offer_student(ineuron_student):
    __studentpackg = 770000 #data abstraction

    def st_offer(self, name, offered, course):
        self.name = name
        self.offered = offered
        self.course = course
        try:
            if self.name == ' ' or self.offered == ' ' or self.course == ' ':
                logging.error("Mandotory fields are  is empty %s %s %s ", self.name, self.offered , course)
                raise ValueError("mandtraoy cannot be blank")
            elif self.offered == 'Y' and self.name in ineuron_student.__list and ineuron_student._st_course == self.course:
                print("you package is RS:" , ineuron_student.__studentspackg)
            else:
                print("not authorized person to see offer")
        except Exception as e:
            print(e)


class ineuron_cousre(ineuron_student):
    def course(self, course_id) :
        self.course_id =course_id
        logging.info("class detail from Ineuron course class")
        try:
            if course_id <=0 :
                logging.error("Mandotory fields are empty %s ")
                raise ValueError("mandtraoy cannot be blank")
            elif course_id > 0 :
                for cours_ in ineuron_student.__incours:
                    if cours_ == course_id:
                        logging.info("course detail availble %s %s", cours_, ineuron_student.__incours[cours_])
                        print("you course and course id is " , cours_, ineuron_student.__incours[cours_])
                    else:
                        print("not authorize preson ")
        except Exception as e:
            print(e)


##method ovriding
class ineuron_student1(ineuron_student):
    student_name = 'Sudhansu'
    _st_course = 'DataScient'
    __list = ['ani', 'Met']

    def student(self, name):
        logging.info("method overiiding ")
        self.name = name
        try:
            if name == ' ' :
                logging.error("student  is empty ")
                raise ValueError("mandtraoy cannot be blank")
            elif name in ineuron_student1.__list:
                logging.info("protected varabile form class student and studen1 %s", ineuron_student_st_course, ineuron_student1._st_course)
                print("you coursse is  ", ineuron_student._st_course , ineuron_student1._st_course)
                logging.info("youra age")
                print("you age is 23")
            else:
                print(" not deatl  avlable")
        except Exception as e:
            print(e)

    def student_eligibilty(self, name, id):
        self.name = name
        self.id = id
        try:
            if name == ' ' or id == ' ':
                logging.error("student  is empty ")
                raise ValueError("mandtraoy cannot be blank")
            else:
                logging.info("Method ovirding fromm studn1 class")
                print("your r name and ID is " , name , id)
        except Exception as e:
            print(e)


class class_:
    class_name = 'FSDS'
    class_type = 'Weekend '

    def dtl(self):
        return class_.class_name + ' ' + class_.class_type

class class2:
    class_name = 'Data ScienceS'
    class_type = 'Daily'

    def dtl(self):
        return class2.class_name + ' ' + class2.class_type


##########################################################################################
#Encaplsualtion

class ineuron_coursefee_en:
    __fee = 17700
    Lstadmin = ['Sudh', 'shiva']

    def __course(self):
        print("print fee for FSDS" , ineuron_coursefee_en.__fee)

    def fee_chg(self, admin,  new_value):
        self.admin = admin
        self.__feechange = new_value
        logging.info("method Encapsulation ")
        try:
            if admin == ' ':
                logging.error("admin is empty ")
                raise ValueError("mandtraoy cannot be blank")
            elif admin in ineuron_coursefee_en.Lstadmin:
                logging.info("admin is %s", admin ,)
                print("you are admin and you are eligible for fee changes")
                logging.info("your old fee: %s ", ineuron_coursefee_en.__fee)
                print("old fee ", ineuron_coursefee_en.__fee)
                try:
                    ineuron_coursefee_en.__fee = ineuron_coursefee_en.__fee +  new_value
                    gst_cal= (ineuron_coursefee_en.__fee * 5)/100
                    ineuron_coursefee_en.__fee = ineuron_coursefee_en.__fee + gst_cal
                    logging.info("your new fee:  %s", ineuron_coursefee_en.__fee)
                    print("new fee: ", ineuron_coursefee_en.__fee)
                except Exception as err:
                    print(err)
            else:
                print(" not deatl  avlable")
        except Exception as e:
            print(e)

class ineuron_interviw_en(ineuron_coursefee_en):
    import datetime
    __intvwdate= "2022-8-16"

    def course(self):
        print("prin __intvwdatet fee for FSDS" , ineuron_coursefee_en.__fee)

    def date_chg(self, admin, Ndays):
        self.admin = admin
        self.__daychange = Ndays
        logging.info("method Encapsulation ")
        try:
            if admin == ' ' and Ndays <= 0:
                logging.error("admin is empty ")
                raise ValueError("mandtraoy cannot be blank")
            elif admin in ineuron_coursefee_en.Lstadmin:
                logging.info("admin is %s", admin ,)
                print("you are admin and you are eligible for date changes")
                olddte = datetime.datetime.strptime(ineuron_interviw_en.__intvwdate, "%Y-%m-%d")
                logging.info("your old date: %s ", olddte)
                print("old date : ",  olddte)
                try:
                    new_date = olddte + datetime.timedelta(days = Ndays)
                    logging.info("your new date:  %s", new_date)
                    print("new date: ", new_date)
                except Exception as err:
                    print(err)
            else:
                print(" not deatl  avlable")
        except Exception as e:
            print(e)

####################################################################
#Polymorphism

class course_FSDS():
    logging.info("method Polymorphism ")
    def course_name(self):
        logging.info("Course Name is Full stack data science ")
        print("Your course name  is FSDS from INEURON")

    def language_used(self):
        logging.info("Lanuage would e PYTHON and DB would be MOngo DB")
        print("In FSDS we mostly used Python to anayze the code.")

    def job_type(self):
        logging.info("JOB type would be 'DS' and 'DA'")
        print("Jobtypes are data scincetis and data analystic.")

class course_Javadvp():
    logging.info("method Polymorphism ")

    def course_name(self):
        logging.info("Course name is JAVA ")
        print("Your course name  is JAVA from INEURON")

    def language_used(self):
        logging.info("language is JS advance Java")
        print("In JAva we mostly used Python to anayze the code.")

    def job_type(self):
        logging.info("Java Developer ")
        print("Type of job are java application developer.")


class ineuron_pl:
    def classname(self):
        print("INeuron")

class student_FSDS(ineuron_pl):
    def intro(self):
        print("studet from FSDS class are there")

    def class_name(self):
        self.classname()
        print("your class for FSDS")


class student_oth(ineuron_pl):
    def class_oth(self):
        self.classname()
        print("your class for other course")


class std_java(student_oth):
    def std(self):
        self.class_oth()
        print("you cna have class  forjava and  all the other technology ")







