from tkinter import *
from time import strftime

window=Tk()


window.geometry("1000x800")

window.configure(bg='white')
window.title('S Restaurent')



#......password entry......





def show():
	u=usernameentry.get()
	print('user name :',u)
	p=password.get()
	print("password  :",p)
	if (u=='sricharan') & (p=='password'):


		window=Toplevel()
		window.geometry('1000x800')
		def calculate():
			Mandi=e1.get()
			biryani=e2.get()
			roti=e3.get()
			noodles=e4.get()
			manchuriya=e5.get()
	
			total=((float(Mandi)*500)+(float(biryani)*200)+(float(roti)*100)+(float(noodles)*150)+(float(manchuriya)*150))

			label14=Label(window,text=total,font='times 18')
			label14.place(x=120,y=450)

			label15=Label(window,text="Total  = ",fg='orange',font="times 18")
			label15.place(x=50,y=450)

   
		label7=Label(window,text='------SV Restaurent-----',fg='violet',font="Bubble 32 bold")
		label7.pack()





		label1=Label(window,text='MENU',bg='red',font="times 28 bold")
		label1.place(x=750,y=70)

		label2=Label(window,text='Mandi		   rs 500',font="times 28")
		label2.place(x=650,y=120)

		label3=Label(window,text='biryani		   rs 200',font="times 28")
		label3.place(x=650,y=150)

		label4=Label(window,text='roti   	                   rs 100',font="times 28")
		label4.place(x=650,y=180)

		label5=Label(window,text='noodles		   rs 150',font="times 28")
		label5.place(x=650,y=210)

		label6=Label(window,text='manchuriya	   rs 150',font="times 28")
		label6.place(x=650,y=240)


 #................BILLING  PART........................

		label8=Label(window,text='Select the items how many u want.',fg='blue',font="times 20 bold")
		label8.place(x=50,y=100)

		label9=Label(window,text='Mandi',font="times 18")
		label9.place(x=50,y=200)

		e1=Spinbox(window,from_=0,to=100)
		e1.place(x=50,y=220)

		label10=Label(window,text='biryani',font="times 18")
		label10.place(x=350,y=200)

		e2=Spinbox(window,from_=0,to=100)
		e2.place(x=350,y=220)

		label11=Label(window,text='roti',font="times 18")
		label11.place(x=50,y=250)

		e3=Spinbox(window,from_=0,to=100)
		e3.place(x=50,y=270)

		label12=Label(window,text='noodles',font="times 18")
		label12.place(x=350,y=250)

		e4=Spinbox(window,from_=0,to=100)
		e4.place(x=350,y=270)

		label13=Label(window,text='manchuriya',font="times 18")
		label13.place(x=50,y=300)

		e5=Spinbox(window,from_=0,to=100)
		e5.place(x=50,y=320)



		b1=Button(window,bg='red',fg='white',text="Bill",width=20,command=calculate)
		b1.place(x=200,y=400)

 #.....time........

		def time():
			string=strftime('%X  (%P)  %Z\n %F  -  %A  -  %B')
			lbl.config(text=string)
			lbl.after(1000,time)
		lbl=Label(window,font='times 14',fg='black',bg='gold')
		lbl.place(x=750,y=5)
		time()

 #...listBox.........

		b1=Listbox(window,height=10,width=40,font='Helvetica 16',bg='pink',relief=SUNKEN,bd='4')

		b1.insert(1," 1.   Mandi")
		b1.insert(2," 2.   Biryani")
		b1.insert(3," 3.   Roti")
		b1.insert(4," 4.   Noodles")
		b1.insert(5," 5.   Manchuriya")

		b1.place(x=650,y=120)

	else:
		errorlabel=Label(window,text='ERROR',font='times 20 bold')	
		errorlabel.pack()

	
labelname=Label(window,text="WELCOME TO SRICHARAN'S PROJECT  \n  PLZ ENTER THE USER NAME & PASSWORD ",font='times 30 bold',fg='blue')
labelname.place(x=180,y=200)

password=StringVar()
#username=stringVar()

labelusername=Label(window,text='Username  :',font='times 18 bold')
labelusername.place(x=320,y=300)

labelpassword=Label(window,text='Password  :',font='times 18 bold')
labelpassword.place(x=320,y=330)

usernameentry=Entry(window,bg='orange')
usernameentry.place(x=420,y=300)
passentry=Entry(window,text=password,show='*',bg='green')
passbutton=Button(window,text='login',command=show)
passentry.place(x=420,y=330)
passbutton.place(x=470,y=360)

window.mainloop()
