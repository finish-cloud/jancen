import random


hand_dict = {
    '1': 'グー',
    '2': 'チョキ',
    '3': 'パー'
}

print('手を入力してください')
print('1:グー 2:チョキ 3:パー')

# ユーザーに手を入力してもらう
player_input = input()
# 入力値が辞書hand_dictのキーとして存在しないことを判定する処理を書きます
if player_input not in hand_dict:
# 1, 2, 3以外が入力されたらプログラムを終了する
    print('入力が正しくありません。')
    exit()

# 入力値に対応した手の名前を辞書hand_dictから取得して、変数playerに代入します
player=hand_dict[player_input]
print('入力した手: ' + player)

# コンピューターの手をランダムに決定する
com_input = random.choice(['1', '2', '3'])
# コンピューターの手の名前を辞書hand_dictから取得して、変数comに代入します
com=hand_dict[com_input]
print('コンピューターの手: ' + com)

# 互いの手を表示する(例. グーvsチョキ)
if player == com:
    result = 'あいこ'

elif player == 'グー':
    if com == 'チョキ':
        result = 'あなたの勝ち'
    else:
        result = 'コンピューターの勝ち'
# チョキの条件
elif player == 'チョキ':
    if com == 'パー':
        result = 'あなたの勝ち'
    else:
        result = 'コンピューターの勝ち'
# パーの条件
else:
    if com == 'グー':
        result = 'あなたの勝ち'
    else:
        result = 'コンピューターの勝ち'

# ここからじゃんけんの勝敗条件を書いていきます。結果は変数resultに代入します
print(result)