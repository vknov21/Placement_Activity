															#*** INSTRUCTIONS TO USE ***#
''' *	 	section .data/.text may or may not be present but 'main:' must be there declared globally in .bss section 								* '''
''' * 		there should not anything between main: and the last section .sth which doesn't belong to that section itself						 	* '''
''' * 		Code will start executing from the position where it either finds any section .sth.. .bss is compulsory for code to run 				* '''
''' * 		The Code is still incomplete but works individually. Translation is working fine but may not give the result for many cases yet			* '''
''' * 		Error are most the way interactive but still not worked on all the types of errors if it could handle 									* '''

err=0
size=0
cntline=0
cnt=0
register={"eax":0,"ebx":3,"ecx":1,"edx":2, "esp":4,"ebp":5,"esi":6,"edi":7}			#Registers allowed by program
opcode={"mov":(3),"add":(3),"sub":(3),"mul":(2,3),"div":(2,3),"cmp":(3),"jmp":(2),"call":(2)}
bss={"resd":4,"resb":1}
text=["global","extern"]
data={"dd":4,"db":1}
types=[str,int,float]
labels={}
addLabel={}
litDict={}
symDict={}
mainp=0
nums=1

def errorCheck(word,txt):
	global err
	#-------------------------------		TEXT		-----------------------------------#
	if txt=="text" and len(word)==2 and err!=1:												#checking for definitions provided under 'section .text'
		#global main, #extern var
		if word[0] in text:										#Only extern and global permissible
			if len(word)!=2:									#Two words compulsorily needed
				err=1
				print("file.asm (line : %d) : " %cntline),
				print("Only one Label is allowed")
				exit()
			elif not word[1][0].isalpha():						#The label should start with alphabet
				err=1
				print("file.asm (line : %d) : " %cntline),
				print("First letter should only be Alphabet")
				exit()
		else:													#if neither global nor extern is first word
			err=1
			print("file.asm (line : %d) : " %cntline),
			print(".text can have 'Global' or 'Extern' only")
			exit()
			
	#-------------------------------		BSS 		-----------------------------------#	
	elif txt=="bss" and len(word)>=3 and err!=1:											#checking for definitions under 'section .bss'
			#a resd 10, #b resb 20
		if len(word)!=3:										#Count of words should be three
			err=1
			print("file.asm (line : %d) : " %cntline),
			print("Only three words are permitted")
			exit()
		elif not word[0][0].isalpha():							#Label should start with alphabet
			err=1
			print("file.asm (line : %d) : " %cntline),
			print("First letter should only be Alphabet")
			return
		elif word[1] not in bss.keys():							#'resd' and 'resb' are allowed
			err=1
			print("file.asm (line : %d) : " %cntline),
			print("'resd' or 'resb' is expected")
			return
		elif type(eval(word[2]))!=str or type(eval(word[2]))!=int:	#Either a string value to be stroed in variable or should be int
			err=1
			print("file.asm (line : %d) : " %cntline),
			print("attempt to reserve non-constant quantity of BSS space")
			return
		word=word[2:]												#Taking value assigned to variable
		line=' '.join(word)
		word=line.replace(',',' ')
		word=word.split()
		try:
			map(type,map(eval,word))
		except:
			print("file.asm (line : %d) : " %cntline),
			print("Wrong Format1")
			err=1
			return
		else:
			err=0
			
	#-------------------------------		DATA		-----------------------------------#
	elif txt=="data" and len(word)>=3 and err!=1:											#checking for definitions under 'section .data'
		#a dd 30,10, #b db 10
		if not word[0][0].isalpha():								#Label should start with Alphabet
			err=1
			print("file.asm (line : %d) : " %cntline),
			print("First letter should only be Alphabet")
			return
		elif word[1] not in data.keys():							#Either 'dd' or 'db' should be permitted
			err=1
			print("file.asm (line : %d) : " %cntline),
			print("'dd' or 'db' is expected")
			return													
		word=word[2:]												#Value stored in variables are taken only
		line=' '.join(word)
		word=line.replace(',',' ')
		word=word.split()
		try:														#To check whether the value is string or int... if some alphabet came not in format of string then it will be treated as unassigned variable or format not recognised
			map(type,map(eval,word))
		except:
			print("file.asm (line : %d) : " %cntline),
			print("Wrong Format2")
			err=1
			return
		#-------------------------------		 AFTER		-----------------------------------#
	elif txt=="after" and len(word)>=1 and err!=1:					#Checking for main definition of program
		if not word[0] in opcode.keys() and ':' not in word[0]:		#first word either label (ends with ':') or any opcode
			print("file.asm (line : %d) : " %cntline),
			err=1
			print("Opcode is expected")
		elif word[0] or word[1] in opcode.keys():					
			if word[0] or word[1] in ["mov","sub","add","cmp"]:
				errMov(word)										#For three word line cases of opcode statement error check
			elif word[0] or word[1] in ["mul","div"]:
				errMul(word)										#For two word line cases of opcode statement error check
			elif word[0] or word[1] in ["jmp","inc","call"]:
				errJump(word)										#For one word line cases of opcode statement error check
		else:
			err=1
			print("file.asm (line : %d) : " %cntline),
			print("Format Error")							#Neither Label nor Opcode
	
	else:
		err=1														#Length is 0 or error is there
		print("file.asm (line : %d) : " %cntline),
		print("Wrong Format3")
		exit()

def errMov(word):
	global err
	if ':' in word[0] and word.count(':')==1:						#Checking Format ''opcode reg/dword reg/dword/imm''
		if word[0][0].isalpha():
			word=word[1:]
	line=' '.join(word)
	if(word.count(',')==1):
		word=line.replace(',',' ')
		word=line.split()
		if(len(word)==3):
			if word[0] in opcode.keys():
				word=word[1:]
				if word[0] in register.keys():
					err=0
				elif word[0][:6]=="dword[" and word[0][-1]=="]":	#allowed dword[] syntax just after opcode
					word=word[0][6:-1]
					if ',' or '.' or ':' or '[' or ']' not in word:	#special symbols are not allowed
						line=' '.join(word)
						if line.count('+')<=1:
							if '*' not in word:
								word=line.split('+')
								if word[0] and word[1] in opcode.keys:
									None
								else:
									err=1
									print("file.asm (line : %d) : " %cntline),
									print("Wrong Format4")
							else:
								word=line.replace('+',' ')
								word=line.replace('*',' ')
								word=line.split()
								for i in range(0,len(word)):
									if type(eval(word[i]))==int:
										num=num*eval(word[i])
								if(num!=1 or 2 or 4 or 8):
									err=1
									print("file.asm (line : %d) : " %cntline),
									print("Wrong Format5")
					else:
						err=1
				elif word[1][:6]=="dword[" and word[1][-1]=="]":	#allowed dword[] syntax of last word
					word=word[1][6:-1]
					if ',' or '.' or ':' or '[' or ']' not in word:	#special symbols are not allowed
						line=' '.join(word)
						if line.count('+')==1:
							if '*' not in word:
								word=line.split('+')
								if word[0] and word[1] in opcode.keys:
									None
								else:
									err=1
									print("file.asm (line : %d) : " %cntline),
									print("Wrong Format6")
							else:
								word=line.replace('+',' ')
								word=line.replace('*',' ')
								word=line.split()
								for i in range(0,len(word)):
									if type(eval(word[i]))==int:
										num=num*eval(word[i])
								if(num!=1 or 2 or 4 or 8):
									err=1
									print("file.asm (line : %d) : " %cntline),
									print("Wrong Done")
						else:
							print("file.asm (line : %d) : " %cntline),
							print("Limit exceed")
							err=1
					else:
						print("file.asm (line : %d) : " %cntline),
						print("Syntax Error")
						err=1
				elif type(eval(word[0]))==int:
					None
				else:
					print("file.asm (line : %d) : " %cntline),
					print("Wrong Syntax")
					err=1
			else:
				None
		else:
			err=1
			print("file.asm (line : %d) : " %cntline),
			print("Spaces Exceeds")
	else:
		print("file.asm (line : %d) : " %cntline),
		print("',' Separator is needed")
		err=1				#Separator ',' is needed

def errMul(word):													#Checking format ''opcode reg/imm''
	if ':' in word[0] and word.count(':')==1:
		if word[0][0].isalpha():
			word=word[1:]
	if(len(word)==3):
		errMov(word)
	if err==0:
		if(len(word)==2):
			word[1:1]=["eax"]										#Becomes same as errMov form of words length 3
			errMov(word)

def errJump(word):													#Checking Format ''inc reg'' or ''jmp Label''
	if ':' in word[0] and word.count(':')==1:
		if word[0][0].isalpha():
			word=word[1:]
	if word[0] in opcode.keys():
		if word[1].count(':')==1 and word[1][-1]==':':
			None
		else:
			print("file.asm (line : %d) : " %cntline),
			print("Syntax Error")
			err=1
	else:
		err=1
		print("file.asm (line : %d) : " %cntline),
		print("Syntax Error")

def literalTable(word,txt):										#Collecting labels and creating a literal table file
	translate=[]
	lit=open("LiteralTable.txt","a+")
	if txt=="text":
		if word[1] not in litDict.keys():
			if word[0]=="global":
				litDict[word[1]]="ext"
			elif word[0]=="extern":
				litDict[word[1]]="glo"
		elif litDict[word[1]]!=word[0][0:3]:
			err=1
			print("file.asm (line : %d) : " %cntline),
			print("Cannot define Again")
		return
	
	elif txt=="bss" or txt=="data":
		if word[0] not in litDict.keys():
			if txt=="bss":
				litDict[word[0]]="bss"
			else:
				litDict[word[0]]="data"
			liter=word[0]
			word=word[2:]
			if '"' in line:
				line=' '.join(word)
				word=line.split('"')
				word=word[1:]
				word[1]=word[1].split(',')
				word[1:]=word[1]
				word[1:2]=[]										#Separating string and integers data
			else:
				word=line.split()
			if type(eval(word[0]))==str:
				for i in range(0,len(word)):
					lit.write("%s " %word[i])
			for i in range(0,len(word)):
				if type(word[i])==str:
					for j in range(0,len(word[i])):
						translate=translate+[hex(ord(word[i][j]))[2:]]		#Translating into hex of the values and storing in Literal Table
				else:
					translate=translate+[hex(ord(eval(word[i][j])))[2:]]
			translate=''.join(translate)	
			lit.write("%d\t%s\t%s" %(size,liter,translate))
		else:
			print("file.asm (line : %d) : " %cntline),
			print("Cannot declare again")
			err=1

def opcodeTable(word,txt):
	if word[0][-1]==':':
		addLabel[word[0][0:-1]]=size
		word=word[1:]
	if len(word)>0:
		mod="-"
		wide=0
		litTbl=open("Literal Table.txt","a+")
		if word[1] in register.keys() and word[1][0]!="j":
			lt0="reg"
			wide=1
		elif word[1][0:5]=="dword":
			lt0="dword"
			wide=1
		elif word[1][0]=="j":
			None
		if len(word[2])>0:	
			if word[2] in register.keys():
				lt1="reg"
				mod="mod"
				wide=2
			elif word[2][0:5]=="dword":
				lt1="dword"
				wide=2
			elif type(eval(word[2]))==int:
				lt1="imm"
				wide=5
#		litTbl.write("%s\t%d\t%s\t%s\t%s\t%d\t%d\n" %(word[0],len(word[1:]),lt0,lt1,mod,'''yet to decide''',

def symbolTable(word,txt):
	cnt=cnt+1
	lit=open("LiteralTable.txt","r")
	symTbl=open("SymbolTable.txt","a+")
	litLine=lit.readline()
	litChar=litLine.split()

	if txt=="text":
		if word[0]=="global":
			symDict[word[1]]="gU"
		elif word[0]=="extern":
			symDict[word[1]]="U"
		symTbl.write("%d\t%s\t%s\tt\t-\t-\t%s\n" %(cnt,word[1],cnt,symDict[word[1]]))

	elif txt=="data":
		ds=0
		size=0
		if word[1] in data.keys():
			symDict[word[0]]="D"
			ds=data[word[1]]
		word=word[2:]
		line=' '.join(word)
		if '"' in line:
			word2=line.split('"')
		word=word2[2:]
		line=' '.join(word)
		word=line.split(',')
		ds=(len(word2)+len(word)-1)*ds
		size=size+ds
		symTbl.write("%d\t%s\t%d\t%s\t%d\t%d\t%s" %(cnt,word[0],size,"d",ds,len(word),symDict[word[0]]))

	elif txt=="bss":
		ds=0
		size=0
		for i in range(0,len(word)):
			if "\"" in word[i]:
				print("file.asm (line : %d) : " %cntline),
				print("String are yet not allowed in BSS")
				err=1
				return
		if word[1] in bss.keys():
			symDict[word[0]]="D"
			k=bss[word[1]]
		word=word[2:]
		line=' '.join(word)
		line=line.replace(',',' ')
		word=line.split()
		for i in range(0,len(word)):
			ds=ds+k*eval(word[i])
		size=size+ds			#Take care of String constant
		symTbl.write("%d\t%s\t%d\t%s\t%d\t%d\t%s" %(cnt,word[0],size,"b",ds,len(word),symDict[word[0]]))

	elif txt=="after":
		if word[0][-1]==':':
			if word[0:-1] not in labels:
				labels[word[0:-1]]="U"
			elif labels[word[0:-1]]=="U":
				err=1
				print("file.asm (line : %d) : " %cntline),
				print("Cannot define again")
			elif labels[word[0:-1]]=="U1":
				labels[word[0:-1]]="D"
		
	#	symTbl.write("%d\t%s\t%d\t%s\t%d\t%d\t%s" %(cnt,word[0],

def displayError():
	exit()

if __name__=="__main__":
	symtbl=open("file.asm","r")									#Opening ASM file to read
	line="starting..."
	cntline+=1													
	lists=["section .data","section .text","section .bss"]		#Memory allocating "sections"
	while "main:" not in line:					#Assumed before main:, sections will be defined having memories of variable
		line=symtbl.readline()
		line=line.strip('\t')
		line=line.strip('\n')
		word=line.split()
		if line in lists:
			if line=="section .text" and "main:" not in line:	#if any section is matched its corresponding variable is stored with UNDEF
				size=0
				cntline+=1
				while word not in lists:
					line=symtbl.readline()
					line=line.strip('\t')
					line=line.strip('\n')
					word=line.split()
					cntline+=1
					if line=='' or line=="main:":
						break
					else:
						err=errorCheck(word,"text")				#finding any error.. if found just terminate and reflect error
						symDict[word[1]]="U"
						if err==0:
							literalTable(word,"text")			#Values of symbol generation function
							symbolTable(word,"text")			#Generating the variables symbol table
						else:
							displayError()						#Displaying error and terminate
						if line=="global main":					#Searching for global main declaration
							mainp=1								#If present, flag set to 1
							symDict["main"]='U'					#Dictionary of symbols in sections
			if line=="section .bss" and "main:" not in line:
				size=0
				cntline+=1
				while word not in lists:
					line=symtbl.readline()
					line=line.strip('\t')
					line=line.strip('\n')
					word=line.split()
					cntline+=1
					if line=='' or line=="main:":
						break
					else:
						err=errorCheck(word,"bss")
						symDict[word[0]]="U"
						if err==0:
							literalTable(word,"bss")
							symbolTable(word,"bss")
						else:
							displayError()
							exit()
			if line=="section .data" and "main:" not in line:
				size=0
				cntline+=1
				while word not in lists:
					line=symtbl.readline()
					line=line.strip('\t')
					line=line.strip('\n')
					word=line.split()
					cntline+=1
					if line=='' or line=="main:":
						break
					else:
						err=errorCheck(word,"data")
						symDict[word[0]]="U"
						if err==0:
							literalTable(word,"data")
							symbolTable(word,"data")
						else:
							displayError()
			
			
	if "main:" in word:											#Assuming from main: the program will be present
		size=0
		if mainp==1:
			symDict["main"]="d"									#Main is defined if it was defined in section .text before 
			while line!='':
				line=symtbl.readline()
				line=line.strip('\t')
				line=line.strip('\n')
				word=line.split()
				if "main:" in word:
					err=1
					print("file.asm (line : %d) : " %cntline),
					print("Cannot redefine main")
				err=errorCheck(word,"after")
				if err==0 and len(word)!=0:
					opcodeTable(word,"after")
					symbolTable(word,"after")
				elif len(word)==0:
					continue
				if err==1:
					displayError()
					exit()
		else:
			print("main: Label not Defined globally")
	if err==0:
		print("Successful")
