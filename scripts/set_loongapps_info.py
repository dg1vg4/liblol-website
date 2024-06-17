# coding=utf-8
import pandas as pd
import json
import os


# wget -O ../static/data/loongapplist-update.csv https://github.com/AOSC-Dev/liblol-website/releases/download/latest/loongapplist-update.csv
df = pd.read_csv(
    "../static/data/loongapplist-update.csv", engine="python", encoding="utf-8-sig"
)
# 以appid生成文件名
for id in df["编号"]:
    filename = "../content/docs/apps/loongapps/" + str(id) + ".md"
    title = str(df.loc[df["编号"] == id, "应用名称"].values)
    title = title[2:-2]
    version = str(df.loc[df["编号"] == id, "版本"].values)[2:-2]
    update_time = str(df.loc[df["编号"] == id, "更新时间"].values)[2:-2]
    package_url = str(df.loc[df["编号"] == id, "下载链接"].values)[2:-2]
    deb_size = str(df.loc[df["编号"] == id, "文件大小"].values)[2:-2]
    command = str(df.loc[df["编号"] == id, "可执行文件"].values)[2:-2]
    head = (
        "---\n" +
        "id: " + json.dumps(id, ensure_ascii=False) + "\n" +
        "title: " + json.dumps(title, ensure_ascii=False) + "\n" +
        "weight: " + json.dumps(id, ensure_ascii=False) + "\n" +
        "version: " + json.dumps(version, ensure_ascii=False) + "\n" +
        "updateTime: " + json.dumps(update_time, ensure_ascii=False) + "\n" +
        "debName: " + json.dumps(package_url, ensure_ascii=False) + "\n" +
        "debSize: " + json.dumps(deb_size, ensure_ascii=False) + "\n" +
        "command: " + json.dumps(command, ensure_ascii=False) + "\n" +
        "---\n"
    )
    with open(filename, "w", encoding="utf-8-sig") as file:
        file.write(head)



