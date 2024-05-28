from tkinter import *
from tkinter import messagebox as mb
from pytube import YouTube

#download bottun
# Defining the downloader function for YouTube Video Downloader project using Python
def downloader(link, directory, filename):
    yt_link = link.get()
    save_path = directory.get()
    aftersave_filename = filename.get()

    try:
        yt = YouTube(yt_link)
        video = yt.streams.first()#extracts the video
        video.download(save_path, aftersave_filename)
    except:
        mb.showerror('Error', 'Connection Error! You are offline!')


#reset button 
def reset(l_strvar, d_strvar, fn_strvar):
    l_strvar.set('')
    d_strvar.set('')
    fn_strvar.set('')



#design
root=Tk()
root.title("youtube video downloder")
root.geometry('700x300')
root.resizable(0, 0)
root.config(bg="lightgreen")

#in frame design
Label(root,text="Youtube Video Downloder with coding....!",font=("Times New Roman",18),bg="lightgreen").place(relx=0.25,rely=0.05)

#entry boxes


Label(root,text="Paste the Youtube Video link :-",font=("Times New Roman",13),bg="lightgreen").place(relx=0.05,rely=0.25)
Label(root,text="Enter the save location :-",font=("Times New Roman",13),bg="lightgreen").place(relx=0.05,rely=0.40)

Label(root,text="Enter the File Name :-",font=("Times New Roman",13),bg="lightgreen").place(relx=0.05,rely=0.55)

#entry boxes
#link entry
link_strvar = StringVar(root)
link_entry=Entry(root,width=50,bg="orange",textvariable=link_strvar).place(relx=0.30,rely=0.25)
#file name entry
dir_strvar = StringVar(root)
dir_entry=Entry(root,width=50,bg="orange",textvariable=dir_strvar).place(relx=0.30,rely=0.40)
#file name
filename_strvar = StringVar(root)
filename_entry=Entry(root,width=50,bg="orange",textvariable=filename_strvar).place(relx=0.30,rely=0.55)



# Creating the buttons
download_btn = Button(root, text='Download', font=7, bg='Aquamarine',command=lambda: downloader(link_entry, dir_entry, filename_entry)).place(relx=0.3, rely=0.75)
reset_btn = Button(root, text='Reset', font=7, bg='Aquamarine',command=lambda: reset(link_strvar, dir_strvar, filename_strvar)).place(relx=0.5, rely=0.75)

# Finalizing the window of Python YouTube Video Downloader project
root.update()


root.mainloop()
