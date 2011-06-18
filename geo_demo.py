# geo_demo.py

"""
Author Justin Barber
2011 June

Playing around with geolocation, cherry py and google maps
"""

import os, logging
log = logging.getLogger(__name__)

import cherrypy

class GeoDemo:
    title = 'Geo Demo'

    def header(self):
        return '''
                <html>
                    <head>
                        <title>%s</title>
                        <script type="text/javascript" src="geo.js"></script>
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
    current_dir = os.path.dirname(os.path.abspath(__file__))
    log.debug("Current Working Directory %s" % current_dir)
    cherrypy.log("Current Working Directory %s" % current_dir)
    conf = { '/geo.js': {
        'tools.staticfile.on' : True, 
        'tools.staticfile.filename' : os.path.join(current_dir,'public/js/geo.js')
        }
    }
    cherrypy.quickstart(GeoDemo(),'/',config=conf)
