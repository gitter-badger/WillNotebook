from browser import document, alert, ajax, window
from browser.html import TEXTAREA, CENTER, DIV, PRE, FORM, INPUT, BUTTON, BR

jq = window.jQuery.noConflict(True)

def shortcuts(ev):
    id = document.activeElement.id
    if ev.shiftKey and ev.which == 13:
        handleShiftEnter(id)
        ev.returnValue = False
    elif ev.which == 13:
        handleInEnter(id)
    elif ev.shiftKey and ev.which == 46:
        handleShiftDelete(id)
        ev.returnValue = False
    elif ev.altKey and ev.which == 78:
        handleAltN(id)
        ev.returnValue = False
    elif ev.shiftKey and ev.which == 38:
        handleShiftUp(id)
        ev.returnValue = False
    elif ev.shiftKey and ev.which == 40:
        handleShiftDown(id)
        ev.returnValue = False
    elif ev.which == 27:
        handleEsc(id)
        ev.returnValue = False
    elif ev.altKey and ev.which == 67:
        handleInAltC(id)
        ev.returnValue = False
    elif ev.altKey and ev.which == 69:
        handleInAltE(id)
        ev.returnValue = False
    elif ev.altKey and ev.which == 49:
        handleInAlt1(id)
        ev.returnValue = False
    elif ev.altKey and ev.which == 50:
        handleInAlt2(id)
        ev.returnValue = False
    elif ev.altKey and ev.which == 51:
        handleInAlt3(id)
        ev.returnValue = False
    elif ev.altKey and ev.which == 52:
        handleInAlt4(id)
        ev.returnValue = False
    elif ev.altKey and ev.which == 53:
        handleInAlt5(id)
        ev.returnValue = False
    elif ev.altKey and ev.which == 73:
        handleInAltI(id)
        ev.returnValue = False

def outShortcuts(ev):
    global lastFocused
    try:
        id = document.activeElement.id
        print('Focused on: ',id)
        if ev.shiftKey and ev.which == 38:
            handleShiftUp(id)
            ev.returnValue = False
        elif ev.shiftKey and ev.which == 40:
            handleShiftDown(id)
            ev.returnValue = False
        elif ev.which == 13:
            handleOutEnter(id)
            ev.returnValue = False
        elif ev.shiftKey and ev.which == 46:
            handleShiftDelete(id)
            ev.returnValue = False
        elif ev.altKey and ev.which == 78:
            handleAltN(id)
            ev.returnValue = False
        elif ev.altKey and ev.which == 67:
            handleOutAltC(id)
            ev.returnValue = False
        elif ev.altKey and ev.which == 69:
            handleOutAltE(id)
            ev.returnValue = False
        elif ev.altKey and ev.which == 49:
            handleOutAlt1(id)
            ev.returnValue = False
        elif ev.altKey and ev.which == 50:
            handleOutAlt2(id)
            ev.returnValue = False
        elif ev.altKey and ev.which == 51:
            handleOutAlt3(id)
            ev.returnValue = False
        elif ev.altKey and ev.which == 52:
            handleOutAlt4(id)
            ev.returnValue = False
        elif ev.altKey and ev.which == 53:
            handleOutAlt5(id)
            ev.returnValue = False
        elif ev.altKey and ev.which == 73:
            handleOutAltI(id)
            ev.returnValue = False
    except Exception as e:
        print(e)

def handleShiftEnter(id):
    global page
    id = id.replace('S','')
    id = id.replace('C','')
    id = id.replace('L','')
    print('ID: ',id)
    print('last: ',page[-1])
    if id == page[-1]:
        newCell()
    else:
        idDown = str(page[page.index(id)+1])
        if not document[idDown].style.display == 'none':
            document[idDown].focus()
        else:
            document['co'+idDown].focus()
    try:
        eval(id)
    except Exception as e:
        print('Exception: ',e)

def handleAltN(id):
    print('Insert after ',id)
    global jq,lastFocused,cellCounter
    id = id.replace('co','')
    newCell()
    jq("#c"+str(cellCounter-1)).insertAfter("#co"+id)
    jq("#co"+str(cellCounter-1)).insertAfter("#c"+str(cellCounter-1))
    document[str(cellCounter-1)].focus()
    document[id].style.display = 'none'
    sendNewCell(page.index(id)+1)
    page.insert(str(page.index(id)+1),page.pop())

def handleShiftDelete(id):
    if id == page[-1]:
        document[id].value = ''
    elif 'co' in id:
        del document[id] #del co
        del document[id[0]+id[2:]] #del c
        focusNextCell(id)
        sendDeleteCell(page.index(id[2:]))
        page.remove(id[2:])
    else: #soh numero
        del document['co'+id]
        del document['c'+id]
        focusNextCell(id)
        sendDeleteCell(page.index(id))
        page.remove(id)
    updateSectionNumbers()
    updateFigureNumbers()
    window.math.reNumber()
    print('Cell deleted')
    print(page)

lastFocused = None
def lastFocus(ev):
    global lastFocused
    lastFocused = ev.target.id

def handleShiftUp(id):
    global page
    print('ShiftUp')
    print('Active element: ',id)
    print(page)
    id = id.replace('c','').replace('o','')
    if not id == page[0]:
        print('not first')
        upId = page.index(id)-1
        print('Focus on: o',page[upId])
        if document[page[upId]].style.display == 'none':
            print('if')
            document['co'+page[upId]].focus()
        else:
            document[page[upId]].focus()
            print('else')

def handleShiftDown(id):
    print('ShiftDown')
    print('Active element: ',id)
    id = id.replace('c','').replace('o','')
    global page
    if not id == page[-1]:
        print('not last')
        downId = page.index(id)+1
        print('Focus on: o',downId)
        if document[page[downId]].style.display == 'none':
            document['co'+page[downId]].focus()
        else:
            document[page[downId]].focus()

def handleOutEnter(id):
    id = id.replace('co','')
    document[id].style.display = 'block'
    try:
        ## No caso de imagens
        document['F'+id].style.display = 'block'
    except:
        pass
    document[id].focus()

def handleInEnter(id):
    try:
        document[id].rows += 1
    except:
        pass

def handleEsc(id):
    document[id].style.display = 'none'
    try:
        ## No caso de imagens
        document['F'+id].style.display = 'none'
    except:
        pass
    document['co'+id].focus()

def handleInAltC(id):
    if not '#code <label>\n' in document[id].value:
        document[id].value = '#code <label>\n' + document[id].value

def handleInAltE(id):
    if not '!eq <label>\n' in document[id].value:
        document[id].value = '!eq <label>\n' + document[id].value

def handleInAlt1(id):
    if not '!# ' in document[id].value:
        document[id].value = '!# ' + document[id].value

def handleInAlt2(id):
    if not '!## ' in document[id].value:
        document[id].value = '!## ' + document[id].value

def handleInAlt3(id):
    if not '!### ' in document[id].value:
        document[id].value = '!### ' + document[id].value

def handleInAlt4(id):
    if not '!#### ' in document[id].value:
        document[id].value = '!#### ' + document[id].value

def handleInAlt5(id):
    if not '!##### ' in document[id].value:
        document[id].value = '!##### ' + document[id].value

def handleInAltI(id):
    global page,cellCounter
    del document['co'+id]
    del document['c'+id]
    newInImg = CENTER(FORM([INPUT(type="file",name='img',id=id),BR(),'Label:',INPUT(name='label',id="L"+id),BR(),'Caption:',INPUT(name='caption',id="C"+id),BR(),'Source:',INPUT(name='source',id="S"+id)],id='F'+id,enctype="multipart/form-data",method="POST",action="image"),id="c"+id)
    newOutCell = CENTER(DIV(style={'width':800,'height':200,'text-align':'justify'}, id='o'+id),id="co"+id,tabindex="0")
    document['page'] <= newInImg
    document['page'] <= newOutCell
    bindShortcuts(newInImg)
    bindOutShortcuts(newOutCell)
    newInImg.bind('blur',lastFocus)
    newOutCell.bind('blur',lastFocus)
    document[id].focus()

def handleOutAltC(id):
    handleAltN(id)
    handleInAltC(nextId(id))
    
def handleOutAltE(id):
    handleAltN(id)
    handleInAltE(nextId(id))

def handleOutAlt1(id):
    handleAltN(id)
    handleInAlt1(nextId(id))

def handleOutAlt2(id):
    handleAltN(id)
    handleInAlt2(nextId(id))

def handleOutAlt3(id):
    handleAltN(id)
    handleInAlt3(nextId(id))

def handleOutAlt4(id):
    handleAltN(id)
    handleInAlt4(nextId(id))

def handleOutAlt5(id):
    handleAltN(id)
    handleInAlt5(nextId(id))

def handleOutAltI(id):
    global page,cellCounter
    print('calledAltI')
    id = id.replace('co','')
    newImageCell()
    print('Ended')
    print('insert after',id)
    print('cell',cellCounter-1)
    jq("#c"+str(cellCounter-1)).insertAfter("#co"+id)
    jq("#co"+str(cellCounter-1)).insertAfter("#c"+str(cellCounter-1))
    document[str(cellCounter-1)].focus()
    document[id].style.display = 'none'
    sendNewCell(page.index(id)+1)
    page.insert(str(page.index(id)+1),page.pop())

def newImageCell():
    global page,cellCounter
    try:
        id = str(cellCounter)
        newInImg = CENTER(FORM([INPUT(type="file",name='img',id=id),BR(),'Label:',INPUT(name='label',id="L"+id),BR(),'Caption:',INPUT(name='caption',id="C"+id),BR(),'Source:',INPUT(name='source',id="S"+id)],id='F'+id,enctype="multipart/form-data",method="POST",action="image"),id="c"+id,Class="dontprint")
        newOutCell = CENTER(DIV(style={'width':800,'height':200,'text-align':'justify'}, id='o'+id),id="co"+id,tabindex="0")
        document['page'] <= newInImg
        document['page'] <= newOutCell
        bindShortcuts(newInImg)
        bindOutShortcuts(newOutCell)
        newInImg.bind('blur',lastFocus)
        newOutCell.bind('blur',lastFocus)
        document[id].focus()
        page.append(id)
        cellCounter += 1
    except Exception as e:
        print('Exceptio: ',e)

cellCounter = 0
def newCell():
    global page,cellCounter
    id = str(cellCounter)
    newInCell = CENTER(TEXTAREA(style={'width':800,'height':200},id=id,action="evalCell"),id="c"+id,Class="dontprint")
    newOutCell = CENTER(DIV(style={'width':800,'height':200,'text-align':'justify'}, id='o'+id),id="co"+id,tabindex="0")
    document['page'] <= newInCell
    document['page'] <= newOutCell
    bindShortcuts(newInCell)
    bindOutShortcuts(newOutCell)
    newInCell.bind('blur',lastFocus)
    newOutCell.bind('blur',lastFocus)
    document[id].focus()
    page.append(id)
    print(page)
    cellCounter += 1

def showCode(ev):
    id = ev.currentTarget.children[0].id[1:]
    print('Show code id ',id)
    document[id].style.display = 'block'
    
# To keep track of the right output cell
outIndex = None
def eval(id):
    # Handles the cell evaluation
    global outIndex,page
    outIndex = str(id)
    print('OutIndex ',outIndex)
    if document[id].tagName == 'TEXTAREA':
        send(document[str(id)].value)
        document[id].style.display = 'none'
    else:
        img = document[id].files[0]
        label = document['L'+id].value
        source = document['S'+id].value
        caption = document['C'+id].value
        sendImg(img,label,source,caption)
        document['F'+id].style.display = 'none'
        document[id].style.display = 'none'
    print('submitted')
    
def bindShortcuts(element):
    element.bind('keydown',shortcuts)
    print('Binded ',element.id)

def bindOutShortcuts(element):
    element.bind('dblclick',showCode)
    element.bind('keydown',outShortcuts)

def receive(req):
	# Receiving the server handler output as req.text
    global outIndex
    try:
        print('Receiving...',outIndex)
        if req.status==200 or req.status==0:
            print('Received: ',req.text)
            document['o'+outIndex].innerHTML =  req.text
            window.math.reNumber()
            #window.MathJax.Hub.Queue(["Typeset",window.MathJax.Hub])
            updateSectionNumbers()
            print('o'+outIndex)
    except Exception as e:
        print('Exception: ',e)

def receiveImg(req):
	# Receiving the server handler output as req.text
    global outIndex
    try:
        print('Receiving...',outIndex)
        document['o'+outIndex].innerHTML = req
        updateFigureNumbers()
        print('o'+outIndex)
    except Exception as e:
        print('Exception: ',e)

def send(content):
    # Sends the cell content to the server handlers
    req = ajax.ajax()
    req.bind('complete',receive)
    req.open('POST','http://127.0.0.1:8080/evalCell',True)
    req.set_header('content-type','application/x-www-form-urlencoded')
    req.send({'cell':page.index(outIndex),'content':content})

def sendImg(img,label,source,caption):
    # Sends the cell content to the server handlers
    window.uploadFile(page.index(outIndex),img,label,source,caption)

def openFile(ev):
    req = ajax.ajax()
    req.bind('complete',renderFile)
    req.open('post','http://127.0.0.1:8080/openFile',True)
    req.set_header('content-type','application/x-www-form-urlencoded')
    req.send({'filename':document['filename'].value})

def sendNewCell(index):
    print('New cell pending')
    req = ajax.ajax()
    req.bind('complete',ack)
    req.open('post','http://127.0.0.1:8080/newCell',True)
    req.set_header('content-type','application/x-www-form-urlencoded')
    req.send({'index':index})

def sendDeleteCell(index):
    print('Delete cell pending')
    req = ajax.ajax()
    req.bind('complete',ack)
    req.open('post','http://127.0.0.1:8080/deleteCell',True)
    req.set_header('content-type','application/x-www-form-urlencoded')
    req.send({'index':index})

def ack(req):
    print('ACK: ',req.text)

def renderFile(req):
    global page,cellCounter
    if req.status==200 or req.status==0:
        del document['page']
        document <= DIV(id="page")
        page = []
        print('Done deleting')
        try:
            document['page'].innerHTML +=  req.text
            cellCounter = 0
            while str(cellCounter) in document:
                print('Cell :',cellCounter)
                bindShortcuts(document['c'+str(cellCounter)])
                bindOutShortcuts(document['co'+str(cellCounter)])
                page.append(str(cellCounter))
                print(page)
                cellCounter += 1
            newCell()
            window.math.reNumber()
            #window.MathJax.Hub.Queue(["Typeset",window.MathJax.Hub])
            updateSectionNumbers()
            updateFigureNumbers()
            print('Done loading file')
        except Exception as e:
            print(e)

def focusNextCell(id):
    global page
    idDown = nextId(id)
    if document[idDown].style.display == 'none':
        document['co'+idDown].focus()
    else:
        document[idDown].focus()

def nextId(id):
    global page
    id = id.replace('c','').replace('o','')
    if page.index(id)+1 < len(page):
        return page[page.index(id)+1]
    else:
        return page[-1]

def updateSectionNumbers():
    def replaceNumber(content,tag,numbering):
        if '<span>' in content:
            heading = content[content.index('</span>'):]
            print('If: ',heading)
            return tag+'<span>'+numbering+heading
        else:
            heading = content.replace(tag,'')
            print('Else: ',heading)
            return tag+'<span>'+numbering+'</span>'+heading

    S,SS,SSS,SSSS,SSSSS = 0,0,0,0,0
    for id in page:
        html = document['o'+id].html
        if html:
            if '<h1>' in html:
                S+=1
                SS,SSS,SSSS,SSSSS = 0,0,0,0
                document['o'+id].html = replaceNumber(html,'<h1>',str(S)+'. ')
            elif '<h2>' in html:
                SS+=1
                SSS,SSSS,SSSSS = 0,0,0
                document['o'+id].html = replaceNumber(html,'<h2>',str(S)+'.'+str(SS)+'. ')
            elif '<h3>' in html:
                SSS+=1
                SSSS,SSSSS = 0,0
                document['o'+id].html = replaceNumber(html,'<h3>',str(S)+'.'+str(SS)+'.'+str(SSS)+'. ')
            elif '<h4>' in html:
                SSSS+=1
                SSSSS = 0
                document['o'+id].html = replaceNumber(html,'<h4>',str(S)+'.'+str(SS)+'.'+str(SSS)+'.'+str(SSSS)+'. ')
            elif '<h5>' in html:
                SSSSS+=1
                document['o'+id].html = replaceNumber(html,'<h5>',str(S)+'.'+str(SS)+'.'+str(SSS)+'.'+str(SSSS)+'.'+str(SSSSS)+'. ')
                
def updateFigureNumbers():
    def replaceNumber(content,tag,numbering):
        print('Content: ',content)
        if '<span>' in content:
            caption = content[content.index('</span>'):]
            print('If: ',caption)
            return '<br><center>'+tag+'<span>'+numbering+caption
        else:
            caption = content[content.index(tag)+len(tag):]
            print('Else: ','<center>'+tag+'<span>'+numbering+'</span>'+caption)
            return '<br><center>'+tag+'<span>'+numbering+'</span>'+caption

    N = 0
    for id in page:
        html = document['o'+id].html
        if html:
            if '<figcaption>' in html:
                N+=1
                document['o'+id].html = replaceNumber(html,'<figcaption>','<b>Fig. '+str(N)+':</b> ')

# Initialize the first cell
page = []
newCell()
document['openButton'].bind('click',openFile)
window.receiveImg = receiveImg
