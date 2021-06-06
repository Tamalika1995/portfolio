from flask import Flask, render_template,request,redirect
import  csv
app = Flask(__name__)

@app.route("/")
def My_home():
   return render_template('index.html')
@app.route('/<string:page_name>')
def html_page(page_name):
   return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def login():
   if request.method=='POST':
      try:
         data=request.form.to_dict()
         write_to_csv(data)
         return redirect('/thankyou.html')
      except:
         return 'did to saved to database'
   else:
      return 'something went wrong'
def append_to_database(data):
   with open('database.txt',mode='a') as database:
      email=data['email']
      subject=data['subject']
      msg=data['msg']
      file=database.write(f'\n{email},{subject},{msg}')

def write_to_csv(data):
   with open('database.csv',newline='',mode='a') as database1:
      email=data['email']
      subject=data['subject']
      msg=data['msg']
      csv_writer=csv.writer(database1,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
      csv_writer.writerow([email,subject,msg])

