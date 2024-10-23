from flask import Flask,redirect, url_for, request, render_template

app=Flask(__name__)


@app.route('/')
def hellow():
    return render_template('login.html')

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name



# converts int accepts integer  float  for flpating point values  path accepts  slashes  used as  directory  seprater decorator
# varible rules with example
# variable rules with integer value
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID


# variable rules with float value
@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo




# url building

@app.route('/admin')
def hello_admin():
    return  "Hello Admin"


@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest


@app.route('/admin/<name>')
def hello_user(name):
    if name == 'admin':
        return  redirect(url_for('hello_admin'))
    else:
        return  redirect(url_for('hello_guest',guest= name))


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host, port, debug, options)