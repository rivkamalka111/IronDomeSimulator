import random
#מילון בתוך מילון שבמילון הראשי יש שם ומדינה ובתוך כל מילון יש רשימה של טילים עם מהירות לדקה
missileLebanon = {"Fajr-3": 23, "Zelzal-2": 25}
missileSyria = {"M-302": 28, "Fajr-5": 33, "SS-21": 10}
missileIran = {"Shahab-3": 200, "Fateh-110": 250, "Zolfaghar": 210, "Qiam-1": 220}
EnemyCountries = {"Lebanon": missileLebanon, "Syria": missileSyria, "Iran": missileIran}

# מילון של מדינות עם מרחקם מהגבול הישראלי
limCountry = {"Lebanon": 80, "Syria": 100, "Iran": 1000}

# מילון של ערים עם מרחק מהגבול הישראלי
limcity = {"Ashdod": 250, "Ashkelon": 280, "Tel-Aviv": 160, "Haifa": 120, "Kiryat-Shmona": 30, "Nahariya": 50, "Beit-Shemesh": 220, "Tiberias": 120, "Rishon LeZion": 120}

# מילון של ערים ששם יש כיפות ברזל ומרחקם מהגבול הישראלי
limIronDome = {"Beit-Shemesh": 220, "Haifa": 120, "Tiberias": 120, "Jerusalem": 260}


# הגרלה של מדינה שממנה נשלח הטיל והצבה במשתנים את שם המדינה ואת המרחק שלה מהגבול הישראלי
listEnemy = list(limCountry.keys())
enemy_state = random.choices(listEnemy)
nameEnemy = enemy_state[0]
kmFrom_the_Enemy = limCountry[nameEnemy]

# הגרלה של עיר שאליה נשלח הטיל והצבה במשתנים את שם העיר והמרחק מהגבול הישראלי
listCity = list(limcity.keys())
c = random.choices(listCity)
cityIs = c[0]
diss = limcity[cityIs]

#  רשימת הטילים של המדינה שיצאה בהגרלה
missileCountry = EnemyCountries[nameEnemy]

# הגרלה של טיל מתוך המדינה שהוגרלה והצבתי של שם הטיל והמהירות לדקה במשתנים
missilee = random.choice(list(missileCountry.items()))
Missile = missilee[0]
Speed = missilee[1]


all = (kmFrom_the_Enemy+diss)//Speed

MIN = {abs(v-diss): k for k, v in limIronDome.items()if abs(v-diss) < 1000}

cityIronDome = MIN[min(MIN)]
