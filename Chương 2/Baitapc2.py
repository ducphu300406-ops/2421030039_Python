strl = "Hello World"
print(strl[0])
print(strl[:])
print(strl[0:])
print(strl[:5])
print(strl[0:4])
print(strl[1:8])
#vd2....
strl = "dia tin hoc"
print(strl[5:9])
print(strl[8:4])
#vd3....
s = 'Hello'
s += 'python'
print(s)
s2 = ',goodbye'
s3 = s + s2
#vd4....
print('a' in 'abc')
#ham len(...)....
a = "Hello World"
print(len(a))
#ham lower()....
a = " Hello World"
print(a.lower())
#ham upper()....
a = "Hello World"
print(a.upper())
#vd5....
str1 = "vi du ham find() trong python"
str2 = "find"
print(str1.find(str2))
print(str1.find(str2, 10))
print(str1.find(str2, 20))
#vd6....
str1 = "vi du ham count trong python, hoc lap trinh python"
sub = "py"
print("str1.count(sub,10):", str1.count(sub, 10))
print("str1.count(sub,10,30):", str1.count(sub, 10, 30))
sub = "ham"
print("str1.count(sub):", str1.count(sub))
#vd7....
str = 'hello word'
newstr = str.replace('hello','bye') 
print(newstr)
#vd8....
str = "AABBAACCAADDAAEE"
newstr = str.replace('AA','aa',2)
print(newstr)
#vd9....
srt = 'hello world'
print(str.split(''))
print("ABCDE".split(""))
print("ABCDR".split("",1))
print("ABCDE".split("",3))
#vd10....
strl = 'vd ham Istrip() trong python'
print(strl.Istrip())
strl = 'vd ham Istrip() trong python'
print(strl.Istrip(1))
#vd11...
strl = "hello python"
print(strl.isalpha())
strl = "Hello 123"
print(strl.isalpha())
#vd12....
strl = "hello python"
print(strl.isdigit())
strl = "Hello 123"
print(strl.isdigit())
strl = "123"
print(strl.isdigit())
#vd13....
>>> [1,2,3,4,5]
>>> ['a'.'b','c','d']
>>> [[1,2],[3,4]]
[[1,2],[3,44]]
>>> [1,'one',[2,'two']]
[1,'one',[2,'two']]
#vd14....
>>> 1st = [1,2,5"a,b,c"]
>>> 1st
[1.2.5,'abc']
>>> empty_list = []
>>> empty_list.[]
#vd15.....
strl "DH Mo_Dia Chat"
print(strl [0:0])
print(strl [0:3])
print(srtl [4:7])
print(strl [ :11])
#vd16....
>>> 1st = list ('IKTER')
>>> 1st 
['k','T','E','R','k','T','E','R']
>>> [1,2]
[1,2,1,2,1,2]
>>> 1st
#vd17....
list1 = [123,'abc','xyz']
list2 = ['java','python','phy','C++']
print("do dai cua list dau tien la:",len(list1))
print("do dai cua list dau tien la:",len(list2))
#vd18.....
list1 = ['123','abc','xyz','def']
list2 = [222,333,111]
print("pahn tu co gia tri lon nhat la:",max(list1))
print("phan tu co gia tri nho nhat la:",min(list2))
#vd19....
list1 = ['123','abc','456']
list2 = ['789','123','456','101112']
print("ptu co gia tri nho nhat 1 la:",min(list1))
print("ptu co gia tri nho nhat 2 la:",min(list2))
#vd20....
aTuple = ('123','abc','xyz''def')
alist = list(aTuple)
print("cac phan tu cua Tuple la:",aTuple)
print("cac phan tu cua list la:",alist)
#vd21...
list1 = ["ave",'python','C++']
list2 = ["phan tu cua list truoc khi them:",list1]
list1.append('python')
print("phan tu cua list sau khi them:",list1)
##vd22...
list1 = ['jave','python','C++','python']
print("so lan 'python' xuat hien trong list la:",list1.count('python'))
print("so lan 'java' xuat hien trong list la:",list1.count('java'))
#vd23...
list1 = ['jav','python','C++']
list2 = ['C++','rq']
list1.extend(list2);
print('list sau khi duoc mo trong than la:',list1)
#vd24....
#phuong thuc indez().....
list1 = ['java','python','C++','php','sql']
print("chi muc cua 'python' la:",list1.index('python'))
print("chi muc 'python' la:",list1.indax('php'))
#phuong thuc insert()....
list1 = ('java','python','C++','php','rql')
list1.insert(3,'andeoid')
#phuong thuc pop ...
list1 = ['java','python','C++','php','sql']
list1.pop()
print("list:",list1)
list1.pop(2)
#phuong thuc remove...
list1 = ['java','python','C++','php','sql']
list1.remove('C++')
print("list:",list1)
list1.remove('java')
#vd25.....
#xoa ptu list bang lenh del...
fruits = ["apple","banana","guava"]
del fruits [0]
print(fruits)
#phuong thuc reverre()....
list1 = ['java','python','C++','php','sql']
list1.reverse();
print("li9t bi dao nguoc:",list1)
#phuong thuc clear()....
fruits = ["apple","banana","guava"]
fruits.clear()
print(fruits);
#vd26.....
#1 so ham su ly list.....
>>> 1st = [[1,2,3],[4,5,6]]
>>> 1st 
[[1,2,3],[4,5,6]]
>>> 1st [0]
[1,2,3]
>>> 1st [1]
[4,5,6]
#vd27.....
#cach khoi tao tuple.....
>>> tuple = (1,2,3,4)
>>> tuple
91 (1,2,3,4)
>>> e_tuple = ()
>>> e_tuple
()
#ma tran...
>>> tuple = ((1,2,3),[4,5])
>>> tuple [0]
(1,2,3)
>>> tuple [0] {2}
3
>>> tuple [1] [0]
4 
#phuong thuc count().....
>>> tuple = (1,5,3,5,6,1,1)
>>> tuple.count(1)
3
>>> tuple.count(4)
0
#in ra tung hang theo cot khong dung for.....
print(*matrix [0])
print(*matrix [1])
print(*matrix [2])
print(*matrix [3])



