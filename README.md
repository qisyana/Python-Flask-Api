## 🛠️ Python-Flask-Api

- Search Lirik Lagu
- Search Chord Lagu
- Random Quotes
- Info Gempa
- Stalk Instagram


# Cara Penggunaan

# Search Lirik Lagu
```
https://localhost:8080/api/lirik?search=Alan Walker
```
# Response
```
{
    "results": "\n(feat. K-391 & Emelie Hollow)\n\r\n[Verse 1: Emelie Hollow]\r\nLily was a little girl\r\nAfraid of the big, wide world\r\nShe grew up within her castle walls\r\nNow and then she tried to run\r\nAnd then on the night with the setting sun\r\nShe went in the woods away\r\nSo afraid, all alone\n\r\n[Pre-Chorus: Emelie Hollow]\r\nThey warned her, don\u2019t go there\r\nThere's creatures who are hiding in the dark\r\nThen something came creeping\r\nIt told her, don\u2019t you worry just\n\r\n[Chorus: Emelie Hollow]\r\nFollow everywhere I go\r\nTop over the mountains of valley low\r\nGive you everything you\u2019ve been dreaming of\r\nJust let me in, ooh\r\nEverything you watch and go\r\nThat'll be the magic story you\u2019ve been told\r\nAnd you\u2019ll be safe under my control\r\nJust let me in, ooh\r\nJust let me in, ooh\n\r\n[Verse 2: Emelie Hollow]\r\nShe knew she was hypnotized\r\nAnd walking on cold thin ice\r\nThen it broke, and she awoke again\r\nThen she ran faster and\r\nStarted screaming, is there someone out there?\r\nPlease help me\r\nCome get me\r\nBehind her, she can hear it say\n\r\n[Chorus: Emelie Hollow]\r\nFollow everywhere I go\r\nTop over the mountains of valley low\r\nGive you everything you\u2019ve been dreaming of\r\nJust let me in, ooh\r\nEverything you watch and go\r\nThat'll be the magic story you\u2019ve been told\r\nAnd you\u2019ll be safe under my control\r\nJust let me in, ooh\r\nJust let me in, ooh\n\r\n[Bridge: Emelie Hollow]\r\nOoh, ooh, ooh, ooh\r\nEverything you wanted gotta be the magic story you\u2019ve been told\r\nAnd you\u2019ll be safe under my control\r\nJust let me in, ooh\n\r\n[Outro: Emelie Hollow]\r\nFollow everywhere I go\r\nTop over the mountains of valley low\r\nGive you everything you\u2019ve been dreaming of\r\nJust let me in, ooh\r\nThen she ran faster and\r\nStarted screaming, is there someone out there?\r\nPlease help me\r\nJust let me in, ooh"
}
```

# Search Chord Lagu
```
https://localhost:8080/api/chord?q=alone
```
# Response
```
{
    "results": "\n(feat. K-391 & Emelie Hollow)\n\r\n[Verse 1: Emelie Hollow]\r\nLily was a little girl\r\nAfraid of the big, wide world\r\nShe grew up within her castle walls\r\nNow and then she tried to run\r\nAnd then on the night with the setting sun\r\nShe went in the woods away\r\nSo afraid, all alone\n\r\n[Pre-Chorus: Emelie Hollow]\r\nThey warned her, don\u2019t go there\r\nThere's creatures who are hiding in the dark\r\nThen something came creeping\r\nIt told her, don\u2019t you worry just\n\r\n[Chorus: Emelie Hollow]\r\nFollow everywhere I go\r\nTop over the mountains of valley low\r\nGive you everything you\u2019ve been dreaming of\r\nJust let me in, ooh\r\nEverything you watch and go\r\nThat'll be the magic story you\u2019ve been told\r\nAnd you\u2019ll be safe under my control\r\nJust let me in, ooh\r\nJust let me in, ooh\n\r\n[Verse 2: Emelie Hollow]\r\nShe knew she was hypnotized\r\nAnd walking on cold thin ice\r\nThen it broke, and she awoke again\r\nThen she ran faster and\r\nStarted screaming, is there someone out there?\r\nPlease help me\r\nCome get me\r\nBehind her, she can hear it say\n\r\n[Chorus: Emelie Hollow]\r\nFollow everywhere I go\r\nTop over the mountains of valley low\r\nGive you everything you\u2019ve been dreaming of\r\nJust let me in, ooh\r\nEverything you watch and go\r\nThat'll be the magic story you\u2019ve been told\r\nAnd you\u2019ll be safe under my control\r\nJust let me in, ooh\r\nJust let me in, ooh\n\r\n[Bridge: Emelie Hollow]\r\nOoh, ooh, ooh, ooh\r\nEverything you wanted gotta be the magic story you\u2019ve been told\r\nAnd you\u2019ll be safe under my control\r\nJust let me in, ooh\n\r\n[Outro: Emelie Hollow]\r\nFollow everywhere I go\r\nTop over the mountains of valley low\r\nGive you everything you\u2019ve been dreaming of\r\nJust let me in, ooh\r\nThen she ran faster and\r\nStarted screaming, is there someone out there?\r\nPlease help me\r\nJust let me in, ooh"
}
```

# Random Quotes
```
https://localhost:8080/api/random/quotes
```
# Response 
```
    {"author":"George W.","quotes":"Harapan tak pernah meninggalkan kita, kita yang meninggalkan harapan.","status":200}
```

# Info Gempa
```
https://localhost:8080/api/infogempa
```
# Response 
```
    {"kedalaman":"10 km","koordinat":"5.63 LS - 101.60 BT","lokasi":"Pusat gempa berada di laut 80 km BaratDaya Enggano","magnitude":"6.5","map":"https://ews.bmkg.go.id/tews/data/20210210195227.mmi.jpg","potensi":"Dirasakan (Skala MMI): II-III Enggano, II Kota Bengkulu, II Kepahiang","status":200,"waktu":"10 Feb 2021, 19:52 WIB"}
```

# Stalk Instagram
```
https://localhost:8080/api/ig/stalk?username=ekooju
```
# Response 
```
{
    "results": https://static.xx.fbcdn.net/rsrc.php/v3/yt/l/0,cross/sHzueLzk5lu.css?_nc_x=Ij3Wp8lg5Kz
}
```

# Live API
* https://python-api-zhirrr.herokuapp.com/
- Gunakan Parameter Yg Sama Yak :)
