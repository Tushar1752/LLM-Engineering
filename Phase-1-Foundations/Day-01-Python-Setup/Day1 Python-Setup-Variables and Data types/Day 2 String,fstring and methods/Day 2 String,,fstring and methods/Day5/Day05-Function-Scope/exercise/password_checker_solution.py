SYMBOLS =set("1334)(*&^%$#@@!&*(()))")

def check_password(pw,min_length=8):
    count=0
    if len(pw)>min_length:
        count+=1
    if any(ch.isdigit() for ch in pw):
        count+=1
    if any(ch.isupper() for ch in pw):
        count+=1
    if any(ch in SYMBOLS for ch in pw):
        count+=1

    if count>=4:
        return "Strong password"
    elif count>=2:
        return "medium"
    else:
        return "week"
    

pw=input("Enter the password:")
ss= check_password(pw)
print("The rule is pw.length >= 8 and The password you enter is:",ss)
st=check_password(pw,min_length=12)
print("The rule is that length of password should be >=12 And The password you entered is:",st)

