import tkinter as tk;
from tkinter import filedialog,OptionMenu;
def fnnew():
	win=tk.Toplevel(root);
	win.grab_set();
	win.lift();
	win.focus_force();
	win.title("New Alarm");
	win.geometry("400x300");
	tk.Label(win,text="ADD NEW ALARM",font=("Arial",24)).pack(pady=10);
	win_tframe=tk.Frame(win);
	win_tframe.pack(fill="x",pady=5);
	win_aframe=tk.Frame(win);
	win_aframe.pack(fill="x",pady=5);
	tk.Label(win_tframe,text="Time:",font=("Arial",24)).pack(side="left",fill="x",padx=(0,5));
	hour=tk.Entry(win_tframe,width=2);
	hour.pack(side="left",fill="x");
	tk.Label(win_tframe,text=":",font=("Arial",24)).pack(side="left",fill="x",padx=(0,2));
	minute=tk.Entry(win_tframe,width=2);
	minute.pack(side="left",fill="x");
	tk.Label(win_aframe,text="Audio:",font=("Arial",24)).pack(side="left",fill="x",padx=(0,5));
	path=tk.Entry(win_aframe);
	path.pack(side="left",fill="x",padx=(0,10));
	def file_opener():
		path.delete(0,tk.END);
		path.insert(0,filedialog.askopenfilename(title="Select a audio you want for alarm ringtone",filetypes=[("MP3 Files","*.mp3"),("ALL FILES","*.*")]))
		win.lift();
		win.focus_force();
	tk.Button(win_aframe,text="Select...",font=("Arial",12),command=file_opener).pack(side="left",fill="x",padx=(0,5));
	def extracter():
		alarm_time=[];
		alarm_sound=[];
		alarm_active=[];
		with open("alarm_data.txt","r") as context:
			content=[i.rstrip() for i in context]
			if not(content==[]):
				alarm_time=content[0].split(",");
				alarm_sound=content[1].split(",");
				alarm_active=content[2].split(",");
			if not((hour.get()+":"+minute.get()) in alarm_time):
				alarm_active.append("on");
				alarm_time.append(hour.get()+":"+minute.get());
				alarm_sound.append("\""+path.get()+"\"");
		with open("alarm_data.txt","w") as content:
			content.write(",".join(alarm_time)+"\n"+",".join(alarm_sound)+"\n"+",".join(alarm_active));
		win.destroy();
	tk.Button(win,text="Done",font=("Arial",30),command=extracter).pack(pady=10);
def fndelete():
	win=tk.Toplevel(root);
	win.title("Delete Alarm");
	win.grab_set();
	win.lift();
	win.focus_force();
	win.geometry("400x300");
	tk.Label(win,text="Select a alarm to delete",font=("Arial",24)).pack(pady=10);
	opt=tk.StringVar(value="select one...");
	alarm_time=[];
	alarm_sound=[];
	alarm_active=[];
	with open("alarm_data.txt","r") as context:
		content=[i.rstrip() for i in context]
		if not(content==[]):
			alarm_time=content[0].split(",");
			alarm_sound=content[1].split(",");
			alarm_active=content[2].split(",");
	OptionMenu(win,opt,*alarm_time).pack();
	def delalarm():
		if opt.get() in alarm_time:
			index=alarm_time.index(opt.get());
			del alarm_time[index];
			del alarm_sound[index];
			del alarm_active[index];
			if alarm_time!=[]:
				with open("alarm_data.txt","w") as content:
					content.write(",".join(alarm_time)+"\n"+",".join(alarm_sound)+"\n"+",".join(alarm_active));
			else:
				with open("alarm_data.txt","w") as content:
					pass
			win.destroy();
	tk.Button(win,text="Delete",font=("Arial",30),command=delalarm).pack(pady=10);
def fnactivate():
	win=tk.Toplevel(root);
	win.title("Activation Setting");
	win.grab_set();
	win.lift();
	win.focus_force();
	win.geometry("400x300");
	tk.Label(win,text="Set the activation for alarm",font=("Arial",24)).pack(pady=10);
	opt=tk.StringVar(value="select one...");
	alarm_time=[];
	alarm_sound=[];
	alarm_active=[];
	with open("alarm_data.txt","r") as context:
		content=[i.rstrip() for i in context]
		if not(content==[]):
			alarm_time=content[0].split(",");
			alarm_sound=content[1].split(",");
			alarm_active=content[2].split(",");
	OptionMenu(win,opt,*alarm_time).pack();
	apt=tk.StringVar(value="on");
	OptionMenu(win,apt,*["on","off"]).pack();
	def fnchange():
		if opt.get() in alarm_time:
			alarm_active[alarm_time.index(opt.get())]=apt.get();
			with open("alarm_data.txt","w") as content:
				content.write(",".join(alarm_time)+"\n"+",".join(alarm_sound)+"\n"+",".join(alarm_active));
	tk.Button(win,text="Change",font=("Arial",30),command=fnchange).pack(pady=10);
	tk.Button(win,text="Exit",font=("Arial",30),command=win.destroy).pack(pady=10);
def fnedit():
	dwin=tk.Toplevel(root);
	dwin.title("Edit Alarm");
	dwin.grab_set();
	dwin.lift();
	dwin.focus_force();
	dwin.geometry("400x300");
	tk.Label(dwin,text="Select a alarm to edit...",font=("Arial",24)).pack(pady=10);
	opt=tk.StringVar(value="select one...");
	alarm_time=[];
	alarm_sound=[];
	alarm_active=[];
	with open("alarm_data.txt","r") as context:
		content=[i.rstrip() for i in context]
		if not(content==[]):
			alarm_time=content[0].split(",");
			alarm_sound=content[1].split(",");
			alarm_active=content[2].split(",");
	OptionMenu(dwin,opt,*alarm_time).pack();
	def fndelnew():
		dwin.destroy();
		if opt.get() in alarm_time:
			win=tk.Toplevel(root);
			win.title("Edit:"+opt.get());
			win.grab_set();
			win.lift();
			win.focus_force();
			win.geometry("400x300");
			tk.Label(win,text="Edit Alarm",font=("Arial",24)).pack(pady=10);
			win_tframe=tk.Frame(win);
			win_tframe.pack(fill="x",pady=5);
			win_aframe=tk.Frame(win);
			win_aframe.pack(fill="x",pady=5);
			tk.Label(win_tframe,text="Time:",font=("Arial",24)).pack(side="left",fill="x",padx=(0,5));
			hour=tk.Entry(win_tframe,text=tk.StringVar(value=opt.get().split(":")[0]),width=2);
			hour.pack(side="left",fill="x");
			tk.Label(win_tframe,text=":",font=("Arial",24)).pack(side="left",fill="x",padx=(0,2));
			minute=tk.Entry(win_tframe,text=tk.StringVar(value=opt.get().split(":")[1]),width=2);
			minute.pack(side="left",fill="x");
			tk.Label(win_aframe,text="Audio:",font=("Arial",24)).pack(side="left",fill="x",padx=(0,5));
			path=tk.Entry(win_aframe,text=tk.StringVar(value="".join(alarm_sound[alarm_time.index(opt.get())].split("\""))));
			path.pack(side="left",fill="x",padx=(0,10));
			def file_opener():
				path.delete(0,tk.END);
				path.insert(0,filedialog.askopenfilename(title="Select a audio you want for alarm ringtone",filetypes=[("MP3 Files","*.mp3"),("ALL FILES","*.*")]))
				win.lift();
				win.focus_force();
			tk.Button(win_aframe,text="Select...",font=("Arial",12),command=file_opener).pack(side="left",fill="x",padx=(0,5));
			def extracter():
				alarm_time=[];
				alarm_sound=[];
				alarm_active=[];
				with open("alarm_data.txt","r") as context:
					content=[i.rstrip() for i in context]
					if not(content==[]):
						alarm_time=content[0].split(",");
						alarm_sound=content[1].split(",");
						alarm_active=content[2].split(",");
				index=alarm_time.index(opt.get());
				del alarm_time[index];
				del alarm_sound[index];
				del alarm_active[index];
				if alarm_time!=[]:
					with open("alarm_data.txt","w") as content:
						content.write(",".join(alarm_time)+"\n"+",".join(alarm_sound)+"\n"+",".join(alarm_active));
				else:
					with open("alarm_data.txt","w") as content:
						pass
				alarm_time=[];
				alarm_sound=[];
				alarm_active=[];
				with open("alarm_data.txt","r") as context:
					content=[i.rstrip() for i in context]
					if not(content==[]):
						alarm_time=content[0].split(",");
						alarm_sound=content[1].split(",");
						alarm_active=content[2].split(",");
					if not((hour.get()+":"+minute.get()) in alarm_time):
						alarm_active.append("on");
						alarm_time.append(hour.get()+":"+minute.get());
						alarm_sound.append("\""+path.get()+"\"");
				with open("alarm_data.txt","w") as content:
					content.write(",".join(alarm_time)+"\n"+",".join(alarm_sound)+"\n"+",".join(alarm_active));
				win.destroy();
				fnedit();
				return
			tk.Button(win,text="Done",font=("Arial",30),command=extracter).pack(pady=10);
	tk.Button(dwin,text="Edit",font=("Arial",30),command=fndelnew).pack(pady=10);
	tk.Button(dwin,text="Exit",font=("Arial",30),command=dwin.destroy).pack(pady=10);
def fncheck():
	win=tk.Toplevel(root);
	win.title("View Current Alarm Status");
	win.geometry("500x300");
	win.grab_set();
	win.lift();
	win.focus_force();
	tk.Label(win,text="All Alarm Status:",font=("Arial",30)).pack(pady=10);
	alarm_time=[];
	alarm_sound=[];
	alarm_active=[];
	with open("alarm_data.txt","r") as context:
		content=[i.rstrip() for i in context]
		if not(content==[]):
			alarm_time=content[0].split(",");
			alarm_sound=content[1].split(",");
			alarm_active=content[2].split(",");
	tk.Label(win,text="\n".join([alarm_time[i]+","+alarm_active[i] for i in range(len(alarm_time))])).pack();
	tk.Button(win,text="Exit",font=("Arial",20),command=win.destroy).pack(pady=10);
root=tk.Tk();
root.title("simple_alarm");
root.geometry("1000x600");
root.configure(bg="lightgreen");
top_title=tk.Label(root,text="Alarm Controller",font=("Arial",24)).pack(pady=10);
tk.Button(root,text="New",bd=5,font=("Arial",30),command=fnnew).pack(fill="both",expand=True);
tk.Button(root,text="Delete",bd=5,font=("Arial",30),command=fndelete).pack(fill="both",expand=True);
tk.Button(root,text="Activation",bd=5,font=("Arial",30),command=fnactivate).pack(fill="both",expand=True);
tk.Button(root,text="Edit",bd=5,font=("Arial",30),command=fnedit).pack(fill="both",expand=True);
tk.Button(root,text="View Current Alarm Status",bd=5,font=("Arial",30),command=fncheck).pack(fill="both",expand=True);
root.mainloop();
