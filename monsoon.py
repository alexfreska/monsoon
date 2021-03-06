"""
    monsoon.py
    ~~~~~~~~~~~~~~~~~~

    Unlimited cloud storage

    :copyright: (c) 2013 Raymond Jacobson

"""
import cli.app, os
from lib.db import *
from lib.dbox import *
from lib.generator import *

def put(file):
  print "putting..."
  if (decideNewAccount(os.stat(file).st_size)):
    generateNewAccount()
  account = getNewestAccount()
  uploadFileToAccount(file, account['access_token'])

def grab(file):
  print "grabbing..."
  db_file = getUploadedFile(file)
  print "pub link: " + db_file['short_link']
  print "DL link: " + db_file['downloadable_link']

def config(app_key,app_secret):
  file = open('config.py','r+')
  file.write("config = {'app_key': '" + str(app_key) + "','app_secret': '" + str(app_secret) + "'}")
  print file.read()
  file.close()

@cli.app.CommandLineApp
def monsoon(app):
  if (app.params.action == 'put'):
    put(app.params.file)
  elif (app.params.action == 'grab'):
    grab(app.params.file)
  elif (app.params.action == 'config'):
    config(app.params.file,app.params.third)
  else:
    print "invalid arguments. -h for help."
    exit(1)

monsoon.add_param("action", help="either 'put' or 'grab' a file into the cloud", default=1)
monsoon.add_param("file", help="file to commit action on", default=2)
monsoon.add_param("-t", "--third", help="---", default=False, action="store_true")

if __name__ == "__main__":
    monsoon.run()
