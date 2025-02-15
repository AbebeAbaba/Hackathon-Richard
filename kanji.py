import json


def main():
    # JSONファイルのパス
    # 漢字右左ファイル
    file_path_lr = 'kanji_left_right.json'
    # 漢字上下ファイル
    file_path_tp = 'kanji_top_buttom.json'

    # JSONファイル読み込み
    try:
        json_data_lr = load_json(file_path_lr)
        json_data_tp = load_json(file_path_tp)

    # 読み込み失敗
    except FileNotFoundError:
        print("エラー: JSONファイルが見つかりません。")
        return
    except json.JSONDecodeError:
        print("エラー: JSONの形式が正しくありません。")
        return

    # 配列として入力受け取り
    user_input = list(input("比較したい文字を入力してください: "))

    # 入力された文字とJSON内の漢字を1文字ずつ比較
    for kanji in user_input:
        # 漢字右左分解 成功 -> 0
        if(compare_with_input(json_data_lr, kanji) != 0):
            # 漢字上下分解 成功 -> 0
            if(compare_with_input(json_data_tp, kanji) != 0):
                # 両方失敗 -> 失敗報告
                print(f"入力された文字 '{kanji}' はキーに存在しません。")


# JSONファイル読み込み関数 漢字リスト
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# 入力とJSONファイル内の漢字を比較する関数aaa
def compare_with_input(json_data, kanji):
    # 1文字ずつ確認する あれば進む
    if kanji in json_data:
        # 対応する配列を取得
        # array_data: 分解後の漢字を含む配列
        array_data = json_data[kanji]
        # 結果出力
        print(f"入力された文字 '{kanji}' はキーに存在します。対応する配列: {array_data}")
        #成功報告
        return 0


# 実行部分
if __name__ == "__main__":
    main()
