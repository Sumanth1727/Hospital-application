from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField,RadioField,SelectField,TextField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,Length
class createcustomer(FlaskForm):
    firstname=StringField('First Name',validators=[DataRequired()])
    lastname=StringField('Last Name',validators=[DataRequired()])
    gender=SelectField('Gender',choices=[('Male', 'Male'), ('Female', 'Female'),('Other', 'Other')],validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    phone=StringField('Phone Number',validators=[DataRequired()])
    age=StringField('Age',validators=[DataRequired()])
    address=TextAreaField('Address',validators=[DataRequired()])
    Intial_Month_charge=StringField('Intial Month charge',validators=[DataRequired()])
    charge=StringField('Amont Charged for Month ',validators=[DataRequired()])
    Reason_for_joining=StringField('Reason for joining ',validators=[DataRequired()])
    submit=SubmitField("create")

class Visitor_Details_form(FlaskForm):
    firstname=StringField('First Name',validators=[DataRequired()])
    lastname=StringField('Last Name')
    phone=StringField('Phone Number',validators=[DataRequired()])
    Droppeditems=TextAreaField('Dropped Items',validators=[DataRequired()])
    address=TextAreaField('Address',validators=[DataRequired()])
    Relationship_with_Patient=StringField('Relationship with Patient',validators=[DataRequired()])
    Comments=StringField('Comments ')
    Entered_by=StringField('Entered_by ',validators=[DataRequired()])
    submit=SubmitField("create")

class Expenses_form(FlaskForm):
    moneyspent=StringField('Money Spent',validators=[DataRequired()])
    fullname=StringField('Spent by (Name)',validators=[DataRequired()])
    reason=TextAreaField('Reason for Spending',validators=[DataRequired()])

    submit=SubmitField("create")



class searchform(FlaskForm):
    user=StringField('Enter first Name or last name or patient  id ',validators=[DataRequired()])
    submit=SubmitField("Search")

class EditEmployee(FlaskForm):
    firstname=StringField('First Name')
    lastname=StringField('Last Name')
    gender=SelectField('Gender',choices=[('Male', 'Male'), ('Female', 'Female'),('Other', 'Other')])
    phone=StringField('Phone Number')
    balance=StringField('Current Desposited Amount')
    age=StringField('Age')
    address=TextAreaField('Address')
    submit=SubmitField("Edit")

class GenrateChargesForm(FlaskForm):
    Month=SelectField('Month',choices=[('January', 'January'), ('February', 'February'),('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')],validators=[DataRequired()])
    Year=SelectField('Year',choices=[('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')],validators=[DataRequired()])
    submit=SubmitField("Generate")

class ExpenseReportForm(FlaskForm):
    Month=SelectField('Month',choices=[('All', 'All'),('January', 'January'), ('February', 'February'),('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')],validators=[DataRequired()])
    Year=SelectField('Year',choices=[('All', 'All'),('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')],validators=[DataRequired()])
    submit=SubmitField("Generate")

class TransactionForm(FlaskForm):
    Transaction_Type=SelectField('Transaction Type',choices=[('PhonePe', 'PhonePe'), ('GPay', 'GPay'), ('By Hand', 'By Hand'), ('paytm', 'paytm')],validators=[DataRequired()])
    Transaction_PhoneNumber=StringField('Phone Number',validators=[DataRequired()])
    Transaction_Name=StringField('Deposited By (Name)',validators=[DataRequired()])
    Transaction_Amount=StringField('Amount Paid',validators=[DataRequired()])
    Transaction_AcctNo=StringField('Account Number(Optional)')
    submit=SubmitField("Submit")

class EvaluationForm(FlaskForm):
    Approve=SubmitField("Approve")
    Decline=SubmitField("Decline")
class LoginForm(FlaskForm):

    user = StringField('UserName',validators=[DataRequired()])
    passl  = StringField("Password",validators=[DataRequired()])
    submit = SubmitField('Login ')
class PayAmountForm(FlaskForm):
    AmounttobePaid=StringField('Amount to be paid',validators=[DataRequired()])
    submit=SubmitField("Submit")
