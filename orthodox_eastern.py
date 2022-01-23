from datetime import *


def getPasxa(year):
        year=int(year)
        if year%4==0 and (year%100 != 0 or year%400==0):
            plus_days=timedelta(days=1)
            a=year%19
            b=year%4
            c=year%7

            delta=((a*19)+15)%30
            epsilon=(((2*b)+(4*c)+(6*delta)+6))%7

            final=delta+epsilon+4
            if final>30:
                final=final-30

                teliko=date(year,5,final)
                orthodox_eastern=teliko+timedelta(days=1)
            else:
                teliko=date(year,4,final)
                orthodox_eastern=teliko+timedelta(days=1)
            return orthodox_eastern
        else:
            plus_days=timedelta(days=1)
            a=year%19
            b=year%4
            c=year%7

            delta=((a*19)+15)%30
            epsilon=(((2*b)+(4*c)+(6*delta)+6))%7

            final=delta+epsilon+4
            if final>30:
                final=final-30

                orthodox_eastern=date(year,5,final)
            else:
                orthodox_eastern=date(year,4,final)
            return orthodox_eastern

def get_monday(date):
    last_monday = date - timedelta(days=date.weekday())
    return last_monday

year=2022

pasxa=getPasxa(year)
print("orthodox eastern: ",pasxa.strftime("%d/%m/%Y"))
back_46_days=pasxa-timedelta(days=46)
cleansed_monday=get_monday(back_46_days)
print("cleansed_monday: ",cleansed_monday.strftime("%d/%m/%Y"))
pentikosti=pasxa+timedelta(days=49)
agio_pneyma=pasxa+timedelta(days=50)
print("pentikosti: ",pentikosti.strftime("%d/%m/%Y"))
print("agio pneyma: ",agio_pneyma.strftime("%d/%m/%Y"))
