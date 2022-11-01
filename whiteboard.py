import re

text = "RT @test test2 https://regex101.com/ help #lol pls 😂."

#clean = re.sub(r'(@[\w]*)|(https?:\/\/[A-Za-z0-9\s]*\.com\/?)|(#)|([^a-zA-Z0-9\s])|([R][T])', '',text)


print(clean)