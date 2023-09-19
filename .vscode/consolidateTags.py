import re

def consolidate_tags(input_text):
    consolidated_tags = []
    consolidated_text = ""

    # Use regex to match the tags and content
    matches = re.findall(r'<v ([^>]*)>(.*?)</v>', input_text)

    prev_tag = None
    for tag, content in matches:
        if tag != prev_tag:
            if prev_tag is not None:
                consolidated_tags.append(f"</v>")
            consolidated_tags.append(f"<v {tag}>")
        consolidated_tags.append(content)
        prev_tag = tag

    if prev_tag is not None:
        consolidated_tags.append(f"</v>")
        
    consolidated_text = "".join(consolidated_tags)

    return consolidated_text

# Usage example
input_text = '''<v Jeroen>Hello</v><v Jeroen>How are you</v><v Simon>Goed</v><v Simon>En met jou</v><v Jeroen>Met mij gaat het goed</v><v Jeroen>Doei</v>
<v Simon>Houdoe</v>'''

consolidated_text = consolidate_tags(input_text)
print(consolidated_text)