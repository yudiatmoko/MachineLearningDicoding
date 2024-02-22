# lower -> upper
lowerString = "dicoding"
lowerString = lowerString.upper()
print(lowerString)

# upper -> lower
upperString = "DICODING"
upperString = upperString.lower()
print(upperString)

# remove whitespace sebelah kanan
print("DicodingR      ".rstrip())

# remove whitespace sebelah kiri
print("            LDicoding".lstrip())

# remove whitespace sebelah kanan dan kiri
print("            LDicodingR          ".strip())

# remove other character
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))

# find character awal kata -> boolean
kata = 'CodeDicoding'
print(kata.startswith("Code"))

# find character akhir kata -> boolean
kata = 'CodeDicoding'
print(kata.endswith("ing"))

# join string ( _ adalah delimiter atau penggabung)
print('_'.join(['Dicoding','Indonesia', '!']))

# split string
print("Ilham2Yudiatmoko2!".split("2"))

print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))

# replace string -> case sensitive
oldString = "Halo Ilham"
newString = oldString.replace("Ilham", "Jawa")
print(newString)