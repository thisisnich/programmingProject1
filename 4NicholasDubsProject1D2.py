###################################
#4NicholasDubsUITestFile
#Nicholas Dubs
#ECE2404 Group 5
#Group Project 1
#Refinging UI adding rest of functionality i.e cart view
#Using TabView instead of forgetting nd repacking frames
#06/06/24
##################################
#import customTkinter for ui
import customtkinter

#Items in each category, each item has name, serial number and price as float
drinks = [["Neo's Green Tea", "N32", 3],["Drink 2","C12",2.85],["Drink 3","D120",4]]
beer = [["Beer 1", "C13", 3],["Beer 2","C14",2.85]]
frozen = [["frozen 1", "C15", 3],["frozen 2","C16",2.85]]
household = [["Household 1", "C17", 3],["Household 2","C18",2.85]]
snacks = [["Snack 1", "C19", 3],["Snack 2","C20",2.85]]

#final catalog with category names, category items and category serial number
catalog = [["Drinks", drinks, "CD20"], ["Beer", beer, "CB20"], ["Frozen", frozen, "CF30"], ["Household", household, "CH40"], ["Snacks", snacks, "CS50"]]
#initialize cart as an empty list
cart = []

#Discounts with name, and discount amount as a percentage % = value*100
discounts = [["None",0],["Senior", 0.1],['Member',.08],["NS man",.05]]

#Declaring variables
#Selected item from category
selectedSn = 0
#Selected Category
selectedCat = 0
#Selected discount type
selectedDiscount = 0
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

#set the size of cart as an array that has the same dimensions as catalog
#so if catalog size chagnes cart changes automatically
for i in range(len(catalog)):
    a = len(catalog[i][1])
    b = [0]*a
    #print(b) #Debug: priny empty list of each cat
    cart.append(b)
    #print(cart) #Debug: Print empty cart up to that point

#print(cart) #Debug print cart to console
#appearance mode set to dark
customtkinter.set_appearance_mode("dark")
#colour theme set to dark blue
customtkinter.set_default_color_theme("dark-blue")

#define root window
root = customtkinter.CTk()
#set default size
root.geometry("500x350")

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
        print("cant go below 0")
    update_labels()
    #print(cart) #Debug print cart

#function called when category dropbox value is selected
def cat_callback(choice):
    #set global variables
    global selectedCat
    global itemList
    #while there are categories in the catalog
    for i in catalog:
        #print(i) #Debug print i
        # print(i[0]) #Debug print category name
        #check which value matches the selected item
        if choice == i[0]:
            #set selectedCat to that value
            selectedCat = catalog.index(i)
    # print(selectedCat) #Debug print the selected category

    print(f'combobox dropdown clicked {choice}' #debug print the selected cat
          #f' : {menu[selectedCat][0]}' #Debug print the name
          )
    #set item list to the new items in the selected cat
    itemList = get_items()
    update_labels()


#Function called when item dropdown is selected
def sn_callback(choice):
    #declaring global vars
    global selectedSn
    # print(choice) #debug pritn selected item
    #check which item name matches an item in the selected category
    for i in catalog[selectedCat][1]:
        #print(i) #Debug print i
        #when the selected item is matched set the selected item to selectedSbn
        if choice == i[0]:
            selectedSn=catalog[selectedCat][1].index(i)
    #print(selectedSn) #Debub print the selected sn

    print(f'combobox dropdown clicked {choice}' #Debug print choice
          #f' : {menu[selectedCat][0]}' #Debug print choice name
          )
    update_labels()

#Function called when discount dropdown selected
def discount_callback(choice):
    #Declare globals
    global selectedDiscount
    #check which discount name matches the selected discount
    for i in discounts:
        if choice == i[0]:
            #set selected discount to the correspnding precentage
            selectedDiscount = discounts.index(i)
    update_labels()


#function to get items in a category
def get_items():
    #initialise a temporary list
    tempList = []
    #while there is items in the selected category, add the item to the temp list
    for i in catalog[selectedCat][1]:
        tempList.append(i[0])
    return tempList

#calculation function
def calculate_sum():
    #declare globals
    global subtotal,total, gstAmt, discountAmount, afterDiscount
    #declare workig value
    tempCost = 0
    #while there are items in cart, find the corresponding price, and multiply number of items in cart by price
    for i in range(len(cart)):
        for y in range(len(cart[i])):
            # print(cart[i][y])         #Debug: print value in cart
            # print(menu[i][1][y][2])   #Debug: print corresponding price
            #add the total price to tempCost
            tempCost += (cart[i][y])*(catalog[i][1][y][2])
            # print(tempCost)           #Debug: print current temporary Value
    #Set subtotal to the temporary cost
    subtotal=tempCost
    #Print subtotal
    print(f'Subtotal ${subtotal:.2f}')
    #Calculate toatal with GST
    total=subtotal*1.09
    #Print total after GST
    print(f'Total ${total:.2f}')
    #calculate the amount of gst charged
    gstAmt = subtotal*.09
    #Pring amount of gst charged
    print(f'GST ${gstAmt:.2f}')
    #print(discounts[selectedDiscount])  #Debug: print selected discount
    #Calculate the amount of discount given based on the selected discount
    discountAmount = total*discounts[selectedDiscount][1]
    #Print the amount of discount deducted
    print(f'Discount amt: {discountAmount:.2f}')
    #calculate total after discount
    afterDiscount = total*(1-discounts[selectedDiscount][1])
    #print total after discount
    print(f'Total after discount ${afterDiscount:.2f}')

    #update labels to reflect the totals
    discountAmountLabel.configure(text=f'Discount amount: ${discountAmount:.2f}')
    subtotalLabel.configure(text=f'subtotal: ${subtotal:.2f}')
    totalLabel.configure(text=f'total: ${total:.2f}')
    gstLabel.configure(text=f"GST: ${gstAmt:.2f}")
    afterDiscountLabel.configure(text=f'Total after discount ${afterDiscount:.2f}')


#function to update labels
def update_labels():
    #declare global variables
    global itemList, catalog,selectedSn,selectedCat
    #update the item combobox options
    snComboBox.configure(values=itemList)
    #update the label that displays the item code
    codeLabel.configure(text=catalog[selectedCat][1][selectedSn][1])
    #update the label that shows number of items in cart
    itemCountLabel.configure(text=str(read_cart()))
    #update the label that shows selected discount
    discountLabel.configure(text=f'Discount: {(discounts[selectedDiscount][1]*100)}%')
    #update label that shows price of item
    priceLabel.configure(text = f'${catalog[selectedCat][1][selectedSn][2]}')
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
    output=cart[selectedCat][selectedSn]
    return output

#function to update label to show cart to user
def show_cart():
    #declare globals
    global cartOut
    #initialise empty cart output
    cartOut=''
    #while there are items in cart get the value and item name
    for i in range(len(cart)):
        for y in range(len(cart[i])):
            # print(cart[i][y]) #Debug print amount in cart
            #check if the value in cart is more than 0
            if cart[i][y] >=1:
                # print(menu[i][1][y][0])       #Debug print item name
                #total cost of item is the amount of items in cart, multiplied by cost per item
                itemCost = cart[i][y] * catalog[i][1][y][2]
                # print(itemCost)           #Debug: Print total item cost
                # print(f'{menu[i][1][y][0]:.<16}{cart[i][y]:.^8}${itemCost}')      #Debug: Print a the line that will be added to cart
                #add item name, amount, and total cost of item to cart out as well as a new line
                cartOut += f'{catalog[i][1][y][0]:<16}{cart[i][y]:^8}${itemCost:.2f}\n'
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
masterFrame = customtkinter.CTkTabview(master=root,)

#pack master frame to window
masterFrame.pack()

#add tabs to master frame
masterFrame.add('shopping')
masterFrame.add('cart')
masterFrame.add('checkout')

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
catComboBox = customtkinter.CTkComboBox(master=leftFrame, values=[cat[0] for cat in catalog], command=cat_callback)
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


codeLabel = customtkinter.CTkLabel(master=rightFrame, text=catalog[selectedCat][1][selectedSn][1])
codeLabel.pack(padx=10, pady=12)
priceLabel=customtkinter.CTkLabel(master=rightFrame, text = f'${catalog[selectedCat][1][selectedSn][2]}')
priceLabel.pack(padx=10,pady=12)
subtotalLabel = customtkinter.CTkLabel(master=masterFrame.tab('checkout'), text=('subtotal: $' + str(subtotal)))
subtotalLabel.pack(padx=10,pady=12)
totalLabel = customtkinter.CTkLabel(master=masterFrame.tab('checkout'), text=('total: $' + str(total)))
totalLabel.pack(padx=10, pady=12)
gstLabel = customtkinter.CTkLabel(master=masterFrame.tab('checkout'), text=f"GST: ${gstAmt:.2f}")
gstLabel.pack(padx=10,pady=12)
discountComboBox = customtkinter.CTkComboBox(master=masterFrame.tab('checkout'), values=[i[0] for i in discounts], command=discount_callback)
discountComboBox.pack(padx=10,pady=12)
discountLabel = customtkinter.CTkLabel(master=masterFrame.tab('checkout'), text=f'Discount: {(discounts[selectedDiscount][1] * 100)}%')
discountLabel.pack(padx=10,pady=12)
discountAmountLabel = customtkinter.CTkLabel(master=masterFrame.tab('checkout'), text=f'Discount amount: ${discountAmount}')
discountAmountLabel.pack(padx=10,pady=12)
afterDiscountLabel = customtkinter.CTkLabel(master=masterFrame.tab('checkout'), text=f'Total after discount ${afterDiscount}')
afterDiscountLabel.pack(padx=10,pady=12)
cartLabel = customtkinter.CTkLabel(master=masterFrame.tab('cart'), text = cartOut)
cartLabel.pack(padx=10,pady=12)


root.mainloop()