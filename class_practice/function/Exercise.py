import re

regular_expression = "yes" if re.fullmatch(r'\d+[A-z][a-z]*[A-z][a-z]*', '`AratbAbate') else 'no'
print(regular_expression)
