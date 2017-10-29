def mutate_string(string, position, character):
    list_var=list(string)
    list_var[position]=character
    str_var=''.join(list_var)
    return str_var
