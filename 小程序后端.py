# 2024-07-08,15点17d   算法最终的服务: nohup ~/miniconda3/bin/python  backend.py  &

import sqlite3
# import cv2
import os
import io
import json

from io import BytesIO  
import os
print(os.cpu_count(), 'cpushuliaing')



from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # 解决跨域问题

basedir = os.path.abspath(os.path.dirname(__file__))  # 定义一个根目录 用于保存图片用
UPLOAD_ROOT_PATH = 'pic_data'
# http://172.27.118.204:5050

@app.route('/food/list', methods=['GET', 'POST'])
def editorData222222():
    # 食物的图片使用网络图片url和本地路径都可以.
    return jsonify({'list':[{'name':'类别1','food':[{
        'id':0,
        'name':'食物1',
        'price':'11',
        'image_url':'https://pic2.zhimg.com/v2-d1b6b63c5a4549271dadc37b9d562a10_1200x500.jpg',
        
        
        },{
'id':1,
        'name':'食物2',
        'price':'12',
        'image_url':'/images/index/b_2.jpg',
        
        
        },
        {'id':2,
        'name':'食物3',
        'price':'12',
        'image_url':'/images/index/b_2.jpg',
        
        
        },
        {
        'name':'食物4',
        'price':'12',
        'image_url':'/images/index/b_2.jpg',
        
        
        },
        {
        'name':'食物5',
        'price':'12',
        'image_url':'/images/index/b_2.jpg',
        
        
        },
        {
        'name':'食物6',
        'price':'12',
        'image_url':'/images/index/b_2.jpg',
        
        
        },
        {
        'name':'食物7',
        'price':'12',
        'image_url':'/images/index/b_2.jpg',
        
        
        }
        ]},{'name':'类别2','food':[{
        'name':'食物21',
        'price':'11',
        'image_url':'/images/index/b_2.jpg',
        
        
        },{
        'name':'食物22',
        'price':'12',
        'image_url':'/images/index/b_2.jpg',
        
        
        }
        ]},{'name':'类别3','food':[{
        'name':'食物31',
        'price':'11',
        'image_url':'/images/index/b_2.jpg',
        
        
        },{
        'name':'食物32',
        'price':'12',
        'image_url':'/images/index/b_2.jpg',
        
        
        }
        ]},{'name':'类别4','food':[{
        'name':'食物41',
        'price':'11',
        'image_url':'/images/index/b_2.jpg',
        
        
        },{
        'name':'食物42',
        'price':'12',
        'image_url':'/images/index/b_2.jpg',
        
        
        }
        ]}],
                    'promotion':['1','2','3']
                    
                    })


@app.route('/food/index', methods=['GET', 'POST'])
def editorData():
    
    return jsonify({'list':['1','2','3'],
                    'promotion':['1','2','3']
                    
                    })

@app.route('/user/setting', methods=['GET', 'POST'])
def editorData222():
    
    return jsonify({'isLogin':True})









if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug=True)
