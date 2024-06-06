###################################
#4NicholasDubsUITestFile
#Nicholas Dubs
#ECE2404 Group ____
#Group Project 1
#Refinging UI adding rest of functionality i.e cart view
#Using TabView instead of forgetting nd repacking frames
#06/06/24
##################################
import customtkinter

drinks = [["Neo's Green Tea", "N32", 3],["Drink 2","C12",2.85]]
beer = [["Beer 1", "C13", 3],["Beer 2","C14",2.85]]
frozen = [["frozen 1", "C15", 3],["frozen 2","C16",2.85]]
household = [["Household 1", "C17", 3],["Household 2","C18",2.85]]
snacks = [["Snack 1", "C19", 3],["Snack 2","C20",2.85]]

catalog = [["Drinks", drinks, "CD20"], ["Beer", beer, "CB20"], ["Frozen", frozen, "CF30"], ["Household", household, "CH40"], ["Snacks", snacks, "CS50"]]
cart = []
discounts = [["None",0],["Senior", 0.1],['Member',.08],["NS man",.05]]

selectedSn = 0
selectedCat = 0
selectedDiscount = 0
subtotal = 0
total = 0
gstAmt = 0
discountAmount = 0
afterDiscount = 0
cartOut = ''

# print(menu)

for i in range(len(catalog)):
    a = len(catalog[i][1])
    b = [0]*a
    # print(b)
    cart.append(b)
    # print(cart)

# print(cart)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def plus_buton():
    cart[selectedCat][selectedSn] += 1
    print(cart)
    update_labels()
def subtract_button():
    if cart[selectedCat][selectedSn]>0:
        cart[selectedCat][selectedSn] -= 1
    else:
        print("cant go below 0")
    print(cart)
    update_labels()
# for item in menu:
#     print(item)

def cat_callback(choice):
    global selectedCat
    global itemList
    for i in catalog:
        print(i)
        # print(i[0])
        if choice == i[0]:
            selectedCat = catalog.index(i)
    # print(selectedCat)
    print(f'combobox dropdown clicked {choice}'
          #f' : {menu[selectedCat][0]}'
          )
    itemList = get_items()
    update_labels()



def sn_callback(choice):
    global selectedSn
    # print(choice)
    for i in catalog[selectedCat][1]:
        print(i)
        if choice == i[0]:
            selectedSn=catalog[selectedCat][1].index(i)
    print(selectedSn)

    print(f'combobox dropdown clicked {choice}'
          #f' : {menu[selectedCat][0]}'
          )
    update_labels()

def discount_callback(choice):
    global selectedDiscount
    for i in discounts:
        if choice == i[0]:
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
    if not event.char.isdigit() and event.keysym != 'BackSpace' and event.keysym!='Return':
        print('n')
        return 'break'


def set_amt(event):
    print('WOW')
    cart[selectedCat][selectedSn]=int(amountEntry.get())
    update_labels()




itemList = get_items()
mainFrame = customtkinter.CTkTabview(master=root)

# root.rowconfigure(0,weight = 1)
# root.columnconfigure(0,weight =3)
# root.columnconfigure(1,weight =1)
# mainFrame.pack(pady=12,padx=10)
mainFrame.pack()

mainFrame.add('shopping')
mainFrame.add('cart')
mainFrame.add('checkout')
mainFrame.set('shopping')
leftFrame = customtkinter.CTkFrame(master=mainFrame.tab('shopping'))
leftFrame.grid(column=0, row=0, sticky ='nsew', pady=19)
rightFrame = customtkinter.CTkFrame(master=mainFrame.tab('shopping'))
rightFrame.grid(column=1, row=0, sticky ='nsew', pady=19)
mainFrame.tab('shopping').rowconfigure(0,weight = 1)
mainFrame.tab('shopping').columnconfigure(0,weight =2)
mainFrame.tab('shopping').columnconfigure(1,weight =1)


catComboBox = customtkinter.CTkComboBox(master=leftFrame, values=[cat[0] for cat in catalog], command=cat_callback)
catComboBox.pack(pady=12, padx=10)
snComboBox = customtkinter.CTkComboBox(master=leftFrame, values=itemList, command=sn_callback)
snComboBox.pack(padx=10,pady=12)
itemCountLabel = customtkinter.CTkLabel(master=rightFrame, text=str(read_cart()))
itemCountLabel.pack(padx=12, pady=12)
amountEntry=customtkinter.CTkEntry(master=leftFrame,placeholder_text=str(cart[selectedCat][selectedSn]))
amountEntry.pack(padx=12,pady=12)
amountEntry.bind('<KeyPress>',validate_key)
amountEntry.bind('<Return>',set_amt)
# addButton = customtkinter.CTkButton(master=leftFrame, text='+', font = ('Roboto', 24), command=plus_buton)
# addButton.pack(padx=10,pady=12)
# subtractButton = customtkinter.CTkButton(master=leftFrame, text='-', font = ('Roboto', 24), command=subtract_button)
# subtractButton.pack(padx=10,pady=12)
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
totalLabel.pack(padx=10, pady=12)
discountComboBox.pack(padx=10,pady=12)
gstLabel.pack(padx=10,pady=12)
discountLabel.pack(padx=10,pady=12)
discountAmountLabel.pack(padx=10,pady=12)
afterDiscountLabel.pack(padx=10,pady=12)
cartLabel = customtkinter.CTkLabel(master=mainFrame.tab('cart'), text = cartOut)
cartLabel.pack(padx=10,pady=12)


root.mainloop()