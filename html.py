
import json
from pprint import pprint as pp

row = '''<div class="alert alert-light" role="alert">
        <a href={link:}>{content:}</a></div>'''

fi = json.load(open('AllData.json','r'))

for html in fi:
    fil = open(list(html.keys())[0] + '.html', 'a+')
    fil.write('''<!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <style> 
            a{ margin: 0 12px;}
            a:hover{color: black;font-weight:bold;}
            </style></head><body>
                  <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <!-- <a class="navbar-brand" href="#">Navbar</a> -->
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
                <a class="nav-item nav-link active" href="News.html">News <span class="sr-only">(current)</span></a>
                <a class="nav-item nav-link"  id="a1" href="Get Ahead.html">Get Ahead</a>
                <a class="nav-item nav-link"  id="a1" href="Business.html">Business</a>
                <a class="nav-item nav-link"  id="a1" href="Cricket.html">Cricket</a>
                <a class="nav-item nav-link"  id="a1" href="Sports.html">Sports</a>
                <a class="nav-item nav-link"  id="a1" href="Movies.html">Get Ahead</a>
                <a class="nav-item nav-link"  id="a1" href="Slide Shows.html">Slide Shows</a>
                <a class="nav-item nav-link"  id="a1" href="Columns.html">Columns</a>
                <a class="nav-item nav-link"  id="a1" href="Specials.html">Specials </a>
                <a class="nav-item nav-link"  id="a1" href="Interviews.html">Interviews</a>
            </div>
            </div>
        </nav>''')
    
    for key, value in html[list(html.keys())[0]].items():
        fil.write(row.format(link=value, content=key))

    fil.write('''<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
            integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
            crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
            integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
            crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
            integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
            crossorigin="anonymous"></script>
            </body>
            </html>''')

    fil.close()
