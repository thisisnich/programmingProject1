###################################
#4NicholasDubsUITestFile
#Nicholas Dubs
#ECE2404 Group ____
#Group Project 1
#File to test out custom tkinter library
#Designing UI and understanding functionality for project
##################################
import customtkinter

drinks = [["Drink 1", "C11", 3, 0],["Drink 2","C12",2.85]]
beer = [["Beer 1", "C11", 3],["Beer 2","C12",2.85]]
frozen = [["frozen 1", "C11", 3],["frozen 2","C12",2.85]]
household = [["Household 1", "C11", 3],["Household 2","C12",2.85]]
snacks = [["Snack 1", "C11", 3],["Snack 2","C12",2.85]]

catalog = [["Drinks", drinks, "CD20"], ["Beer", beer, "CB20"], ["Frozen", frozen, "CF30"], ["Household", household, "CH40"], ["Snacks", snacks, "CS50"]]
cart = []
selectedSn = 0
selectedCat = 0
# print(menu)



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def plus_buton():
    cart[selectedSn] += 1
    print(cart)
def subtract_button():
    if cart[selectedSn]>0:
        cart[selectedSn] -= 1
    else:
        print("cant go below 0")
    print(cart)
for item in catalog:
    print(item)
# def login():
#     print("Test")
def cat_callback(choice):
    global selectedCat
    for i in catalog:
        print(i[0])
        if choice == i[0]:
            selectedCat = catalog.index(i)
    print(selectedCat)
    print(f'combobox dropdown clicked{choice}{catalog[0][0]}')

def get_items(cat):
    for i in catalog[cat]:
        print(i)
def sn_callback(choice):
    global selectedSn
    selectedSn=int(choice)
    print(f'combobox dropdown clicked{choice}')
# print(get_items(0))
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill = "both", expand = True)

catComboBox = customtkinter.CTkComboBox(master=frame, values=[cat[0] for cat in catalog], command=cat_callback)
catComboBox.pack(pady=12, padx=10)
snComboBox = customtkinter.CTkComboBox(master=frame, values=['1'], command=sn_callback)
snComboBox.pack(pady=12, padx=10)
addButton = customtkinter.CTkButton(master=frame, text='+', font = ('Roboto',24),command=plus_buton)
addButton.pack(pady=12, padx=10)
subtractButton = customtkinter.CTkButton(master=frame, text='-', font = ('Roboto',24),command=subtract_button)
subtractButton.pack(pady=12, padx=10)

# label = customtkinter.CTkLabel(master=frame, text="Login System", font = ("Roboto", 24))
# label.pack(pady = 12, padx=10)
#
# userEntry = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
# userEntry.pack(pady=12,padx=10)
# passwordEntry = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show='*')
# passwordEntry.pack(pady=12,padx=10)
#
# button = customtkinter.CTkButton(master=frame, text="Login",command=login)
# button.pack(pady=12,padx=10)
#
# checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
# checkbox.pack(pady=12,padx=10)

root.mainloop()