# Name : Rana Das
# School : Tagore Public School      Class : XII-B
# Academic Session : 2020 - 2021
# I.P. Project
# School Management v0.1

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


# Libraries Required : Mysql; Operator; Random; Time; matplotlib; Pandas; Numpy

import random
import time
from operator import itemgetter
import mysql.connector as sql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option("display.max_rows", None, "display.max_columns", None)

# Declaring Global Variables
school_name = "Tagore Public School"
school_address = "Tagore Lane, Shastri Nagar, Jaipur - 302016"
school_phone = "+91 0141 2280988"
school_email = "tpsshastrinagar@gmail.com"


# user defined functions

def connect():
    while True:
        try:
            global SQLhost
            SQLhost = input("\nSpecify SQL Server/Host to connect --->>> ")
            time.sleep(0.5)
            global SQLuser
            SQLuser = input("Enter Username --->>> ")
            time.sleep(0.5)
            global SQLpassword
            SQLpassword = input("Enter Password for User " + SQLuser + " --->>> ")
            time.sleep(0.5)
            global conn
            conn = sql.connect(host=SQLhost, user=SQLuser, password=SQLpassword, buffered=True, autocommit=True)
            global cursor
            cursor = conn.cursor()
            time.sleep(1)
            print("\nConnection Established with SQL Server")
            time.sleep(0.5)
            break
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")
            menu00()
    menu01()
    time.sleep(0.5)


def end():
    data = ["adieu", "cheerio", "sayonara", "adios", "so long", "good day", "farewell", "godspeed", "hasta la vista",
            "ciao", "जल्द ही मिलेंगे"]
    rndm = random.choice(data)
    print("\nTerminating School Management v0.1")
    time.sleep(1.5)
    print("\n" + rndm + "\n")
    while True:
        try:
            if conn.is_connected() is True:
                conn.disconnect()
                raise SystemExit
            else:
                raise SystemExit
        except NameError:
            raise SystemExit


def create_database():
    data = ["Student"]
    i = 0
    while i < len(data):
        try:
            query = "CREATE DATABASE " + data[i]
            cursor.execute(query)
            time.sleep(1)
            print("\nDatabase for " + data[i] + " Created")
            i += 1
            conn.commit()
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")
            i += 1


def Create_Student_Table():
    try:
        query1 = """CREATE TABLE Stud_data_personal (adm_no varchar(5), Name varchar(100), adm_class varchar(2), 
            DOB varchar(10), Gender Set("M", "F", "Trans"), Nationality varchar(25), HomeTown varchar(25), Category set(
            "GEN", "OBC", "SC", "ST", "OTHERS"),BloodGroup set("A+","A-","B+","B-","O+","O-","AB+","AB-"), 
            crnt_add varchar(255), crnt_pin varchar(6), prmnt_add varchar(255), prmnt_pin varchar(6), 
            No_of_siblings varchar(1), prvs_schl varchar(255), prvs_class varchar(2), prvs_score varchar(6), 
            PRIMARY KEY (adm_no)) """
        cursor.execute(query1)
        time.sleep(0.5)
        print("\nTable Stud_data_personal Created in Database Student")
        conn.commit()
    except sql.Error as err:
        time.sleep(0.5)
        print(f"Something Went Wrong: {err}")
    try:
        query2 = """CREATE TABLE Stud_data_guardian (adm_no varchar(5), Name varchar(100), Mother_Name varchar( 100), 
        M_Qualification varchar(100), M_occ varchar(100), M_designation varchar(100), M_off_add varchar( 255), 
        M_phone varchar(15),M_Email varchar(100), Father_Name varchar(100), F_Qualification varchar(100), 
        F_occ varchar( 100), F_designation varchar(100), F_off_add varchar(255), F_phone varchar(15), 
        F_Email varchar(100), PRIMARY KEY (adm_no)) """
        cursor.execute(query2)
        time.sleep(0.5)
        print("\nTable Stud_data_guardian Created in Database Student")
        conn.commit()
    except sql.Error as err:
        time.sleep(0.5)
        print(f"Something Went Wrong: {err}")
    try:
        query3 = """CREATE TABLE Results (adm_no varchar(5), Name varchar(100), Class varchar(2), english int(3),
         science int(3), Mathematics int(3), SSt int(3), Computer int(3), PRIMARY KEY (adm_no))"""
        cursor.execute(query3)
        time.sleep(0.5)
        print("\nTable Results Created in Database Student\n")
        conn.commit()
    except sql.Error as err:
        time.sleep(0.5)
        print(f"Something Went Wrong: {err}")


def addstudent():
    while True:
        try:
            time.sleep(0.5)
            print("\n<<Add Student Menu>>\n")
            print("1. Add Student Data in Table : {Student_Data_Personal}")
            print("2. Add Student Data in Table : {Student_Data_Guardian}")
            print("3. GoTo Student Database Menu")
            print("4. GoTo Database Menu")
            print("5. GoTo Program Menu\n")
            print("To Enter Your Choice Type Corresponding Menu Item Number.\n")
            usrin = int(input("Enter Your Choice Here --->>> "))
            if usrin == 1:
                cursor.execute("DESC stud_data_personal")
                time.sleep(0.5)
                adm_no = str(input("\nAdmission Number(5 digits) --->>> "))
                name = str(input("Name --->>> "))
                adm_class = str(input("Admission Sought in Class(2 Digits) --->>> "))
                dob = str(input("Date of Birth(DD-MM-YYYY) of Student --->>> "))
                gender = str(input("""Gender("M", "F", "Trans") --->>> """))
                nationality = str(input("Nationality --->>> "))
                home_town = str(input("HomeTown --->>> "))
                category = str(input("""Category("GEN", "OBC", "SC", "ST", "OTHERS") --->>> """))
                blood_group = str(input("""Blood Group of Student("A+","A-","B+","B-","O+","O-","AB+","AB-") --->>> """
                                        ))
                crnt_add = str(input("Current Address --->>> "))
                crnt_pin = str(input("Current Area PIN(6 Digits) --->>> "))
                prmnt_add = str(input("Permanent Address --->>> "))
                prmnt_pin = str(input("Permanent PIN(6 Digits) --->>> "))
                no_of_sib = str(input("Number of Siblings(1 Digits) --->>> "))
                prvs_schl = str(input("Previous School --->>> "))
                prvs_cls = str(input("Previous Class(2 Digits) --->>> "))
                perinprvscls = str(input("% Score Secured in Previous Class --->>> "))
                query = 'INSERT INTO Stud_data_personal VALUES(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', ' \
                        '\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', ' \
                        '\'{}\', \'{}\')'.format(adm_no, name, adm_class, dob, gender, nationality, home_town,
                                                 category, blood_group, crnt_add, crnt_pin, prmnt_add, prmnt_pin,
                                                 no_of_sib, prvs_schl, prvs_cls, perinprvscls)
                cursor.execute(query)
                conn.commit()
                time.sleep(1)
                print("\nEntries Stored in Table {Student_Data_Personal}")
            elif usrin == 2:
                cursor.execute("DESC stud_data_guardian")
                time.sleep(0.5)
                adm_no = str(input("\nAdmission Number(5 Digits) --->>> "))
                name = str(input("Name --->>> "))
                m_name = str(input("Mother's Name --->>> "))
                m_qual = str(input("Mother's Qualification --->>> "))
                M_Occ = str(input("Mother's Occupation --->>> "))
                M_designation = str(input("Mother's Designation --->>> "))
                M_off_add = str(input("Mother's Office Address --->>> "))
                M_phone = str(input("Mother's Contact Number --->>> "))
                M_Email = str(input("Mother's Email --->>> "))
                F_name = str(input("Father's Name --->>> "))
                F_Qual = str(input("Father's Qualification --->>> "))
                F_Occ = str(input("Father's Occupation --->>> "))
                F_designation = str(input("Father's Designation --->>> "))
                F_off_add = str(input("Father's Office Address --->>> "))
                F_phone = str(input("Father's Contact Number --->>> "))
                F_Email = str(input("Father's Email --->>> "))
                query = "INSERT INTO stud_data_guardian Values(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', " \
                        "\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')" \
                    .format(adm_no, name, m_name, m_qual, M_Occ, M_designation, M_off_add, M_phone, M_Email, F_name,
                            F_Qual, F_Occ, F_designation, F_off_add, F_phone, F_Email)
                cursor.execute(query)
                conn.commit()
                time.sleep(1)
                print("\nEntries Stored in Table {Student_Data_Guardian}")
            elif usrin == 3:
                time.sleep(0.5)
                student_menu()
            elif usrin == 4:
                time.sleep(0.5)
                menu01()
            elif usrin == 5:
                time.sleep(0.5)
                menu00()
                break
            else:
                time.sleep(2)
                print("\nInvalid Choice. Enter a Valid Choice")
                menu01()
        except ValueError:
            time.sleep(1)
            print("\nInvalid Value. Enter a Valid Choice ")
            time.sleep(2)
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")


def modifystudent():
    while True:
        try:
            time.sleep(0.5)
            print("\n<<Modify Student Data Menu>>\n")
            print("1. Modify Data in Table : {Student_Data_Personal}")
            print("2. Modify Data in Table : {Student_Data_Guardian}")
            print("3. GoTo Student Database Menu")
            print("4. GoTo Database Menu")
            print("5. GoTo Program Menu\n")
            print("To Enter Your Choice Type Corresponding Menu Item Number.\n")
            usrin = int(input("Enter Your Choice Here --->>> "))
            if usrin == 1:
                cursor.execute("DESC stud_data_personal")
                modifystudentpersonal()
            elif usrin == 2:
                cursor.execute("DESC stud_data_personal")
                modifystudentguardian()
            elif usrin == 3:
                time.sleep(0.5)
                student_menu()
            elif usrin == 4:
                time.sleep(0.5)
                menu01()
            elif usrin == 5:
                time.sleep(0.5)
                menu00()
                break
            else:
                time.sleep(1.5)
                print("\nInvalid Choice. Enter a Valid Choice")
                menu01()
        except ValueError:
            time.sleep(1)
            print("\nInvalid Value. Enter a Valid Choice ")
            time.sleep(2)
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")


def modifystudentpersonal():
    while True:
        try:
            time.sleep(0.5)
            print("\n<<Modify Personal Student Data Menu>>\n")
            print("1. Change Student's Name")
            print("2. Change Student's Class Admitted in")
            print("3. Change Student's Date of Birth")
            print("4. Change Student's Gender")
            print("5. Change Student's Nationality")
            print("6. Change Student's HomeTown")
            print("7. Change Student's Category")
            print("8. Change Student's BloodGroup")
            print("9. Change Student's Current Address")
            print("10. Change Student's Current Area PIN")
            print("11. Change Student's Permanent Address")
            print("12. Change Student's Permanent Area PIN")
            print("13. Change Student's Number of Siblings")
            print("14. Change Student's Previous School")
            print("15. Change Student's Previous Class")
            print("16. Change Student's Previous Class %")
            time.sleep(0.5)
            print("17. GoTo Modify Student Data Menu")
            print("18. GoTo Student Database Menu")
            print("19. GoTo Database Menu")
            print("20. GoTo Program Menu\n")
            print("To Enter Your Choice Type Corresponding Menu Item Number.\n")
            time.sleep(0.5)
            usrin = int(input("Enter Your Choice Here --->>> "))
            time.sleep(0.5)
            if usrin == 1:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Student's Name --->>> ")
                query = "UPDATE stud_data_personal SET Name = " + "'" + data + "'" + "WHERE adm_no = " + str(adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 2:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Class Admitted in --->>> ")
                query = "UPDATE stud_data_personal SET adm_class = " + "'" + data + "'" + "WHERE adm_no = " + str(
                    adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 3:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Date of Birth --->>> ")
                query = "UPDATE stud_data_personal SET DOB = " + "'" + data + "'" + "WHERE adm_no = " + str(adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 4:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("""Enter Gender("M", "F", "Trans") --->>> """)
                query = "UPDATE stud_data_personal SET Gender = " + "'" + data + "'" + "WHERE adm_no = " + str(adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 5:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Nationality --->>> ")
                query = "UPDATE stud_data_personal SET Nationality = " + "'" + data + "'" + "WHERE adm_no = " + str(
                    adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 6:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter HomeTown --->>> ")
                query = "UPDATE stud_data_personal SET HomeTown = " + "'" + data + "'" + "WHERE adm_no = " + str(adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 7:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Category --->>> ")
                query = "UPDATE stud_data_personal SET Category = " + "'" + data + "'" + "WHERE adm_no = " + str(adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 8:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("""Enter BloodGroup("A+","A-","B+","B-","O+","O-","AB+","AB-") --->>> """)
                query = "UPDATE stud_data_personal SET BloodGroup = " + "'" + data + "'" + "WHERE adm_no = " + str(
                    adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 9:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Current Address --->>> ")
                query = "UPDATE stud_data_personal SET crnt_add = " + "'" + data + "'" + "WHERE adm_no = " + str(adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 10:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Current Area PIN --->>> ")
                query = "UPDATE stud_data_personal SET crnt_pin = " + "'" + data + "'" + "WHERE adm_no = " + str(adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 11:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Permanent Address --->>> ")
                query = "UPDATE stud_data_personal SET prmnt_add = " + "'" + data + "'" + "WHERE adm_no = " + str(
                    adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 12:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Permanent Area PIN --->>> ")
                query = "UPDATE stud_data_personal SET prmnt_pin = " + "'" + data + "'" + "WHERE adm_no = " + str(
                    adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 13:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Number of Siblings --->>> ")
                query = "UPDATE stud_data_personal SET No_of_siblings = " + "'" + data + "'" + "WHERE adm_no = " + str(
                    adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 14:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Previous School --->>> ")
                query = "UPDATE stud_data_personal SET prvs_schl = " + "'" + data + "'" + "WHERE adm_no = " + str(
                    adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 15:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Previous Class --->>> ")
                query = "UPDATE stud_data_personal SET prvs_class = " + "'" + data + "'" + "WHERE adm_no = " + str(
                    adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 16:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Previous % --->>> ")
                query = "UPDATE stud_data_personal SET prvs_score = " + "'" + data + "'" + "WHERE adm_no = " + str(
                    adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 17:
                time.sleep(0.5)
                modifystudent()
            elif usrin == 18:
                time.sleep(0.5)
                student_menu()
            elif usrin == 19:
                time.sleep(0.5)
                menu01()
            elif usrin == 20:
                time.sleep(0.5)
                menu00()
                break
            else:
                time.sleep(1.5)
                print("\nInvalid Choice. Enter a Valid Choice")
                menu01()
        except ValueError:
            time.sleep(1)
            print("\nInvalid Value. Enter a Valid Choice ")
            time.sleep(2)
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")


def modifystudentguardian():
    while True:
        try:
            time.sleep(0.5)
            print("\n<<Modify Student Guardian Data Menu>>\n")
            print("1. Change Student's Name")
            print("2. Change Mother's Name")
            print("3. Change Mother's Qualification")
            print("4. Change Mother's Occupation")
            print("5. Change Mother's Designation")
            print("6. Change Mother's Office Address")
            print("7. Change Mother's Phone Number")
            print("8. Change Mother's Email")
            print("9. Change Father's Name")
            print("10. Change Father's Qualification")
            print("11. Change Father's Occupation")
            print("12. Change Father's Designation")
            print("13. Change Father's Office Address")
            print("14. Change Father's Phone Number")
            print("15. Change Father's Email")
            time.sleep(0.5)
            print("16. GoTo Modify Student Data Menu")
            print("17. GoTo Student Database Menu")
            print("18. GoTo Database Menu")
            print("19. GoTo Program Menu\n")
            print("To Enter Your Choice Type Corresponding Menu Item Number.\n")
            time.sleep(0.5)
            usrin = int(input("Enter Your Choice Here --->>> "))
            time.sleep(0.5)
            if usrin == 1:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Student's Name --->>> ")
                query = "UPDATE stud_data_guardian SET Name = " + "'" + data + "'" + "WHERE adm_no = " + str(adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 2:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Mother's Name --->>> ")
                query = "UPDATE stud_data_guardian SET Mother_Name = " + "'" + data + "'" + "WHERE adm_no = " + str(
                    adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 3:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Mother's Qualification --->>> ")
                query = f"UPDATE stud_data_guardian SET M_Qualification = \'{data}\'WHERE adm_no = {str(adm_no)}"
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 4:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("""Enter Mother's Occupation --->>> """)
                query = f"UPDATE stud_data_guardian SET M_occ = \'{data}\'WHERE adm_no = {str(adm_no)}"
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 5:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Mother's Designation --->>> ")
                query = "UPDATE stud_data_guardian SET M_designation = \'{0}\'WHERE adm_no = {1}".format(data, str(
                    adm_no))
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 6:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Mother's Office Address --->>> ")
                query = f"UPDATE stud_data_guardian SET M_off_add = \'{data}\'WHERE adm_no = {str(adm_no)}"
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 7:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Mother's Phone Number --->>> ")
                query = f"UPDATE stud_data_guardian SET M_phone = \'{data}\'WHERE adm_no = {str(adm_no)}"
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 8:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("""Enter Mother's Email --->>> """)
                query = "UPDATE stud_data_guardian SET M_Email = \'{0}\'WHERE adm_no = {1}".format(data, str(
                    adm_no))
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 9:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Father's Name --->>> ")
                query = "UPDATE stud_data_guardian SET Father_Name = " + "'" + data + "'" + "WHERE adm_no = " + \
                        str(adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 10:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Father's Qualification --->>> ")
                query = f"UPDATE stud_data_guardian SET F_Qualification = \'{data}\'WHERE adm_no = {str(adm_no)}"
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 11:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("""Enter Father's Occupation --->>> """)
                query = f"UPDATE stud_data_guardian SET F_occ = \'{data}\'WHERE adm_no = {str(adm_no)}"
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 12:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Father's Designation --->>> ")
                query = "UPDATE stud_data_guardian SET F_designation = \'{0}\'WHERE adm_no = {1}".format(data, str(
                    adm_no))
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 13:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Father's Office Address --->>> ")
                query = f"UPDATE stud_data_guardian SET F_off_add = \'{data}\'WHERE adm_no = {str(adm_no)}"
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 14:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Father's Phone Number --->>> ")
                query = f"UPDATE stud_data_guardian SET F_phone = \'{data}\'WHERE adm_no = {str(adm_no)}"
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 15:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("""Enter Father's Email --->>> """)
                query = "UPDATE stud_data_guardian SET F_Email = \'{0}\'WHERE adm_no = {1}".format(data, str(
                    adm_no))
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 16:
                time.sleep(0.5)
                modifystudent()
            elif usrin == 17:
                time.sleep(0.5)
                student_menu()
            elif usrin == 18:
                time.sleep(0.5)
                menu01()
            elif usrin == 19:
                time.sleep(0.5)
                menu00()
                break
            else:
                time.sleep(1.5)
                print("\nInvalid Choice. Enter a Valid Choice")
                menu01()
        except ValueError:
            time.sleep(1)
            print("\nInvalid Value. Enter a Valid Choice ")
            time.sleep(2)
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")


def deletestudent():
    while True:
        try:
            time.sleep(0.5)
            print("\n<<Delete Student Menu>>\n")
            print("1. Delete Data in Table : {Student_Data_Personal}")
            print("2. Delete Data in Table : {Student_Data_Guardian}")
            print("3. GoTo Student Database Menu")
            print("4. GoTo Database Menu")
            print("5. GoTo Program Menu\n")
            print("To Enter Your Choice Type Corresponding Menu Item Number.\n")
            usrin = int(input("Enter Your Choice Here --->>> "))
            if usrin == 1:
                cursor.execute("DESC stud_data_personal")
                delete_student_personal()
            elif usrin == 2:
                cursor.execute("DESC stud_data_personal")
                delete_student_guardian()
            elif usrin == 3:
                time.sleep(0.5)
                student_menu()
            elif usrin == 4:
                time.sleep(0.5)
                menu01()
            elif usrin == 5:
                time.sleep(0.5)
                menu00()
                break
            else:
                time.sleep(1.5)
                print("\nInvalid Choice. Enter a Valid Choice")
                menu01()
        except ValueError:
            time.sleep(1)
            print("\nInvalid Value. Enter a Valid Choice ")
            time.sleep(2)
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")


def delete_student_personal():
    while True:
        try:
            time.sleep(0.5)
            print("\n<<Delete Personal Student Data Menu>>\n")
            print("1. <<CAUTION>> Proceed To Deletion")
            time.sleep(0.5)
            print("2. GoTo Delete Student Data Menu")
            print("3. GoTo Student Database Menu")
            print("4. GoTo Database Menu")
            print("5. GoTo Program Menu\n")
            print("To Enter Your Choice Type Corresponding Menu Item Number.\n")
            time.sleep(0.5)
            usrin = int(input("Enter Your Choice Here --->>> "))
            time.sleep(0.5)
            if usrin == 1:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                query = "DELETE FROM stud_data_personal " + "WHERE adm_no = " + str(adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Deleted")
            elif usrin == 2:
                time.sleep(0.5)
                deletestudent()
            elif usrin == 3:
                time.sleep(0.5)
                student_menu()
            elif usrin == 4:
                time.sleep(0.5)
                menu01()
            elif usrin == 5:
                time.sleep(0.5)
                menu00()
                break
            else:
                time.sleep(1.5)
                print("\nInvalid Choice. Enter a Valid Choice")
                menu01()
        except ValueError:
            time.sleep(1)
            print("\nInvalid Value. Enter a Valid Choice ")
            time.sleep(2)
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")


def delete_student_guardian():
    while True:
        try:
            time.sleep(0.5)
            print("\n<<Delete Student Guardian Data Menu>>\n")
            print("1. <<CAUTION>> Proceed To Deletion")
            time.sleep(0.5)
            print("2. GoTo Delete Student Data Menu")
            print("3. GoTo Student Database Menu")
            print("4. GoTo Database Menu")
            print("5. GoTo Program Menu\n")
            print("To Enter Your Choice Type Corresponding Menu Item Number.\n")
            time.sleep(0.5)
            usrin = int(input("Enter Your Choice Here --->>> "))
            time.sleep(0.5)
            if usrin == 1:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                query = "DELETE FROM stud_data_guardian " + "WHERE adm_no = " + str(adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Deleted")
            elif usrin == 2:
                time.sleep(0.5)
                deletestudent()
            elif usrin == 3:
                time.sleep(0.5)
                student_menu()
            elif usrin == 4:
                time.sleep(0.5)
                menu01()
            elif usrin == 5:
                time.sleep(0.5)
                menu00()
                break
            else:
                time.sleep(1.5)
                print("\nInvalid Choice. Enter a Valid Choice")
                menu01()
        except ValueError:
            time.sleep(1)
            print("\nInvalid Value. Enter a Valid Choice ")
            time.sleep(2)
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")


def showstudent():
    while True:
        try:
            time.sleep(0.5)
            print("\n<<Show Student Menu>>\n")
            print("1. Show Data in Table : {Student_Data_Personal}")
            print("2. Show Data in Table : {Student_Data_Guardian}")
            print("3. GoTo Student Database Menu")
            print("4. GoTo Database Menu")
            print("5. GoTo Program Menu\n")
            print("To Enter Your Choice Type Corresponding Menu Item Number.\n")
            usrin = int(input("Enter Your Choice Here --->>> "))

            if usrin == 1:
                cursor.execute("DESC stud_data_personal")
                print(school_name)
                print(school_address)
                print('Phone :', school_phone, ' Email :', school_email)
                print("---------------------------------------------------------------------------------------------"
                      + "-------------------------")
                query = "SELECT * from stud_data_personal"
                table = pd.read_sql(query, conn)
                print(table)
            elif usrin == 2:
                cursor.execute("DESC stud_data_guardian")
                print(school_name)
                print(school_address)
                print('Phone :', school_phone, ' Email :', school_email)
                print("---------------------------------------------------------------------------------------------"
                      + "-------------------------")
                query = "SELECT * from stud_data_guardian"
                table = pd.read_sql(query, conn)
                print(table)
            elif usrin == 3:
                time.sleep(0.5)
                student_menu()
            elif usrin == 4:
                time.sleep(0.5)
                menu01()
            elif usrin == 5:
                time.sleep(0.5)
                menu00()
                break
            else:
                time.sleep(1.5)
                print("\nInvalid Choice. Enter a Valid Choice")
                menu01()
        except ValueError:
            time.sleep(1)
            print("\nInvalid Value. Enter a Valid Choice ")
            time.sleep(2)
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")


def modify_results():
    while True:
        try:
            time.sleep(0.5)
            print("\n<<Modify Personal Student Data Menu>>\n")
            print("1. Change Student's Name")
            print("2. Change Student's Class")
            print("3. Change English Marks")
            print("4. Change Science Marks")
            print("5. Change Mathematics Marks")
            print("6. Change Social Studies Marks")
            print("7. Change Computer Marks")
            time.sleep(0.5)
            print("8. GoTo Results Menu")
            print("9. GoTo Student Database Menu")
            print("10. GoTo Database Menu")
            print("11. GoTo Program Menu\n")
            print("To Enter Your Choice Type Corresponding Menu Item Number.\n")
            time.sleep(0.5)
            usrin = int(input("Enter Your Choice Here --->>> "))
            time.sleep(0.5)
            if usrin == 1:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Student's Name --->>> ")
                query = "UPDATE Results SET Name = " + "'" + data + "'" + "WHERE adm_no = " + str(adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 2:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Class --->>> ")
                query = "UPDATE Results SET Class = " + "'" + data + "'" + "WHERE adm_no = " + str(
                    adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 3:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = int(input("Enter English Marks --->>> "))
                query = "UPDATE Results SET english = {} WHERE adm_no = {}".format(data, adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 4:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("""Enter Science Marks --->>> """)
                query = "UPDATE Results SET science = {} WHERE adm_no = {}".format(data, adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 5:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Mathematics Marks --->>> ")
                query = "UPDATE Results SET Mathematics = {} WHERE adm_no = {}".format(data, adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 6:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter S.St Marks --->>> ")
                query = "UPDATE Results SET SSt = {} WHERE adm_no = {}".format(data, adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 7:
                adm_no = input("Specify Student Admission Number --->>> ")
                time.sleep(0.5)
                data = input("Enter Computer Marks --->>> ")
                query = "UPDATE Results SET Computer = {} WHERE adm_no = {}".format(data, adm_no)
                cursor.execute(query)
                conn.commit()
                time.sleep(0.5)
                print("Entry Updated")
            elif usrin == 8:
                time.sleep(0.5)
                results()
            elif usrin == 9:
                time.sleep(0.5)
                student_menu()
            elif usrin == 10:
                time.sleep(0.5)
                menu01()
            elif usrin == 11:
                time.sleep(0.5)
                menu00()
                break
            else:
                time.sleep(1.5)
                print("\nInvalid Choice. Enter a Valid Choice")
                menu01()
        except ValueError:
            time.sleep(1)
            print("\nInvalid Value. Enter a Valid Choice ")
            time.sleep(2)
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")


def graph():
    while True:
        try:
            time.sleep(0.5)
            print("\n<<Graph Menu>>\n")
            print("1. <<Bar Chart>>")
            print("2. <<Scatter Plot>>")
            print("3. GoTo Results Menu")
            print("4. GoTo Student Database Menu")
            print("5. GoTo Database Menu")
            print("6. GoTo Program Menu\n")
            print("To Enter Your Choice Type Corresponding Menu Item Number.\n")
            usrin = int(input("Enter Your Choice Here --->>> "))
            cursor.execute("DESC results")
            if usrin == 1:
                print('\n<<Bar Chart>>\n')
                cursor.execute("DESC results")
                adm = input("Enter Student's Admission --->>> ")
                query = "SELECT * from results"
                dataframe = pd.read_sql(query, conn)
                dataframe['Total'] = dataframe['english'] + dataframe['science'] + dataframe['Mathematics'] + dataframe[
                    'SSt'] + dataframe['Computer']
                d_frame_stud = dataframe.loc[dataframe['adm_no'] == adm]
                d_frame_max = dataframe[dataframe['Total'] == dataframe['Total'].max()]
                stud_list = []
                for index, rows in d_frame_stud.iterrows():
                    row1 = [rows.english, rows.science, rows.Mathematics, rows.SSt, rows.Computer]
                    stud_list = row1
                max_list = []
                for index, rows in d_frame_max.iterrows():
                    row2 = [rows.english, rows.science, rows.Mathematics, rows.SSt, rows.Computer]
                    max_list = row2
                x_lab = ['English', 'Science', 'Mathematics', 'SSt', 'Computer']
                plt.bar(np.arange(1, 10, 2), max_list, label='Topper', color='#ff0000', width=0.75)
                plt.bar(np.arange(1.75, 10.75, 2), stud_list, label='Student', color='#00ff00', width=0.75)
                plt.xticks(np.arange(1.375, 10.375, 2), x_lab)
                plt.xlabel('Subjects')
                plt.ylabel('Marks')
                plt.legend()
                plt.show()
            elif usrin == 2:
                print('\n<<Scatter Plot>>\n')
                cursor.execute("DESC results")
                query = "SELECT * from results"
                dataframe = pd.read_sql(query, conn)
                dataframe['Total'] = dataframe['english'] + dataframe['science'] + dataframe['Mathematics'] + dataframe[
                    'SSt'] + dataframe['Computer']
                d_frame_max = dataframe[dataframe['Total'] == dataframe['Total'].max()]
                stud_list = []
                i = 0
                while i < (len(dataframe)):
                    color = "#" + ''.join([random.choice('6789CDEF') for _ in range(6)])
                    for index, rows in dataframe.iterrows():
                        row1 = [rows.english, rows.science, rows.Mathematics, rows.SSt, rows.Computer]
                        stud_list.append(row1)
                    row2 = stud_list[i]
                    plt.scatter(np.arange(1 + i / 100, 10 + i / 100, 2), row2, color=color, marker='.')
                    i += 1
                max_list = []
                for index, rows in d_frame_max.iterrows():
                    row3 = [rows.english, rows.science, rows.Mathematics, rows.SSt, rows.Computer]
                    max_list = row3
                plt.scatter(np.arange(1 + len(dataframe) / 200, 10 + len(dataframe) / 200, 2), max_list, label='Topper', color='#000000')
                x_lab = ['English', 'Science', 'Mathematics', 'SSt', 'Computer']
                plt.xticks(np.arange(1 + len(dataframe) / 200, 10 + len(dataframe) / 200, 2), x_lab)
                plt.xlabel('Subjects')
                plt.ylabel('Marks')
                plt.legend()
                plt.show()
            elif usrin == 3:
                results()
                time.sleep(0.5)
            elif usrin == 4:
                time.sleep(0.5)
                student_menu()
            elif usrin == 5:
                time.sleep(0.5)
                menu01()
            elif usrin == 6:
                time.sleep(0.5)
                menu00()
                break
            else:
                time.sleep(1.5)
                print("\nInvalid Choice. Enter a Valid Choice")
                menu01()
        except ValueError:
            time.sleep(1)
            print("\nInvalid Value. Enter a Valid Choice ")
            time.sleep(2)
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")


def import_csv():
    while True:
        try:
            time.sleep(0.5)
            print("\n<<Import CSV Data Menu>>\n")
            print("1. Import Student Data in Table : {Student_Data_Personal}")
            print("2. Import Student Data in Table : {Student_Data_Guardian}")
            print("3. Import Student Results Data in Table : {Results}")
            print("4. GoTo Student Database Menu")
            print("5. GoTo Database Menu")
            print("6. GoTo Program Menu\n")
            print("To Enter Your Choice Type Corresponding Menu Item Number.\n")
            usrin = int(input("Enter Your Choice Here --->>> "))
            cursor.execute("SET GLOBAL local_infile=1")
            if usrin == 1:
                cursor.execute("DESC stud_data_personal")
                time.sleep(0.5)
                path = str(input("Specify Path of CSV File --->>> "))
                df = pd.read_csv('{}'.format(path))
                i = 0
                while i < len(df.index):
                    temp_series = df.iloc[i]
                    temp_list = temp_series.tolist()
                    [adm_no, name, adm_class, dob, gender, nationality, home_town, category, blood_group, crnt_add,
                     crnt_pin, prmnt_add, prmnt_pin, no_of_sib, prvs_schl, prvs_cls, perinprvscls] = itemgetter(
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)(temp_list)
                    cursor.execute("INSERT INTO stud_data_personal VALUES(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', "
                                   "\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', "
                                   "\'{}\', \'{}\', \'{}\')".format(adm_no, name, adm_class, dob, gender,
                                                                    nationality, home_town, category,
                                                                    blood_group, crnt_add, crnt_pin, prmnt_add,
                                                                    prmnt_pin, no_of_sib, prvs_schl, prvs_cls,
                                                                    perinprvscls))
                    conn.commit()
                    i += 1
                time.sleep(1)
                print("\nData Stored in Table {Student_Data_Personal}")
            elif usrin == 2:
                cursor.execute("DESC stud_data_guardian")
                time.sleep(0.5)
                path = str(input("Specify Path of CSV File --->>> "))
                df = pd.read_csv('{}'.format(path))
                i = 0
                while i < len(df.index):
                    temp_series = df.iloc[i]
                    temp_list = temp_series.tolist()
                    [adm_no, name, m_name, m_qual, M_Occ, M_designation, M_off_add, M_phone, M_Email, F_name, F_Qual,
                     F_Occ, F_designation, F_off_add, F_phone, F_Email] = itemgetter(
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)(temp_list)
                    cursor.execute(
                        "INSERT INTO stud_data_guardian Values(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', "
                        "\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')".format(
                            adm_no, name, m_name, m_qual, M_Occ, M_designation, M_off_add, M_phone, M_Email, F_name,
                            F_Qual, F_Occ, F_designation, F_off_add, F_phone, F_Email))
                    conn.commit()
                    i += 1
                time.sleep(1)
                print("\nData Stored in Table {Student_Data_Guardian}")
            elif usrin == 3:
                cursor.execute("DESC Results")
                time.sleep(0.5)
                path = str(input("Specify Path of CSV File --->>> "))
                df = pd.read_csv('{}'.format(path))
                i = 0
                while i < len(df.index):
                    temp_series = df.iloc[i]
                    temp_list = temp_series.tolist()
                    adm_no, Name, Class, eng, sc, math, sst, comp = itemgetter(
                        0, 1, 2, 3, 4, 5, 6, 7, )(temp_list)
                    cursor.execute('INSERT INTO Results VALUES({}, \'{}\', {}, {}, {}, {}, {},'
                                   ' {})'.format(adm_no, Name, Class, eng, sc, math, sst, comp))
                    conn.commit()
                    i += 1
                time.sleep(1)
                print("\nData Stored in Table {Results}")
            elif usrin == 4:
                time.sleep(0.5)
                student_menu()
            elif usrin == 5:
                time.sleep(0.5)
                menu01()
            elif usrin == 6:
                time.sleep(0.5)
                menu00()
                break
            else:
                time.sleep(2)
                print("\nInvalid Choice. Enter a Valid Choice")
                menu01()
        except ValueError:
            time.sleep(1)
            print("\nInvalid Value. Enter a Valid Choice ")
            time.sleep(2)
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")
        except FileNotFoundError:
            print("\nFile Not Found\n")
    raise SystemExit


def results():
    while True:
        try:
            print("\n<<Results Menu>>\n")
            print("1. Add New Results")
            print("2. Modify Entries")
            print("3. Delete Entries")
            print("4. Show Results")
            print("5. Generate Graph for a Student's Result")
            print("6. GoTo Student Database Menu")
            print("7. GoTo Database Menu")
            print("8. GoTo Program Menu\n")
            print("To Enter Your Choice Type Corresponding Menu Item Number.\n")
            usrin = int(input("Enter Your Choice Here --->>> "))
            if usrin == 1:
                print("<<Add New Results>>")
                time.sleep(0.5)
                adm_no = str(input("Enter Admission Number --->>> "))
                Name = str(input("Enter Student Name --->>> "))
                Class = str(input("Enter Class --->>> "))
                eng = int(input("Enter Marks Scored in English --->>> "))
                sc = int(input("Enter Marks Scored in Science --->>> "))
                math = int(input("Enter Marks Scored in Mathematics --->>> "))
                sst = int(input("Enter Marks Scored in Social Studies --->>> "))
                comp = int(input("Enter Marks Scored in Computer --->>> "))
                query = 'INSERT INTO Results VALUES({}, \'{}\', {}, {}, {}, {}, {}, ' \
                        '{})'.format(adm_no, Name, Class, eng, sc, math, sst, comp)
                cursor.execute(query)
                conn.commit()
                time.sleep(1)
                print("\nEntries Stored in Table {Results}\n")
            elif usrin == 2:
                modify_results()
                time.sleep(0.5)
            elif usrin == 3:
                while True:
                    try:
                        time.sleep(0.5)
                        print("\n<<Delete Result Menu>>\n")
                        print("1. <<Caution>>Delete Data")
                        print("2. GoTo Results Menu")
                        print("3. GoTo Student Database Menu")
                        print("4. GoTo Database Menu")
                        print("5. GoTo Program Menu\n")
                        print("To Enter Your Choice Type Corresponding Menu Item Number.\n")
                        usrin = int(input("Enter Your Choice Here --->>> "))
                        if usrin == 1:
                            cursor.execute("DESC Results")
                            adm_no = input("Specify Student Admission Number --->>> ")
                            time.sleep(0.5)
                            query = "DELETE FROM Results " + "WHERE adm_no = " + str(adm_no)
                            cursor.execute(query)
                            conn.commit()
                            time.sleep(0.5)
                            print("Entry Deleted")
                        elif usrin == 2:
                            results()
                            time.sleep(0.5)
                        elif usrin == 3:
                            time.sleep(0.5)
                            student_menu()
                        elif usrin == 4:
                            time.sleep(0.5)
                            menu01()
                        elif usrin == 5:
                            time.sleep(0.5)
                            menu00()
                            break
                        else:
                            time.sleep(1.5)
                            print("\nInvalid Choice. Enter a Valid Choice")
                            menu01()
                    except ValueError:
                        time.sleep(1)
                        print("\nInvalid Value. Enter a Valid Choice ")
                        time.sleep(2)
                    except sql.Error as err:
                        time.sleep(0.5)
                        print(f"Something Went Wrong: {err}")
                raise SystemExit
            elif usrin == 4:
                while True:
                    try:
                        time.sleep(0.5)
                        print("\n<<Show Student Results Menu>>\n")
                        print("1. Show Data in Table : {Results}")
                        print("2. GoTo Results Menu")
                        print("3. GoTo Student Database Menu")
                        print("4. GoTo Database Menu")
                        print("5. GoTo Program Menu\n")
                        print("To Enter Your Choice Type Corresponding Menu Item Number.\n")
                        usrin = int(input("Enter Your Choice Here --->>> "))
                        if usrin == 1:
                            cursor.execute("DESC results")
                            print(school_name)
                            print(school_address)
                            print('Phone :', school_phone, ' Email :', school_email)
                            print(
                                "----------------------------------------------------------------------------------"
                                + "------------------------------------")
                            query = "SELECT * from results"
                            table = pd.read_sql(query, conn)
                            table['Total'] = table['english'] + table['science'] + table[
                                'Mathematics'] + table[
                                                     'SSt'] + table['Computer']
                            print(table.sort_values(by='Total', ascending=False))
                        elif usrin == 2:
                            results()
                            time.sleep(0.5)
                        elif usrin == 3:
                            time.sleep(0.5)
                            student_menu()
                        elif usrin == 4:
                            time.sleep(0.5)
                            menu01()
                        elif usrin == 5:
                            time.sleep(0.5)
                            menu00()
                            break
                        else:
                            time.sleep(1.5)
                            print("\nInvalid Choice. Enter a Valid Choice")
                            menu01()
                    except ValueError:
                        time.sleep(1)
                        print("\nInvalid Value. Enter a Valid Choice ")
                        time.sleep(2)
                    except sql.Error as err:
                        time.sleep(0.5)
                        print(f"Something Went Wrong: {err}")
                raise SystemExit
            elif usrin == 5:
                graph()
                time.sleep(0.5)
            elif usrin == 6:
                time.sleep(0.5)
                student_menu()
            elif usrin == 7:
                time.sleep(0.5)
                menu01()
            elif usrin == 8:
                time.sleep(0.5)
                menu00()
                break
        except ValueError:
            time.sleep(1)
            print("\nInvalid Value. Enter a Valid Choice ")
            time.sleep(2)
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")


# Menus-----------------------------------------------------------------------------------------------------------------

# Menu 00
def menu00():
    while True:
        # Greetings
        time.sleep(1)
        print("\n")
        print("""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""")
        print("""░████████████░███████░████████░""")
        print("""░░░░░░██░░░░░░██░░░██░██░░░░░░░""")
        print("""░░░░░░██░░░░░░███████░████████░""")
        print("""░░░░░░██░░░░░░██░░░░░░░░░░░░██░""")
        print("""░░░░░░██░░░░░░██░░░░░░████████░""")
        print("""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""")
        time.sleep(0.5)
        print("\n\nWelcome To School Management v0.1\n")
        time.sleep(0.5)
        print("\nMore Program Functionality and Utility Will be Included in Future Release.\nCurrently Program is "
              "in it's infancy. \nOnly <Student> Database is Active. More will be Added Soon.\n\n ")
        try:
            print("<<<<<<Program Menu>>>>>>\n")
            time.sleep(0.5)
            print("1. Connect to SQL Server")
            print("2. Terminate Program")
            print("\nTo Enter Your Choice Type Corresponding Menu Item Number.\n")
            usrin = int(input("Enter Your Choice Here --->>> "))
            if usrin == 1:
                time.sleep(0.5)
                connect()
            elif usrin == 2:
                time.sleep(0.5)
                end()
                time.sleep(1)
            else:
                print("\nInvalid Choice. Enter 1 or 2 ")
                time.sleep(1)
                menu00()
        except ValueError:
            time.sleep(1)
            print("\nInvalid Value. Enter 1 or 2 ")


# Menu01
def menu01():
    while True:
        try:
            print("\n<<<<<<Database Menu>>>>>>\n")
            print("1. Student Database")
            print("9. GoTo Program Menu")
            print("0. <<CAUTION>> Create Database Framework")
            usrin = int(input("\nTo Enter Your Choice Type Corresponding Menu Item Number --->>> "))
            if usrin == 1:
                query = "USE Student"
                cursor.execute(query)
                time.sleep(0.5)
                print("\nActive Database --->>> Student\n")
                time.sleep(0.5)
                student_menu()
            elif usrin == 0:
                time.sleep(0.5)
                create_database()
                time.sleep(1)
            elif usrin == 9:
                time.sleep(0.5)
                menu00()
            else:
                time.sleep(0.5)
                print("\nInvalid Choice. Enter a Valid Choice")
                menu01()
        except ValueError:
            time.sleep(0.5)
            print("\nInvalid Value. Enter a Valid Choice ")
            time.sleep(1)
        except sql.Error as err:
            time.sleep(0.5)
            print(f"Something Went Wrong: {err}")


# Student Menu
def student_menu():
    while True:
        try:
            time.sleep(0.5)
            time.sleep(0.5)
            print("<<<Student Database Menu>>>")
            print("1. Add Student Data")
            print("2. Modify Student Data")
            print("3. Delete Student Data")
            print("4. Show Student Data")
            print("5. Results")
            print("6. GoTo Database Menu")
            print("7. GoTo Program Menu")
            print("9. <<CAUTION>> Load Data in CSV Format")
            print("0. <<CAUTION>> Create Table FrameWork")
            time.sleep(0.5)
            usrin = int(input("\nEnter Your Choice Here --->>> "))
            if usrin == 1:
                time.sleep(0.5)
                addstudent()
            elif usrin == 2:
                time.sleep(0.5)
                modifystudent()
            elif usrin == 3:
                time.sleep(0.5)
                deletestudent()
            elif usrin == 4:
                time.sleep(0.5)
                showstudent()
            elif usrin == 5:
                time.sleep(0.5)
                results()
            elif usrin == 6:
                time.sleep(0.5)
                menu01()
            elif usrin == 7:
                time.sleep(0.5)
                menu00()
            elif usrin == 0:
                time.sleep(0.5)
                Create_Student_Table()
            elif usrin == 9:
                time.sleep(0.5)
                import_csv()
            else:
                time.sleep(1)
                print("\nInvalid Choice. Enter a Valid Choice")
                student_menu()
        except ValueError:
            time.sleep(0.5)
            print("\nInvalid Value. Enter a Valid Choice ")
            time.sleep(1)


menu00()
