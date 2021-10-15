Path = r'C:\Users\24131\Desktop\x\wallhaven-6q22kl.jpg'
Path = Path.strip("\\u202a")  #不删除“\u202a”
HtmlFile = open(r'' + Path, 'r', encoding='utf-8')
