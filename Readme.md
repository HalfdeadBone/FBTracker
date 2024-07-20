# FBTracker [Abandoned]
The program that you see here is an old bet between me and my friend.
The idea was to create the activity tracker Stalk bot, as a type of fun project with overusing requests.

On facebook website officialy it's impossible to do so. Why? 
Facbook changed old api to graph api + incoming values are hidden or have inconsistant clases. 

After some "digging", meaning 5 hours of rapidly clicking on every part of the site... I gave up. 
![sadcat](https://en.meming.world/images/en/1/13/Thumbs_Up_Crying_Cat.jpg)

UNTIL I REMEMBERD THAT there is mobile facebook, and oh boy oh boy. There is gold - buddyList

But Ivar! On a right site there is a bar with active people. Why not just scrap this?

Welp - The problem is, that "activebar" is limited to 20-25 people active + groups. Even more - updates are irregular and might be off by up to 5 mins or in worse case scenario "stuck" until reload. Reloading is kind of dangerous, cause facebook analyze's trafic and bans certain functions.. sooo.. Nope

About Active status. Facebook fucked it up real hard. How, you might ask? So listen.
If you stay in the "browser", sometimes present cookie, might be loaded after leaving facebook.com (also because facebook loves to take "necesary cookies" out of the browser), so you might be active, even if you left facebook site and turned off your phone.

Congratulation Meta or Facebook. Whatever

# Requirements
1. Python 3.x
2. Selenium
3. BeautifulSoup4
4. webdriver_manager
5. requests

## How to use it?

Head to the config folder and find cookie.json. Paste there cookies with headings 

1. datr (cookie accept)
2. xs (expiration)
3. m_pixel_ratio(apparently it checks on login facebook da fuq)
4. c_user (user id)
5. oo
6. sb

!! Change in cookie all valuse from "sameSite" to Strict

```JSON
[
    {
        "name": "one of the cookies",
        "sameSite": "Strict"
    },
    {
        "name": "one of the cookies",
        "sameSite": "Strict"
    }
]

```

in bash run

```bash
python main.py
```

Then the program should run and open the selenium page. In colleceted_data folder you will find created files with active hours.
Don't close selenium window. Program sends data every minute to folders , where the DIR name  is that of the user. Data is segregated by date.
## Plans
Curetnly the program is in phase of development.
- [x] Optimizing Data holding and saving
- [x] Saving data after quiting
- [x] temp files as bakcup during fails
- [x] recovery
- [ ] Further code cleaning
- [ ] JSON summary of the person (quick scrap)
- [ ] Data analyzer
