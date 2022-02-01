import requests,bs4,datetime

TIMEOUT = 10
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0"}


#=====上記データを整形して、管理サイトにアクセス、管理サイトのフォームにて新規作成する。============
#詳細:https://noauto-nolife.com/post/python-requests-post-method/


#ここにIDとパスワードを入力する。
ID      = "asahina"
PASS    = "seiya0723"

#ここにで管理サイトのURLを入力(デプロイした後は下記URLを変更する。)
URL     = ""
LOGIN   = URL + "admin/login/"
TIMEOUT = 10
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}

#(1) セッションを維持する(セッションメソッドからオブジェクトを作る)
client = requests.session()
r = client.get(LOGIN,timeout=TIMEOUT,headers=HEADERS)
print(r)

#(2) CSRFトークンを手に入れ、投稿するデータを辞書型で生成
if 'csrftoken' in client.cookies:
    csrftoken = client.cookies['csrftoken']
    print(csrftoken)

login_data   = { "csrfmiddlewaretoken":csrftoken,
                 "username":ID,
                 "password":PASS
                 }

#(3) ログインする
r   = client.post(LOGIN,data=login_data,headers={"Referer":LOGIN})

#(4) ログインに使用したセッションで天気のフォームにアクセス。name属性はモデルのフィールド名と同じ。日時型は分離している点に注意
POST_URL    = URL + "admin/tenki/weather/add/"

#ログインした後、新規作成フォームのページにアクセスする。(CSRFトークンを手に入れるため。) 
r = client.get(POST_URL,headers=HEADERS)


import csv

with open('test.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

        #CSRFトークンをセットし直す。
        if 'csrftoken' in client.cookies:
            csrftoken = client.cookies['csrftoken']
            print(csrftoken)
        
        post_data   = {
                "csrfmiddlewaretoken":csrftoken,
                "place":row[0],
                "dt_0":row[1],
                "dt_1":row[2],
                "today":row[3],
                "tomorrow":row[4],
                "today_high_temp":row[5],
                "today_low_temp":row[6],
                "tomorrow_high_temp":row[7],
                "tomorrow_low_temp":row[8],
                }
        
        print(post_data)
        
        r   = client.post(POST_URL,data=post_data,headers={"Referer":LOGIN})
        print(r)





