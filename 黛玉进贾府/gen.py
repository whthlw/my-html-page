# -*- coding: utf-8 -*-
import os, glob

LQ = chr(0x201c)
RQ = chr(0x201d)
CK = chr(0x2714)
CR = chr(0x2716)
NL = chr(10)
SQ = chr(39)

base = os.path.dirname(os.path.abspath(__file__))
html_files = glob.glob(os.path.join(base, '*.html'))
html_path = html_files[0]
print('Found: ' + html_path)

L = []

L.append('<script>')
L.append(SQ + 'use strict' + SQ + ';')
L.append('var curScene=0, answers=[], typingTimer=null;')
L.append('var SCENES=[')

# ============ Scene 1 ============
s = '{'
s += 'title:' + SQ + '第一关：弃舟登岸' + SQ + ','
s += 'img:' + SQ + './pic/scene1.jpeg' + SQ + ','
s += 'story:' + SQ
s += '黛玉自扬州乘船北上，终于抵达京城码头。'
s += '贾府早已派了轿子和婆子在此等候。'
s += '黛玉下船时，几个婆子连忙上前搀扶行礼。'
s += '黛玉虽年幼丧母、寄人篱下，却深知礼数不可废。'
s += '面对这些远道迎接的贾府下人，黛玉该如何回应？'
s += SQ + ','
s += 'choices:['
s += '{text:' + SQ + 'A. 微微颔首，轻声道'
s += LQ + '有劳各位' + RQ + SQ + ',correct:true},'
s += '{text:' + SQ + 'B. 低头不语，默默跟随' + SQ + ',correct:false},'
s += '{text:' + SQ + 'C. 高声致谢，连连作揖' + SQ + ',correct:false}'
s += '],'
s += 'correctIdx:0,'
s += 'feedback:' + SQ
s += CK + ' 正确！黛玉出身书香门第，虽是寄居，但礼数周全、不卑不亢。'
s += '微微颔首既显教养，' + LQ + '有劳各位' + RQ + '四字更见体贴。'
s += '原著中黛玉' + LQ + '步步留心，时时在意' + RQ + '，正是这般得体。'
s += SQ + ','
s += 'wrongFB:' + SQ
s += CR + ' 不太合适。低头不语显得失礼怯懦；'
s += '高声致谢则过于热络，不合大家闺秀的矜持。'
s += '黛玉应当不卑不亢，以微微颔首、轻声致谢为宜。'
s += SQ
s += '},'
L.append(s)

# ============ Scene 2 ============
s = '{'
s += 'title:' + SQ + '第二关：入城观街' + SQ + ','
s += 'img:' + SQ + './pic/scene2.jpeg' + SQ + ','
s += 'story:' + SQ
s += '轿子穿过京城繁华街市，黛玉坐在轿中，只觉外面车水马龙、热闹非凡。'
s += '这与扬州的秀丽婉约截然不同。'
s += '黛玉心中好奇，想看看这天子脚下的都城风貌，'
s += '但又想起母亲生前教导' + LQ + '大家闺秀不可轻易抛头露面' + RQ + '。'
s += '黛玉该如何做？'
s += SQ + ','
s += 'choices:['
s += '{text:' + SQ + 'A. 掀开轿帘大方观看' + SQ + ',correct:false},'
s += '{text:' + SQ + 'B. 从轿帘缝隙悄悄观察' + SQ + ',correct:true},'
s += '{text:' + SQ + 'C. 端坐不动，目不斜视' + SQ + ',correct:false}'
s += '],'
s += 'correctIdx:1,'
s += 'feedback:' + SQ
s += CK + ' 正确！从轿帘缝隙悄悄观察，既满足了好奇心，又不失闺秀体统。'
s += '原著写黛玉' + LQ + '从纱窗向外瞧了一瞧' + RQ + '，'
s += '正是这般含蓄细腻的观察方式，体现了她的聪慧与谨慎。'
s += SQ + ','
s += 'wrongFB:' + SQ
s += CR + ' 不太合适。掀帘大看有失体统；完全不看则不合常理，'
s += '也不符合黛玉聪敏好学的性格。'
s += '最佳做法是从缝隙中悄悄观察，既好奇又矜持。'
s += SQ
s += '},'
L.append(s)

# ============ Scene 3 ============
s = '{'
s += 'title:' + SQ + '第三关：进入荣国府' + SQ + ','
s += 'img:' + SQ + './pic/scene3.jpeg' + SQ + ','
s += 'story:' + SQ
s += '轿子终于停在荣国府大门前。'
s += '黛玉注意到正门未开，轿子从西角门进入。'
s += '进府后换了几次轿夫，黛玉暗暗观察这些规矩。'
s += '到了垂花门前，众婆子让黛玉下轿步行。'
s += '黛玉该如何应对这一路的见闻？'
s += SQ + ','
s += 'choices:['
s += '{text:' + SQ + 'A. 大声询问为何换人' + SQ + ',correct:false},'
s += '{text:' + SQ + 'B. 默默留意换人的规矩' + SQ + ',correct:true},'
s += '{text:' + SQ + 'C. 不以为意随意跟行' + SQ + ',correct:false}'
s += '],'
s += 'correctIdx:1,'
s += 'feedback:' + SQ
s += CK + ' 正确！黛玉' + LQ + '步步留心，时时在意' + RQ + '，'
s += '默默观察贾府的规矩排场，'
s += '既不多嘴多舌，又将一切看在眼里记在心中。这正是她聪慧谨慎的体现。'
s += SQ + ','
s += 'wrongFB:' + SQ
s += CR + ' 不太合适。大声询问显得冒失无礼；不以为意则辜负了黛玉的聪慧。'
s += '初入贾府，最明智的做法是默默观察、暗记规矩。'
s += SQ
s += '},'
L.append(s)

# ============ Scene 4 ============
s = '{'
s += 'title:' + SQ + '第四关：初见贾母' + SQ + ','
s += 'img:' + SQ + './pic/scene4.jpeg' + SQ + ','
s += 'story:' + SQ
s += '黛玉终于来到贾母房中。'
s += '外祖母一见黛玉，一把搂入怀中，心肝儿肉叫着大哭起来。'
s += '黛玉想起亡母，也忍不住哭泣。众人在旁劝慰。'
s += '此时黛玉该如何表现？'
s += SQ + ','
s += 'choices:['
s += '{text:' + SQ + 'A. 放声大哭以表思母之情' + SQ + ',correct:false},'
s += '{text:' + SQ + 'B. 努力克制悲伤，收住眼泪' + SQ + ',correct:true},'
s += '{text:' + SQ + 'C. 强颜欢笑安慰贾母' + SQ + ',correct:false}'
s += '],'
s += 'correctIdx:1,'
s += 'feedback:' + SQ
s += CK + ' 正确！黛玉虽然悲痛，但深知初来乍到不宜过分失态。'
s += '原著中' + LQ + '方欲拜见时，早被他外祖母一把搂入怀中' + RQ + '，'
s += '黛玉哭泣后很快收住，既表达了真情，又不失分寸。'
s += SQ + ','
s += 'wrongFB:' + SQ
s += CR + ' 不太合适。放声大哭虽是真情流露，但初来乍到过于失态；'
s += '强颜欢笑则显得虚伪。最得体的做法是适度表达悲伤后克制收住。'
s += SQ
s += '},'
L.append(s)

# ============ Scene 5 ============
s = '{'
s += 'title:' + SQ + '第五关：拜见舅母' + SQ + ','
s += 'img:' + SQ + './pic/scene5.jpeg' + SQ + ','
s += 'story:' + SQ
s += '贾母让黛玉拜见大舅母邢夫人和二舅母王夫人。'
s += '在王夫人房中，王夫人坐在西边下首，见黛玉来了，便往东让。'
s += '黛玉心想：这正房炕上的位次必有讲究。'
s += '王夫人再三让座，黛玉该如何做？'
s += SQ + ','
s += 'choices:['
s += '{text:' + SQ + 'A. 听从王夫人的话坐上首' + SQ + ',correct:false},'
s += '{text:' + SQ + 'B. 料定是长辈位次，不肯坐，只在挨炕的椅上坐了' + SQ + ',correct:true},'
s += '{text:' + SQ + 'C. 站着不坐以示恭敬' + SQ + ',correct:false}'
s += '],'
s += 'correctIdx:1,'
s += 'feedback:' + SQ
s += CK + ' 正确！黛玉料定那是贾政之位，绝不肯坐，只在挨炕的椅子上坐了。'
s += '原著中黛玉' + LQ + '度其位次，便不上炕，只向东边椅子上坐了' + RQ + '。'
s += '这体现了她的聪慧和对礼数的精准把握。'
s += SQ + ','
s += 'wrongFB:' + SQ
s += CR + ' 不太合适。贸然坐上首是不知礼数；一直站着又显得过于拘谨。'
s += '黛玉应当判断出那是长辈之位，选择合适的位置落座。'
s += SQ
s += '},'
L.append(s)

# ============ Scene 6 ============
s = '{'
s += 'title:' + SQ + '第六关：初见王熙凤' + SQ + ','
s += 'img:' + SQ + './pic/scene6.jpeg' + SQ + ','
s += 'story:' + SQ
s += '正说话间，只听后院中有人笑声说：'
s += LQ + '我来迟了，不曾迎接远客！' + RQ
s += '黛玉心想：这些人个个皆敛声屏气，这来者是谁，竟如此放诞无礼？'
s += '只见一群媳妇丫鬟围拥着一个人从后房门进来。'
s += '此人打扮与众姑娘不同，彩绣辉煌，恍若神妃仙子。'
s += '面对这位泼辣张扬的王熙凤，黛玉该如何应对？'
s += SQ + ','
s += 'choices:['
s += '{text:' + SQ + 'A. 起身行礼，自报家门' + SQ + ',correct:false},'
s += '{text:' + SQ + 'B. 含笑不语，暗中观察' + SQ + ',correct:true},'
s += '{text:' + SQ + 'C. 直接询问对方身份' + SQ + ',correct:false}'
s += '],'
s += 'correctIdx:1,'
s += 'feedback:' + SQ
s += CK + ' 正确！黛玉初见王熙凤时' + LQ + '不知是何许人也' + RQ + '，'
s += '便含笑不语、暗中观察。'
s += '待贾母介绍后才知是' + LQ + '凤辣子' + RQ + '。'
s += '这种沉稳观察的态度，正是大家闺秀的风范。'
s += SQ + ','
s += 'wrongFB:' + SQ
s += CR + ' 不太合适。在不知对方身份时贸然行礼或询问都不够稳妥。'
s += '黛玉的做法是先观察、后应对，待长辈介绍后再做回应。'
s += SQ
s += '},'
L.append(s)

# ============ Scene 7 ============
s = '{'
s += 'title:' + SQ + '第七关：初见贾宝玉' + SQ + ','
s += 'img:' + SQ + './pic/scene7.jpeg' + SQ + ','
s += 'story:' + SQ
s += '晚间，贾宝玉从庙里还愿回来。'
s += '黛玉一见，心中大吃一惊：好生奇怪，倒像在哪里见过一般。'
s += '宝玉问黛玉可曾读书、名字叫什么，又问有没有玉。'
s += '黛玉想起母亲说过宝玉有一块落草时衔来的通灵宝玉。'
s += '宝玉问' + LQ + '可也有玉没有' + RQ + '，黛玉该如何回答？'
s += SQ + ','
s += 'choices:['
s += '{text:' + SQ + 'A. 如实回答' + LQ + '我没有那个。你那玉亦是件罕物，岂能人人有的' + RQ + SQ + ',correct:true},'
s += '{text:' + SQ + 'B. 说' + LQ + '我也有一块' + RQ + '以拉近关系' + SQ + ',correct:false},'
s += '{text:' + SQ + 'C. 沉默不答避开话题' + SQ + ',correct:false}'
s += '],'
s += 'correctIdx:0,'
s += 'feedback:' + SQ
s += CK + ' 正确！黛玉如实回答，既诚实又得体。'
s += '原著中黛玉答道' + LQ + '我没有那个。你那玉亦是件罕物，岂能人人有的' + RQ + '。'
s += '然而宝玉听后竟摔玉发狂，这让黛玉十分自责，也为后文埋下伏笔。'
s += SQ + ','
s += 'wrongFB:' + SQ
s += CR + ' 不太合适。说谎不符合黛玉的性格；沉默不答则显得失礼。'
s += '黛玉应当如实回答，这也是原著中的情节。'
s += SQ
s += '}'
L.append(s)

L.append('];')

# ============ Game Logic Functions ============
L.append('function showScreen(id){')
L.append("  document.querySelectorAll('.screen').forEach(function(s){s.classList.remove('active')});")
L.append("  document.getElementById(id).classList.add('active');")
L.append('  window.scrollTo(0,0);')
L.append('}')

L.append('function startGame(){')
L.append('  curScene=0;')
L.append('  answers=[];')
L.append("  localStorage.removeItem('daiyu_save');")
L.append("  showScreen('gameScreen');")
L.append('  renderScene();')
L.append('}')

L.append('function renderScene(){')
L.append('  var sc=SCENES[curScene];')
L.append("  document.getElementById('sceneBg').src=sc.img;")
L.append("  document.getElementById('sceneTitle').textContent=sc.title;")
L.append("  document.getElementById('sceneNum').textContent=" + SQ + '第' + SQ + '+(curScene+1)+' + SQ + '关 / 共' + SQ + '+SCENES.length+' + SQ + '关' + SQ + ';')
L.append("  var stEl=document.getElementById('storyText');")
L.append("  stEl.textContent='';")
L.append('  clearInterval(typingTimer);')
L.append('  var ci=0;')
L.append('  typingTimer=setInterval(function(){')
L.append('    if(ci<sc.story.length){stEl.textContent+=sc.story[ci];ci++;}')
L.append('    else{clearInterval(typingTimer);}')
L.append('  },30);')
L.append("  var cd=document.getElementById('choicesDiv');")
L.append("  cd.innerHTML='';")
L.append('  var prev=answers[curScene];')
L.append('  sc.choices.forEach(function(ch,idx){')
L.append("    var btn=document.createElement('button');")
L.append("    btn.className='choice-btn';")
L.append('    btn.textContent=ch.text;')
L.append('    if(prev!==undefined){')
L.append('      btn.disabled=true;')
L.append("      if(idx===sc.correctIdx)btn.classList.add('correct');")
L.append("      else if(idx===prev)btn.classList.add('wrong');")
L.append('    }else{')
L.append('      btn.onclick=function(){handleChoice(idx);};')
L.append('    }')
L.append('    cd.appendChild(btn);')
L.append('  });')
L.append("  var fb=document.getElementById('feedbackDiv');")
L.append("  fb.className='feedback';")
L.append('  if(prev!==undefined){')
L.append("    fb.textContent=(prev===sc.correctIdx)?sc.feedback:sc.wrongFB;")
L.append("    fb.classList.add('show',(prev===sc.correctIdx)?'correct-fb':'wrong-fb');")
L.append('  }')
L.append("  document.getElementById('prevBtn').disabled=(curScene===0);")
L.append('  var isLast=(curScene===SCENES.length-1);')
L.append("  var nb=document.getElementById('nextBtn');")
L.append('  nb.disabled=(prev===undefined);')
L.append("  nb.textContent=isLast?" + SQ + '查看复盘' + SQ + ':' + SQ + '下一关' + SQ + ';')
L.append("  var pd=document.getElementById('progressDiv');")
L.append("  pd.innerHTML='';")
L.append('  for(var i=0;i<SCENES.length;i++){')
L.append("    var dot=document.createElement('span');")
L.append("    dot.className='dot';")
L.append("    if(answers[i]!==undefined)dot.classList.add('done');")
L.append("    if(i===curScene)dot.classList.add('cur');")
L.append('    pd.appendChild(dot);')
L.append('  }')
L.append('  saveGame();')
L.append('}')

L.append('function handleChoice(idx){')
L.append('  answers[curScene]=idx;')
L.append('  renderScene();')
L.append('}')

L.append('function nextScene(){')
L.append('  if(curScene<SCENES.length-1){curScene++;renderScene();}')
L.append('  else{showReview();}')
L.append('}')

L.append('function goPrev(){')
L.append('  if(curScene>0){curScene--;renderScene();}')
L.append('}')

L.append('function showReview(){')
L.append("  showScreen('reviewScreen');")
L.append('  var correct=0;')
L.append('  answers.forEach(function(ans,i){if(ans===SCENES[i].correctIdx)correct++;});')
L.append("  document.getElementById('scoreText').textContent=" + SQ + '你答对了 ' + SQ + '+correct+' + SQ + ' / ' + SQ + '+SCENES.length+' + SQ + ' 题' + SQ + ';')
L.append("  var rl=document.getElementById('reviewList');")
L.append("  rl.innerHTML='';")
L.append('  SCENES.forEach(function(sc,i){')
L.append("    var div=document.createElement('div');")
L.append("    div.className='review-item';")
L.append('    var isRight=(answers[i]===sc.correctIdx);')
L.append("    var h='<h3>'+sc.title+(isRight?' " + chr(0x2713) + "':' " + chr(0x2717) + "')+'</h3>';")
L.append("    h+='<div class=" + chr(34) + "your-ans" + chr(34) + ">你的选择：'+sc.choices[answers[i]].text+'</div>';")
L.append("    if(!isRight)h+='<div class=" + chr(34) + "correct-ans" + chr(34) + ">正确答案：'+sc.choices[sc.correctIdx].text+'</div>';")
L.append("    h+='<div class=" + chr(34) + "analysis" + chr(34) + ">'+sc.feedback.substring(2)+'</div>';")
L.append('    div.innerHTML=h;')
L.append('    rl.appendChild(div);')
L.append('  });')
L.append("  localStorage.removeItem('daiyu_save');")
L.append('}')

L.append('function restartGame(){')
L.append("  showScreen('startScreen');")
L.append('}')

L.append('function saveGame(){')
L.append('  try{')
L.append("    localStorage.setItem('daiyu_save',JSON.stringify({scene:curScene,answers:answers}));")
L.append('  }catch(e){}')
L.append('}')

L.append('function loadGame(){')
L.append('  try{')
L.append("    var d=JSON.parse(localStorage.getItem('daiyu_save'));")
L.append('    if(d&&d.answers&&d.answers.length>0){')
L.append('      curScene=d.scene;')
L.append('      answers=d.answers;')
L.append("      showScreen('gameScreen');")
L.append('      renderScene();')
L.append('      return true;')
L.append('    }')
L.append('  }catch(e){}')
L.append('  return false;')
L.append('}')

L.append('window.onload=function(){loadGame();};')
L.append('</script>')
L.append('</body></html>')

# ============ Write to HTML file ============
with open(html_path, 'a', encoding='utf-8') as f:
    for line in L:
        f.write(line + chr(10))

print('Done! Appended script section to ' + html_path)