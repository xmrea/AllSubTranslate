import os
import time
from utils import translate_and_compose
import re

for root, dirs, files in os.walk("./put_files_here"):
    for name in files:
        if re.match(r".*(?<!-\w{2})\.srt$", name):
            folder = os.path.abspath(root)
            source_file = os.path.join(folder, name)
            dest_file = os.path.join(folder, f'{os.path.splitext(name)[0]}-tr.srt')
            if os.path.isfile(dest_file):
                print(f'( {name} )  ᴛʀᴀɴsʟᴀᴛᴇᴅ ʙᴇғᴏʀᴇ!! \n')
            else:
                print(f' ᴛʀᴀɴsʟᴀᴛɪɴɢ...  ( {name} )')
                file_must_update = False
                with open(source_file, 'r', encoding="utf8") as srt_file:
                    srt_content = srt_file.read()
                    # remove extra numbers
                    new_srt_content = re.sub(r"(^|\n)(\d+)(\n+)(\d+\n+)", r"\n\2\n", srt_content)

                    # remove newLine from file beginning
                    new_srt_content = re.sub(r"^\n+", "", new_srt_content)

                    # replace &amp;
                    new_srt_content = new_srt_content.replace("&amp;", "&")
                if srt_content is not new_srt_content:
                    os.rename(source_file, source_file + ".backup")
                    with open(source_file, 'w', encoding="utf8") as srt_file_w:
                        srt_file_w.write(new_srt_content)
                translate_and_compose(source_file, dest_file, 'auto', 'tr', mode='naive', both=False)
                print(f'   √ ᴛʀᴀɴsʟᴀᴛᴇᴅ  ( {name} ) \n')
                time.sleep(3)

while True:
    for root, dirs, files in os.walk("./put_files_here"):
        for name in files:
            if re.match(r".*(?<!-\w{2})\.srt\.backup$", name):
                folder = os.path.abspath(root)
                file_to_remove = os.path.join(folder, name)
                os.remove(file_to_remove)
    print()
    os.system('pause')            
    break
