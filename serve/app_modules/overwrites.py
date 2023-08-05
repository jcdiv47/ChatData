from __future__ import annotations
# from .utils import *
import gradio as gr


with open("./assets/custom.js", "r", encoding="utf-8") as f:
    customJS = f.read()
with open("./assets/Kelpy-Codos.js", "r", encoding="utf-8") as f2:
    kelpyCodos = f2.read()


def reload_javascript():
    print("Reloading javascript...")
    js = f'<script>{customJS}</script><script>{kelpyCodos}</script>'

    def template_response(*args, **kwargs):
        res = GradioTemplateResponseOriginal(*args, **kwargs)
        res.body = res.body.replace(b'</html>', f'{js}</html>'.encode("utf8"))
        res.init_headers()
        return res

    gr.routes.templates.TemplateResponse = template_response


GradioTemplateResponseOriginal = gr.routes.templates.TemplateResponse
