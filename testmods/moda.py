from . import modsvar
print ("module a is importing 'modsvar' (id:%d)" % id(modsvar))
modsvar.var = "moda"