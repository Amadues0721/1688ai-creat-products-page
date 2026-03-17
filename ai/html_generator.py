def generate_html(product_info: dict) -> str:
    """
    将AI生成的商品信息转换为HTML详情页
    """

    title = product_info.get("title", "")
    selling_points = product_info.get("selling_points", [])
    description = product_info.get("description", "")
    price = product_info.get("price", "")

    # 卖点转HTML
    selling_points_html = ""
    for point in selling_points:
        selling_points_html += f"<li>{point}</li>\n"

    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial;
                padding: 20px;
                line-height: 1.6;
            }}
            h1 {{
                color: #d81e06;
            }}
            .price {{
                color: #ff4400;
                font-size: 24px;
                font-weight: bold;
            }}
            ul {{
                background: #f8f8f8;
                padding: 15px;
            }}
        </style>
    </head>

    <body>

        <h1>{title}</h1>

        <p class="price">参考价格：¥{price}</p>

        <h2>核心卖点</h2>
        <ul>
            {selling_points_html}
        </ul>

        <h2>商品详情</h2>
        <p>{description.replace(chr(10), "<br>")}</p>

    </body>
    </html>
    """

    return html