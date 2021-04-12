import time
from time import sleep
from os import system
from colorama import Fore
from tqdm import tqdm
from selenium import webdriver
import sys
import os
import random
from selenium.webdriver.firefox.options import Options
import webbrowser
from selenium.webdriver.common.keys import Keys

gmail_sign = "@"
phone_sign = "-"

# This is a open src script that is going to be posted on GitHub


def loading():
    os.system("cls")
    print(Fore.LIGHTCYAN_EX + """
                                    
                                     __   __     ______     _____     ______     __  __    
                                    /\ "-.\ \   /\  __ \   /\  __-.  /\  __ \   /\_\_\_\   
                                    \ \ \-.  \  \ \ \/\ \  \ \ \/\ \ \ \ \/\ \  \/_/\_\/_  
                                     \ \_\\"\_\   \ \_____\  \ \____-  \ \_____\   /\_\/\_\ 
                                      \/_/ \/_/   \/_____/   \/____/   \/_____/   \/_/\/_/ 
                                                       


                            Welcome to the Open Source Version. If you have any questions contact me Tex#4721

                                                            Coded by Tex#4721
            """)

    print(Fore.RESET)


def questions():

    while True:
        time.sleep(7.0)
        os.system("cls")
        while True:
            os.system("cls")

            user_name = input("What is your first and last name => ")
            if len(user_name) > 4:
                print("Storing . . .")
                time.sleep(1.5)
                for num in tqdm(range(100)):
                    sleep(0.01)
                break

            elif len(user_name) < 1:
                print("You didn't enter a first and last name")
                time.sleep(1.5)
            else:
                print("Error invalid input")
                time.sleep(1.5)

        while True:
            os.system('cls')

            user_address = input("What is your address => ")
            if len(user_address) > 3:
                print("Storing . . .")
                time.sleep(1.5)
                for num in tqdm(range(100)):
                    sleep(0.01)
                break
            elif len(user_address) < 1:
                print("You didn't enter any address")
                time.sleep(1.5)
            else:
                print("Error invalid input")
                time.sleep(1.5)

        while True:
            os.system('cls')

            user_state = input("What is your state => ")
            if len(user_state) >= 4:
                print("Storing . . .")
                time.sleep(1.5)
                for num in tqdm(range(100)):
                    sleep(0.01)
                break

            elif len(user_state) < 1:
                print("You didn't enter a state")
                time.sleep(1.5)

            else:
                print("Error invalid input")
                time.sleep(1.5)

        while True:
            os.system("cls")

            user_city = input("What is your city => ")
            if len(user_city) > 2:
                print("Storing . . .")
                time.sleep(1.5)
                for num in tqdm(range(100)):
                    sleep(0.01)
                break

            elif len(user_city) < 1:
                print("You didn't enter a city")
                time.sleep(1.5)

            else:
                print("Error invalid input")
                time.sleep(1.5)
        while True:
            os.system("cls")

            user_zipcode = input("What is your zipcode => ")
            if len(user_zipcode) > 2:
                print("Storing . . .")
                time.sleep(1.5)
                for num in tqdm(range(100)):
                    sleep(0.01)
                break

            elif len(user_zipcode) < 1:
                print("You didn't enter a zipcode")
                time.sleep(1.5)

            else:
                print("Error invalid input")
                time.sleep(1.5)
        while True:
            os.system("cls")

            user_first_name = input("What is only your first name => ")
            if len(user_first_name) >= 3:
                print("Storing . . .")
                time.sleep(1.5)
                for num in tqdm(range(100)):
                    sleep(0.01)
                break

            elif len(user_first_name) < 1:
                print("You didn't enter a first name")
                time.sleep(1.5)

            else:
                print("Error invalid input")
                time.sleep(1.5)

        while True:
            os.system("cls")

            user_last_name = input("What is only your last name => ")
            if len(user_last_name) >= 3:
                print("Storing . . .")
                time.sleep(1.5)
                for num in tqdm(range(100)):
                    sleep(0.01)
                break

            elif len(user_last_name) < 1:
                print("You didn't enter a last name")
                time.sleep(1.5)

            else:
                print("Error invalid input")

        while True:
            os.system("cls")

            user_gmail = input("What is your gmail => ")
            if gmail_sign not in user_gmail:
                print("You didn't enter a gmail")
                time.sleep(1.5)

            elif gmail_sign in user_gmail:
                print("Storing . . .")
                time.sleep(1.5)
                for num in tqdm(range(100)):
                    sleep(0.01)
                break
            else:
                print("Error invalid input")
                time.sleep(1.5)

        while True:
            os.system("cls")

            user_phone = input(
                "What is your phone number, must include - in it => ")
            if phone_sign in user_phone:
                print("Storing . . .")
                time.sleep(1.5)
                for num in tqdm(range(100)):
                    sleep(0.01)
                break

            elif phone_sign not in user_phone:
                print("You didn't enter a phone number")
                time.sleep(1.5)

            else:
                print("Error invalid input")
                time.sleep(1.5)

        while True:
            os.system("cls")

            user_city_state = input("What is your city, state => ")
            if len(user_city_state) > 3:
                print("Storing . . .")
                time.sleep(1.5)
                for num in tqdm(range(100)):
                    sleep(0.01)
                break

            elif len(user_city_state) < 1:
                print("You didn't enter a city, state")
                time.sleep(1.5)

            else:
                print("Error invalid input")
                time.sleep(1.5)

        os.system("cls")

        user_confirmation = input(
            "Did you mistype anything throughout that process => ")
        if user_confirmation.lower() == "yes":
            print("Sending you back . . .")
            time.sleep(1.5)
            for num in tqdm(range(100)):
                sleep(0.01)

        elif user_confirmation.lower() == "no":
            print("Sending you to menu . . .")
            time.sleep(1.5)
            for num in tqdm(range(100)):
                sleep(0.01)
            menu(user_name, user_address, user_gmail, user_city, user_zipcode,
                 user_city_state, user_phone, user_first_name, user_last_name)
            break

        else:
            print("Error invalid input")
            time.sleep(1.5)


def password_security():
    os.system("cls")
    print("""  
 ______   ______     ______     ______     __     __     ______     ______     _____     ______    
/\  == \ /\  __ \   /\  ___\   /\  ___\   /\ \  _ \ \   /\  __ \   /\  == \   /\  __-.  /\  ___\   
\ \  _-/ \ \  __ \  \ \___  \  \ \___  \  \ \ \/ ".\ \  \ \ \/\ \  \ \  __<   \ \ \/\ \ \ \___  \  
 \ \_\    \ \_\ \_\  \/\_____\  \/\_____\  \ \__/".~\_\  \ \_____\  \ \_\ \_\  \ \____-  \/\_____\ 
  \/_/     \/_/\/_/   \/_____/   \/_____/   \/_/   \/_/   \/_____/   \/_/ /_/   \/____/   \/_____/ 
                                                                                                                                                                                           
    """)
    print("""Using the same password more than once is as bad as having the password 123
You should be using the maximum length password whenever possible. For example if gmail has the
maximum character length of 12, your password should be 12 characters long. The longer it is
the longer it will take for someone to crack it. You should also be aware of database leaks.
Checking for your information in database leaks will let you know if you need to change anything.
I recommend you using the password generator this script has.
""")

    user_done = input("Are you done reading (yes/no) => ")

    if user_done.lower() == "yes":
        print("Sending you back to the menu. . .")
        time.sleep(0.6)
        menu()

    elif len(user_done) < 1:
        print("You didn't enter anything. . .")

    elif user_done.lower() == "no":
        print("Please continue to read.")

    else:
        print("Error invalid input")


def understanding_denial_services():
    os.system("cls")
    print("""  
 _____     ______     __   __     __     ______     __            ______     ______      ______     ______     ______     __   __   __     ______     ______    
/\  __-.  /\  ___\   /\ "-.\ \   /\ \   /\  __ \   /\ \          /\  __ \   /\  ___\    /\  ___\   /\  ___\   /\  == \   /\ \ / /  /\ \   /\  ___\   /\  ___\   
\ \ \/\ \ \ \  __\   \ \ \-.  \  \ \ \  \ \  __ \  \ \ \____     \ \ \/\ \  \ \  __\    \ \___  \  \ \  __\   \ \  __<   \ \ \'/   \ \ \  \ \ \____  \ \  __\   
 \ \____-  \ \_____\  \ \_\\"\_\  \ \_\  \ \_\ \_\  \ \_____\     \ \_____\  \ \_\       \/\_____\  \ \_____\  \ \_\ \_\  \ \__|    \ \_\  \ \_____\  \ \_____\ 
  \/____/   \/_____/   \/_/ \/_/   \/_/   \/_/\/_/   \/_____/      \/_____/   \/_/        \/_____/   \/_____/   \/_/ /_/   \/_/      \/_/   \/_____/   \/_____/ 
                                                                                                                                                                

    """)


def choosing_passwords():
    os.system("cls")
    print("""  
 ______     __  __     ______     ______     ______     __     __   __     ______        ______   ______     ______     ______     __     __     ______     ______     _____     ______    
/\  ___\   /\ \_\ \   /\  __ \   /\  __ \   /\  ___\   /\ \   /\ "-.\ \   /\  ___\      /\  == \ /\  __ \   /\  ___\   /\  ___\   /\ \  _ \ \   /\  __ \   /\  == \   /\  __-.  /\  ___\   
\ \ \____  \ \  __ \  \ \ \/\ \  \ \ \/\ \  \ \___  \  \ \ \  \ \ \-.  \  \ \ \__ \     \ \  _-/ \ \  __ \  \ \___  \  \ \___  \  \ \ \/ ".\ \  \ \ \/\ \  \ \  __<   \ \ \/\ \ \ \___  \  
 \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\  \/\_____\  \ \_\  \ \_\\"\_\  \ \_____\     \ \_\    \ \_\ \_\  \/\_____\  \/\_____\  \ \__/".~\_\  \ \_____\  \ \_\ \_\  \ \____-  \/\_____\ 
  \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_/   \/_/ \/_/   \/_____/      \/_/     \/_/\/_/   \/_____/   \/_____/   \/_/   \/_/   \/_____/   \/_/ /_/   \/____/   \/_____/ 
                                                                                                                                                                                           

    """)


def understanding_botnets():
    os.system("cls")
    print("""
 ______     ______     ______   __   __     ______     ______   ______    
/\  == \   /\  __ \   /\__  _\ /\ "-.\ \   /\  ___\   /\__  _\ /\  ___\   
\ \  __<   \ \ \/\ \  \/_/\ \/ \ \ \-.  \  \ \  __\   \/_/\ \/ \ \___  \  
 \ \_____\  \ \_____\    \ \_\  \ \_\\"\_\  \ \_____\    \ \_\  \/\_____\ 
  \/_____/   \/_____/     \/_/   \/_/ \/_/   \/_____/     \/_/   \/_____/ 
                                                                                                                                   
    """)


def protection_against_sniffing():
    while True:
        os.system("cls")
        print("""  
    ______   ______     ______     __  __     ______     ______      ______     __   __     __     ______   ______   __     __   __     ______    
    /\  == \ /\  __ \   /\  ___\   /\ \/ /    /\  ___\   /\__  _\    /\  ___\   /\ "-.\ \   /\ \   /\  ___\ /\  ___\ /\ \   /\ "-.\ \   /\  ___\   
    \ \  _-/ \ \  __ \  \ \ \____  \ \  _"-.  \ \  __\   \/_/\ \/    \ \___  \  \ \ \-.  \  \ \ \  \ \  __\ \ \  __\ \ \ \  \ \ \-.  \  \ \ \__ \  
     \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_____\    \ \_\     \/\_____\  \ \_\\"\_\  \ \_\  \ \_\    \ \_\    \ \_\  \ \_\\"\_\  \ \_____\ 
      \/_/     \/_/\/_/   \/_____/   \/_/\/_/   \/_____/     \/_/      \/_____/   \/_/ \/_/   \/_/   \/_/     \/_/     \/_/   \/_/ \/_/   \/_____/ 
                                                                                                                                                

        """)
        print("""
            Packet sniffing can be used against you at any time. In order to prevent this, use a vpn
            One of the reasons that people packet sniff, is to find information on someone
            If they sniff the data that you put out there, they can find information like
            Emails, Passwords, Read conversations, Gather credit card information etc.
            In order to prevent this from happening to you, You must use a vpn
            and go on websites that have https, but by far the best is using a vpn
            A vpn routes all of your data in a encrypted network.
            Using a Free vpn is better than using no vpn.
        """)
        user_done = input("Are you done reading => ")
        if user_done.lower() == "yes":
            print("Sending you back to the menu . . .")
            time.sleep(1.5)
            break

        elif len(user_done) < 1:
            print("You didn't enter anything")
            time.sleep(1.5)

        elif user_done.lower() == "no":
            print("Continue reading")
            time.sleep(1.5)

        else:
            print("Error invalid input")
            time.sleep(1.5)


def password_generator():
    while True:
        os.system("cls")
        chars = "abcdefghijklmnopqrstuvwxyz12345678910!@#$%^&*()"

        how_many = int(input("How many passwords do you want => "))
        user_input = int(input("How long do you want the password to be => "))

        for x in range(how_many):
            password = " "

            for i in range(user_input):
                password += random.choice(chars)
            print(password)

        user_done = input(
            "Are you done writing down a password on a piece of paper => ")

        if user_done.lower() == "yes":
            do_you = input("Do you want to use it again => ")
            if do_you.lower() == "yes":
                print("Ok")
                time.sleep(1.5)

            elif do_you.lower() == "no":
                print("Sending you back to staying safe . . .")
                time.sleep(1.5)
                break

            elif len(do_you) < 1:
                print("You didn't enter any option")
                time.sleep(1.5)

            else:
                print("Error invalid input")
                time.sleep(1.5)

        elif user_done.lower() == "no":
            print("Please write it down and then type")
            time.sleep(1.5)

        elif len(user_done) < 1:
            print("You didn't enter any option")
            time.sleep(1.5)

        else:
            print("Error invalid input")
            time.sleep(1.5)


def staying_safe(user_name, user_address, user_gmail, user_city, user_zipcode, user_city_state, user_phone, user_first_name, user_last_name):
    while True:
        os.system("cls")
        print(r"""
 ______     ______   ______     __  __     __     __   __     ______        ______     ______     ______   ______    
/\  ___\   /\__  _\ /\  __ \   /\ \_\ \   /\ \   /\ "-.\ \   /\  ___\      /\  ___\   /\  __ \   /\  ___\ /\  ___\   
\ \___  \  \/_/\ \/ \ \  __ \  \ \____ \  \ \ \  \ \ \-.  \  \ \ \__ \     \ \___  \  \ \  __ \  \ \  __\ \ \  __\   
 \/\_____\    \ \_\  \ \_\ \_\  \/\_____\  \ \_\  \ \_\\"\_\  \ \_____\     \/\_____\  \ \_\ \_\  \ \_\    \ \_____\ 
  \/_____/     \/_/   \/_/\/_/   \/_____/   \/_/   \/_/ \/_/   \/_____/      \/_____/   \/_/\/_/   \/_/     \/_____/ 
                                                                                                         
    I have combined all of my knowledge, and gathered information that I think is useful from actual Experts that work for companies, and put it into this option

                                                                    OPTIONS:
                                                                [1]Password Security
                                                                [2]Understanding Denial Of Service Attacks
                                                                [3]Choosing Passwords
                                                                [4]Understanding Botnets
                                                                [5]Protecting Yourself Against Sniffing
                                                                [6]Menu  
                                                                [7]PasswordGenerator
                                                    
    """)

        user_staying_safe = int(input("Enter a option => "))
        if user_staying_safe == 1:
            print("Sending you to Password Security")
            time.sleep(1.5)
        elif user_staying_safe < 1:
            print("You didn't enter any option")
            time.sleep(1.5)
        elif user_staying_safe == 2:
            print("Sending you to Understanding Denial Of Service Attacks")
            time.sleep(1.5)
        elif user_staying_safe == 3:
            print("Sending you to Choosing Passwords")
            time.sleep(1.5)
        elif user_staying_safe == 4:
            print("Sending you to Understanding Botnets")
            time.sleep(1.5)
        elif user_staying_safe == 5:
            print("Sending you to Protecting Yourself Against Sniffing")
            time.sleep(1.5)
            protection_against_sniffing()

        elif user_staying_safe == 6:
            print("Sending you back to menu . . .")
            time.sleep(1.5)
            menu(user_name, user_address, user_gmail, user_city, user_zipcode,
                 user_city_state, user_phone, user_first_name, user_last_name)
            break

        elif user_staying_safe == 7:
            print("Sending you to password generator . . .")
            time.sleep(1.5)
            password_generator()

        else:
            print("Error invalid input")
            time.sleep(1.5)


def familytree_now(user_name, user_address, user_gmail, user_city, user_zipcode, user_city_state, user_phone, user_first_name, user_last_name):
    os.system('cls')
    print(Fore.LIGHTGREEN_EX + """
 ______   ______     __    __     __     __         __  __     ______   ______     ______     ______    
/\  ___\ /\  __ \   /\ "-./  \   /\ \   /\ \       /\ \_\ \   /\__  _\ /\  == \   /\  ___\   /\  ___\   
\ \  __\ \ \  __ \  \ \ \-./\ \  \ \ \  \ \ \____  \ \____ \  \/_/\ \/ \ \  __<   \ \  __\   \ \  __\   
 \ \_\    \ \_\ \_\  \ \_\ \ \_\  \ \_\  \ \_____\  \/\_____\    \ \_\  \ \_\ \_\  \ \_____\  \ \_____\ 
  \/_/     \/_/\/_/   \/_/  \/_/   \/_/   \/_____/   \/_____/     \/_/   \/_/ /_/   \/_____/   \/_____/ 
                                                                                                        
""")
    print(Fore.RESET)
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(
        options=options)
    driver.get("https://www.familytreenow.com")
    print(driver.title)
    driver.implicitly_wait(10)  # seconds
    family_first_name = driver.find_element_by_id("First")
    family_first_name.send_keys(user_first_name)
    family_last_name = driver.find_element_by_id("Last")
    family_last_name.send_keys(user_last_name)
    family_city = driver.find_element_by_id("CityStateZip")
    family_city.send_keys(user_city_state)
    driver.find_element_by_xpath(
        "/html/body/div[3]/div[1]/div[1]/div/form/div/div/div/div[4]/button").send_keys(Keys.ENTER)
    time.sleep(1.5)
    browser = webbrowser.get()
    browser.open_new(driver.current_url)
    family_tree_do = input("Do you see your information => ")
    if family_tree_do.lower() == "yes":
        print(Fore.LIGHTGREEN_EX + "<========Ok========>")
        print("I will now take you to the removal page")
        print(Fore.RESET)
        driver.get("https://www.familytreenow.com/optout")
        driver.implicitly_wait(10)  # seconds
        family_opt = driver.find_element_by_id("Email")
        family_opt.send_keys(user_gmail)

        os.sytem('cls')
        family_recaptcha = input(
            "Complete the recaptcha then type [yes] => ")
        if family_recaptcha.lower() == 'yes':
            print(Fore.LIGHTGREEN_EX + "<========Ok========>")
            print(Fore.RESET)
            driver.find_element_by_xpath(
                "/html/body/div[3]/div[1]/div/form/button").click()
            opt_out_family = driver.find_element_by_id("First")
            opt_out_family.send_keys(user_first_name)
            opt_out_last = driver.find_element_by_id("Last")
            opt_out_last.send_keys(user_last_name)
            opt_out_city = driver.find_element_by_id("CityStateZip")
            opt_out_city.send_keys(user_city_state)
            driver.find_element_by_xpath(
                '//*[@id="criteriaForm"]/form/div[5]/div/button').click()
            user_input = input("Click on your record, and then type [yes] =>")
            if user_input.lower() == 'yes':
                os.system('cls')
                print(Fore.LIGHTGREEN_EX + "<=======Ok=======>")
                print(Fore.RESET)
                driver.find_element_by_xpath(
                    "/html/body/div[3]/div[1]/div[2]/div[3]/div/div[1]/div/a").click()
                print("Go to your gmail, and follow the directions from the link")
                print("I will now take you back to the menu of the program")
                time.sleep(2)
                menu(user_name, user_address, user_gmail, user_city, user_zipcode,
                     user_city_state, user_phone, user_first_name, user_last_name)

            elif user_input.lower() == 'no':
                print("Good Bye ")
                time.sleep(2)
                driver.quit()
                sys.exit()
            else:
                print("Error invlid input")

        elif family_recaptcha.lower() == 'no':
            print("Good Bye Then")
            time.sleep(2)
            driver.quit()
            sys.exit()

        else:
            print("Error Invalid Input")

    elif family_tree_do.lower() == 'no':
        print("You have reached the end of the free version of the program")
        print("I will now take you back to the menu")
        driver.quit()
    else:
        print("Error invalid input")


def truepeoplesearch(user_name, user_address, user_gmail, user_city, user_zipcode, user_city_state, user_phone, user_first_name, user_last_name):
    os.system('cls')
    print(Fore.LIGHTCYAN_EX + """

.___________..______       __    __   _______ .______    _______   ______   .______    __       _______ 
|           ||   _  \     |  |  |  | |   ____||   _  \  |   ____| /  __  \  |   _  \  |  |     |   ____|
`---|  |----`|  |_)  |    |  |  |  | |  |__   |  |_)  | |  |__   |  |  |  | |  |_)  | |  |     |  |__   
    |  |     |      /     |  |  |  | |   __|  |   ___/  |   __|  |  |  |  | |   ___/  |  |     |   __|  
    |  |     |  |\  \----.|  `--'  | |  |____ |  |      |  |____ |  `--'  | |  |      |  `----.|  |____ 
    |__|     | _| `._____| \______/  |_______|| _|      |_______| \______/  | _|      |_______||_______|
                                                                                                        
                                                                      
""")
    print(Fore.RESET)
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(
        options=options)
    driver.get("https://www.truepeoplesearch.com")
    print(driver.title)
    driver.implicitly_wait(10)  # seconds
    name_ = driver.find_element_by_id("id-d-n")
    name_.send_keys(user_name)
    zipcode_ = driver.find_element_by_id("id-d-loc-name")
    zipcode_.send_keys(user_zipcode)
    driver.find_element_by_id("btnSubmit-d-n").send_keys(Keys.ENTER)
    time.sleep(1.5)
    browser = webbrowser.get()
    browser.open_new(driver.current_url)
    do_you = input("\nDo you see your information => ")
    if do_you.lower() == "yes":
        print(Fore.LIGHTCYAN_EX + "<==========Ok=========>")
        print("I will now send you to the removal process")
        print(Fore.RESET)
        os.system('cls')
        driver = webdriver.Firefox()
        driver.get("https://www.truepeoplesearch.com/removal")
        driver.implicitly_wait(10)  # seconds
        driver_email_link = driver.find_element_by_id("Email")
        driver_email_link.send_keys(user_gmail)
        driver.find_element_by_id("AgreeTerms").click()
        user_recaptcha = input("Complete The recaptcha then type [yes] => ")
        if user_recaptcha.lower() == 'yes':
            print(Fore.LIGHTCYAN_EX + '<==========Ok==========>')
            print(Fore.RESET)
            os.system('cls')
            driver.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div[2]/div/form/button').click()
            driver.implicitly_wait(10)  # seconds
            removal_name = driver.find_element_by_id("id-d-n")
            removal_name.send_keys(user_name)
            removal_city = driver.find_element_by_id("id-d-loc-name")
            removal_city.send_keys(user_city_state)
            driver.find_element_by_id("btnSubmit-d-n").click()
            print("Find your record, and click view details")
            print("In order for me to click the button, I must be able to see it")
            print(
                "Scroll all the way down until you see [Remove this record]")
            remove_record = input(
                "Have you scrolled down to the remove record option [yes], [no] => ")
            if remove_record.lower() == 'yes':
                print(Fore.LIGHTCYAN_EX + "<========Ok========>")
                print(Fore.RESET)
                os.system('cls')
            elif remove_record.lower() == 'no':
                print("Please do so")
                another_chance = input("Have you done so now => ")
                if another_chance.lower() == 'yes':
                    print(Fore.LIGHTCYAN_EX + "<========Ok========>")
                    print(Fore.RESET)
                    driver.find_element_by_id("btnSubmit-d-n").click()
                    print("Good bye")
                    time.sleep(2)
                    sys.exit()
            else:
                print("Error Invalid Option")

            user_removal_process = input(
                "Type [yes] once you have clicked view details => ")
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/div[2]/div[1]/div[21]/div/a").click()
            print("They have now sent a link to your gmail")
            time.sleep(2)
            os.system('cls')
            print("Click on the link, and follow the directions they give")
            print("You Will Want To Check On These Websites every month or so")
            print("They like to readd information occasionally")
            print("The program will now return to the menu")
            time.sleep(2)
            menu(user_name, user_address, user_gmail, user_city, user_zipcode,
                 user_city_state, user_phone, user_first_name, user_last_name)

        elif user_recaptcha.lower() == 'no':
            print("Good Bye")
            driver.quit()
            sys.exit()

    elif do_you.lower() == "no":
        print(Fore.LIGHTCYAN_EX + "Next website")
        print(Fore.RESET)
        time.sleep(1.0)

    else:
        print(Fore.LIGHTCYAN_EX + "Error Invalid Input")
        print(Fore.RESET)


def thatsthem(user_name, user_address, user_gmail, user_city, user_zipcode, user_city_state, user_phone, user_first_name, user_last_name):
    os.system('cls')
    print(Fore.LIGHTRED_EX + """
 ______   __  __     ______     ______   ______     ______   __  __     ______     __    __    
/\__  _\ /\ \_\ \   /\  __ \   /\__  _\ /\  ___\   /\__  _\ /\ \_\ \   /\  ___\   /\ "-./  \   
\/_/\ \/ \ \  __ \  \ \  __ \  \/_/\ \/ \ \___  \  \/_/\ \/ \ \  __ \  \ \  __\   \ \ \-./\ \  
   \ \_\  \ \_\ \_\  \ \_\ \_\    \ \_\  \/\_____\    \ \_\  \ \_\ \_\  \ \_____\  \ \_\ \ \_\ 
    \/_/   \/_/\/_/   \/_/\/_/     \/_/   \/_____/     \/_/   \/_/\/_/   \/_____/   \/_/  \/_/ 
                                                                                               
""")
    print(Fore.RESET)
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(
        options=options)
    driver.get("https://thatsthem.com")
    print(driver.title)
    driver.implicitly_wait(10)  # seconds
    thats_them_name = driver.find_element_by_id("fullName")
    thats_them_name.send_keys(user_name)
    thats_them_address = driver.find_element_by_id("address")
    thats_them_address.send_keys(user_address)
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/main/section[1]/div/form/div/button').send_keys(Keys.ENTER)
    time.sleep(1.5)
    browser = webbrowser.get()
    browser.open_new(driver.current_url)
    thatsthem_confirmation = input("Do you see your information => ")
    if thatsthem_confirmation.lower() == 'yes':
        print(Fore.LIGHTRED_EX + "<==========Ok==========>")
        print("I will now take you to the removal page")
        print(Fore.RESET)
        os.system('cls')
        driver = webdriver.Firefox()
        driver.get("https://thatsthem.com/optout")
        driver.implicitly_wait(10)  # seconds
        thatsthem_optout_name = driver.find_element_by_xpath(
            "/html/body/div[2]/div/main/section[3]/form/div/input[1]")
        thatsthem_optout_name.send_keys(user_name)
        thatsthem_optout_email = driver.find_element_by_xpath(
            "/html/body/div[2]/div/main/section[3]/form/div/input[2]")
        thatsthem_optout_email.send_keys(user_gmail)
        thatsthem_optout_phone = driver.find_element_by_xpath(
            "/html/body/div[2]/div/main/section[3]/form/div/input[3]")
        thatsthem_optout_phone.send_keys(user_phone)
        thatsthem_optout_street = driver.find_element_by_xpath(
            "/html/body/div[2]/div/main/section[3]/form/div/input[4]")
        thatsthem_optout_street.send_keys(user_address)
        thatsthem_optout_city = driver.find_element_by_xpath(
            "/html/body/div[2]/div/main/section[3]/form/div/input[5]")
        thatsthem_optout_city.send_keys(user_city)
        print("You will have to select your state manually")
        thatsthem_optout_state = input(
            "Type [yes] once you have selected your state => ")
        if thatsthem_optout_state.lower() == 'yes':
            print(Fore.LIGHTRED_EX + "<==========Ok=========>")
            print(Fore.RESET)
            os.system('cls')
            thatsthem_optout_zipcode = driver.find_element_by_xpath(
                "/html/body/div[2]/div/main/section[3]/form/div/input[6]")
            thatsthem_optout_zipcode.send_keys(user_zipcode)
            driver.find_element_by_id("contactUpdates").click()
            driver.find_element_by_id("theftProtection").click()
            print("You will now need to complete the recaptcha")
            thatsthem_recaptcha = input(
                "Did you complete the recaptcha [yes] [no] => ")
            if thatsthem_recaptcha.lower() == 'yes':
                print(Fore.LIGHTRED_EX + "<==========Ok==========>")
                print(Fore.RESET)
                os.system('cls')
                driver.find_element_by_xpath(
                    "/html/body/div[2]/div/main/section[3]/form/div/button").click()
                print("They take forever to remove records off their website")
                print("So dont expect it to be gone immediately")
                print("I will now take you back to the menu")
                time.sleep(3)
                driver.quit()
                menu(user_name, user_address, user_gmail, user_city, user_zipcode,
                     user_city_state, user_phone, user_first_name, user_last_name)
            elif thatsthem_recaptcha == 'no':
                print("Complete the recaptcha")
                thats_them_redemption = input(
                    "Did you complete the recaptcha before typing [yes] [no] => ")
                if thats_them_redemption.lower() == 'yes':
                    print(Fore.LIGHTRED_EX + "<==========Ok==========>")
                    print(Fore.RESET)
                    driver.find_element_by_xpath(
                        "/html/body/div[2]/div/main/section[3]/form/div/button").click()
                    print("They take forever to remove records of there website")
                    print("So dont expect it to be gone immediately")
                    print("I will now take you back to the menu")
                    time.sleep(2)
                    menu(user_name, user_address, user_gmail, user_city, user_zipcode,
                         user_city_state, user_phone, user_first_name, user_last_name)

            else:
                print(Fore.LIGHTRED_EX + "Error Invalid Option")
                print(Fore.RESET)

        elif thatsthem_optout_state.lower() == 'no':
            print(Fore.LIGHTRED_EX +
                  "The program will close now since you dont want to follow simple directions")
            print(Fore.RESET)
            time.sleep(3)
            sys.exit()

        else:
            print(Fore.LIGHTRED_EX + "Error Invalid Option")
            print(Fore.RESET)

    elif thatsthem_confirmation.lower() == 'no':
        print(Fore.LIGHTRED_EX +
              "Next website")
        print(Fore.RESET)
        time.sleep(1.0)

    else:
        print(Fore.LIGHTRED_EX + "Error Invalid Option")
        print(Fore.RESET)


def information_checker(user_name, user_address, user_gmail, user_city, user_zipcode, user_city_state, user_phone, user_first_name, user_last_name):
    truepeoplesearch(user_name, user_address, user_gmail, user_city, user_zipcode,
                     user_city_state, user_phone, user_first_name, user_last_name)
    thatsthem(user_name, user_address, user_gmail, user_city, user_zipcode,
              user_city_state, user_phone, user_first_name, user_last_name)
    familytree_now(user_name, user_address, user_gmail, user_city, user_zipcode,
                   user_city_state, user_phone, user_first_name, user_last_name)


def menu(user_name, user_address, user_gmail, user_city, user_zipcode, user_city_state, user_phone, user_first_name, user_last_name):
    while True:
        os.system("cls")
        print(r"""
███╗░░██╗░█████╗░██████╗░░█████╗░██╗░░██╗
████╗░██║██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝
██╔██╗██║██║░░██║██║░░██║██║░░██║░╚███╔╝░
██║╚████║██║░░██║██║░░██║██║░░██║░██╔██╗░
██║░╚███║╚█████╔╝██████╔╝╚█████╔╝██╔╝╚██╗
╚═╝░░╚══╝░╚════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝

                                 OPTIONS:
                             [1]Information Checker
                             [2]Gmail Pwned
                             [3]Staying Safe
                             [4]Help""")
        user_menu = int(input("Enter a option => "))
        if user_menu == 1:
            print("Sending you to Information Checker . . .")
            time.sleep(1.5)
            for num in tqdm(range(100)):
                sleep(0.01)
            information_checker(user_name, user_address, user_gmail, user_city, user_zipcode,
                                user_city_state, user_phone, user_first_name, user_last_name)

        elif user_menu == 2:
            print("Sending you to Gmail Pwned")
            time.sleep(1.5)
            for num in tqdm(range(100)):
                sleep(0.01)
            break

        elif user_menu == 3:
            print("Sending you to Staying Safe . . .")
            time.sleep(1.5)
            for num in tqdm(range(100)):
                sleep(0.01)
            staying_safe(user_name, user_address, user_gmail, user_city, user_zipcode,
                         user_city_state, user_phone, user_first_name, user_last_name)

        elif user_menu == 4:
            print("Sending you to Help . . .")
            time.sleep(1.5)
            for num in tqdm(range(100)):
                sleep(0.01)
            break

        else:
            print("Error invalid input")
            time.sleep(1.5)


loading()
questions()
