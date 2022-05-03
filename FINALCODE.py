from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkcalendar import Calendar, DateEntry
import os
from datetime import date
from tkinter import messagebox
from tkinter import StringVar


PATH = "/Users/isabella/Desktop"
os.chdir(PATH)
db_name = "campers.db"

def create_table(db_name):
    """
    You only need to create a database for the first time
    """
    # Create a database or connect to one
    conn = sqlite3.connect(db_name)

    # create cursor
    c = conn.cursor()

    # Create table - only need to run onetime

    c.execute(""" CREATE TABLE campers(
              first_name text, 
              last_name text,
              address text,
              city text,
              state text,
              zipcode integer,
              emergency text,
              ecnumber integer,
              forms text,
              equipment text,
              bunk text,
              tribe text,
              payment_date text) """)

# Create the database
create_table(db_name)    
    

def master():
    global root
    global f_name
    global l_name
    global address
    global city 
    global state
    global zipcode
    global emergency
    global ecnumber
    global forms
    global equipment
    global bunk
    global payment_date
    global query_box
    global clicked
    global search_entry
    global variable1
    global variable2
    global outputvar
    global totalvar
    
    root = Tk()
    root.title('Gila Breath Camp')
    root.geometry("1200x800")
    variable1 = StringVar(root)
    variable2 = StringVar(root)
    variable1.set("bunk")
    variable2.set("tribe")


    # Create a Form Label
    label_1 = Label(root, text = "Camper Application Search", font = ("Calibri", 50), 
                    padx = 20, pady = 30)
    label_1.pack()
    
    # Create a Two Frames
    frame_detail = LabelFrame(root, text = "Camper Details", padx = 5, pady = 5)
    frame_detail.pack(side = LEFT, padx = 10, pady = 10)
    
    # Create a Two Frames
    frame_search = LabelFrame(root, text = "Query & Search", padx = 5, pady = 5)
    frame_search.pack(side = LEFT, padx = 10, pady = 10)
    
    #---------------------- Detail Frame -------------------------------
    # Create Text Boxes
    f_name = Entry(frame_detail, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    
    l_name = Entry(frame_detail, width=30)
    l_name.grid(row=1, column=1)
    
    address = Entry(frame_detail, width=30)
    address.grid(row=2, column=1)
    
    city = Entry(frame_detail, width=30)
    city.grid(row=3, column=1)
    
    state = Entry(frame_detail, width=30)
    state.grid(row=4, column=1)
    
    zipcode = Entry(frame_detail, width=30)
    zipcode.grid(row=5, column=1)
    
    emergency = Entry(frame_detail, width=30)
    emergency.grid(row=6, column=1)
    
    ecnumber = Entry(frame_detail, width=30)
    ecnumber.grid(row=7, column=1)
    
    forms = Entry(frame_detail, width=30)
    forms.grid(row=8, column=1)
    
    equipment = Entry(frame_detail, width=30)
    equipment.grid(row=9, column=1)
    
    bunk = OptionMenu(frame_detail, variable1, "bunk 1, girl", "bunk 2, girl", "bunk 3, girl", "bunk 1, boy", "bunk 2, boy", "bunk 3, boy")
    bunk.config(width=26)
    bunk.grid(row=10, column=1)
    
    tribe = OptionMenu(frame_detail, variable2, "tribe 1", "tribe 2", "tribe 3")
    tribe.config(width=26)
    tribe.grid(row=11, column=1)
    
    payment_date = DateEntry(frame_detail,width=30,bg="darkblue",fg="white", 
                             year = date.today().year)
    payment_date.grid(row=12, column=1)
    
    query_box = Entry(frame_detail, width = 30)
    query_box.grid(row=14, column = 1, padx = 20)
    
    # Create Text Box Labels
    f_name_label = Label(frame_detail, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0), sticky = W)
    l_name_label = Label(frame_detail, text="Last Name")
    l_name_label.grid(row=1, column=0, sticky = W)
    address_label = Label(frame_detail, text="Address")
    address_label.grid(row=2, column=0, sticky = W)
    city_label = Label(frame_detail, text="City")
    city_label.grid(row=3, column=0, sticky = W)
    state_label = Label(frame_detail, text="State")
    state_label.grid(row=4, column=0, sticky = W)
    zipcode_label = Label(frame_detail, text="Zipcode")
    zipcode_label.grid(row=5, column=0, sticky = W)
    emergency_label = Label(frame_detail, text="Emergency Contact")
    emergency_label.grid(row=6, column=0, sticky = W)
    ecnumber_label = Label(frame_detail, text="Emergency Contact Number")
    ecnumber_label.grid(row=7, column=0, sticky = W)
    forms_label = Label(frame_detail, text="Forms Sumbmitted (Y/N)")
    forms_label.grid(row=8, column=0, sticky = W)
    equipment_label = Label(frame_detail, text="Required Equipment (Y/N)")
    equipment_label.grid(row=9, column=0, sticky = W)
    bunk_label = Label(frame_detail, text="Bunk Preference")
    bunk_label.grid(row=10, column=0, sticky = W)
    tribe_label = Label(frame_detail, text="Tribe Preference")
    tribe_label.grid(row=11, column=0, sticky = W)
    payment_label = Label(frame_detail, text="Payment Date")
    payment_label.grid(row=12, column=0, sticky = W)
    
    query_label = Label(frame_detail, text = "Enter Application ID")
    query_label.grid(row=14, column =0, sticky = W)
    
    
    # create submit button
    submit_btn = Button(frame_detail, text="Save Records", command = submit)
    submit_btn.grid(row=13, column=0, columnspan = 2,  pady=10, padx=10)

    update_btn = Button(frame_detail, text = "Update Records", command = update)
    update_btn.grid(row =15, column=1,  pady=10, padx=10)
    
    
    query_btn = Button(frame_detail, text = "Search Records", command = search)
    query_btn.grid(row =15, column= 0, pady=10, padx=10)
    
    
    # -------------------- Search Frame ------------------------
    outputvar = StringVar()
    totalvar = StringVar()
    
    
    Label(frame_search, text="Search By", bg = 'white', fg = 'red').grid(row = 0, column = 0)
    menu_list = ['first_name', 'last_name', 'address', 'city',
                 'state', 'zipcode', 'emergency', 'ecnumber',
                 'forms', 'equipment', 'bunk', 'tribe', 'payment_date']
    
    oMenuWidth = len(max(menu_list, key=len))
    
    clicked = StringVar()
    clicked.set(menu_list[0])
    
    search_drop = OptionMenu(frame_search, clicked, *menu_list)
    search_drop.config(width=oMenuWidth)
    search_drop.grid(row = 0, column = 1)
    
    search_entry = Entry(frame_search, width=30)
    search_entry.grid(row = 0, column = 2)
    
    Button(frame_search, text = "Query", command = query).grid(row = 0, column= 3)

    total = Label(frame_search, height = 1, width = 50, 
                  textvariable = totalvar, anchor = W).grid(row = 1, columnspan = 4)
    
    output = Label(frame_search, height = 16, width = 50, 
                   textvariable = outputvar, anchor = W).grid(row = 2, columnspan = 4)
    
    root.mainloop()


def submit():
    
	# Create a database or connect to one
    conn = sqlite3.connect(db_name)
	# Create cursor
    c = conn.cursor()

	# Insert Into Table
    c.execute("""INSERT INTO campers VALUES (:f_name, :l_name, :address, 
                                               :city, :state,  :zipcode, :emergency, 
                                               :ecnumber, :forms, :equipment, :bunk, :tribe,
                                               :p_date)""",
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'address': address.get(),
				'city': city.get(),
				'state': state.get(),
				'zipcode': zipcode.get(),
                'emergency': emergency.get(),
                'ecnumber': ecnumber.get(),
                'forms': forms.get(),
                'equipment': equipment.get(),
                'bunk': variable1.get(),
                'tribe': variable2.get(),
                'p_date':payment_date.get_date()
			})


	#Commit Changes
    conn.commit()

	# Close Connection 
    conn.close()
    
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    emergency.delete(0, END)
    ecnumber.delete(0, END)
    forms.delete(0, END)
    equipment.delete(0, END)
    variable1.set("bunk")
    variable2.set("tribe")
    payment_date.delete(0, END)
    
    messagebox.showinfo("Success!",
                        'The record has been saved successfully!')

	# Clear The Text Boxes


def search():
    
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    emergency.delete(0, END)
    ecnumber.delete(0, END)
    forms.delete(0, END)
    equipment.delete(0, END)
    variable1.set("bunk")
    variable2.set("tribe")
    payment_date.delete(0, END)
    
    conn = sqlite3.connect(db_name)
	# Create cursor
    c = conn.cursor()
    record_id = query_box.get()

    c.execute("SELECT * FROM campers WHERE oid = " + record_id)
    records = c.fetchall()
    if len(records) == 0:
        messagebox.showerror('Warning!',
                             "This record doesn't exist!")
        

    # loop through records
    for record in records:
        f_name.insert(0, record[0])
        l_name.insert(0, record[1])
        address.insert(0, record[2])
        city.insert(0, record[3])
        state.insert(0, record[4])
        zipcode.insert(0, record[5])
        emergency.insert(0, record[6])
        ecnumber.insert(0, record[7])
        forms.insert(0, record[8])
        equipment.insert(0, record[9])
        bunk.insert(0, record[10])
        tribe.insert(0, record[11])
        payment_date.insert(0, record[12])


def update():
    conn = sqlite3.connect(db_name)
	# Create cursor
    c = conn.cursor()
    record_id = query_box.get()


	# Query the database
    c.execute("""UPDATE campers SET
           first_name = :first,
		   last_name = :last,
		   address = :address,
		   city = :city,
		   state = :state,
		   zipcode = :zipcode,
           emergency = :emergency,
           ecnumber = :contact,
           forms = :forms,
           equipment = :equipment,
           bunk = :bunk,
           tribe = :tribe,
           payment_date = :payment
		   WHERE oid = :oid""",
		{
		'first': f_name.get(),
		'last': l_name.get(),
		'address': address.get(),
		'city': city.get(),
		'state': state.get(),
		'zipcode': zipcode.get(),
        'emergency': emergency.get(),
        'contact': ecnumber.get(),
        'forms': forms.get(),
        'equipment': equipment.get(),
        'bunk': variable1.get(),
        'tribe': variable2.get(),
        'payment': payment_date.get_date(),    
		'oid': record_id
		})            
    
    #Commit Changes
    conn.commit()

	# Close Connection 
    conn.close()
    
    messagebox.showinfo("Success!",
                        'The record has been updated successfully!')
    
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    emergency.delete(0, END)
    ecnumber.delete(0, END)
    forms.delete(0, END)
    equipment.delete(0, END)
    variable1.set("bunk")
    variable2.set("tribe")
    payment_date.delete(0, END)


def query():
    totalvar.set(" ")    
    outputvar.set(" ")
    
    field = clicked.get()
    field_value= search_entry.get()
    print(field, field_value)
    
    
    conn = sqlite3.connect(db_name)
	# Create cursor
    c = conn.cursor()
    
    execution = f"SELECT rowid, * FROM campers WHERE {field} = ? "
    
    c.execute(execution, (field_value, ))
    records = c.fetchall()
    total = len(records)
    
    if total == 0:
        messagebox.showerror('Warning!',
                             "This record doesn't exist!")
    print_records = ''
    for rec in records:
        print_records += (str(rec[0]) + "  " + str(rec[1]) + "   " +str(rec[2]) + " "+ "\t" 
                         +str(rec[8]) + "  " + str(rec[9]) + "\n")
    
    total_records = f"A total of {total} records found"
    totalvar.set(total_records)    
    outputvar.set(print_records)
    
    
master()
