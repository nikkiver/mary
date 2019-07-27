from flask import  render_template ,redirect ,json ,send_file , session ,url_for
from app.forms.userform import UserForm
from app.forms.loginform import LoginForm
from app.forms.teacherform import  TeacherForm
from app.forms.subjectform import  SubjectForm
from app.forms.collectionform import CollectionForm
from app.forms.DefaultersListForm import  DefaultersListForm
from app.forms.defaultersform import DefaultersForm
from app.models import  User
from app.models import  Teacher
from app.models import Subject
from app.models import Collectionrecord
from app.models import  Defaulter

from .middleware import loginrequired
import pandas as pd
from app import  app , db

@app.route("/" , methods =['GET'])
def index():
    return redirect('/registeruser')


@app.route('/registeruser' , methods=['GET','POST'])
def registerUser():
    userForm = UserForm()

    if userForm.validate_on_submit():
        usr = User(username=userForm.username.data , password = userForm.password.data)
        db.session.add(usr)
        db.session.commit();
        return "Registration successful " , 200

    return  render_template('newuser.html' , form =userForm )


@app.route('/login' , methods=['GET' ,'POST'])
def login():
    logf = LoginForm()

    if logf.validate_on_submit():
        usr = User.query.filter_by(username = logf.username.data ,password = logf.password.data).limit(1).all()
        session['username']=usr[0].username
        return render_template('dashboard.html' , username=usr[0].username)
    return render_template('login.html' , form=logf)

@app.route('/logout')
def logout():
    session.pop('username' , None)
    return  redirect(url_for('login'))


@app.route("/teachers" , methods=['GET' , 'POST'])
def registerTeacher():
    teacher =TeacherForm()

    if teacher.validate_on_submit():
        teach =Teacher(name=teacher.name.data , initials = teacher.initials.data , dob=teacher.dob.data)
        db.session.add(teach)
        db.session.commit()
        tchrs = Teacher.query.all()
        return  render_template("teacherslist.html" , teachers= tchrs)


    return render_template("newteacher.html" , form=teacher)


@app.route('/subjects' ,methods=['GET', 'POST'])
@loginrequired
def addSubject():
    subjc = SubjectForm()
    if subjc.validate_on_submit():
        sb=Subject(title=subjc.title.data)
        db.session.add(sb)
        db.session.commit()
        subjects = Subject.query.all()
        return render_template('subjectlist.html' , subjects=subjects , form=None)
    return render_template('subjectlist.html' , form=subjc)



@app.route('/subject/<int:id>' , methods =['GET' ,'DELETE'])
def removeSubject(id):
    sub = Subject.query.get(id)
    db.session.delete(sub)
    db.session.commit()
    subjs = Subject.query.all()
    return render_template('subjectlist.html' , subjects=subjs)

@app.route('/collections' , methods =['GET' ,'POST'])
def showCollectionForm():
    colform = CollectionForm()
    if colform.validate_on_submit():
        colrec= Collectionrecord(description=colform.description.data , collectiondate = colform.doc.data , standard=colform.standard.data , teacherinitials=colform.teacher.data)
        db.session.add(colrec)
        db.session.commit();
        cols =Collectionrecord.query.all()
        return render_template('collectionlist.html' , collections =cols)

    return  render_template('newcollection.html' , form =CollectionForm())

@app.route('/deleteCollection/<int:cid>' , methods=['GET'])
def deleteCollection(cid):
    col=Collectionrecord.query.get(cid)
    db.session.delete(col)
    db.session.commit()
    return render_template('collectionlist.html',collections=Collectionrecord.query.all())

@app.route('/collectionrecord' , methods=['GET'])
def  showCollectionRecords():
    colrec = Collectionrecord.query.all()
    return render_template('collectionlist.html' , collections=colrec)



@app.route('/defaulters/<int:id>' , methods = ['GET' ])
def selectDefaulters(id):
    colrec = Collectionrecord.query.get(id)
    defform = DefaultersListForm()
    #fetch list of student from collection record specified standard
    udf = pd.read_excel('G://PYTHTON-PROJECTS//NIV.xlsx', header=None)
    for x in udf.iterrows():
        ad = DefaultersForm()
        ad.name = x[1][2]
        ad.admno = x[1][1]
        defform.defaulters.append_entry(ad)
    return  render_template('defaultersform.html', form=defform , collection=colrec)

@app.route('/defaulters/<int:id>' , methods=['POST'])
def addDefaulters(id):
    colrec = Collectionrecord.query.get(id)
    defform = DefaultersListForm()
    for entry in defform.defaulters.entries:
        #print(entry.data['status'])
        if entry.data['status'] == 'NS':
            print(entry.data['status'])
            defl = Defaulter(admno=entry.data['admno'], name=entry.data['name'],status=entry.data['status'] , collection_id =id)
            #colrec.defaulters.append(defl)
            db.session.add(defl)
            db.session.commit()
    colrecs = Defaulter.query.filter_by(collection_id=id).all()
    print(colrecs)
    return  render_template('defaulterslist.html' , defaulters=colrecs ,collectionid=id)

@app.route('/showDefaulters/<int:cid>' ,methods=['GET'])
def showDefaulters(cid):
    if 'username' in session:
        defaulters = Defaulter.query.filter_by(collection_id=cid).all()
        return render_template('defaulterslist.html', defaulters=defaulters ,collectionid=cid)
    return  redirect(url_for('login'))






@app.route('/removedefaulter/<int:id>', methods=['GET'])
def removeDefaulter(id):
    print('Removing defaulter')
    defl = Defaulter.query.get(id)
    cid=defl.collection_id
    db.session.delete(defl)
    db.session.commit()
    colrecs = Defaulter.query.filter_by(collection_id=cid).all()
    return  render_template('defaulterslist.html' , defaulters=colrecs , collectionid=cid)


@app.route('/saveas/<int:cid>', methods=['GET'])
def export(cid):
    defaulters = Defaulter.query.filter_by(collection_id=cid).all()
    data = []
    for d in defaulters:
        data.append(('1',d.admno, d.name))
    df = pd.DataFrame()
    print(df)
    writer = pd.ExcelWriter('g://DEFL.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    worksheet.set_column('B:B', 7)
    worksheet.set_column('C:C', 20)
    header_format = workbook.add_format({
        'bold': 2,
        'text_wrap': True,
        'valign': 'top',
        'align': 'center',
        'fg_color': '#D7E4BC',
        'border': 2})

    merge_format = workbook.add_format({
        'bold': 2,
        'border': 2,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'yellow'})
    worksheet.merge_range('A1:C1', 'SPREADSHEET L-2', header_format)
    worksheet.merge_range('A2:C2', 'DEFAULTERS LIST', merge_format)
    worksheet.add_table('A3:C5', {'header_row': True, 'autofilter': False, 'columns': [
        {'header': 'Sno'},
        {'header': 'Admno'},
        {'header': 'Name'},

    ], 'data': data})
    print(str(len(data)))
    writer.save()
    return send_file('g://DEFL.xlsx', as_attachment=True)


