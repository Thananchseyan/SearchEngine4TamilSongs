from flask import Flask, render_template,request
from searchquery import basicSearch,basic_search_with_fields, search_advanced_query
app = Flask(__name__, template_folder='templates')
@app.route('/search',methods=['GET', 'POST'])

def helloWorld():

    if request.method =='POST':
        qery =request.form['searchTerm']
        fields = {}
        #Here I am going to map the request value with the values for the later function
        #I selected A.R.Rahman, Ilayaraja, Vidyasagar and Yuvan Shankar Raja
        Composer = {
            "arrahman": "ஏ. ஆர். ரஹ்மான்",
            "ilayaraja": "இளையராஜா",
            "vidyasagar": "வித்யாசாகர்",
            "yuvan": "யுவன் ஷங்கர் ராஜா"
        }
        #following is the sample collection of the lyricist
        Lyricist = {
            "vairamuthu": "வைரமுத்து",
            "vaali": "வாலி",
            "na.muthukumar": "நா முத்துக்குமார்",
            "damarai": "தாமரை",
            "yugaparathi": "யுகபாரதி"
        }
        #following collection is the name of the heros
        Star = {
            "vijay": "விஜய்",
            "maddy": "மாதவன்",
            "vikram": "விக்ரம்",
            "ajith": "அஜித்"
        }
        if request.form['Composer'] != 'none':
            fields["Composer"] = Composer[request.form['Composer']]
        if request.form['Lyricist'] != 'none':
            fields["Lyricist "] = Lyricist[request.form['Lyricist']]
        if request.form['Star'] != 'none':
            fields["Star"] = Star[request.form['Star']]

        fields["Year"] = {
            "gte": int(request.form['start_year']),
            "lte": int(request.form['end_year'])
        }
        response = basic_search_with_fields(fields)

        # check request.form dict have basic or advanced key
        print(request.form.get('basic'))
        if request.form['basic'] == 'Basic':
            response = basicSearch(qery)
            fields = qery
        elif request.form['basic'] == 'Advanced':
            response = search_advanced_query(qery)
            fields = qery
        else:
            response = basic_search_with_fields(fields)

        hits =response['hits']['hits']
        time =response['took']
        num_of_results = response['hits']['total']['value']

        return render_template('result.html', query=fields, hits=hits, num_results=num_of_results, time=time)
    if request.method =='GET':
        return render_template('result.html',init='True')
if __name__ =='__main__':
    app.debug =True
    app.run(port=5000)