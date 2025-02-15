import json

def main_kn(user_input):
    # JSONファイルのパス
    # 漢字配列
    file_path = 'list.json'

    # JSONファイル読み込み
    try:
        json_data = load_json(file_path)

    # 読み込み失敗
    except FileNotFoundError:
        return
    except json.JSONDecodeError:
        return
    result_kn =[]

    # 入力された文字とJSON内の漢字を1文字ずつ比較
    for kanji in user_input:
        result = compare_with_input(json_data, kanji)
        result_kn.append({kanji: result})
    return result_kn


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
        #結果報告
        return array_data


# 実行部分
if __name__ == "__main__":
    main_kn()
