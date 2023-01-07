To create a Django file, the command for windows is,

django admin.exe startproject PROJECTNAME

After creating project,
   __init__.py
   asgi.py
   settings.py
    .   
     . 
    ...manage.py 
   THESE ABOVE files are created automatically
    manage.py - management of website
    settings.py - it contains configuration of website
    urls.py - URL management
    wsgi.py/asgi.py - deployment server

### DEFAULT DATABASE IN DJANGO- sqlite3
    ''' django has pre-built sub applications 
        we can create tables using those sub applications by following command
        "python manage.py migrate"
    we need to be in project directory in order to create table
     "cd projectdirectory" 
    To run the app the commmand is
     "python manage.py runserver" 
    '''
