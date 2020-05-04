# -*- coding:utf-8 -*-

import sys,os

if __name__ == "__main__":

    """
    for line in sys.stdin:
        line_list=line.strip('\n').split('\t')
        name=[ line_list[k] for k in range(len(line_list)) if k%2==1 ]
    """
    #name = input().strip("\r").split("\t")
    #score = input().strip("\r").split("\t")
    file = sys.argv[1]
    cnt = 0
    with open(file,encoding='UTF-8') as f:
    #with open(file) as f:
        for line in f:
            if cnt>=2:
                break
            if cnt == 0:
                name = line.strip("\n").strip("\r").split("\t")
            else:
                score = line.strip("\n").strip("\r").split("\t")
            cnt += 1


    for k in range(len(name)):
        if "总量" in name[k]:
            pos = k
            break

    #name = [ name[k].strip("总量") for k in range(len(name)) if k%2==1 ]  
    name = [ name[k].strip("总量") for k in range(pos,len(name)) ] 
    #score = [ int(score[k]) for k in range(len(score)) if k%2==1 ]
    score = [ int(score[k]) for k in range(pos,len(score)) ] 
    score_map = { name[k]:score[k] for k in range(len(name)) }
    #print( score_map )
    
    total = float(sum(score))
    pert = [ "{:.2f}".format(float(k)/total) for k in score ]
    pert_map = { name[k]:pert[k] for k in range(len(name)) }

    score_map = sorted(score_map.items(), key=lambda d:d[1], reverse = True)
    #print( score_map )

    for (k,_) in score_map:
        pert_map[k] = pert_map.pop(k)
    #print( pert_map )

    #print( "\t".join( [ name[k]+str(score[k]) for k in range(len(name)) ] ) )
    #print( "\t".join( [ name[k]+str(pert[k]) for k in range(len(name)) ] ) )

    print( "\t".join( [ k+str(v)  for (k,v) in score_map ] ) )
    print( "\t".join( [ k+v for (k,v) in pert_map.items() ] ) )



