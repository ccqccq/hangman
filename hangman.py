import re


def guess_next_letter(pattern, used_letters=[], word_list=[]):
    """Returns a letter from the alphabet.
    Input parameters:
				pattern: current state of the game board, with underscores "_" in the
            places of spaces (for example, "____e", that is, four underscores
            followed by 'e').
        used_letters: letters you have guessed in previous turns for the same
            word (for example, ['a', 'e', 's']).
        word_list: list of words from which the game word is drawn.
    """
    # match word in word_list. using regular expressions
    reg = re.compile('^' + pattern.replace('_','.') + '$')
    match_word_list = [word for word in word_list if reg.match(word)]

    # string join
    match_word_str = ''
    match_word_str = match_word_str.join(match_word_list)

    # get wordlist set (Filter duplicate letters)
    match_word_set = set(list(match_word_str))

    # delete used_letters
    match_word_set = match_word_set - set(used_letters)

    # delete pattern letter
    match_word_set = match_word_set - set(list(pattern.replace('_','')))

    # get the number of letter occurrences
    letters_set = {x:match_word_str.count(x) for x in match_word_set}
    #print(letters_set)
    
    # sort by occurrences
    letters_sort_list = sorted(letters_set.items(), key=lambda x:x[1], reverse=True)
    #print(letters_sort_list[0][0])
    
    # return first letter
    return letters_sort_list[0][0]


def test_function_should_return_boun():
	pattern = "a____d"
	used_letters = list("ad")
	word_list = ['about', 'abound', 'abandon', 'something']
	assert guess_next_letter(pattern, used_letters, word_list) is not None


def test_function_should_return_bou():
	pattern = "____t"
	used_letters = list("t")
	word_list = ['about', 'abound', 'abandon', 'something']
	assert guess_next_letter(pattern, used_letters, word_list) is not None


def test_function_should_return_omthing():
	pattern = "s__e_____"
	used_letters = list("se")
	word_list = ['about', 'abound', 'abandon', 'something']
	assert guess_next_letter(pattern, used_letters, word_list) is not None

def test_function_should_return_rv():
	pattern = "______e"
	used_letters = list("e")
	word_list = ['stomach','receive','freedom','natural','observe']
	assert guess_next_letter(pattern, used_letters, word_list) is not None

# call test function
test_function_should_return_boun()
test_function_should_return_bou()
test_function_should_return_omthing()
test_function_should_return_rv()