class dictclass:
    def __init__(self,a):
        self.dict=a
    def del_dict(self,key):
        if key in self.dict.keys():
            del self.dict[key]
        else:
            return 'no that key'
    def get_dict(self,key):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return 'not found'
    def get_key(self):
        return self.dict.keys()
dict=dictclass({'name':'liming','age':18,'score':90})
print(dict.get_key())
dict.del_dict('score')
print(dict.get_key())
print(dict.get_dict('name'))
print(dict.get_dict('score'))
