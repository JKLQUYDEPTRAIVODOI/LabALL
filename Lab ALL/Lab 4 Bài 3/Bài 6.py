from tkinter import*
from tkinter.ttk import Combobox
import tkinter.messagebox as mbox
import re

root = Tk()
root.title("Dang ky hoc phan")
root.geometry("550x300+500+300")
root.configure(background="light green")

root.rowconfigure(0, pad=10)

mssv = StringVar()
hoten = StringVar()
email = StringVar()
sdt = StringVar()
hocky = StringVar()
ngaysinh = StringVar()

def CheckMSSV():
    ms = mssv.get()
    if not(len(ms)==7 and ms.isdigit()):
        mbox.showerror("Error", "MSSV chi duoc nhap 7 so")
        mssv.set("")

def CheckEmail():
    em = email.get()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not(re.match(pattern, em)):
        mbox.showerror("Error", "Email khong hop le")
        email.set("")

def CheckSDT():
    ms = sdt.get()
    if not(len(ms)==10 and ms.isdigit()):
        mbox.showerror("Error", "SDT chi duoc nhap 10 so")
        sdt.set("")

def CheckHocKy():
    hk = hocky.get()
    var = int(hk)
    if var < 1 or var > 3:
        mbox.showerror("Error", "Hoc ki chi duoc nhap 1, 2, 3")
        hocky.set("")

def CheckNgaySinh():
    ns = ngaysinh.get()
    pattern = r'^\d{2}/\d{2}/\d{4}$'
    if not(re.match(pattern, ns)):
        mbox.showerror("Error", "Ngay sinh khong hop le")
        ngaysinh.set("")

def CheckEmty():
    if not mssv.get() or not hoten.get() or not ngaysinh.get() or not email.get() or not sdt.get() or not hocky.get():
        mbox.showwarning("Warning", "Vui long dien du thong tin")
    if not var1.get() or not var2.get() or not var3.get() or not var4.get():
        mbox.showwarning("Warning", "Vui long chon mot mon hoc")

def RegisterForm():
    CheckEmty()
    CheckMSSV()
    CheckEmail()
    CheckNgaySinh()
    CheckSDT()
    CheckHocKy()

Label(root, text="THÔNG TIN ĐĂNG KÝ HỌC PHẦN", fg="red", bg="light green", font=20).grid(row=0, column=1)
Label(root, text="Mã số sinh viên", bg="light green").grid(row=1, column=0, sticky=W, padx=30)
Label(root, text="Họ tên", bg="light green").grid(row=2, column=0, sticky=W, padx=30)
Label(root, text="Ngày sinh", bg="light green").grid(row=3, column=0, sticky=W, padx=30)
Label(root, text="Email", bg="light green").grid(row=4, column=0, sticky=W, padx=30)
Label(root, text="Số điện thoại", bg="light green").grid(row=5, column=0, sticky=W, padx=30)
Label(root, text="Học kỳ", bg="light green").grid(row=6, column=0, sticky=W, padx=30)
Label(root, text="Năm học", bg="light green").grid(row=7, column=0, sticky=W, padx=30)
Label(root, text="Chọn môn học", bg="light green").grid(row=8, column=0, sticky=W, padx=30)

Entry(root, width=55, textvariable=mssv).grid(row=1, column=1)
Entry(root, width=55, textvariable=hoten).grid(row=2, column=1)
Entry(root, width=55, textvariable=ngaysinh).grid(row=3, column=1)
Entry(root, width=55, textvariable=email).grid(row=4, column=1)
Entry(root, width=55, textvariable=sdt).grid(row=5, column=1)
Entry(root, width=55, textvariable=hocky).grid(row=6, column=1)

cbbNamHoc = Combobox(root, width=52, textvariable=StringVar())
cbbNamHoc["values"] = ("2022-2023", "2023-2024", "2024-2025")
cbbNamHoc.grid(row=7, column=1)
cbbNamHoc.current(0)

var1 = BooleanVar()
var2 = BooleanVar()
var3 = BooleanVar()
var4 = BooleanVar()

chkLTP = Checkbutton(root, text="Lập trình Python", bg="light green", variable=var1).grid(row=8, column=1, sticky=W)
chkLTj = Checkbutton(root, text="Lập trình Java", bg="light green", variable=var2).grid(row=8, column=1, sticky=E, padx=59)
chkCNPM = Checkbutton(root, text="Công nghệ phần mềm", bg="light green", variable=var3).grid(row=9, column=1, sticky=W, pady=5)
chkPTUDW = Checkbutton(root, text="Phát triển ứng dụng web", bg="light green", variable=var4).grid(row=9, column=1, sticky=E)

Button(root, text="Đăng ký", bg="light blue", command=RegisterForm).grid(row=10, column=1, sticky=W, padx=60, pady=10)
Button(root, text="Thoát", bg="light blue", command=quit).grid(row=10, column=1, sticky=E, padx=60)

root.mainloop()