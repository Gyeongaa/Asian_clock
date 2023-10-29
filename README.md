# Asian_clock⏰

## Project Description
This talking clock was developed as a group project for the 'Introduction to Voice Technology' and 'Programming' courses as part of the MSc Voice Technology program at RUG - Campus Fryslan.

## Installation ✅
To get started, follow the installation instructions below.
1. Python version
    Ensure you have Python 3.9 installed on your system. You can download new Python versions from here: https://www.python.org/downloads/
2. Clone the repository
    Open your terminal or command prompt; change the current working directory to the location where you want the cloned directory; run ‘git clone https://github.com/Gyeongaa/Asian_clock.git’ to clone the project repository from GitHub to your local machine.
    Alternatively, you can download the project as a ZIP file by clicking the green 'Code' button at the top of the repository and selecting 'Download ZIP.' Extract the ZIP archive to your desired installation location.
3. Run 'pip install audio_effects' 
4. Run ' pip install -r requirements.txt' to install the dependencies required.    
5. Run the project
    After setting up the project and its dependencies, you can run the project. Refer to the project's README or documentation for detailed usage instructions.


## Usage
Open the terminal and change the current working directory to the one where the repository is installed. Run python main.py in the terminal.

An interactive GUI window will pop up, displaying an Asian map with flags marking five Asian countries. Next to each country, there is a button that the user can click on. When a button with the country's name is clicked, the clock will tell the current time in that country in its language.

On the left side of the window, the current time in Singapore is shown by default. Below the time, there are two slider bars that allow users to adjust the speaking rate (0-2) and volume (0-1) of the audio according to their preferences. There is also a 'Toggle Mode' button that lets users switch to different modes.

In the lower-left corner, there is a 'Set Custom Alarm' button, which allows users to set alarm times in one of the five Asian timezones to remind themselves of specific tasks. After the alarm is set, a text with the format 'Alarm Alarm_name: year-month-date hour-minute-second AM/PM is set' is diaplayed.

Video Demonstration: 

mov: https://drive.google.com/file/d/1JMlYQhxqeblZx-_0_98iq_cb_dYJFQBB/view?usp=drive_link

mp4: https://drive.google.com/file/d/1pEQTudxevmeS-sZAjiHRE06Ml-nCwuTf/view?usp=drive_link

## Audio Languages Supported 🌏
- Chinese 
- English 
- Thai 
- Japanese 
- Korean 

## Linguistic Rules for Expressing Time

### Chinese 🇨🇳
In Chinese, the time is typically expressed in the 24-hour clock format or 12-hour clock format. Here's how time is commonly expressed in Chinese of 12-hour clock format:

"现在是" (It's now) + "上午" (AM) or "下午" (PM) + hour + "点" (hour) + minute + "分" (minute)

Where:

上午 is used for times from midnight (00:00) until noon (12:00 PM).
下午 is used for times from noon (12:00 PM) until midnight (00:00 AM, next day).
hour is the current hour in digits (e.g., 01, 02, ..., 12, 13, ..., 23).
minute is the current minute in digits (e.g., 00, 01, ..., 58, 59).

For example:

06:30 AM - 现在上午六点三十分 (It's now 06:30 AM).

10:45 PM - 现在下午十点四十五分 (It's now 10:45 PM).


### English 🇸🇬
In English, the time in 12-hour clock format is commonly expressed as:

"It's" + minutes/(a) quarter(s) + "past" "to"  + hour + (optional) "AM" or "PM"

Here's a breakdown of the components:

"Past" is used to indicate minutes that have passed beyond the hour.

"To" is used to indicate minutes until the next hour.

"A quarter" is used to indicate a 15-minute interval or a quarter of an hour.

"AM" is used for times from midnight (00:00) until noon (12:00 PM).

"PM" is used for times from noon (12:00 PM) until midnight (00:00 AM of the next day).

The "hour" is the current hour represented in digits (e.g., 01, 02, ..., 12).

The "minutes" are the current minutes represented in digits (e.g., 00, 01, ..., 58, 59).

For example:

00:30 AM - "It's 12:30 AM"

10:40 PM - "It's 10:40 PM"

03:15 AM - "It's a quarter past 3 AM"

10:50 PM - "It's 10 minutes to 11 PM"

### Thai 🇹🇭
Thai people commonly express time using a 6-hour clock system, and this can be divided into four time periods, as well as four special expressions:

*Four Time Periods:*

1. Morning from 6 AM to 11 AM: The format is a number + โมง (o’clock) + ตอนเช้า (am for 6-11am). For example:
   - 6 AM = 6 โมงเช้า

2. Afternoon from 1 PM to 5 PM: The format is บ่าย (pm for 1-5pm) + a number + โมง (o’clock). For example:
   - 1 PM = บ่ายโมง 
   - 2 PM = บ่าย2โมง

3. Evening from 6 PM to 11 PM: The format is a number + ทุ่ม (pm for 6-11pm). Fo example:
   - 7 PM = 7 ทุ่ม 
   - 8 PM = 8 ทุ่ม 

4. Midnight from 1 AM to 5 AM: The format is ตี (am for 1-5 am) + a number. For example:
   - 1 AM = ตี1 
   - 2 AM = ตี2 

5. Specific words for 12pm and 12 am.
   - 12 am: เที่ยงคืน
   - 12 pm: เที่ยง

The whole sentence to express time in Thai:
ตอนนี้เวลา (the current time is) + am/pm & hour (follow the rules above) + number + นาที (minute)

### Japanese 🇯🇵
In Japanese, time is typically expressed in a 12-hour clock format. The common format for time expression is as follows:

"現在は"（It's now） + "午前" (AM) or "午後" (PM) + hour + "時" (hour) + minute + "分" (minute) + "です" (desu).

Where:

"午前" (AM) is used to indicate morning.
"午後" (PM) is used to indicate afternoon.
The hour is expressed in numeric form (e.g., 1, 2, ..., 12).
"時" (hour) indicates the hour.
Minutes are expressed numerically (e.g., 00, 01, ..., 58, 59).
"です" (desu) serves as the ending particle for politeness.

Here are some examples:

9:30 AM - "現在は午前9時30分です" (It's now 9:30 AM).

3:45 PM - "現在は午後3時45分です" (It's now 3:45 PM).

### Korean 🇰🇷
In South Korea, time is typically expressed using the 12-hour clock format. In the Korean language, the common way to express time is as follows:

"지금은" (It's now) + "오전" (AM) or "오후" (PM) + the hour + "시" (hour) + the minute + "분" (minute) + "입니다" (is).

Here's an explanation:

"오전" (AM) is used to indicate morning or AM times.
"오후" (PM) is used to indicate afternoon or PM times.
The hour is represented using numerical digits (e.g., 1, 2, ..., 12).
"시" (hour) indicates the hour.
The minute is represented in numerical form (e.g., 00, 01, ..., 58, 59).
"분" (minute) represents the minutes.
"입니다" (is) is a polite ending term.

Here are some examples:

9:30 AM - "지금은 오전 9시 30분입니다" (It's now 9:30 AM).

3:45 PM - "지금은 오후 3시 45분입니다" (It's now 3:45 PM).

## GDPR Compliance
The audio files used were generated using gTTS（[Google Text-to-Speech](https://gtts.readthedocs.io/en/latest/)） APIs. For Chinese, English, Thai, Japanne and Korean.

The Chinese natural voice is based on recordings by a member of group.
The consent form and data processing record for the individual voice are included in documentation.
So all the data we use complies with GDPR regulations.
