print("Задача 2")

import re

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm' \
         'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV' \
         'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA' \
         'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV' \
         'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW' \
         'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC' \
         'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR' \
         'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm' \
         'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn' \
         'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS' \
         'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf' \
         'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH' \
         'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN' \
         'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ' \
         'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# 1. Решение с помощью re
line_2_a = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2)
print('С модулем re: \n', line_2_a)

# 2. Решение без re
designation_1 = list(map(lambda x: chr(x), list(range(65, 91))))
designation_2 = list(map(lambda x: chr(x), list(range(97, 123))))
line_2_b = list(line_2)

lst = []
i = len(line_2_b) - 1
while i >= 0:
       if line_2_b[i] in designation_2:
              lst.append(line_2_b[i])
       elif line_2_b[i] in designation_1 and i <= len(line_2_b) - 3 and line_2_b[i + 1] in designation_1 and line_2_b[
              i + 2] in designation_1:
              lst.append(line_2_b[i])
       else:
              lst.append(' ')
       i -= 1
lst.reverse()

i = 0
lst2 = []
registr = True
while i <= len(lst) - 1:
       if lst[i] in designation_2:
              registr = True
       if lst[i] in designation_1 and lst[i - 1] in designation_2 and lst[i - 2] in designation_2:
              lst2.append(lst[i])
              registr = False
       elif lst[i] in designation_1 and registr == False:
              lst2.append(lst[i])
       else:
              lst2.append(' ')
       i += 1
stroka = ''.join(lst2).split(' ')

line_str_3 = [i for i in stroka if i != '']
print('Без модуля re: \n', line_str_3)
