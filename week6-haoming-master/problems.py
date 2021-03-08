import re

def problem1(searchstring):
    """
    Match phone numbers.

    :param searchstring: string
    :return: True or False
    """
    p1 = re.compile(r'\(\d\d\d\)\s\d\d\d\-\d\d\d\d')
    p2 = re.compile(r'\d\d\d\-\d\d\d\-\d\d\d\d')
    p3 = re.compile(r'\d\d\d\-\d\d\d\d')

    if (p1.match(searchstring) or p2.match(searchstring) or p3.match(searchstring)) :
        return True 
    else :
        return False
        
def problem2(searchstring):
    """
    Extract street name from address.

    :param searchstring: string
    :return: string
    """
    p = re.compile(r'[0-9]+\s+(([A-Z][a-z]* )+)(Ave.|St.|Dr.|Rd.)')
    searchstring = p.search(searchstring).group(1)
    return searchstring
    
def problem3(searchstring):
    """
    Garble Street name.

    :param searchstring: string
    :return: string
    """
    p = re.compile(r'([0-9]+) (([A-Z][a-z]* )+)(Ave.|St.|Dr.|Rd.)')
    searchstring = p.sub(p.search(searchstring).group(1) + " " + (p.search(searchstring).group(2)[:-1])[::-1] + " " + p.search(searchstring).group(4), searchstring)
    return searchstring


if __name__ == '__main__' :
    print(problem1('765-494-4600')) #True
    print(problem1(' 765-494-4600 ')) #False
    print(problem1('(765) 494 4600')) #False
    print(problem1('(765) 494-4600')) #True    
    print(problem1('494-4600')) #True
    
    print(problem2('The EE building is at 465 Northwestern Ave.')) #Northwestern
    print(problem2('Meet me at 201 South First St. at noon')) #South First
    
    print(problem3('The EE building is at 465 Northwestern Ave.'))
    print(problem3('Meet me at 201 South First St. at noon'))
