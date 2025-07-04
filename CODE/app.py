from flask import Flask ,flash, render_template,request,session,redirect,url_for
import pymysql
import datetime
from datetime import date 

db=pymysql.connect(host="localhost",passwd="",user="root",port=3306,database="Hostel")
cursor=db.cursor()

app = Flask(__name__)
app.secret_key = 'abc'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form['un1']
        password=request.form['pd1']
        sql="select * from users where email=%s and password=%s and status=%s" 
        val =(username,password,'Accepted')
        cursor.execute(sql,val)
        a=cursor.fetchall()
        print(a)
        if a!=():
            session['un']=username
            return render_template("log.html",username=username,password=password)
        else:
            return render_template("userlogin.html",msg="Invalid Credentails")
    return render_template("userlogin.html")


@app.route('/register' , methods=['POST','GET'])
def register():
    return render_template("user registration.html")

@app.route("/payrent")
def payrent():
    print( session['un'])
    usermail =  session['un']
    sql = "select * from application where mail='%s'"%(usermail)
    cursor.execute(sql)
    data = cursor.fetchall()
    print("=============")
    print(data) 
    
    return render_template("payrent.html",data =data)

@app.route("/payamount/<int:id>")
def payamount(id = 0):
    print(id)
    sql = "select * from application where id='%s'"%(id)
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    
    sql = "select hostelname from application"
    cursor.execute(sql)
    data1 = cursor.fetchall()
    return render_template("payamount.html",data=data,data1=data1)

@app.route("/rentdetails")
def rentdetails():
    sql= " select * from payment"
    cursor.execute(sql)
    data = cursor.fetchall()
    return render_template("rentdetails.html",data=data)

@app.route("/rentpay",methods=["POST","GET"])
def rentpay():
    if request.method=="POST":
        uid =request.form['uid']
        un =request.form['un']
        mail =request.form['mail']
        mn =request.form['mn']
        ht =request.form['ht']
        hn =request.form['hn']
        amount =request.form['amount']
        cardnumber =request.form['cardnumber']
        cvv =request.form['cvv']
        todays_date = date.today() 
        sql = "insert into payment(uid,un,mail,mn,ht,hn,amount,cardnumber,cvv,todaysdate)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (uid,un,mail,mn,ht,hn,amount,cardnumber,cvv,todays_date)
        cursor.execute(sql,val)
        db.commit()
        flash('Payment Sent Successfully.....!')
        return redirect(url_for('payrent'))
        
        
    # return render_template("rentpay.html")
# @app.route('/log',methods=['POST','GET'])
# def log():
#     if request.method=='POST':
#         username=request.form['un1']
#         password=request.form['pd1']
#         sql="select * from users where email=%s and password=%s and status=%s" 
#         val =(username,password,'Accepted')
#         cursor.execute(sql,val)
#         a=cursor.fetchall()
#         if a!=[]:
#             session['un']=username
#             return render_template("log.html",username=username,password=password)
#         else:
#             return render_template ("userlogin.html",msg="submit1")
#     return render_template("log.html")


@app.route('/statusAccept/<id>',methods=['POST','GET'])
def statusAccept(id):
    print(id)
    if request.method=='POST':
        print(id)
        sql="update users set status='%s' where User_id='%d'" %('Accepted',int(id))
        cursor.execute(sql)
        db.commit()
        return redirect(url_for('reguser'))

@app.route('/statusReject/<id>',methods=['POST','GET'])
def statusReject(id):
    print(id)
    if request.method=='POST':
        print(id)
        sql="update users set status='%s' where User_id='%d'" %('Rejected',int(id))
        cursor.execute(sql)
        db.commit()

        return redirect(url_for('reguser'))

@app.route('/reg',methods=['POST','GET'])
def reg():
    if request.method=='POST':
        # user_id=request.form['uid']
        username=request.form['un']
        password=request.form['pwd']
        mail=request.form['mail']
        mobileno=request.form['mn']
        address=request.form['ad']
        status='pending'
        sql="insert into users(username,password,email,mobile,address,status) values ('%s','%s','%s','%s','%s','%s')" %(username,password,mail,mobileno,address,status)
        cursor.execute(sql)
        db.commit()
        session['mail']=mail
        print(session['mail'])
        return render_template("user registration.html",username=username,password=password,mail=mail,mobileno=mobileno,address=address,msg="registered")
    return render_template("userlogin.html")

@app.route('/reguser',methods=['POST','GET'])
def reguser():
    sql="select * from users"
    cursor.execute(sql)
    a=cursor.fetchall()
    print(a)
    return render_template("reguser.html",reguser=a)


@app.route('/logout',methods=['POST','GET'])
def logout():

    session['un']=None
    return redirect(url_for("home"))
  #  return render_template("logout.html")

@app.route('/adlogin')
def adlogin():
    return render_template("adlogin.html")

@app.route('/sign',methods=['POST','GET'])
def sign():
    return render_template("sign up.html")

# @app.route('/areg',methods=['POST','GET'])
# def areg():
#     if request.method=='POST':
#         aun=request.form['aun']
#         apd=request.form['apd']
#         acpd=request.form['acpd']
#         print(aun)
#         print(apd)
#         print(acpd)
#         sql = "insert into admin(adminname,password,confirmpassword) values ('%s','%s','%s')" % (aun,apd,acpd)
#         cursor.execute(sql)
#         db.commit()
#         return render_template("adlogin.html",aun=aun,apd=apd,acpd=acpd)

@app.route('/adpage',methods=['POST','GET'])
def adpage():
    if request.method=='POST':
        aun=request.form['aun']
        apd=request.form['apd']
        if aun=='admin@gmail.com' and apd == 'admin':
            return render_template("adpage.html",aun=aun,apd=apd)
        else:
            return render_template("adlogin.html",msg="msg1")
    return render_template("adlogin.html")


@app.route('/savepage',methods=['POST' ,'GET'])
def savepage():
    if request.method=='POST':
        hostel_id=request.form['hostelid']
        hostelname=request.form['hostelname']
        rooms=request.form['rooms']
        roomsharing=request.form['roomsharing']
        location=request.form['address']
        city=request.form['city']
        feeamount = request.form['feeamount']
        #fee = request.form['enterfee']
        contact=request.form['contact']
        a = int(rooms) * int(roomsharing)
        #c = int(roomsharing) * int(non_acrooms)
        b=str(a)
        #d=str(c)
        sql="insert into hosteldetails(hostel_id,Hostelname,rooms,Roomsharing,location,city,feeamount,roomvacancy,contact_no) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(hostel_id,hostelname,rooms,roomsharing,location,city,feeamount,b,contact)
        cursor.execute(sql)
        db.commit()
        return render_template("hdetails.html",hostel_id=hostel_id,hostelname=hostelname,rooms=rooms,roomsharing=roomsharing,location=location,city=city,feeamount=feeamount,contact=contact,msg="msg1")
    return render_template("adpage.html")


@app.route('/hostel')
def hostel():
    sql="select * from hosteldetails "
    cursor.execute(sql)
    a=cursor.fetchall()
    print(a)
    return render_template("hostel.html",result=a)

@app.route('/viewadmin',methods=['POST','GET'])
def viewadmin():
    sql = "select * from hosteldetails "
    cursor.execute(sql)
    a = cursor.fetchall()
    print(a)
    return render_template("viewadminhostel.html", result=a)


@app.route('/Hdetails',methods=['POST','GET'])
def Hdetails():
    return render_template("hdetails.html")

@app.route('/Appli',methods=['POST','GET'])
def Appli():
    return render_template("application.html")

@app.route('/fback',methods=['POST','GET'])
def fback():
    if 'un' in session:
        username=session['un']
        print("feedback:",username)
    return render_template("feedback.html",msg="msgap")

@app.route('/user',methods=['POST','GET'])
def application():
    usermail=""
    if 'un' in session:
        usermail = session['un']
        print('uername:',usermail)

    sql_1 = "select * from users where email='%s'" % (usermail)
    cursor.execute(sql_1)
    results = cursor.fetchall()
    

    if request.method=='POST':
        user_id=request.form['uid']
        username=request.form['un']
        mail=request.form['mail']
        mobileno=request.form['mn']
        hosteltype=request.form['ht']
        hostelname=request.form['hn']
        address=request.form['ad']
        
        import datetime
        x = datetime.datetime.now()
        print(x)
        sql="select * from application where User_id='%s' and hostelname='%s' and mail='%s'"%(user_id,hostelname ,mail)
        cursor.execute(sql)
        data = cursor.fetchall()
        print("===============")
        print(data)
        print("===============")
        if data==():
            sql="insert into application(User_id,Username,mail,mobile,hosteltype,hostelname,address,date_time) values ('%s','%s','%s','%s','%s','%s','%s','%s')" %(user_id,username,mail,mobileno,hosteltype,hostelname,address,x)
            cursor.execute(sql)
            db.commit()
            session['mail'] = mail
            session['hostelname']=hostelname
            sql_Q="select AC_roomvacancy,Non_AC_roomvacancy from hosteldetails where hostelname='%s'" %(hostelname)
            cursor.execute(sql_Q)
            a=cursor.fetchall()


            sql_QUy = "update hosteldetails set Non_AC_roomvacancy= Non_AC_roomvacancy - 1 where hostelname='%s' " %(hostelname)
            cursor.execute(sql_QUy)
            db.commit()

            sql_QU = "update hosteldetails set AC_roomvacancy= AC_roomvacancy - 1 where hostelname='%s' " % (hostelname)
            cursor.execute(sql_QU)
            db.commit()
        else:
            return render_template("application.html",results=results,msg="Already this application submitted for this Hostel....!")
        return render_template("application.html",user_id=user_id,username=username,mail=mail,mobileno=mobileno,hosteltype=hosteltype,hostelname=hostelname,msg="Application Submitted Successfully......!",results=results)
    return render_template("application.html",results=results)


@app.route('/vuser',methods=['POST','GET'])
def vuser():
        sql="select * from application "
        cursor.execute(sql)
        a=cursor.fetchall()
        print(a)
        return render_template("view.html",vuser=a)


@app.route('/view',methods=['POST','GET'])
def view():
    return render_template("viewusers.html")

@app.route('/vac',methods=['POST','GET'])
def vac():
    return render_template("vacate.html")

@app.route('/vacate',methods=['POST','GET'])
def vacate():
    if 'un' in session:
        usermail = session['un']
        print(usermail)
    # sql_1 = "select username,email from users where email='%s'" % (usermail)
    # cursor.execute(sql_1)
    # results = cursor.fetchall()
    # print(results)

    # if 'un' in session:
    #     usermail = session['un']
    #     print(usermail)
    sql_1 = "select username,mail,hostelname from application where mail='%s'" % (usermail)
    cursor.execute(sql_1)
    a = cursor.fetchall()
    print(a)

    if request.method=='POST':
        username=request.form['un']
        mail=request.form['mail']
        hostelname=request.form['hostelname']
        vacate=request.form['vacate']
        reason=request.form['reason']
        print(username,mail,hostelname,vacate,reason)

        
        x=datetime.datetime.now()
        print(x)

        sql="insert into vacate(Username,mail,hostelname,vacatestatus,reason,date_time) values('%s','%s','%s','%s','%s','%s')" %(username,mail,hostelname,vacate,reason,x)
        cursor.execute(sql)
        db.commit()
        session['hostelname']=hostelname
        print(session['hostelname'])

        if 'hostelname' in session:
            hostelname=session['hostelname']
            print(hostelname)

        sql_QUy = "update hosteldetails set Non_AC_roomvacancy= Non_AC_roomvacancy + 1 where hostelname='%s' " % (hostelname)
        cursor.execute(sql_QUy)
        db.commit()

        sql_QU = "update hosteldetails set AC_roomvacancy= AC_roomvacancy + 1 where hostelname='%s' " % (hostelname)
        cursor.execute(sql_QU)
        db.commit()
        return  render_template("vacate.html",username=username,mail=mail,vacate=vacate,reason=reason,msg="vacate",results=a)
    return render_template("vacate.html", results=a)

@app.route('/viewvacate',methods=['POST','GET'])
def viewvacte():
    sql="select * from vacate"
    cursor.execute(sql)
    a=cursor.fetchall()
    print(a)
    return render_template("viewvacate.html",viewvacte=a)

@app.route('/feedb',methods=['POST','GET'])
def feedb():
    if request.method=='POST':
        com=request.form['com']
        print(com)
        if 'mail' in session:
            appname=session['mail']
            print(appname)
        sql_q = "select mail from application where mail='%s'" %(appname)
        cursor.execute(sql_q)
        a = cursor.fetchall()
        print(a)

        sql="insert into feedback(feedback,mail) values ('%s','%s')" %(com,appname)
        cursor.execute(sql)
        db.commit()

        return render_template("feedback.html",com=com,msg="msg2")
    return render_template("feedback.html")

@app.route('/userfb',methods=['POST','GET'])
def userfb():
    sql = "select * from feedback"
    cursor.execute(sql)
    a = cursor.fetchall()
    print(a)
    return render_template("fb.html", userfb=a)


@app.route('/fees',methods=['POST','GET'])
def fees():
    return render_template("fees details.html")


if __name__ == '__main__':
    app.run(debug=True)
