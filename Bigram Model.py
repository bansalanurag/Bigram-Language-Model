words=[]
bigram_words=[]
bigram_tags=[]
wordandtag=[]
tags={'<s>':1}
p_tags={}
f = open('new 3.txt','r')
data = f.readlines();

first = '<s>'
total_tags=0

# Individual words &  Individual Tags
for i in range(0,len(data)-1):		
	line1=data[i]
	ia= line1.find("\t")
	sa= line1.find("\n")	
	
	tempa = line1[:ia]
	temp1a = line1[ia+1:sa]
	
	if(temp1a == ''):
		temp1a = '<s>'
	if(temp1a == '.'):
		temp1a = '</s>'
	
	if(not(temp1a in tags)):
		tags[temp1a] = 1
	else:
		val = tags.get(temp1a)
		val=val+1
		tags[temp1a] = val
	
	if(tempa=='' or tempa=='.'):
		continue		
	words.append(tempa)
val = tags.get('</s>')
val=val+1		
tags['</s>'] = val

#Bigram - words	
for i in range(0,len(data)-1):		
	line1=data[i]	
	line2=data[i+1]
		
	ia= line1.find("\t")
	ib= line2.find("\t")	
	
	tempa = line1[:ia]
	tempb = line2[:ib]
	
	if(tempa==''):
		tempa='<s>'	
	if(tempb==''):
		tempb='</s>'	
	
	if(tempa=='.'):
		continue
	if(tempb=='.'):
		tempb='</s>'
	
	if(i==0):
		bigram_words.append([first,tempa])
		bigram_words.append([tempa,tempb])
	else:
		bigram_words.append([tempa,tempb])

#Bigram - tags Tagj given Tagi
for i in range(0,len(data)-1):			
	line1=data[i]	
	line2=data[i+1]
	
	ia= line1.find("\t")
	sa= line1.find("\n")
	ib= line2.find("\t")	
	sb= line2.find("\n")	
	
	tempa = line1[ia+1:sa]
	tempb = line2[ib+1:sb]
	
	if(tempa==''):
		tempa='<s>'	
	if(tempb==''):
		tempb='</s>'	
	
	if(tempa=='.'):
		continue
	if(tempb=='.'):
		tempb='</s>'
	
	if(i==0):
		bigram_tags.append([first,tempa])
		bigram_tags.append([tempa,tempb])
	else:
		bigram_tags.append([tempa,tempb])
	
#wordandtag
for i in range(0,len(data)-1):			
	line1=data[i]
	
	ia= line1.find("\t")
	sa= line1.find("\n")
	
	tempa = line1[:ia]
	tempb = line1[ia+1:sa]	
	
	if(tempa=='.' or tempa=='\n' or tempa==''):
		continue	
	wordandtag.append([tempa,tempb])
		
for i in tags:
	total_tags = total_tags + tags[i]

	p_tags = tags.copy()
for i in p_tags:
	p_tags[i] = p_tags[i]/total_tags
	p_tags[i] = float("{0:0.5f}".format(p_tags[i]))

#A matrix
a_size = len(tags.keys())
a_matrix = [[0 for j in range(a_size)] for i in range(a_size)]

i=0
for key in tags:
	f_tag = key
	j=0
	for key in tags:
		s_tag = key
		num = bigram_tags.count([f_tag,s_tag]) + 1
		den = tags[s_tag] + a_size
		a_matrix[i][j] = round(num/den,4)
		j = j+1
	i = i+1	

#B matrix
b_row_size = len(tags.keys())
b_col_size = len(words)
b_matrix = [[0 for j in range(b_col_size)] for i in range(b_row_size)]

i=0
for key in tags:
	s_tag = key
	j=0
	for w in words:
		f_tag = w
		num = wordandtag.count([f_tag,s_tag]) + 1
		den = tags[s_tag] + b_row_size
		b_matrix[i][j] = round(num/den,4)
		j = j+1
	i = i+1	

print(bigram_tags)
print("\n")	
print(bigram_words)
print("\n")	
print(a_matrix)
print("\n")
print(b_matrix)









