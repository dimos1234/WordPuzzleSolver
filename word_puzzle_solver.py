f=open('words_alpha.txt','r')

onelist=[]
twolist=[]
threelist=[]
fourlist=[]
fivelist=[]
sixlist=[]
sevenlist=[]
eightlist=[]
ninelist=[]
tenlist=[]
elevenlist=[]
twelvelist=[]
thirteenlist=[]
fourteenlist=[]
fifteenlist=[]

big_lis=[
onelist,
twolist,
threelist,
fourlist,
fivelist,
sixlist,
sevenlist,
eightlist,
ninelist,
tenlist,
elevenlist,
twelvelist,
thirteenlist,
fourteenlist,
fifteenlist
]

num_of_letters=0

letters=input('enter your letters\n')

for line in f:
	correct=[]
	for letter in letters:
		if letter in line.rstrip():
			correct.append(letter)
		if len(correct)==len(line.rstrip()):
			if len(correct)==1:
				onelist.append(line)
			if len(correct)==2:
				twolist.append(line)
			if len(correct)==3:
				threelist.append(line)
			if len(correct)==4:
				fourlist.append(line)
			if len(correct)==5:
				fivelist.append(line)
			if len(correct)==6:
				sixlist.append(line)
			if len(correct)==7:
				sevenlist.append(line)
			if len(correct)==8:
				eightlist.append(line)
			if len(correct)==9:
				ninelist.append(line)
			if len(correct)==10:
				tenlist.append(line)
			if len(correct)==11:
				elevenlist.append(line)
			if len(correct)==12:
				twelvelist.append(line)
			if len(correct)==13:
				thirteenlist.append(line)
			if len(correct)==14:
				fourteenlist.append(line)
			if len(correct)==15:
				fifteenlist.append(line)

for lis in big_lis:
	num_of_letters+=1
	print(f'\n\n\n\n{num_of_letters} letter words:\n')
	for word in lis:
		print(word)



f.close()