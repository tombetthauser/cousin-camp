import os

def convert_markdown_to_html():
    md_file = "README.md"
    html_file = "index.html"
    css_file = "app.css"
    
    if not os.path.exists(md_file):
        print(f"Error: File '{md_file}' not found.")
        return
    
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.readlines()
    
    if not md_content:
        print(f"Error: File '{md_file}' is empty.")
        return
    
    html_content = ""
    in_list = False
    
    for line in md_content:
        line = line.strip()
        
        # Handle Markdown headers
        if line.startswith("# "):
            html_content += f"<h1>{line[2:].strip()}</h1>\n"
        elif line.startswith("## "):
            html_content += f"<h2>{line[3:].strip()}</h2>\n"
        elif line.startswith("### "):
            html_content += f"<h3>{line[4:].strip()}</h3>\n"
        
        # Handle unordered lists
        elif line.startswith("- "):
            if not in_list:
                html_content += "<ul>\n"
                in_list = True
            html_content += f"    <li>{line[2:].strip()}</li>\n"
        
        # Handle horizontal rules (---)
        elif line == "---":
            html_content += "<hr>\n"
        
        # Handle images in Markdown syntax (![alt text](url))
        elif line.startswith("!["):
            end_alt = line.find("]")
            start_url = line.find("(") + 1
            end_url = line.find(")")
            
            print("IMAGE")
            print(f"end_alt: {end_alt}")
            print(f"start_url: {start_url}")
            print(f"end_url: {end_url}")
            
            if end_alt != -1 and start_url != -1 and end_url != -1:
                alt_text = line[2:end_alt]
                img_url = line[start_url:end_url]
                # Print "IMAGE" when an image is encountered
                html_content += f'<img src="{img_url}" alt="{alt_text}">\n'
        
        # Handle other paragraphs and text
        else:
            if in_list:
                html_content += "</ul>\n"
                in_list = False
            if line:
                html_content += f"<p>{line}</p>\n"
    
    # Close any unclosed unordered list
    if in_list:
        html_content += "</ul>\n"
    
    # Wrap the converted content in the HTML template
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README</title>
    <link rel="stylesheet" href="{css_file}">
</head>
<body>
    {html_content}
</body>
</html>"""
    
    # Write the final HTML to a file
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_template)
    
    print(f"Converted '{md_file}' to '{html_file}'")

if __name__ == "__main__":
    convert_markdown_to_html()
