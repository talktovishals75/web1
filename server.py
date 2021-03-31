from flask import Flask,render_template,url_for,request,redirect

import csv
app = Flask(__name__)

@app.route('/')
def file1():
    return render_template('index.html')
	
@app.route('/<string:page_name>')
def file2(page_name):
    return render_template(page_name)
	
	
	
	
# def write2db_txt(data1):
	# with open('db_txt.txt','a') as fh1:
		# fh1.write(f'{data1["email"]},{data1["subject"]},{data1["message"]}\n')
		
def write2db_csv(data2):
	with open('db_csv.csv','a',newline='') as fh2:
		csv_ob1=csv.writer(fh2)
		csv_ob1.writerow([data2["email"],data2["subject"],data2["message"]])
		
		
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method=='POST':
		#try:
		data=request.form.to_dict()
		print(data)
		#write2db_txt(data)
		write2db_csv(data)
		return redirect('/Thank_you.html')
		#except:
		#	return 'did not save to database'
	else:
		return 'something went wrong,try again'
	
	
