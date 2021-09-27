from basecong import db
#####################################
####################################
###################################

# Let's create our first model!
# We inherit from db.Model class



class B_Admin(db.Model):


    __tablename__ = 'B_Admin'
    __table_args__ = {'extend_existing': True}

    A_id = db.Column(db.Text,primary_key=True)

    A_pass=db.Column(db.Text)

    def __init__(self,A_id,A_pass):
        self.A_id=A_id
        self.A_pass=A_pass


    def __repr__(self):
        #
        return "succesful"


######################################################################################################################################
########################################################################################################################################






######################################################################################################################################
########################################################################################################################################






class B_Customer(db.Model):
    __tablename__ = 'B_Customer'
    __table_args__ = {'extend_existing': True}
    C_id = db.Column(db.Text,primary_key=True)
    C_firstname = db.Column(db.Text)
    C_lastname = db.Column(db.Text)
    C_gender = db.Column(db.Text)
    C_age = db.Column(db.Integer)
    C_email=db.Column(db.Text)
    C_address=db.Column(db.Text)
    C_number = db.Column(db.Integer)
    C_Intial_Month_charge=db.Column(db.Text)
    C_charge=db.Column(db.Text)
    C_join_date =db.Column(db.Text)
    C_join_time=db.Column(db.Text)
    C_Reason_for_joining=db.Column(db.Text)
    C_Intial_Month_charge_status=db.Column(db.Text)


    def __init__(self,C_id,firstname,lastname,gender,age,email,address,number,Intial_Month_charge,charge,join_date,join_time,Reason_for_joining,Intial_Month_charge_status):

        self.C_id = C_id
        self.C_firstname = firstname
        self.C_lastname = lastname
        self.C_gender = gender
        self.C_age = age
        self.C_email=email
        self.C_address=address
        self.C_number=number
        self.C_Intial_Month_charge=Intial_Month_charge
        self.C_charge=charge
        self.C_join_date=join_date
        self.C_join_time=join_time
        self.C_Reason_for_joining=Reason_for_joining
        self.C_Intial_Month_charge_status=Intial_Month_charge_status


    def __repr__(self):

        return f"customer fetched{self.C_id}"





######################################################################################################################################
########################################################################################################################################

class Charge_Details(db.Model):
    __tablename__ = 'Charge_Details'
    __table_args__ = {'extend_existing': True}
    Ch_id = db.Column(db.Text,primary_key=True)
    T_id_details = db.Column(db.Text)
    C_id = db.Column(db.Text)
    C_fullname=db.Column(db.Text)
    Year = db.Column(db.Text)
    Month = db.Column(db.Text)
    Amount_charged = db.Column(db.Integer)
    Amount_paid = db.Column(db.Integer)
    Amount_due =db.Column(db.Integer)
    Status =db.Column(db.Text)
    date=db.Column(db.Text)
    time=db.Column(db.Text)


    def __init__(self,Ch_id,T_id_details,C_id,C_fullname,Year,Month,Amount_charged,Amount_paid,Amount_due,Status,date,time):
        self.Ch_id = Ch_id
        self.T_id_details = T_id_details
        self.C_id = C_id
        self.C_fullname = C_fullname
        self.Year = Year
        self.Month = Month
        self.Amount_charged=Amount_charged
        self.Amount_paid=Amount_paid
        self.Amount_due=Amount_due
        self.Status=Status
        self.date=date
        self.time=time



    def __repr__(self):

        return f"customer fetched"



class Transaction_Details(db.Model):
    __tablename__ = 'Transaction_Details'
    __table_args__ = {'extend_existing': True}
    T_id = db.Column(db.Text,primary_key=True)
    C_id = db.Column(db.Text)
    T_type=db.Column(db.Text)
    T_fullname = db.Column(db.Text)
    T_phonenumber = db.Column(db.Text)
    T_accountnumber = db.Column(db.Integer)
    T_Amount_paid = db.Column(db.Integer)
    T_Amount_remaining = db.Column(db.Integer)
    T_Amount_used = db.Column(db.Integer)
    T_time =db.Column(db.Text)
    T_date=db.Column(db.Text)



    def __init__(self,T_id,C_id,T_type,T_fullname,T_phonenumber,T_accountnumber,Amount_paid,Amount_remaining,Amount_used,time,date):
        self.T_id = T_id
        self.C_id = C_id
        self.T_type = T_type
        self.T_fullname = T_fullname
        self.T_phonenumber = T_phonenumber
        self.T_accountnumber = T_accountnumber
        self.T_Amount_paid=Amount_paid
        self.T_Amount_remaining=Amount_remaining
        self.T_Amount_used=Amount_used
        self.T_time=time
        self.T_date=date




    def __repr__(self):

        return f"customer fetched"


class Inner_Transactions(db.Model):
    __tablename__ = 'Inner_Transactions'
    __table_args__ = {'extend_existing': True}
    Dummy_key=db.Column(db.Text,primary_key=True)
    IT_id = db.Column(db.Text)
    C_id = db.Column(db.Text)
    Ch_id = db.Column(db.Text)
    Year = db.Column(db.Text)
    Month = db.Column(db.Text)
    Charge_due=db.Column(db.Integer)
    Charge_due_after_payment=db.Column(db.Integer)
    T_id=db.Column(db.Text)
    T_Amount_remaining=db.Column(db.Integer)
    T_Amount_remaining_after_payment=db.Column(db.Integer)
    IT_time =db.Column(db.Text)
    IT_date=db.Column(db.Text)



    def __init__(self,Dummy_key,IT_id,C_id,Ch_id,Year,Month,Charge_due,Charge_due_after_payment,T_id,T_Amount_remaining,T_Amount_remaining_after_payment,IT_time,IT_date):
        self.Dummy_key = Dummy_key
        self.IT_id = IT_id
        self.C_id = C_id
        self.Ch_id = Ch_id
        self.Year = Year
        self.Month = Month
        self.Charge_due = Charge_due
        self.Charge_due_after_payment=Charge_due_after_payment
        self.T_id=T_id
        self.T_Amount_remaining=T_Amount_remaining
        self.T_Amount_remaining_after_payment=T_Amount_remaining_after_payment
        self.IT_time=IT_time
        self.IT_date=IT_date




    def __repr__(self):

        return f"customer fetched"


class Visitor_Details(db.Model):
    __tablename__ = 'Visitor_Details'
    __table_args__ = {'extend_existing': True}
    V_id = db.Column(db.Text,primary_key=True)
    C_id = db.Column(db.Text)
    V_firstname=db.Column(db.Text)
    V_lastname = db.Column(db.Text)
    V_phonenumber = db.Column(db.Text)
    V_droppeditems = db.Column(db.Text)
    V_address = db.Column(db.Text)
    V_Relationship_with_Patient=db.Column(db.Text)
    Comments = db.Column(db.Text)
    Entered_by = db.Column(db.Text)
    V_time =db.Column(db.Text)
    V_date=db.Column(db.Text)


    def __init__(self,V_id,C_id,V_firstname,V_lastname,V_phonenumber,V_droppeditems,V_address,V_Relationship_with_Patient,Comments,Entered_by,V_time,V_date):
        self.V_id = V_id
        self.C_id = C_id
        self.V_firstname = V_firstname
        self.V_lastname = V_lastname
        self.V_phonenumber = V_phonenumber
        self.V_droppeditems = V_droppeditems
        self.V_address = V_address
        self.V_Relationship_with_Patient = V_Relationship_with_Patient
        self.Comments=Comments
        self.Entered_by = Entered_by
        self.V_time = V_time
        self.V_date = V_date




    def __repr__(self):

        return f"customer fetched"



class Expenses(db.Model):
    __tablename__ = 'Expenses'
    __table_args__ = {'extend_existing': True}
    E_id = db.Column(db.Text,primary_key=True)
    E_fullname=db.Column(db.Text)
    E_moneyspent = db.Column(db.Integer)
    E_day = db.Column(db.Integer)
    E_month = db.Column(db.Integer)
    E_year = db.Column(db.Integer)
    E_Time= db.Column(db.Integer)
    E_reason = db.Column(db.Text)




    def __init__(self,E_id,E_fullname,E_moneyspent,E_day,E_month,E_year,E_Time,E_reason):
        self.E_id = E_id
        self.E_fullname = E_fullname
        self.E_moneyspent = E_moneyspent
        self.E_day = E_day
        self.E_month = E_month
        self.E_year=E_year
        self.E_Time = E_Time
        self.E_reason = E_reason






    def __repr__(self):

        return f"customer fetched"





db.create_all()
