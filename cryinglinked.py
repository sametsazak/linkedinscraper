from selenium import webdriver
from time import sleep
import csv
import cmd
from selenium.webdriver.common.keys import Keys
from terminaltables import AsciiTable
import os
import re

intro = '''\033[1m\033[91m 


 ██████╗██████╗ ██╗   ██╗██╗███╗   ██╗ ██████╗ ██╗     ██╗███╗   ██╗██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗╚██╗ ██╔╝██║████╗  ██║██╔════╝ ██║     ██║████╗  ██║██║ ██╔╝██╔════╝██╔══██╗
██║     ██████╔╝ ╚████╔╝ ██║██╔██╗ ██║██║  ███╗██║     ██║██╔██╗ ██║█████╔╝ █████╗  ██║  ██║
██║     ██╔══██╗  ╚██╔╝  ██║██║╚██╗██║██║   ██║██║     ██║██║╚██╗██║██╔═██╗ ██╔══╝  ██║  ██║
╚██████╗██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝███████╗██║██║ ╚████║██║  ██╗███████╗██████╔╝
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═════╝ 
                                                                                            

\033[0m
            Version    : 1.0
            Author     : Samet Sazak
            Twitter    : @belleveben
            Github     : @sametsazak
            Note       : Get chromeweb driver with the same directory and pip3 install -r req.txt
 \033[1m\033[94m[*]\033[0m You can use "help" command for access help section\033[0m.
'''

class CryingLinkedCmd(cmd.Cmd):

    global helpText
    helpText = "Commands"
    def do_info(self, line):
        print("\n \033[1m\033[94m[*]\033[0m Module Info\033[0m\n")
        print("+ MODULE INFO")
        print("\n \033[1m\033[94m[*]\033[0m Module Options\033[0m")
        optionsValues = [
            ["Modules", "Description"],
            ["Generate CSV File", "Linkedin Username/Email Required"],
            ["Generate Emails", "Linkedin Email generator"],
        ]
        optTable = AsciiTable(optionsValues)
        optTable.outer_border = False
        optTable.inner_column_border = False
        optTable.justify_columns[1] = "center"
        print("\n" + optTable.table + "\n")

    def __init__(self, intro=intro, prompt="\033[1mCryingLinked > \033[0m"):
        cmd.Cmd.__init__(self)
        self.intro = intro
        self.prompt = prompt
        self.doc_header = helpText
        global moduleName
        moduleName = ""

    def do_list(self, line):
        optionsValues = [
            ["ID", "Module", "Description"],
            ["1", "Linkedin Scraper to CSV", "Generate a CSV File which includes given company employees"],
            ["2", "Generate Emails", "Generate Email from given pattern"],
        ]
        optTable = AsciiTable(optionsValues)
        optTable.outer_border = False
        optTable.inner_column_border = True
        print("\n" + optTable.table + "\n")

    def do_use(self, line):
        try:
            global moduleName
            moduleName = line.split()[0]
        except IndexError:
            print("\n \033[1m\033[91m[!]\033[0m You need to give a valid payload id.\033[0m\n")
        if moduleName == "1":
            moduleName = "generateCSV"
            generateCSVs = generateCSV()
            generateCSVs.cmdloop()
        elif moduleName == "2":
            moduleName = "genEmailMain"
            genEmailMains = genEmailMain()
            genEmailMains.cmdloop()        
        else:
            pass

    def do_exit(self, line):
        print(" \n \033[1m\033[94m[*]\033[0m Cya!\033[0m\n")
        return True

    def emptyline(self):
        pass

    def help_list(self):
        print("List available payloads")

    def help_use(self):
        print("Use specific . Syntax: use <id> ")

    def help_exit(self):
        print("Exit CryingLinked")

    def help_info(self):
        print("Show module options and parameter values")

    def help_set(self):
        print("Set value to parameter. Syntax: set <parameter> <value>")

    def help_generate(self):
        print("Run module with current values.")

    def help_back(self):
        print("Back to CryingLinked main menu.")



class generateCSV(CryingLinkedCmd):
    global linkedin_password
    global linkedin_username
    global linkedin_url
    global linkedin_filename
    global linkedin_page
    def __init__(self):
        CryingLinkedCmd.__init__(
            self, intro=" \n\n \033[1m\033[91m This module generates a CSV file which includes Employee Name and Employee Title from given company.\033[0m\n", prompt="\033[1mCryingLinked > generateCSV \033[0m")

    def do_info(self, line):
        print("\n \033[1m\033[94m[*]\033[0m Module Info\033[0m\n")
        print(''' This module can be used to generate CSV file from given company.''')
        print("\n \033[1m\033[94m[*]\033[0m Module Options\033[0m")
        optionsValues = [
            ["Set options", "Description"],
            ["Username", "Linkedin Username/Email Required"],
            ["Password", "Linkedin Passsword Required"],
            ["URL", "Linkedin Company Page Required, Example : https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%22162479%22%5D"],
            ["Page", "How many pages you want to scrape? Max. 100"],
        ]
        optTable = AsciiTable(optionsValues)
        optTable.outer_border = False
        optTable.inner_column_border = False
        optTable.justify_columns[1] = "center"
        print("\n" + optTable.table + "\n")

    def do_set(self, line):
        global linkedin_username
        global linkedin_password
        global linkedin_page
        global linkedin_url
        try:
            if line.split()[0].upper().lower() == "username":
                try:
                    linkedin_username= line.split()[1]
                    print("Username is set=> " + line.split()[1])
                except:
                    print("Please enter a valid email")
            elif line.split()[0].upper().lower() == "password":
                try:
                    linkedin_password = line.split()[1]
                    print("Password is set=> " + line.split()[1])
                except:
                    print("Please enter a valid password")
            elif line.split()[0].upper().lower() == "page":
                try:
                    linkedin_page = line.split()[1]
                    print("Page is set=> " + line.split()[1])
                except:
                     print("Please enter a valid page")
            elif line.split()[0].upper().lower() == "url":
                try:
                    linkedin_url = line.split()[1]
                    print("URL is set => " + line.split()[1])    
                except:
                    print("Please enter a valid email")                         
            else:
                print("\n \033[1m\033[91m[!]\033[0m Please enter valid value.\n")

        except:
            print("Something went wrong, try again.")

    def do_generate(self, line):
        if None in (linkedin_password, linkedin_username, linkedin_page, linkedin_url):
            print("\n \033[1m\033[91m[!]\033[0m Please check your values.\n")
        else:
            print("\n \033[1m\033[94m[*]\033[0m Generating CSV...\n")
            fetch = InformationGather(linkedin_url, linkedin_username, linkedin_password, linkedin_page)
            fetch.GatherByLinkedin()
    def do_back(self, line):
        return True

    def do_exit(self, line):
        return True

class InformationGather:
    def __init__(self, url, username, password, page):
        self.url = url
        self.username = username
        self.password = password
        self.page = page
    def GatherByLinkedin(self):
        current_working_directory = os.getcwd()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(current_working_directory + '/chromedriver', options=options)
        driver.get('https://www.linkedin.com/nhome')
        driver.find_element_by_id('login-email').send_keys(self.username)
        driver.find_element_by_id ('login-password').send_keys(self.password)
        driver.find_element_by_id('login-submit').click()
        driver.get(self.url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        names = driver.find_elements_by_xpath(("//span[@class='name actor-name']"))
        title = driver.find_elements_by_xpath(("//p[@class='subline-level-1 t-14 t-black t-normal search-result__truncate']"))
        with open('Output.csv', 'w') as csvfile:
            print("\n \033[1m\033[94m[*]\033[0m Fetching Started...\n")
            fieldnames = ['name', 'title']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for k in range(2,int(self.page)):
                driver.get('{0}&page={1}'.format(self.url, k))
                sleep(2)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(0.5)
                names = driver.find_elements_by_xpath(("//span[@class='name actor-name']"))
                title = driver.find_elements_by_xpath(("//p[@class='subline-level-1 t-14 t-black t-normal search-result__truncate']"))
                for i in range(0,len(names)):
                    writer.writerow({'name': names[i].text, 'title': title[i].text})
        print("\n \033[1m\033[94m[+]\033[0m Fetching Finished!...\n")


class genEmailMain(cmd.Cmd):
    intro = " \033[1m\033[94m[*]\033[0m Generate Emails Module \033[0m."
    global helpText
    helpText = "Commands"
    def do_info(self, line):
        print("\n \033[1m\033[94m[*]\033[0m Module Info\033[0m\n")
        print("+ MODULE INFO")
        print("\n \033[1m\033[94m[*]\033[0m Module Options\033[0m")
        optionsValues = [
            ["ID", "Pattern", "Description"],
            ["1", "(firstname).(surname)@company.com", "Generate Emails given pattern"],
            ["2", "(surname).(firstname)@company.com", "Generate Emails given pattern"],
            ["3", "(s).(firstname)@company.com", "(s) is the first character of surname"],
            ["4", "(firstname).(s)@company.com", "(s) is the first character of surname"],
            ["5", "(f).(surname)@company.com", "(f) is the first character of firstname"],
            ["6", "(surname).(f)@company.com", "(f) is the first character of firstname"],
            ["7", "(firstname)(surname)@company.com", "Generate Emails given pattern"],
            ["8", "(surname)(firstname)@company.com", "Generate Emails given pattern"],
        ]    
        optTable = AsciiTable(optionsValues)
        optTable.outer_border = False
        optTable.inner_column_border = False
        optTable.justify_columns[1] = "center"
        print("\n" + optTable.table + "\n")
    def __init__(self, intro=intro, prompt="\033[1mCryingLinked > Generate Emails > \033[0m"):
        cmd.Cmd.__init__(self)
        self.intro = intro
        self.prompt = prompt
        self.doc_header = helpText
        global moduleName
        moduleName = ""

    def do_list(self, line):
        optionsValues = [
            ["ID", "Pattern", "Description"],
            ["1", "(firstname).(surname)@company.com", "Generate Emails given pattern"],
            ["2", "(surname).(firstname)@company.com", "Generate Emails given pattern"],
            ["3", "(s).(firstname)@company.com", "(s) is the first character of surname"],
            ["4", "(firstname).(s)@company.com", "(s) is the first character of surname"],
            ["5", "(f).(surname)@company.com", "(f) is the first character of firstname"],
            ["6", "(surname).(f)@company.com", "(f) is the first character of firstname"],
            ["7", "(firstname)(surname)@company.com", "Generate Emails given pattern"],
            ["8", "(surname)(firstname)@company.com", "Generate Emails given pattern"],

        ]
        optTable = AsciiTable(optionsValues)
        optTable.outer_border = False
        optTable.inner_column_border = True
        print("\n" + optTable.table + "\n")

    def do_use(self, line):
        try:
            global moduleName
            moduleName = line.split()[0]
        except IndexError:
            print("\n \033[1m\033[91m[!]\033[0m You need to give a valid module id.\033[0m\n")
        if moduleName == "1":
            generateEmailx = generateEmails(1)
            generateEmailx.cmdloop()
        elif moduleName == "2":
            generateEmailx = generateEmails(2)
            generateEmailx.cmdloop()
        elif moduleName == "3":
            generateEmailx = generateEmails(3)
            generateEmailx.cmdloop()   
        elif moduleName == "4":
            generateEmailx = generateEmails(4)
            generateEmailx.cmdloop()               
        elif moduleName == "5":
            generateEmailx = generateEmails(5)
            generateEmailx.cmdloop()  
        elif moduleName == "6":
            generateEmailx = generateEmails(5)
            generateEmailx.cmdloop() 
        elif moduleName == "7":
            generateEmailx = generateEmails(7)
            generateEmailx.cmdloop() 
        elif moduleName == "8":
            generateEmailx = generateEmails(8)
            generateEmailx.cmdloop() 
        else:
            pass

          
    def do_exit(self, line):
        print(" \n \033[1m\033[94m[*]\033[0m Cya!\033[0m\n")
        return True

    def emptyline(self):
        pass

    def help_list(self):
        print("List available modules")

    def help_use(self):
        print("Use specific module. Syntax: use <id> ")

    def help_exit(self):
        print("Exit CryingLinked")

    def help_info(self):
        print("Show module options and parameter values")

    def help_set(self):
        print("Set value to parameter. Syntax: set <parameter> <value>")

    def help_generate(self):
        print("Run module with current values.")

    def help_back(self):
        print("Back to CryingLinked main menu.")



class generateEmails(CryingLinkedCmd):
    output_file = None
    domain_adress = None
    file_input = None
    names_1 = []
    names_2 = []
    peopleWithOneName_raw = []
    peopleWithTwoName_raw = []
    maillist_one = []
    def __init__(self, moduleName):
        self.moduleName = moduleName
        CryingLinkedCmd.__init__(
            self, intro=" \n\n \033[1m\033[91m This module generates a Emails with patterns from a CSV file\033[0m\n", prompt="\033[1mCryingLinked > generateEmails \033[0m")

    def do_info(self, line):
        print("\n \033[1m\033[94m[*]\033[0m Module Info\033[0m\n")
        print(''' This module can be used to generate Emails''')
        print("\n \033[1m\033[94m[*]\033[0m Module Options\033[0m")
        optionsValues = [
            ["Set options", "Example"],
            ["Input", "Default: output.csv"],
            ["Output", "Default: Emails.txt"],
            ["Domain", "example.com"],
        ]
        optTable = AsciiTable(optionsValues)
        optTable.outer_border = False
        optTable.inner_column_border = False
        optTable.justify_columns[1] = "center"
        print("\n" + optTable.table + "\n")

    def do_set(self, line):
        try:
            if line.split()[0].upper().lower() == "output":
                try:
                    self.output_file= line.split()[1]
                    print("Output is set=> " + line.split()[1])
                except:
                    print("Please enter a valid output file name")
            elif line.split()[0].upper().lower() == "domain":
                try:
                    self.domain_adress= line.split()[1]
                    print("Domain is set=> " + line.split()[1])
                except:
                    print("Please enter a valid domain adress like 'example.com'")
            elif line.split()[0].upper().lower() == "input":
                try:
                    self.file_input= line.split()[1]
                    print("Input is set=> " + line.split()[1])
                except:
                    print("Please enter a valid file input name")
            else:
                print("\n \033[1m\033[91m[!]\033[0m Please enter valid value.\n")
        except:
            print("Something went wrong, try again.")
    def validate_email(self, email):
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if match == None:
            return False
        else:
            return True

    def do_generate(self, line):
        if self.domain_adress is None:
            self.domain_adress = "example.com"
        if self.file_input is None:
            self.file_input = "Output.csv"
        if self.output_file is None:
            self.output_file = "Emails.txt" 
        self.loadFromCSV()
        if self.moduleName == 1:
            self.pattern1()
        elif self.moduleName == 2:
            self.pattern2()     
        elif self.moduleName == 3:
            self.pattern3()   
        elif self.moduleName == 4:
            self.pattern4()    
        elif self.moduleName == 5:
            self.pattern5()   
        elif self.moduleName == 6:
            self.pattern6()  
        elif self.moduleName == 7:
            self.pattern7()  
        elif self.moduleName == 8:
            self.pattern8()
    def do_back(self, line):
        return True
    def do_exit(self, line):
        return True
    def pattern1(self):
        for i in self.peopleWithOneName_raw:
            name_english = self.replaceWithEnglish(i[0]).lower()
            surname_english = self.replaceWithEnglish(i[1]).lower()
            pattern = "{0}.{1}@{2}".format(name_english, surname_english, self.domain_adress)
            self.maillist_one.append(pattern)
        for i in self.peopleWithTwoName_raw:
            firstname_english = self.replaceWithEnglish(i[0]).lower() # firstname 
            secondname_english = self.replaceWithEnglish(i[1]).lower() ## secondname
            lastname_english = self.replaceWithEnglish(i[2]).lower() # lastname
            pattern = "{0}.{1}@{2}".format(firstname_english, lastname_english, self.domain_adress)
            pattern2 = "{0}.{1}@{2}".format(secondname_english, lastname_english, self.domain_adress)
            self.maillist_one.append(pattern) # generating possible firstname.lastname@company.com
            self.maillist_one.append(pattern2) # generating possible secondname.lastname@company.com
        try:
            with open(self.output_file, 'w', newline='') as csvfile:
                fieldnames = ['email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for i in self.maillist_one:
                    if self.validate_email(i):
                        writer.writerow({'email': i})
                    else:
                        pass
            print("File : {0} generated".format(self.output_file))
        except Exception as e:
            print(e)
            pass
    def pattern2(self):
        for i in self.peopleWithOneName_raw:
            name_english = self.replaceWithEnglish(i[0]).lower()
            surname_english = self.replaceWithEnglish(i[1]).lower()
            pattern = "{1}.{0}@{2}".format(name_english, surname_english, self.domain_adress)
            self.maillist_one.append(pattern)
        for i in self.peopleWithTwoName_raw:
            firstname_english = self.replaceWithEnglish(i[0]).lower() # firstname 
            secondname_english = self.replaceWithEnglish(i[1]).lower() ## secondname
            lastname_english = self.replaceWithEnglish(i[2]).lower() # lastname
            pattern = "{1}.{0}@{2}".format(firstname_english, lastname_english, self.domain_adress)
            pattern2 = "{1}.{0}@{2}".format(secondname_english, lastname_english, self.domain_adress)
            self.maillist_one.append(pattern) # generating possible firstname.lastname@company.com
            self.maillist_one.append(pattern2) # generating possible secondname.lastname@company.com        
        try:
            with open(self.output_file, 'w', newline='') as csvfile:
                fieldnames = ['email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for i in self.maillist_one:
                    if self.validate_email(i):
                        writer.writerow({'email': i})
                    else:
                        pass
            print("File : {0} generated".format(self.output_file))
        except Exception as e:
            print(e)
            pass
    def pattern3(self):
        for i in self.peopleWithOneName_raw:
            name_english = self.replaceWithEnglish(i[0]).lower()
            surname_english = self.replaceWithEnglish(i[1]).lower()
            firstCharacterOfSurname = surname_english[0]
            pattern = "{0}.{1}@{2}".format(name_english, firstCharacterOfSurname, self.domain_adress)
            self.maillist_one.append(pattern)
        for i in self.peopleWithTwoName_raw:
            firstname_english = self.replaceWithEnglish(i[0]).lower() # firstname 
            secondname_english = self.replaceWithEnglish(i[1]).lower() ## secondname
            lastname_english = self.replaceWithEnglish(i[2]).lower() # lastname
            firstCharacterOfLastName = lastname_english[0]
            pattern = "{0}.{1}@{2}".format(firstname_english, firstCharacterOfLastName, self.domain_adress)
            pattern2 = "{0}.{1}@{2}".format(secondname_english, firstCharacterOfLastName, self.domain_adress)
            self.maillist_one.append(pattern) # generating possible firstname.l@company.com
            self.maillist_one.append(pattern2) # generating possible secondname.l@company.com        
        try:
            with open(self.output_file, 'w', newline='') as csvfile:
                fieldnames = ['email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for i in self.maillist_one:
                    if self.validate_email(i):
                        writer.writerow({'email': i})
                    else:
                        pass
            print("File : {0} generated".format(self.output_file))
        except Exception as e:
            print(e)
            pass
    def pattern4(self):
        #["4", "(firstname).(s)@company.com", "(s) is first character of surname"]
        for i in self.peopleWithOneName_raw:
            name_english = self.replaceWithEnglish(i[0]).lower()
            surname_english = self.replaceWithEnglish(i[1]).lower()
            firstCharacterOfLastname = surname_english[0]
            pattern = "{0}.{1}@{2}".format(name_english, firstCharacterOfLastname, self.domain_adress)
            self.maillist_one.append(pattern)
        for i in self.peopleWithTwoName_raw:
            firstname_english = self.replaceWithEnglish(i[0]).lower() # firstname 
            secondname_english = self.replaceWithEnglish(i[1]).lower() ## secondname
            lastname_english = self.replaceWithEnglish(i[2]).lower() # lastname
            firstCharacterOfLastname = lastname_english[0]
            pattern = "{0}.{1}@{2}".format(firstname_english, firstCharacterOfLastname, self.domain_adress)
            pattern2 = "{0}.{1}@{2}".format(secondname_english, firstCharacterOfLastname, self.domain_adress)
            self.maillist_one.append(pattern) # generating possible f.lastname@company.com
            self.maillist_one.append(pattern2) # generating possible s.lastname@company.com        
        try:
            with open(self.output_file, 'w', newline='') as csvfile:
                fieldnames = ['email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for i in self.maillist_one:
                    if self.validate_email(i):
                        writer.writerow({'email': i})
                    else:
                        pass
            print("File : {0} generated".format(self.output_file))
        except Exception as e:
            print(e)
            pass
    def pattern5(self):
        #["5", "(f).(surname)@company.com", "(s) is first character of surname"]
        for i in self.peopleWithOneName_raw:
            name_english = self.replaceWithEnglish(i[0]).lower()
            surname_english = self.replaceWithEnglish(i[1]).lower()
            firstCharacterOfFirstName = name_english[0]
            pattern = "{0}.{1}@{2}".format(firstCharacterOfFirstName, surname_english, self.domain_adress)
            self.maillist_one.append(pattern)
        for i in self.peopleWithTwoName_raw:
            firstname_english = self.replaceWithEnglish(i[0]).lower() # firstname 
            secondname_english = self.replaceWithEnglish(i[1]).lower() ## secondname
            lastname_english = self.replaceWithEnglish(i[2]).lower() # lastname
            firstCharacterOfFirstName = firstname_english[0]
            firstCharacterOfFirstName2 = secondname_english[0]
            pattern = "{0}.{1}@{2}".format(firstCharacterOfFirstName, lastname_english, self.domain_adress)
            pattern2 = "{0}.{1}@{2}".format(firstCharacterOfFirstName2, lastname_english, self.domain_adress)
            self.maillist_one.append(pattern) # generating possible f.lastname@company.com
            self.maillist_one.append(pattern2) # generating possible s.lastname@company.com        
        try:
            with open(self.output_file, 'w', newline='') as csvfile:
                fieldnames = ['email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for i in self.maillist_one:
                    if self.validate_email(i):
                        writer.writerow({'email': i})
                    else:
                        pass
            print("File : {0} generated".format(self.output_file))
        except Exception as e:
            print(e)
            pass
    def pattern6(self):
        for i in self.peopleWithOneName_raw:
            name_english = self.replaceWithEnglish(i[0]).lower()
            surname_english = self.replaceWithEnglish(i[1]).lower()
            firstCharacterOfFirstName = name_english[0]
            pattern = "{1}.{0}@{2}".format(firstCharacterOfFirstName, surname_english, self.domain_adress)
            self.maillist_one.append(pattern)
        for i in self.peopleWithTwoName_raw:
            firstname_english = self.replaceWithEnglish(i[0]).lower() # firstname 
            secondname_english = self.replaceWithEnglish(i[1]).lower() ## secondname
            lastname_english = self.replaceWithEnglish(i[2]).lower() # lastname
            firstCharacterOfFirstName = firstname_english[0]
            firstCharacterOfFirstName2 = secondname_english[0]
            pattern = "{1}.{0}@{2}".format(firstCharacterOfFirstName, lastname_english, self.domain_adress)
            pattern2 = "{1}.{0}@{2}".format(firstCharacterOfFirstName2, lastname_english, self.domain_adress)
            self.maillist_one.append(pattern) # generating possible f.lastname@company.com
            self.maillist_one.append(pattern2) # generating possible s.lastname@company.com        
        try:
            with open(self.output_file, 'w', newline='') as csvfile:
                fieldnames = ['email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for i in self.maillist_one:
                    if self.validate_email(i):
                        writer.writerow({'email': i})
                    else:
                        pass
            print("File : {0} generated".format(self.output_file))
        except Exception as e:
            print(e)
            pass
    def pattern7(self):
        for i in self.peopleWithOneName_raw:
            name_english = self.replaceWithEnglish(i[0]).lower()
            surname_english = self.replaceWithEnglish(i[1]).lower()
            pattern = "{0}{1}@{2}".format(name_english, surname_english, self.domain_adress)
            self.maillist_one.append(pattern)
        for i in self.peopleWithTwoName_raw:
            firstname_english = self.replaceWithEnglish(i[0]).lower() # firstname 
            secondname_english = self.replaceWithEnglish(i[1]).lower() ## secondname
            lastname_english = self.replaceWithEnglish(i[2]).lower() # lastname
            pattern = "{0}.{1}@{2}".format(firstname_english, lastname_english, self.domain_adress)
            pattern2 = "{0}.{1}@{2}".format(secondname_english, lastname_english, self.domain_adress)
            self.maillist_one.append(pattern) # generating possible f.lastname@company.com
            self.maillist_one.append(pattern2) # generating possible s.lastname@company.com        
        try:
            with open(self.output_file, 'w', newline='') as csvfile:
                fieldnames = ['email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for i in self.maillist_one:
                    if self.validate_email(i):
                        writer.writerow({'email': i})
                    else:
                        pass
            print("File : {0} generated".format(self.output_file))
        except Exception as e:
            print(e)
            pass
    def pattern8(self):
        for i in self.peopleWithOneName_raw:
            name_english = self.replaceWithEnglish(i[0]).lower()
            surname_english = self.replaceWithEnglish(i[1]).lower()
            pattern = "{1}{0}@{2}".format(name_english, surname_english, self.domain_adress)
            self.maillist_one.append(pattern)
        for i in self.peopleWithTwoName_raw:
            firstname_english = self.replaceWithEnglish(i[0]).lower() # firstname 
            secondname_english = self.replaceWithEnglish(i[1]).lower() ## secondname
            lastname_english = self.replaceWithEnglish(i[2]).lower() # lastname
            pattern = "{1}.{0}@{2}".format(firstname_english, lastname_english, self.domain_adress)
            pattern2 = "{1}.{0}@{2}".format(secondname_english, lastname_english, self.domain_adress)
            self.maillist_one.append(pattern) # generating possible f.lastname@company.com
            self.maillist_one.append(pattern2) # generating possible s.lastname@company.com        
        try:
            with open(self.output_file, 'w', newline='') as csvfile:
                fieldnames = ['email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for i in self.maillist_one:
                    if self.validate_email(i):
                        writer.writerow({'email': i})
                    else:
                        pass
            print("File : {0} generated".format(self.output_file))
        except Exception as e:
            print(e)
            pass
    def loadFromCSV(self):
        with open(self.file_input, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                temporary_item = row['name'].split(',')
                for i in temporary_item:
                    if len(list(i)) < 8:
                        pass
                    else:
                        self.names_2.append(i)
                        listo = i.split(" ")
                        if len(listo) <= 2:
                            self.peopleWithOneName_raw.append(listo)
                        else:
                            self.peopleWithTwoName_raw.append(listo)
    def cleanup(self):
        pass
    def replaceWithEnglish(self, word):
        turkish_list = {
         "ı": "i",
         "I": "i",
         "Ç": "c",
         "ç": "c",
         "ş": "s",
         "Ş": "s",
         "Ğ": "g",
         "ğ": "g",
         "Ü": "u",
         "ü": "u",
         "Ö": "o",
         "ö": "o"}
        for karakter in turkish_list:
            word = word.replace(karakter, turkish_list[karakter])
        return word
def main():
    Mainloop = CryingLinkedCmd()
    Mainloop.cmdloop()
main()
