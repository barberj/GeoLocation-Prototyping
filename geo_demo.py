# geo_demo.py

"""
Author Justin Barber
2011 June
git@github.com:barberj/GeoLocation-Prototyping.git

Playing around with geolocation, cherry py and google maps
"""

import os, logging
log = logging.getLogger(__name__)
current_dir = os.path.dirname(os.path.abspath(__file__))

import cherrypy

class GeoDemo:
    title = 'Geo Demo'

    def header(self):
        return '''
                <html>
                    <head>
                        <title>%s</title>
                        <script type="text/javascript" src="public/js/geo.js"></script>
                    </head>
                    <body>
                ''' % self.title

    def footer(self):
        return '''
                    </body>
                </html>
               ''' 

    @cherrypy.expose
    def index(self):
        return self.header() + \
                '''<h2>Geo Demo!</h2>
                <script language="javascript">
                    getGeoLocal();
                </script>''' + \
                self.footer()

if __name__ == '__main__':
    conf = os.path.join(current_dir,"geo.ini")

    log.debug("Current Working Directory %s" % current_dir)
    cherrypy.log("Current Working Directory %s" % current_dir)
    cherrypy.log("Using configuration file %s" % conf)

    cherrypy.quickstart(GeoDemo(),'/',config=conf)
