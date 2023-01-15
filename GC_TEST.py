def GCcount(seq):
    seq=seq.lower()
    gcount=seq.count("g")
    ccount=seq.count("c")
    
    return gcount+ccount
    
    
def test_gc_count():
    assert GCcount("g")==1 
    assert GCcount("cG")==2
    assert GCcount("gatcgtATGCC")==6
    
    
