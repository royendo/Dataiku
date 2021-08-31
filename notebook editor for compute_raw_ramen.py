
# coding: utf-8

# In[ ]:



import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from tabelog import Tabelog


# In[ ]:


class Saketime:
    """
    食べログスクレイピングクラス
    test_mode=Trueで動作させると、最初のページの３店舗のデータのみを取得できる
    """
    def __init__(self, base_url, test_mode=False, prefecture='hokkaido', begin_page=1, end_page=30):

        # 変数宣言
        self.store_id = ''
        self.store_id_num = 0
        self.store_name = ''
        self.score = 0
        self.prefecture = prefecture
        self.review_cnt = 0
        self.review = ''
        self.review_star = ''
        self.address = ''
        self.url= ''
        self.columns = ['store_id', 'store_name', 'address', 'score', 'prefecture', 'review_cnt', 'review', 'review_star', 'url']
        self.df = pd.DataFrame(columns=self.columns)
        self.__regexcomp = re.compile(r'\n|\s') # \nは改行、\sは空白

        page_num = begin_page # 店舗一覧ページ番号

        if test_mode:
            # list_url = base_url + str(page_num) +  '/?Srt=D&SrtT=rt&sort_mode=1' #食べログの点数ランキングでソートする際に必要な処理
            list_url = base_url + "/" + self.prefecture
            self.scrape_list(list_url, mode=test_mode)
        else:
            while True:
                list_url = base_url + str(page_num) +  '/?Srt=D&SrtT=rt&sort_mode=1' #食べログの点数ランキングでソートする際に必要な処理
                if self.scrape_list(list_url, mode=test_mode) != True:
                    break

                # INパラメータまでのページ数データを取得する
                if page_num >= end_page:
                    break
                page_num += 1
        return

    def scrape_list(self, list_url, mode):
        """
        店舗一覧ページのパーシング
        """
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
        r = requests.get(url=list_url, headers=headers)
        
        if r.status_code != requests.codes.ok:
            return False
        
        soup = BeautifulSoup(r.content, 'html.parser')
        soup_h2_list = soup.find_all('h2')
        
        if len(soup_h2_list) == 0:
            return False
        
        if mode:
            for h2 in soup_h2_list[:1]:
                a = h2.find_all('a', href=True)
                item_url = 'https://www.saketime.jp/ranking' + a.find_all('a', href=True)[0]['href']
                self.store_id_num += 1
                self.scrape_item(item_url, mode)
                
        return True

    def scrape_item(self, item_url, mode):
        """
        個別店舗情報ページのパーシング
        """
        start = time.time()

        r = requests.get(item_url)
        if r.status_code != requests.codes.ok:
            print(f'error:not found{ item_url }')
            return

        soup = BeautifulSoup(r.content, 'html.parser')

        # 店舗名称取得
        self.sake_name = soup.find('h1').contents[0].strip()
        self.store_name = soup.find('a', href="#maker").text
        print('{}→銘柄：{} / {}'.format(self.store_id_num, self.sake_name, self.store_name), end='')
        
        # 評価点数取得
        rating_score = soup.find('span', class_='point').text
        self.rating_score = rating_score
        print('  評価点数：{}点'.format(self.rating_score), end='')
        
        # 評価が3.5未満店舗は除外
        if float(rating_score) < 3:
            print(' 評価が3未満のため処理対象外')
            self.store_id_num -= 1
            return

        # 銘柄サマリー
        reviews = []
        summary = soup.find('div', class_='mod-subsection mod-centerbox').find('p').text
        reviews.append(summary)
        
        # レビュー取得
        list_reviews = soup.find('div', id='review').find_all('p', class_='r-body')
        i = 0
        for review in list_reviews:
            review = review.text.replace(" ", "").replace("\n", "").replace("\r", "").replace("\u3000", "")
            reviews.append(review)
            i += 1
        
        print('  レビュー件数：{}'.format(i)
        self.review_cnt = i

        page_num = 1 #1ページ*20 = 20レビュー 。この数字を変えて取得するレビュー数を調整。

        # レビュー一覧ページから個別レビューページを読み込み、パーシング
        # 店舗の全レビューを取得すると、食べログの評価ごとにデータ件数の濃淡が発生してしまうため、
        # 取得するレビュー数は１ページ分としている（件数としては１ページ*20=２0レビュー）
        while True:
            review_url = review_tag + 'COND-0/smp1/?lc=0&rvw_part=all&PG=' + str(page_num)
            #print('\t口コミ一覧リンク：{}'.format(review_url))
            print(' . ' , end='') #LOG
            if self.scrape_review(review_url) != True:
                break
            if page_num >= 1:
                break
            page_num += 1

        process_time = time.time() - start
        print('  取得時間：{}'.format(process_time))

        return

    def scrape_review(self, review_url):
        """
        レビュー一覧ページのパーシング
        """
        r = requests.get(review_url)
        if r.status_code != requests.codes.ok:
            print(f'error:not found{ review_url }')
            return False

        # 各個人の口コミページ詳細へのリンクを取得する
        #<div class="rvw-item js-rvw-item-clickable-area" data-detail-url="/tokyo/A1304/A130401/13141542/dtlrvwlst/B408082636/?use_type=0&amp;smp=1">
        #</div>
        soup = BeautifulSoup(r.content, 'html.parser')
        review_url_list = soup.find_all('div', class_='rvw-item') # 口コミ詳細ページURL一覧

        if len(review_url_list) == 0:
            return False

        for url in review_url_list:
            review_detail_url = 'https://tabelog.com' + url.get('data-detail-url')
            #print('\t口コミURL：', review_detail_url)

            # 口コミのテキストを取得
            self.get_review_text(review_detail_url)

        return True

    def get_review_text(self, review_detail_url):
        """
        口コミ詳細ページをパーシング
        """
        r = requests.get(review_detail_url)
        if r.status_code != requests.codes.ok:
            print(f'error:not found{ review_detail_url }')
            return

        # ２回以上来訪してコメントしているユーザは最新の1件のみを採用
        #<div class="rvw-item__rvw-comment" property="v:description">
        #  <p>
        #    <br>すごい煮干しラーメン凪 新宿ゴールデン街本館<br>スーパーゴールデン1600円（20食限定）を喰らう<br>大盛り無料です<br>スーパーゴールデンは、新宿ゴールデン街にちなんで、ココ本店だけの特別メニューだそうです<br>相方と歌舞伎町のtohoシネマズの映画館でドラゴンボール超ブロリー を観てきた<br>ブロリー 強すぎるね(^^)面白かったです<br>凪の煮干しラーメンも激ウマ<br>いったん麺ちゅるちゅる感に、レアチャーと大トロチャーシューのトロけ具合もうめえ<br>煮干しスープもさすが！と言うほど完成度が高い<br>さすが食べログラーメン百名店<br>と言うか<br>2日連チャンで、近場の食べログラーメン百名店のうちの2店舗、昨日の中華そば葉山さんと今日の凪<br>静岡では考えられん笑笑<br>ごちそうさまでした
        #  </p>
        #</div>
        soup = BeautifulSoup(r.content, 'html.parser')
        review = soup.find_all('div', class_='rvw-item__rvw-comment')#reviewが含まれているタグの中身をすべて取得
        if len(review) == 0:
            review = ''
        else:
            review = review[0].p.text.strip() # strip()は改行コードを除外する関数
        
        # 各レビューの★の数を取得
        review_star = soup.find_all('b', class_='c-rating-v2__val c-rating-v2__val--strong rvw-item__ratings--val')
        if len(review_star) == 0:
            review_star = ''
        else:
            review_star = review_star[0].string

        #print('\t\t口コミテキスト：', review)
        self.review = review
        self.review_star = review_star

        # データフレームの生成
        self.make_df()
        return

    def make_df(self):
        self.store_id = str(self.store_id_num).zfill(8) #0パディング
        se = pd.Series([self.store_id, self.store_name, self.address, self.score, self.prefecture, self.review_cnt, self.review, self.review_star], self.columns) # 行を作成
        self.df = self.df.append(se, self.columns) # データフレームに行を追加
        return


# In[155]:


base_url = 'https://www.saketime.jp/ranking/hokkaido/'
#base_url = 'https://www.saketime.jp/brands/4994/'


# In[156]:


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}

r = requests.get(url=base_url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')


# In[157]:


soup_h2_list = soup.find_all('h2')


# In[158]:


soup_h2_list


# In[25]:


soup_a_list = soup.find_all('div', class_='headline clearfix') # 店名一覧


# In[51]:


soup_h2_all = soup.find_all('h2')
for h2 in soup_h2_all:
    a = h2.find_all('a', href=True)
    for href in a:
        # href.get('href')
        url = 'https://www.saketime.jp/ranking' + href['href']
        sake_name = href.text
        


# In[57]:


soup_h2_all[0].find_all('a', href=True)[0]


# In[59]:


item_url = 'https://www.saketime.jp/brands/4994/'
r = requests.get(url = item_url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')


# In[109]:


soup.find('h1').contents[0].strip()


# In[112]:


soup.find('a', href="#maker").text


# In[114]:


soup.find('span', class_='point').text


# In[121]:


soup.find('a', id='pricerange').contents[1]


# In[127]:


summary = soup.find('div', class_='mod-subsection mod-centerbox').find('p').text


# In[153]:


list_reviews = soup.find('div', id='review').find_all('p', class_='r-body')
reviews = []
for review in list_reviews:
    review = review.text.replace(" ", "").replace("\n", "").replace("\r", "").replace("\u3000", "")
    reviews.append(review)


# In[154]:


reviews


# In[ ]:


from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import requests


# In[ ]:


raw_ramen = Tabelog(base_url="https://tabelog.com/tokyo/rstLst/ramen/",
                    test_mode=False, p_ward='東京都内',
                    begin_page=31, end_page=40) # begin_page=31, end_page=40 5/6/2021


# In[ ]:


raw_ramen_df = raw_ramen.df


# In[8]:


from saketime import Saketime

