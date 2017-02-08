global words

def word_count(words):
  word_list = words.strip.replace("\n", " ").split()
  
  dictionary_result = {}
  
  for word in word_list:
    dictionary_result[word] += 1
    if word not in dictionary_result:
      dictionary_result[word] = 1
      
  return dictionary_result
      
  
