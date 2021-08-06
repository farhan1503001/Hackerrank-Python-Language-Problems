def html_tag_generator(opentag,endtag):
    def decorator(func):
        def wrapper(*args,**kwargs):
            msg=func(*args,**kwargs)
            return "{}{}{}".format(opentag,msg,endtag)
        return wrapper
    return decorator
@html_tag_generator('<i>','</i>')
def printer(word):
    return word
@html_tag_generator('<b>','</b>')
def bolder(word1):
    return word1
@html_tag_generator('<div>','</div>')
def divider(word,word1):
    return '\n{}\n{}\n'.format(printer(word),bolder(word1))
if __name__=='__main__':
    word=input('Enter the word: ')
    word1=input('Enter word:')
    print(printer(word))
    print(bolder(word1))
    print(divider(word,word1))
