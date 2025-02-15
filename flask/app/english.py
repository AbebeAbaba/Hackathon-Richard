def main(user_input):
    prefix = ["anti","de","dis",
              "en","em","fore",
              "in","im","il",
              "ir","inter","mid",
              "mis","non","over",
              "pre","re","semi",
              "sub","super","trans",
              "un","under"
              ]

    suffix = ["able","ible","ed",
              "en","er","est",
              "ful","ic","ing",
              "ion","ty","ive",
              "less","ly","ment",
              "ness","ous"
              ]
    
    flag = 0
    result = [];

    
    # 入力された文字とJSON内の漢字を1文字ずつ比較
    for pre in prefix:
        if(user_input.startswith(pre) == True):
            result.insert(0,pre)
            flag = 1
            break

    for suf in suffix:
        if(user_input.endswith(suf) == True):
            result.insert(1,suf)
            flag = 1
            break
    
    if(flag == 0):
        return result
    else:
        return result

# 実行部分
if __name__ == "__main__":
    main()