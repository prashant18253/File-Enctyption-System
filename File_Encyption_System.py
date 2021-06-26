from tkinter import *
import time 
import datetime
from tkinter import filedialog 
##########################################################################################################################################################
import string 
import pickle 

import numpy
from pyfinite import ffield
import copy 

Sbox = [['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76' ],
['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']]
RC = ['01','02','04','08','10','20','40','80','1B','36']
Sbox_inv = [['52', '09', '6A', 'D5', '30', '36', 'A5', '38', 'BF', '40', 'A3', '9E', '81', 'F3', 'D7', 'FB'],
['7C', 'E3', '39', '82', '9B', '2F', 'FF', '87', '34', '8E', '43', '44', 'C4', 'DE', 'E9', 'CB'],
['54', '7B', '94', '32', 'A6', 'C2', '23', '3D', 'EE', '4C', '95', '0B', '42', 'FA', 'C3', '4E'],
['08', '2E', 'A1', '66', '28', 'D9', '24', 'B2', '76', '5B', 'A2', '49', '6D', '8B', 'D1', '25'],
['72', 'F8', 'F6', '64', '86', '68', '98', '16', 'D4', 'A4', '5C', 'CC', '5D', '65', 'B6', '92'],
['6C', '70', '48', '50', 'FD', 'ED', 'B9', 'DA', '5E', '15', '46', '57', 'A7', '8D', '9D', '84'],
['90', 'D8', 'AB', '00', '8C', 'BC', 'D3', '0A', 'F7', 'E4', '58', '05', 'B8', 'B3', '45', '06'],
['D0', '2C', '1E', '8F', 'CA', '3F', '0F', '02', 'C1', 'AF', 'BD', '03', '01', '13', '8A', '6B'],
['3A', '91', '11', '41', '4F', '67', 'DC', 'EA', '97', 'F2', 'CF', 'CE', 'F0', 'B4', 'E6', '73'],
['96', 'AC', '74', '22', 'E7', 'AD', '35', '85', 'E2', 'F9', '37', 'E8', '1C', '75', 'DF', '6E'],
['47', 'F1', '1A', '71', '1D', '29', 'C5', '89', '6F', 'B7', '62', '0E', 'AA', '18', 'BE', '1B'],
['FC', '56', '3E', '4B', 'C6', 'D2', '79', '20', '9A', 'DB', 'C0', 'FE', '78', 'CD', '5A', 'F4'],
['1F', 'DD', 'A8', '33', '88', '07', 'C7', '31', 'B1', '12', '10', '59', '27', '80', 'EC', '5F'],
['60', '51', '7F', 'A9', '19', 'B5', '4A', '0D', '2D', 'E5', '7A', '9F', '93', 'C9', '9C', 'EF'],
['A0', 'E0', '3B', '4D', 'AE', '2A', 'F5', 'B0', 'C8', 'EB', 'BB', '3C', '83', '53', '99', '61'],
['17', '2B', '04', '7E', 'BA', '77', 'D6', '26', 'E1', '69', '14', '63', '55', '21', '0C', '7D']]
stoh_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D': 13, 'E':14, 'F':15}


root = Tk() 
root.geometry("1200x6000")
root.title("File Encryption and Decryption")
Tops = Frame(root, width = 1600, relief = SUNKEN) 
Tops.pack(side = TOP)
f1 = Frame(root, width = 800, height = 700, relief = SUNKEN) 
f1.pack(side = LEFT) 

####################time################################################
localtime = time.asctime(time.localtime(time.time())) 
lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'),text = " File Encrption and decryption",fg = "Black", bd = 10, anchor='w') 
lblInfo.grid(row = 0, column = 0) 
lblInfo = Label(Tops, font=('arial', 20, 'bold'), text = localtime, fg = "Steel Blue", bd = 10, anchor = 'w')                           
lblInfo.grid(row = 1, column = 0) 
  
File = StringVar()
key = StringVar() 
mode = StringVar() 
Result = StringVar() 
historys=StringVar()
####################exit################################################
def qExit(): 
    root.destroy() 

#################reset###################################################
def Reset(): 
    File.set("") 
    key.set("") 
    mode.set("") 
    Result.set("")

#################################################################### 
def browseFiles(): 
    global filename 
    filename= filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("all files", "*.*"), ("all files", "*.*"))) #("Text files", "*.txt*")
    label_file_explorer.configure(text=filename)

lblReference = Label(f1, font = ('arial', 16, 'bold'),text = "File Name:", bd = 16, anchor = "w")    
lblReference.grid(row = 0, column = 0)
label_file_explorer = Label(f1,  text = "", width = 100, height = 10,  fg = "blue")
label_file_explorer.grid(row = 0, column = 1)

button_explore = Button(f1, font = ('arial', 16, 'bold'),text = "Browse Files", command = browseFiles)  
button_explore.grid(row = 1, column = 0)

lblkey = Label(f1, font = ('arial', 16, 'bold'),text = "KEY", bd = 16, anchor = "w")             
lblkey.grid(row = 2, column = 0) 
txtkey = Entry(f1, font = ('arial', 16, 'bold'), textvariable = key, bd = 10, insertwidth = 4,bg = "powder blue", justify = 'right')          
txtkey.grid(row = 2, column = 1) 
  

lblmode = Label(f1, font = ('arial', 16, 'bold'),text = "MODE(e for encrypt, d for decrypt)",bd = 16, anchor = "w")                             
lblmode.grid(row = 3, column = 0) 
txtmode = Entry(f1, font = ('arial', 16, 'bold'), textvariable = mode, bd = 10, insertwidth = 4,bg = "powder blue", justify = 'right')         
txtmode.grid(row = 3, column = 1) 

lblService = Label(f1, font = ('arial', 16, 'bold'),text = "The Result-", bd = 16, anchor = "w")              
lblService.grid(row = 2, column = 2) 
txtService = Entry(f1, font = ('arial', 16, 'bold'), textvariable = Result, bd = 10, insertwidth = 4,bg = "powder blue", justify = 'right') 
txtService.grid(row = 2, column = 3) 

#hist = Label(f1,  text = "", width = 100, height = 10,  fg = "blue")
#hist.grid(row = 0, column = 3)

txthis = Entry(f1, font = ('arial', 10, 'bold'), textvariable = historys, bd = 5, insertwidth = 4,bg = "powder blue", justify = 'right') 
txthis.grid(row = 0, column = 3) 
############################################################################################################################################################################


def generate_roundkeys(main_key, no_of_rounds):
	roundkeys_array = []
	temp = main_key
	roundkeys_array.append(temp)
	for i in range(no_of_rounds):
		temp = generate_key(temp, i)
		roundkeys_array.append(temp)
	return roundkeys_array

def generate_key(a_key, round):
	
	w0 = a_key[0]
	w1 = a_key[1]
	w2 = a_key[2]
	w3 = a_key[3]
	
	w4 = [w3[1], w3[2], w3[3], w3[0]]
	
	w4=substitute_word(w4)
	
	w4 = xor_word(w4, [RC[round],'00','00','00'])
	w4 = xor_word(w4, w0)
	
	w5 = xor_word(w4, w1)
	
	w6 = xor_word(w5, w2)
	
	w7= xor_word(w6, w3)
	new_key = [w4, w5, w6, w7]
	
	return new_key

def add_round_key (state_matrix, key):
	for i in range(len(state_matrix)):
		w = state_matrix.pop(0)
		k = key[i]
		state_matrix.append(xor_word(w,k))

def substitute_matrix (state_matrix):
	for i in range(len(state_matrix)):
		w = state_matrix.pop(0)
		state_matrix.append(substitute_word(w))

def Inv_substitute_matrix (state_matrix):
	for i in range(len(state_matrix)):
		w = state_matrix.pop(0)
		state_matrix.append(Inv_substitute_word(w))

def shift_row (state_matrix):
	state_matrix = numpy.array(state_matrix).T.tolist()
	state_matrix.append(state_matrix.pop(0))
	w = state_matrix.pop(0)
	w.append(w.pop(0))
	state_matrix.append(w)
	w = state_matrix.pop(0)
	w.append(w.pop(0))
	w.append(w.pop(0))
	state_matrix.append(w)
	w = state_matrix.pop(0)
	w.append(w.pop(0))
	w.append(w.pop(0))
	w.append(w.pop(0))
	state_matrix.append(w)
	state_matrix = numpy.array(state_matrix).T.tolist()
	return state_matrix

def Inv_shift_row (state_matrix):
	state_matrix = numpy.array(state_matrix).T.tolist()
	state_matrix.append(state_matrix.pop(0))
	w = state_matrix.pop(0)
	w.append(w.pop(0))
	w.append(w.pop(0))
	w.append(w.pop(0))
	state_matrix.append(w)
	w = state_matrix.pop(0)
	w.append(w.pop(0))
	w.append(w.pop(0))
	state_matrix.append(w)
	w = state_matrix.pop(0)
	w.append(w.pop(0))
	state_matrix.append(w)
	state_matrix = numpy.array(state_matrix).T.tolist()
	return state_matrix

def substitute_word (word):
	w = []
	for i in word:
		hex = Sbox[stoh_dict[i[0]]][stoh_dict[i[1]]]
		w.append(hex)
	return w

def Inv_substitute_word (word):
	w = []
	for i in word:
		hex = Sbox_inv[stoh_dict[i[0]]][stoh_dict[i[1]]]
		w.append(hex)
	return w


def xor_word(w1, w2):
	ans = []
	for i in range(0, len(w1)):
		s1 = w1[i]
		s2 = w2[i]
		ans.append(hexxor(s1, s2).upper())
	return ans

def hexxor(a, b):
	return "".join(["%x" % (int(x,16) ^ int(y,16)) for (x, y) in zip(a, b)])




def mix_column(state_matrix):
	state_matrix = numpy.array(state_matrix).T.tolist()
	temp = []
	for x in range(0, 4):
		temp.append("")

	for i in range(0, 4):
		for j in range(0, 4):
			temp[j] = state_matrix[j][i]

		single_column(temp)

		for j in range(0, 4):
			state_matrix[j][i] = temp[j]

	beautify(state_matrix)
	
	return (numpy.array(state_matrix).T.tolist())

def Inv_mix_column(state_matrix):
	state_matrix = numpy.array(state_matrix).T.tolist()
	temp = []
	for x in range(0, 4):
		temp.append("")

	for i in range(0, 4):
		for j in range(0, 4):
			temp[j] = state_matrix[j][i]

		Inv_single_column(temp)

		for j in range(0, 4):
			state_matrix[j][i] = temp[j]

	beautify(state_matrix)
	
	return (numpy.array(state_matrix).T.tolist())
			
def single_column(r):

	toHex(r)

	temp = copy.deepcopy(r)

	F = ffield.FField(8,gen=0x11b,useLUT=0)

	r[0] = F.Multiply(temp[0], 2) ^ F.Multiply(temp[1], 3) ^ F.Multiply(temp[2], 1) ^ F.Multiply(temp[3], 1)
	r[1] = F.Multiply(temp[0], 1) ^ F.Multiply(temp[1], 2) ^ F.Multiply(temp[2], 3) ^ F.Multiply(temp[3], 1)
	r[2] = F.Multiply(temp[0], 1) ^ F.Multiply(temp[1], 1) ^ F.Multiply(temp[2], 2) ^ F.Multiply(temp[3], 3)
	r[3] = F.Multiply(temp[0], 3) ^ F.Multiply(temp[1], 1) ^ F.Multiply(temp[2], 1) ^ F.Multiply(temp[3], 2)
	r[0] = hex(r[0]); r[1] = hex(r[1])
	r[2] = hex(r[2]); r[3] = hex(r[3])

def Inv_single_column(r):

	toHex(r)

	temp = copy.deepcopy(r)

	F = ffield.FField(8,gen=0x11b,useLUT=0)

	r[0] = F.Multiply(temp[0], 14) ^ F.Multiply(temp[1], 11) ^ F.Multiply(temp[2], 13) ^ F.Multiply(temp[3], 9)
	r[1] = F.Multiply(temp[0], 9) ^ F.Multiply(temp[1], 14) ^ F.Multiply(temp[2], 11) ^ F.Multiply(temp[3], 13)
	r[2] = F.Multiply(temp[0], 13) ^ F.Multiply(temp[1], 9) ^ F.Multiply(temp[2], 14) ^ F.Multiply(temp[3], 11)
	r[3] = F.Multiply(temp[0], 11) ^ F.Multiply(temp[1], 13) ^ F.Multiply(temp[2], 9) ^ F.Multiply(temp[3], 14)
	r[0] = hex(r[0]); r[1] = hex(r[1])
	r[2] = hex(r[2]); r[3] = hex(r[3])

def toHex(w1):

	for i in range(0, len(w1)):
		st = w1[i]
		w1[i] = '0x' + st
		hex_int = int(w1[i], 16)
		w1[i] = hex_int

def beautify(state_matrix):

	for i in range(0, 4):
		for j in range(0, 4):
			state_matrix[i][j] = state_matrix[i][j][2:].upper()

			if(len(state_matrix[i][j]) == 1):
				state_matrix[i][j] = '0' + state_matrix[i][j]




def encrypt(key,text):
	cypher_bytes = []
	key_bytes = []
	for i in text:
		cypher_bytes.append(format(ord(i),'X'))
	for j in key:
		key_bytes.append(format(ord(j),'X'))
	short = (16-len(cypher_bytes)%16)%16
	for i in range(short):
		cypher_bytes.append('0'+format(short,'X'))

	no_of_blocks = len(cypher_bytes)/16

	block_list = []
	t_list = []
	b_list= []
	for i in range(len(cypher_bytes)):
		t_list.append(cypher_bytes[i])
		if (i+1)%4==0:
			b_list.append(t_list)
			t_list = []
		if (i+1)%16==0:
			block_list.append(b_list)
			b_list=[]

	key_matrix = []
	b_list = []
	for i in range(len(key_bytes)):
		b_list.append(key_bytes[i])
		if(i+1)%4==0:
			key_matrix.append(b_list)
			b_list= []

	roundkeys_array = generate_roundkeys(key_matrix, 10)
	
	final_cyphertext = ""
	for i in range(len(block_list)):
		b = block_list.pop(0)
		add_round_key(b, roundkeys_array[0])
		for j in range(9):
			substitute_matrix(b)
			b=shift_row(b)
			b=mix_column(b)
			add_round_key(b, roundkeys_array[j+1])
		substitute_matrix(b)
		b=shift_row(b)
		add_round_key(b, roundkeys_array[10])
		block_list.append(b)

		for j in b:
			for k in j:
				final_cyphertext = final_cyphertext + k
	return block_list

def decrypt(dec_key, block_list):
	key_bytes=[]
	for j in dec_key:
	  key_bytes.append(format(ord(j),'X'))
	key_matrix = []
	b_list = []
	for i in range(len(key_bytes)):
	  b_list.append(key_bytes[i])
	  if(i+1)%4==0:
	    key_matrix.append(b_list)
	    b_list= []
	roundkeys_array = generate_roundkeys(key_matrix, 10)

	final_decipheredtext=""
	for i in range(len(block_list)):
	  b = block_list.pop(0)
	  add_round_key(b, roundkeys_array[10])
	  b=Inv_shift_row(b)
	  Inv_substitute_matrix(b)
	  for j in range(9):
	  	add_round_key(b, roundkeys_array[9-j])
	  	b=Inv_mix_column(b)
	  	b=Inv_shift_row(b)
	  	Inv_substitute_matrix(b)
	  add_round_key(b, roundkeys_array[0])
	  block_list.append(b)

	  for j in b:
	    for k in j:
	      final_decipheredtext = final_decipheredtext + k
	fin=bytes.fromhex(final_decipheredtext).decode('utf-8')
	#print(fin)
	#print(str(fin))
	#print(int(fin))
	s=""
	for i in str(fin):
		if (i.isdigit()):
			s=s+i
		else:
			break
	return int(s)



def Ref():
	F =str(label_file_explorer.cget("text"))
	k=str(key.get())
	m=mode.get()
	if(m.rfind('e') != -1):
		fin=open(F,'rb')
		image=fin.read()
		fin.close()
		image=bytearray(image)
		with open('data.pickle', 'rb') as f2 :
			data = pickle.load(f2) 
		with open('history.pickle', 'rb') as f3 :
			his = pickle.load(f3)
			if(F not in his.keys()):
				his[F]=[]
		if(F in data.keys()):
			Result.set("file already encrypted")
			his[F].append("Already encrypted: "+str(time.asctime(time.localtime(time.time()))))
			with open('history.pickle', 'wb') as f4 :          
				pickle.dump(his,f4) 
		else:
			block_list=encrypt(k, str(image[0]))
			fin=open(F,'wb')
			image[0]=1
			fin.write(image)
			fin.close()
			data[F]=k, block_list
			his[F].append("Encryption: "+str(time.asctime(time.localtime(time.time()))))

			#data[F][2].append("Encryption: "+str(time.asctime(time.localtime(time.time()))))
			print(data)
			with open('data.pickle', 'wb') as f1 :          
				pickle.dump(data,f1) 
			with open('history.pickle', 'wb') as f4 :          
				pickle.dump(his,f4) 
			Result.set("File encrypted")   

	else:
		fin=open(F,'rb')
		image=fin.read()
		fin.close()
		image=bytearray(image)
		with open('data.pickle', 'rb') as f2: 
			data = pickle.load(f2)
		with open('history.pickle', 'rb') as f3 :
			his = pickle.load(f3)
			if (F not in his):
				his[F]=[]

		if(F in data.keys()):
			if(data[F][0]==k):
				x=decrypt(data[F][0],data[F][1])
				image[0]=x
				fin=open(F,'wb')
				fin.write(image)
				fin.close()
				#his[F].append("Encryption: "+str(time.asctime(time.localtime(time.time()))))
				del data[F]
				with open('data.pickle', 'wb') as f1 :          
					pickle.dump(data,f1) 
				his[F].append("Decryption: "+str(time.asctime(time.localtime(time.time()))))
				Result.set("file decrypted")
				with open('history.pickle', 'wb') as f4 :          
					pickle.dump(his,f4) 
			else:
				Result.set("Wrong key")
				his[F].append("Wrong key: "+str(time.asctime(time.localtime(time.time()))))
				with open('history.pickle', 'wb') as f4 :          
					pickle.dump(his,f4) 

		else:
			Result.set("file already decrypted")
			his[F].append("Already decrypted: "+str(time.asctime(time.localtime(time.time()))))
			with open('history.pickle', 'wb') as f4 :          
				pickle.dump(his,f4) 		

def his():
	F =str(label_file_explorer.cget("text"))
	with open('history.pickle', 'rb') as f2 :
		his = pickle.load(f2)
	s=''
	for i in his[F]:
		s=s+i+"\n"
	historys.set(s)

	#s=s.translate({ord(c): None for c in string.whitespace})cd
	#encrypt(k,s)
####################################################################

btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", font = ('arial', 16, 'bold'), width = 10, text = "Show Message", bg = "powder blue",  command = Ref).grid(row = 7, column = 1)  
btnExit = Button(f1, padx = 16, pady = 8, bd = 16,  fg = "black", font = ('arial', 16, 'bold'),  width = 10, text = "Exit", bg = "red", command = qExit).grid(row = 7, column = 2) 
btnhis = Button(f1, padx = 16, pady = 8, bd = 16,  fg = "black", font = ('arial', 16, 'bold'),  width = 10, text = "history", bg = "red", command = his).grid(row = 7, column = 3)
####################################################################
root.mainloop()