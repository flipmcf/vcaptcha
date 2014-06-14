#!/usr/bin/python
import cgi
import 

formData = cgi.FieldStorage()

tscript = formData.getValue('transcript')
tscript = formData.getValue('stime')
tscript = formData.getValue('dur')
tscript = formData.getValue('vid')

save(stime=stime, dur=dur, vid=vid, tscript=tscript)

def save(stime, dur, vid, tscript):
    savefile(stime, dur, vid, tscript)
    
def savefile(stime, dur, vid, tscript):
    with open("/var/www/html/vcaptcha/tscript.dat", mode="a+") as fh:
        fh.write()
        fh.write(','.join([stime, dur, vid, tscript]))
        fh.write('\n')
        
        

        
    
