"""
仕様書: https://hackmd.io/SFtaslrOSq2AwPJ5QrVsZw
"""
import responder
import os
import re
# サンプル用
import csv

api = responder.API(cors=True, cors_params={
    'allow_origins': ['*'],
    'allow_methods': ['*'],
    'allow_headers': ['*'],
    # https://qiita.com/DeliciousBar/items/19ec5107853bd1019f53
})


@api.route("/confirm")
def confirm(req, resp):
    result = {}
    if req.method == "get":
        """
        フォルダの存在確認

        Method: GET
        エンドポイント: localhost:3000/confirm
        クエリパラメータ: folderpath=<絶対パス>
        """
        if "folderpath" in req.params:
            path = req.params["folderpath"]
            try:
                if os.path.isdir(path):
                    if os.path.isfile(path + "/result.csv"):  # TODO: 結果ファイル名の決定
                        result["dataExist"] = True
                        result["message"] = "Data exists in the folder"
                    else:
                        result["dataExist"] = False
                        result["message"] = "No data in the folder"
                else:
                    resp.status_code = api.status_codes.HTTP_404
                    result["message"] = "Requested folder does not exist"
            except:
                resp.status_code = api.status_codes.HTTP_500
                result["message"] = "There was a problem fetching"
        else:
            resp.status_code = api.status_codes.HTTP_400
            result["message"] = "The request was invalid(Check query)"
    else:
        resp.status_code = api.status_codes.HTTP_400
        result["message"] = "The request was invalid(Check request method)"

    resp.media = result


@api.route("/data")
async def data(req, resp):
    result = {}
    if req.method == "get":
        """
        フォルダ情報の取得

        Method：　GET
        エンドポイント：　localhost:3000/data
        クエリパラメータ：　folderpath=<絶対パス>
        """
        if "folderpath" in req.params:
            path = req.params["folderpath"]
            try:
                if os.path.isdir(path):
                    if path[:-1] != "/":
                        path += "/"
                    if os.path.isfile(path + "result.csv"):  # TODO: 結果ファイル名/
                        data = []
                        with open(path + "result.csv", 'r') as f:
                            for row in csv.DictReader(f):
                                print(row)
                                row["cataractScoreAI"] = bool(int(row["cataractScoreAI"]))
                                row["hypertensionScoreAI"] = bool(int(row["hypertensionScoreAI"]))
                                row["cataractScoreDr"] = bool(int(row["cataractScoreDr"]))
                                row["hypertensionScoreDr"] = bool(int(row["hypertensionScoreDr"]))
                                data.append(row)

                        result["data"] = data

                        # TODO: ここで csv/db を json にして返す
                        # # 以下はサンプル
                        # result = {
                        #     "data": [
                        #         {
                        #             "id"                 : 0,
                        #             "image"              : "Thinkoutlogo.png",
                        #             "cataractScoreAI"    : True,
                        #             "hypertensionScoreAI": False,
                        #             "cataractScoreDr"    : True,
                        #             "hypertensionScoreDr": True,
                        #             "note"               : "sample"
                        #         },
                        #         {
                        #             "id"                 : 1,
                        #             "image"              : "Thinkoutlogo.png",
                        #             "cataractScoreAI"    : False,
                        #             "hypertensionScoreAI": False,
                        #             "cataractScoreDr"    : False,
                        #             "hypertensionScoreDr": False,
                        #             "note"               : "sample"
                        #         },
                        #         {
                        #             "id"                 : 2,
                        #             "image"              : "Thinkoutlogo.png",
                        #             "cataractScoreAI"    : True,
                        #             "hypertensionScoreAI": True,
                        #             "cataractScoreDr"    : True,
                        #             "hypertensionScoreDr": True,
                        #             "note"               : "sample"
                        #         }
                        #     ]
                        # }
                        pass
                    else:
                        result["dataExist"] = False
                        result["message"] = "No data in the folder"
                else:
                    resp.status_code = api.status_codes.HTTP_404
                    result["message"] = "Requested folder does not exist"

            except:
                resp.status_code = api.status_codes.HTTP_500
                result["message"] = "There was a problem fetching"
        else:
            resp.status_code = api.status_codes.HTTP_400
            result["message"] = "The request was invalid(Query Required)"

    elif req.method == "post":
        """
        フォルダの画像診断

        Method: POST
        エンドポイント: localhost:3000/data
        リクエストボディ:
            {
              "folderpath": <絶対パス>
            }
        """
        try:
            body = await req.media()
            if "folderpath" in body:
                path = body["folderpath"]
            try:
                if os.path.isdir(path):
                    # 参考: http://skattun.hatenablog.jp/entry/2017/02/20/001924
                    pattern = ".*\.(jpg|png|bmp)"
                    files = [f for f in os.listdir(path) if re.search(pattern, f, re.IGNORECASE)]
                    if files:
                        try:
                            @api.background.task
                            def ai():
                                # ここにAI処理
                                pass

                            ai()
                            result["message"] = "Diagnosis completed"

                        except:  # TODO: 適宜 AI実行処理失敗例外文を追加
                            resp.status_code = api.status_codes.HTTP_500
                            result["message"] = "There was a problem during diagnosis"

                    else:
                        resp.status_code = api.status_codes.HTTP_404
                        result["message"] = "The image does not exist in the requested folder"

                else:
                    resp.status_code = api.status_codes.HTTP_404
                    result["message"] = "Requested folder does not exist"

            except:
                resp.status_code = api.status_codes.HTTP_500
                result["message"] = "There was a problem fetching"

            else:
                resp.status_code = api.status_codes.HTTP_400
                result["message"] = "The request was invalid(Check request body)"
        except:
            resp.status_code = api.status_codes.HTTP_400
            result["message"] = "The request was invalid(Check request body - No Content)"

    elif req.method == "put":
        """
        Method：　PUT
        エンドポイント: localhost:3000/data
        リクエストボディ
            {
              data:{
                "id": 0,
                "cataractScoreDr": true,
                "hypertensionScoreDr": false,
                "note": "sample"
              },
              "folderpath": <絶対パス>
            }
        """
        result = {}
        query = await req.media()
        if ("folderpath" in query) and ("data" in query):
            if ("id" and "cataractScoreDr" and "hypertensionScoreDr" and "note") in query["data"]:
                path = query["folderpath"]
                if os.path.isdir(path):
                    try:
                        if path[:-1] != "/":
                            path += "/"
                        if os.path.isfile(path + "result.csv"):  # TODO: 結果ファイル名
                            data = []
                            with open(path + "result.csv", 'r') as f:
                                for row in csv.DictReader(f):
                                    if row["id"] == query["data"]["id"]:
                                        row["cataractScoreDr"] = int(query["data"]["cataractScoreDr"])
                                        row["hypertensionScoreDr"] = int(query["data"]["hypertensionScoreDr"])
                                        row["note"] = query["data"]["note"]
                                    data.append(row)
                            header = ['id', 'image', 'cataractScoreAI', 'hypertensionScoreAI', 'cataractScoreDr', 'hypertensionScoreDr', 'note']
                            with open(path + "result.csv", 'w') as f:
                                writer = csv.DictWriter(f, fieldnames=header)
                                writer.writeheader()
                                writer.writerows(data)
                    except:
                        resp.status_code = api.status_codes.HTTP_500
                        result["message"] = "There was a problem updating"
                else:
                    resp.status_code = api.status_codes.HTTP_404
                    result["message"] = "Requested folder does not exist"
            else:
                resp.status_code = api.status_codes.HTTP_400
                result["message"] = "The request was invalid(Query Required)"
        else:
            resp.status_code = api.status_codes.HTTP_400
            result["message"] = "The request was invalid(Query Required)"

        pass

    resp.media = result


if __name__ == '__main__':
    api.run(port=3000)
