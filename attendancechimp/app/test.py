'''Basic test harness to make sure all of the functionality works
'''

#importing time
import time

# Some boilerplate code to get things running
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendancechimp.settings")
django.setup()
print("[1] Initializing Django successful")


# import data from models to test
from app.models import *
print("[2] Import from models.py successful")


# do some clean up
from django.contrib.auth.models import User
for user in User.objects.all():
    user.delete()
print("[3] Deleted all users")

# create some fake data
# create a test instructor
ts_django , ts_up = create_ac_user("Taylor Swift", "ts@gmail.com", "shakeitoff", True)
mimi_django, mimi_up = create_ac_user("Mariah Carey", "mimi@gmail.com", "rainbow", True)
print("[4] Instructor user creation successful")

# create a test course
# TSwift
start = "21:45:00"
end = "21:46:00"
course_tswift = create_course("Intro to Data Eng", ts_up, ["M", "W", "F"], start, end)
assert(Course.objects.count() == 1)
print("[6] TSwift Course Creation successful")

# Mimi
start = "21:48:00"
end = "21:49:00"
course_mimi = create_course("Intro to Music", mimi_up, ["M", "W", "F"], start, end)
assert(Course.objects.count() == 1)
print("[7] Mimi Course Creation successful")

# create a test student
# duplicate 19 times
# Tswift class
bb_django , bb_up = create_ac_user("Bob Bar", "bb@gmail.com", "1234", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Bob Bar user creation successful")

bs_django , bs_up = create_ac_user("Barbara Striesand", "babss@gmail.com", "5678", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Barbara Striesand user creation successful")

ag_django , ag_up = create_ac_user("Ariana Grande", "ag@gmail.com", "2468", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Ariana Grande user creation successful")

ku_django , ku_up = create_ac_user("Kali Uchis", "ku@gmail.com", "1357", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Kali Uchis user creation successful")

at_django , at_up = create_ac_user("Abel Tesfaye", "at@gmail.com", "1111", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Abel Tesfaye user creation successful")

sw_django , sw_up = create_ac_user("Summer Walker", "sw@gmail.com", "2222", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Summer Walker user creation successful")

lg_django , lg_up = create_ac_user("Lady Gaga", "lg@gmail.com", "3333", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Lady Gaga user creation successful")

ws_django , ws_up = create_ac_user("Willow Smith", "ws@gmail.com", "4444", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Willow Smith user creation successful")

jz_django , jz_up = create_ac_user("Jay Zee", "jz@gmail.com", "5555", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Jay Zee user creation successful")

al_django , al_up = create_ac_user("Adam Levine", "al@gmail.com", "6666", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Adam Levine user creation successful")

# Mimi class

rs_django , rs_up = create_ac_user("Rina Sawayama", "rs@gmail.com", "7777", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Rina Sawayama user creation successful")

nf_django , nf_up = create_ac_user("Nelly Furtado", "nf@gmail.com", "8888", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Nelly Furtado user creation successful")

ab_django , ab_up = create_ac_user("Azealia Banks", "ab@gmail.com", "9999", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Azealia Banks user creation successful")

dc_django , dc_up = create_ac_user("Doja Cat", "dc@gmail.com", "1212", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Doja Cat user creation successful")

meg_django , meg_up = create_ac_user("Megan Pete", "meg@gmail.com", "1313", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Megan Pete user creation successful")

pp_django , pp_up = create_ac_user("Pink Pantheress", "pp@gmail.com", "1414", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Pink Pantheress user creation successful")

rih_django , rih_up = create_ac_user("Rihanna Fenty", "rih@gmail.com", "1515", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Rihanna Fenty user creation successful")

sol_django , sol_up = create_ac_user("Solange Knowles", "sol@gmail.com", "1616", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Solange Knowles user creation successful")

steve_django , steve_up = create_ac_user("Steve Lacy", "steve@gmail.com", "1717", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Steve Lacy user creation successful")

sza_django , sza_up = create_ac_user("Solana Rowe", "sza@gmail.com", "1818", False)
assert(User.objects.count() == 2)
assert(UniversityPerson.objects.count() == 2)
print("[5] Solana Rowe user creation successful")

# create a qr code - Tswift
code = create_qr_code(course_tswift)
assert(QRCode.objects.count() == 1)
print("[8] TSwift QRCode Creation successful with code=",code.code)

# create a qr code - Mimi
code = create_qr_code(course_mimi)
assert(QRCode.objects.count() == 1)
print("[9] Mimi QRCode Creation successful with code=",code.code)

# Tswift

# create qr code upload
upload = process_upload(course_tswift, bb_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[10] TSwift QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(10)

# create qr code upload
upload = process_upload(course_tswift, bs_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[10] TSwift QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(10)

# create qr code upload
upload = process_upload(course_tswift, ag_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[10] TSwift QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(10)

# create qr code upload
upload = process_upload(course_tswift, ku_up, None)
assert(QRCodeUpload.objects.count() == 1)
print("[10] TSwift QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(10)

# create qr code upload
upload = process_upload(course_tswift, at_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[10] TSwift QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(30)

# create qr code upload
upload = process_upload(course_tswift, sw_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[10] TSwift QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(10)

# create qr code upload
upload = process_upload(course_tswift, lg_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[10] TSwift QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(10)

# create qr code upload
upload = process_upload(course_tswift, ws_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[10] TSwift QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(10)

# create qr code upload
upload = process_upload(course_tswift, jz_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[10] TSwift QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(10)

# create qr code upload
upload = process_upload(course_tswift, al_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[10] TSwift QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(75)

# Mimi

# create qr code upload
upload = process_upload(course_mimi, rs_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[11] Mimi QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(5)

# create qr code upload
upload = process_upload(course_mimi, nf_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[11] Mimi QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(5)

# create qr code upload
upload = process_upload(course_mimi, ab_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[11] Mimi QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(5)

# create qr code upload
upload = process_upload(course_mimi, dc_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[11] Mimi QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(5)

# create qr code upload
upload = process_upload(course_mimi, meg_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[11] Mimi QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(120)

# create qr code upload
upload = process_upload(course_mimi, pp_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[11] Mimi QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(10)

# create qr code upload
upload = process_upload(course_mimi, rih_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[11] Mimi QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(10)

# create qr code upload
upload = process_upload(course_mimi, sol_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[11] Mimi QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(10)

# create qr code upload
upload = process_upload(course_mimi, steve_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[11] Mimi QRCodeUpload successful by student = ",upload.student.user.username)

time.sleep(10)

# create qr code upload
upload = process_upload(course_mimi, sza_up, None) 
assert(QRCodeUpload.objects.count() == 1)
print("[11] Mimi QRCodeUpload successful by student = ",upload.student.user.username)

