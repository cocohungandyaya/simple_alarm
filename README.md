# simple_alarm
A alarm app that can works as a simple alarm,by choosing the audio you want and the time you want,it will work just like a alarm(even though i forgot to write stop button for sudden stop)

update for this project:it doesnt support windows motherfucker,the crate i use cause a constant stuck so yeah it works on my pc then it is fine bruh

so the gui is work on window and linux but the backend core code only works on linux but not window bruh

whatever i am just a jerk

## App Update log:
10 Oct 2026:i write the basic backend of my simple alarm app using rust

11 Oct 2026:fix a small bug that it can't detect 00:00 sth like that

still 11 Oct 2026:i fix the problem that it delay activate for 1 second,also i added activation check for if the alarm is on or not

uhh...emmm....yeah still 11 Oct 2026:due to i am really kinda jobless so i done the gui bruh
## How to use(the backend version):
it will auto generate a alarm_data.txt,open it,here is an example:
```txt
22:00,23:00
"your/path/to/audio","your/path/to/audio"
on,off
```
## How to use(backend&frontend):
download the latest release zip file and unzip it,run the (simple_alarm || simple_alarm.exe) you will see it auto generate a file call alarm_data.txt and then run the (simple_alarm_gui || simple_alarm_gui.exe)
