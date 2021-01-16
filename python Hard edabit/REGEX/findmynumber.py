import re


txt ="Hello my Number is 123456789 and  my friends number is 987654321"
             
regex = '\d+'

match = re.findall(regex,txt)
print(match)

#['123456789', '987654321']