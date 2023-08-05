database_schema_dict = [
    {
        "table_name": "stores",
        "column_names": [
                "store_id", "brand_id", "brand_name", "mall_id", "mall_name", "category", "city", "open_date", "close_date", "area"
            ]
    },
    {
        "table_name": "malls",
        "column_names": [
                "mall_id", "mall_name", "address", "city", "open_date", "close_date", "area"
            ]
    },
    {
        "table_name": "brand_similarity",
        "column_names": [
            "brand_id", "brand_name", "brand_name_similar", "similarity"
        ]
    }
]

database_schema_string = "\n".join(
    [
        f"Table: {table['table_name']}\nColumns: {', '.join(table['column_names'])}"
        for table in database_schema_dict
    ]
)

SQL_AGENT_FUNCTIONS = [
    {
        "name": "ask_database",
        "description": "Use this function to answer user questions. Output should be a fully formed SQL query.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": f"""
                            SQL query extracting info to answer the user's question.
                            SQL should be written using this database schema:
                            {database_schema_string}
                            The query should be returned in plain text, not in JSON.
                            """,
                }
            },
            "required": ["query"],
        },
    },
]

TOKENIZE_WARMUP_MESSAGES = [
    {
        "role": "system",
        "content": """
        You are a helpful assistant who is proficient in the task of Named Entity Recognition.
        You are fluent in both English and Chinese.
        """
    },
    {
        "role": "user",
        "content": """
        Given an input text in Chinese, extract the important entities mentioned in the text below.
        First extract all mall names, then extract all brand names, finally extract all city names.
        Please return a list of dictionaries in json format with keys ``name`` for original value in string and ``type`` for entity type.
        Here is the text:
        Starbucks在广州市的面积最大的门店所在商场名称
        """
    },
    {
        "role": "assistant",
        "content": """
        Entities 1: [
    {"name": "海蓝之谜", "type": "brand"},
    {"name": "上海市", "type": "city"}
    ]"""
    },
]


# Text 1:
# Entities 1: [
#     {"name": "海蓝之谜", "type": "brand"},
#     {"name": "上海市", "type": "city"}
# ]
# ##
# Text 2: Starbucks在环贸iapm有多少门店
# Entities 2: [
#     {"name": "Starbucks", "type": "brand"},
#     {"name": "环贸iapm", "type": "mall"}
# ]
# ##
# Text 3: 请列出和耐克最相似的5个品牌
# Entities 3: [
#     {"name": "耐克", "type": "brand"}
# ]

