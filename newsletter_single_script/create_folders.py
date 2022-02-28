import os
import shutil

#local run uses this:
dir='../testing'

def check_leap_year(x):
    if x%100 == 0:
        if x%400 == 0:
            return True
        else: return False
    elif x%4 == 0:
        return True
    else: return False

def check_month(x):
    if x>0 and x<13:
        return True
    else: return False

def days_of_months(x,y):
    if x == 2 and check_leap_year(y) == True:
        return 29
    if x ==  2 and check_leap_year(y) == False:
        return 28
    if x%2 == 1:
        return 31
    else: return 30


#these two going to depends on the input
bulan = int(input("masukan bulan dalam angka: "))
tahun = int(input("masukan tahun dalam angka: "))

if check_month(bulan):
    days=days_of_months(bulan,tahun)
    for i in range(1,days+1):
         nameformat=str(i)+"-"+str(bulan)+"-"+str(tahun)
         newdir=dir+'/'+nameformat
         os.makedirs(newdir)
         shutil.copy('/Users/iganarendra/automation/Main Article Template.docx',newdir+'/topic1_'+nameformat+'.docx')
         shutil.copy('/Users/iganarendra/automation/Main Article Template.docx',newdir+'/topic2_'+nameformat+'.docx')
         shutil.copy('/Users/iganarendra/automation/Main Article Template.docx',newdir+'/topic3_'+nameformat+'.docx')