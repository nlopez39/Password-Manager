from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    password_list = [random.choice(letters)for char in range(nr_letters)]
      # password_list.append(random.choice(letters))

    password_list += [random.choice(symbols) for ch in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list += [random.choice(numbers) for chr in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    enter_pass.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = enter_web.get()
    email = enter_name.get()
    password = enter_pass.get()
    new_data = {
        web: {
            "email": email,
            "password": password,
        }
    }
    #check whether anyhting was written
    if len(web) ==0 or len(password) ==0 or len(email) == 0:
        messagebox.showerror(title="Error", message= "Nothing was entered for password or website")
    #create message box to check the details they entered
    else:
        try:
            with open("data.json", "r") as data_file:
                # json.dump(new_data,file, indent=4) #write into json file
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #update data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(data,data_file, indent=4)
        finally:
            enter_web.delete(0,END)
            enter_pass.delete(0,END)

def search():
    web = enter_web.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        for key in data:
            if web == key:
                email1 = data[key]["email"]
                password_1 = data[key]["password"]
                messagebox.showinfo(title=f"{web}", message=f"Email:{email1}\n Password: {password_1}" )
            else:
                messagebox.showerror(title="Input Error", message=f"Webname {web} not found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)
#website label
website = Label(text="Website")
website.grid(column=0, row=1)

#Email/username label
user_name = Label(text="Email/Username")
user_name.grid(column=0,row=2)
#password label
pass_word = Label(text="Password")
pass_word.grid(column=0, row=3)
#website entry box
enter_web = Entry(width=35)
enter_web.grid(column=1, row=1)
enter_web.focus()
#username entry box
enter_name = Entry(width=35)
enter_name.grid(column=1, row=2)
enter_name.insert(0,"angela@gmail.com")
#password entry box
enter_pass = Entry(width=35)
enter_pass.grid(column=1, row=3)

#generate password button
gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(column=2, row=3)
#search button
search_button = Button(text="Search", width= 15, command= search)
search_button.grid(column=2, row =1)
#Add button
add_button = Button(text="Add",command=save)
add_button.grid(column=1, row= 4)































window.mainloop()