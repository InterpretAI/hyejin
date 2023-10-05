import sqlalchemy
import sqlite3
import os
import openai

openai.api_key = '*'

def GPT_QNA(content):
    model = "gpt-3.5-turbo"
    messages = [{
        "role": "system",
        "content": content
    }]

    response = openai.ChatCompletion.create(model=model, messages=messages, temperature=0)
    answer = response['choices'][0]['message']['content']

    return answer

# 최근에 수정한 순서대로 item 가져오기
def generate_answer(content: str):

    generation = GPT_QNA(content)
    return generation



def get_connection():

    uri = os.getcwd()+'/app/iai.db'
    creator = lambda: sqlite3.connect(uri, uri=True)
    db = sqlalchemy.create_engine('sqlite:////', creator=creator)
    conn = db.raw_connection()
    
    return conn

# 최근에 수정한 순서대로 item 가져오기
def get_viewed_list(user_id: int):
    conn = get_connection()

    sql = '''
        select id, component, content, create_date, user_id, user, modify_date
        from Prompt
        where user_id = {}
        order by create_date desc
        order by modify_date desc
    '''.format(user_id)

    cursor = conn.cursor()
    cursor.execute(sql)

    row = cursor.fetchall()

    view_list = []

    for obj in row :
        data_dic = {
            'item_title' : obj[0]
        }
        view_list.append(data_dic)
    
    conn.close

    return view_list

