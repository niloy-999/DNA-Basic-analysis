import tkinter as tk
from tkinter import filedialog
import random
import  Colo

sequence = ""

codon_color = {} #dictionary of color and count of codon in list 





#opening files
def browse_Fasta():
    
    #take sequence as global
    global sequence
    
    
    file_path = filedialog.askopenfilename(
        title="Select FASTA File",
        filetypes=(("FASTA files", "*.fasta *.fa"), ("All files", "*.*")) #only for fasta
    )
    
    
    if file_path:
        try:
            with open(file_path, 'r') as fasta_file:
                fasta_content = fasta_file.readlines()
                
                #file into string
                
                for line in fasta_content:
                    if not line.startswith(">"):
                        sequence += line.strip()
                        
                #priting the length        
                input_display.config(state = tk.NORMAL)
                input_display.delete(1.0, tk.END)
                input_display.insert(tk.END,len(sequence)) #length 
                input_display.config(state = tk.DISABLED)
                
                
        except Exception as e:
            print(f"Error reading file: {e}")

 
#make the codon as a list of strings
            
def process_Seq(seq):
    
    codon_list = [sequence[i:i+3] for i in range(0, len(seq),3)
                  if len(seq[i:i+3])==3
                  ]
    return codon_list            



#Analysis the sequence

def codon_s():
    
    #taking global
    global codon_color
    
    #Get the sequence as codon           
    codon_list = process_Seq(sequence)
    
    
    codon_display.config(state=tk.NORMAL)
    codon_display1.config(state=tk.NORMAL)
    codon_display2.config(state=tk.NORMAL)
    
    #start to make color
    for codon in codon_list:
        
        #take in dictionary as initial element
        
        if codon not in codon_color:
            codon_color[codon] = [Colo.col(),1]  #initial element [color , count]
        
        #increment codon count    
        else:
            codon_color[codon][1] +=1
        
        #set color     
        color = codon_color[codon][0]     
        codon_display.insert(1.0, codon,codon)
        codon_display.tag_config(codon , foreground=color )
        
        #only for color
        codon_display1.insert(1.0, codon,codon)
        codon_display1.tag_config(codon , foreground=color , background=color )
    
    #count the codon repeptions
    for codon , data in codon_color.items():
        color , count = data
        codon_display2.insert(tk.END, f"{codon}: {count} times\n")    
    
        
    codon_display.config(state=tk.DISABLED)
    codon_display1.config(state=tk.DISABLED)         
    codon_display2.config(state=tk.DISABLED)        
    
                

# Top level window 
frame = tk.Tk() 
frame.title("Graphics Software Development") 
frame.geometry('1280x580') 

#button for FASTA file
browse_button = tk.Button(frame, text="Browse FASTA File", command=browse_Fasta)
browse_button.pack(pady=10)

#button for see codon
browse_button = tk.Button(frame, text="See the codons", command=codon_s)
browse_button.pack(pady=10)


#length display
inputdisplay_label = tk.Label(frame, text="Length of the Sequence : ")
inputdisplay_label.pack(side=tk.LEFT) 


input_display = tk.Text(frame , wrap=tk.WORD, width=15, height=2)
input_display.pack(side=tk.LEFT)
input_display.config(state = tk.DISABLED)



#codon display
codondisplay_label = tk.Label(frame, text="CODON : ")
codondisplay_label.pack(side=tk.LEFT) 


codon_display = tk.Text(frame , wrap=tk.WORD, width=30, height=10)
codon_display.pack(side=tk.LEFT , padx=10)
codon_display.config(state = tk.DISABLED)



#codon count

codon_display2 = tk.Text(frame , wrap=tk.WORD, width=18, height=20)
codon_display2.pack(side=tk.RIGHT , padx=20) 
codon_display2.config(state = tk.DISABLED)


codondisplay_label2 = tk.Label(frame, text="Codon Count")
codondisplay_label2.pack(side=tk.RIGHT , padx=10)


#codon background

codon_display1 = tk.Text(frame , wrap=tk.WORD, width=30, height=20)
codon_display1.pack( side=tk.RIGHT)
codon_display1.config(state = tk.DISABLED)


codondisplay_label1 = tk.Label(frame, text="Only color: ")
codondisplay_label1.pack( side=tk.RIGHT ) 



#codon background

codon_display2 = tk.Text(frame , wrap=tk.WORD, width=5, height=2)
codon_display2.pack(padx=30)
codon_display2.config(state = tk.DISABLED)


codondisplay_label2 = tk.Label(frame, text="GC Count: ")
codondisplay_label2.pack() 




# Start the Tkinter main loop
frame.mainloop()