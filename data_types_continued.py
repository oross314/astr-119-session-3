#string

s="I am a string"
print(type(s))				#will say str

#boolean

yes = True					#boolean True
print(type(yes))			

no = False					#Boolean false
print(type(no))

#List -- ordered and changeable

alpha_list =["a","b","c"]		#list initialization
print(type(alpha_list))			#will say tuple				if this is a tuple why can you cnage
print(type(alpha_list[0]))		#will say string					review
alpha_list.append("d")			#will add "d" to the list end
print(alpha_list)				#will print list

#Tuple -- ordered and unchangeable

alpha_tuple = ("a","b","c")		#tuple initialization
print(type(alpha_tuple))		#will say tuple

try:
	alpha_tuple[2]= "d"			#won't work and will raise Type Error
except TypeError:
	print("We can't add elements to tuples!")  #print this message
print(alpha_tuple)