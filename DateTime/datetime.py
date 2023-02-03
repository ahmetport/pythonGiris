from _datetime import datetime
import _locale
_locale.setlocale(_locale.LC_ALL,"")


print(datetime.now()) #2022-12-08 14:27:40.935958
şu_an = datetime.now()
print(datetime.strftime(şu_an,"%Y" "%B" "%A"))  #2022AralıkPerşembe

şu_an = datetime.fromtimestamp(0)
print(şu_an) # 1970-01-01 03:00:00 bilgisayar aleminde zamanın başlaması