


def normalize_str(in_str):
    norm_str=''
    for char_in in in_str:
        if (char_in.isalpha()):
            norm_str=norm_str+char_in
        elif (char_in==' '):
            norm_str = norm_str + char_in
    norm_str=norm_str.lower()
    return (norm_str)

def udalenie_korotkih (in_list):
    for slov in in_list:
        if len(slov)<4:
            in_list.remove(slov)
    return (in_list)

def netochnoe_sravnenie (str1,str2):
    kol_sovpd=0
    str1=normalize_str(str1)
    str2=normalize_str(str2)
    str1_split=str1.split(' ')
    str2_split=str2.split(' ')
    udalenie_korotkih(str1_split)
    udalenie_korotkih(str2_split)
    for slov in str1_split:
        kol_sovpd=kol_sovpd+str2_split.count(slov)

    if ((kol_sovpd*100)/((len(str2_split)+len(str1_split))/2))>70:
        print('sovpadenii',(kol_sovpd*100)/((len(str2_split)+len(str1_split))/2) )






netochnoe_sravnenie('Трагедия в кизляре напомнила о судьбе всех русских Дагестана','Трагедия в кизляре напомнила j всех русских Дагестана')