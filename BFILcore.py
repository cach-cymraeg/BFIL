def sgn(x): return int(x>0) - int(x<0)

def intrp(inp,strt = 0):
    prg = inp.lower()
    prg = prg.split("\n")
    p = 0; state = "m"; func = {}
    mem_set = (-1,-1)
    outs = ""
    for c in prg:
        i = c.strip()
        ins = i.split(" ")[0] ; per = ""; out = ""
        
        if len(i.split(" "))>1 : per = i.split(" ")[1]
        if ins == "gt":
            out += ("<" if sgn(p-int(per)) == 1 else ">")*abs(p-int(per))
            p=int(per)
        if ins == "set" : out+= "[-]" + ("+"*int(per) if per != "max" else "-")
        if ins == "loop": out+= "["
        if ins == "end" : out+= "]"
        if ins == "inc" : out+= "+"
        if ins == "dec" : out+= "-"
        if ins == "add" : out+= "+"*int(per)
        if ins == "sub" : out+= "-"*int(per)
        if ins == "mvf" : out+= ">"*int(per) ; p += int(per)
        if ins == "mvb" : out+= "<"*int(per) ; p -= int(per)
        if ins == "trav": out+= "+[-<+]-" if per == "+" else "[<]"
        if ins == "prnt": out+= "[-]" + "+"*(ord(per) if per[0] != "{" else int(per[1:])) + "."
        if ins == "lprnt":
            hld = i.replace("lprnt ","")
            val = 0 ; tmp = ""
            for i in hld:
                am = ord(i) - val ; sign = sgn(am) ; val = ord(i)
                am = abs(am)
                tmp += ("-" if sign < 0 else "+" if sign > 0 else "")*am + "."
            out += tmp
        if ins == "stm" :
            na = mem_set[1] + int(per) ; wa = mem_set[0]
     
            out += intrp(f"loop\ndec\ngt {wa}\ninc\ngt {na}\n inc\ngt {p}\nend",p) + intrp( f"gt {wa} \n loop \n dec \n gt {p} \n inc \n gt {wa} \n end \n gt {p}",p)
        if ins == "ldm" :
            na = mem_set[1] + int(per) ; wa = mem_set[0]
            out += intrp(f"gt {na} \n loop\ndec\ngt {wa}\ninc\ngt {p}\ninc\ngt {na}\nend\ngt {wa}\nloop\ndec\ngt {na}\ninc\ngt {wa}\nend\ngt {p}",p)
        if ins == "mem": mem_set = eval(per) ; print(mem_set)
        if ins == "in" : out += ','
        if ins == "out": out += '.'
        if ins == "move":
            a = int(per)
            out += intrp(f"loop\ndec\ngt {a}\ninc\ngt {p}\nend",p)
        if ins == "rmove":
            a = int(per)
            out += intrp(f"loop\ndec\nmvf {a}\ninc\nmvb {p}\nend",p)
        if state == "m" : outs += out
        else: func[m] += out
    return outs

