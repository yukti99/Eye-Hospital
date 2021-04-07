#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lenovo
#
# Created:     23-01-2017
# Copyright:   (c) lenovo 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import os
import random
import pickle
def main():
    pass

if __name__ == '__main__':
    main()

'''                   2016-17 BOARD PROJECT         '''

#Customised exception
def InvalidDataError(Exception):
    pass


class Basics(object):

    def __init__(self):
       print "          Welcome To OJO SPECIALITY INSTITUTE,DELHI   "


#--------------UNIQUE PATIENT ID GENERATION---------------------#

#Use of 'random' module
       r=random.randint(100,10000)
       a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
       i=random.randint(0,26)
       self.id=str(a[i])+str(r)

#-----------PATIENT'S DATA COLLECTION FORM--------------------#

#Exception handling using try-except block
       while True:
        try:
            self.name=raw_input("Patient Name:")
            break

        except:
            print "Invalid data.Pls Enter Name again."

       while True:
        try:
            self.age=int(raw_input(("Patient Age:")))
            if 1<=self.age<=105:
                break

            else:
                raise InvalidDataError


        except:
            print "Data Entered Not Valid"

       while True:
        try:
            self.sex=raw_input("Sex(M/F/T):")
            if self.sex not in ["M","F","T"]:
                raise InvalidDataError
            else:
                break

        except:
            print "Data Entered Not Valid"


       while True:
           try:
            self.email=raw_input("Email id:")
            if "@" and "."   in self.email:
                 break
            else:
                   raise InvalidDataError

           except :
               print "Data Entered Not Valid"


       while True:

           try:
            self.phone=int(raw_input("Phone no(s):"))
            if len(str(self.phone))==10:
                break
            else:
                raise ValueError


           except:
              print "Invalid Phone Number"

#ADDING PATIENT DATA TO HOSPITAL RECORDS

    def Patient_info(self):

        f=open("Patient data.txt","a+")
        f.write ("%s"%(self.id))
        f.write ("\tName:%s\n"%(self.name))
        f.write ("\tAge:%s\n"%(self.age))
        f.write ("\tSex:%s\n"%(self.sex))
        f.write ("\tEmail:%s\n"%(self.email))
        f.write ("\tPhone:%s\n"%(self.phone))
        f.write ("\n")
        f.close()



    def __str__(self):
        return "Id: "+str(self.id)+"\n"+"Name:"+str(self.name)+"\n"+"Age:"+str(self.age)+"\n"+"Sex:"+str(self.sex)+"\n"+"Email:"+str(self.email)+"\n"+"Phone:"+str(self.phone)



    def Eye_Diseases(self):
        print "                         KNOW MORE:                  "
        print "1.Uveitis :is the inflammation of the inside the eye, specifically affecting one or more of the three parts of the eye that make up the uvea."
        print "Bulging eyes, or proptosis: occurs when one or both eyes protrude from the eye sockets due to space taking lesions such as swelling of the muscles, fat, and tissue behind the eye"

        print "Cataracts: are a degenerative form of eye disease in which the lens gradually becomes opaque and vision mists over."
        print "Colour blindness is not actually blindness in the true sense but rather is a colour vision deficiency?people who are affected by it simply do not agree with most other people about colour matching."
        print "Crossed eyes (or strabismus) occur when a person eyes are not able to align on the same point at the same time, and appear to be misaligned or pointed in different directions."
        print "Ocular hypertension: is an increase in pressure in the eye that is above the range considered normal."
        print "Low vision :Whenever ordinary glasses or contact lenses don't produce clear vision, you are considered to have low vision."
        print "Lazy eye:Commonly known as lazy eye, amblyopia is poor vision in an eye that does not receive adequate use during early childhood."
        print "Glaucoma : occurs when a build-up of fluid in the eye creates pressure, damaging the optic nerve."
        print "Eye Floaters: are small specks or clouds that move across your field of vision?especially when you are looking at a bright, plain background, like a blank wall or a cloudless blue sky."

#-----------PATIENT FEEDBACK FORM-----------------#



#-------------DISEASES-------------#

#FILE HANDLING
def Eye_Infection():
    f=open("Eye Infection.txt","rb")
    l=f.read()
    print l
    f.close()

def Eye_Muscle_Problems():
    f=open("Eye Muscle Problems .txt","rb")
    l=f.read()
    print l
    f.close()

def Eye_Ulcers():
    f=open("Eye Ulcers.txt","rb")
    l=f.read()
    print l
    f.close()

def Glaucoma():
    f=open("Glaucoma.txt","rb")
    l=f.read()
    print l
    f.close()

def Cataracts():
    f=open("Cataracts.txt","rb")
    l=f.read()
    print l
    f.close()

def Hypermetropia():
    f=open("Hypermetropia.txt","rb")
    l=f.read()
    print l
    f.close()

def Myopia():
    f=open("Myopia.txt","rb")
    l=f.read()
    print l
    f.close()
def Dry_Eye_Syndrome():
    f=open("Dry Eye Syndrome.txt","rb")
    l=f.read()
    print l
    f.close()
def Night_Blindness():
    f=open("Night Blindness.txt","rb")
    l=f.read()
    print l
    f.close()

#---------------DIAGNOSIS---------------------#
def Examination():
    f=open("Symptoms.txt","r+")
    s=f.read()
    print s
    Ques=int(raw_input("Please describe your symptom according to the list(1/2/3/4/5/6/7/8/9)"))
    if Ques==1:
        power=random.randrange(-4,0)
        print "After close examination you are diagnosed with:"
        Myopia()
        print "Your Power is %d"%(power)
        p=raw_input("Do you want to know more about power(Y/N)")
        if p=='Y':
            with open("Power.txt","r+") as f:
                a=f.read()
                print a
    if Ques==2:
        power=random.randrange(1,4)
        print "After close examination you are diagnosed with :"
        Hypermetropia()
        print "Your Power is %d"%(power)
        p=raw_input("Do you want to know more about power(Y/N)")
        if p=='Y':
            with open("Power.txt","r+") as f:
                a=f.read()
                print a


    if Ques==3:
        q1=raw_input("Do you have difficulty in seeing in the dark or dim light?(Y/N)")
        if q1=="Y":
              print "After close examination you are diagnosed with:"
              Night_Blindness()

        else:
            print "Please carefully examine your symptoms again and choose from the options"
            with open("Symptoms.txt","r+") as f1:
                l=f1.read()
                print l


            print "Medical Advice: Please undergo a computerised Eye Checkup"


    if Ques==4:
        q1=raw_input("Is your age more than 60 yrs?(Y/N)")
        q2=raw_input("Is your vision frosty or fogged-up window(Y/N)")
        q3=raw_input("Do you experience double vision or vision loss?(Y/N)")
        if q1=="Y"or q2=="Y" or q3=="Y":
            print "After close examination you are diagnosed with"
            Cataracts()

        else:
            print "Please carefully examine your symptoms again and choose from the options"
            with open("Symptoms.txt","r+") as f1:
                l=f1.read()
                print l


            print "Medical Advice: Please undergo a computerised Eye Checkup"

    if Ques==5:
        q1=raw_input("Do you experience rainbow-colored circles around bright lights?(Y/N)")
        q2=raw_input("Are you having severe eye and head ache for some weeks?(Y/N)")
        q3=raw_input("Hazy or blurred vision?(Y/N)")
        if q1=="Y"or q2=="Y" or q3=="Y":
            print "After close examination you are diagnosed with"
            Glaucoma()

        else:
            print "Please carefully examine your symptoms again and choose from the options"
            with open("Symptoms.txt","r+") as f1:
                l=f1.read()
                print l



            print "Medical Advice: Please undergo a computerised Eye Checkup"

    if Ques==6:
        q1=raw_input("Blurry or hazy vision?(Y/N)")
        q2=raw_input("Eye Itching and discharge?(Y/N)")
        q3=raw_input("Sensitivity to light ?(Y/N)")
        q4=raw_input("any White patch on eye?(Y/N)")
        if q1=="Y"or q2=="Y" or q3=="Y" or q4=="Y":
            print "After close examination you are diagnosed with:"
            Eye_Ulcers()
            print "For acute case: Suggested treatments....."
            print "Corneal Transplant, microlaser therapy"

        else:
             print "Please carefully examine your symptoms again and choose from the options"
             with open("Symptoms.txt","r+") as f1:
                l=f1.read()
                print l


             print "Medical Advice: Please undergo a computerised Eye Checkup"




    if Ques==7:
        q1=raw_input("Do you have a sensation of a foreign body in the eye(Y/N)")
        q2=raw_input("Do you experience aversion to light?(Y/N)")
        q3=raw_input("Have you had redness or small red lines in the white of the eye ?(Y/N)")
        if q1=="Y"or q2=="Y" or q3=="Y":
            print "After close examination you are diagnosed with:"
            Eye_Infection()

        else:
            print "Please carefully examine your symptoms again and choose from the options"
            with open("Symptoms.txt","r+") as f1:
                l=f1.read()
                print l


            print "Medical Advice: Please undergo a computerised Eye Checkup"



    if Ques==8:
        q1=raw_input("Are you having blurry vision or focus problems?(Y/N)")
        q2=raw_input("Foreign body sensation -- the feeling that something is in the eye, whether real or imagined.?(Y/N)")
        q3=raw_input("Are you suffering with severe eye pain and redness?(Y/N)")
        q4=raw_input("Do you feel like keeping your eye closed for long times especially during the night?(Y/N)")
        if q1=="Y"or q2=="Y" or q3=="Y" or q4=="Y":
            print "After close examination you are diagnosed with: Eye Muscle weakening"
            Eye_Muscle_Problems()

        else:
            print "Please carefully examine your symptoms again and choose from the options"
            with open("Symptoms.txt","r+") as f1:
                l=f1.read()
                print l


            print "Medical Advice: Please undergo a computerised Eye Checkup"


    if Ques==9:
        q1=raw_input("Do you feel discomfort and sensitivity to light?(Y/N)")
        q2=raw_input("Do you have a dry, inflamed or red eye?(Y/N)")
        q3=raw_input("Are you a woman above the age of 50?(Y/N)")
        if q1=="Y"or q2=="Y" or q3=="Y":
            print "After close examination you are diagnosed with:"
            Dry_Eye_Syndrome()

        else:
            print "Please carefully examine your symptoms again and choose from the options"
            with open("Symptoms.txt","r+") as f1:
                l=f1.read()
                print l


            print "Medical Advice: Please undergo a computerised Eye Checkup"

#-------------APPOINTMENT------------------#

def appointment():
        r=raw_input("Want a Next Appointment Date:(Y/N)")
        if r=="Y":

            d=random.randint(1,28)
            m=random.randint(1,12)
            y=random.randint(2017,2018)

            print "Your next Appointment date: %d/%d/%d" %(d,m,y)



#INHERITANCE
class feedback_form():
    def feeback(self):
        print "         HELP US DO BETTER           "
        print " A: Excellent B: Good C:Satisfactory D:Need improvement."
        self.a=raw_input("Behaviour of Staff")
        self.b=raw_input("Neat and Clean Premises")
        self.c=raw_input("Ease of finding where to go")
        self.d=raw_input("Advice and treatment of Doctor")
        self.e=raw_input("Overall experience?")
        self.f=raw_input("Would you refer us to your friends or relatives?(Y/N)")
        self.g=raw_input("Any other advice?")
        print "Thank you for sparing your valuable time!"

class feedback_evaluation(Basics,feedback_form):

    def evaulation(self):
        feedback_form.feeback(self)
        f=open("feedback.txt","a+")
        f.write("\n---------------------------------------------------------------------\n")
        A="Excellent"
        B="Good"
        C="satisfactory"
        D="Need improvement"
        f.write("Name:%s \n"%(self.name))
        f.write("Behaviour of Staff           :")

        if self.a=="A":
            f.write(A)

        if self.a=="B":
            f.write(B)

        if self.a=="C":
            f.write(C)

        if self.a=="D":
            f.write(D)

        f.write("\n")

        f.write("Neat and Clean Premises      :")

        if self.b=="A":
            f.write(A)

        if self.b=="B":
            f.write(B)

        if self.b=="C":
            f.write(C)

        if self.b=="D":
            f.write(D)

        f.write("\n")

        f.write("Ease of finding where to go   :")
        if self.c=="A":
            f.write(A)

        if self.c=="B":
            f.write(B)

        if self.c=="C":
            f.write(C)

        if self.c=="D":
            f.write(D)

        f.write("\n")

        f.write("Advice and treatment of Doctor  :")
        if self.d=="A":
            f.write(A)

        if self.d=="B":
            f.write(B)

        if self.d=="C":
            f.write(C)

        if self.d=="D":
            f.write(D)

        f.write("\n")

        f.write("Overall experience?     :")
        if self.e=="A":
            f.write(A)

        if self.e=="B":
            f.write(B)

        if self.e=="C":
            f.write(C)

        if self.e=="D":
            f.write(D)

        f.write("\n")

        f.write("Would you refer us to your friends or relatives?(Y/N):   ")
        if self.f=="Y":
            f.write("Yes")

        if self.f=="N":
            f.write("No")

        f.write("\n")

        f.write("Any other advice?:     ")
        f.write("%s"%(self.g))
        f.write("\n")
        f.close()

    def __init__(self):
      super(feedback_evaluation,self).__init__()
      super(feedback_evaluation,self).Patient_info()
      super(feedback_evaluation,self).Eye_Diseases()

      Examination()
      appointment()
      self.evaulation()

#---------------THANK YOU----------------#

b=feedback_evaluation()
a=raw_input("Do you want to check your information?")
if a=="Y":
    print b


print "bye!Get well soon"
os.system("pause")



