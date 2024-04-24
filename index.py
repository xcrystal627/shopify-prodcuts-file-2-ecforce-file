import csv



with open('output.csv', 'w', newline='', encoding='utf-8') as newFile:
    csv_writer = csv.writer(newFile)
    csv_writer.writerow([  "商品名",  "商品コード",  "商品ラベルID",  "SKUコード",  "マスターSKU商品の指定",  "単品・定期",  "ステータス",  "販売中",  "公開開始日",  "公開終了日",  "通常価格",  "販売価格",  "税率設定ID",  "詳細",  "詳細（モバイル）",  "規格名1",  "分類名1",  "規格名2",  "分類名2",  "規格名3",  "分類名3",  "送料の個別設定ID",  "支払い手数料の個別設定ID",  "同梱物",  "注文毎の購入制限数",  
                         "購入数の下限",  "購入数の上限",  "顧客毎の購入制限数",  "未成年者の購入制限",  "未成年者の設定",  "同梱物の購入制限",  "ポイント交換",  "変更可能SKUグループID",  
                         "原価",  "大きさ",  "会員ランク制御",  "注意喚起文（画面上部）",  "注意喚起文",  "支払い方法割引設定（支払い方法ID）",  "支払い方法割引設定（割引額）",  
                         "支払い方法割引設定（割引率）",  "支払い方法割引設定（初回のみ）",  "詳細（サブ）",  "詳細（サブ、モバイル）",  "メタディスクリプション",  "メタキーワード",  
                         "新着フラグ",  "セールフラグ",  "購入画面への表示",  "メール画面への表示",  "帳票への表示",  "メーカーID",  "カテゴリーID",  "商品画像",  "SKU商品画像1",  
                         "SKU商品画像2",  "SKU商品画像3",  "SKU商品画像4",  "SKU商品画像5",  "定期お約束回数",  "配送サイクル",  "何ヶ月ごとの何日に配送",  "何日ごとに配送", 
                        "何ヶ月ごとの何回目の何曜日に配送",  "選択可能間隔（日付・曜日）",  "選択可能間隔（間隔）",  "連携用商品番号",  "連携用SKU番号",  "自由入力1",  "自由入力2",  
                        "自由入力3",  "自由入力4",  "自由入力5",  "自由入力6",  "自由入力7",  "自由入力8",  "自由入力9",  "自由入力10"])
    count = 1
    with open('shopify-products.csv','r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            #title, price, type, published, status
            if row[1] != '':
                count += 1
                prefix = ''
                if count < 10:
                    prefix = '00'
                elif count < 100:
                    prefix = '0'
                else:
                    prefix = ''

                # print(row[1], row[20],  row[5], row[7], row[47] )
                selling = 1
                status = 'active'

                if row[7] == 'true':
                    selling = 1
                else :
                    selling = 0
                    
                if row[47] == 'draft':
                    status = 'inactive'
                if row[47] == 'active':
                    status = 'active'

                csv_writer.writerow([row[1], f"product-v-{prefix}{str(count)}", row[25],  f"product-v-{prefix}{str(count)}", '',0, status, selling,'','', row[20], row[20], '','','','','','','','','','','','','',
                                     '','','','','','','','',
                                    row[20],1,'','','','','',
                                    '','','','','','',
                                    '','','','','','','','','',
                                    '','','','','','','','',
                                    '','','','','','','',
                                    '','','','','','','','' ])