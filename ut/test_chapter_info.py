import json
from logic.chapter_info import ChapterInfoLogic

_op = ChapterInfoLogic()
data = [{
                "index": 1,
                "barrier_types": [1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999],
                "barrier_indexs": [2, 4, 8],
                "boss": [{
                    "index": 3,
                    "num": 18
                }]
            }, {
                "index": 2,
                "barrier_types": [1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999],
                "barrier_indexs": [13, 15, 16, 12],
                "boss": [{
                    "index": 20,
                    "num": 18
                }]
            }, {
                "index": 3,
                "barrier_types": [1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999],
                "barrier_indexs": [13, 24, 28, 15],
                "boss": [{
                    "index": 20,
                    "num": 18
                }]
            }, {
                "index": 4,
                "barrier_types": [1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999],
                "barrier_indexs": [15, 24, 35],
                "boss": [{
                    "index": 20,
                    "num": 36
                }]
            }, {
                "index": 5,
                "barrier_types": [1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999],
                "barrier_indexs": [25, 27, 33, 31],
                "boss": [{
                    "index": 20,
                    "num": 72
                }]
            }, {
                "index": 6,
                "barrier_types": [1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999],
                "barrier_indexs": [14, 15, 16, 27],
                "boss": [{
                    "index": 21,
                    "num": 18
                }]
            }, {
                "index": 7,
                "barrier_types": [1, 1, 1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 999, 999],
                "barrier_indexs": [14, 15, 16, 22, 27, 28],
                "boss": [{
                    "index": 21,
                    "num": 27
                }]
            }, {
                "index": 8,
                "barrier_types": [1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999],
                "barrier_indexs": [16, 22, 27, 28],
                "boss": [{
                    "index": 15,
                    "num": 27
                }]
            }, {
                "index": 9,
                "barrier_types": [1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999],
                "barrier_indexs": [16, 22, 27, 28],
                "boss": [{
                    "index": 21,
                    "num": 18
                }]
            }, {
                "index": 10,
                "barrier_types": [1, 1, 1, 1, 1, 0],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 999, 9],
                "barrier_indexs": [7, 8, 9, 25, 26, 27],
                "boss": [{
                    "index": 20,
                    "num": 18
                }]
            }, {
                "index": 11,
                "barrier_types": [1, 1, 1, 1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 999, 999, 999],
                "barrier_indexs": [7, 8, 9, 25, 26, 27, 10],
                "boss": [{
                    "index": 20,
                    "num": 18
                }]
            }, {
                "index": 12,
                "barrier_types": [1, 1, 1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 999, 999],
                "barrier_indexs": [7, 8, 9, 25, 26, 27],
                "boss": [{
                    "index": 20,
                    "num": 18
                }]
            }, {
                "index": 13,
                "barrier_types": [1, 1, 1, 1, 1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 999, 999, 999, 999],
                "barrier_indexs": [7, 8, 9, 11, 25, 26, 27, 28],
                "boss": [{
                    "index": 20,
                    "num": 18
                }]
            }, {
                "index": 14,
                "barrier_types": [1, 1, 1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 999, 999],
                "barrier_indexs": [7, 8, 15, 19, 26, 27],
                "boss": [{
                    "index": 20,
                    "num": 27
                }]
            }, {
                "index": 15,
                "barrier_types": [1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999],
                "barrier_indexs": [7, 8, 26, 27],
                "boss": [{
                    "index": 20,
                    "num": 36
                }]
            }, {
                "index": 16,
                "barrier_types": [1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999],
                "barrier_indexs": [32, 33],
                "boss": [{
                    "index": 20,
                    "num": 36
                }]
            }, {
                "index": 17,
                "barrier_types": [1, 1, 1, 1, 1, 1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 999, 999, 999, 999, 999],
                "barrier_indexs": [14, 15, 16, 17, 20, 23, 26, 27, 29],
                "boss": [{
                    "index": 21,
                    "num": 36
                }]
            }, {
                "index": 18,
                "barrier_types": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
                "barrier_indexs": [14, 15, 16, 17, 20, 23, 26, 27, 29, 35, 38, 39, 40, 41],
                "boss": [{
                    "index": 21,
                    "num": 18
                }]
            }, {
                "index": 19,
                "barrier_types": [1, 1, 1, 1, 1, 1, 2, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 999, 999, 99, 999],
                "barrier_indexs": [8, 9, 10, 14, 16, 20, 21, 22],
                "boss": [{
                    "index": 15,
                    "num": 18
                }]
            }, {
                "index": 20,
                "barrier_types": [1, 1, 1, 1, 0, 0, 1, 2, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 18, 18, 999, 99, 999],
                "barrier_indexs": [14, 15, 16, 17, 20, 22, 26, 27, 28],
                "boss": [{
                    "index": 21,
                    "num": 56
                }]
            }, {
                "index": 21,
                "barrier_types": [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 9, 9, 999, 999, 999, 999],
                "barrier_indexs": [7, 10, 14, 15, 19, 22, 25, 28, 32, 33],
                "boss": [{
                    "index": 21,
                    "num": 18
                }]
            }, {
                "index": 22,
                "barrier_types": [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 99, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 9, 99],
                "barrier_indexs": [1, 2, 3, 4, 6, 11, 12, 14, 15, 17, 25, 26, 27, 23, 19, 28],
                "boss": [{
                    "index": 21,
                    "num": 18
                }]
            }, {
                "index": 23,
                "barrier_types": [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 999, 999, 999, 999, 9, 9, 9],
                "barrier_indexs": [14, 15, 16, 13, 26, 27, 28, 25, 19, 20, 22],
                "boss": [{
                    "index": 21,
                    "num": 18
                }]
            }, {
                "index": 24,
                "barrier_types": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 9, 9],
                "barrier_indexs": [1, 2, 3, 4, 7, 10, 13, 15, 16, 25, 27, 28, 14, 26],
                "boss": [{
                    "index": 9,
                    "num": 36
                }]
            }, {
                "index": 25,
                "barrier_types": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 9, 9],
                "barrier_indexs": [1, 2, 3, 4, 7, 10, 13, 15, 16, 25, 26, 28, 14, 27],
                "boss": [{
                    "index": 9,
                    "num": 36
                }]
            }, {
                "index": 26,
                "barrier_types": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2],
                "ballNum": 9,
                "barrier_nums": [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 9, 9, 99],
                "barrier_indexs": [2, 3, 4, 8, 10, 13, 17, 21, 25, 26, 28, 15, 19, 23],
                "boss": [{
                    "index": 9,
                    "num": 18
                }]
            }, {
                "index": 27,
                "barrier_types": [1, 1, 0, 0, 0, 0, 2],
                "ballNum": 9,
                "barrier_nums": [999, 999, 9, 9, 9, 9, 99],
                "barrier_indexs": [26, 28, 14, 16, 20, 22, 21],
                "boss": [{
                    "index": 15,
                    "num": 36
                }]
            }, {
                "index": 28,
                "barrier_types": [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2],
                "ballNum": 9,
                "barrier_nums": [9, 9, 9, 9, 999, 999, 9, 9, 9, 9, 9, 9, 99],
                "barrier_indexs": [14, 16, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 21],
                "boss": [{
                    "index": 15,
                    "num": 36
                }]
            }, {
                "index": 29,
                "barrier_types": [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                "ballNum": 9,
                "barrier_nums": [9, 9, 9, 999, 999, 9, 999, 999, 9, 9, 9, 9, 9, 9],
                "barrier_indexs": [8, 10, 15, 17, 20, 22, 25, 27, 30, 32, 37, 39, 44, 46],
                "boss": [{
                    "index": 3,
                    "num": 18
                }]
            }, {
                "index": 30,
                "barrier_types": [0, 0, 1, 0, 2, 2, 0, 1, 1, 1, 1, 2, 2, 0, 0, 0, 0, 0],
                "ballNum": 9,
                "barrier_nums": [9, 9, 999, 9, 99, 99, 9, 999, 999, 999, 999, 99, 99, 9, 9, 9, 9, 9],
                "barrier_indexs": [3, 7, 8, 10, 12, 15, 17, 18, 23, 25, 28, 31, 31, 34, 37, 40, 43, 46],
                "boss": [{
                    "index": 2,
                    "num": 56
                }]
            }]

for info in data:
    _= _op.manage_info(chapter_index=info.get("chapter_index"),
                boss=json.dumps(info.get("boss")),
                ball_num=info.get("ball_num"),
                barrier_indexs=json.dumps(info.get("barrier_indexs")),
                barrier_nums=json.dumps(info.get("barrier_nums")),
                barrier_types=json.dumps(info.get("barrier_types")),
                barrier_offset=json.dumps(info.get("barrier_offset")),
                )
    print _