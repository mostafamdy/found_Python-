from root.app import app

if __name__=="__main__":
     app.debug=True
     app.run(host='192.168.1.2',)
    # from waitress import serve

    # serve(app,)