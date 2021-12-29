# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from logging import NullHandler
from typing import Any, Text, Dict, List
import os
import math
import random
import smtplib
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
import webbrowser
import mysql.connector
from mysql.connector import errorcode

from rasa_sdk.events import AllSlotsReset

login_user=''
database_password = "vaibhav"
class ActionRestart(Action):

     def name(self) -> Text:
            return "action_restart"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("Session ended! Please login/signup again.")

         return [AllSlotsReset()]

class BillForm(Action):
    def name(self) -> Text:
        return "bill_payment"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["bill_type"]

        for slot_name in required_slots:
            if  tracker.slots.get(slot_name) is None:

                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
            

        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("Form Submitted.")


    

class ResetSlot(Action):

    def name(self):
        return "action_reset_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("bill_type", None)]

class ResetCode(Action):

    def name(self):
        return "action_reset_code"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("code", None)]

# class action_billtype(Action):

#      def name(self) -> Text:
#          return "action_billtype"
    
#      billtype = ""

#      def run(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
#          dispatcher.utter_message(text="Bill Type Set")
#          return [SlotSet("bill_type", billtype)]

# class action_from_date(Action):
#     def name(self) -> Text:
#         return "action_from_date"
#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         required_slots = ["from_date"]

#         for slot_name in required_slots:
#             if  tracker.slots.get(slot_name) is None:

#                 # The slot is not filled yet. Request the user to fill this slot next.
#                 return [SlotSet("requested_slot", slot_name)]
            

#         return [SlotSet("requested_slot", None)]

# class action_to_date(Action):

#      def name(self) -> Text:
#          return "action_from_date"
    
#      date = ""

#      def run(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
#          dispatcher.utter_message(text="Date set")
#          return [SlotSet("to_date", date)]





# from rasa_core.agent import Agent
# from rasa_core.interpreter import RasaNLUInterpreter
# from rasa_core.utils import EndpointConfig
# from rasa_core.run import serve_application
# import rasa_core

# def talk():
#     agent = Agent.load('./models/dialogue',
#         interpreter=RasaNLUInterpreter('./models/nlu/default/so_health/'),
#         action_endpoint=EndpointConfig(url="http://172.17.0.3:8080/"))

#     print("Hi dude! I'm a bot. Are you a new user or existing user? ")
#     while True:
#         a = input()
#         if a == 'stop':
#             break
#         responses = agent.handle_message(a)
  
#         for response in responses:
#             print(response["text"])


# talk()


class ActionFacilitySearch(Action):

    def name(self) -> Text:
        return "action_amount"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        msg=tracker.get_slot("new_card_otp")
        print(msg)
        
        #otp for new card
        digits="0123456789"
        OTP=""
        for i in range(6):
            OTP+=digits[math.floor(random.random()*10)]
        otp = OTP + " is your OTP"
        msg= otp

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("notvalid99999@gmail.com","totallyinvalid")
        emailid =tracker.get_slot("email")
        print(emailid)
        s.sendmail('&&&&&&&&&&&',emailid,msg)

        if msg==OTP:
            dispatcher.utter_message("Please confirm your details: Card number - XXXXX4567, Bank: Axis, CVV & Temporary will be sent on SMS after you confirm.  \n enter confirm or if you want to edit enter edit")
            return [SlotSet("new_card_otp", msg)]
        else:
            dispatcher.utter_message("Invalid otp please enter it again")
            return [SlotSet("new_card_otp", "None")]

class DBFetch(Action):

    def name(self) -> Text:
        return "action_signup"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name=tracker.get_slot("name")
        email=tracker.get_slot("email")
        phone=tracker.get_slot("phone")
        password=tracker.get_slot("password")
        login_user=email
        print(name, email, phone, password)
        
        cnx = mysql.connector.connect(user='root',password=database_password, database='bankingbot')
        cursor = cnx.cursor()

        add_user = ("INSERT INTO user "
                    "(email,password,phone,name) "
                    "VALUES (%s, %s, %s, %s)")

        val = (email,password,phone,name)

        # Insert new employee
        cursor.execute(add_user, val)
        emp_no = cursor.lastrowid


        cnx.commit()

        cursor.close()
        cnx.close()

        dispatcher.utter_message("Signup Successful! Please login now by typing 'login'.")
        return [AllSlotsReset()]


class StoreDB(Action):

    def name(self) -> Text:
        return "action_verify"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email=tracker.get_slot("email")
        password=tracker.get_slot("password")
      
        login_user=email
        print(email, password)
        
        cnx = mysql.connector.connect(user='root',password=database_password, database='bankingbot')
        cursor = cnx.cursor()

        query = ("SELECT user_id,email FROM user "
                "WHERE email= %s and  password= %s")

        cursor.execute(query, (email, password))
        uid = -1
        for (a,b) in cursor:
            
            uid = a
        cursor.close()
        cnx.close()
        if uid!=-1:
            dispatcher.utter_message("Welcome! I am your banking bot. (Type 'tutorial' for help)")

            return_slots = []
            return return_slots
            
        else:

            dispatcher.utter_message("Invalid email or password Please try it again\n Would you like to login or signup")
            return_slots = []
            return_slots.append(SlotSet("password",None))
            return_slots.append(SlotSet("email",None))
            return return_slots
                

#action_benificiary

class Benificiary(Action):

    def name(self) -> Text:
        return "action_benificiary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name=tracker.get_slot("name")
        email=tracker.get_slot("email")
        phone=tracker.get_slot("phone")

        
        cnx = mysql.connector.connect(user='root',password=database_password, database='bankingbot')
        cursor = cnx.cursor()

        add_user = ("INSERT INTO  benificiary"
                    "(user_id,ben_name,ben_mail,ben_number,account_no) "
                    "VALUES ( %s, %s, %s, %s, %s)")

        val = (uid,name,email,phone,"50499679514")

        # Insert new employee
        cursor.execute(add_user, val)
        emp_no = cursor.lastrowid


        cnx.commit()

        cursor.close()
        cnx.close()

        dispatcher.utter_message("Benificiary added successfully")


# account information



class StoreDB(Action):

    def name(self) -> Text:
        return "action_account_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email=tracker.get_slot("email")
        password=tracker.get_slot("password")
        cnx = mysql.connector.connect(user='root',password=database_password, database='bankingbot')
        cursor = cnx.cursor()
        print(email,password)

        query = ("SELECT user_id,email FROM user "
                "WHERE email= %s and  password= %s")

        cursor.execute(query, (email, password))
        uidd=-1
        for (a,b) in cursor:
            uidd = a
        
        cnx.close()
        cnx = mysql.connector.connect(user='root',password=database_password, database='bankingbot')
        cursor2 = cnx.cursor()
        print(uidd)
     

        query2 = ("SELECT account_no,bank_name,Branch_address,balance  FROM account WHERE user_id= %s")
        print("query written")

        cursor2.execute(query2,(uidd,))
        print("query executed")
        
        for (a,b,c,d) in cursor2:
            dispatcher.utter_message("Account No::{}\nBank Name:: {}\nBank Address:: {}\nAccount Balance::{}".format(a,b,c,d))



# benificiary  information



class StoreDB(Action):

    def name(self) -> Text:
        return "action_benificiary_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email=tracker.get_slot("email")
        password=tracker.get_slot("password")
        cnx = mysql.connector.connect(user='root',password=database_password, database='bankingbot')
        cursor = cnx.cursor()
        print(email,password)

        query = ("SELECT user_id,email FROM user "
                "WHERE email= %s and  password= %s")

        cursor.execute(query, (email, password))
        uidd=-1
        for (a,b) in cursor:
            uidd = a
        
        cnx.close()
        cnx = mysql.connector.connect(user='root',password=database_password, database='bankingbot')
        cursor2 = cnx.cursor()
        print(uidd)
     

        query2 = ("SELECT ben_name,account_no  FROM benificiary WHERE user_id= %s")
        print("query written")

        cursor2.execute(query2,(uidd,))
        print("query executed")
        list=[];
        
        for (a,b) in cursor2:
            list.append(a,b)
            dispatcher.utter_message("Benificiary Name{}\nAccount No:: {}".format(a,b))

# statement generation

class StoreDB(Action):

    def name(self) -> Text:
        return "action_transaction_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email=tracker.get_slot("email")
        password=tracker.get_slot("password")
        cnx = mysql.connector.connect(user='root',password=database_password, database='bankingbot')
        cursor = cnx.cursor()
        print(email,password)

        query = ("SELECT user_id,email FROM user "
                "WHERE email= %s and  password= %s")

        cursor.execute(query, (email, password))
        uidd=-1
        for (a,b) in cursor:
            uidd = a
        
        cnx.close()
        cnx = mysql.connector.connect(user='root',password=database_password, database='bankingbot')
        cursor2 = cnx.cursor()
        print(uidd)
     

        query2 = ("SELECT  transaction_date,from_account,to_account,amount  FROM transactions WHERE user_id= %s")
        print("query written")

        cursor2.execute(query2,(uidd,))
        print("query executed")
        
        for (a,b,c) in cursor2:
            dispatcher.utter_message("on {} from account no {} to account no {}, {} rupees has been transfered".format(a,b,c,d))
  


# add account

class StoreDB(Action):

    def name(self) -> Text:
        return "action_add_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("hfidsi")
        email=tracker.get_slot("email")
        password=tracker.get_slot("password")
        cnx = mysql.connector.connect(user='root',password=database_password, database='bankingbot')
        cursor = cnx.cursor()
        print(email,password)

        query = ("SELECT user_id,email FROM user "
                "WHERE email= %s and  password= %s")

        cursor.execute(query, (email, password))
        uidd=-1
        for (a,b) in cursor:
            uidd = a
    
        cursor.close()
        cnx.close()
        cnx = mysql.connector.connect(user='root',password=database_password, database='bankingbot')
        cursor2 = cnx.cursor()
        acc_no=tracker.get_slot("account_number")
        bName=tracker.get_slot("bank_name")
        bAddr=tracker.get_slot("branch_address")
        print(acc_no,bName,bAddr,uidd)

        query = ("INSERT INTO account(account_no,user_id,bank_name,Branch_address) VALUES (%s, %s, %s, %s)")
        

        cursor2.execute(query,(acc_no,uidd,bName,bAddr))
        cnx.commit()
        cursor2.close();

        cnx.close()
        dispatcher.utter_message("Account added successfully")
     


#Fund transfer action


class StoreDB(Action):

    def name(self) -> Text:
        return "action_fund_transfer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email=tracker.get_slot("email")
        password=tracker.get_slot("password")
        cnx = mysql.connector.connect(user='root',password=database_password, database='bankingbot')
        cursor = cnx.cursor()
        print(email,password)

        query = ("SELECT user_id,email FROM user "
                "WHERE email= %s and  password= %s")

        cursor.execute(query, (email, password))
        uidd=-1
        for (a,b) in cursor:
            uidd = a
    
        cursor.close()
        cnx.close()
        cnx = mysql.connector.connect(user='root',password=database_password, database='bankingbot')
        cursor2 = cnx.cursor()
        acc_no=tracker.get_slot("account_number")
        amount=tracker.get_slot("amount")
        

        query = ("Update account set balance=balance-%s where user_id=%s")
        

        cursor2.execute(query,(amount,uidd))
        cnx.commit()
        cursor2.close();

        cnx.close()
        dispatcher.utter_message("{} tranferred to {}".format(amount,acc_no))
        return_slots = []
        return_slots.append(SlotSet("account_number",None))
        return_slots.append(SlotSet("amount",None))
        return return_slots     


# signup
# wrong login
# right login
# correct utter. (Welcome back)
# tutorial
# debit card services
# new card
# master card
# wrong otp
# right otp
# confirm
# restart
# /restart
