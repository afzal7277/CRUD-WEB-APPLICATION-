import os
from flask import Flask, render_template , request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
######Database Configuration######
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app)
Migrate(app,db)
#################################
#####Model Creation##############
class Hospital(db.Model):
    """docstring for ."""
    __tablenmae__="Hospital"
    id=db.Column(db.Integer,primary_key=True)
    pt_name=db.Column(db.Text)
    sex=db.Column(db.Text)
    age=db.Column(db.Integer)
    doc_name=db.Column(db.Text)
    par_name=db.Column(db.Text)
    ph_num=db.Column(db.Integer)
    def __init__(self,pt_name,sex,age, doc_name,par_name,ph_num):
        self.pt_name = pt_name
        self.sex = sex
        self.age = age
        self.doc_name=doc_name
        self.par_name = par_name
        self.ph_num=ph_num
    def __repr__(self):
        return "Hospital Name - {} , Doctor's Name - {} , Phone Number - {}".format(self.p_name,self.doc_name,self.ph_num)
################################

@app.route("/",methods=['GET','POST'])
def index():

    pt_name=request.form.get('name')
    sex=request.form.get('sex')
    age=request.form.get('age')
    doc_name=request.form.get('doc')
    par_name=request.form.get('parname')
    ph_num=request.form.get('ph')
    print(pt_name,sex,age)
    if pt_name==None  or sex==None or age==None or doc_name==None or par_name==None or ph_num==None:
        pass
    else:

        data=Hospital(pt_name=pt_name,sex=sex,age=age,doc_name=doc_name,par_name=par_name,ph_num=ph_num)
        db.session.add(data)
        db.session.commit()

    return render_template('index.html')

@app.route("/display")
def display():
    info=Hospital.query.all()

    return render_template('display.html',info=info)


#################################

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method=='POST':

        pt_name=request.form.get('name')
        sex=request.form.get('sex')
        age=request.form.get('age')
        doc_name=request.form.get('doc')
        par_name=request.form.get('parname')
        ph_num=request.form.get('ph')

        data = Hospital.query.filter_by(id=id).first()
        data.pt_name = pt_name
        data.sex=sex
        data.age=age
        data.doc_name=doc_name
        data.par_name=par_name
        data.ph_num=ph_num
        db.session.add(data)
        db.session.commit()
        return redirect("/display")

    info = Hospital.query.filter_by(id=id).first()
    return render_template('update.html', info=info)


################################


@app.route('/delete/<int:id>')
def delete(id):
    data = Hospital.query.filter_by(id=id).first()

    db.session.delete(data)
    db.session.commit()
    return redirect("/display")








if __name__=='__main__':
    app.run(debug=True)
