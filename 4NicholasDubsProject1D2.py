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
    print(b)
    cart.append(b)
    print(cart)

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


def get_items():
    tempList = []
    for i in catalog[selectedCat][1]:
        tempList.append(i[0])


    return tempList
def calculate_sum():
    global subtotal,total, gstAmt, discountAmount, afterDiscount
    tempCost = 0
    for i in range(len(cart)):
        for y in range(len(cart[i])):
            # print(cart[i][y])
            # print(menu[i][1][y][2])
            tempCost += (cart[i][y])*(catalog[i][1][y][2])
            # print(tempCost)
    subtotal=tempCost
    print(f'Subtotal ${subtotal}')
    total=subtotal*1.09
    print(f'Total ${total}')
    gstAmt = subtotal*.09
    print(f'GST ${gstAmt}')
    print(discounts[selectedDiscount])
    discountAmount = total*discounts[selectedDiscount][1]
    print(f'Discount amt: {discountAmount}')
    afterDiscount = total*(1-discounts[selectedDiscount][1])
    print(f'Total after discount ${afterDiscount}')

    discountAmountLabel.configure(text=f'Discount amount: ${discountAmount:.2f}')

    subtotalLabel.configure(text=f'subtotal: ${subtotal:.2f}')
    totalLabel.configure(text=f'total: ${total:.2f}')
    gstLabel.configure(text=f"GST: ${gstAmt:.2f}")
    afterDiscountLabel.configure(text=f'Total after discount ${afterDiscount:.2f}')


def update_labels():
    global itemList, catalog,selectedSn,selectedCat
    snComboBox.configure(values=itemList)
    codeLabel.configure(text=catalog[selectedCat][1][selectedSn][1])
    itemCountLabel.configure(text=str(read_cart()))
    discountLabel.configure(text=f'Discount: {(discounts[selectedDiscount][1]*100)}%')
    priceLabel.configure(text = f'${catalog[selectedCat][1][selectedSn][2]}')
    if amountEntry.get()!='':
        amountEntry.delete(0,'end')
    amountEntry.configure(placeholder_text=cart[selectedCat][selectedSn])

    show_cart()
    calculate_sum()


def read_cart():
    output=cart[selectedCat][selectedSn]
    return output

def show_cart():
    global cartOut
    cartOut=''
    for i in range(len(cart)):
        for y in range(len(cart[i])):
            # print(cart[i][y])
            if cart[i][y] >=1:
                # print(menu[i][1][y][0])
                itemCost = cart[i][y] * catalog[i][1][y][2]
                # print(itemCost)
                # print(f'{menu[i][1][y][0]:.<16}{cart[i][y]:.^8}${itemCost}')
                cartOut += f'{catalog[i][1][y][0]:<16}{cart[i][y]:^8}${itemCost:.2f}\n'
    cartLabel.configure(text=cartOut)


def validate_key(event):
    print(event.keysym)
    if not event.char.isdigit() and event.keysym != 'BackSpace' and event.keysym!=('Return' or 'Down' or 'Up' or'Left' or 'Right'):
        print('n')
        return 'break'


def set_amt(event):
    print('WOW')
    print(amountEntry.get())
    print('WOW')
    cart[selectedCat][selectedSn]=int(amountEntry.get())
    update_labels()




itemList = get_items()
mainFrame = customtkinter.CTkTabview(master=root,)

# root.rowconfigure(0,weight = 1)
# root.columnconfigure(0,weight =3)
# root.columnconfigure(1,weight =1)
# mainFrame.pack(pady=12,padx=10)
mainFrame.pack()

mainFrame.add('shopping')
mainFrame.add('cart')
mainFrame.add('checkout')
leftFrame = customtkinter.CTkFrame(master=mainFrame.tab('shopping'))
leftFrame.grid(column=0, row=0, sticky ='nsew', pady=19)
rightFrame = customtkinter.CTkFrame(master=mainFrame.tab('shopping'))
rightFrame.grid(column=1, row=0, sticky ='nsew', pady=19)
mainFrame.tab('shopping').rowconfigure(0,weight = 1)
mainFrame.tab('shopping').columnconfigure(0,weight =2)
mainFrame.tab('shopping').columnconfigure(1,weight =1)

buttonFrame = customtkinter.CTkFrame(master=leftFrame)

catComboBox = customtkinter.CTkComboBox(master=leftFrame, values=[cat[0] for cat in catalog], command=cat_callback)
catComboBox.pack(pady=12, padx=10)
snComboBox = customtkinter.CTkComboBox(master=leftFrame, values=itemList, command=sn_callback)
snComboBox.pack(padx=10,pady=12)
buttonFrame.pack(padx=10,pady=12)
buttonFrame.columnconfigure(0,weight=1)
buttonFrame.columnconfigure(1,weight=1)
buttonFrame.columnconfigure(2,weight=1)
addButton = customtkinter.CTkButton(master=buttonFrame, text='+', font = ('Roboto', 24), command=plus_buton, width=50)
addButton.grid(column = 0,row = 0)
itemCountLabel = customtkinter.CTkLabel(master=buttonFrame, text=str(read_cart()))
itemCountLabel.grid(column = 1, row = 0, padx=12)
subButton = customtkinter.CTkButton(master=buttonFrame, text='-', font = ('Roboto', 24), command=sub_button, width=50)
subButton.grid(column = 2, row=0)

amountEntry=customtkinter.CTkEntry(master=leftFrame,placeholder_text=str(cart[selectedCat][selectedSn]))
amountEntry.pack(padx=12,pady=12)
amountEntry.bind('<KeyPress>',validate_key)
amountEntry.bind('<Return>',set_amt)


codeLabel = customtkinter.CTkLabel(master=rightFrame, text=catalog[selectedCat][1][selectedSn][1])
codeLabel.pack(padx=10, pady=12)
priceLabel=customtkinter.CTkLabel(master=rightFrame, text = f'${catalog[selectedCat][1][selectedSn][2]}')
priceLabel.pack(padx=10,pady=12)
subtotalLabel = customtkinter.CTkLabel(master=mainFrame.tab('checkout'), text=('subtotal: $' + str(subtotal)))
subtotalLabel.pack(padx=10,pady=12)
totalLabel = customtkinter.CTkLabel(master=mainFrame.tab('checkout'), text=('total: $' + str(total)))
gstLabel = customtkinter.CTkLabel(master=mainFrame.tab('checkout'), text=f"GST: ${gstAmt:.2f}")
discountComboBox = customtkinter.CTkComboBox(master=mainFrame.tab('checkout'), values=[i[0] for i in discounts], command=discount_callback)
discountLabel = customtkinter.CTkLabel(master=mainFrame.tab('checkout'), text=f'Discount: {(discounts[selectedDiscount][1] * 100)}%')
discountAmountLabel = customtkinter.CTkLabel(master=mainFrame.tab('checkout'), text=f'Discount amount: ${discountAmount}')
afterDiscountLabel = customtkinter.CTkLabel(master=mainFrame.tab('checkout'), text=f'Total after discount ${afterDiscount}')
gstLabel.pack(padx=10,pady=12)
totalLabel.pack(padx=10, pady=12)
discountComboBox.pack(padx=10,pady=12)
discountLabel.pack(padx=10,pady=12)
discountAmountLabel.pack(padx=10,pady=12)
afterDiscountLabel.pack(padx=10,pady=12)
cartLabel = customtkinter.CTkLabel(master=mainFrame.tab('cart'), text = cartOut)
cartLabel.pack(padx=10,pady=12)


root.mainloop()