a = {
    "Name":"Charudatt",
    "School":"PHSC",
    "Friend":['Awesh','Jamil','Narendra','Azhar'],
    "Collage":"CDGI"
}
# print(a["School"])
# a['Friend']=['Myself']
print(a)
# print(a.keys())
# print(a.values())
# print(a.item())
a2={
    'Adress':"3,Ram Nager Ext.",
    "Brother":"Rohit"
}
a.update(a2)
a.update({"Profession":"Student"})
print(a)
print(a.get('adress'))

