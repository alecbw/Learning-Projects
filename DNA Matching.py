"""Context: A spy deleted important files from a computer. There were a few witnesses at the scene of the crime, but no one is sure who exactly the spy was. Three possible suspects were apprehended based on surveillance video. Each suspect had a sample of DNA taken from them. The computer's keyboard was also swabbed for DNA evidence and, luckily, one small DNA sample was successfully retrieved from the computer's keyboard.

Given the three suspects' DNA and the sample DNA retreived from the keyboard, it's up to you to figure out who the spy is!

The project should have methods for each of the following:

* Given a file, read in the DNA for each suspect and save it as a string
* Take a DNA string and split it into a list of codons
* Iterate through a suspect's codon list to see how many of their codons match the sample codons
* Pick the right suspect to continue the investigation on"""

# the sample reflects what was 'found' on the keyboard
sample = ['GTA','GGG','CAC']

def read_dna(dna_file):
  dna_data = ""
  # we're using f as short for file, because file is a keyword in python
  with open(dna_file, "r") as f:
    for line in f:
      dna_data += line
  return dna_data
	# this function as a whole opens the suspects dna files
  # writes their dna_data line by line
  # and auto-closes the files 

def dna_codons(dna):
  codons = []
  for i in range(0, len(dna), 3):
    # checks iterator i doesn't exceed length of dna
    if (i+3) < len(dna):
      codons.append(dna[i:i+3])
  return codons 
	# this function slices the raw dna into 3 character codons and adds them to the list 'codons'

def match_dna(dna):
  matches = 0
  for codon in dna: 
    if codon in sample:
    	matches += 1
  return matches 

def is_criminal(dna_sample):
  sample_number = dna_sample[7]
  print "For Suspect #" + str(sample_number) + ":"
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print str(num_matches) + " codons matches have been found."
    print "Therefore, the suspect must be guilty. \n"
  else:
    print "There are " + str(num_matches) + " codons matches, so the investigation must continue. \n"
  
is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")
