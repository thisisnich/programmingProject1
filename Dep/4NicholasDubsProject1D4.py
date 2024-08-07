###################################
#4NicholasDubsProjectD4
#Nicholas Dubs
#ECE2404 Group Team 7
#Group Project 1
#Finalizing UI
#12/07/24
##################################
#TODO
#REmove frames when opening a new one Doris
#Add logo Doris
#Thank you for shopping with us Doris
#Error message when no items in cart Nicholas       DONE
#Confirmation when removing from cart Nicholas      DONE
#Debug options Doris
#Save Card info Nicholas                            WIP
#Clean up comments Nicholas
#clean up payment method radio buttons Nicholas     DONE
##################################
import customtkinter
from CTkMessagebox import CTkMessagebox
from PIL import Image

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
        "FP78": {"name": "FP Facial Tissues", "price": 9.5},
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

print(catalog)
cart = {category: {sn: 0 for sn in items} for category, items in catalog.items()}
print(cart)
#for cart buttons
globals_namespace = globals()

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

#appearance mode set to dark
customtkinter.set_appearance_mode("dark")
#colour theme set to dark blue
customtkinter.set_default_color_theme("dark-blue")

#define root window
root = customtkinter.CTk()
#set default size
root.geometry("410x370")
#set icon
root.iconbitmap('f.ico')
#set window name
root.title("DorNick")
#set minimum window size
root.minsize(410,370)


#function run when plus button is pressed
def plus_buton():
    #find location in cart that corresponds to selected category and item and increment by 1
    cart[selectedCat][selectedItem] += 1
    #print(cart) #Debug print cart
    #duh
    update_labels()


def sub_button():
    #if the value of the corresponding spot in cart is more than 0 subtract by 1
    if cart[selectedCat][selectedItem]>1:
        cart[selectedCat][selectedItem] -= 1
        #if the amount of items is zero, run remove_cart_label, and pass the selected serial number -> remover the label in cart that is now 0
        if cart[selectedCat][selectedItem] == 0:
            remove_cart_label(selectedItem, globals_namespace)
    #if it is 0 then print 'cant go below 0' and dont reduce by 1
    else:
        print("can't go below 0")
    update_labels()
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


#function to update image
def update_img():
    #get height and width of root window
    # print(f'height: {root.winfo_height()}')     #Debug: print window height
    # print(f'width: {root.winfo_width()}')       #Debug: print window width
    #get max width and height the image can be
    maxImgHeight = int(root.winfo_height()/5)
    maxImgWidth = int(root.winfo_width()/6)
    # print(f'img height: {maxImgHeight}')        #Debug: print max image height
    # print(f'img width: {maxImgWidth}')          #Debug: print max image width
    #because square image, set image size to be the smallest of teh maximum values
    imgSize = min(maxImgWidth, maxImgHeight)

    #update image  with selected item serial number and set image size to maximum size
    itemImage.configure(light_image=get_image(),
                        dark_image=get_image(),
                        size=(imgSize,imgSize))
    imageLabel.configure(image=itemImage)


#function to update labels
def update_labels():
    update_img()
    snComboBox.configure(values=itemList)
    #update the label that displays the item code
    codeLabel.configure(text=selectedItem)
    snComboBox.set(catalog[selectedCat][selectedItem]['name'])
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
    #Run function to make new cart labels
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
                #calculate cost of item
                item_cost = cart[cat][sn]*catalog[cat][sn]['price']
                #run make cart label function with the item sn and as well as item name, and cost
                make_cart_label(cart[cat][sn],item_cost,catalog[cat][sn]["name"],globals_namespace,sn)


#function to check that only accepted keys are registered
def validate_key(event):
    # print(event.keysym) #Debug:print key that was pressed
    #only accept digits, backspace, Enter, Left or right
    if not event.char.isdigit() and event.keysym not in ('BackSpace', 'Return', 'Left', 'Right'):
        # print('key not accepted')  #Debug: print message when keypress is not accepted
        return 'break'
    # print(amountEntry.get())  #Debug: print current stored value in Entry field


#function called when enter key is pressed
# sets cart at selected category and selected item to value that is in the entry box
def set_amt(event):
    #print('-----')             #Debug: print lines to show what the read input is
    # print(amountEntry.get())  #Debug: print read input
    #print('-----')             #Debug: print lines to show what the read input is
    #set cart value to the value stored in Entry
    cart[selectedCat][selectedItem]=int(amountEntry.get())
    #call update labels function
    if cart[selectedCat][selectedItem] == 0:
        remove_cart_label(selectedItem, globals_namespace)
    update_labels()


###ADD
def checkout_button():
    cartExists = False
    for cat in cart:
        for item in cart[cat]:
            if cart[cat][item] >=1:
                cartExists = True
    if cartExists:
        masterFrame.place_forget()
        checkoutFrame.place(anchor= 'center', relheight = 0.8, relwidth=0.65, relx=0.5, rely=0.5)
        subtotalLabel.pack(padx=10,pady=12)
        totalLabel.pack(padx=10, pady=12)
        gstLabel.pack(padx=10,pady=12)
        discountComboBox.pack(padx=10,pady=12)
        discountLabel.pack(padx=10,pady=12)
        discountAmountLabel.pack(padx=10,pady=12)
        afterDiscountLabel.pack(padx=10,pady=12)
    else:
        CTkMessagebox(title="Error", message="No items in cart",icon="warning", option_1="Back")



###ADD
def back_button():
    checkoutFrame.place_forget()
    masterFrame.place(anchor='center', relheight=0.85, relwidth=0.85, relx=0.5, rely=0.5)


#function called when appearance menu is selected sets appearance to the selected type
def appearance_callback(choice: str):
    customtkinter.set_appearance_mode(choice)


#function called when item in scaling menu is selected, sets scaling to selected number
def scaling_callback(choice: str):
    #removes % from string
    new_scaling_float = int(choice.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)


#function to make labels for cart
def make_cart_label(amt, price, name, namespace, sn):
    global selectedItem
    #try to configure an existing label with the serial number. i.e. sn = N32 frame = N32Frame
    try:
        namespace[f'{sn}Label'].configure(text=f'{name:<16}{amt:^8}${price:.2f}')
        #print('label already exists')      #Debug: if label already exists
    #if label doesnt exist, create a new label
    except:
        # print('Making new frame')  #Debug: print if a new label is made
        #make new frame for this item
        namespace[f'{sn}Frame'] = customtkinter.CTkFrame(cartFrame)
        namespace[f'{sn}Frame'].columnconfigure(0, weight=3)
        # namespace[f'{name}Frame'].columnconfigure(1, weight=1)
        #Display name, amount ordered and cost of this item
        namespace[f'{sn}Label'] = customtkinter.CTkLabel(namespace[f'{sn}Frame'], text=f'{name:<16}{amt:^8}${price:.2f}')
        namespace[f'{sn}Label'].grid(column=0, row = 0)
        #Button to remove item from cart, runs remove_cart_label function, passes serial number
        namespace[f'{sn}Button'] = customtkinter.CTkButton(namespace[f'{sn}Frame'],text='Remove', width = 50, command=lambda: remove_cart_label(sn, namespace))
        namespace[f'{sn}Button'].grid(column=2, row=0, padx=10, pady=5)
    #pack label
    namespace[f'{sn}Frame'].pack(pady=1)


#functino to remove label
def remove_cart_label(sn, namespace):
    confirmDelete = CTkMessagebox(title="Confirm", message="Are you sure you want to remove this item?", icon="check", option_1="Cancel", option_2="Yes")
    response = confirmDelete.get()
    if response == "Yes":
        #try forgetting
        try:
            namespace[f'{sn}Frame'].pack_forget()
        #uf label does not exist, continue
        except:
            pass
        #check which item needs to be removed, set that item in cart to 0
        for cat in cart:
            for item in cart[cat]:
                if sn == item:
                    cart[cat][item]= 0
        #update labels
        update_labels()


#get image
def get_image():
    try:
        output = Image.open(f'resources/{selectedItem}.jpg')
        return output
    except:
        output = Image.open('../resources/default.jpg')
        return output


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
masterFrame.add('settings')
checkoutFrame = customtkinter.CTkScrollableFrame(master=root) ###edited
cartFrame = customtkinter.CTkScrollableFrame(master=masterFrame.tab('cart'))
cartFrame.pack(side='top',fill='both', expand=True)
# checkoutFrame.place(anchor= 'center', relheight = .8, relwidth=.65, relx=.5, rely=.5)

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
paymentButton = customtkinter.CTkButton(master=checkoutFrame,text="Continue Payment")
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

itemImage = customtkinter.CTkImage(light_image=get_image(),
                                   dark_image = get_image(),
                                   size=(90,90))
imageLabel = customtkinter.CTkLabel(rightFrame, image=itemImage, text='')
imageLabel.pack(padx=10, pady=0)
#label that displays item code in right frame of shopping tap
codeLabel = customtkinter.CTkLabel(master=rightFrame, text=selectedItem)
codeLabel.pack(padx=10, pady=10)
#Label that displays price of item in right frame of shopping tab
priceLabel=customtkinter.CTkLabel(master=rightFrame, text = f'${catalog[selectedCat][selectedItem]['price']}')
priceLabel.pack(padx=10,pady=10)
shopSubtotalLabel = customtkinter.CTkLabel(master=rightFrame, text=(f'Subtotal: ${subtotal:.2f}'))
shopSubtotalLabel.pack(padx=10,pady=10)




#label that displays subtotal in checkout tab
subtotalLabel = customtkinter.CTkLabel(master=checkoutFrame, text=(f'Subtotal: ${subtotal:.2f}'))
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


#SETTINGS TAB
appearanceComboBox = customtkinter.CTkOptionMenu(master=masterFrame.tab('settings'), values=["Light", "Dark", "System"],
                                                          command=appearance_callback)
appearanceComboBox.pack(pady=10)
appearanceComboBox.set("Dark")
scalingComboBox = customtkinter.CTkOptionMenu(masterFrame.tab("settings"), values=["80%", "90%", "100%", "110%", "120%","130%","140%","150%"],
                                                               command=scaling_callback)
scalingComboBox.pack(pady=10)
scalingComboBox.set("100%")
#
# root.bind('<Configure>', update_img)

#start customtkinter window
root.mainloop()
