print ("Hello warld")
#[]リスト
print  (["hello","world"])
print(["a","b","c",["1","2","3"]])

print(["a","b","c",["1","2","3"]][2])
#0123の2を取り出す
print(["a","b","c",["1","2","3"]][3])
print(["a","b","c",["1","2","3"]][3][2])
#3を取り出し、その中の2を取り出す

print (["a", "b", "c", "d", "e"][0:3])
#０～３を取り出し
print ([0,1,2,3,4,5,6,7,8,9,10][0:8:1])
print ([0,1,2,3,4,5,6,7,8,9,10][0:8:2])
#０～８の2つおきに取り出し
print ([0,1,2,3,4,5,6,7,8,9,10][0:8:3])

print ([0,1,2,3,4,5,6,7,8,9,10][:])

x = [1,2,3,["a","b","c"]]
x[1] = "BBQ"
print (x)
print (x[1])

#ｘにAを追加
x.append("A")
print (x)

x[3].append(4)
#入れ子を指定、４を追加
print (x)

x.extend([5,6])
print(x)
x.append([5,6])
print (x)
#appendとextendの違いに注意
#加えると付け加える

x.remove(5)
print (x)
x[6].remove(5)
#入れ子6を指定、5を削除
print (x)
