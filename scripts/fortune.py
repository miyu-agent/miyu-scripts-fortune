#!/usr/bin/env python3
# Display name: Fortune
# 显示名称：吉凶占
# Description: Draw one fortune from seven grades, great blessing down to great misfortune, with a one-line meaning; the reading is yours.
# 描述：吉凶占：从大吉到大凶七档里抽一档，附一句释义，只抽签，不解读。
# Timeout: 10
# Clicall: no
# Parameters:
# {"type": "object", "properties": {
#   "question": {"type": "string", "description": "The question asked; echoed back, never used in the draw."}
# }}
import json
import secrets
import sys

FORTUNES = [
    ("大吉", "运势的最高峰，万事亨通，求财、姻缘、事业皆极顺遂。"),
    ("吉", "稳健的吉利状态。运势持久。"),
    ("中吉", "非常不错的好运，虽不如大吉猛烈，但平稳且有上升空间。"),
    ("小吉", "有小小的福气或幸运，平淡中带有喜悦，不宜过分强求大富大贵。"),
    ("末吉", "吉利的末尾。意味着目前处于谷底。"),
    ("凶", "运势不佳，容易遇到阻碍或犯错，需要格外小心谨慎、反省自身。"),
    ("大凶", "最差、最险恶的运势。多伴随口舌、破财或灾祸。"),
]


def main():
    try:
        args = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(f"错误：参数不是 JSON：{exc}")
        sys.exit(1)
    question = str(args.get("question") or "").strip()
    grade, meaning = secrets.choice(FORTUNES)
    out = [f"问题：{question}"] if question else []
    out.append(f"**{grade}**：{meaning}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
