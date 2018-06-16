#process.env.PYTHONIOENCODING = "utf-8";
import random
print("ゲーム開始!チャンスは5回")
score = 0

for i in range(5):
    #for 変数 in range(回数)
    print(str(i+1)+"回目")
    num = random.randint(1,3)
    #random.randint(1,3)
    #（上限値、下限値）

    answer = input('1～3の数字を入力＞＞')

    if num == int(answer):
        print("あたり")
        score = score + 1
    else:
        print("はずれ！正解は"+str(num))

print("ゲーム終了！得点は"+str(score)+"/5 !")
