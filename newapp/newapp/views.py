from django.shortcuts import render_to_response
import pymysql.cursors


def book_list(request):
	db=pymysql.connect(user='root',db='mydb',passwd='admin',host='localhost')
	cursor=db.cursor()
	cursor.execute('SELECT name FROM books ORDER BY name')
	names = cursor.fetchone()
	db.close()
	return render_to_response('appfolder/book_list.html',{'names':names})
