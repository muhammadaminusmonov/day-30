# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["keyssss"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} is not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up")
# height = float(input("Enter your height: "))
# weight = int(input("Enter your weight: "))
#
# if height > 3:
#     raise ValueError("Human cannot be over 3 metres")
#
# bmi = weight / height ** 2
# print(bmi)


# exercises
# fruits = ["Apple", "Pear", "Orange"]
#
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(0)


# facebook_posts = [
#     {"Likes": 21, "Comments": 2},
#     {"Likes": 13, "Comments": 2, "Share": 1},
#     {"Likes": 33, "Comments": 8, "Share": 3},
#     {"Comments": 2, "Share": 2},
#     {"Comments": 2, "Share": 1},
#     {"Likes": 19, "Comments": 3},
# ]
#
# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes += post["Likes"]
#     except KeyError:
#         post["Likes"] = 0
#         total_likes += post["Likes"]
# print(total_likes)


# import pandas
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# data_dic = {row.letter: row.code for (index, row) in data.iterrows()}
#
#
# def generate_phonetic():
#     word = input("Enter your name: ").upper()
#     try:
#         formated_word = [data_dic[key] for key in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet can be entered!")
#         generate_phonetic()
#     else:
#         print(formated_word)
#
#
# generate_phonetic()


import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- SEARCH ENGINE ------------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No Data File Found", message="The Data File Is Not Exists Yet.\n"
                                                                "Please Enter Passwords to work this function")
    else:
        if website in data:
            user = data[website]['user']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email/Username: {user}\n"
                                                       f"Password: {password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No Details For The {website} Exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_entry.get()
    user = email_entry.get()
    user_password = password_entry.get()

    new_data = {
        website: {
            "user": user,
            "password": user_password
        }
    }

    if not website or not user or not user_password:
        messagebox.showerror(title="Missing", message="You left filed empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canva = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canva.create_image(100, 100, image=logo_img)
canva.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

web_entry = Entry(width=30)
web_entry.grid(column=1, row=1)
web_entry.focus()
email_entry = Entry(width=48)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "muhammadamincoder@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=40, command=save_data)
add_button.grid(column=1, row=4, columnspan=3)

window.mainloop()
