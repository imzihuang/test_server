import json
from logic.chapter_info import ChapterInfoLogic

_op = ChapterInfoLogic()
data = {
            "chapter_index": 1,
            "boss": [{"index": 3, "num": 18}],
            "barrier_types": [1, 1, 1],
            "ballNum": 9,
            "barrier_nums": [999, 999, 999],
            "barrier_indexs": [2, 4, 8],
            "barrier_offset": [0, 0, 0],
        }
_= _op.manage_info(chapter_index=data.get("chapter_index"),
                boss=json.dumps(data.get("boss")),
                ball_num=data.get("ball_num"),
                barrier_indexs=json.dumps(data.get("barrier_indexs")),
                barrier_nums=json.dumps(data.get("barrier_nums")),
                barrier_types=json.dumps(data.get("barrier_types")),
                barrier_offset=json.dumps(data.get("barrier_offset")),
                )
print _