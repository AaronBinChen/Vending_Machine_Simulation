from tkinter import *
from PIL import ImageTk, Image
import pygame

# Initializing pygame mixer to play audio later
pygame.mixer.init()

# Python Dictionary to hold number of each product available in the vending machine
inventory_dict = {
    "Arizona": 5,
    "Fanta": 5,
    "Caprisun": 5,
    "Yakult": 5
}

# Python dictionary to hold the price of each product available in the vending machine
price_dict = {
    "Arizona": 1,
    "Fanta": 2,
    "Caprisun": 1.50,
    "Yakult": 0.50
}

# Dictionary used to print image to the dispensary when item is purchased
dispense_dict = {
    "Arizona": "images/Arizona.png",
    "Fanta": "images/Fanta.jpg",
    "Caprisun": "images/Caprisun.png",
    "Yakult": "images/Yakult.jpg"
}

# Image Lists 
arizona_images = ["images/Arizona.png", "images/Arizona1.jpg", "images/Arizona2.jpg", "images/Arizona3.png", "images/Arizona4.jpg"]
caprisun_images = ["images/Caprisun.png", "images/Caprisun1.jpg", "images/Caprisun2.png", "images/Caprisun3.png", "images/Caprisun4.jpg"]
fanta_images = ["images/Fanta.jpg", "images/Fanta1.jpg", "images/Fanta2.png", "images/Fanta3.jpg", "images/Fanta4.jpg"]
yakult_images = ["images/Yakult.jpg", "images/Yakult1.png", "images/Yakult2.png"]

# Global variables that will be used later in different functions                               
inserted_payment = 0                    # Variable to keep track of current money inserted in VM
item_amount = 0                         # Variable to denote the amount of one product that a customer wants to buy
payment_success = False                 # Boolean used to denote if the payment went through or not
i = 0                                   # Used to keep track of images being iterated for previews
j = 0                                   # Used to keep track of images being iterated for previews
k = 0                                   # Used to keep track of images being iterated for previews
l = 0                                   # Used to keep track of images being iterated for previews

# Function used to play audio for vending machine dispensing
def play_audio():
    pygame.mixer.music.load("audio/dispensing_audio.mp3")
    pygame.mixer.music.play(loops = item_amount)

# Function to be called when the payment amount is typed into the entry field and button is clicked
def payment_processing():
    # Attempt to take the float() of the content from the entry field. If float() returns an error, we know that the input is either typed wrong OR no money was inserted
    try:
        # Money can only be positive. If the inserted money is positive or 0, we will enable the buttons to be clicked.
        if float(payment_entry.get()) >= 0:
            if product1_button['state'] == DISABLED:
                product1_button['state'] = NORMAL
            if product2_button['state'] == DISABLED:
                product2_button['state'] = NORMAL
            if product3_button['state'] == DISABLED:
                product3_button['state'] = NORMAL
            if product4_button['state'] == DISABLED:
                product4_button['state'] = NORMAL
    # No money was inserted or they typed the payment in an illiterate format 
    except:
        raise ValueError ("Value typed not understandable or no money was inserted")
    
# Function to be called when we enter the amount of product we want to buy. 
# Assigns a value to the variable item_amount so we can use it in the buy_product function 
def input_item_amt():
    global item_amount
    if (int(item_amt_entry.get()) >= 0):
        item_amount = int(item_amt_entry.get())
    else:
        print("Input item amount has to be greater than or equal to 0")

# Function to show various product images when label is hovered
def product1_change_image(self):
    global i
    if i <= 4:
        img = ImageTk.PhotoImage(Image.open(arizona_images[i]).resize((500,500), Image.ANTIALIAS))
        image_hover_label.config(image = img)
        image_hover_label.image = img
        i += 1
    else:
        i = 0
        product1_change_image(self)

# function to not display product images when label is not hovered
def product1_change_image_back(self):
    image_hover_label.config(image = "")
    image_hover_label.image = ""

# Function to show various product images when label is hovered
def product2_change_image(self):
    global j
    if j <= 4:
        img = ImageTk.PhotoImage(Image.open(fanta_images[j]).resize((500,500), Image.ANTIALIAS))
        image_hover_label.config(image = img)
        image_hover_label.image = img
        j += 1
    else:
        j = 0
        product2_change_image(self)

# function to not display product images when label is not hovered
def product2_change_image_back(self):
    image_hover_label.config(image = "")
    image_hover_label.image = ""

# Function to show various product images when label is hovered
def product3_change_image(self):
    global k
    if k <= 2:
        img = ImageTk.PhotoImage(Image.open(yakult_images[k]).resize((500,500), Image.ANTIALIAS))
        image_hover_label.config(image = img)
        image_hover_label.image = img
        k += 1
    else:
        k = 0
        product3_change_image(self)

# function to not display product images when label is not hovered
def product3_change_image_back(self):
    image_hover_label.config(image = "")
    image_hover_label.image = ""

# Function to show various product images when label is hovered
def product4_change_image(self):
    global l
    if l <= 4:
        img = ImageTk.PhotoImage(Image.open(caprisun_images[l]).resize((500,500), Image.ANTIALIAS))
        image_hover_label.config(image = img)
        image_hover_label.image = img
        l += 1
    else:
        l = 0
        product4_change_image(self)

# function to not display product images when label is not hovered
def product4_change_image_back(self):
    image_hover_label.config(image = "")
    image_hover_label.image = ""

# Function to be called when one of the product button is clicked on
def buy_product(product_type):
    global inserted_payment 
    global payment_success

    dispenser_label.config(image = "")
    dispenser_label.image = ""
    
    # If there is not enough money, add the currently inserted money to the previous vlaue
    inserted_payment = inserted_payment + float(payment_entry.get()) 
    # Obtaining price of a product from the price dictionary
    item_price = price_dict[product_type]
    # Caclulating the change to give back to the customer
    change = inserted_payment - (item_price * item_amount)
    # Finding the amount of product left in the vending machine
    current_number_of_product = inventory_dict[product_type]

    # If the amount that the customer wants to buy exceeds the availbility, return a message in the payment box. Return the money to the customer by setting inserted_payment equal to 0.
    if ((current_number_of_product != 0) and (item_amount > current_number_of_product)):
        inserted_payment = 0
        payment_status.insert(END, "There is only " + str(current_number_of_product) + " " + str(product_type) + " left!")
    
    # Checks if there is availability and if the requested amount is less than or equal to the availability
    elif ((current_number_of_product != 0) and (item_amount <= current_number_of_product)):
        # If there is enough for the customer, checking for the change allows us to see if there's enough money inserted or not.
        # If the change is positive, we know that there was definitely enough money inserted.
        if change > 0:
            inventory_dict[product_type] -= item_amount                                                         # Reduce the availability in the vending machine
            payment_success = True                                                                              # Payment was successful as they bought the requested items
            if payment_status.size() >= 3 and payment_success is True:                                          # Checks if the previous transaction is still on the screen and get rid of it
                payment_status.delete(0, END)
                payment_success = False
            payment_status.insert(END, "You inserted $" + str(inserted_payment))                                # Printing to the payment_status box
            payment_status.insert(END, "You bought " + str(item_amount) + " " + str(product_type))              # Printing to the payment_status box
            payment_status.insert(END, "Here's your change: $" + str(change))                                   # Printing to the payment_status box
            inserted_payment = 0                                                                                # Now that the transaction ended and change was given, set the inserted_payment to 0 again
            if inventory_dict[product_type] == 0:                                                               # If that product is finished, send a message to the status box so future customers know it's out of stock. 
                status_box.insert(END, str(product_type) + " is out of stock!")
            dispense_image = ImageTk.PhotoImage(Image.open(dispense_dict[product_type]).resize((500,500), Image.ANTIALIAS))
            dispenser_label.config(image = dispense_image)                                                      # Changing dispensary image to the product that was just dispensed
            dispenser_label.image = dispense_image
            play_audio()
        elif change == 0.0:                                                                                     # Just enough money was inserted to buy the product, hence, no change                                        
            inventory_dict[product_type] -= item_amount                                                         # Reduce the availability in the vending machine
            payment_success = True                                                                              # Payment was successful as they bought the requested items
            if payment_status.size() >= 3 and payment_success is True:                                          # Checks if the previous transaction is still on the screen and gets rid of it
                payment_status.delete(0, END)
                payment_success = False
            payment_status.insert(END, "You inserted $" + str(inserted_payment))                                # Printing to the payment_status box
            payment_status.insert(END, "You bought " + str(item_amount) + " " + str(product_type))              # Printing to the payment_status box
            payment_status.insert(END, "Here's your change: $" + str(change))                                   # Printing to the payment_status box
            inserted_payment = 0                                                                                # Now that the transaction ended and change was given, set the inserted_payment to 0 again
            if inventory_dict[product_type] == 0:                                                               # If the product is finished, send a message to the status box so future customers know it's out of stock.
                status_box.insert(END, str(product_type) + " is out of stock!")
            dispense_image = ImageTk.PhotoImage(Image.open(dispense_dict[product_type]).resize((500,500), Image.ANTIALIAS))
            dispenser_label.config(image = dispense_image)                                                      # Changing dispensary image to the product that was just dispensed
            dispenser_label.image = dispense_image
            play_audio()
        else:                                                                                                   # If change is negative, we know that there was not enough money inserted.
            payment_status.insert(END, "Not enough money! You only inserted " + str(inserted_payment))          # Print to payment_status box to alert the customer that they need to insert more money
    
    # If there is no availability, send message to alert customer that product is out of stock
    elif current_number_of_product == 0:                                                                                                       
        status_box.insert(END, str(product_type) + " is out of stock!")

    # Once the transaction is finished, we want to disable the buttons again so people can't buy anything before inserting their money/payment
    if product1_button['state'] == NORMAL:
        product1_button['state'] = DISABLED
    if product2_button['state'] == NORMAL:
        product2_button['state'] = DISABLED
    if product3_button['state'] == NORMAL:
        product3_button['state'] = DISABLED
    if product4_button['state'] == NORMAL:
        product4_button['state'] = DISABLED

# Function to restock the supplies in the vending machine
def restock():
    for key in inventory_dict.keys():
        inventory_dict[key] = 30
    
    # Test to see if dictionary values are updated
    # for key in inventory_dict.keys():
    #     print(key, "->", inventory_dict[key])

# Front End Design ##########################################################################################################################################################################
# Create a window 
root = Tk()
root.title("Vending Machine Simulation")

# Create Giant Product Frame ################################################################################################################################################################
product_frame = Frame(root, height=500*2, width=510*2)
product_frame.grid_propagate(0)

# Create 4 mini product frames.
product1 = Frame(product_frame, bg = "pale green", height=500, width=500)
product1.grid(row = 0, column = 0)
product2 = Frame(product_frame, bg = "orange", height=500, width=500)
product2.grid(row = 0, column = 1)
product3 = Frame(product_frame, bg = "bisque", height=500, width=500)
product3.grid(row = 1, column = 0)
product4 = Frame(product_frame, bg = "aquamarine", height=500, width=500)
product4.grid(row = 1, column = 1)

# Creating photoimage object to use image for all products
arizona_image = ImageTk.PhotoImage(Image.open("images/Arizona.png").resize((500,450), Image.ANTIALIAS))
fanta_image = ImageTk.PhotoImage(Image.open("images/Fanta.jpg").resize((500,450), Image.ANTIALIAS))
yakult_image = ImageTk.PhotoImage(Image.open("images/Yakult.jpg").resize((500,450), Image.ANTIALIAS))
caprisun_image = ImageTk.PhotoImage(Image.open("images/Caprisun.png").resize((500,450), Image.ANTIALIAS))

# Create product buttons and imagees
product1_button = Button(product1, text = "Arizona", image = arizona_image, bd = 4, relief = RIDGE, state = DISABLED, command = lambda: buy_product("Arizona"))
product1_button.grid(row = 0, column = 0, sticky="nsew")

product2_button = Button(product2, text = "Fanta", image = fanta_image, bd = 4, relief = RIDGE, state = DISABLED, command=lambda: buy_product("Fanta"))
product2_button.grid(row = 0, column = 0, sticky="nsew")

product3_button = Button(product3, text = "Yakult", image = yakult_image, bd = 4, relief = RIDGE, state = DISABLED, command=lambda: buy_product("Yakult"))
product3_button.grid(row = 0, column = 0, sticky="nsew")

product4_button = Button(product4, text = "Caprisun", image = caprisun_image, bd = 4, relief = RIDGE, state = DISABLED, command=lambda: buy_product("Caprisun"))
product4_button.grid(row = 0, column = 0, sticky="nsew")

# Initialize product name labels
product1_label = Label(product1, text = "Arizona Iced Tea", font = ("Helvetica", 12, "bold"), height = 2, bg = "pale green")
product2_label = Label(product2, text = "Fanta - Orange Juice", font = ("Helvetica", 12, "bold"), height = 2, bg = "orange")
product3_label = Label(product3, text = "Yakult - Sweet Probiotic Milk Boba Flavor", font = ("Helvetica", 12, "bold"), height = 2, bg = "bisque")
product4_label = Label(product4, text = "Caprisun - Fruit Juice", font = ("Helvetica", 12, "bold"), height = 2, bg = "aquamarine")

product1_label.grid(row = 1, column = 0)
product2_label.grid(row = 1, column = 0)
product3_label.grid(row = 1, column = 0)
product4_label.grid(row = 1, column = 0)

product1_label.bind("<Enter>", product1_change_image)
product1_label.bind("<Leave>", product1_change_image_back)
product2_label.bind("<Enter>", product2_change_image)
product2_label.bind("<Leave>", product2_change_image_back)
product3_label.bind("<Enter>", product3_change_image)
product3_label.bind("<Leave>", product3_change_image_back)
product4_label.bind("<Enter>", product4_change_image)
product4_label.bind("<Leave>", product4_change_image_back)

product_frame.grid(row = 0, column = 0)

# Middle frame ###########################################################################################################################################################################
middle_frame = Frame(root, bg = "floral white", height = 1000, width = 500)
middle_frame.grid_propagate(0)

# Top half of the middle frame is to give a preview of the items
hover_frame = Frame(middle_frame, bg = "black", height = 500, width = 500)
hover_frame.grid(row = 0, column = 0, sticky = "nsew")

# Label inside this top half of the middle frame
image_hover_label = Label(hover_frame, image = "")
image_hover_label.grid(row = 0, column = 0, sticky = "nsew")

# Bottom Half of the middle frame is to show the product that was bought
dispenser_frame = Frame(middle_frame, bg = "blue", height = 500, width = 500)
dispenser_frame.grid(row = 1, column = 0, sticky = "nsew")

# Dispenser Label 
dispenser_label = Label(dispenser_frame, image = "")
dispenser_label.grid(row = 0, column = 0, sticky = "nsew")

# denote the middle of the GUI 
middle_frame.grid(row = 0, column = 1)

# Right Hand Side Made for Vending Machine Status, Payment Status, Entry Fields for item amount and money ###################################################################################
right_hand_frame = Frame(root, bg = "black", height = 1000, width = 400)
right_hand_frame.grid_propagate(0)

status_box_frame = Frame(right_hand_frame, bg = "blue", height = 500, width = 400)
status_box_frame.grid(row = 0, column = 0)

# Vending Machine Status Box
status_box = Listbox(status_box_frame, height = 25, width = 400, bg = "mint cream", font = ("Helvetica", 12, "bold"), fg = "#3B466B")
# status_box = Label(status_box_frame, width = 400, height = 30, fg = "black")
status_box.grid(row = 0, column = 0, sticky = "nsew")

# Payment Frame
payment_frame = Frame(right_hand_frame, bg = "yellow", height = 500, width = 400)
payment_frame.grid(row = 1, column = 0, sticky = "nsew")

# Payment Status
payment_status = Listbox(payment_frame, height = 10,width = 400, bg = "alice blue", font = ("Helvetica", 12, "bold"), fg = "#3B466B")
payment_status.grid(row = 0, column = 0, sticky = "nsew")

# Price Box (Displays the prices of each product)
price_box = Listbox(payment_frame, height = 4, width = 400, bg = "lavender", font = ("Helvetica", 12, "bold"), fg = "#3B466B")
price_box.insert(1, "Arizona: $1")
price_box.insert(2, "Fanta: $2")
price_box.insert(3, "Caprisun: $1.50")
price_box.insert(4, "Yakult: $0.50")
price_box.grid(row = 1, column = 0, sticky = "nsew")

# Payment Entry Entry Field
payment_entry = Entry(payment_frame, width = 400, borderwidth = 5)
payment_entry.grid(row = 2, column = 0, sticky = "nsew")

# Button to submit payment
payment_button = Button(payment_frame, fg = "black", bg = "spring green", text = "Pay Now", anchor = "w", font = ("Helvetica", 12, "bold"), borderwidth = 2, relief = "raised", padx = 40, pady = 5, command = payment_processing)
payment_button.grid(row = 3, column = 0, sticky = "nsew")

# Separates the Pay Now Button and the Item Amount Entry Field
separator = Frame(payment_frame, bg = "black", height = 20, width = 400)
separator.grid(row = 4, column = 0, sticky = "nsew")

# Item Amount Entry Field
item_amt_entry = Entry(payment_frame, width = 400, borderwidth = 5)
item_amt_entry.grid(row = 5, column = 0, sticky = "nsew")

# Button to submit item amount
item_amt_button = Button(payment_frame, fg = "black", bg = "IndianRed1", text = "Submit Item Amount", font = ("Helvetica", 12, "bold"), borderwidth = 2, relief = "raised", anchor = "w", padx = 40, pady = 5, command = input_item_amt)
item_amt_button.grid(row = 6, column = 0, sticky = "nsew")

# Button to allow for restocking
restock_button = Button(payment_frame, fg = "black", bg = "thistle1", text = "Restock", font = ("Helvetica", 12, "bold"), anchor = "w", borderwidth = 2, relief = "raised", padx = 40, pady = 11, command = restock)
restock_button.grid(row = 7, column = 0, sticky = "nsew")

# Denote the right side of the GUI (Left side is the product frame, middle is the dispenser)
right_hand_frame.grid(row = 0, column = 2)

root.mainloop()