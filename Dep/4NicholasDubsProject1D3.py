###################################
#4NicholasDubsUITestFile
#Nicholas Dubs
#ECE2404 Group 5
#Group Project 1
#Refinging UI adding rest of functionality i.e cart view
#Using TabView instead of forgetting nd repacking frames
#03/07/24
##################################
#import customTkinter for ui
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

#Discounts with name, and discount amount as a percentage % = value*100
discounts = {"None" : 0,
             "Senior" : 0.1,
             "Member" : 0.08,
             "NS man": 0.05}


#Declaring variables
#Selected item from category
selectedSn = "N32"
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
#set title
root.title("Shop")
#set minimum window size
root.minsize(410,360)

#function run when plus button is pressed
def plus_buton():
    #find location in cart that corresponds to selected category and item and increment by 1
    cart[selectedCat][selectedSn] += 1
    #print(cart) #Debug print cart
    #duh
    update_labels()

    # function run when plus button is pressed

def sub_button():
    #if the value of the corresponding spot in cart is more than 0 subtract by 1
    if cart[selectedCat][selectedSn]>0:
        cart[selectedCat][selectedSn] -= 1
    #if it is 0 then print 'cant go below 0' and dont reduce by 1
    else:
        print("can't go below 0")
    update_labels()
    #print(cart) #Debug print cart

#function called when category dropbox value is selected
def cat_callback(choice):
    #set global variables
    global selectedCat, itemList,selectedSn
    print(f'combobox dropdown clicked {choice}'  # debug print the selected cat
          # f' : {menu[selectedCat][0]}' #Debug print the name
          )
    selectedCat = choice
    #set item list to the new items in the selected cat
    itemList = get_items()
    temp = list(catalog[selectedCat])
    selectedSn=temp[0]


    update_labels()


#Function called when item dropdown is selected
def sn_callback(choice):
    #declaring global vars
    global selectedSn
    print(choice) #debug pritn selected item
    #check which item name matches an item in the selected category
    for sn in catalog[selectedCat]:
        # print(sn) #Debug print sn
        #when the selected item is matched set the selected item to selectedSbn
        # print(catalog[selectedCat][sn]['name']) #debug: print name of item at 'sn'
        if choice == catalog[selectedCat][sn]['name']:
            selectedSn=sn
    print(selectedSn) #Debub print the selected sn

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
    gstAmt = subtotal*.09
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

    #update labels to reflect the totals
    discountAmountLabel.configure(text=f'Discount amount: ${discountAmount:.2f}')
    subtotalLabel.configure(text=f'Subtotal: ${subtotal:.2f}')
    shopSubtotalLabel.configure(text=f'Subtotal: ${subtotal:.2f}')
    totalLabel.configure(text=f'Total: ${total:.2f}')
    gstLabel.configure(text=f"GST: ${gstAmt:.2f}")
    afterDiscountLabel.configure(text=f'Total after discount ${afterDiscount:.2f}')


#function to update labels
def update_labels():
    #declare global variables
    global itemList, catalog,selectedSn,selectedCat
    #update the item combobox options
    snComboBox.configure(values=itemList)
    #update the label that displays the item code
    codeLabel.configure(text=selectedSn)
    #update the label that shows number of items in cart
    itemCountLabel.configure(text=str(read_cart()))
    #update the label that shows selected discount
    discountLabel.configure(text=f'Discount: {(discounts[selectedDiscount]*100)}%')
    #update label that shows price of item
    priceLabel.configure(text = f'${catalog[selectedCat][selectedSn]['price']}')
    #if the value in amount entry is not empty, clear it
    #When using amountEntry.delete() subsequent entries return empty when enter is pressed
    # if amountEntry.get()!='':
    #     amountEntry.delete(0,'end')
    #update the placeholder text in the entry to the amount in cart: doesnt do anything if entry isnt cleared
    amountEntry.configure(placeholder_text=cart[selectedCat][selectedSn])

    #Run function to update cart label to show item names
    show_cart()
    #run function to calculate sum
    calculate_sum()

#function to read cart at selected category and selected item
def read_cart():
    # print(cart)
    # print(selectedCat)
    # print(selectedSn)
    return cart[selectedCat][selectedSn]

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
    cart[selectedCat][selectedSn]=int(amountEntry.get())
    #call update labels function
    update_labels()



#call get_items to set itemList
itemList = get_items()
#master frame that contains all the tabs
masterFrame = customtkinter.CTkTabview(master=root)

#pack master frame to window
masterFrame.place(anchor= 'center', relheight = .85, relwidth=.85, relx=.5, rely=.5)
masterFrame.pack_propagate(False)

#add tabs to master frame
masterFrame.add('shopping')
masterFrame.add('cart')
masterFrame.add('checkout')
checkoutFrame = customtkinter.CTkScrollableFrame(master=masterFrame.tab('checkout'))
checkoutFrame.place(anchor= 'center', relheight = .8, relwidth=.65, relx=.5, rely=.5)

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

#combo box to select category, calls cat_callback function when an option is selected
catComboBox = customtkinter.CTkComboBox(master=leftFrame, values=list(catalog.keys()), command=cat_callback)
catComboBox.pack(pady=12, padx=10)
#combo box to select item, calls sn_callback function when an option is selected
snComboBox = customtkinter.CTkComboBox(master=leftFrame, values=itemList, command=sn_callback)
snComboBox.pack(padx=10,pady=12)
#pack button frame
buttonFrame.pack(padx=10,pady=12)
#configure button frame columns
buttonFrame.columnconfigure(0,weight=2)
buttonFrame.columnconfigure(1,weight=1)
buttonFrame.columnconfigure(2,weight=2)
#plus button, calls plus_button when pressed -> increments value in cart by 1
addButton = customtkinter.CTkButton(master=buttonFrame, text='+', font = ('Roboto', 24), command=plus_buton, width=50)
addButton.grid(column = 0,row = 0)
#label that shows number of items in cart
itemCountLabel = customtkinter.CTkLabel(master=buttonFrame, text=str(read_cart()))
itemCountLabel.grid(column = 1, row = 0, padx=12)
#minus button, calls sub_button when pressed -> decrements value in cart by 1
subButton = customtkinter.CTkButton(master=buttonFrame, text='-', font = ('Roboto', 24), command=sub_button, width=50)
subButton.grid(column = 2, row=0)

#Entry box
amountEntry=customtkinter.CTkEntry(master=leftFrame,placeholder_text=str(cart[selectedCat][selectedSn]))
amountEntry.pack(padx=12,pady=12)
#on key press run validate_key
amountEntry.bind('<KeyPress>',validate_key)
#on enter press run set_amt
amountEntry.bind('<Return>',set_amt)

#label that displays item code in right frame of shopping tap
codeLabel = customtkinter.CTkLabel(master=rightFrame, text=selectedSn)
codeLabel.pack(padx=10, pady=12)
#Label that displays price of item in right frame of shopping tab
priceLabel=customtkinter.CTkLabel(master=rightFrame, text = f'${catalog[selectedCat][selectedSn]['price']}')
priceLabel.pack(padx=10,pady=12)
shopSubtotalLabel = customtkinter.CTkLabel(master=rightFrame, text=('Subtotal: $' + str(subtotal)))
shopSubtotalLabel.pack(padx=10,pady=12)
#label that displays subtotal in checkout tab
subtotalLabel = customtkinter.CTkLabel(master=checkoutFrame, text=('Subtotal: $' + str(subtotal)))
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
#label that displays the cart
cartLabel = customtkinter.CTkLabel(master=masterFrame.tab('cart'), text = cartOut)
cartLabel.pack(padx=10,pady=12)


#start customtkinter window
root.mainloop()