import pandas as pd

def get_shorts():
    df = pd.read_csv('book_utf8.csv')
    # 调整格式
    df.columns = ['star', 'vote', 'shorts']
    star_to_number = {
        '力荐' : 5,
        '推荐' : 4,
        '还行' : 3,
        '较差' : 2,
        '很差' : 1
    }
    df['new_star'] = df['star'].map(star_to_number)

    # 查看数量
    # df.groupby('new_star').count()
    df2 = df[df['new_star'] == 3 ]
    # 取得评论内容  
    return df2['shorts'].to_string()


import jieba.analyse
text = get_shorts()
stop_words=r'day0402/extra_dict/stop_words.txt'
jieba.analyse.set_stop_words(stop_words)
# 基于TF-IDF算法进行关键词抽取
tfidf = jieba.analyse.extract_tags(text,
topK=10,                   # 权重最大的topK个关键词
withWeight=False) 
# >>> tfidf
# ['汤川', '东野', '短篇', '故事', '伽利略', '系列', '汤川学', '魔术', '神探', '扩写']