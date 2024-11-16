from flask import Flask, render_template, request, redirect
import os
import psycopg2
from datetime import datetime
os.environ['FLASK_APP'] = 'app.py'
app = Flask(__name__)


def connect_to_database():
    try:
        conn = psycopg2.connect(
            database='phase5',
            user='postgres',
            password='',
            host='127.0.0.1',
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
@app.route('/')
def root():
    return redirect('/home')
@app.route('/home')
def home_page():
    return render_template('home.html')
@app.route('/department')
def display_department():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_department(conn)
        conn.close()
        return render_template('department.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_department(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM department')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/bill')
def display_bill():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_bill(conn)
        conn.close()
        return render_template('bill.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_bill(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bill')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/pays')
def display_pays():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_pays(conn)
        conn.close()
        return render_template('pays.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_pays(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pays')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/books')
def display_books():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_books(conn)
        conn.close()
        return render_template('books.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_books(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    data = cursor.fetchall()
    cursor.close()
    return data
@app.route('/dependents')
def display_dependents():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_dependents(conn)
        conn.close()
        return render_template('dependents.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."
def fetch_dependents(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dependent')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/award')
def display_award():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_award(conn)
        conn.close()
        return render_template('award.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."
def fetch_award(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM award')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/shift')
def display_shift():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_shift(conn)
        conn.close()
        return render_template('shift.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."
def fetch_shift(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM shift')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/receives')
def display_receives():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_receives(conn)
        conn.close()
        return render_template('receives.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."
def fetch_receives(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM receives')
    data = cursor.fetchall()
    cursor.close()
    return data


@app.route('/provides')
def display_provides():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_provides(conn)
        conn.close()
        return render_template('provides.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_provides(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM provides')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/event')
def display_event():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_event(conn)
        conn.close()
        return render_template('event.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_event(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM event')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/holds')
def display_holds():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_holds(conn)
        conn.close()
        return render_template('holds.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_holds(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM holds')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/contractor')
def display_contractor():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_contractor(conn)
        conn.close()
        return render_template('contractor.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_contractor(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contractor')
    data = cursor.fetchall()
    cursor.close()
    return data


@app.route('/supplier')
def display_supplier():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_supplier(conn)
        conn.close()
        return render_template('supplier.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_supplier(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM supplier')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/inventory')
def display_inventory():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_inventory(conn)
        conn.close()
        return render_template('inventory.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_inventory(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventory')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/supplies')
def display_supplies():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_supplies(conn)
        conn.close()
        return render_template('supplies.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_supplies(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM supplies')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/location')
def display_location():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_location(conn)
        conn.close()
        return render_template('location.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_location(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM location')
    data = cursor.fetchall()
    cursor.close()
    return data




#add   
@app.route('/bill/add', methods=['GET', 'POST'])
def add_bill():
    error_message = None
    if request.method == 'POST':
        bid = request.form['billid']
        DC = request.form['DC']
        GT = request.form['GT']
        cid = request.form['cid']

        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                
                cursor.execute("INSERT INTO bill (bill_id, date_created, grand_total,  customer_id_fk) VALUES (%s,%s, %s, %s)",
                           (bid,DC,GT,cid))
                conn.commit()
                conn.close()
                
            except Exception as e:
                error_message = f"Error adding bill: {e}"
                return render_template('add_bill.html', error_message=error_message)
            return redirect('/bill')
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_bill.html',error_message=error_message) 
    
@app.route('/pays/add', methods=['GET', 'POST'])
def add_pays():
    error_message = None
    if request.method == 'POST':
        bid = request.form['billid']
        DC = request.form['PD']
        GT = request.form['AP']
        cid = request.form['PM']

        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                
                cursor.execute("INSERT INTO pays (bill_id_fk, payment_date, amount_paid,  payment_method) VALUES (%s,%s, %s, %s)",
                           (bid,DC,GT,cid))
                conn.commit()
                conn.close()
                
            except Exception as e:
                error_message = f"Error adding payment: {e}"
                return render_template('add_pays.html', error_message=error_message)
            return redirect('/pays')
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_pays.html',error_message=error_message) 
@app.route('/department/add', methods=['GET', 'POST'])
def add_department():
    error_message = None
    if request.method == 'POST':
        name = request.form['name']
        pn = request.form['pn']
        loc = request.form['loc']
        
        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                
                cursor.execute("INSERT INTO department(name, phone_number, location) VALUES (%s, %s, %s);",(name,pn,loc))
                conn.commit()
                conn.close()
                
            except Exception as e:
                error_message = f"Error adding department: {e}"
                return render_template('add_department.html', error_message=error_message)
            return redirect('/department')
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_department.html',error_message=error_message)

    
@app.route('/books/add', methods=['GET', 'POST'])
def add_books():
    error_message = None
    if request.method == 'POST':
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        room_number = request.form['room_number']
        customer_id = request.form['customer_id']
        date_booked = request.form['date_booked']

        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO books (start_timestamp, end_timestamp, roomnumber_fk, customerid_fk, date_booked) VALUES (%s, %s, %s, %s, %s)",
                               (start_time, end_time, room_number, customer_id, date_booked))
                conn.commit()
                conn.close()
                return redirect('/books')
            except Exception as e:
                error_message = f"Error adding book: {e}"
                return render_template('add_books.html', error_message=error_message)
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_books.html', error_message=error_message)

@app.route('/dependent/add', methods=['GET', 'POST'])
def add_dependent():
    error_message = None

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        staff_id = request.form['staff_id']
        relationship = request.form['relationship']
        birth_date = request.form['birth_date']
        phone_number = request.form['phone_number']
        gender = request.form['gender']

        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO dependent (first_name, last_name, staffid_fk, relationship, birth_date, phone_number, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                               (first_name, last_name, staff_id, relationship, birth_date, phone_number, gender))
                conn.commit()
                conn.close()
                return redirect('/dependents')
            except Exception as e:
                error_message = f"Error adding dependent: {e}"
                return render_template('add_dependent.html', error_message=error_message)
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_dependent.html', error_message=error_message)

@app.route('/award/add', methods=['GET', 'POST'])
def add_award():
    error_message = None

    if request.method == 'POST':
        badge_id = request.form['badgeid']
        validity_period = request.form['validity_period']
        bonus = request.form['bonus']
        category = request.form['category']
        description = request.form['description']

        conn = connect_to_database()

        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO award (badgeid, validity_period, bonus, category, description) VALUES (%s, %s, %s, %s, %s)",
                               (badge_id, validity_period, bonus, category, description))
                conn.commit()
                conn.close()
                return redirect('/award')
            except Exception as e:
                error_message = f"Error adding award: {e}"
                return render_template('add_award.html', error_message=error_message)
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_award.html', error_message=error_message)

@app.route('/shift/add', methods=['GET', 'POST'])
def add_shift():
    error_message = None

    if request.method == 'POST':
        shift_id = request.form['shift_id']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        day = request.form['day']

        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO shift (shift_id, start_time, end_time, day) VALUES (%s, %s, %s, %s)",
                               (shift_id, start_time, end_time, day))
                conn.commit()
                conn.close()
                return redirect('/shift')
            except Exception as e:
                error_message = f"Error adding shift: {e}"
                return render_template('add_shift.html', error_message=error_message)
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_shift.html', error_message=error_message)

@app.route('/receives/add', methods=['GET', 'POST'])
def add_receives():
    error_message = None
    if request.method == 'POST':
        staff_id = request.form['staffid_fk']
        badge_id = request.form['badgeid_fk']
        date = request.form['date']

        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO receives (staffid_fk, badgeid_fk, date) VALUES (%s, %s, %s)",
                               (staff_id, badge_id, date))
                conn.commit()
                conn.close()
                return redirect('/receives')
            except Exception as e:
                error_message = f"Error adding entry: {e}"
                return render_template('add_receives.html', error_message=error_message)
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_receives.html', error_message=error_message)

@app.route('/provides/add', methods=['GET', 'POST'])
def add_provides():
    error_message = None

    if request.method == 'POST':
        StaffID = request.form['StaffID']
        ServiceID = request.form['ServiceID']
        Shift_ID = request.form['Shift_ID']

        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO public.provides( staffid_fk, serviceid_fk, shift_id_fk) VALUES (%s,%s, %s);",(StaffID, ServiceID, Shift_ID))
                conn.commit()
                conn.close()
                return redirect('/provides')
            except Exception as e:
                error_message = f"Error adding provides: {e}"
                return render_template('add_provides.html', error_message=error_message)
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_provides.html', error_message=error_message)
    
@app.route('/event/add', methods=['GET', 'POST'])
def add_event():
    error_message = None

    if request.method == 'POST':
        EventID = request.form['EventID']
        Name = request.form['Name']
        Type = request.form['Type']
        Description = request.form['Description']
        Location = request.form['Location']
        Capacity = request.form['Capacity']
        
        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO public.event (eventid, name, type, description, location, capacity) VALUES (%s, %s, %s, %s,%s, %s);",(EventID, Name, Type,Description,Location, Capacity))
                conn.commit()
                conn.close()
                return redirect('/event')
            except Exception as e:
                error_message = f"Error adding event: {e}"
                return render_template('add_event.html', error_message=error_message)
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_event.html', error_message=error_message)
    
@app.route('/holds/add', methods=['GET', 'POST'])
def add_holds():
    error_message = None

    if request.method == 'POST':
        ServiceID = request.form['ServiceID']
        EventID = request.form['EventID']
        Date = request.form['Date']
        Start_time = request.form['Start_time']
        End_time = request.form['End_time']
        
        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO public.holds( serviceid_fk, eventid_fk, date, start_time, end_time) VALUES (%s, %s, %s, %s, %s);",(ServiceID, EventID, Date,Start_time,End_time))
                conn.commit()
                conn.close()
                return redirect('/holds')
            except Exception as e:
                error_message = f"Error adding holds: {e}"
                return render_template('add_holds.html', error_message=error_message)
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_holds.html', error_message=error_message)

@app.route('/contractor/add', methods=['GET', 'POST'])
def add_contractor():
    error_message = None

    if request.method == 'POST':
        Name  = request.form['Name']
        Start_date = request.form['Start_date']
        End_date = request.form['End_date']
        Type = request.form['Type']
        Phone_number = request.form['Phone_number']
        Location  = request.form['Location']
        ServiceID = request.form['ServiceID']
        Amount = request.form['Amount']
        Supervisor = request.form['Supervisor']
        Description = request.form['Description']
        
        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO public.contractor( name, start_date, end_date, type, phone_number, location, serviceid_fk, amount, supervisor, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(Name, Start_date, End_date,Type,Phone_number,Location,ServiceID,Amount,Supervisor,Description))
                conn.commit()
                conn.close()
                return redirect('/contractor')
            except Exception as e:
                error_message = f"Error adding holds: {e}"
                return render_template('add_contractor.html', error_message=error_message)
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_contractor.html', error_message=error_message)
    
@app.route('/supplier/add', methods=['GET', 'POST'])
def add_supplier():
    error_message = None

    if request.method == 'POST':
        Name = request.form['Name']
        Phone_number = request.form['Phone_number']
        Location = request.form['Location']
        Type = request.form['Type']
        Email = request.form['Email']
       
        
        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO public.supplier( name, phone_number, location, type, email) VALUES (%s, %s, %s, %s, %s);",(Name, Phone_number, Location,Type,Email))
                conn.commit()
                conn.close()
                return redirect('/supplier')
            except Exception as e:
                error_message = f"Error adding supplier: {e}"
                return render_template('add_supplier.html', error_message=error_message)
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_supplier.html', error_message=error_message)
    
@app.route('/inventory/add', methods=['GET', 'POST'])
def add_inventory():
    error_message = None

    if request.method == 'POST':
        Inventory_ID = request.form['Inventory_ID']
        Dep_Name = request.form['Dep_Name']
        Type = request.form['Type']
        Name = request.form['Name']
        Price = request.form['Price']
        Amount = request.form['Amount']
       
        
        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO public.inventory( inventory_id, dep_name_fk, type, name, price, amount) VALUES (%s, %s, %s, %s, %s, %s);",(Inventory_ID, Dep_Name, Type,Name,Price,Amount))
                conn.commit()
                conn.close()
                return redirect('/inventory')
            except Exception as e:
                error_message = f"Error adding inventory: {e}"
                return render_template('add_inventory.html', error_message=error_message)
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_inventory.html', error_message=error_message)
    
@app.route('/supplies/add', methods=['GET', 'POST'])
def add_supplies():
    error_message = None

    if request.method == 'POST':
        Date_supplied = request.form['Date_supplied']
        InventoryID = request.form['InventoryID']
        SupplierName = request.form['SupplierName']
        Amount = request.form['Amount']
       
        
        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO public.supplies(date_supplied, inventoryid_fk, suppliername_fk, amount) VALUES (%s, %s, %s, %s);",(Date_supplied, InventoryID, SupplierName,Amount))
                conn.commit()
                conn.close()
                return redirect('/supplies')
            except Exception as e:
                error_message = f"Error adding supplies: {e}"
                return render_template('add_supplies.html', error_message=error_message)
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_supplies.html', error_message=error_message)
    
@app.route('/location/add', methods=['GET', 'POST'])
def add_location():
    error_message = None

    if request.method == 'POST':
        Location = request.form['Location']
        InventoryID = request.form['InventoryID']
       
        
        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO public.location( location, inventoryid_fk) VALUES (%s, %s);",(Location, InventoryID))
                conn.commit()
                conn.close()
                return redirect('/location')
            except Exception as e:
                error_message = f"Error adding location: {e}"
                return render_template('add_location.html', error_message=error_message)
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_location.html', error_message=error_message)
    


#edit
@app.route('/bill/edit/<int:bill_id>', methods=['GET', 'POST'])
def edit_bill(bill_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    if request.method == 'POST':
        try:
            cursor.execute("UPDATE bill SET date_created = %s, grand_total = %s, customer_id_fk = %s WHERE bill_id = %s",
                           (request.form['DC'], request.form['GT'], request.form['cid'], bill_id))
            conn.commit()
            conn.close()
        except Exception as e:
                error_message = f"Error adding bill: {e}"
                return render_template('edit_bill.html', error_message=error_message)
        return redirect('/bill')
    else:
        cursor.execute("SELECT * FROM bill WHERE bill_id = %s", (bill_id,))
        bill_data = cursor.fetchone()
        conn.close()
        return render_template('edit_bill.html', bill=bill_data)

@app.route('/pays/edit/<payment_date>/<int:bill_id>', methods=['GET', 'POST'])
def edit_pays(payment_date, bill_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    if request.method == 'POST':
        try:
            new_payment_date = request.form['PD']
            new_amount_paid = request.form['AP']
            new_payment_method = request.form['PM']

            cursor.execute("UPDATE pays SET payment_date = %s, amount_paid = %s, payment_method = %s WHERE payment_date = %s AND bill_id_fk = %s",
                           (new_payment_date, new_amount_paid, new_payment_method, payment_date, bill_id))
            
            conn.commit()
            conn.close()
            return redirect('/pays')
        except Exception as e:
            error_message = f"Error editing payment: {e}"
            return render_template('edit_pays.html', error_message=error_message)
    else:
        cursor.execute("SELECT * FROM pays WHERE payment_date = %s AND bill_id_fk = %s", (payment_date, bill_id))
        pay_data = cursor.fetchone()
        conn.close()
        return render_template('edit_pays.html', pay=pay_data)


    
@app.route('/department/edit/<name>', methods=['GET', 'POST'])
def edit_department(name):
    conn = connect_to_database()
    cursor = conn.cursor()
    if request.method == 'POST':
        try:
            cursor.execute("UPDATE department SET phone_number = %s, location = %s WHERE name = %s",
                           (request.form['pn'], request.form['loc'], name))
            conn.commit()
            conn.close()
        except Exception as e:
                error_message = f"Error editing department: {e}"
                return render_template('edit_department.html', error_message=error_message)
        return redirect('/department')
    else:
        cursor.execute("SELECT * FROM department WHERE name = %s", (name,))
        dep_data = cursor.fetchone()
        conn.close()
        return render_template('edit_department.html', dep=dep_data)
# Route to delete a customer
@app.route('/books/edit/<start_time>/<end_time>/<room_number>/<customer_id>', methods=['GET', 'POST'])
def edit_books(start_time, end_time, room_number, customer_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        try:
            new_start_time = request.form['start_time']
            new_end_time = request.form['end_time']
            new_room_number = request.form['room_number']
            new_customer_id = request.form['customer_id']
            new_date_booked = request.form['date_booked']

            cursor.execute("UPDATE books SET start_timestamp = %s, end_timestamp = %s, roomnumber_fk = %s, customerid_fk = %s, date_booked = %s WHERE start_timestamp = %s AND end_timestamp = %s AND roomnumber_fk = %s AND customerid_fk = %s",
                           (new_start_time, new_end_time, new_room_number, new_customer_id, new_date_booked, start_time, end_time, room_number, customer_id))
            conn.commit()
            conn.close()
            return redirect('/books')
        except Exception as e:
            error_message = f"Error editing book: {e}"
            return render_template('edit_books.html', error_message=error_message)
    else:
        cursor.execute("SELECT * FROM books WHERE start_timestamp = %s AND end_timestamp = %s AND roomnumber_fk = %s AND customerid_fk = %s",
                       (start_time, end_time, room_number, customer_id))
        book_data = cursor.fetchone()
        conn.close()
        return render_template('edit_books.html', book=book_data)

@app.route('/dependents/edit/<first_name>/<last_name>/<int:staff_id>', methods=['GET', 'POST'])
def edit_dependent(first_name, last_name, staff_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    if request.method == 'POST':
        try:
            new_last_name = request.form['last_name']
            new_staff_id = request.form['staff_id']
            new_relationship = request.form['relationship']
            new_birth_date = request.form['birth_date']
            new_phone_number = request.form['phone_number']
            new_gender = request.form['gender']

            cursor.execute("UPDATE dependent SET last_name = %s, staffid_fk = %s, relationship = %s, birth_date = %s, phone_number = %s, gender = %s WHERE first_name = %s AND last_name = %s AND staffid_fk = %s",
                           (new_last_name, new_staff_id, new_relationship, new_birth_date, new_phone_number, new_gender, first_name, last_name, staff_id))
            
            conn.commit()
            conn.close()
            return redirect('/dependents')
        except Exception as e:
            error_message = f"Error editing dependent: {e}"
            return render_template('edit_dependents.html', error_message=error_message, dep=[first_name, last_name, staff_id])
    else:
        cursor.execute("SELECT * FROM dependent WHERE first_name = %s AND last_name = %s AND staffid_fk = %s", (first_name, last_name, staff_id))
        dep_data = cursor.fetchone()
        conn.close()
        return render_template('edit_dependents.html', dep=dep_data)

@app.route('/award/edit/<badgeid>', methods=['GET', 'POST'])
def edit_award(badgeid):
    conn = connect_to_database()
    cursor = conn.cursor()

    if request.method == 'POST':
        try:
            new_validity_period = request.form['validity_period']
            new_bonus = request.form['bonus']
            new_category = request.form['category']
            new_description = request.form['description']

            cursor.execute("UPDATE award SET validity_period = %s, bonus = %s, category = %s, description = %s WHERE badgeid = %s",
                           (new_validity_period, new_bonus, new_category, new_description, badgeid))
            
            conn.commit()
            conn.close()
            return redirect('/award')
        except Exception as e:
            error_message = f"Error editing award: {e}"
            return render_template('edit_award.html', error_message=error_message, award={'badgeid': badgeid})
    else:
        cursor.execute("SELECT * FROM award WHERE badgeid = %s", (badgeid,))
        award_data = cursor.fetchone()
        conn.close()
        return render_template('edit_award.html', award=award_data)

@app.route('/shift/edit/<shift_id>', methods=['GET', 'POST'])
def edit_shift(shift_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    if request.method == 'POST':
        try:
            new_start_time = request.form['start_time']
            new_end_time = request.form['end_time']
            new_day = request.form['day']

            cursor.execute("UPDATE shift SET start_time = %s, end_time = %s, day = %s WHERE shift_id = %s",
                           (new_start_time, new_end_time, new_day, shift_id))

            conn.commit()
            conn.close()
            return redirect('/shift')
        except Exception as e:
            error_message = f"Error editing shift: {e}"
            return render_template('edit_shift.html', error_message=error_message, shift={'shift_id': shift_id})
    else:
        cursor.execute("SELECT * FROM shift WHERE shift_id = %s", (shift_id,))
        shift_data = cursor.fetchone()
        conn.close()
        return render_template('edit_shift.html', shift=shift_data)

@app.route('/receives/edit/<staff_id>/<badge_id>/<date>', methods=['GET', 'POST'])
def edit_receives(staff_id, badge_id, date):
    conn = connect_to_database()
    cursor = conn.cursor()

    if request.method == 'POST':
        try:
            new_staff_id = request.form['staffid_fk']
            new_badge_id = request.form['badgeid_fk']
            new_date = request.form['date']

            cursor.execute("UPDATE receives SET staffid_fk = %s, badgeid_fk = %s, date = %s WHERE staffid_fk = %s AND badgeid_fk = %s AND date = %s",
                           (new_staff_id, new_badge_id, new_date, staff_id, badge_id, date))
            
            conn.commit()
            conn.close()
            return redirect('/receives')
        except Exception as e:
            error_message = f"Error editing entry: {e}"
            return render_template('edit_receives.html', error_message=error_message, entry={'staffid_fk': staff_id, 'badgeid_fk': badge_id, 'date': date})
    else:
        cursor.execute("SELECT * FROM receives WHERE staffid_fk = %s AND badgeid_fk = %s AND date = %s", (staff_id, badge_id, date))
        entry_data = cursor.fetchone()
        conn.close()
        return render_template('edit_receives.html', entry=entry_data)

@app.route('/provides/edit/<int:staff_id>/<int:service_id>/<int:shift_id>', methods=['GET', 'POST'])
def edit_provides(staff_id, service_id, shift_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    if request.method == 'POST':
        try:
            cursor.execute("UPDATE public.provides SET staffid_fk = %s, serviceid_fk = %s, shift_id_fk = %s WHERE staffid_fk = %s AND serviceid_fk = %s AND shift_id_fk = %s",
                           (request.form['staffid'], request.form['serviceid'], request.form['shift_id'], staff_id, service_id, shift_id))
            conn.commit()
            conn.close()
        except Exception as e:
            error_message = f"Error updating provides: {e}"
            return render_template('edit_provides.html', error_message=error_message)
        
        return redirect('/provides')
    else:
        cursor.execute("SELECT * FROM public.provides WHERE staffid_fk = %s AND serviceid_fk = %s AND shift_id_fk = %s", (staff_id, service_id, shift_id))
        provides_data = cursor.fetchone()
        conn.close()
        return render_template('edit_provides.html', provides=provides_data)



@app.route('/event/edit/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    if request.method == 'POST':
        try:
            cursor.execute("UPDATE public.event SET EventID = %s, Name = %s, Type = %s, Description = %s, Location = %s, Capacity = %s WHERE EventID = %s",
                           (request.form['event_id'], request.form['name'], request.form['type'], request.form['description'], request.form['location'], request.form['capacity'], event_id))
            conn.commit()
            conn.close()
        except Exception as e:
            error_message = f"Error updating event: {e}"
            return render_template('edit_event.html', error_message=error_message)

        return redirect('/event')
    else:
        cursor.execute("SELECT * FROM public.event WHERE EventID = %s", (event_id,))
        event_data = cursor.fetchone()
        conn.close()
        return render_template('edit_event.html', event=event_data)

    


@app.route('/holds/edit/<int:service_id>/<int:event_id>/<string:date>', methods=['GET', 'POST'])
def edit_holds(service_id, event_id, date):
    conn = connect_to_database()
    cursor = conn.cursor()

    if request.method == 'POST':
        try:
            cursor.execute("UPDATE public.holds SET ServiceID_fk = %s, EventID_fk = %s, Date = %s, Start_time = %s, End_time = %s WHERE ServiceID_fk = %s AND EventID_fk = %s AND Date = %s",
                           (request.form['service_id'], request.form['event_id'], request.form['date'], request.form['start_time'], request.form['end_time'], service_id, event_id, date))
            conn.commit()
            conn.close()
        except Exception as e:
            error_message = f"Error updating holds: {e}"
            return render_template('edit_holds.html', error_message=error_message)

        return redirect('/holds')
    else:
        cursor.execute("SELECT * FROM public.holds WHERE ServiceID_fk = %s AND EventID_fk = %s AND Date = %s", (service_id, event_id, date))
        holds_data = cursor.fetchone()
        conn.close()
        return render_template('edit_holds.html', holds=holds_data)


@app.route('/contractor/edit/<string:name>/<string:start_date>/<string:end_date>', methods=['GET', 'POST'])
def edit_contractor(name, start_date, end_date):
    conn = connect_to_database()
    cursor = conn.cursor()

    if request.method == 'POST':
        try:
            cursor.execute("UPDATE public.contractor SET Name = %s, Start_date = %s, End_date = %s, Type = %s, Phone_number = %s, Location = %s, ServiceID_fk = %s, Amount = %s, Supervisor = %s, Description = %s WHERE Name = %s AND Start_date = %s AND End_date = %s",
                           (request.form['name'], request.form['start_date'], request.form['end_date'], request.form['type'], request.form['phone_number'], request.form['location'], request.form['service_id_fk'], request.form['amount'], request.form['supervisor'], request.form['description'], name, start_date, end_date))
            conn.commit()
            conn.close()
        except Exception as e:
            error_message = f"Error updating contractor: {e}"
            return render_template('edit_contractor.html', error_message=error_message)

        return redirect('/contractor')
    else:
        cursor.execute("SELECT * FROM public.contractor WHERE Name = %s AND Start_date = %s AND End_date = %s", (name, start_date, end_date))
        contractor_data = cursor.fetchone()
        conn.close()
        return render_template('edit_contractor.html', contractor=contractor_data)



@app.route('/supplier/edit/<string:name>', methods=['GET', 'POST'])
def edit_supplier(name):
    conn = connect_to_database()
    cursor = conn.cursor()

    if request.method == 'POST':
        try:
            cursor.execute("UPDATE public.supplier SET Name = %s, Phone_number = %s, Location = %s, Type = %s, Email = %s WHERE Name = %s",
                           (request.form['name'], request.form['phone_number'], request.form['location'], request.form['type'], request.form['email'], name))
            conn.commit()
            conn.close()
        except Exception as e:
            error_message = f"Error updating supplier: {e}"
            return render_template('edit_supplier.html', error_message=error_message)

        return redirect('/supplier')
    else:
        cursor.execute("SELECT * FROM public.supplier WHERE Name = %s", (name,))
        supplier_data = cursor.fetchone()
        conn.close()
        return render_template('edit_supplier.html', supplier=supplier_data)



@app.route('/inventory/edit/<int:inventory_id>', methods=['GET', 'POST'])
def edit_inventory(inventory_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    if request.method == 'POST':
        try:
            cursor.execute("UPDATE public.inventory SET Inventory_ID = %s, Dep_Name_fk = %s, Type = %s, Name = %s, Price = %s, Amount = %s WHERE Inventory_ID = %s",
                           (request.form['inventory_id'], request.form['dep_name_fk'], request.form['type'], request.form['name'], request.form['price'], request.form['amount'], inventory_id))
            conn.commit()
            conn.close()
        except Exception as e:
            error_message = f"Error updating inventory: {e}"
            return render_template('edit_inventory.html', error_message=error_message)

        return redirect('/inventory')
    else:
        cursor.execute("SELECT * FROM public.inventory WHERE Inventory_ID = %s", (inventory_id,))
        inventory_data = cursor.fetchone()
        conn.close()
        return render_template('edit_inventory.html', inventory=inventory_data)



@app.route('/supplies/edit/<string:date_supplied>/<int:inventory_id_fk>/<string:supplier_name_fk>', methods=['GET', 'POST'])
def edit_supplies(date_supplied, inventory_id_fk, supplier_name_fk):
    conn = connect_to_database()
    cursor = conn.cursor()

    if request.method == 'POST':
        try:
            cursor.execute("UPDATE public.supplies SET Date_supplied = %s, InventoryID_fk = %s, SupplierName_fk = %s, Amount = %s WHERE Date_supplied = %s AND InventoryID_fk = %s AND SupplierName_fk = %s",
                           (request.form['date_supplied'], request.form['inventory_id_fk'], request.form['supplier_name_fk'], request.form['amount'], date_supplied, inventory_id_fk, supplier_name_fk))
            conn.commit()
            conn.close()
        except Exception as e:
            error_message = f"Error updating supplies: {e}"
            return render_template('edit_supplies.html', error_message=error_message)

        return redirect('/supplies')
    else:
        cursor.execute("SELECT * FROM public.supplies WHERE Date_supplied = %s AND InventoryID_fk = %s AND SupplierName_fk = %s", (date_supplied, inventory_id_fk, supplier_name_fk))
        supplies_data = cursor.fetchone()
        conn.close()
        return render_template('edit_supplies.html', supplies=supplies_data)
    
    
@app.route('/location/edit/<string:location>/<int:inventory_id_fk>', methods=['GET', 'POST'])
def edit_location(location, inventory_id_fk):
    conn = connect_to_database()
    cursor = conn.cursor()

    if request.method == 'POST':
        try:
            cursor.execute("UPDATE public.location SET Location = %s, InventoryID_fk = %s WHERE Location = %s AND InventoryID_fk = %s",
                           (request.form['location'], request.form['inventory_id_fk'], location, inventory_id_fk))
            conn.commit()
            conn.close()
        except Exception as e:
            error_message = f"Error updating location: {e}"
            return render_template('edit_location.html', error_message=error_message)

        return redirect('/location')
    else:
        cursor.execute("SELECT * FROM public.location WHERE Location = %s AND InventoryID_fk = %s", (location, inventory_id_fk))
        location_data = cursor.fetchone()
        conn.close()
        return render_template('edit_location.html', location=location_data)

@app.route('/error', methods=['GET'])
def provides_error():
    error_message = "An error occurred in the provides context."
    return render_template('error.html', error_message=error_message, redirect_url='/provides', redirect_label='')



#delete
@app.route('/bill/delete/<int:bill_id>', methods=['POST'])
def delete_bill(bill_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bill WHERE bill_id = %s", (bill_id,))
    conn.commit()
    conn.close()
    return redirect('/bill')
@app.route('/pays/delete/<payment_date>/<int:bill_id>', methods=['POST'])
def delete_pays(payment_date, bill_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM pays WHERE payment_date = %s AND bill_id_fk = %s", (payment_date, bill_id))
        conn.commit()
        conn.close()
    except Exception as e:
        error_message = f"Error deleting payment: {e}"
        return render_template('delete_pays.html', error_message=error_message, pay=[payment_date, bill_id])

    return redirect('/pays')

@app.route('/department/delete/<name>', methods=['POST'])
def delete_department(name):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM department WHERE name = %s", (name,))
    conn.commit()
    conn.close()
    return redirect('/department')
@app.route('/books/delete/<start_time>/<end_time>/<int:room_number>/<int:customer_id>', methods=['POST'])
def delete_book(start_time, end_time, room_number, customer_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE start_timestamp = %s AND end_timestamp = %s AND roomnumber_fk = %s AND customerid_fk = %s", (start_time, end_time, room_number, customer_id))
    conn.commit()
    conn.close()
    return redirect('/books')
@app.route('/dependents/delete/<first_name>/<last_name>/<staff_id>', methods=['POST'])
def delete_dependent(first_name, last_name, staff_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        try:
            cursor.execute("DELETE FROM dependent WHERE first_name = %s AND last_name = %s AND staffid_fk = %s", (first_name, last_name, staff_id))
            conn.commit()
            conn.close()
            return redirect('/dependents')
        except Exception as e:
            error_message = f"Error deleting dependent: {e}"
            return render_template('dependents.html', error_message=error_message)

@app.route('/award/delete/<badgeid>', methods=['POST'])
def delete_award(badgeid):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM award WHERE badgeid = %s", (badgeid,))
        conn.commit()
        conn.close()
        return redirect('/award')  # Redirect to the award page after successful deletion
    except Exception as e:
        error_message = f"Error deleting award: {e}"
        # Handle the error accordingly
        return error_message  # Or return a specific error message or redirect somewhere else

@app.route('/shift/delete/<int:shift_id>', methods=['POST'])
def delete_shift(shift_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM shift WHERE shift_id = %s", (shift_id,))
        conn.commit()
        conn.close()
        return redirect('/shift')  # Redirect to the shift display page after deletion
    except Exception as e:
        # Handle the exception and display an error message or redirect to an error page
        error_message = f"Error deleting shift: {e}"
        return render_template('error.html', error_message=error_message)

@app.route('/receives/delete/<staffid_fk>/<badgeid_fk>/<date>', methods=['POST'])
def delete_receives(staffid_fk, badgeid_fk, date):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM receives WHERE staffid_fk = %s AND badgeid_fk = %s AND date = %s",
                       (staffid_fk, badgeid_fk, date))
        conn.commit()
        conn.close()
        return redirect('/receives')
    except Exception as e:
        error_message = f"Error deleting receives entry: {e}"
        return render_template('receives.html', error_message=error_message)

@app.route('/provides/delete/<int:staff_id>/<int:service_id>/<int:shift_id>', methods=['POST'])
def delete_provides(staff_id, service_id, shift_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM public.provides WHERE StaffID_fk = %s AND ServiceID_fk = %s AND Shift_ID_fk = %s",
                       (staff_id, service_id, shift_id))
        conn.commit()
        conn.close()
    except Exception as e:
        error_message = f"Error deleting provides entry: {e}"
        print("noob")
        #return render_template('delete_provides.html', error_message=error_message, provides=[staff_id, service_id, shift_id])
        return render_template('error.html', error_message=error_message, redirect_url='/provides', redirect_label='Provides')
    return redirect('/provides')


@app.route('/event/delete/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM public.event WHERE EventID = %s", (event_id,))
        conn.commit()
        conn.close()
    except Exception as e:
        error_message = f"Error deleting event: {e}"
        print("noob")
        return render_template('error.html', error_message=error_message, redirect_url='/event', redirect_label='event')

    return redirect('/event')


@app.route('/holds/delete/<int:service_id>/<int:event_id>/<string:date>', methods=['POST'])
def delete_holds(service_id, event_id, date):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM public.holds WHERE ServiceID_fk = %s AND EventID_fk = %s AND Date = %s",
                       (service_id, event_id, date))
        conn.commit()
        conn.close()
    except Exception as e:
        error_message = f"Error deleting holds entry: {e}"
        return render_template('error.html', error_message=error_message, redirect_url='/holds', redirect_label='holds')


    return redirect('/holds')

@app.route('/contractor/delete/<string:name>/<string:start_date>/<string:end_date>', methods=['POST'])
def delete_contractor(name, start_date, end_date):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM public.contractor WHERE Name = %s AND Start_date = %s AND End_date = %s",
                       (name, start_date, end_date))
        conn.commit()
        conn.close()
    except Exception as e:
        error_message = f"Error deleting contractor: {e}"
        return render_template('error.html', error_message=error_message, redirect_url='/contractor', redirect_label='contractor')

    return redirect('/contractor')

@app.route('/supplier/delete/<string:name>', methods=['POST'])
def delete_supplier(name):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM public.supplier WHERE Name = %s", (name,))
        conn.commit()
        conn.close()
    except Exception as e:
        error_message = f"Error deleting supplier: {e}"
        return render_template('error.html', error_message=error_message, redirect_url='/supplier', redirect_label='supplier')

    return redirect('/supplier')

@app.route('/inventory/delete/<int:inventory_id>', methods=['POST'])
def delete_inventory(inventory_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM public.inventory WHERE Inventory_ID = %s", (inventory_id,))
        conn.commit()
        conn.close()
    except Exception as e:
        error_message = f"Error deleting inventory: {e}"
        return render_template('error.html', error_message=error_message, redirect_url='/inventory', redirect_label='inventory')

    return redirect('/inventory')

@app.route('/supplies/delete/<string:date_supplied>/<int:inventory_id_fk>/<string:supplier_name_fk>', methods=['POST'])
def delete_supplies(date_supplied, inventory_id_fk, supplier_name_fk):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM public.supplies WHERE Date_supplied = %s AND InventoryID_fk = %s AND SupplierName_fk = %s",
                       (date_supplied, inventory_id_fk, supplier_name_fk))
        conn.commit()
        conn.close()
    except Exception as e:
        error_message = f"Error deleting supplies entry: {e}"
        return render_template('error.html', error_message=error_message, redirect_url='/supplies', redirect_label='supplies')

    return redirect('/supplies')

@app.route('/location/delete/<string:location>/<int:inventory_id_fk>', methods=['POST'])
def delete_location(location, inventory_id_fk):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM public.location WHERE Location = %s AND InventoryID_fk = %s",
                       (location, inventory_id_fk))
        conn.commit()
        conn.close()
    except Exception as e:
        error_message = f"Error deleting location entry: {e}"
        return render_template('error.html', error_message=error_message, redirect_url='/location', redirect_label='location')

    return redirect('/location')



#Complex Queries

@app.route('/customer_payment')
def customer_payment():
    conn = connect_to_database()
    cursor = conn.cursor()
    query = """
	WITH 
	min_date AS(
		SELECT MIN(c.latest_checkin) AS first_checkin_not_check_out, c.customerid_fk
				FROM (
					SELECT ci.roomnumber_fk, ci.customerid_fk, MAX(ci.date) AS latest_checkin
					FROM checks_in ci
					GROUP BY ci.roomnumber_fk, ci.customerid_fk ) AS c
				LEFT JOIN checks_out co ON c.roomnumber_fk = co.roomnumber_fk
				AND c.customerid_fk = co.customerid_fk AND co.date> c.latest_checkin
				WHERE co.date IS NULL 
				GROUP BY c.customerid_fk
	),
	payment1 AS (
		SELECT SUM(b.amount_paid) AS total_amount_paid, c.customer_id_fk
		FROM pays AS b
		JOIN bill c ON c.Bill_ID = b.Bill_ID_fk 
		WHERE b.payment_date  >= (
			SELECT first_checkin_not_check_out
			FROM min_date AS m
			WHERE m.customerid_fk = c.customer_id_fk
		)
		GROUP BY  c.customer_id_fk
	),
	payment2 AS (
		SELECT SUM(b.grand_total) AS grandTotal, b.customer_id_fk 
		FROM bill AS b
		WHERE b.date_created >= (
			SELECT first_checkin_not_check_out
			FROM min_date AS m
			WHERE m.customerid_fk = b.customer_id_fk
		)
		GROUP BY b.customer_id_fk
	)

	SELECT p.customer_id_fk, p.total_amount_paid, p2.grandTotal, (p2.grandTotal- p.total_amount_paid) AS remaining
	FROM payment1 p
	JOIN payment2 p2 ON p.customer_id_fk = p2.customer_id_fk;



    """

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()

    return render_template('customer_payment.html', data=result)


@app.route('/supplier_com', methods=['GET', 'POST'])
def supplier_com():
    if request.method == 'POST':
        supplier_name = request.form['supplier']

        # SQL query with parameter
        query = """
            SELECT name, phone_number
            FROM department
            WHERE name IN (
                SELECT DISTINCT dep_name_fk 
                FROM inventory
                WHERE inventory_id IN (
                    SELECT DISTINCT inventoryid_fk
                    FROM supplies
                    WHERE LOWER(suppliername_fk) LIKE LOWER(%s)
                )
            );
        """

        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute(query, (f'%{supplier_name}%',))
        results = cursor.fetchall()
        conn.close()

        return render_template('supplier_com.html', results=results)

    return render_template('supplier_com.html')


@app.route('/search_staff', methods=['GET', 'POST'])
def search_staff():
    if request.method == 'POST':
        min_salary = request.form['min_salary']
        max_salary = request.form['max_salary']

        # SQL query with parameters for minimum and maximum salary
        query = """
            WITH sid(staffid) AS (
                SELECT staffid FROM staff
                EXCEPT 
                SELECT DISTINCT staffid_fk FROM receives
            )
            SELECT *
            FROM staff AS st
            WHERE (
                (EXISTS (SELECT staffid FROM sid LIMIT 1) 
                AND st.staffid IN (
                    (WITH filter_dep(staffid, CO) AS (
                        SELECT d.staffid_fk, COUNT(d.*) AS CO FROM dependent AS d
                        WHERE d.staffid_fk IN (SELECT S.staffid FROM sid AS S)
                        GROUP BY d.staffid_fk)
                    SELECT staffid
                    FROM filter_dep
                    WHERE ((CO BETWEEN (SELECT MAX(CO) FROM filter_dep) AND (SELECT MAX(CO) - 1 FROM filter_dep))
                        OR CO =(SELECT MAX(CO) FROM filter_dep))
                    ))
                ) 
                OR st.staffid IN (
                    (WITH filter_receives(staffid_fk, CO) AS (
                        SELECT r.staffid_fk, COUNT(r.*) AS CO 
                        FROM receives AS r
                        GROUP BY r.staffid_fk),
                    filter_dep(staffid, COO) AS (
                        SELECT f.staffid_fk, COUNT(f.*) AS COO 
                        FROM filter_receives f 
                        JOIN dependent d ON d.staffid_fk = f.staffid_fk
                        WHERE f.CO BETWEEN (SELECT MIN(CO) FROM filter_receives) AND (SELECT MIN(CO) + 1 FROM filter_receives)
                        GROUP BY f.staffid_fk )
                    SELECT fi.staffid 
                    FROM filter_dep AS fi
                    WHERE fi.COO BETWEEN (SELECT MAX(COO) FROM filter_dep) AND (SELECT MAX(COO) - 1 FROM filter_dep)
                    OR fi.COO = (SELECT MAX(COO) FROM filter_dep))
                )
            ) AND st.salary BETWEEN %s AND %s;
        """

        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute(query, (min_salary, max_salary))
        results = cursor.fetchall()
        conn.close()

        return render_template('search_staff.html', results=results)

    return render_template('search_staff.html')

@app.route('/customer_com', methods=['GET', 'POST'])
def customer_com():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        # SQL query with parameters for customer's first and last names
        query = """
            SELECT h.start_time, u.date, e.* , ARRAY_AGG(co.name) AS contractors
            FROM holds h
            JOIN uses u ON CAST(u.date AS TIME) >= h.start_time
                        AND CAST(u.date AS TIME) <= h.end_time 
                        AND CAST(u.date AS DATE) = h.date
            JOIN customer c ON c.customer_id = u.customerid_fk
            JOIN service s ON s.id = h.serviceid_fk AND s.ID = u.serviceid_fk
            JOIN event e ON h.eventid_fk = e.eventid
            JOIN contractor co ON co.serviceid_fk = s.id 
            WHERE c.first = %s AND c.last = %s
            GROUP BY h.start_time, u.date, e.eventid;
        """

        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute(query, (first_name, last_name))
        results = cursor.fetchall()
        conn.close()

        return render_template('customer_com.html', results=results)

    return render_template('customer_com.html')
@app.route('/service_usage')
def display_service_usage():
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT C.customer_id, S.type, COUNT(S.type) AS Nb_Uses
            FROM service AS S
            JOIN uses AS U ON U.serviceid_fk = S.ID
            JOIN customer AS C ON U.customerid_fk = C.customer_id
            WHERE U.DATE BETWEEN 
                (SELECT MAX(date) FROM checks_in WHERE customerid_fk = C.customer_id) AND 
                (SELECT MAX(date) FROM checks_out WHERE customerid_fk = C.customer_id)
            GROUP BY C.customer_id, S.type;
        """)

        data = cursor.fetchall()
        conn.close()
        return render_template('service_usage.html', data=data)
    except Exception as e:
        error_message = f"Error fetching service usage data: {e}"
        return render_template('service_usage.html', error_message=error_message)

@app.route('/display_complaint')
def display_complaint():
    event_name = request.args.get('event_name')  # Fetch event name from user input
    holds_date = request.args.get('holds_date')  # Fetch holds date from user input

    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT St.staffid, St.fname, St.lname
            FROM STAFF AS St
            WHERE EXISTS (
                SELECT 1
                FROM Provides AS P
                WHERE P.shift_id_fk IN (
                    SELECT S.shift_id
                    FROM shift AS S
                    WHERE EXISTS (
                        SELECT 1
                        FROM Holds AS H
                        LEFT JOIN Event AS E ON H.eventid_fk = E.eventid 
                        WHERE E.name = %s
                            AND S.start_time <= H.end_time
                            AND S.end_time >= H.start_time
                            AND TO_CHAR(H.date, 'FMDay') = S.day
                            AND H.serviceid_fk = P.serviceid_fk
                            AND H.date = %s
                        )
                    )

                    AND P.staffid_fk = St.staffid
                )
                AND NOT EXISTS (
                    SELECT *
                    FROM dependent AS D
                    WHERE D.staffid_fk = St.staffid
                )
                AND St.gender='Female';
            """, (event_name, holds_date))

        data = cursor.fetchall()
        conn.close()
        return render_template('complaint.html', data=data)
    except Exception as e:
        error_message = f"Error fetching staff data: {e}"
        return render_template('complaint.html', error_message=error_message)

@app.route('/update_staff_salary', methods=['GET'])
def update_staff_salary():

    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        
        update_query = '''
            WITH award_subquery AS (
                SELECT staffid_fk, COUNT(*) AS AwardsCount
                FROM receives 
                WHERE date BETWEEN current_date - INTERVAL '1 year' AND current_date
                GROUP BY staffid_fk
                HAVING COUNT(*) >= 5
            ), shift_subquery AS (
                SELECT staffid_fk, COUNT(*) AS ShiftsCount
                FROM provides
                GROUP BY staffid_fk
                HAVING COUNT(*) > 5
            )
            UPDATE staff
            SET salary = (((award_subquery.AwardsCount * 0.05) + 
                         ((shift_subquery.ShiftsCount - 5) * 0.05)) * Salary) + salary
            FROM award_subquery, shift_subquery
            WHERE staff.staffid = award_subquery.staffid_fk
              AND staff.staffid = shift_subquery.staffid_fk
            RETURNING staff.staffid, 
            award_subquery.AwardsCount, 
            shift_subquery.ShiftsCount,
            staff.salary;
        '''

        cursor.execute(update_query)
        updated_staff = cursor.fetchall()

        conn.commit()
        conn.close()

        return render_template('updated_staff.html', updated_staff=updated_staff)

    except Exception as e:
        error_message = f"Error updating staff salary: {e}"
        return render_template('updated_staff.html', error_message=error_message)

@app.route('/room_availability', methods=['GET', 'POST'])
def room_availability():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        conn = connect_to_database()
        cursor = conn.cursor()

        try:
            query = """
            SELECT
                Room_Number,
                Room_type,
                Price,
                %s AS AvailableStart,
                %s AS AvailableEnd
            FROM
                Room
            WHERE
                Room_Number NOT IN (
                    SELECT DISTINCT RoomNumber_fk
                    FROM Books
                    WHERE Start_timestamp <= %s
                    AND End_timestamp >= %s
                )
            ORDER BY Price;
            """
            cursor.execute(query, (start_date, end_date, end_date, start_date))
            room_results = cursor.fetchall()

            cursor.close()
            conn.close()

            return render_template('room_availability.html', room_results=room_results)
        except Exception as e:
            error_message = f"Error fetching room availability: {e}"
            return render_template('room_availability.html', error_message=error_message)

    return render_template('room_availability.html')


@app.route('/customer')
def display_customer():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_customer(conn)
        conn.close()
        return render_template('customer.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_customer(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM public.customer')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/customer/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        customer_id = request.form['customer_id']

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birth_date = request.form['birth_date']
        address = request.form['address']
        email = request.form['email']
        gender = request.form['gender']
        phone_number = request.form['phone_number']
        iddocument = request.form['iddocument']

        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO public.customer (customer_id, first, last, birth_date, address, email, gender, phone_number, iddocument) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)",
                           (customer_id,first_name, last_name, birth_date, address, email, gender, phone_number, iddocument))
            conn.commit()
            conn.close()
            return redirect('/customer')
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_customer.html') 

# Route to edit a customer
@app.route('/customer/edit/<int:customer_id>', methods=['GET', 'POST'])
def edit_customer(customer_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("UPDATE public.customer SET first = %s, last = %s, birth_date = %s, address = %s, email = %s, gender = %s, phone_number = %s, iddocument = %s WHERE customer_id = %s",
                       (request.form['first'], request.form['last'], request.form['birth_date'], request.form['address'], request.form['email'], request.form['gender'], request.form['phone_number'], request.form['iddocument'], customer_id))
        conn.commit()
        conn.close()
        return redirect('/customer')
    else:
        cursor.execute("SELECT * FROM public.customer WHERE customer_id = %s", (customer_id,))
        customer_data = cursor.fetchone()
        conn.close()
        return render_template('edit_customer.html', customer=customer_data)  # Pass customer_data to populate the edit form

# Route to delete a customer
@app.route('/customer/delete/<int:customer_id>', methods=['POST'])
def delete_customer(customer_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM public.customer WHERE customer_id = %s", (customer_id,))
    conn.commit()
    conn.close()
    return redirect('/customer')


@app.route('/uses')
def display_uses():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_uses(conn)
        conn.close()
        return render_template('uses.html', data=data)
    else:
        return "Error connecting to the database."

def fetch_uses(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Uses')
    data = cursor.fetchall()
    cursor.close()
    return data
@app.route('/uses/add', methods=['GET', 'POST'])
def add_uses():
    if request.method == 'POST':
        # Get form data
        date = request.form['date']
        customer_id = request.form['customer_id']
        service_id = request.form['service_id']

        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Uses (Date, CustomerID_fk, ServiceID_fk) VALUES (%s, %s, %s)",
                           (date, customer_id, service_id))
            conn.commit()
            conn.close()
            return redirect('/uses')
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_uses.html')  # Render form to add Uses entry
@app.route('/uses/edit/<string:date>/<int:customer_id>/<int:service_id>', methods=['GET', 'POST'])
def edit_uses(date, customer_id, service_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    if request.method == 'POST':
        # Update Uses entry
        cursor.execute("UPDATE Uses SET Date = %s, CustomerID_fk = %s, ServiceID_fk = %s WHERE Date = %s AND CustomerID_fk = %s AND ServiceID_fk = %s",
                       (request.form['date'], request.form['customer_id'], request.form['service_id'], date, customer_id, service_id))
        conn.commit()
        conn.close()
        return redirect('/uses')
    else:
        cursor.execute("SELECT * FROM Uses WHERE Date = %s AND CustomerID_fk = %s AND ServiceID_fk = %s", (date, customer_id, service_id,))
        uses_data = cursor.fetchone()
        conn.close()
        return render_template('edit_uses.html', uses=uses_data)  # Pass uses_data to populate the edit form
@app.route('/uses/delete/<string:date>/<int:customer_id>/<int:service_id>', methods=['POST'])
def delete_uses(date, customer_id, service_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Uses WHERE Date = %s AND CustomerID_fk = %s AND ServiceID_fk = %s", (date, customer_id, service_id,))
    conn.commit()
    conn.close()
    return redirect('/uses')
@app.route('/room')
def display_room():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_room(conn)
        conn.close()
        return render_template('room.html', data=data)
    else:
        return "Error connecting to the database."

def fetch_room(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Room')
    data = cursor.fetchall()
    cursor.close()
    return data
@app.route('/room/add', methods=['GET', 'POST'])
def add_room():
    if request.method == 'POST':
        room_number = request.form['room_number']
        room_type = request.form['room_type']
        price = request.form['price']

        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Room (Room_Number, Room_type, Price) VALUES (%s, %s, %s)",
                           (room_number, room_type, price))
            conn.commit()
            conn.close()
            return redirect('/room')
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_room.html')
@app.route('/room/edit/<int:room_number>', methods=['GET', 'POST'])
def edit_room(room_number):
    conn = connect_to_database()
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("UPDATE Room SET Room_type = %s, Price = %s WHERE Room_Number = %s",
                       (request.form['room_type'], request.form['price'], room_number))
        conn.commit()
        conn.close()
        return redirect('/room')
    else:
        cursor.execute("SELECT * FROM Room WHERE Room_Number = %s", (room_number,))
        room_data = cursor.fetchone()
        conn.close()
        return render_template('edit_room.html', room=room_data)
@app.route('/room/delete/<int:room_number>', methods=['POST'])
def delete_room(room_number):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Room WHERE Room_Number = %s", (room_number,))
    conn.commit()
    conn.close()
    return redirect('/room')
@app.route('/checks_in')
def display_checks_in():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_checks_in(conn)
        conn.close()
        return render_template('checks_in.html', data=data)
    else:
        return "Error connecting to the database."

def fetch_checks_in(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Checks_in')
    data = cursor.fetchall()
    cursor.close()
    return data
@app.route('/checks_in/add', methods=['GET', 'POST'])
def add_checks_in():
    if request.method == 'POST':
        room_number = request.form['room_number']
        customer_id = request.form['customer_id']
        date = request.form['date']

        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Checks_in (RoomNumber_fk, CustomerID_fk, Date) VALUES (%s, %s, %s)",
                           (room_number, customer_id, date))
            conn.commit()
            conn.close()
            return redirect('/checks_in')
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_checks_in.html')
@app.route('/checks_in/edit/<int:room_number>/<int:customer_id>/<string:date>', methods=['GET', 'POST'])
def edit_checks_in(room_number, customer_id, date):
    conn = connect_to_database()
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("UPDATE Checks_in SET Date = %s WHERE RoomNumber_fk = %s AND CustomerID_fk = %s AND Date = %s",
                       (request.form['date'], room_number, customer_id, date))
        conn.commit()
        conn.close()
        return redirect('/checks_in')
    else:
        cursor.execute("SELECT * FROM Checks_in WHERE RoomNumber_fk = %s AND CustomerID_fk = %s AND Date = %s",
                       (room_number, customer_id, date))
        checks_in_data = cursor.fetchone()
        conn.close()
        return render_template('edit_checks_in.html', checks_in=checks_in_data)
@app.route('/checks_in/delete/<int:room_number>/<int:customer_id>/<string:date>', methods=['POST'])
def delete_checks_in(room_number, customer_id, date):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Checks_in WHERE RoomNumber_fk = %s AND CustomerID_fk = %s AND Date = %s",
                   (room_number, customer_id, date))
    conn.commit()
    conn.close()
    return redirect('/checks_in')

# Fetch data from Checks_out table
@app.route('/checks_out')
def display_checks_out():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_checks_out(conn)
        conn.close()
        return render_template('checks_out.html', data=data)  # Pass 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_checks_out(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Checks_out')
    data = cursor.fetchall()
    cursor.close()
    return data

# Add a new checkout record
@app.route('/checks_out/add', methods=['GET', 'POST'])
def add_checks_out():
    if request.method == 'POST':
        # Gather form data
        room_number = request.form['room_number']
        customer_id = request.form['customer_id']
        date = request.form['date']
        
        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Checks_out (RoomNumber_fk, CustomerID_fk, Date) VALUES (%s, %s, %s)",
                           (room_number, customer_id, date))
            conn.commit()
            conn.close()
            return redirect('/checks_out')
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_checks_out.html') 

# Edit a checkout record
@app.route('/checks_out/edit/<int:room_number>/<int:customer_id>/<string:date>', methods=['GET', 'POST'])
def edit_checks_out(room_number, customer_id, date):
    conn = connect_to_database()
    cursor = conn.cursor()
    if request.method == 'POST':
        # Update record
        cursor.execute("UPDATE Checks_out SET Date = %s WHERE RoomNumber_fk = %s AND CustomerID_fk = %s AND Date = %s",
                       (request.form['date'], room_number, customer_id, date))
        conn.commit()
        conn.close()
        return redirect('/checks_out')
    else:
        # Fetch record data to populate the edit form
        cursor.execute("SELECT * FROM Checks_out WHERE RoomNumber_fk = %s AND CustomerID_fk = %s AND Date = %s", (room_number, customer_id, date))
        checks_out_data = cursor.fetchone()
        conn.close()
        return render_template('edit_checks_out.html', checks_out=checks_out_data)  # Pass data to populate the edit form

# Delete a checkout record
@app.route('/checks_out/delete/<int:room_number>/<int:customer_id>/<string:date>', methods=['POST'])
def delete_checks_out(room_number, customer_id, date):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Checks_out WHERE RoomNumber_fk = %s AND CustomerID_fk = %s AND Date = %s", (room_number, customer_id, date))
    conn.commit()
    conn.close()
    return redirect('/checks_out')


@app.route('/visitor')
def display_visitor():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_visitor(conn)
        conn.close()
        return render_template('visitor.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_visitor(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Visitor')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/visitor/add', methods=['GET', 'POST'])
def add_visitor():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        customer_id_fk = request.form['customer_id_fk']
        date_of_visit = request.form['date_of_visit']
        gender = request.form['gender']
        phone_number = request.form['phone_number']

        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Visitor (First_name, Last_name, Customer_ID_fk, Date_of_visit, Gender, Phone_number) VALUES (%s, %s, %s, %s, %s, %s)",
                           (first_name, last_name, customer_id_fk, date_of_visit, gender, phone_number))
            conn.commit()
            conn.close()
            return redirect('/visitor')
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_visitor.html') 

@app.route('/visitor/edit/<string:first_name>/<string:last_name>/<int:customer_id_fk>/<string:date_of_visit>', methods=['GET', 'POST'])
def edit_visitor(first_name, last_name, customer_id_fk, date_of_visit):
    conn = connect_to_database()
    cursor = conn.cursor()
    if request.method == 'POST':
        new_date_of_visit = request.form['date_of_visit']
        new_phone_number = request.form['phone_number']

        cursor.execute("UPDATE Visitor SET Date_of_visit = %s, Phone_number = %s WHERE First_name = %s AND Last_name = %s AND Customer_ID_fk = %s AND Date_of_visit = %s",
                       (new_date_of_visit, new_phone_number, first_name, last_name, customer_id_fk, date_of_visit))
        conn.commit()
        conn.close()
        return redirect('/visitor')
    else:
        cursor.execute("SELECT * FROM Visitor WHERE First_name = %s AND Last_name = %s AND Customer_ID_fk = %s AND Date_of_visit = %s",
                       (first_name, last_name, customer_id_fk, date_of_visit))
        visitor_data = cursor.fetchone()
        conn.close()
        return render_template('edit_visitor.html', visitor=visitor_data)  # Pass visitor_data to populate the edit form

@app.route('/visitor/delete/<string:first_name>/<string:last_name>/<int:customer_id_fk>/<string:date_of_visit>', methods=['POST'])
def delete_visitor(first_name, last_name, customer_id_fk, date_of_visit):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Visitor WHERE First_name = %s AND Last_name = %s AND Customer_ID_fk = %s AND Date_of_visit = %s",
                   (first_name, last_name, customer_id_fk, date_of_visit))
    conn.commit()
    conn.close()
    return redirect('/visitor')
@app.route('/service')
def display_service():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_service(conn)
        conn.close()
        return render_template('service.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_service(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Service')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/service/add', methods=['GET', 'POST'])
def add_service():
    if request.method == 'POST':
        service_id = request.form['service_id']
        price = request.form['price']
        service_type = request.form['service_type']
        location = request.form['location']
        start_timestamp = request.form['start_timestamp']
        end_timestamp = request.form['end_timestamp']

        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Service (ID, Price, Type, Location, Start_timestamp, End_timestamp) VALUES (%s, %s, %s, %s, %s, %s)",
                           (service_id, price, service_type, location, start_timestamp, end_timestamp))
            conn.commit()
            conn.close()
            return redirect('/service')
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_service.html')

@app.route('/service/edit/<int:service_id>', methods=['GET', 'POST'])
def edit_service(service_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("UPDATE Service SET Price = %s, Type = %s, Location = %s, Start_timestamp = %s, End_timestamp = %s WHERE ID = %s",
                       (request.form['price'], request.form['service_type'], request.form['location'], request.form['start_timestamp'], request.form['end_timestamp'], service_id))
        conn.commit()
        conn.close()
        return redirect('/service')
    else:
        cursor.execute("SELECT * FROM Service WHERE ID = %s", (service_id,))
        service_data = cursor.fetchone()
        conn.close()
        return render_template('edit_service.html', service=service_data)

@app.route('/service/delete/<int:service_id>', methods=['POST'])
def delete_service(service_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Service WHERE ID = %s", (service_id,))
    conn.commit()
    conn.close()
    return redirect('/service')
@app.route('/staff')
def display_staff():
    conn = connect_to_database()
    if conn is not None:
        data = fetch_staff(conn)
        conn.close()
        return render_template('staff.html', data=data)  # Passing 'data' to the template
    else:
        return "Error connecting to the database."

def fetch_staff(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM public.staff')
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/staff/add', methods=['GET', 'POST'])
def add_staff():
    conn = connect_to_database()
    departments = fetch_department(conn)
    if request.method == 'POST':
        staff_id = request.form['staff_id']
        salary = request.form['salary']
        gender = request.form['gender']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birth_date = request.form['birth_date']
        address = request.form['address']
        id_document = request.form['id_document']
        department_fk = request.form['department_fk']

        conn = connect_to_database()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO public.staff (StaffID, Salary, Gender, Fname, Lname, Birth_date, Address, IDdocument, Department_fk) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (staff_id, salary, gender, first_name, last_name, birth_date, address, id_document, department_fk))
            conn.commit()
            conn.close()
            return redirect('/staff')
        else:
            return "Error connecting to the database."
    else:
        return render_template('add_staff.html', departments=departments) 

@app.route('/staff/edit/<int:staff_id>', methods=['GET', 'POST'])
def edit_staff(staff_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("UPDATE public.staff SET Salary = %s, Gender = %s, Fname = %s, Lname = %s, Birth_date = %s, Address = %s, IDdocument = %s, Department_fk = %s WHERE StaffID = %s",
                       (request.form['salary'], request.form['gender'], request.form['first_name'], request.form['last_name'], request.form['birth_date'], request.form['address'], request.form['id_document'], request.form['department_fk'], staff_id))
        conn.commit()
        conn.close()
        return redirect('/staff')
    else:
        cursor.execute("SELECT * FROM public.staff WHERE StaffID = %s", (staff_id,))
        staff_data = cursor.fetchone()
        conn.close()
        return render_template('edit_staff.html', staff=staff_data)  # Pass staff_data to populate the edit form

@app.route('/staff/delete/<int:staff_id>', methods=['POST'])
def delete_staff(staff_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM public.staff WHERE StaffID = %s", (staff_id,))
    conn.commit()
    conn.close()
    return redirect('/staff')
@app.route('/Murder')
def Murder():
    # Connect to your database (replace 'your_database.db' with your actual database)
    conn = connect_to_database()   
    cursor = conn.cursor()

    # Your SQL query
    query = """
    -- List of all males who were associated with the "Pool" service on a specific date
    WITH MaleCustomers AS (
      SELECT DISTINCT C.Customer_ID, C.First, C.Last
      FROM Customer AS C
      INNER JOIN Uses AS U ON C.Customer_ID = U.CustomerID_fk
      INNER JOIN Service AS S ON U.ServiceID_fk = S.ID
      WHERE S.Type = 'Pool/day' -- Replace 'Pool' with your specific service type
        AND DATE(U.Date) = '2023-11-10' -- Replace 'SpecificDate' with the date
        AND C.Gender = 'Male'
    ),
    MaleVisitors AS (
      SELECT DISTINCT V.First_name, V.Last_name, V.Gender
      FROM Visitor AS V
      INNER JOIN Customer AS C ON V.Customer_ID_fk = C.Customer_ID
      INNER JOIN Uses AS U ON C.Customer_ID = U.CustomerID_fk
      INNER JOIN Service AS S ON U.ServiceID_fk = S.ID
      WHERE S.Type = 'Pool/day' -- Replace 'Pool' with your specific service type
        AND DATE(U.Date) = '2023-11-10' -- Replace 'SpecificDate' with the date
        AND V.Gender = 'Male'
    ),
    MaleStaff AS (
      SELECT DISTINCT St.StaffID, St.Fname, St.Lname
      FROM Staff AS St
      INNER JOIN Provides AS P ON St.StaffID = P.StaffID_fk
      INNER JOIN Service AS S ON P.ServiceID_fk = S.ID
      INNER JOIN Shift AS Sh ON P.Shift_ID_fk = Sh.Shift_ID
      WHERE S.Type = 'Pool/day' -- Replace 'Pool' with your specific service type
        AND Sh.Day = 'Friday' -- Replace 'SpecificDay' with the day
        AND St.Gender = 'Male'
    )
    -- Combine the results into a single table
    SELECT 'Male Customers' AS "Category", Customer_ID AS "ID", First AS "First Name", Last AS "Last Name"
    FROM MaleCustomers
    UNION ALL
    SELECT 'Male Visitors' AS "Category", NULL, First_name, Last_name
    FROM MaleVisitors
    UNION ALL
    SELECT 'Male Staff' AS "Category", StaffID, Fname, Lname
    FROM MaleStaff;

    """

    # Execute the query
    cursor.execute(query)
    results = cursor.fetchall()

    # Close the connection
    conn.close()

    # Pass the results to the HTML template for rendering
    return render_template('index.html', results=results)
@app.route('/revenu')
def revenu():
    # Connect to your database
    conn = connect_to_database()
    cursor = conn.cursor()

    # Your SQL query
    query = """
    -- Calculate the total amount paid by each customer in 2023
    WITH CustomerRevenue AS (
      SELECT
        SUM(Amount_paid) AS TotalAmountPaid
      FROM pays
      WHERE EXTRACT(YEAR FROM Payment_date) = 2023
    )
    
    -- Calculate the total yearly salary for each employee
    , EmployeeSalary AS (
      SELECT
        Salary * 12 AS TotalSalary
      FROM Staff
    )
    
    -- Calculate the total yearly price for contractors
    , ContractorExpense AS (
      SELECT
        SUM(Amount) AS TotalContractorExpense
      FROM Contractor
      WHERE Start_date <= '2023-12-31' AND End_date >= '2023-01-01'
    )
    -- Calculate the total yearly price for inventory
    , InventoryExpense AS (
      SELECT
        SUM(i.Price * s.Amount) AS TotalInventoryExpense
      FROM Inventory i
      JOIN Supplies s ON i.Inventory_ID = s.InventoryID_fk
      WHERE EXTRACT(YEAR FROM s.Date_supplied) = 2023
    )
    
    -- Calculate the overall revenue for 2023
    SELECT
      COALESCE(cr.TotalAmountPaid, 0) AS CustomerRevenue,
      COALESCE(SUM(es.TotalSalary), 0) AS TotalSalaryExpense,
      COALESCE(ce.TotalContractorExpense, 0) AS TotalContractorExpense,
      COALESCE(ie.TotalInventoryExpense, 0) AS TotalInventoryExpense,
      COALESCE(cr.TotalAmountPaid, 0) - COALESCE(SUM(es.TotalSalary), 0)
      - COALESCE(ce.TotalContractorExpense, 0) - COALESCE(ie.TotalInventoryExpense, 0) AS Revenue
    FROM CustomerRevenue cr
    CROSS JOIN EmployeeSalary es
    CROSS JOIN ContractorExpense ce
    CROSS JOIN InventoryExpense ie
    GROUP BY ce.TotalContractorExpense, cr.TotalAmountPaid, ie.TotalInventoryExpense;


    """

    # Execute the query
    cursor.execute(query)
    results = cursor.fetchall()

    # Close the connection
    conn.close()

    # Pass the results to the HTML template for rendering
    return render_template('revenu.html', results=results)

if __name__ == '__main__':
    app.run()
    print("The Flask app is running on:")
