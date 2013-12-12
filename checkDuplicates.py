import os, commands



t3_path = "srm://t3se01.psi.ch:8443/srm/managerv2\?SFN="
pnfpath = "/pnfs/psi.ch/cms/trivcat/store/user/decosa/tH/ntuplesV1/THminus_4FS_edmntuples/"
pnfpathBKU = "/pnfs/psi.ch/cms/trivcat/store/user/decosa/tH/ntuplesV1/THminus_4FS_removed/"
cmd_cp = "lcg-cp -b -D srmv2 "
cmd_del = "lcg-del -b -D srmv2 -l "

cmd_del += t3_path + pnfpath

cmd = "ls -lrth " + pnfpath
print cmd

status,ls_la = commands.getstatusoutput( cmd )
list_ = ls_la.split(os.linesep)
list_.remove(list_[0])

files = []
size = []
filesToRemove = []

for a in list_:
    b = a.split(" ")
    files.append(b[-1])
    size.append(b[4])

for c in files:
    check = []
    splitc = c.split("_")
    ntuple = "_".join(splitc[:4])
    ntuple += '_'
    #print ntuple
    check = [(h.startswith(ntuple) and h != c) for h in files]
    
    dupl_index = []
    size_short = []
    dupl_index = [files.index(h) for h in files if (h.startswith(ntuple) and h != c)]      
    if (len(dupl_index)>0):
        dupl_index.append(files.index(c))
        size_short = [size[i] for i in dupl_index]
        m = max(size_short)
        ind_m = size_short.index(m)
        dupl_index.remove(dupl_index[ind_m])
        toRemove = [files[i] for i in dupl_index ]
        filesToRemove+=toRemove
        [files.remove(i) for i in toRemove]
        

        
print filesToRemove
print len(filesToRemove)

for f in filesToRemove:
    cmd_rm = cmd_del + f
    print cmd_rm
    cmd_copy = cmd_cp + t3_path + pnfpath + f +" "+ t3_path + pnfpathBKU + f
    print cmd_copy
    os.system(cmd_copy)
    os.system(cmd_rm)





#        toCheck = [h for h in files if (h.startswith(ntuple) and h != c)]      
##         toCheck.append(c)                    
##         #print toCheck
##         num = [h.split("_")[3] for h in toCheck]
##         m = max(num)
##         #print num
##         srmlscmd = [ commands.getstatusoutput( "srmls " + t2_path + dirpath +  h )[1].split(" ")[2] for h in toCheck]
##         size = [s[0] for s in srmlscmd]
##         #print srmlscmd
##         #print toPickUp
##         #sizeFiles = [os.path.getsize("srmv2 " + t2_path + dirpath +  h) for h in toCheck] 
##         #print sizeFiles            
##         sizeMax = max(size)
##         toPickUp = toCheck[num.index(str(m))]
##         #toPickUp = toCheck[size.index(str(sizeMaxa))]
##         edmCleaned.append(toPickUp)
##         toCheck.remove(toPickUp)
##         print '================================='
##         #print toCheck
##         [files.remove(h) for h in toCheck]
##             #print edmCleaned
            
##      if (True not in check):
##             #print splitc[3]
##             edmCleaned.append(c)
##      if (True in check):
##             edmCopies.append(c)

## print '---------------------'
## #print len(edmCleaned)
## for e in edmCopies:
##     print e

#for e in edmCleaned:

  #  cmd_copy = cmd_cp + t2_path + dirpath + str(e) + " " + t2_path + dirpath + edmdir + str(e)

    #print cmd_copy

#print filesCleaned


