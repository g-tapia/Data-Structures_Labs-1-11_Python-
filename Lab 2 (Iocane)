def record_guess(pattern_dict, pattern, guess):
    """Updates the `pattern_dict` dictionary by either creating a new entry
    or updating an existing entry for key `pattern`, increasing the count 
    corresponding to `guess` in the list."""
    dictionary=pattern_dict
    if int(guess)==1:
        dictionary.setdefault(pattern, [0,0])
        a=dictionary.get(pattern,[])
        a[0]=a[0]+1
    if int(guess)==2:
        dictionary.setdefault(pattern,[0,0])
        a=dictionary.get(pattern,[])
        a[1]=a[1]+1
        
def next_placement(pattern_dict, pattern):
    dictionary=pattern_dict
    a='1'
    b='2'
    if dictionary=={}:
        return b
    temp=dictionary.setdefault(pattern,[0,0])
    f=int(temp[0])
    g=int(temp[1])
    if f==g and pattern in dictionary:
        return b
    if (pattern in dictionary)==False:
        return b
    if f>g and pattern in dictionary:
        return b
    if f<g and pattern in dictionary:
        return a
    else:
        return b
    
 def play_interactive(pattern_length=4):
    pattern = ''
    poison_position = ''
    userGuess = ''
    userPatternGuess = 0
    patternDictionary = {}
    userPatternList = []
    score = [0,0]
    while True:
        userGuess=input('Where is the iocane powder: my cup (1) or yours (2):')
        userPatternGuess=int(userGuess)
    
        if 1 < userPatternGuess > 2 :
            break
    
        userPatternList.append(userGuess)
        poison_position=next_placement(patternDictionary,pattern)
    
        if len(pattern)==pattern_length:
            pattern=pattern[1:]
        
        for x in range(0,len(userPatternList)-1):
            pattern=pattern+userPatternList[x]
            poison_position=next_placement(patternDictionary,pattern)
            record_guess(patternDictionary, pattern,userGuess)
            userPatternList.pop(0)
        if (poison_position==userGuess):
            score[1]=score[1]+1
            print('Good guess! Ack! I drank the poison')
            print('You died', score[0], 'times, and I drank the poison', score[1],'times')
        if (poison_position != userGuess):
            print('Wrong! Ha! Never bet against a Sicilian!')
            score[0] = score[0] + 1
            print('You died', score[0], 'times, and I drank the poison ', score[1], 'times')
            
play_interactive(3)




def play_batch(guesses, pattern_length=4):
    poison_position=''
    pattern=''
    patternDictionary={}
    guessPatternList=[]
    score=[0,0]
    guesses=list(guesses)
    
    for i in range(0,len(guesses)):
        p=guesses[i]
        guessPatternList.append(p)
        poison_position=next_placement(patternDictionary, pattern)
        
        if len(pattern) == pattern_length:
            pattern = pattern[1:]
            
        for x in range(0,len(guessPatternList)-1):
            pattern=pattern+guessPatternList[x]
            poison_position=next_placement(patternDictionary,pattern)
            record_guess(patternDictionary,pattern, p)
            guessPatternList.pop(0)
        
        if(poison_position == p):
            score[0]=score[0]+1
        if(poison_position != p):
            score[1]=score[1]+1
    return(score[0],score[1])
