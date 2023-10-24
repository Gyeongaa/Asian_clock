# Asian_clock

## Project description
This is the talking clock that we developed for the course 'Introduction to Voice Technology.' The talking clock can announce the current time in five Asian countries: China, Singapore, Thailand, Japan, and Korea. It does so in their respective time zones and languages, providing clear audio outputs. Additionally, it features an alarm function that allows users to set reminders for specific tasks in particular time zones.


## Installation
To get started, follow the installation instructions below.
1. Python version
    ensure you have Python 3.9 installed on your system. You can download new Python versions from here: https://www.python.org/downloads/
2. clone the repository.
    Open your terminal or command prompt; change the current working directory to the location where you want the cloned directory; run ‘git clone https://github.com/Gyeongaa/Asian_clock.git’ to clone the project repository from GitHub to your local machine.
    Alternatively, you can download the project as a ZIP file by clicking the 'Code' button on the repository page and selecting 'Download ZIP.' Extract the ZIP archive to your desired installation location.
    Run ` pip install -r requirements.txt` to install the dependencies required.
4. run the project
    After setting up the project and its dependencies, you can run the project. Refer to the project's README or documentation for detailed usage instructions.


## Usage
Run `python main.py` in the terminal. Make sure to be in the same directory where the repository is installed in the terminal. It will open an interactive GUI with which you can interact with.

Each button will tell the current time in a different language. The text on each  button says "What's the time?" in the language it will speak. For example, in Romania people say "Cât e(ste) ceasul?" to ask about the current time.

The slider at the bottom adjusts the speed at which the time is said. A setting of `1.5` will tell the time 1.5x faster than the default speech rate.

## Languages supported
- Chinese 
- English
- Thai
- Japanese
- Korean

## Linguistic rules for telling time

### Chinese

### English

### Thai

### Japanese

### Korean


## GDPR Compliance
The audio files used were generated using TTS APIs. For Romanian, Polish, Irish and French, Narakeet was used (https://www.narakeet.com/languages/).
The voice used for Romanian was Alina, for Polish, Justyna, for Irish, Dearbhla, and for French, Marion.
The French voice is meant to resemble Metropolitan French, whereas the Irish voice resembles Ulster (or colloquially known as Donegal) Irish.

No consent forms were required for the collection of this data since there were no individuals recorded by us
to generate this speech. The data used for the speaking clock therefore complies
with GDPR regulations.
