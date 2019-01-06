from . import modsvar
print ("module b is importing 'modsvar' (id:%d)" % id(modsvar))
modsvar.var = "modb"