amount = 1
price = 10
name = "neos"
import tkinter
import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("410x360")
#set icon
root.iconbitmap('f.ico')
#set minimum window size
root.minsize(410,360)
globals_namespace = globals()
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


make_cart_label(2, 42, name,globals_namespace)
make_cart_label(3, 2, "gay",globals_namespace)
make_cart_label(3, 2, "french",globals_namespace)
make_cart_label(2, 42, "wefwfe",globals_namespace)
make_cart_label(3, 2, "fwef",globals_namespace)
make_cart_label(3, 2, "fewwef",globals_namespace)

root.mainloop()
