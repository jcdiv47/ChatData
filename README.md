
# Quick Start

- Download embeddings files and put them under ``chat/db/``.
- A proxy is also required since the project needs to access openai models.

It is recommended to use **python3.10** and set up an environment, either via venv or conda.

```bash
pip install -r requirements.txt
```

Set up openai api key in environment variable ``OPENAI_API_KEY``.

Run
```bash
python app.py
```
to set up and open a running gradio interface.

To be able to query for data in the database,
the following variables have to be first set up in environment variables:

- ``MYSQL_USER``
- ``MYSQL_PASSWORD``
- ``MYSQL_HOST``
- ``MYSQL_PORT``
- ``MYSQL_DB``

MySQL is the default and the only supported database dialect for the moment.


# Tests
## Questions to ask:

The following are some test questions.

### Probably answers correctly:
- 请告诉sk-2在上海市有多少家门店
- 请列出和sk-2最相似的5个品牌
- 那么海蓝之谜在上海市面积最大的5个门店在什么商场
- 兴业太古汇里有多少家护肤化妆品的门店
- 哪个护肤化妆品的品牌在兴业太古汇的开业时间最长

### Not so much:
- sk-ii在上海最大的5个门店所在的商场中，开业时间最早的两个商场


# Reference
[\[Best practices for prompt engineering with OpenAI API\]](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)