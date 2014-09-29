import os
import sys
import pickle
import binascii

#
# 2014-09-28 - By Dirk van den Bekerom
# FOM Institute DIFFER - www.differ.nl
# v1.1
#

def runPlotScript(buf,plotpath):
  libname = '_mplib'
  while (buf.find(libname) + 1):
    libname = '_' + libname
  exec('import matplotlib as ' + libname + '\n' + \
       libname + '.use("' + fext + '")\n' + buf + '\n' + \
       libname + '.pyplot.savefig("' + plotpath + '")')
  
filedir = sys.argv[2]
plotdir = sys.argv[3]

if not os.path.exists(plotdir):
  os.makedirs(plotdir)

print('\nPytexplot: ' + str(sys.argv[1]))
print('Pytexplot: output = '+plotdir)

fext = 'pdf'

filepath = filedir + '\\' + sys.argv[1] + '.py'
plotpath = plotdir + '\\' + sys.argv[1] + '.' + fext

try:
  fr = open('pydump','rb')
  crc_dict = pickle.load(fr)
  fr.close()
except:
  crc_dict = {}

fpy = open(filepath,'r')
buf = fpy.read()
fpy.close()

crc = binascii.crc32(buf.encode())
print('Pytexplot: CRC32 = '+str(crc))

try:
  if crc_dict[filepath] != crc or not os.path.isfile(plotpath):
    raise Exception()
  else: print('Pytexplot: No changes!')
except:
  print('Pytexplot: Redrawing...')
  crc_dict[filepath] = crc

  fw = open('pydump','wb')
  pickle.dump(crc_dict,fw)
  fw.close()

  runPlotScript(buf,plotpath)

print('Pytexplot: Done!')
