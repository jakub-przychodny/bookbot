def calculate_num_of_words(content):    
    words = content.split()
    return len(words)
    
def calculate_num_of_characters(content):    
    result = {}
    
    for character in content:
        char = character.lower()
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
            
    return result

def sort_on(items):
    return items["num"]

def sort_characters(characters):
    result = []
    
    for character in characters:
        result.append({
            "char": character,
            "num": characters[character]
        })
    result.sort(reverse=True,key=sort_on) 
    return result