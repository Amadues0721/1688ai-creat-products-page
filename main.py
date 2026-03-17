from ai.generator import generate_product_info
from ai.html_generator import generate_html

if __name__ == "__main__":
    result = generate_product_info("蓝牙耳机")

    if result:
        html = generate_html(result)

        # 保存成HTML文件
        with open("product.html", "w", encoding="utf-8") as f:
            f.write(html)

        print("HTML生成成功！已保存为 product.html")
    else:
        print("生成失败")