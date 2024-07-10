import customtkinter
from customtkinter import *
catalog = {
    "Drinks": {
        "N32": {"name": "Neo's Green Tea", "price": 3},
        "C12": {"name": "Drink 2", "price": 2.85},
        "D120": {"name": "Drink 3", "price": 4},
        "N14": {"name": "Nirigold UHT Milk", "price": 4.5}
    },
    "Beer": {
        "C13": {"name": "Beer 1", "price": 3},
        "C14": {"name": "Beer 2", "price": 2.85}
    },
    "Frozen": {
        "C15": {"name": "Frozen 1", "price": 3},
        "C16": {"name": "Frozen 2", "price": 2.85}
    },
    "Household": {
        "C17": {"name": "Household 1", "price": 3},
        "C18": {"name": "Household 2", "price": 2.85}
    },
    "Snacks": {
        "C19": {"name": "Snack 1", "price": 3},
        "C20": {"name": "Snack 2", "price": 2.85}
    }
}

print(catalog)
cart = {category: {sn: 0 for sn in items} for category, items in catalog.items()}
print(cart)
#for cart buttons
globals_namespace = globals() #add

#Discounts with name, and discount amount as a percentage % = value*100
discounts = {"None" : 0,
             "Senior" : 0.1,
             "Member" : 0.08,
             "NS man": 0.05}


#Declaring variables
#Selected item from category
selectedItem = "N32"
#Selected Category
selectedCat = "Drinks"
#Selected discount type
selectedDiscount = "None"
#Subtotal before gst
subtotal = 0
#Total after gst
total = 0
#Amount of gst
gstAmt = 0
#Amount of discount
discountAmount = 0
#Total after discount
afterDiscount = 0
#Debug value to print cart
cartOut = ''

###ADD
payment_method= ["Debit Card","Credit Card"]

#appearance mode set to dark
customtkinter.set_appearance_mode("dark")
#colour theme set to dark blue
customtkinter.set_default_color_theme("dark-blue")

#define root window
root = customtkinter.CTk()
#set default size
root.geometry("410x360")
#set icon
root.iconbitmap('f.ico')
#set minimum window size
root.minsize(410,360)

#function run when plus button is pressed
def plus_buton():
    #find location in cart that corresponds to selected category and item and increment by 1
    cart[selectedCat][selectedItem] += 1
    #print(cart) #Debug print cart
    #duh
    update_labels()

def sub_button():
    #if the value of the corresponding spot in cart is more than 0 subtract by 1
    if cart[selectedCat][selectedItem]>0:
        cart[selectedCat][selectedItem] -= 1
    #if it is 0 then print 'cant go below 0' and dont reduce by 1
    else:
        print("can't go below 0")
    update_labels() #####
    #print(cart) #Debug print cart

#function called when category dropbox value is selected
def cat_callback(choice):
    #set global variables
    global selectedCat, itemList,selectedItem
    print(f'combobox dropdown clicked {choice}'  # debug print the selected cat
          # f' : {menu[selectedCat][0]}' #Debug print the name
          )
    selectedCat = choice
    #set item list to the new items in the selected cat
    itemList = get_items()
    temp = list(catalog[selectedCat])
    selectedItem=temp[0]
    update_labels()

#Function called when item dropdown is selected
def item_callback(choice):
    #declaring global vars
    global selectedItem
    print(choice) #debug pritn selected item
    #check which item name matches an item in the selected category
    for sn in catalog[selectedCat]:
        # print(sn) #Debug print sn
        #when the selected item is matched set the selected item to selectedSbn
        # print(catalog[selectedCat][sn]['name']) #debug: print name of item at 'sn'
        if choice == catalog[selectedCat][sn]['name']:
            selectedItem=sn
    print(selectedItem) #Debub print the selected sn

    print(f'combobox dropdown clicked {choice}' #Debug print choice
          #f' : {menu[selectedCat][0]}' #Debug print choice name
          )
    update_labels()

#Function called when discount dropdown selected
def discount_callback(choice):
    #Declare globals
    global selectedDiscount
    #check which discount name matches the selected discount
    selectedDiscount=choice
    update_labels()

#function to get items in a category
def get_items():
    return [catalog[selectedCat][sn]["name"] for sn in catalog[selectedCat]]

#calculation function
def calculate_sum():
    #declare globals
    global subtotal,total, gstAmt, discountAmount, afterDiscount
    #declare workig value
    tempCost = 0
    #while there are items in cart, find the corresponding price, and multiply number of items in cart by price
    for cat in cart:
        for sn in cart[cat]:
            #print(cat,sn)
            # print(cart[i][y])         #Debug: print value in cart
            # print(menu[i][1][y][2])   #Debug: print corresponding price
            #add the total price to tempCost

            tempCost += cart[cat][sn]*catalog[cat][sn]['price']
            # print(tempCost)           #Debug: print current temporary Value
    #Set subtotal to the temporary cost
    subtotal=tempCost
    #Print subtotal
    # print(f'Subtotal ${subtotal:.2f}') #Debug print new subtotal
    #Calculate toatal with GST
    total=subtotal*1.09
    #Print total after GST
    # print(f'Total ${total:.2f}') # Debug: print new total
    #calculate the amount of gst charged
    gstAmt = subtotal*0.09
    #Pring amount of gst charged
    # print(f'GST ${gstAmt:.2f}') #Debug: print new gst amount
    #print(discounts[selectedDiscount])  #Debug: print selected discount
    #Calculate the amount of discount given based on the selected discount
    # print(selectedDiscount) #Debug: print selected discount
    discountAmount = total*discounts[selectedDiscount]
    #Print the amount of discount deducted
    # print(f'Discount amt: {discountAmount:.2f}') #Debug: print new discount amount
    #calculate total after discount
    afterDiscount = total*(1-discounts[selectedDiscount])
    #print total after discount
    # print(f'Total after discount ${afterDiscount:.2f}') #new price after discount

    # update labels to reflect the totals
    discountAmountLabel.configure(text=f'Discount amount: ${discountAmount:.2f}')
    subtotalLabel.configure(text=f'Subtotal: ${subtotal:.2f}')
    shopSubtotalLabel.configure(text=f'Subtotal: ${subtotal:.2f}')
    totalLabel.configure(text=f'Total: ${total:.2f}')
    gstLabel.configure(text=f"GST: ${gstAmt:.2f}")
    afterDiscountLabel.configure(text=f'Total after discount ${afterDiscount:.2f}')

#function to update labels
def update_labels():
    #declare global variables
    global itemList, catalog,selectedItem,selectedCat
    #update the item combobox options
    snComboBox.configure(values=itemList)
    #update the label that displays the item code
    codeLabel.configure(text=selectedItem)
    #update the label that shows number of items in cart
    itemCountLabel.configure(text=str(read_cart()))
    #update the label that shows selected discount
    discountLabel.configure(text=f'Discount: {(discounts[selectedDiscount]*100)}%')
    #update label that shows price of item
    priceLabel.configure(text = f'${catalog[selectedCat][selectedItem]['price']}')
    #if the value in amount entry is not empty, clear it
    #When using amountEntry.delete() subsequent entries return empty when enter is pressed
    # if amountEntry.get()!='':
    #     amountEntry.delete(0,'end')
    #update the placeholder text in the entry to the amount in cart: doesnt do anything if entry isnt cleared
    amountEntry.configure(placeholder_text=cart[selectedCat][selectedItem])

    #Run function to update cart label to show item names
    show_cart()
    #run function to calculate sum
    calculate_sum()

#function to read cart at selected category and selected item
def read_cart():
    # print(cart)
    # print(selectedCat)
    # print(selectedSn)
    return cart[selectedCat][selectedItem]

#function to update label to show cart to user
def show_cart():
    #declare globals
    global cartOut
    #initialise empty cart output
    cartOut=''
    #while there are items in cart get the value and item name
    for cat in cart:
        for sn in cart[cat]:
            if cart[cat][sn] >=1:
                itemCost = cart[cat][sn]*catalog[cat][sn]['price']
                cartOut += f'{catalog[cat][sn]["name"]:<16}{cart[cat][sn]:^8}${itemCost:.2f}\n'
                make_cart_label(cart[cat][sn], itemCost, catalog[cat][sn]["name"], globals_namespace) #add
    #Update cart label to show cartOut
    cartLabel.configure(text=cartOut)

#function to check that only accepted keys are registered
def validate_key(event):
    #print(event.keysym) #Debug:print key that was pressed
    #only accept digits, backspace, Enter, Left or right
    if not event.char.isdigit() and event.keysym!=('BackSpace' or 'Return' or 'Left' or 'Right'):
        #print('key not accepted')  #Debug: print message when keypress is not accepted
        return 'break'
    # print(amountEntry.get())  #Debug: print current stored value in Entry field
    ####??? After using delete function amountEntry.get() always returns ''

#function called when enter key is pressed
# sets cart at selected category and selected item to value that is in the entry box
def set_amt(event):
    #print('-----')             #Debug: print lines to show what the read input is
    # print(amountEntry.get())  #Debug: print read input
    #print('-----')             #Debug: print lines to show what the read input is
    #set cart value to the value stored in Entry
    cart[selectedCat][selectedItem]=int(amountEntry.get())
    #call update labels function
    update_labels()

###ADD
def checkout_button():
    checkoutFrame.place(anchor= 'center', relheight = 0.8, relwidth=0.65, relx=0.5, rely=0.5)
    subtotalLabel.pack(padx=10,pady=12)
    totalLabel.pack(padx=10, pady=12)
    gstLabel.pack(padx=10,pady=12)
    discountComboBox.pack(padx=10,pady=12)
    discountLabel.pack(padx=10,pady=12)
    discountAmountLabel.pack(padx=10,pady=12)
    afterDiscountLabel.pack(padx=10,pady=12)
    cartLabel.pack(padx=10,pady=12)

###ADD
def back_button():
    checkoutFrame.place_forget()
    masterFrame.place(anchor='center', relheight=0.85, relwidth=0.85, relx=0.5, rely=0.5)
# def ShowChoice():
#     choice= radio_var.get()
#     print(choice,payment_method[choice])

def payment_button():
    global choice
    choice = radio_var.get()
    # print(choice+1, payment_method[choice])
    choiceFrame.place(anchor= 'center', relheight = 0.8, relwidth=0.65, relx=0.5, rely=0.5)
    choice1.place(anchor='center', relx= 0.5, rely= 0.5)
    choice2.place(anchor='center', relx= 0.5, rely= 0.6)

def pay_method():
    paymentFrame.place(anchor= 'center', relheight = 0.8, relwidth=0.65, relx=0.5, rely=0.5)
    choice = radio_var.get()
    # print(choice, payment_method[choice])
    card_label.grid(row=0, column=0)
    password_label.grid(row=1, column=0)
    cardEntry.grid(row= 0, column= 2)
    passwordEntry.grid(row=1, column=2)

#nich add #ask
#change appearance of ui
def appearance_callback(choice: str):
    customtkinter.set_appearance_mode(choice)
def scaling_callback(choice: str):
    new_scaling_float = int(choice.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)

def make_cart_label(amt, price, name, namespace):
    namespace[f'{name}Frame'] = customtkinter.CTkFrame(root)
    namespace[f'{name}Frame'].pack(pady=1)
    namespace[f'{name}Frame'].columnconfigure(0, weight=3)
    # namespace[f'{name}Frame'].columnconfigure(1, weight=1)
    namespace[f'{name}Label'] = customtkinter.CTkLabel(namespace[f'{name}Frame'], text=f'{name:<16}{amt:^8}${price:.2f}')
    namespace[f'{name}Label'].grid(column=0, row = 0)
    namespace[f'{name}Button'] = customtkinter.CTkButton(namespace[f'{name}Frame'],text='Remove', width = 50, command=lambda: remove_cart_label(name, namespace))
    namespace[f'{name}Button'].grid(column=2, row=0, padx=10, pady=5)

def remove_cart_label(name, namespace):
    print("ive run")
    namespace[f'{name}Frame'].pack_forget()


#call get_items to set itemList
itemList = get_items()
#master frame that contains all the tabs
masterFrame = customtkinter.CTkTabview(master=root)

#pack master frame to window
masterFrame.place(anchor= 'center', relheight = 0.85, relwidth=0.85, relx=0.5, rely=0.5)
masterFrame.pack_propagate(False)

#add tabs to master frame
masterFrame.add('shopping')
masterFrame.add('cart')
masterFrame.add('settings') #add
# masterFrame.add('checkout')
checkoutFrame = customtkinter.CTkScrollableFrame(master=root) ###edited
# checkoutFrame.place(anchor= 'center', relheight = .8, relwidth=.65, relx=.5, rely=.5)

###ADD
choiceFrame = customtkinter.CTkFrame(master= root)
paymentFrame = customtkinter.CTkFrame(master= root)

#frame on the left of the shopping tab, with inputs
leftFrame = customtkinter.CTkFrame(master=masterFrame.tab('shopping'))
leftFrame.grid(column=0, row=0, sticky ='nsew', pady=19)
#frame on right of shopping tab with display like item code and price per item
rightFrame = customtkinter.CTkFrame(master=masterFrame.tab('shopping'))
rightFrame.grid(column=1, row=0, sticky ='nsew', pady=19)
#confugure rows and columns of shopping tab
masterFrame.tab('shopping').rowconfigure(0,weight = 1)
masterFrame.tab('shopping').columnconfigure(0,weight =2)
masterFrame.tab('shopping').columnconfigure(1,weight =1)

#frame to hold buttons and the label to show amount
buttonFrame = customtkinter.CTkFrame(master=leftFrame)

##ADD
checkoutButton = customtkinter.CTkButton(master=masterFrame.tab("cart"),text='Checkout',command=checkout_button)
checkoutButton.pack(side="bottom",padx=10,pady=12)
backButton = customtkinter.CTkButton(master=checkoutFrame,text="Back",command=back_button)
backButton.pack(side="bottom",padx=10,pady=12)
paymentButton = customtkinter.CTkButton(master=checkoutFrame,text="Continue Payment",command=payment_button)
paymentButton.pack(side="bottom",padx=10,pady=12)

#combo box to select category, calls cat_callback function when an option is selected
catComboBox = customtkinter.CTkComboBox(master=leftFrame, values=list(catalog.keys()), command=cat_callback)
catComboBox.pack(pady=12, padx=10)
#combo box to select item, calls sn_callback function when an option is selected
snComboBox = customtkinter.CTkComboBox(master=leftFrame, values=itemList, command=item_callback)
snComboBox.pack(padx=10,pady=12)
#pack button frame
buttonFrame.pack(padx=10,pady=12)
#configure button frame columns
buttonFrame.columnconfigure(0,weight=2)
buttonFrame.columnconfigure(1,weight=1)
buttonFrame.columnconfigure(2,weight=2)
#plus button, calls plus_button when pressed -> increments value in cart by 1
addButton = customtkinter.CTkButton(master=buttonFrame, text='+', font = ('Roboto', 24), command=plus_buton, width=50)
addButton.grid(column = 2,row = 0) #column changed
#label that shows number of items in cart
itemCountLabel = customtkinter.CTkLabel(master=buttonFrame, text=str(read_cart()))
itemCountLabel.grid(column = 1, row = 0, padx=12)
#minus button, calls sub_button when pressed -> decrements value in cart by 1
subButton = customtkinter.CTkButton(master=buttonFrame, text='-', font = ('Roboto', 24), command=sub_button, width=50)
subButton.grid(column = 0, row=0) #column changed

#Entry box
amountEntry=customtkinter.CTkEntry(master=leftFrame,placeholder_text=str(cart[selectedCat][selectedItem]))
amountEntry.pack(padx=12,pady=12)
#on key press run validate_key
amountEntry.bind('<KeyPress>',validate_key)
#on enter press run set_amt
amountEntry.bind('<Return>',set_amt)

###ADD
radio_var = customtkinter.IntVar(value=0)
choice1= customtkinter.CTkRadioButton(master=choiceFrame,text= "Debit Card",variable=radio_var, value= 1, command=pay_method)
choice2= customtkinter.CTkRadioButton(master=choiceFrame,text= "Credit Card",variable=radio_var, value= 2, command=pay_method)

card_label = customtkinter.CTkLabel(master=paymentFrame, text= "Card Number")
password_label = customtkinter.CTkLabel(master=paymentFrame, text= "Password")
cardEntry = customtkinter.CTkEntry(master=paymentFrame)
passwordEntry = customtkinter.CTkEntry(master=paymentFrame)

#label that displays item code in right frame of shopping tap
codeLabel = customtkinter.CTkLabel(master=rightFrame, text=selectedItem)
codeLabel.pack(padx=10, pady=12)
#Label that displays price of item in right frame of shopping tab
priceLabel=customtkinter.CTkLabel(master=rightFrame, text = f'${catalog[selectedCat][selectedItem]['price']}')
priceLabel.pack(padx=10,pady=12)
shopSubtotalLabel = customtkinter.CTkLabel(master=rightFrame, text=('Subtotal: $' + str(subtotal)))
shopSubtotalLabel.pack(padx=10,pady=12)

#label that displays subtotal in checkout tab
subtotalLabel = customtkinter.CTkLabel(master=checkoutFrame, text=('Subtotal: $' + str(subtotal)))
### subtotalLabel.pack(padx=10,pady=12)
#label to display total after gst in checkout tab
totalLabel = customtkinter.CTkLabel(master=checkoutFrame, text=('Total: $' + str(total)))
### totalLabel.pack(padx=10, pady=12)
#Label to display GST amount in checkout tab
gstLabel = customtkinter.CTkLabel(master=checkoutFrame, text=f"GST: ${gstAmt:.2f}")
### gstLabel.pack(padx=10,pady=12)
#Combo box to select discount. calls discount_Callback function
discountComboBox = customtkinter.CTkComboBox(master=checkoutFrame, values=list(discounts), command=discount_callback)
### discountComboBox.pack(padx=10,pady=12)
#label to show selected discount in checkout tab
discountLabel = customtkinter.CTkLabel(master=checkoutFrame, text=f'Discount: {(discounts[selectedDiscount] * 100)}%')
### discountLabel.pack(padx=10,pady=12)
#label to show amount of discount given
discountAmountLabel = customtkinter.CTkLabel(master=checkoutFrame, text=f'Discount amount: ${discountAmount}')
### discountAmountLabel.pack(padx=10,pady=12)
#label to show final cost after discount
afterDiscountLabel = customtkinter.CTkLabel(master=checkoutFrame, text=f'Total after discount ${afterDiscount}')
### afterDiscountLabel.pack(padx=10,pady=12)
#label that displays the cart
cartLabel = customtkinter.CTkLabel(master=masterFrame.tab('cart'), text = cartOut)
cartLabel.pack(padx=10,pady=12)

#SETTINGS TAB #add
appearanceComboBox = customtkinter.CTkOptionMenu(master=masterFrame.tab('settings'), values=["Light", "Dark", "System"],
                                                          command=appearance_callback)
appearanceComboBox.pack(pady=10)
appearanceComboBox.set("Dark")
scalingComboBox = customtkinter.CTkOptionMenu(masterFrame.tab("settings"), values=["80%", "90%", "100%", "110%", "120%","130%","140%","150%"],
                                                               command=scaling_callback)
scalingComboBox.pack(pady=10)
scalingComboBox.set("100%")

#start customtkinter window
root.mainloop()

