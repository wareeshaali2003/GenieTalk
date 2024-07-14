"""hi,this module serves to display every single item in a list,a list within a list,alist within a list within a list and even more.enjoy"""
def display(sth):
    """you will need to swap "sth" with ur own list name:P"""
    for each_item in sth:
        if isinstance(each_item,list):
            display(each_item)
        else:
            print(each_item)
            
