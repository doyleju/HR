# sample input 100,000,000.000
# sample output
# 100
# 000
# 000
# 000

import re
regex_pattern = r"[.,]+"
print("\n".join(re.split(regex_pattern, input())))
