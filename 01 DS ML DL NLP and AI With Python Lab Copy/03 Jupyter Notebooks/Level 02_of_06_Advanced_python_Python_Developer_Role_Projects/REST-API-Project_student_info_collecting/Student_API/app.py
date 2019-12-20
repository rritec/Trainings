from flask import Flask, jsonify, request, render_template, redirect
import pymongo
from datetime import datetime
app = Flask(__name__)

myclient = pymongo.MongoClient(u"mongodb://localhost:27017")
mydb = myclient["rritec_20191109"]
coll_name = 'students'
mycol = mydb[coll_name]

# added as part of UI
@app.route('/')
def hello_world():
    
    return render_template('index.html')

@app.route('/Framework', methods=['POST'])

def Loadpage():
     if request.method == 'POST':
        if request.form['submit_button'] == 'registration':
            return render_template('Student_Registration.html')
        else:
            return render_template('Enquiry_Form.html') 

   
        
    
            
# Insert one document into mongo collection


@app.route('/Registration', methods=['POST'])
def add_framework():

    name = request.form['q3_Name']
    email = request.form['q12_email']
    mobile = request.form['q13_phoneNumber[full]']
    gender = request.form['q11_gender']
    courses = request.form['q14_courses']
    comments = request.form['q10_comments']

    mycol.insert({'Name': name,
                  'Email': email,
                  'Mobile': mobile,
                  'Gender': gender,
                  'Courses': courses,
                  'Comments': comments,
                  'Enrolled_Date': datetime.today().strftime('%Y-%m-%d')
                  })

    return render_template('Thanks_Form.html')

# Get All documents from mongo collection
@app.route('/Student_Info', methods=['GET'])
def get_Student_Data():
    output = []

    for q in mycol.find():
        output.append({'Name': q['Name'], 'Email': q['Email'], 'Mobile': q['Mobile'], 'Gender': q['Gender'],
                       'Courses': q['Courses'], 'Comments': q['Comments']})
    
        print(output)
        
    return render_template("Enquiry_Form.html", value=output)
    #return render_template("sample.html", value=output)
 
    #return jsonify({'data': output})


# Get one documents from mongo collection by filtering on name
""" @app.route('/Student_Info/<Enrolled_Date>', methods=['GET'])
def get_one_frameworks(Enrolled_Date):
    output = []
    Enrolled_Date=request.form['lite_mode_17']

    q = mycol.find_one({'Enrolled_Date' : Enrolled_Date})
    print(q)

    if q:
        output = {'Name' : q['Name'],'Email' : q['Email'], 'Mobile' : q['Mobile'],'Gender' : q['Gender'], 'Courses' : q['Courses'],'Comments' : q['Comments']}
    else:
        output = 'No results found'

    return jsonify({'result' : output}) """

if __name__ == '__main__':
    app.run(debug=True)
