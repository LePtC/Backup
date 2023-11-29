from DrissionPage import WebPage

def get_cibs():
    liGetCibs = [] 

    x = page.ele('tag:cib-serp')
    y = x.sr.ele('tag:cib-conversation')
    for z in y.sr.eles('tag:cib-chat-turn'): # 多轮对话
        for u in z.sr.eles('tag:cib-message-group'): # 这层有俩 cib-message-group，user 和 response
            for m in u.sr.eles('tag:cib-message'): # response下可能分多条发

                if 'type="meta"' in m.html:
                    liGetCibs.append(m.sr.html) # 正在搜索xx
                else:
                    for w in m.sr.eles('tag:cib-shared'): # 主要内容
                        liGetCibs.append(w.html)

                if "cib-message-attributions" in m.sr.html: # 参考文献
                    try:
                        a = m.sr.ele('tag:cib-message-attributions')
                        liGetCibs.append(a.sr.html)
                    except Exception as e:
                        print(len(liGetCibs), 'cib-message-attributions', e)

    print(len(liGetCibs))
    return liGetCibs



from IPython.display import HTML, display

def display_liCib(liGetCibs):
    for x in liGetCibs:
        if x:
            if 'class="learn-more"' in x:
                display(HTML(parse_cib(x)))
            else:
                display(HTML(remove_button_content(x)))
        else:
            print("[warn] 遇到空消息")

display_liCib(liGetCibs)



import re

def remove_button_content(text):
    pattern = r'<button type="button" class="js-code-copy".*?</button>'
    clean_text = re.sub(pattern, '', text, flags=re.DOTALL)
    return clean_text

# 示例
# text = liGetCibs[9]
# clean_text = remove_svg_content(text)
# print(clean_text)



def link_css(htm):
    title = re.findall('title="(.*?)"', htm)
    if title:
        ret = '<p class="linkp">' + htm + title[0] + '</p>'
    else:
        ret = '<p class="linkp">' + htm + '</p>'
    return ret

def parse_cib(htm):
    pattern2 = "<a class=\"attribution-item(.+?)</a>" 
    matches2 = re.findall(pattern2, htm, re.DOTALL)
    result2 = ["<a class=\"attribution-item"+match+"</a>" for match in matches2]
#     print(result2)
    return ''.join([link_css(x) for x in result2])
    
# display(HTML(parse_cib(remove_button_content(liGetCibs[5]))))




def fuzzy(s, test):
    ss = s.strip()
    l = len(ss)
    if ss[int(l*0.1):int(l*0.9)] in test.strip():
        return True
    else:
        return False
    

def save_hist_skipdup(liCibs, rtime='', offset=0):
    if rtime:
        tm = str2unix(rtime)
    else:
        tm = time.time()
    print(f"[{unix2chs(tm)}] len:{len(liCibs)}")
    col = monTY['book']['chatnb2307']
    liDic = [{'_id': tm+i+offset, 'data':liCibs[i]} for i in range(len(liCibs))]
    
    liDone = list(col.find({}, sort=[("_id", -1)], limit=20, skip=0))
    done = [[x.get('data',''), unix2chs(x['_id'])] for x in liDone]
    
    liSel = []
    for y in liDic:
        if any([fuzzy(y['data'], d[0]) for d in done]): # 需要模糊匹配
            print("跳过重复", unix2chs(y["_id"]))
        else:
            liSel.append(y)
    
    print(col.insert_many(liSel))
#     printli_safe(liSel)

