
from flask import Flask, render_template, session, redirect, url_for, session,flash,request
from wtforms.validators import DataRequired
from tables import db,B_Customer,B_Admin,Charge_Details,Transaction_Details,Visitor_Details,Expenses,Inner_Transactions
from datetime import datetime
from basecong import app,mail
from flask_mail import *
from forms import createcustomer,LoginForm,searchform,EditEmployee,GenrateChargesForm,TransactionForm,PayAmountForm,Visitor_Details_form,Expenses_form,ExpenseReportForm
# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html

##############################################
#############Login #########################3
#############################################
@app.route('/', methods=['GET', 'POST'])
def index():

    # Create instance of the form.
    form = LoginForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():


        # Grab the data from the breed on the form.
        m=form.user.data
        n=form.passl.data

        print(m)
        Admin1 = B_Admin.query.filter_by(A_id=form.user.data).first()

        if(Admin1.A_pass==form.passl.data):
        		return redirect(url_for("admin",id=m))
        else:
                return "username and pasword doesn't match"

        

    return render_template('index.html', form=form)


##############################################
#############Admin ##########################
#############################################

@app.route('/admin/<id>', methods=['GET', 'POST'])
def admin(id):

    return render_template('admin.html',id=id)

@app.route('/admin/<id>/CreateCustomer', methods=['GET', 'POST'])
def CreateCustomer(id):
    form=createcustomer()
    if form.validate_on_submit():
        try:
            cus = B_Customer.query.filter_by(C_id="P1").first()
            cuslast = B_Customer.query.all()[-1]
            cusid="P"+str(int(cuslast.C_id[1:])+1)
        except Exception as e:
            cusid="P1"
        now = datetime.now()
        join_date = now.strftime("%B %d %Y")
        join_time=  now.strftime("%H:%M ")
        cus1=B_Customer(C_id=cusid, firstname=form.firstname.data,lastname=form.lastname.data,gender=form.gender.data, age=form.age.data, email=form.email.data, address=form.address.data, number=form.phone.data,Intial_Month_charge=form.Intial_Month_charge.data ,charge=form.charge.data,join_date=join_date,join_time=join_time,Reason_for_joining=form.Reason_for_joining.data,Intial_Month_charge_status="due")
        db.session.add(cus1)
        db.session.commit()
        flash("Patient Record succesfully created -- Patient Id - "+cusid)
    else:
        err=form.errors
        for i in err:
            flash(i+"-"+str(err[i]))

    return render_template('CreateNewCustomer.html',id=id,form=form)

@app.route('/admin/<id>/EditCustomer',methods=['GET', 'POST'])
def EditCustomer(id):


    # Create instance of the form.
    form1 = searchform()

    # If the form is valid on submission (we'll talk about validation next)
    if form1.validate_on_submit():
        # Grab the data from the breed on the form.
        try:
            cust=B_Customer.query.filter_by(C_id=form1.user.data).first()
            return redirect(url_for("EditCustomerDetails",id=id,cid=cust.C_id))
        except Exception as e:
            try:
                cust=B_Customer.query.filter_by(C_firstname=form1.user.data).first()
                return redirect(url_for("EditCustomerDetails",id=id,cid=cust.C_id))
            except Exception as e:
                try:
                    cust=B_Customer.query.filter_by(C_lastname=form1.user.data).first()
                    return redirect(url_for("EditCustomerDetails",id=id,cid=cust.C_id))
                except Exception as e:
                    flash("No patient found with the given info")


    return render_template('EditCustomer.html',id=id,form1=form1)


@app.route('/admin/<id>/EditCustomerDeatils/<cid>',methods=['GET', 'POST'])
def EditCustomerDetails(id,cid):

    form=EditEmployee()
    custm=B_Customer.query.filter_by(C_id=cid).first()

    if form.validate_on_submit():

        custm=B_Customer.query.filter_by(C_id=cid).first()
        if(form.firstname.data):
            custm.C_firstname=form.firstname.data
        if(form.lastname.data):
            custm.C_lastname=form.lastname.data
        if(form.gender.data):
            custm.C_gender=form.gender.data
        if(form.age.data):
            custm.C_age=form.age.data
        if(form.address.data):
            custm.C_address=form.address.data
        if(form.phone.data):
            custm.C_number=form.phone.data
        db.session.add(custm)
        db.session.commit()
        flash("succesfully Edited")
    else:
        err=form.errors
        for i in err:
            flash(i+"-"+str(err[i]))


    return render_template('EditCustomerDetails.html',id=id, form=form,custm=custm)



@app.route('/admin/<id>/SearchCustomer',methods=['GET', 'POST'])
def SearchCustomer(id):

    cust= False
    # Create instance of the form.
    form = searchform()

    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():

        cust=B_Customer.query.filter_by(C_firstname=form.user.data).first()
        if not cust:
            cust=B_Customer.query.filter_by(C_id=form.user.data).first()
        if not cust:
            cust=B_Customer.query.filter_by(C_lastname=form.user.data).first()
        if not cust:

            flash("no Customer found")





    return render_template('SearchCustomor.html',id=id, form=form, cust=cust)


@app.route('/admin/<id>/GenrateCharges',methods=['GET', 'POST'])
def GenrateCharges(id):


    # Create instance of the form.
    form = GenrateChargesForm()

    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():

        custs=B_Customer.query.all()
        print("----------------")
        print(custs)
        print("----------------")
        now = datetime.now()
        a=1
        for cust in custs:
            date = now.strftime("%B %d %Y")
            time=  now.strftime("%H:%M ")
            RID="CRG"+ now.strftime("%Y%m%d")+now.strftime("%H%M")+str(a)
            fullname=cust.C_firstname+cust.C_lastname
            if cust.C_Intial_Month_charge_status=="due":
                charge=cust.C_Intial_Month_charge
                cust.C_Intial_Month_charge_status="done"
            else:
                charge=cust.C_charge

            chrg=Charge_Details(Ch_id=RID,T_id_details="",C_id=cust.C_id,C_fullname=fullname,Year=form.Year.data,Month=form.Month.data,Amount_charged=cust.C_charge,Amount_paid="0",Amount_due=charge,Status="due",date=date,time=time)
            db.session.add(chrg)
            db.session.commit()
            db.session.add(cust)
            db.session.commit()
            a=a+1
            flash(cust.C_id+"  Succesfully Done")

    return render_template('GenrateCharges.html',id=id, form=form)


@app.route('/admin/<id>/<cid>/Transaction',methods=['GET', 'POST'])
def Transaction(id,cid):


    # Create instance of the form.
    form = TransactionForm()
    cust=B_Customer.query.filter_by(C_id=cid).first()

    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():

        cust=B_Customer.query.filter_by(C_id=cid).first()
        print("----------------")
        print(cust)
        print("----------------")
        now = datetime.now()
        date = now.strftime("%B %d %Y")
        time=  now.strftime("%H:%M ")
        TID="T"+ now.strftime("%Y%m%d")+now.strftime("%H%M%S%f")
        Trans=Transaction_Details(T_id=TID,C_id=cid,T_type=form.Transaction_Type.data,T_fullname=form.Transaction_Name.data,T_phonenumber=form.Transaction_PhoneNumber.data,T_accountnumber=form.Transaction_AcctNo.data,Amount_paid=form.Transaction_Amount.data,Amount_remaining=form.Transaction_Amount.data,Amount_used="0",time=time,date=date)
        db.session.add(Trans)
        db.session.commit()
        flash("Succesfully Done")


    return render_template('TransactionDetails.html',id=id,cust=cust, form=form)


@app.route('/admin/<id>/ViewDuePayments',methods=['GET', 'POST'])
def ViewDuePayments(id):
    form = searchform()
    dues1= False

    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():

        cust=B_Customer.query.filter_by(C_firstname=form.user.data).first()

        if not cust:
            cust=B_Customer.query.filter_by(C_id=form.user.data).first()
        if not cust:
            cust=B_Customer.query.filter_by(C_lastname=form.user.data).first()
        if cust:
            dues1=Charge_Details.query.filter_by(C_id=cust.C_id , Status="due").all()
        if not cust:
            flash("no Customer found")


    Dues=Charge_Details.query.filter_by(Status="due").all()

    return render_template('ViewDuePayments.html',id=id,Dues=Dues,dues1=dues1,form=form)




@app.route('/admin/<id>/<Ch_id>/payPatientDues',methods=['GET', 'POST'])
def PayPatientDues(id,Ch_id):
    chrg=Charge_Details.query.filter_by(Ch_id=Ch_id).first()
    trans=Transaction_Details.query.filter_by(C_id=chrg.C_id).all()
    form=PayAmountForm()
    T_amount=0
    for tran in trans:
        T_amount=T_amount+tran.T_Amount_remaining
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        if(int(form.AmounttobePaid.data) >int(chrg.Amount_due)):
            flash("amount should be less or equal to due amount")
        elif(int(form.AmounttobePaid.data)> T_amount ):
                flash("you don't have sufficient balance ")
                flash("Amount paid should be less than your total balance i.e. "+str(T_amount))
        else:
            transaction(Ch_id,int(form.AmounttobePaid.data))


    return render_template('PayAmounttoPatient.html',id=id,chrg=chrg,trans=trans,form=form,T_amount=T_amount)












def transaction(Ch_id,k):
    chrg=Charge_Details.query.filter_by(Ch_id=Ch_id).first()
    trans=Transaction_Details.query.filter_by(C_id=chrg.C_id).all()

    for tran in trans:
        if tran.T_Amount_remaining>0:
            if tran.T_Amount_remaining >= k:
                T_remaining=tran.T_Amount_remaining-k
                T_used=tran.T_Amount_used+k

                A_due=chrg.Amount_due-k
                A_paid=chrg.Amount_paid+k
                now = datetime.now()
                date = now.strftime("%B %d %Y")
                time=  now.strftime("%H:%M ")
                ITID="IT"+ now.strftime("%Y%m%d")+now.strftime("%H%M%S%f")
                ITID1="IT"+ now.strftime("%Y%m%d")+now.strftime("%H%M%S")
                In=Inner_Transactions(Dummy_key=ITID,IT_id=ITID1,C_id=chrg.C_id,Ch_id=chrg.Ch_id,Year=chrg.Year,Month=chrg.Month,Charge_due=chrg.Amount_due,Charge_due_after_payment=A_due,T_id=tran.T_id,T_Amount_remaining=tran.T_Amount_remaining,T_Amount_remaining_after_payment=T_remaining,IT_time=time,IT_date=date)
                if(A_due==0):
                    chrg.Status="Paid"
                chrg.Amount_due=A_due
                chrg.Amount_paid=A_paid
                tran.T_Amount_remaining=T_remaining
                tran.T_Amount_used=T_used
                k=0
                db.session.add(tran)
                db.session.add(chrg)
                db.session.add(In)
                db.session.commit()
                break


            else:
                T_remaining=tran.T_Amount_remaining
                T_used=tran.T_Amount_used+T_remaining
                k=k-T_remaining
                A_due=chrg.Amount_due-T_remaining
                A_paid=chrg.Amount_paid+T_remaining
                if(A_due==0):
                    chrg.Status="Paid"
                now = datetime.now()
                date = now.strftime("%B %d %Y")
                time=  now.strftime("%H:%M ")
                ITID="IT"+ now.strftime("%Y%m%d")+now.strftime("%H%M%S%f")
                ITID1="IT"+ now.strftime("%Y%m%d")+now.strftime("%H%M%S")
                In=Inner_Transactions(Dummy_key=ITID,IT_id=ITID1,C_id=chrg.C_id,Ch_id=chrg.Ch_id,Year=chrg.Year,Month=chrg.Month,Charge_due=chrg.Amount_due,Charge_due_after_payment=A_due,T_id=tran.T_id,T_Amount_remaining=tran.T_Amount_remaining,T_Amount_remaining_after_payment=0,IT_time=time,IT_date=date)
                chrg.Amount_due=A_due
                chrg.Amount_paid=A_paid
                tran.T_Amount_remaining=0
                tran.T_Amount_used=T_used
                db.session.add(tran)
                db.session.add(chrg)
                db.session.add(In)
                db.session.commit()
        else:
            print("tran.T_Amount_remaining=0")


@app.route('/admin/<id>/<cid>/AddVisitorRecord', methods=['GET', 'POST'])
def New_Visitor_Log(id,cid):
    cust = B_Customer.query.filter_by(C_id=cid).first()
    form=Visitor_Details_form()
    if form.validate_on_submit():
        print("entered validate")
        try:
            v= Visitor_Details.query.filter_by(v_id="V1").first()
            vlast = Visitor_Details.query.all()[-1]
            vid="V"+str(int(vlast.v_id[1:])+1)
        except Exception as e:
            vid="V1"
        now = datetime.now()
        date = now.strftime("%B %d %Y")
        time=  now.strftime("%H:%M ")
        cus1=Visitor_Details(V_id=vid,C_id=cid,V_firstname=form.firstname.data , V_lastname=form.lastname.data , V_phonenumber=form.phone.data ,V_droppeditems=form.Droppeditems.data ,V_address=form.address.data ,V_Relationship_with_Patient=form.Relationship_with_Patient.data ,Comments=form.Comments.data ,Entered_by=form.Entered_by.data ,V_time=time,V_date=date)
        db.session.add(cus1)
        db.session.commit()
        flash("Visitor Record succesfully created -- Visitor Id - "+vid)
    else:
        err=form.errors
        for i in err:
            flash(i+"-"+str(err[i]))

    return render_template('CreateVisitorLog.html',id=id,form=form,cust=cust)


@app.route('/admin/<id>/addnewexpense', methods=['GET', 'POST'])
def New_Expense_log(id):
    form=Expenses_form()
    if form.validate_on_submit():
        print("entered validate")
        try:
            E= Expenses.query.filter_by(E_id="E1").first()
            elast = Expenses.query.all()[-1]
            eid="E"+str(int(elast.E_id[1:])+1)
        except Exception as e:
            eid="E1"
        now = datetime.now()
        day = now.strftime("%d")
        month=now.strftime("%B")
        year=now.strftime("%Y")
        time=  now.strftime("%H:%M ")
        cus1=Expenses(E_id=eid,E_fullname=form.fullname.data,E_moneyspent=form.moneyspent.data,E_day=day,E_month=month,E_year=year,E_Time=time,E_reason=form.reason.data)
        db.session.add(cus1)
        db.session.commit()
        flash("Expenses Record succesfully created -- Record Id - "+eid)
    else:
        err=form.errors
        for i in err:
            flash(i+"-"+str(err[i]))

    return render_template('NewExpenseReport.html',id=id,form=form)



@app.route('/admin/<id>/ViewAllExpensesLogs',methods=['GET', 'POST'])
def ViewAllExpensesReports(id):
    form = ExpenseReportForm()
    expense= False
    search=False

    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():

        if form.Month.data=="All" and form.Year.data=="All":
            expense=Expenses.query.all()
        if form.Month.data!="All" and form.Year.data=="All":
            expense=Expenses.query.filter_by(E_month=form.Month.data).all()
        if form.Month.data=="All" and form.Year.data!="All":
            expense=Expenses.query.filter_by(E_year=form.Year.data).all()
        if form.Month.data!="All" and form.Year.data!="All":
            expense=Expenses.query.filter_by(E_month=form.Month.data, E_year=form.Year.data).all()
        search=True
        print("--------------------------------------")
        print(expense)
        print("--------------------------------------")



    expenses=Expenses.query.filter_by().all()

    return render_template('ViewAllexpensereports.html',id=id,expenses=expenses,expense=expense,form=form,search=search)


@app.route('/admin/<id>/ViewAllInterPayments',methods=['GET', 'POST'])
def ViewAllInterPayments(id):
    form = searchform()
    tran= False
    search=False

    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        search=True

        cust=B_Customer.query.filter_by(C_firstname=form.user.data).first()

        if not cust:
            cust=B_Customer.query.filter_by(C_id=form.user.data).first()
        if not cust:
            cust=B_Customer.query.filter_by(C_lastname=form.user.data).first()
        if cust:
            tran=Inner_Transactions.query.filter_by(C_id=cust.C_id ).all()
        if not cust:
            flash("no Customer found")


    trans=Inner_Transactions.query.all()

    return render_template('ViewInnerTransactionDetails.html',id=id,trans=trans,tran=tran,form=form,search=search)

@app.route('/admin/<id>/ViewAllCustomers',methods=['GET', 'POST'])
def ViewAllCustomers(id):
    form = searchform()
    cust= False
    search=False

    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        search=True

        cust=B_Customer.query.filter_by(C_firstname=form.user.data).first()

        if not cust:
            cust=B_Customer.query.filter_by(C_id=form.user.data).first()
        if not cust:
            cust=B_Customer.query.filter_by(C_lastname=form.user.data).first()
        if not cust:
            flash("no Customer found")


    custs=B_Customer.query.all()

    return render_template('ViewAllCustomers.html',id=id,custs=custs,cust=cust,form=form,search=search)





if __name__ == '__main__':
    app.run(debug=True)
