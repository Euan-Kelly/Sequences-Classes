import re

class Sequence:
    def __init__(self,id, seq):
        self._id= id
        self._seq = seq.upper()
        
    @property
    def id(self):
        return self._id 
    
    @property
    def seq(self):
        return self._seq
    
    def __str__(self):
        return (f"sequence ID: {self.id}, seq: {self.seq}({len(self.seq)})")
    
    def make_fasta(self):
        return (f">{self.id}\n{self.seq}\n")
      
class DNAsequence(Sequence):
    
    
        
        
    def translate(self):
             # make a codon table
        bases = "tcag".upper()
        codons = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codon_table = dict(zip(codons, amino_acids))  
        
        AAmerge=""
        for number in range(0,len(self.seq)-2,3):
            codon = self.seq[number: number+3]
            AA = codon_table[codon]
            AAmerge = AAmerge + AA
        return AAmerge
    
    def gc_calc(self, dp=2):
        c_count = self.seq.count('C')
        g_count = self.seq.count('G')
        gc_content = (c_count + g_count) / len(self.seq)
        return round(gc_content, dp)
    
    def protein_seq_lenth(self):
        return len(self.seq)//3
    
    def __len__(self):
        return len(self.seq)

class Protein(Sequence):
                
    def __init__(self, id, seq, desc= "Unknowen"):
        super().__init__(id, seq)
        self._desc = desc
            
    @property
    def desc(self):
        return self._desc
    
    def __iter__(self):
        return (self.seq)
        
                
    def hydrophobic_calc(self,dp=2):
        count = 0
        for aa in self.seq:
            match = re.search(r"[AILMFEYV]", aa)
            if match:
                count = count+1
        hydrophobic_count = (count)/len(self.seq)
        return round(hydrophobic_count, dp)
        
    def protein_seq_lenth(self):
        return len(self.seq)
