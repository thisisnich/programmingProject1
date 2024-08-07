#Programming Group Project
#EGE151-E4
#Group 7
#Dubs Nicholas Francis RuiQiang (241439P)
#Thadar Hpone Myat @ Doris (241442L)

import customtkinter
from CTkMessagebox import CTkMessagebox
from PIL import Image
import json

catalog = {
    "Drinks": {
        "N32": {"name": "Neo's Green Tea", "price": 3},
        "M13": {"name": "Melo Chocolate Malt Drink", "price": 2.85},
        "V76": {"name": "Very-Fair Full Cream Milk", "price": 3.5},
        "N14": {"name": "Nirigold UHT Milk", "price": 4.15}
    },
    "Beer": {
        "L11": {"name": "Lion (24 x 320 ml)", "price": 52},
        "P21": {"name": "Panda (24 x 320 ml)", "price": 78},
        "A54": {"name": "Axe (24 x 320 ml)", "price": 58},
        "H91": {"name": "Henekan (24 x 320 ml)", "price": 68}
    },
    "Frozen": {
        "E11": {"name": "Edker Ristorante Pizza 355g", "price": 6.95},
        "F43": {"name": "Fazzler Frozen Soup 500g", "price": 5.15},
        "CP31": {"name": "CP Frozen Ready Meal 250g", "price": 4.12},
        "D72": {"name": "Duitoni Cheese 270g", "price": 5.6}
    },
    "Household": {
        "FP76": {"name": "FP Facial Tissues", "price": 9.5},
        "FP32": {"name": "FP Premium Kitchen Towel", "price": 5.85},
        "K22": {"name": "Klinex Toilet Tissue Rolls", "price": 7.5},
        "D14": {"name": "Danny Softener", "price": 9.85}
    },
    "Snacks": {
        "SS93": {"name": "Slingshot Seaweed", "price": 3.1},
        "MC14": {"name": "Mei Crab Cracker", "price": 2.05},
        "R35": {"name": "Reo Pokemon Cookie", "price": 4.8},
        "HS11": {"name": "Huat Seng Crackers", "price": 3.55}
    }
}

# print(catalog) #Debug: print catalog
cart = {category: {sn: 0 for sn in items} for category, items in catalog.items()}
# print(cart) #Debug: print the initialised empty cart
#for cart buttons
globals_namespace = globals()

#Discounts with name, and discount amount as a percentage % = value*100
discounts = {"None" : 0,
             "Senior" : 0.1,
             "Member" : 0.08,
             "NS man": 0.05}

#Declaring variables
selectedCat = "Drinks"      #Selected Category
selectedItem = "N32"        #Selected item from category
selectedDiscount = "None"   #Selected discount type
selectedCard = ''           #Default selected card
billtext = ''               #Default bill text(address)
subtotal = 0                #Subtotal before gst
total = 0                   #Total after gst
gstAmt = 0                  #Amount of gst
discountAmount = 0          #Amount of discount
afterDiscount = 0           #Total after discount
#appearance mode set to dark
customtkinter.set_appearance_mode("dark")
#colour theme set to dark blue
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()  #define root window
root.geometry("410x370")    #set default size
root.iconbitmap('resources/Logo_dark.ico') #set icon
root.title("DorNick")       #set window name
root.minsize(410, 370)  #set minimum window size

###Master Frame
##Shopping tab

#function run when plus button is pressed
def plus_button(sn):
    #find location in cart that corresponds to selected category and item and increment by 1
    for cat in cart:
        for item in cart[cat]:
            if item == sn:
                cart[cat][item]+=1
                break
    #print(cart) #Debug: print cart
    update_labels()

#function run when subtract button is pressed
def sub_button(sn,is_cart_button):
    if is_cart_button:
        for cat in cart:
            for item in cart[cat]:
                if item == sn:
                    #if the value of the corresponding spot in cart is more than 0, subtract by 1
                    #if the amount of items is zero, run remove_cart_label, and pass the selected serial number -> remove the label in cart that is now 0
                    if cart[cat][item] == 1:
                        remove_cart_label(sn, globals_namespace, is_cart_button)
                    elif cart[cat][item]>=1:
                        cart[cat][item] -= 1
    else:
        if cart[selectedCat][selectedItem]>=1:
            cart[selectedCat][selectedItem] -= 1
            #if the amount of items is zero, run remove_cart_label, and pass the selected serial number -> remove the label in cart that is now 0
            if cart[selectedCat][selectedItem] == 0:
                remove_cart_label(selectedItem, globals_namespace, is_cart_button)
        #if it is 0, then print "can't go below 0" and don't reduce by 1
        else:
            print("can't go below 0") #Debug: print message when it's 0
            # Warning message will be shown once the value goes below 0
            CTkMessagebox(title="Error", message="Can't go below 0!", icon="cancel", width=350, height=80, button_width=25,
                          button_height=75)
    update_labels()
    #print(cart) #Debug: print cart

#function called when category dropbox value is selected
def cat_callback(choice):
    #set global variables that are changed in the function
    global selectedCat, itemList, selectedItem
    # print(f'combobox dropdown clicked {choice}'  # Debug: print the selected cat
          # f' : {menu[selectedCat][0]}' #Debug: print the name
          # )
    selectedCat = choice
    #set item list to the new items in the selected cat
    itemList = get_items()
    #set a temp list to make sure labels updated properly
    temp = list(catalog[selectedCat])
    selectedItem=temp[0]
    update_labels()

#Function called when item dropdown is selected
def item_callback(choice):
    #declaring global vars that are changed in the function
    global selectedItem
    # print(f'combobox dropdown clicked {choice}'  # Debug: print choice
    #       # f' : {menu[selectedCat][0]}' #Debug: print choice name
    #       )
    #check which item name matches an item in the selected category
    for sn in catalog[selectedCat]:
        # print(sn) #Debug: print sn
        #when the selected item is matched, set the selected item to selectedItem
        # print(catalog[selectedCat][sn]['name']) #Debug: print name of item at 'sn'
        if choice == catalog[selectedCat][sn]['name']:
            selectedItem=sn
    # print(f'item selected: {selectedItem}') #Debug: print the selected item
    update_labels()

#function to get items in a category
def get_items():
    return [catalog[selectedCat][sn]["name"] for sn in catalog[selectedCat]]

#function to update image
def update_img():
    #get height and width of root window
    # print(f'height: {root.winfo_height()}')     #Debug: print window height
    # print(f'width: {root.winfo_width()}')       #Debug: print window width
    #get max width and height the image can be
    maxImgHeight = int(root.winfo_height() / 5)
    maxImgWidth = int(root.winfo_width() / 6)
    # print(f'img height: {maxImgHeight}')        #Debug: print max image height
    # print(f'img width: {maxImgWidth}')          #Debug: print max image width
    #because square image, set image size to be the smallest of the maximum values
    imgSize = min(maxImgWidth, maxImgHeight)

    dark, light = get_image()
    #update image with selected item serial number and set image size to maximum size
    itemImage.configure(light_image=light,
                        dark_image=dark,
                        size=(imgSize,imgSize))
    imageLabel.configure(image=itemImage)

#function to check that only accepted keys are registered
def validate_key_int(event):
    # print(event.keysym) #Debug:print key that was pressed
    #only accept digits, backspace, Enter, delete, Left or right
    if not event.char.isdigit() and event.keysym not in ('BackSpace', 'Return', 'Left', 'Right', 'Delete'):
        # print('key not accepted')  #Debug: print message when keypress is not accepted
        return 'break'
    # print(amountEntry.get())  #Debug: print current stored value in Entry field

#function called when enter key is pressed
# sets cart at selected category and selected item to value that is in the entry box
def set_amt(event, sn, is_cart, entry):
    # print(entry)
    #print('-----')             #Debug: print lines to show what the read input is
    # print(amountEntry.get())  #Debug: print read input
    #print('-----')             #Debug: print lines to show what the read input is
    #set cart value to the value stored in Entry
    if is_cart and int(globals_namespace[entry].get())==0:
        remove_cart_label(sn, globals_namespace, is_cart)
    else:
        cart[selectedCat][selectedItem]=int(globals_namespace[entry].get())
        if cart[selectedCat][selectedItem] == 0:
            remove_cart_label(sn, globals_namespace, is_cart)
    update_labels()

#function to update labels
def update_labels():
    update_img() #update the image
    snComboBox.configure(values=itemList)
    #update the label that displays the item code
    codeLabel.configure(text=selectedItem)
    snComboBox.set(catalog[selectedCat][selectedItem]['name'])
    #update the label that shows number of items in cart
    itemCountLabel.configure(text=str(cart[selectedCat][selectedItem]))
    #update the label that shows selected discount
    discountLabel.configure(text=f'Discount: {(discounts[selectedDiscount]*100)}%')
    #update label that shows price of item
    priceLabel.configure(text = f'${catalog[selectedCat][selectedItem]['price']}')
    #if the value in amount entry is not empty, clear it
    #When using amountEntry.delete() subsequent entries return empty when enter is pressed
    # if amountEntry.get()!='':
    #     amountEntry.delete(0,'end')
    #update the placeholder text in the entry to the amount in cart: doesn't do anything if entry isn't cleared
    amountEntry.delete(0,'end')
    amountEntry.insert(0,cart[selectedCat][selectedItem])
    #Run function to make new cart labels
    show_cart()
    #run function to calculate sum
    calculate_sum()

##Cart tab
#function to read cart at selected category and selected item
def read_cart():
    # print(cart)
    # print(selectedCat)
    # print(selectedSn)
    return cart[selectedCat][selectedItem]

#function to update label to show cart to user
def show_cart():
    #while there are items in cart, get the value and item name
    for cat in cart:
        for sn in cart[cat]:
            #if there is an order for any item, make a new label in cart for that item
            if cart[cat][sn] >= 1:
                #calculate cost of item
                item_cost = cart[cat][sn] * catalog[cat][sn]['price']
                #run make_cart_label function with the item 'sn' and as well as item name, and cost
                make_cart_label(cart[cat][sn], item_cost, catalog[cat][sn]["name"], globals_namespace,cat, sn)

#function to make labels for cart
def make_cart_label(amt, price, name, namespace,cat, sn):
    #try to configure an existing label with the serial number. i.e. sn = N32 frame = N32Frame
    try:
        namespace[f'{sn}Label'].configure(text=f'{name:<16}{amt:^{len(str(amt))+6}}${price:.2f}')
        namespace[f'{sn}Entry'].delete(0,'end')
        namespace[f'{sn}Entry'].insert(0,cart[cat][sn])
        namespace[f'{sn}Entry'].configure(width=(23+(len(str(cart[cat][sn])))*7))
        #print('label already exists')      #Debug: if label already exists
    #if label doesn't exist, create a new label
    except:
        # print('Making new frame')  #Debug: print if a new label is made
        #make new frame for this item
        namespace[f'{sn}Frame'] = customtkinter.CTkFrame(cartFrame)
        namespace[f'{sn}Frame'].columnconfigure(0, weight=3)
        # namespace[f'{name}Frame'].columnconfigure(1, weight=1)
        #Display name, amount ordered and cost of this item
        namespace[f'{sn}Label'] = customtkinter.CTkLabel(namespace[f'{sn}Frame'],
                                                         text=f'{name:<16}{amt:^{len(str(amt))+6}}${price:.2f}')
        namespace[f'{sn}Label'].grid(column=0, row = 0)
        #Button to remove item from cart, runs remove_cart_label function, passes serial number
        ###PYCHARM SUGGESTED CODE####
        #lambda is required since we need to pass arguments to "remove_cart_label" function
        #lambda creates a small, throwaway function which will not be reused elsewhere
        namespace[f'{sn}ButtonFrame']=customtkinter.CTkFrame(namespace[f'{sn}Frame'])
        namespace[f'{sn}ButtonFrame'].grid(column = 1, row = 0)  # pack button frame
        # configure button frame columns
        namespace[f'{sn}ButtonFrame'].columnconfigure(0, weight=4)
        namespace[f'{sn}ButtonFrame'].columnconfigure(1, weight=1)
        namespace[f'{sn}ButtonFrame'].columnconfigure(2, weight=4)
        # plus button, calls plus_button when pressed -> increments value in cart by 1
        namespace[f'{sn}AddButton'] = customtkinter.CTkButton(master=namespace[f'{sn}ButtonFrame'], text='+',
                                                              font=('Roboto', 24), command=lambda : plus_button(sn),
                                            width=30, height=25)
        namespace[f'{sn}AddButton'].grid(column=3, row=0)  # column changed
        namespace[f'{sn}Entry'] = customtkinter.CTkEntry(master=namespace[f'{sn}ButtonFrame'],
                                                         placeholder_text=str(cart[selectedCat][selectedItem]),
                                                         width = 30, height=35)
        namespace[f'{sn}Entry'].grid(column=2, row=0)
        namespace[f'{sn}Entry'].bind('<KeyPress>', validate_key_int)
        namespace[f'{sn}Entry'].bind('<Return>', lambda event: set_amt(event, sn,True,f'{sn}Entry'))
        # minus button, calls sub_button when pressed -> decrements value in cart by 1
        namespace[f'{sn}SubButton'] = customtkinter.CTkButton(master=namespace[f'{sn}ButtonFrame'], text='-',
                                                              font=('Roboto', 24), command=lambda : sub_button(sn,True),
                                            width=30,height=25)
        namespace[f'{sn}SubButton'].grid(column=0, row=0)  # column changed

        # namespace[f'{sn}Button'] = customtkinter.CTkButton(namespace[f'{sn}Frame'],text='Remove', width = 50, command=lambda: remove_cart_label(sn, namespace, True))
        # namespace[f'{sn}Button'].grid(column=2, row=0, padx=10, pady=5)
    #pack label
    namespace[f'{sn}Frame'].pack(pady=1)

#function to remove label
def remove_cart_label(sn, namespace, is_cart_button):
    if is_cart_button:
        confirmDelete = CTkMessagebox(title="Confirm", message="Are you sure you want to remove this item?",
                                      icon="question", option_1="Cancel", option_2="Yes", width=350, height=100,
                                      button_height=30)
        response = confirmDelete.get()
        if response == "Yes":
            #try forgetting
            try:
                # print('removing label') # Debug: print when a label is removed

                namespace[f'{sn}Frame'].pack_forget()
                # check which item needs to be removed, set that item in cart to 0
                for cat in cart:
                    for item in cart[cat]:
                        if sn == item:
                            cart[cat][item] = 0
            #if label does not exist, continue
            except:
                pass
        else:
            print('no')
    else:
        try:
            # print('removing label') # Debug: print when a label is removed
            namespace[f'{sn}Frame'].pack_forget()
        # if label does not exist, continue
        except:
            pass

        update_labels() #update labels

def update_cart_labels():
    for cat in cart:
        for item in cart[cat]:
            if cart[cat][item] >= 1:
                print(item)

#Function called when "checkout" button is clicked
def checkout_button():
    #initialise variable as cart is not existing
    cartExists = False
    #if there is an item with an order of 1 or more, set that cart does exist
    for cat in cart:
        for item in cart[cat]:
            if cart[cat][item] >= 1:
                cartExists = True
                break
    #if cart exists, allow checkout
    if cartExists:
        #place 'checkout' frame, remove 'master' frame
        masterFrame.place_forget()
        checkoutFrame.place(anchor='center', relheight=0.8, relwidth=0.65, relx=0.5, rely=0.5)
        # print("You are checking out") #Debug: print when the condition is met
    #if cart does not exist, send error message box
    else:
        CTkMessagebox(title="Error", message="No items in the cart", icon="warning", option_1="Back", height=50,
                      button_width=25, button_height=75)
        #print("No items in the cart") #Debug: print when the condition isn't met


##Setting tab
#function called when appearance menu is selected, sets appearance to the selected type
def appearance_callback(choice: str):
    customtkinter.set_appearance_mode(choice)

#function called when item in scaling menu is selected, sets scaling to selected number
def scaling_callback(choice: str):
    #removes % from string
    new_scaling_float = int(choice.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)

###Checkout frame
#calculation function
def calculate_sum():
    #declaring global vars that are changed in the function

    global subtotal,total, gstAmt, discountAmount, afterDiscount
    #declare working value
    temp_cost = 0
    #while there are items in cart, find the corresponding price, and multiply number of items in cart by price
    for cat in cart:
        for sn in cart[cat]:
            #print(cat,sn)
            # print(cart[i][y])         #Debug: print value in cart
            # print(menu[i][1][y][2])   #Debug: print corresponding price
            #add the total price to tempCost

            temp_cost += cart[cat][sn]*catalog[cat][sn]['price']
            # print(tempCost)           #Debug: print current temporary Value
    #Set subtotal to the temporary cost
    subtotal=temp_cost
    #Print subtotal
    # print(f'Subtotal ${subtotal:.2f}') #Debug print new subtotal
    #Calculate total with GST
    total=subtotal*1.09
    #Print total after GST
    # print(f'Total ${total:.2f}') # Debug: print new total
    #calculate the amount of gst charged
    gstAmt = subtotal*0.09
    #print amount of gst charged
    # print(f'GST ${gstAmt:.2f}') #Debug: print new gst amount
    #print(discounts[selectedDiscount])  #Debug: print selected discount
    #Calculate the amount of discount given based on the selected discount
    # print(selectedDiscount) #Debug: print selected discount
    discountAmount = total*(discounts[selectedDiscount])
    #Print the amount of discount deducted
    # print(f'Discount amt: {discountAmount:.2f}') #Debug: print new discount amount
    #calculate total after discount
    afterDiscount = total*(1-discounts[selectedDiscount])
    #print total after discount
    # print(f'Total after discount ${afterDiscount:.2f}') #new price after discount

    # update labels to reflect the totals
    subtotalLabel.configure(text=f'Subtotal: ${subtotal:.2f}')
    shopSubtotalLabel.configure(text=f'Subtotal: ${subtotal:.2f}')
    totalLabel.configure(text=f'Total: ${total:.2f}')
    gstLabel.configure(text=f"GST: ${gstAmt:.2f}")
    discountAmountLabel.configure(text=f'Discount amount: ${discountAmount:.2f}')
    afterDiscountLabel.configure(text=f'Total after discount ${afterDiscount:.2f}')
    #for billing statement
    billTotalLabel.configure(text=f'Total ${afterDiscount:.2f}')
    billSubTLabel.configure(text=f'Subtotal: ${subtotal:.2f}')
    billGSTLabel.configure(text=f"GST: ${gstAmt:.2f}")
    billDiscountLabel.configure(text=f'Discount amount: ${discountAmount:.2f}')

#Function called when discount dropdown is selected
def discount_callback(choice):
    #Declare globals
    global selectedDiscount
    #check which discount name matches the selected discount
    selectedDiscount=choice
    update_labels()

#Function called when "back" button is selected to bring the user back to the "cart tab"
def back_button():
    checkoutFrame.place_forget() #remove 'checkout' frame
    masterFrame.place(anchor='center', relheight=0.85, relwidth=0.85, relx=0.5, rely=0.5)
    # print("Back to the cart") #Debug: print when the button is pressed

#Function called when "continue payment" button is clicked
def payment_button():
    #remove 'checkout' frame and place 'choice' frame
    checkoutFrame.place_forget()
    choiceFrame.place(anchor= 'center', relheight = 0.8, relwidth=0.65, relx=0.5, rely=0.5)
    # print("Proceeding to payment section...") #Debug: print message when the button is pressed


###Payment frame
#Function called when "payment method" is chosen
def pay_method():
    global selectedCard
    #if the user chose 'debit card' option, the value of radio_default= 1
    if radio_default.get() == 1:
        selectedCard = 'Debit' # when the value is 1
    # if the user chose 'credit card' option, the value of radio_default= 2
    else:
        selectedCard = 'Credit' #when the value is 2
    #print(f"You're paying with {selectedCard} card.") #Debug: print the selected card
    if cardEntry.get():
        #delete values in entries
        cardEntry.delete(0, 'end')
        dateEntry.delete(0, 'end')
        cvvEntry.delete(0, 'end')
        addressEntry.delete(0, 'end')
        cardEntry.configure(placeholder_text="eg- 1234 5678 9123 4567")
        dateEntry.configure(placeholder_text="MM/YY")
        cvvEntry.configure(placeholder_text="777")
        addressEntry.configure(placeholder_text="S569830, #02-1234")
    #if there is information stored for the selected card, insert it into the entries
    if get_card_info('card_number') != False:
        cardEntry.insert(0, get_card_info('card_number'))
        dateEntry.insert(0, get_card_info('expiry_date'))
        cvvEntry.insert(0, get_card_info('cvv'))
        addressEntry.insert(0, get_card_info('address'))

    #remove 'choice' frame and place 'payment' frame
    choiceFrame.place_forget()
    paymentFrame.place(anchor= 'center', relheight = 0.8, relwidth=0.65, relx=0.5, rely=0.5)
    #configuring the label to update in the billing statement
    selectedCardLabel.configure(text=f"Payment method: {selectedCard} card")

#Function called when the "place order" button is pressed
#Function to validate the entries
def card_validation():
    global card_number, expiry_date, cvv, address, billtext
    #receiving entries
    card_number = cardEntry.get()
    expiry_date = dateEntry.get()
    cvv = cvvEntry.get()
    address = addressEntry.get()
    #if one of the entries is empty, the warning message will be released
    if not card_number or not expiry_date or not cvvEntry or not addressEntry:
        CTkMessagebox(title="Error", message="All fields are required!", icon="warning", option_1="Retry", height=100,
                      button_width=50, button_height=30)
        # print("All fields are required")  # Debug: print message to remind the user to fill up every field
        return
    save_all_info()  # run function to save card info
    #remove 'payment' frame and place 'bill' frame
    paymentFrame.place_forget()
    billFrame.place(anchor='center', relheight=0.85, relwidth=0.85, relx=0.5, rely=0.5)
    #to display address info in 'bill' frame
    #if no new data is saved, the already existed address of respective card in the file will be shown
    billtext = addressEntry.get()
    # print(f"Billing Address: {billtext}") #Debug: print the address in the billing statement
    #configuring the label to update in the billing statement
    billtextLabel.configure(text=f'{billtext}')

#Function to save the entries if the "save" checkbox is clicked
def save_all_info():
    #when the checkbox is chosen, the value will become 1
    if save_info_default.get() ==1:
        # print("You've saved your personal information") #Debug: print when the "checkbox" is ticked
        # print(save_allInfo.get()) #Debug: print all the saved info
        if save_allInfo.get():
            info = {
                "card_type": str(selectedCard),
                "card_number": str(card_number),
                "expiry_date": str(expiry_date),
                "cvv": str(cvv),
                "address": str(address)
            }
            save_info(info) #run function to save card info to json file
    #if the "checkbox" isn't chosen, the value will stay default 0
    else:
        return
        # print("No data/new data was saved") #Debug: print when the user didn't choose the saving option


#funtion is passed a dictionary with card information and it is saved to a json file
def save_info(card_info):
    # print('saved info') #Debug: print when the new card info is saved
    #print(card_info)   #DEBUG: print the card info dict that will be saved
    #try opening file
    try:
        #open and read file to get data stored
        with open('resources/card_info.json') as file:
            try:
                #try loading data from file
                data = json.load(file)
            except json.JSONDecodeError:
                #if no data in file, return an empty list
                data = []
    except FileNotFoundError:
        #if no file, return an empty list
        data= []

    #initialise a variable to save if the selected card type is already saved
    card_exists = False
    #check through the items in the Json file, and compare to selected card types
    ####CHATGPT CODE####
    #chatGPT suggested to simplify like this
    #enumerate is used to iterate over the 'data' list with both index 'i' and the element 'card'
    #provides the index 'i' along with 'card' element, helps modify the list 'data' at the specific index
    for i, card in enumerate(data):
        #if the selected card type is on the file
        if card['card_type'] == card_info['card_type']:
            #overwrite data at that position with new card info
            data[i] = card_info
            #set card exists as True
            card_exists = True
            break
    #if the card does not exist yet, append card info to the file
    if not card_exists:
        data.append(card_info)
    #overwrite new data to file
    with open('resources/card_info.json', 'w') as file:
        json.dump(data, file, indent=4)

    #to display address info in 'bill' frame
    #if new data was saved, the new address of respective card will be shown
    billtext = addressEntry.get()  # for the billing statement
    # print(f"Billing Address: {billtext}") #Debug: print the new address in the billing statement
    # configuring the label to update in the billing statement
    billtextLabel.configure(text=f'{billtext}')


#Entries validation
#function to check that length of card number is not longer than 16
def validate_card_no_length(event):
    # print(len(cardEntry.get()))
    #if the length of cardEntry is more than 16, delete everything after that point
    if len(cardEntry.get()) > 16:
        cardEntry.delete(16, 'end')


#function to check that length of cvv is not longer than 3
def validate_cvv_length(event):
    # print(len(cvvEntry.get()))'
    #if length of cardEntry is more than 3, delete everything after that point
    if len(cvvEntry.get()) > 3:
        cvvEntry.delete(3, 'end')


def validate_date_key(event):
    # print(event.keysym) #Debug:print key that was pressed
    #only accept digits, backspace, Enter, Left or right
    if not event.char.isdigit() and event.keysym not in ('BackSpace', 'Return', 'Left', 'Right', 'slash'):
        # print('key not accepted')  #Debug: print message when keypress is not accepted
        return 'break'
    # print(amountEntry.get())  #Debug: print current stored value in Entry field


#function to check that length of date is not longer than 5
def validate_date_length(event):
    # print(len(dateEntry.get()))
    #if length of cardEntry is more than 5, delete everything after that point
    if len(dateEntry.get()) > 5:
        dateEntry.delete(5,7)


#check for only address related characters
def validate_address_key(event):
    # print(event.keysym) #Debug:print key that was pressed
    #only accept digits, backspace, Enter, Left or right
    if not event.char.isdigit() and event.keysym not in ('BackSpace', 'Return', 'Left', 'Right', 'S', 'comma',
                                                         'numbersign', 'minus', 'space'):
        # print('key not accepted')  #Debug: print message when keypress is not accepted

        return 'break'
    # print(amountEntry.get())  #Debug: print current stored value in Entry field

#function to check that length of address is not longer than 21
def validate_address_length(event):
    # print(len(addressEntry.get()))
    #if length of address Entry is more than 21, delete everything after that point
    if len(addressEntry.get()) > 21:
        addressEntry.delete(21,'end')

###Detail frame
#Function to run when the 'ok' button is clicked
def okButton():
    #message box will be released when the 'ok' button is pressed
    msg = CTkMessagebox(title="Congratulations!", message="Your purchase has been successfully made!", icon="check",
                        option_1="Ok", option_2="Purchase More", height=100, button_width=75, button_height=30)
    response = msg.get()
    # if the user chose the button "ok", this will lead to the "Thank you" frame
    if response == "Ok":
        # remove 'bill' frame and place 'thank you' frame
        billFrame.place_forget()
        thankyouFrame.place(anchor='center', relheight=0.85, relwidth=0.85, relx=0.5, rely=0.5)
        # print("Thank you for shopping with us!")  # Debug: print when 'ok' button is pressed
    # if the user chose to "purchase more", this will lead back to the "Shopping" tab of the Master Frame
    else:
        # loop while category exists in cart
        for cat in cart:
            # loop while there is an item in the category
            for item in cart[cat]:
                # if there is one or more items in the cart for this item
                if cart[cat][item] >= 1:
                    # print(item)   # Debug: print the item
                    # print(cart[cat][item])    # Debug: print how many of this item in cart
                    # set it to 0
                    cart[cat][item] = 0
                    # remove the label for that item in the cart
                    remove_cart_label(item, globals_namespace, False)

        # remove 'payment' frame , 'bill' frame and place 'master' frame
        billFrame.place_forget()
        paymentFrame.place_forget()
        masterFrame.place(anchor='center', relheight=0.85, relwidth=0.85, relx=0.5, rely=0.5)
        masterFrame.set('shopping')  # setting to bring back to the "shopping" tab
        # print("Have fun shopping!")  # Debug: print when the user is back at the shopping tab

#function to get image from folder and return default image
def get_image():
    #try to get an image with the name being the code of the selected item
    try:
        output = Image.open(f'resources/{selectedItem}.jpg')
        return output, output
    except:
        #if it does not exist, set a default photo
        dark = Image.open('resources/default_logo_dark.png')
        light = Image.open('resources/default_logo_light.png')
        return dark, light


# function to get information from json file
# Takes argument "info" which is the key with which the data is stored
def get_card_info(info):
    # try opening file
    try:
        with open('resources/card_info.json') as file:
            # try reading the file
            try:
                data = json.load(file)
            # if cannot read file, data is empty
            except json.JSONDecodeError:
                data = []
    # if cannot find file, data is empty
    except FileNotFoundError:
        data = []
    # print(data)
    # initialise variable as card not existing
    card_exists = False
    card_info={}
    ###CHATGPT CODE### copied from previous funct
    for i, card in enumerate(data):
        # check if info of the selected card type is saved
        if card['card_type'] == selectedCard:
            card_info = data[i]
            card_exists = True
            # print(f'Information retrieved: {card_info}') #DEBUG: print the info that was retrieved
            break

    # print(data) #Debug: print the data
    # if the card exists, return the data of the selected type
    if card_exists:
        return card_info[info]
    # if card does not exist, return false
    else:
        return False


#call get_items to set itemList
itemList = get_items()

#master frame that contains all the tabs
masterFrame = customtkinter.CTkTabview(master=root)
#pack master frame to window
masterFrame.place(anchor= 'center', relheight = 0.85, relwidth=0.85, relx=0.5, rely=0.5)
masterFrame.pack_propagate(False)

#add tabs to Master frame
masterFrame.add('shopping')
masterFrame.add('cart')
masterFrame.add('settings')

#add additional frames to the root window
checkoutFrame = customtkinter.CTkScrollableFrame(master=root)
choiceFrame = customtkinter.CTkFrame(master= root)
paymentFrame = customtkinter.CTkFrame(master= root)
billFrame = customtkinter.CTkFrame(master= root)
thankyouFrame = customtkinter.CTkFrame(master=root)

#Shopping tab
#frame on the left of the shopping tab, with inputs
leftFrame = customtkinter.CTkFrame(master=masterFrame.tab('shopping'))
leftFrame.grid(column=0, row=0, sticky ='nsew', pady=19)
#frame on the right of the shopping tab with displays like item code and price per item
rightFrame = customtkinter.CTkFrame(master=masterFrame.tab('shopping'))
rightFrame.grid(column=1, row=0, sticky ='nsew', pady=19)
#configure rows and columns of shopping tab
masterFrame.tab('shopping').rowconfigure(0,weight = 1)
masterFrame.tab('shopping').columnconfigure(0,weight =2)
masterFrame.tab('shopping').columnconfigure(1,weight =1)

#labels and widgets
#combo box to select category, calls cat_callback function when an option is selected
catComboBox = customtkinter.CTkComboBox(master=leftFrame, values=list(catalog.keys()), command=cat_callback)
catComboBox.pack(pady=12, padx=10)
#combo box to select item, calls item_callback function when an option is selected
snComboBox = customtkinter.CTkComboBox(master=leftFrame, values=itemList, command=item_callback)
snComboBox.pack(padx=10,pady=12)
#frame to hold buttons and the label to show amount
buttonFrame = customtkinter.CTkFrame(master=leftFrame)
buttonFrame.pack(padx=10,pady=12)   #pack button frame
#configure button frame columns
buttonFrame.columnconfigure(0,weight=2)
buttonFrame.columnconfigure(1,weight=1)
buttonFrame.columnconfigure(2,weight=2)
#plus button, calls plus_button when pressed -> increments value in cart by 1
addButton = customtkinter.CTkButton(master=buttonFrame, text='+', font = ('Roboto', 24),
                                    command=lambda :plus_button(selectedItem), width=50)
addButton.grid(column = 2,row = 0) #column changed
#label that shows number of items in cart
itemCountLabel = customtkinter.CTkLabel(master=buttonFrame, text=str(cart[selectedCat][selectedItem]))
itemCountLabel.grid(column = 1, row = 0, padx=12)
#minus button, calls sub_button when pressed -> decrements value in cart by 1
subButton = customtkinter.CTkButton(master=buttonFrame, text='-', font = ('Roboto', 24),
                                    command=lambda: sub_button(selectedItem,False), width=50)
subButton.grid(column = 0, row=0) #column changed
amountEntry=customtkinter.CTkEntry(master=leftFrame,placeholder_text=str(cart[selectedCat][selectedItem]))
amountEntry.pack(padx=12,pady=12)
#on key press, run validate_key
amountEntry.bind('<KeyPress>',validate_key_int)
#on enter press, run set_amt
amountEntry.bind('<Return>',lambda event: set_amt(event, sn=selectedItem,is_cart=False, entry='amountEntry'))
dark, light = get_image()
itemImage = customtkinter.CTkImage(light_image=light,
                                   dark_image = dark,
                                   size=(90,90))
imageLabel = customtkinter.CTkLabel(rightFrame, image=itemImage, text='')
imageLabel.pack(padx=10, pady=0)
#label that displays item code in right frame of shopping tab
codeLabel = customtkinter.CTkLabel(master=rightFrame, text=selectedItem)
codeLabel.pack(padx=10, pady=10)
#Label that displays price of item in right frame of shopping tab
priceLabel=customtkinter.CTkLabel(master=rightFrame, text = f'${catalog[selectedCat][selectedItem]['price']}')
priceLabel.pack(padx=10,pady=10)
shopSubtotalLabel = customtkinter.CTkLabel(master=rightFrame, text=(f'Subtotal: ${subtotal:.2f}'))
shopSubtotalLabel.pack(padx=10,pady=10)

#Setting tab
appearanceComboBox = customtkinter.CTkOptionMenu(master=masterFrame.tab('settings'), values=["Light", "Dark", "System"],
                                                          command=appearance_callback)
appearanceComboBox.pack(pady=10)
appearanceComboBox.set("Dark")
scalingComboBox = customtkinter.CTkOptionMenu(masterFrame.tab("settings"), values=["80%", "90%", "100%", "110%", "120%",
                                                                                   "130%", "140%", "150%"],
                                              command=scaling_callback)
scalingComboBox.pack(pady=10)
scalingComboBox.set("100%")

#Cart tab
#create scrollable 'cart' frame in the 'cart' tab
cartFrame = customtkinter.CTkScrollableFrame(master=masterFrame.tab('cart'))
cartFrame.pack(side='top',fill='both', expand=True)

#button to lead to the "checkout frame", calls checkout_button function when an option is selected
checkoutButton = customtkinter.CTkButton(master=masterFrame.tab('cart'),text='Checkout',command=checkout_button)
checkoutButton.pack(side="bottom",padx=0,pady=12,ipady=5)

#Checkout frame
#label that displays subtotal in checkout tab
subtotalLabel = customtkinter.CTkLabel(master=checkoutFrame, text=(f'Subtotal: ${subtotal:.2f}'))
subtotalLabel.pack(padx=10,pady=12)
#label to display total after gst in checkout tab
totalLabel = customtkinter.CTkLabel(master=checkoutFrame, text=('Total: $' + str(total)))
totalLabel.pack(padx=10, pady=12)
#Label to display GST amount in checkout tab
gstLabel = customtkinter.CTkLabel(master=checkoutFrame, text=f"GST: ${gstAmt:.2f}")
gstLabel.pack(padx=10,pady=12)
#Combo box to select discount. calls discount_Callback function
discountComboBox = customtkinter.CTkComboBox(master=checkoutFrame, values=list(discounts), command=discount_callback)
discountComboBox.pack(padx=10,pady=12)
#label to show selected discount in checkout tab
discountLabel = customtkinter.CTkLabel(master=checkoutFrame, text=f'Discount: {(discounts[selectedDiscount] * 100)}%')
discountLabel.pack(padx=10,pady=12)
#label to show amount of discount given
discountAmountLabel = customtkinter.CTkLabel(master=checkoutFrame, text=f'Discount amount: ${discountAmount}')
discountAmountLabel.pack(padx=10,pady=12)
#label to show final cost after discount
afterDiscountLabel = customtkinter.CTkLabel(master=checkoutFrame, text=f'Total after discount ${afterDiscount}')
afterDiscountLabel.pack(padx=10,pady=12)
#button to lead to the "choice frame", calls payment_button function when an option is selected
paymentButton = customtkinter.CTkButton(master=checkoutFrame,text="Continue Payment",command=payment_button)
paymentButton.pack(side="bottom",padx=10,pady=(15,5))
#button to return back to the 'cart tab', calls back_button function when an option is selected
backButton = customtkinter.CTkButton(master=checkoutFrame,text="Back",command=back_button)
backButton.pack(side="bottom",padx=10,pady=(5,10))


#Choice frame
#Displays Label and Radio Buttons in the "choice frame"
choiceLabel= customtkinter.CTkLabel(master=choiceFrame,text="Choose Payment Method")
choiceLabel.place(anchor='center', relx= 0.5, rely= 0.3)
#setting default value for the radio button
radio_default = customtkinter.IntVar(value=0)
#setting values for each option, calls pay_method function when an option is selected
choice1= customtkinter.CTkRadioButton(master=choiceFrame,text= "Debit Card",variable=radio_default, value= 1,
                                      command=pay_method)
choice1.place(anchor='center', relx= 0.5, rely= 0.5)
choice2= customtkinter.CTkRadioButton(master=choiceFrame,text= "Credit Card",variable=radio_default, value= 2,
                                      command=pay_method)
choice2.place(anchor='center', relx= 0.5, rely= 0.6)

#Payment frame
#Displays Labels in column 0 of the "payment frame"
card_label = customtkinter.CTkLabel(master=paymentFrame, text= "Card Number")
card_label.grid(row=0, column=0, padx=5, pady=5, sticky ='E')
date_label = customtkinter.CTkLabel(master=paymentFrame, text= "Expiry Date")
date_label.grid(row=1, column=0, padx=5, pady=5, sticky ='E')
cvv_label = customtkinter.CTkLabel(master=paymentFrame, text= "CVV")
cvv_label.grid(row=2, column=0, padx=5, pady=5, sticky ='E')
address_label = customtkinter.CTkLabel(master=paymentFrame, text= "Address")
address_label.grid(row=3, column=0, padx=5, pady=5, sticky ='E')
#Displays Entry Widgets in column 1 of the "payment frame"
cardEntry = customtkinter.CTkEntry(master=paymentFrame, placeholder_text="eg- 1234 5678 9123 4567", width=190)
cardEntry.grid(row= 0, column= 1, padx=5, pady=5, sticky ='W')
dateEntry = customtkinter.CTkEntry(master=paymentFrame, placeholder_text= "MM/YY", width=190)
dateEntry.grid(row= 1, column= 1, padx=5, pady=5, sticky ='W')
cvvEntry = customtkinter.CTkEntry(master=paymentFrame, placeholder_text= "777", width=190)
cvvEntry.grid(row=2, column=1, padx=5, pady=5, sticky ='W')
addressEntry = customtkinter.CTkEntry(master=paymentFrame, placeholder_text="S569830, #02-1234", width=190)
addressEntry.grid(row=3, column=1, padx=5, pady=5, sticky ='W')

#setting the default value for the checkbox
save_info_default = customtkinter.IntVar(value=0)
save_allInfo = customtkinter.CTkCheckBox(master=paymentFrame, text="Save information for next purchase",
                                         variable=save_info_default, onvalue=1)
save_allInfo.grid(sticky= 'EW', columnspan= 2 , padx=20, pady=(19,5))
#calls card_validation function when an option is selected
place_order= customtkinter.CTkButton(master=paymentFrame, text= "Place Order", command=card_validation)
place_order.grid(sticky= 'EW', padx=10, pady=19)

#Configure rows and columns, centering the grid in the "payment frame"
paymentFrame.grid_rowconfigure((0,1,2,3), weight=1)
paymentFrame.grid_columnconfigure((0,1),weight=1)

#on key press, run respective validation function
cardEntry.bind('<KeyPress>', validate_key_int)
dateEntry.bind('<KeyPress>', validate_date_key)
cvvEntry.bind('<KeyPress>', validate_key_int)
addressEntry.bind('<KeyPress>', validate_address_key)
#on any key release, run respective validation function
cardEntry.bind('<KeyRelease>', validate_card_no_length)
dateEntry.bind('<KeyRelease>', validate_date_length)
cvvEntry.bind('<KeyRelease>', validate_cvv_length)
addressEntry.bind('<KeyRelease>', validate_address_length)

#Bill Frame
detailFrame = customtkinter.CTkScrollableFrame(master=billFrame) #creating scrollable frame in the 'bill' frame
detailFrame.pack(side='top', fill='both', expand=True)
detailLabel= customtkinter.CTkLabel(master=detailFrame,text="Payment Detail",font=('Arial',16,'bold'))
detailLabel.pack(side="top",padx=10,pady=10)
billdetialLabel = customtkinter.CTkLabel(master=detailFrame,text="Billing Address:",font=('Arial',14,'bold'))
billdetialLabel.pack(padx=10,pady=(10,0))
#Label to display the address, either new info or existed data
billtextLabel = customtkinter.CTkLabel(master=detailFrame,text=f'{billtext}',padx=10,pady=5)
billtextLabel.pack(padx=10,pady=(0,10))
#Label to display selected card
selectedCardLabel= customtkinter.CTkLabel(master=detailFrame,text=f"Payment Method: {selectedCard}",font=('Arial',14,'bold'))
selectedCardLabel.pack(padx=10,pady=12)
#Labels for billing statement
billSubTLabel = customtkinter.CTkLabel(master=detailFrame, text=(f'Subtotal: ${subtotal:.2f}'))
billSubTLabel.pack(padx=10,pady=5)
billDiscountLabel = customtkinter.CTkLabel(master=detailFrame, text=f'Discount amount: ${discountAmount}')
billDiscountLabel.pack(padx=10,pady=5)
taxLabel = customtkinter.CTkLabel(master=detailFrame, text= "Taxes included")
taxLabel.pack(padx=10,pady=(5,0))
billGSTLabel = customtkinter.CTkLabel(master=detailFrame, text=f"GST: ${gstAmt:.2f}")
billGSTLabel.pack(padx=10,pady=(0,5))
billTotalLabel = customtkinter.CTkLabel(master=detailFrame, text=f'Total ${afterDiscount}',font=('Arial',16,'bold'))
billTotalLabel.pack(padx=10,pady=(5,12))
#button to leave 'bill' frame, calls okButton function when an option is selected
okButton = customtkinter.CTkButton(master=billFrame,text='Ok',command=okButton)
okButton.pack(side='bottom',pady=12,ipadx=5)

#Thank You frame
#Displays label and "Logo" image in "thank you frame"
custom_font = ('Times New Roman',25)
thankyouLabel = customtkinter.CTkLabel(master=thankyouFrame, text="Thank you for shopping with us!", font=custom_font)
thankyouLabel.pack(padx=10, pady=(10,5))
darkLogo = Image.open('resources/Final_logo_dark.png')
lightLogo = Image.open('resources/Final_logo_light.png')
logoImage = customtkinter.CTkImage(light_image=lightLogo, dark_image=darkLogo,size=(400,400))
logoLabel = customtkinter.CTkLabel(thankyouFrame,image=logoImage,text='')
logoLabel.pack(fill='both',expand=True)
#Exit the program when an option is selected
exitButton = customtkinter.CTkButton(master=thankyouFrame, text="Exit", command=root.destroy)
exitButton.pack(side='bottom',pady=(0,15))

# root.bind('<Configure>', update_img)
#start customtkinter window
root.mainloop()