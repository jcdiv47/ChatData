# -*- coding:utf-8 -*-

from __future__ import annotations
from typing import List, Tuple
import time
import gradio as gr
from serve.app_modules.utils import *
from serve.app_modules.presets import small_and_beautiful_theme
from chat.agents.sql import SQLAgent
from chat.common.log import logger


def predict(
        text,
        chatbot,
        history,
):
    yield chatbot, history, "Thinking..."
    if text == "":
        yield chatbot, history, "Empty context."
        return
    sql_agent = SQLAgent()
    predictions = sql_agent.run(text)
    # for the purpose of stream output
    for i in range(len(predictions)):
        x = predictions[i]
        a, b = [[y[0], convert_to_markdown(y[1])] for y in history] + [[text, convert_to_markdown(x)]], history + [[text, x]]
        yield a, b, "Generating..."
        time.sleep(0.03)
    yield a, b, "Success"


def retry(
        text,
        chatbot,
        history,
):
    logger.info("Retry...")
    if len(history) == 0:
        yield chatbot, history, f"Empty context"
        return
    chatbot.pop()
    inputs = history.pop()[0]
    for x in predict(inputs, chatbot, history,):
        yield x


def postprocess(
        self,
        y: List[Tuple[str | None, str | None]]
) -> List[Tuple[str | None, str | None]]:
    """
    Parameters:
        y: List of tuples representing the message and response pairs.
        Each message and response should be a string, which may be in Markdown format.
    Returns:
        List of tuples representing the message and response.
        Each message and response will be a string of HTML.
    """
    if y is None or y == []:
        return []
    temp = []
    for x in y:
        user, bot = x
        if not detect_converted_mark(user):
            user = convert_asis(user)
        if not detect_converted_mark(bot):
            bot = convert_mdtext(bot)
        temp.append((user, bot))
    return temp


gr.Chatbot.postprocess = postprocess


def build_demo():
    with open("serve/assets/custom.css", "r", encoding="utf-8") as f:
        customCSS = f.read()

    with gr.Blocks(title="Scishang Chatbot DEMO", css=customCSS, theme=small_and_beautiful_theme) as demo:
        gr.Markdown(
            """
            <p align="center">
                <img src="https://raw.githubusercontent.com/jcdiv47/ChatData/master/serve/assets/scishang-logo.png" width=500 height=300>
            </p>
            """)
        history = gr.State([])
        user_question = gr.State("")
        with gr.Row():
            status_display = gr.Markdown("Success", elem_id="status_display")
        with gr.Row(equal_height=True):
            with gr.Column(scale=5):
                with gr.Row():
                    chatbot = gr.Chatbot(elem_id="chuanhu_chatbot", height="100%")
                with gr.Row():
                    with gr.Column(scale=12):
                        user_input = gr.Textbox(
                            show_label=False,
                            placeholder="Enter text",
                            container=False
                        )
                    with gr.Column(min_width=70, scale=1):
                        submitBtn = gr.Button("发送")
                    with gr.Column(min_width=70, scale=1):
                        cancelBtn = gr.Button("停止")
                with gr.Row():
                    emptyBtn = gr.Button(
                        "🧹 新的对话",
                    )
                    retryBtn = gr.Button("🔄 重新生成")
                    delLastBtn = gr.Button("🗑️ 撤回")

        predict_args = dict(
            fn=predict,
            inputs=[
                user_question,
                chatbot,
                history,
            ],
            outputs=[chatbot, history, status_display],
            show_progress=True,
        )
        retry_args = dict(
            fn=retry,
            inputs=[
                user_input,
                chatbot,
                history,
            ],
            outputs=[chatbot, history, status_display],
            show_progress=True,
        )

        reset_args = dict(
            fn=reset_textbox, inputs=[], outputs=[user_input, status_display]
        )

        # Chatbot
        transfer_input_args = dict(
            fn=transfer_input, inputs=[user_input], outputs=[user_question, user_input, submitBtn], show_progress=True
        )

        predict_event1 = user_input.submit(**transfer_input_args).then(**predict_args)

        predict_event2 = submitBtn.click(**transfer_input_args).then(**predict_args)

        emptyBtn.click(
            reset_state,
            outputs=[chatbot, history, status_display],
            show_progress=True,
        )
        emptyBtn.click(**reset_args)

        predict_event3 = retryBtn.click(**retry_args)

        delLastBtn.click(
            delete_last_conversation,
            [chatbot, history],
            [chatbot, history, status_display],
            show_progress=True,
        )
        cancelBtn.click(
            cancel_outputing, [], [status_display],
            cancels=[
                predict_event1, predict_event2, predict_event3
            ]
        )
    return demo


if __name__ == '__main__':
    demo = build_demo()
    demo.queue(concurrency_count=5, status_update_rate=10, api_open=False).launch(share=True)
