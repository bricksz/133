def translate():
    global word
    word = userInput.get()
    if word in translations:
        answer['text'] = '{0} = {1}'.format(word, translations[word])
    else:
        userInput.setPrompt('Enter translation for {0}'.format(word))
        userInput.setActionText('Save')
        userInput.setAction(save)
        answer['text'] = ''

def save():
    translations[word] = translations
    input('Enter word:')

word = ''
translations = {}
