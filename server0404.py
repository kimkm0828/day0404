from flask import Flask,render_template,request
import myutil

app = Flask(__name__)

@app.route('/student.do',methods=['GET','POST'])
def hello_world():
    fname = ''
    msg = ''
    if request.method =='POST':
        name = request.form['name']
        fname = myutil.getStudentScore(name)
        if fname == 'no':
            msg = "해당학생은 존재하지 않습니다."

    return render_template('student.html',fname=fname,msg=msg)


@app.route('/subject.do',methods=['GET','POST'])
def subjectSco():
    fname =''
    msg = ''
    if request.method =='POST':
        name = request.form['name']
        fname = myutil.getSubjectScore(name)
        if fname == "no":
            msg = "그런 과목은 없습니다."

    return render_template('subject.html',fname=fname,msg=msg)


if __name__ == '__main__':
    app.run(host='203.236.209.96',debug=True)