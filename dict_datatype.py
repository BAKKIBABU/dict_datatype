# what is dict? dict is combination of key value pair 
# a={}
# print(type(a))    # class 'dict'
# a={45} 
# print(type(a))       # class 'set'
# a={45:'python'}
# print(a)               # {45:'python'}
# print(a(45))             #TypeError:'dict' object is not callable
# print(a[45])              # python
# print(type(a))        # class 'dict'
# book={
    # 1:"python programming",
    # 2:"core python programming",
    # 3:"advance python programming"
# }
# print(book[1])      # "python programming"
# print(book[2])    # "core python programming"
# print(book[3])    # "advance python programming"
# print(book(10))     #TypeError: 'dict' object is not callable   
# print(book[10])      #keyError: 10
# h={1:"",2:"python",3:7,4:6.2,
# 5:[1,4],6:(4,3),7:{1,2},
# 8:{3:"world"}
# }
# print(h[1],type(h[1]))       # class "str"
# print(h[2],type(h[2]))         # class "str"
# print(h,type(h))               # class "dict"
# print(h.keys())                #dict_keys ([1,2,3,4,5,6,7,8])
# print(h.values())               #dict_values(["",'python',7,6.2,[1,4],(4,3),{1,2},{3:'world'}])
# print(h.items())               #dict_items([(1,'']),(2,'python'),(3,7),(4,6.2),(5,[1,4],(6,(4,3)),(7,{1,2}),(8,{3:'world'}))
# h={1:"",2:"python",3:7,4:6.2,
# 5:[1,4],6:(4,3),7:{1,2},
# 8:{3:"world"}
# }
# h.clear()              
# print(h)         # {} emty dict
# a=[101,102,103,104,105]
# b=dict.fromkeys(a)
# print(b,type(b))     # {101:None,102:None,103:None,104:None,105:None} class 'dict'
# print(dict.fromkeys(a,23))    # {101:23,102:23,103:23,104:23,105:23}
# print(dict.fromkeys(a,23))    # {101:23,102:23,103:23,104:23,105:23}
# ={1:"",2:"python",3:7,4:6.2,
# 5:[1,4],6:(4,3),7:{1,2},
# 8:{3:"world"}
# }h
# print(h.get(2))      # 'python'
# print(h.get(42))       # 'None'
# print(h[2])             #  'python'
# print(h[23])           # keyError:23
# print(h(23))              #TypeError:'dict' object is not callable
# h.pop()                # TypeError:pop expected at least 1 argument,got 0
# h.pop(4)
# print(h)             # {1:'',2:'python',3:7,5:[1,4],6:(4,3),7:{1,2},8:{3:'world'}}
# h.popitem()
# print(h)              # {1:'',2:'python',3:7,4:6.2,5:[1,4],6:(4,3),7:{1,2}}
# h={1:"",2:"python",3:7,4:6.2,
# 5:[1,4],6:(4,3),7:{1,2},
# 8:{3:"world"}
# }
# h.update({9:'adv python'})
# print(h)                   #{1: '', 2: 'python', 3: 7, 4: 6.2, 5: [1, 4], 6: (4, 3), 7: {1, 2}, 8: {3: 'world'}, 9: 'adv python'}
# h.update({8:'core python'})
# print(h)                     #{1: '', 2: 'python', 3: 7, 4: 6.2, 5: [1, 4], 6: (4, 3), 7: {1, 2}, 8: 'core python'}
# h={1:"",2:"python",3:7,4:6.2,
# 5:[1,4],6:(4,3),7:{1,2},
# 8:{3:"world"}
# }
# h.setdefault(8,'devops')    # no change same key value answer come {1: '', 2: 'python', 3: 7, 4: 6.2, 5: [1, 4], 6: (4, 3), 7: {1, 2}, 8: {3: 'world'}}
# h.setdefault(10,'devops')     # {1: '', 2: 'python', 3: 7, 4: 6.2, 5: [1, 4], 6: (4, 3), 7: {1, 2}, 8: {3: 'world'}, 10: 'devops'}  only add new element
# print(h)
# print(dir(dict))
