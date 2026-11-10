#![windows_subsystem = "windows"]
//i am just a dick bruh,writing this useless piece of shit
//so idk it might be ass but i need it i hate relying on my phone as my fucking alarm bruh
//so this will be a simple alarm app to wake me up and this part will be the backend
//for how it works will be via maybe reading the file by seeing if have file change and sth like that whatever
use std::fs;
use std::path::Path;
use std::time::Duration;
use chrono::{Local,Timelike};
use std::thread::sleep;
use std::io::BufReader;
use rodio::{Decoder,MixerDeviceSink,source::Source};
use std::process::exit;
fn main() {
	let path=Path::new("alarm_data.txt");
	let mut exist:bool=false;
	match fs::exists(path){
		Ok(i)=>{exist=i;},
		Err(e)=>{eprint!("Some error happend idk why bruh");exit(1);}
	}
	if !exist{
		fs::write("alarm_data.txt","");
		println!("file created");
	}
	let mut player:rodio::Player;
	let sink_handle=rodio::DeviceSinkBuilder::open_default_sink().expect("bruh");
	loop{
		let mut time_now=Local::now();
		sleep(Duration::from_secs(((61-time_now.second())%60).into()));
		let data:String=std::fs::read_to_string(path).unwrap();
		if !data.is_empty(){
			let alarm_time:Vec<String>=data.split("\n").map(|x|x.to_string()).collect::<Vec<String>>()[0].split(",").map(|x|x.to_string()).collect::<Vec<String>>();
			let alarm_sound:Vec<String>=data.split("\n").map(|x|x.to_string()).collect::<Vec<String>>()[1].split(",").map(|x|x.to_string()).collect::<Vec<_>>();
			if alarm_time.contains(&format!("{}:{}",time_now.hour(),time_now.minute())){
				sleep(Duration::from_secs(1));
				time_now=Local::now();
				for i in 0..alarm_time.len(){
					if format!("{:02}:{:02}",time_now.hour(),time_now.minute())==alarm_time[i].trim(){
						let file=BufReader::new(fs::File::open(alarm_sound[i].split("\"").collect::<Vec<_>>().join("")).unwrap());
						player=rodio::play(&sink_handle.mixer(),file).unwrap();
					}
				}
			}
		}
	}	
}
