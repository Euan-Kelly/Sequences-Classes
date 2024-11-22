#from sequences import Protein, DNAsequence

class Fasta_Splitter:
    def __init__ (self, file):
        self._file = file
        
    @property
    def file(self):
        return self._file 
     
      
    def readFasta(self, sequence_Class):
        with open (self.file) as input:
            for line_in_fasta in input:
                if line_in_fasta.startswith(">"):
                    seqname = line_in_fasta[1:]
                    seqname = seqname.rstrip()
                        
                    line_in_fasta = next(input)  
                    sequence = line_in_fasta
                    sequence = sequence.rstrip()
                yield sequence_Class(seqname,sequence)
                    
