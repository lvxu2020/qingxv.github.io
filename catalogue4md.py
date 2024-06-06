import re
import argparse

def process_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    toc = []
    processed_lines = []
    header_count = {}
    current_level = [0, 0, 0, 0, 0, 0]  # 最多支持六级标题

    # 正则表达式匹配标题和现有的锚点标签
    header_regex = re.compile(r'^(#{1,6})\s*(.*)')
    anchor_regex = re.compile(r'\s*<a id="([^"]+)"></a>')

    for line in lines:
        header_match = header_regex.match(line)
        if header_match:
            header_level = len(header_match.group(1))
            header_text = header_match.group(2).strip()

            # 生成标题对应的锚点 ID
            header_id = re.sub(r'\W+', '-', header_text.lower()).strip('-')
            current_level[header_level - 1] += 1
            header_id = f"{header_id}-{current_level[header_level - 1]}"
            
            # 添加标题到目录
            toc.append(f"{'    ' * (header_level - 1)}- [{header_text}](#{header_id})\n")
            
            # 添加锚点到标题
            line = re.sub(anchor_regex, '', line)  # 移除现有的锚点标签
            line = f"{'#' * header_level} {header_text} <a id=\"{header_id}\"></a>\n"
        
        processed_lines.append(line)
    
    # 将目录添加到文件开头
    toc.insert(0, "# 目录\n\n")
    processed_lines = toc + ["\n---\n"] + processed_lines
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)

def clean_existing_anchors_and_toc(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()  # 将内容读取为行列表
    
    # 寻找目录开始和结束位置
    toc_start_index = None
    toc_end_index = None

    for i, line in enumerate(content):
        if line.strip() == "# 目录":
            toc_start_index = i
        elif line.strip() == "---":
            toc_end_index = i
            break

    # 更新文件内容
    if toc_start_index is not None and toc_end_index is not None:
        # 替换现有目录内容
        content = content[:toc_start_index] + [""] + content[toc_end_index + 1:]

    # 将内容重新组合成字符串
    content = ''.join(content)

    # 正则表达式匹配现有的锚点标签
    anchor_regex = re.compile(r'<a id="([^"]+)"></a>')

    # 移除所有现有的锚点标签
    content = re.sub(anchor_regex, '', content)

    # 写回文件或打印内容
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    parser = argparse.ArgumentParser(description="Process a Markdown file to add TOC and anchors.")
    parser.add_argument('-file', type=str, required=True, help="Path to the Markdown file.")
    args = parser.parse_args()

    clean_existing_anchors_and_toc(args.file)
    process_markdown(args.file)

if __name__ == "__main__":
    main()