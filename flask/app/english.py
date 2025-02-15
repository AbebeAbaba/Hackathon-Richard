def main_en(user_input):
    prefix = ["anti","de","dis",
              "en","em","fore",
              "inter","im","il",
              "ir","in","mid",
              "mis","non","over",
              "pre","re","semi",
              "sub","super","trans",
              "under","un"
              ]

    suffix = ["able","ible","ed",
              "en","er","est",
              "ful","ic","ing",
              "ion","ty","ive",
              "less","ly","ment",
              "ness","ous"
              ]
    
    flag = 0

    result_en = []

    # 入力された文字とJSON内の漢字を1文字ずつ比較
    for pre in prefix:
        if(user_input.startswith(pre) == True):
            result_en.insert(0,pre)
            flag = 1
            break

    for suf in suffix:
        if(user_input.endswith(suf) == True):
            result_en.insert(1,suf)
            flag = 1
            break
    
    return result_en

# 実行部分
if __name__ == "__main__":
    main_en()