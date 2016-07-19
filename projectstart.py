import re
import json
import requests
import sqlite3 
from BeautifulSoup import BeautifulSoup
from random import randint
from flask import Flask, render_template, request

app = Flask(__name__)

conn = sqlite3.connect('news.db')
print "Opened database successfully";

#conn.execute('CREATE TABLE students (name TEXT, comment TEXT, url TEXT)')
#conn.execute('CREATE TABLE students1 (name1 TEXT, comment1 TEXT, url1 TEXT)')
#$conn.execute('CREATE TABLE students2 (name2 TEXT, comment2 TEXT, url2 TEXT)')
#conn.execute('CREATE TABLE students3 (name3 TEXT, comment3 TEXT, url3 TEXT)')
#conn.execute('CREATE TABLE students4 (name4 TEXT, comment4 TEXT, url4 TEXT)')
#conn.execute('CREATE TABLE students5 (name5 TEXT, comment5 TEXT, url5 TEXT)')
#conn.execute('CREATE TABLE students6 (name6 TEXT, comment6 TEXT, url6 TEXT)')
#conn.execute('CREATE TABLE students7 (name7 TEXT, comment7 TEXT, url7 TEXT)')
#conn.execute('CREATE TABLE students8 (name8 TEXT, comment8 TEXT, url8 TEXT)')
#print "Table created successfully";



@app.route('/')
def student():
   return render_template('student.html')
#@app.route('/result')
#def result():
#   return render_template('result.html')
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   msg=""
   print request.method
   if request.method == 'POST':
      try:
         print "in dfgd try"
         print request.form['a']

         if request.form['a'] == "11":
            #conn.execute('CREATE TABLE students (name TEXT, comment TEXT, url TEXT)')
            nm = request.form['named']
            addr = request.form['data']
            city = request.form['link']
         #pin = request.form['pin']
            with sqlite3.connect("news.db") as con:
               print "in try"
               print nm,addr,city
               cur = con.cursor()
               cur.execute("INSERT INTO students (name,comment,url) VALUES (?,?,?)",(nm,addr,city) )
               print "entered"
               con.commit()
               msg = "Record successfully added"

      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         abcs=res()
         #print abcs, "......................."
         return abcs
         con.close()



@app.route('/addrec1',methods = ['POST', 'GET'])
def addrec1():
   msg=""
   print request.method
   if request.method == 'POST':
      try:
         print "111111111111111111111111111111111111111"
         print request.form['a1']
         if request.form['a1'] == "622":
            #conn.execute('CREATE TABLE students1 (name TEXT, comment TEXT, url TEXT)')
            nm = request.form['named1']
            addr = request.form['data1']
            city = request.form['link1']

            with sqlite3.connect("news.db") as con:
               print "in try"
               print nm,addr,city
               cur = con.cursor()
               cur.execute("INSERT INTO students1 (name1,comment1,url1) VALUES (?,?,?)",(nm,addr,city) )
               print "entered"
               con.commit()
               msg = "Record successfully added"

      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         abcs=res()
         #print abcs, "......................."
         return abcs
         con.close()


@app.route('/addrec2',methods = ['POST', 'GET'])
def addrec2():
   msg=""
   print request.method
   if request.method == 'POST':
      try:
         print "111111111111111111111111111111111111111"
         print request.form['a2']
         if request.form['a2'] == "3":
            #conn.execute('CREATE TABLE students1 (name TEXT, comment TEXT, url TEXT)')
            nm = request.form['named2']
            addr = request.form['data2']
            city = request.form['link2']

            with sqlite3.connect("news.db") as con:
               print "in try"
               print nm,addr,city
               cur = con.cursor()
               cur.execute("INSERT INTO students2 (name2,comment2,url2) VALUES (?,?,?)",(nm,addr,city) )
               print "entered"
               con.commit()
               msg = "Record successfully added"

      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         abcs=res()
         #print abcs, "......................."
         return abcs
         con.close()


@app.route('/addrec3',methods = ['POST', 'GET'])
def addrec3():
   msg=""
   print request.method
   if request.method == 'POST':
      try:
         print "111111111111111111111111111111111111111"
         print request.form['a3']
         if request.form['a3'] == "1":
            #conn.execute('CREATE TABLE students1 (name TEXT, comment TEXT, url TEXT)')
            nm = request.form['named3']
            addr = request.form['data3']
            city = request.form['link3']

            with sqlite3.connect("news.db") as con:
               print "in try"
               print nm,addr,city
               cur = con.cursor()
               cur.execute("INSERT INTO students3 (name3,comment3,url3) VALUES (?,?,?)",(nm,addr,city) )
               print "entered"
               con.commit()
               msg = "Record successfully added"

      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         abcs=res()
         #print abcs, "......................."
         return abcs
         con.close()


@app.route('/addrec4',methods = ['POST', 'GET'])
def addrec4():
   msg=""
   print request.method
   if request.method == 'POST':
      try:
         print "111111111111111111111111111111111111111"
         print request.form['a4']
         if request.form['a4'] == "21":
            #conn.execute('CREATE TABLE students1 (name TEXT, comment TEXT, url TEXT)')
            nm = request.form['named4']
            addr = request.form['data4']
            city = request.form['link4']

            with sqlite3.connect("news.db") as con:
               print "in try"
               print nm,addr,city
               cur = con.cursor()
               cur.execute("INSERT INTO students4 (name4,comment4,url4) VALUES (?,?,?)",(nm,addr,city) )
               print "entered"
               con.commit()
               msg = "Record successfully added"

      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         abcs=res()
         #print abcs, "......................."
         return abcs
         con.close()

@app.route('/addrec5',methods = ['POST', 'GET'])
def addrec5():
   msg=""
   print request.method
   if request.method == 'POST':
      try:
         print "111111111111111111111111111111111111111"
         print request.form['a5']
         if request.form['a5'] == "522":
            #conn.execute('CREATE TABLE students1 (name TEXT, comment TEXT, url TEXT)')
            nm = request.form['named5']
            addr = request.form['data5']
            city = request.form['link5']

            with sqlite3.connect("news.db") as con:
               print "in try"
               print nm,addr,city
               cur = con.cursor()
               cur.execute("INSERT INTO students5 (name5,comment5,url5) VALUES (?,?,?)",(nm,addr,city) )
               print "entered"
               con.commit()
               msg = "Record successfully added"

      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         abcs=res()
         #print abcs, "......................."
         return abcs
         con.close()

@app.route('/addrec6',methods = ['POST', 'GET'])
def addrec6():
   msg=""
   print request.method
   if request.method == 'POST':
      try:
         print "111111111111111111111111111111111111111"
         print request.form['a6']
         if request.form['a6'] == "2":
            #conn.execute('CREATE TABLE students1 (name TEXT, comment TEXT, url TEXT)')
            nm = request.form['named6']
            addr = request.form['data6']
            city = request.form['link6']

            with sqlite3.connect("news.db") as con:
               print "in try"
               print nm,addr,city
               cur = con.cursor()
               cur.execute("INSERT INTO students6 (name6,comment6,url6) VALUES (?,?,?)",(nm,addr,city) )
               print "entered"
               con.commit()
               msg = "Record successfully added"

      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         abcs=res()
         #print abcs, "......................."
         return abcs
         con.close()


@app.route('/addrec7',methods = ['POST', 'GET'])
def addrec7():
   msg=""
   print request.method
   if request.method == 'POST':
      try:
         print "111111111111111111111111111111111111111"
         print request.form['a7']
         if request.form['a7'] == "31":
            #conn.execute('CREATE TABLE students1 (name TEXT, comment TEXT, url TEXT)')
            nm = request.form['named7']
            addr = request.form['data7']
            city = request.form['link7']

            with sqlite3.connect("news.db") as con:
               print "in try"
               print nm,addr,city
               cur = con.cursor()
               cur.execute("INSERT INTO students7 (name7,comment7,url7) VALUES (?,?,?)",(nm,addr,city) )
               print "entered"
               con.commit()
               msg = "Record successfully added"

      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         abcs=res()
         #print abcs, "......................."
         return abcs
         con.close()


@app.route('/addrec8',methods = ['POST', 'GET'])
def addrec8():
   msg=""
   print request.method
   if request.method == 'POST':
      try:
         print "111111111111111111111111111111111111111"
         print request.form['a8']
         if request.form['a8'] == "422":
            #conn.execute('CREATE TABLE students1 (name TEXT, comment TEXT, url TEXT)')
            nm = request.form['named8']
            addr = request.form['data8']
            city = request.form['link8']

            with sqlite3.connect("news.db") as con:
               print "in try"
               print nm,addr,city
               cur = con.cursor()
               cur.execute("INSERT INTO students8 (name8,comment8,url8) VALUES (?,?,?)",(nm,addr,city) )
               print "entered"
               con.commit()
               msg = "Record successfully added"

      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         abcs=res()
         #print abcs, "......................."
         return abcs
         con.close()

@app.route('/list')
def list():
   con = sqlite3.connect("news.db")
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("select name,comment from students")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)


@app.route('/result1')
def result1():
   return render_template('result1.html')

@app.route('/result',methods = ['POST', 'GET'])
def res():
   val = ""
   sp = ""
   final = ''
   words = 0
   fun = {}
   d={}
   d1={}
   m ={}
   if request.method == 'POST':
      result = request.form
      sp=result['name']
      sp=sp.replace(' ','+')
      '''for value in result:
      	val = val+ result[value]
      	words = words + len(val.split())
      	w = val.split()
      	i =0
      	for word in w:
      		if i < (words-1):
      			i = i+1
      			sp = sp + word + '+'

      		else:
      			sp =  sp + word
      	
      	#print sp'''
      
      l = randint(1,4)
      #u = frm.getValue('search')#contains the word given in the search box
      #print u
      #u = str(sachin)
      #op = 'sachin'
      print " enterede in res ",sp
      for l in range(1,4):
         if l == 1:
            url = 'https://in.search.yahoo.com/search?p=' + sp
            response = requests.get(url)
            html = response.content
            soup = BeautifulSoup(html)
#print soup.find_all("a")
            all1 = soup.findAll("a", attrs={"class": "compTitle"})
            count = 0
            p  = soup.body.findAll("a",href=re.compile(r'http://'))

            
            for link in p:
               count = count + 1
               if count == 4 or count == 5 or count == 6 :
                  #print link.get("href")
                  if count == 4:
                     fun = {str(count)+"22" : link.get("href") }
                  else:
                     d1 =  {str(count)+"22" : link.get("href") }
                  d = fun.update(d1)
         m.update(fun)

         print m

         if l ==2:
            url =  'https://www.bing.com/search?q=' + sp
            response = requests.get(url)
            html = response.content
            soup = BeautifulSoup(html)
#print soup.find_all("a")
            all1 = soup.findAll("a", attrs={"class": "compTitle"})
            count = 0
            p  = soup.body.findAll("a",href=re.compile(r'http://'))
            count =0 
               
            for link in p:
               count = count+ 1
               #print link.get('href')
               if count == 1:
                  fun = {str(count)+"1" : link.get("href") } 
               elif count == 2 or count == 3 :
                  d1 = {str(count)+"1" : link.get("href") }
               d = fun.update(d1)
            
         m.update(fun)

         print m
         if l == 3:
            url = 'http://news.ask.com/web?q='+sp
            response = requests.get(url)
            html = response.content
            soup = BeautifulSoup(html)
#print soup.find_all("a")
            all1 = soup.findAll("a", attrs={"class": "compTitle"})
            count = 0
            p  = soup.body.findAll("a",href=re.compile(r'http://'))
            count = 0
            
            for link in p:
               count = count+ 1
               #print link.get('href')
               if count == 1:
                  fun = {str(count) : link.get("href") } 
               elif count == 2 or count == 3 :
                  d1 = {str(count) : link.get("href") }
               d = fun.update(d1)
            
         m.update(fun)   

         print m 
      
      for key, value in m.iteritems() :
         if key == "11":
            print "in key == 11"
            con = sqlite3.connect("news.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from students")
            rows1 = cur.fetchall();
            
      person=[sp]


      for key, value in m.iteritems() :
         if key == "622":
            print "in key == 622"
            con = sqlite3.connect("news.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from students1")
            rows = cur.fetchall();
            
      person=[sp] 

      for key, value in m.iteritems() :
         if key == "3":
            print "in key == 3"
            con = sqlite3.connect("news.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from students2")
            rows2 = cur.fetchall();
            
      person=[sp]

      for key, value in m.iteritems() :
         if key == "1":
            print "in key == 1"
            con = sqlite3.connect("news.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from students3")
            rows3 = cur.fetchall();
            
      person=[sp]

      for key, value in m.iteritems() :
         if key == "21":
            print "in key == 21"
            con = sqlite3.connect("news.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from students4")
            rows4 = cur.fetchall();
            
      person=[sp]

      for key, value in m.iteritems() :
         if key == "522":
            print "in key == 522"
            con = sqlite3.connect("news.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from students5")
            rows5 = cur.fetchall();
            
      person=[sp]

      for key, value in m.iteritems() :
         if key == "2":
            print "in key == 2"
            con = sqlite3.connect("news.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from students6")
            rows6 = cur.fetchall();
            
      person=[sp]

      for key, value in m.iteritems() :
         if key == "31":
            print "in key == 31"
            con = sqlite3.connect("news.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from students7")
            rows7 = cur.fetchall();
            
      person=[sp]

      for key, value in m.iteritems() :
         if key == "422":
            print "in key == 422"
            con = sqlite3.connect("news.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from students8")
            rows8 = cur.fetchall();
            
      person=[sp]

      
      return render_template("result.html",result = m,rows1 = rows1,rows=rows, rows2 =rows2, rows3=rows3, rows4=rows4, rows5=rows5, rows6=rows6, rows7=rows7, rows8=rows8, name=person)


@app.route('/result1',methods = ['POST', 'GET'])
def res1():
   if request.method == 'POST':
      result = request.form
   return render_template("result1.html",result = result) 
if __name__ == '__main__':
   app.run(debug = True)
