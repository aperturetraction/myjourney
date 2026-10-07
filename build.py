import json,os
O='/mnt/user-data/outputs/myjourney'
SITE='https://YOUR-USERNAME.github.io/YOUR-REPO/'
for d in ('assets/css','assets/js'):os.makedirs(f'{O}/{d}',exist_ok=True)
T={
'tag':('Travel • Transfer • Tours • Mobility','旅游 • 接送 • 行程 • 出行'),
'slogan':('Your Journey. We Take Care of the Rest.','您的旅程，其余交给我们。'),
'hero.p':('Travel, airport transfers, private transport, tours, MPV rental and travel booking — all in one place.','旅游、机场接送、专车服务、行程游览、MPV 租赁与旅行预订，一站式安排。'),
'nav.home':('HOME','首页'),'nav.airport':('AIRPORT TRANSFER','机场接送'),'nav.private':('PRIVATE TRANSPORT','专车服务'),'nav.tours':('TOURS & PRIVATE GUIDE','行程与私人导游'),'nav.travel':('TRAVEL BOOKING','旅行预订'),'nav.mpv':('MPV RENTAL','MPV 租赁'),'nav.dest':('DESTINATIONS','目的地'),'nav.about':('ABOUT US','关于我们'),'nav.contact':('CONTACT','联系我们'),
'cta.wa':('WhatsApp Us','WhatsApp 联系我们'),'cta.explore':('Explore Our Services','了解我们的服务'),'cta.quote':('Get a Quote on WhatsApp','WhatsApp 获取报价'),'cta.enq':('Enquire on WhatsApp','WhatsApp 咨询'),'cta.avail':('Check Availability','查询是否有车'),'cta.book':('Book via WhatsApp','通过 WhatsApp 预订'),'cta.continue':('Continue on WhatsApp','通过 WhatsApp 继续'),'cta.reqav':('Request Availability','咨询可用情况'),'cta.reqq':('Request a Quote on WhatsApp','WhatsApp 申请报价'),'cta.tour':('Plan My Private Tour','规划我的私人行程'),
'svc.airport.t':('Airport Transfer','机场接送'),'svc.airport.d':('KLIA / KLIA2 / Hotel / Private Pickup','KLIA / KLIA2 / 酒店 / 私人接送'),'svc.airport.b':('Book Airport Transfer','预订机场接送'),
'svc.private.t':('Private Transport','专车服务'),'svc.private.d':('Point-to-point transport, hourly charter and private transportation.','点对点接送、按小时包车及私人用车。'),'svc.private.b':('Request Transport','申请用车'),
'svc.tours.t':('Tours & Private Guide','行程与私人导游'),'svc.tours.d':('Private tours, sightseeing and customised travel experiences.','私人行程、观光及定制旅行体验。'),'svc.tours.b':('Explore Tours','了解行程'),
'svc.travel.t':('Travel Booking','旅行预订'),'svc.travel.d':('Flight booking, hotel booking and travel packages.','机票预订、酒店预订及旅游套餐。'),'svc.travel.b':('Plan My Trip','规划我的旅程'),
'svc.mpv.t':('MPV Rental','MPV 租赁'),'svc.mpv.d':('MPV rental for families, groups and longer journeys.','适合家庭、团体及长途出行的 MPV 租赁。'),'svc.mpv.b':('Check MPV Availability','查询 MPV 可用情况'),
'p.airport':('Pickup and drop-off for KLIA, KLIA2, Kuala Lumpur, hotels and other destinations. Send your details and we will quote on WhatsApp.','提供 KLIA、KLIA2、吉隆坡、酒店及其他目的地的接送。提交信息后，我们将通过 WhatsApp 报价。'),
'p.private':('Point-to-point, hourly and full-day private transport. Tell us your plan and we will quote on WhatsApp.','点对点、按小时及全天专车服务。告诉我们您的计划，我们将通过 WhatsApp 报价。'),
'p.tours':('Tell us what you would like to see and we will help plan a private tour or guide. We do not publish fixed tour prices, so every trip is customised.','告诉我们您想看什么，我们协助安排私人行程或导游。我们不设固定行程价格，每趟行程均为定制。'),
'p.travel':('Flight arrangements, hotel recommendations and custom travel packages, arranged on request. We do not run a live airline or hotel booking system.','按需安排机票、酒店推荐及定制旅游套餐。我们没有实时的航班或酒店预订系统。'),
'p.mpv':('MPV rental only — Self Drive or With Driver. We do not offer sedan or hatchback rental. Availability is confirmed on request.','仅提供 MPV 租赁——自驾或配司机。我们不提供轿车或掀背车租赁。可用情况需经确认。'),
'ai1':('Airport pickup','机场接机'),'ai2':('Airport drop-off','送机服务'),'ai3':('KLIA Terminal 1','KLIA 第一航站楼'),'ai4':('KLIA Terminal 2 (KLIA2)','KLIA 第二航站楼（KLIA2）'),'ai5':('Kuala Lumpur','吉隆坡'),'ai6':('Hotels','酒店'),'ai7':('Other destinations on request','其他目的地（欢迎咨询）'),'ai8':('Private transfer','私人接送'),'ai9':('Family and group transfer','家庭及团体接送'),
'pt1':('Point-to-point transfer','点对点接送'),'pt2':('Hourly charter','按小时包车'),'pt3':('Full-day transport','全天用车'),'pt4':('Business transportation','商务用车'),'pt5':('Family transportation','家庭出行用车'),'pt6':('Event transportation','活动用车'),
'h.offer':('What we arrange','我们可以安排'),'h.req':('Send your details','提交您的需求'),'h.how':('How it works','流程说明'),'h.more':('More services','更多服务'),'h.faq':('FAQ','常见问题'),'h.svc':('Choose a service','选择服务'),
'st1':('Send your details','发送需求'),'st1d':('Fill in a short enquiry or tap WhatsApp Us.','填写简短咨询，或直接点击 WhatsApp。'),'st2':('Chat on WhatsApp','在 WhatsApp 沟通'),'st2d':('Our team follows up with you personally.','我们的团队将亲自跟进。'),'st3':('Receive a quote','获取报价'),'st3d':('We confirm price and availability.','我们确认价格与可用情况。'),'st4':('Confirm your booking','确认预订'),'st4d':('A booking is confirmed once agreed on WhatsApp.','在 WhatsApp 达成一致后才算预订确认。'),
'fq1':('Do I need to create an account?','需要注册账号吗？'),'fa1':('No. Send your enquiry and continue on WhatsApp.','不需要。提交咨询后直接在 WhatsApp 继续即可。'),
'fq2':('How much does it cost?','费用是多少？'),'fa2':('Prices depend on route, date, vehicle and requirements. Our team gives you a quote after your enquiry.','价格取决于路线、日期、车辆及需求。收到咨询后，我们的团队会为您报价。'),
'fq3':('Is my booking confirmed after I submit the form?','提交表单后预订就确认了吗？'),'fa3':('No. The form only prepares your WhatsApp message. A booking is confirmed once our team agrees the details with you on WhatsApp.','没有。表单只是生成您的 WhatsApp 消息。需我们团队与您在 WhatsApp 确认细节后，预订才算确认。'),
'fq4':('Which languages are available?','支持哪些语言？'),'fa4':('This website is available in English and 中文. Tell us your preferred language when you message us.','本网站支持 English 与中文。联系我们时请告知您偏好的语言。'),
'f.pickup':('Pickup location','接送地点'),'f.dropoff':('Drop-off','目的地'),'f.dest':('Destination','目的地'),'f.date':('Date','日期'),'f.time':('Time','时间'),'f.pax':('Passengers','人数'),'f.luggage':('Luggage','行李'),'f.flight':('Flight number','航班号'),'f.notes':('Additional request','其他要求'),'f.vehicle':('Vehicle preference','车辆偏好'),'f.rdate':('Rental date','租车日期'),'f.retdate':('Return date','还车日期'),'f.mode':('Rental type','租赁方式'),'f.size':('Preferred vehicle size','偏好车型大小'),'f.topic':('Tour type','行程类型'),'f.type':('Enquiry type','咨询类型'),
'opt':('(optional)','（选填）'),'sel':('Select…','请选择…'),
'o.any':('No preference','无偏好'),'o.mpv6':('6-Seater MPV','6 座 MPV'),'o.mpv7':('7-Seater MPV','7 座 MPV'),'o.mpv8':('8-Seater MPV','8 座 MPV'),'o.mpvp':('Premium MPV','高级 MPV'),'o.self':('Self Drive','自驾'),'o.driver':('With Driver','配司机'),'o.custom':('Custom Private Tour','定制私人行程'),'o.flight':('Flight Booking','机票预订'),'o.hotel':('Hotel Booking','酒店预订'),'o.package':('Travel Packages','旅游套餐'),
'note':('No account needed. This opens WhatsApp with your details filled in. Prices and availability are confirmed by our team.','无需注册。点击后将打开 WhatsApp 并自动填好您的信息。价格与可用情况由我们团队确认。'),
'ok':('Your message is ready. If WhatsApp did not open, tap the button below.','您的消息已生成。若 WhatsApp 未自动打开，请点击下方按钮。'),'err.req':('Please fill in this field.','请填写此项。'),'err.num':('Please enter a valid number.','请输入有效数字。'),
'msg.hi':('Hi MY JOURNEY SERVICES,','您好，MY JOURNEY SERVICES，'),'msg.general':('I would like to make an enquiry.','我想进行咨询。'),'msg.airport':('I would like to enquire about Airport Transfer.','我想咨询机场接送服务。'),'msg.transport':('I would like to enquire about Private Transport.','我想咨询专车服务。'),'msg.tours':('I would like to enquire about a Private Tour.','我想咨询私人行程服务。'),'msg.travel':('I would like to enquire about Travel Booking.','我想咨询旅行预订。'),'msg.flight':('I would like to enquire about Flight Booking.','我想咨询机票预订。'),'msg.hotel':('I would like to enquire about Hotel Booking.','我想咨询酒店预订。'),'msg.package':('I would like to enquire about Travel Packages.','我想咨询旅游套餐。'),'msg.mpv':('I would like to check MPV rental availability.','我想查询 MPV 租赁的可用情况。'),'msg.dest':('I would like to ask about availability for a destination.','我想咨询某个目的地的服务可用情况。'),
'none':('None','无'),'colon':(':','：'),'u.pax':('','人'),'u.luggage':('','件'),
'mp.self':('Self Drive','自驾'),'mp.selfd':('You rent the MPV and drive it yourself.','您租用 MPV 并自己驾驶。'),'mp.drv':('With Driver','配司机'),'mp.drvd':('You hire the MPV together with a driver.','您连同司机一起租用 MPV。'),'mp.cats':('Vehicle sizes you can ask about','可咨询的车型大小'),'mp.note':('We do not claim specific vehicles are available until confirmed.','具体车辆是否可用，以我们确认为准。'),
'tr.flight':('Flight Booking','机票预订'),'tr.flightd':('Ask about flight arrangements.','咨询机票安排。'),'tr.hotel':('Hotel Booking','酒店预订'),'tr.hoteld':('Request hotel recommendations or booking assistance.','获取酒店推荐或预订协助。'),'tr.package':('Travel Packages','旅游套餐'),'tr.packaged':('Custom travel arrangements built around your plans.','根据您的计划定制旅行安排。'),
'd.kl':('Kuala Lumpur','吉隆坡'),'d.klia':('KLIA','KLIA 吉隆坡国际机场'),'d.genting':('Genting Highlands','云顶高原'),'d.malacca':('Malacca','马六甲'),'d.cameron':('Cameron Highlands','金马伦高原'),'d.putrajaya':('Putrajaya','布城'),'d.johor':('Johor','柔佛'),'d.other':('Other Malaysia destinations','马来西亚其他地点'),
'dest.note':('Availability varies by destination. Request availability and we will confirm.','各目的地的服务情况不同。请咨询，我们会为您确认。'),
'ab.p1':('MY JOURNEY SERVICES is a travel and transport service that helps customers arrange transportation, tours and travel services.','MY JOURNEY SERVICES 是一家旅游与交通服务公司，协助客户安排交通、行程及旅行服务。'),
'ab.p2':('Tell us what you need, chat with us on WhatsApp, and we will follow up with a quote.','告诉我们您的需求，在 WhatsApp 上沟通，我们会跟进并提供报价。'),
'ab.h':('How we work','我们的方式'),'ab.w1':('Clear communication on WhatsApp','通过 WhatsApp 清晰沟通'),'ab.w2':('Quotes confirmed by our team, not an automated system','报价由团队确认，而非自动系统'),'ab.w3':('Honest about availability — we confirm before you commit','如实告知可用情况——确认后您再决定'),
'ct.p':('The fastest way to reach us is WhatsApp. Tell us the service, date and number of passengers and we will reply with a quote.','联系我们最快的方式是 WhatsApp。告诉我们服务类型、日期和人数，我们会回复报价。'),'ct.email':('Email','电子邮件'),
'end':('Ready to plan your journey?','准备好开始您的行程了吗？'),
'ft.pop':('Popular pages','热门页面'),'terms':('Basic information: quotes and availability are confirmed by our team on WhatsApp. Submitting an enquiry is not a booking. Details you submit are used to respond to your enquiry.','基本说明：报价与可用情况由我们团队通过 WhatsApp 确认。提交咨询不等于预订。您提交的信息仅用于回复您的咨询。'),
}
SEO={ # slug:(service,h1 en,h1 zh,lead en,lead zh)
'klia-airport-transfer':('airport','KLIA Airport Transfer','KLIA 机场接送','Arranging a pickup or drop-off at KLIA Terminal 1 or Terminal 2? Send your flight and passenger details and we will confirm price and availability on WhatsApp.','需要在 KLIA 第一或第二航站楼接机或送机？提交航班和人数信息，我们将通过 WhatsApp 确认价格与可用情况。'),
'kuala-lumpur-airport-transfer':('airport','Kuala Lumpur Airport Transfer','吉隆坡机场接送','Need transport between the airport and Kuala Lumpur or your hotel? Share your details and we will reply with a quote on WhatsApp.','需要往返机场与吉隆坡或酒店？提交信息后，我们将通过 WhatsApp 回复报价。'),
'private-transport-malaysia':('private','Private Transport Malaysia','马来西亚专车服务','Point-to-point, hourly or full-day private transport in Malaysia. Tell us your route and we will check availability and quote on WhatsApp.','马来西亚点对点、按小时或全天专车服务。告诉我们路线，我们将确认可用情况并通过 WhatsApp 报价。'),
'kuala-lumpur-private-transport':('private','Kuala Lumpur Private Transport','吉隆坡专车服务','Need a private ride around Kuala Lumpur for a business day, family outing or event? Request a quote on WhatsApp.','需要在吉隆坡市区用车，如商务、家庭出游或活动？欢迎通过 WhatsApp 申请报价。'),
'private-driver-kuala-lumpur':('private','Private Driver Kuala Lumpur','吉隆坡私人司机','Need a private driver in Kuala Lumpur for a few hours or the full day? Send us your plans and we will quote on WhatsApp.','需要吉隆坡私人司机，几小时或全天均可？告诉我们您的安排，我们将通过 WhatsApp 报价。'),
'mpv-rental-malaysia':('mpv','MPV Rental Malaysia','马来西亚 MPV 租赁','MPV rental for families and groups, Self Drive or With Driver. We rent MPVs only. Check availability on WhatsApp.','适合家庭及团体的 MPV 租赁，可选自驾或配司机。我们仅提供 MPV。请通过 WhatsApp 查询可用情况。'),
'mpv-rental-kuala-lumpur':('mpv','MPV Rental Kuala Lumpur','吉隆坡 MPV 租赁','Looking to rent an MPV in Kuala Lumpur? Choose Self Drive or With Driver and we will confirm availability on WhatsApp.','想在吉隆坡租 MPV？选择自驾或配司机，我们将通过 WhatsApp 确认可用情况。'),
'private-tour-kuala-lumpur':('tours','Private Tour Kuala Lumpur','吉隆坡私人行程','Tell us what you want to see and we will help plan a private tour in and around Kuala Lumpur. No fixed packages, so every trip is customised.','告诉我们您想游览的地方，我们协助规划吉隆坡及周边的私人行程。没有固定套餐，每趟行程均为定制。'),
'malaysia-travel-services':('travel','Malaysia Travel Services','马来西亚旅游服务','Airport transfers, private transport, tours, MPV rental and travel booking help for Malaysia. Tell us what you need and we will guide you on WhatsApp.','马来西亚的机场接送、专车、行程、MPV 租赁及旅行预订协助。告诉我们您的需求，我们将通过 WhatsApp 为您指引。'),
}
for s,(sv,a,b,c,d) in SEO.items():T['h1.'+s]=(a,b);T['p.'+s]=(c,d)
MAIN=[('index.html','nav.home'),('airport-transfer.html','nav.airport'),('private-transport.html','nav.private'),('tours.html','nav.tours'),('travel-booking.html','nav.travel'),('mpv-rental.html','nav.mpv'),('destinations.html','nav.dest'),('about.html','nav.about'),('contact.html','nav.contact')]
V=['o.any','o.mpv6','o.mpv7','o.mpv8','o.mpvp']
FM={'airport':[('pickup','text',1),('dropoff','text',1),('date','date',1),('time','time',1),('pax','number',1),('luggage','number',1),('flight','text',0),('notes','textarea',0)],
'transport':[('date','date',1),('pickup','text',1),('dest','text',1),('time','time',1),('pax','number',1),('vehicle','text',0),('notes','textarea',0)],
'mpv':[('rdate','date',1),('retdate','date',1),('pax','number',1),('pickup','text',1),('mode','select',1,['o.self','o.driver']),('size','select',0,V),('notes','textarea',0)],
'tours':[('topic','select',1,['d.kl','d.genting','d.malacca','d.cameron','o.custom']),('date','date',0),('pax','number',1),('notes','textarea',0)],
'travel':[('type','select',1,['o.flight','o.hotel','o.package']),('dest','text',1),('date','date',0),('pax','number',1),('notes','textarea',0)]}
SV={'airport':('airport-transfer.html','svc.airport','p.airport','cta.quote'),'private':('private-transport.html','svc.private','p.private','cta.reqq'),'tours':('tours.html','svc.tours','p.tours','cta.tour'),'travel':('travel-booking.html','svc.travel','p.travel','cta.enq'),'mpv':('mpv-rental.html','svc.mpv','p.mpv','cta.avail')}
FORM={'airport':'airport','private':'transport','tours':'tours','travel':'travel','mpv':'mpv'}
def i(k,tag='span',c='',x=''):return f'<{tag}{f" class={chr(34)}{c}{chr(34)}" if c else ""} data-i18n="{k}"{x}>{T[k][0]}</{tag}>'
def wa(key,label,c='btn',x=''):return f'<a class="{c}" href="#" target="_blank" rel="noopener" data-wa="{key}"{x} data-i18n="{label}">{T[label][0]}</a>'
def form(s):
  h=f'<form class="card form" data-service="{s}" novalidate>'
  for n,ty,rq,*o in FM[s]:
    lab=i('f.'+n)+('' if rq else ' '+i('opt','em'))
    r=' required' if rq else ''
    if ty=='select':c=f'<select name="{n}"{r}><option value="" data-i18n="sel">{T["sel"][0]}</option>'+''.join(f'<option value="{k}" data-i18n="{k}">{T[k][0]}</option>' for k in o[0])+'</select>'
    elif ty=='textarea':c=f'<textarea name="{n}" rows="3"></textarea>'
    else:c=f'<input name="{n}" type="{ty}"{r}'+(f' min="{0 if n=="luggage" else 1}" inputmode="numeric"' if ty=='number' else '')+'>'
    h+=f'<div class="field"><label>{lab}</label>{c}<small class="err"></small></div>'
  return h+f'<button class="btn" type="submit" data-i18n="cta.continue">{T["cta.continue"][0]}</button><p class="muted">{i("note")}</p><div class="ok" hidden><p>{i("ok")}</p><a class="btn" href="#" target="_blank" rel="noopener" data-i18n="cta.continue">{T["cta.continue"][0]}</a></div></form>'
def steps():
  return '<div class="grid g4">'+''.join(f'<div class="card"><h3>{i(f"st{n}")}</h3><p class="muted">{i(f"st{n}d")}</p></div>' for n in range(1,5))+'</div>'
def faq():
  return ''.join(f'<details class="card"><summary>{i(f"fq{n}")}</summary><p class="muted">{i(f"fa{n}")}</p></details>' for n in range(1,5))
def sec(h,b,c=''):return f'<section class="sec {c}"><div class="w"><h2>{i(h)}</h2>{b}</div></section>'
def related(cur):
  return sec('h.more','<div class="chips">'+''.join(f'<a class="chip" href="{f}" data-i18n="{t}">{T[t][0]}</a>' for f,t in MAIN[1:6] if f!=cur)+'</div>')
def ph(n,c=''):return f'<figure class="ph {c}"><svg viewBox="0 0 120 60" aria-hidden="true"><path d="M10 44V30l12-14h50l22 14 14 4v10z" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linejoin="round"/><circle cx="34" cy="46" r="7" fill="#fff7ed" stroke="currentColor" stroke-width="2.5"/><circle cx="92" cy="46" r="7" fill="#fff7ed" stroke="currentColor" stroke-width="2.5"/></svg><img src="assets/images/{n}.jpg" alt="MPV" loading="lazy" onerror="this.remove()"></figure>'
def hero(h1,lead,cta,key,home=False):
  return f'<section class="hero"><div class="w hg"><div>{i("tag","p","kick") if home else ""}<h1 data-i18n="{h1}">{T[h1][0]}</h1>{i(lead,"p","lead")}<div class="row">{wa(key,cta)}{f"<a class={chr(34)}btn ghost{chr(34)} href={chr(34)}#services{chr(34)} data-i18n={chr(34)}cta.explore{chr(34)}>{T[chr(99)+chr(116)+chr(97)+chr(46)+chr(101)+chr(120)+chr(112)+chr(108)+chr(111)+chr(114)+chr(101)][0]}</a>" if home else ""}</div></div>{ph("mpv-hero","big")}</div></section>'
def page(fn,tk,desc,body,title=None):
  nav=''.join(f'<a href="{f}"{" class=on" if f==fn else ""} data-i18n="{t}">{T[t][0]}</a>' for f,t in MAIN)
  pop=''.join(f'<a href="{s}.html" data-i18n="h1.{s}">{T["h1."+s][0]}</a>' for s in SEO)
  ld=json.dumps({"@context":"https://schema.org","@type":"TravelAgency","name":"MY JOURNEY SERVICES","slogan":T['slogan'][0],"url":SITE})
  html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{T[tk][0]} | MY JOURNEY SERVICES</title><meta name="description" content="{desc}"><link rel="canonical" href="{SITE}{fn}"><meta name="theme-color" content="#fffaf5"><link rel="stylesheet" href="assets/css/style.css"><script type="application/ld+json">{ld}</script></head><body data-title="{tk}"><header><div class="w bar"><a class="logo" href="index.html">MY <b>JOURNEY</b> SERVICES</a><nav id="nav">{nav}</nav><div class="tools"><button id="lang" type="button" aria-label="Language">中文</button><button class="burger" id="burger" type="button" aria-label="Menu">☰</button></div></div></header><main>{body}</main><footer><div class="w"><p class="logo">MY <b>JOURNEY</b> SERVICES</p><p class="muted">{i("tag")}<br>{i("slogan")}</p><div class="row">{wa("general","cta.wa")}<a class="btn ghost" data-email href="#" hidden>{i("ct.email")}</a></div><h4>{i("ft.pop")}</h4><div class="chips">{pop}</div><p class="muted small">{i("terms")}</p><p class="muted small">© MY JOURNEY SERVICES</p></div></footer>{wa("general","cta.wa","fab")}<script src="assets/js/config.js"></script><script src="assets/js/translations.js"></script><script src="assets/js/app.js"></script></body></html>'''
  open(f'{O}/{fn}','w',encoding='utf-8').write(html)
def cards(keys):return '<div class="grid">'+''.join(f'<div class="card">{i(k,"p")}</div>' for k in keys)+'</div>'
AI=[f'ai{n}' for n in range(1,10)];PT=[f'pt{n}' for n in range(1,7)]
def extra(s):
  if s=='airport':return sec('h.offer',cards(AI))
  if s=='private':return sec('h.offer',cards(PT))
  if s=='tours':return sec('h.offer',cards(['d.kl','d.genting','d.malacca','d.cameron','o.custom']))
  if s=='travel':return sec('h.offer','<div class="grid">'+''.join(f'<div class="card"><h3>{i("tr."+k)}</h3><p class="muted">{i("tr."+k+"d")}</p>{wa(k,"cta.enq","btn")}</div>' for k in ('flight','hotel','package'))+'</div>')
  return sec('h.offer',f'<div class="grid"><div class="card"><h3>{i("mp.self")}</h3><p class="muted">{i("mp.selfd")}</p></div><div class="card"><h3>{i("mp.drv")}</h3><p class="muted">{i("mp.drvd")}</p></div></div><div class="grid g3 gal">{ph("mpv-1")}{ph("mpv-2")}{ph("mpv-3")}</div><h3 class="sub">{i("mp.cats")}</h3><div class="chips">'+''.join(f'<span class="chip">{i(k)}</span>' for k in V[1:])+f'</div><p class="muted">{i("mp.note")}</p>')
for s,(fn,t,p,c) in SV.items():
  page(fn,t+'.t',T[p][0],hero(t+'.t',p,c,FORM[s] if s!='mpv' else 'mpv')+extra(s)+sec('h.req',form(FORM[s]),'alt')+sec('h.how',steps())+related(fn))
for s,(sv,a,b,c,d) in SEO.items():
  fn,t,p,cta=SV[sv];
  page(s+'.html','h1.'+s,c,hero('h1.'+s,'p.'+s,cta,FORM[sv])+extra(sv)+sec('h.req',form(FORM[sv]),'alt')+sec('h.how',steps())+related(fn))
home=hero('slogan','hero.p','cta.wa','general',True).replace('<h1 data-i18n="slogan">','<h1 data-i18n="slogan">')
home=home.replace('<h1','<p class="brandline">MY JOURNEY SERVICES</p><h1',1)
sv_cards='<div class="grid g3" id="services">'+''.join(f'<div class="card"><h3>{i(t+".t")}</h3><p class="muted">{i(t+".d")}</p><a class="btn" href="{fn}" data-i18n="{t}.b">{T[t+".b"][0]}</a></div>' for s,(fn,t,p,c) in SV.items())+'</div>'
page('index.html','slogan',T['hero.p'][0],home+sec('h.svc',sv_cards)+sec('h.how',steps(),'alt')+sec('h.faq',faq())+f'<section class="sec"><div class="w center"><h2>{i("end")}</h2>{wa("general","cta.book")}</div></section>')
page('destinations.html','nav.dest',T['dest.note'][0],f'<section class="hero"><div class="w"><h1 data-i18n="nav.dest">{T["nav.dest"][0]}</h1>{i("dest.note","p","lead")}</div></section>'+sec('h.svc','<div class="grid">'+''.join(f'<div class="card"><h3>{i(k)}</h3>{wa("dest","cta.reqav","btn",f" data-dkey={chr(34)}{k}{chr(34)}")}</div>' for k in ('d.kl','d.klia','d.genting','d.malacca','d.cameron','d.putrajaya','d.johor','d.other'))+'</div>'))
page('about.html','nav.about',T['ab.p1'][0],f'<section class="hero"><div class="w"><h1 data-i18n="nav.about">{T["nav.about"][0]}</h1>{i("ab.p1","p","lead")}{i("ab.p2","p","lead")}</div></section>'+sec('h.offer','<div class="chips">'+''.join(f'<a class="chip" href="{fn}" data-i18n="{t}.t">{T[t+".t"][0]}</a>' for s,(fn,t,p,c) in SV.items())+'</div>')+sec('ab.h',cards(['ab.w1','ab.w2','ab.w3']),'alt')+f'<section class="sec"><div class="w">{wa("general","cta.wa")}</div></section>')
page('contact.html','nav.contact',T['ct.p'][0],f'<section class="hero"><div class="w"><h1 data-i18n="nav.contact">{T["nav.contact"][0]}</h1>{i("ct.p","p","lead")}<div class="row">{wa("general","cta.wa")}<a class="btn ghost" data-email href="#" hidden>{i("ct.email")}</a></div></div></section>'+sec('h.faq',faq())+sec('h.how',steps(),'alt'))
# data files
tr={'en':{k:v[0] for k,v in T.items()},'zh':{k:v[1] for k,v in T.items()}}
open(f'{O}/assets/js/translations.js','w',encoding='utf-8').write('/* Edit translations here (and in build.py if you regenerate). */\nwindow.MJS_TRANSLATIONS = '+json.dumps(tr,ensure_ascii=False,indent=1)+';')
open(f'{O}/assets/js/config.js','w').write('''/* Site configuration. Change values here only. */
window.MJS_CONFIG = {
  WHATSAPP_NUMBER: "60108877703", // country code first, digits only
  EMAIL: "",                      // TODO: optional; email buttons stay hidden while empty
  LEAD_ENDPOINT: null             // FUTURE: URL of a lead database / automation webhook. Not connected yet.
};''')
open(f'{O}/assets/js/app.js','w',encoding='utf-8').write(r'''(function(){
var C=window.MJS_CONFIG,TR=window.MJS_TRANSLATIONS,S=window.localStorage,Q=new URLSearchParams(location.search);
var lang=Q.get('lang')||(function(){try{return S.getItem('mjs_lang')}catch(e){}})()||'en';if(!TR[lang])lang='en';
function t(k){return (TR[lang]&&TR[lang][k])!==undefined?TR[lang][k]:(TR.en[k]!==undefined?TR.en[k]:k)}
function url(m){return 'https://wa.me/'+C.WHATSAPP_NUMBER+'?text='+encodeURIComponent(m)}
function hi(k){return t('msg.hi')+'\n\n'+t('msg.'+k)}
function apply(){
  document.documentElement.lang=lang==='zh'?'zh-Hans':'en';
  document.querySelectorAll('[data-i18n]').forEach(function(e){e.textContent=t(e.dataset.i18n)});
  document.querySelectorAll('[data-wa]').forEach(function(a){
    var m=hi(a.dataset.wa);if(a.dataset.dkey)m+='\n\n'+t('f.dest')+t('colon')+'\n'+t(a.dataset.dkey);a.href=url(m)});
  document.querySelectorAll('[data-email]').forEach(function(a){if(C.EMAIL){a.href='mailto:'+C.EMAIL;a.hidden=false}});
  document.querySelectorAll('.err').forEach(function(e){e.textContent=''});
  document.title=t(document.body.dataset.title)+' | MY JOURNEY SERVICES';
  document.getElementById('lang').textContent=lang==='zh'?'English':'中文';
}
function setLang(l){lang=l;try{S.setItem('mjs_lang',l)}catch(e){}apply()}
document.getElementById('lang').onclick=function(){setLang(lang==='zh'?'en':'zh')};
document.getElementById('burger').onclick=function(){document.getElementById('nav').classList.toggle('open')};
var today=new Date().toISOString().slice(0,10);
document.querySelectorAll('input[type=date]').forEach(function(d){d.min=today});
document.querySelectorAll('form[data-service]').forEach(function(f){
  f.addEventListener('submit',function(e){
    e.preventDefault();var ok=true,rows=[],d={};
    f.querySelectorAll('.field').forEach(function(w){
      var i=w.querySelector('[name]'),v=i.value.trim(),er=w.querySelector('.err');er.textContent='';
      if(i.required&&!v){er.textContent=t('err.req');ok=false;return}
      if(i.type==='number'&&v&&(isNaN(v)||+v<+i.min)){er.textContent=t('err.num');ok=false;return}
      d[i.name]=v;
      if(!v&&i.name!=='notes')return;
      var shown=!v?t('none'):i.tagName==='SELECT'?t(v):v+(TR[lang]['u.'+i.name]||'');
      rows.push(t('f.'+i.name)+t('colon')+'\n'+shown);
    });
    if(!ok)return;
    var svc=f.dataset.service,msg=hi(svc)+'\n\n'+rows.join('\n\n'),u=url(msg);
    var lead={name:'',whatsapp:'',email:'',service:svc,date:d.date||d.rdate||'',time:d.time||'',pickup:d.pickup||'',
      destination:d.dropoff||d.dest||d.topic||'',passengers:d.pax||'',vehicle:d.vehicle||d.size||d.mode||'',message:msg,
      language:lang,source:Q.get('utm_source')||Q.get('ref')||document.referrer||'direct',created:new Date().toISOString(),status:'NEW'};
    try{var L=JSON.parse(S.getItem('mjs_leads')||'[]');L.push(lead);S.setItem('mjs_leads',JSON.stringify(L))}catch(x){}
    if(C.LEAD_ENDPOINT){try{fetch(C.LEAD_ENDPOINT,{method:'POST',mode:'no-cors',body:JSON.stringify(lead)})}catch(x){}}
    var ok2=f.querySelector('.ok');ok2.hidden=false;ok2.querySelector('a').href=u;window.open(u,'_blank','noopener');
  });
});
apply();
})();''')
open(f'{O}/assets/css/style.css','w').write('''/* Photos: put MPV images in assets/images/ named mpv-hero.jpg, mpv-1.jpg, mpv-2.jpg, mpv-3.jpg (they appear automatically). */
:root{--bg:#fffaf5;--card:#fff;--alt:#fff1e6;--line:#ecdccf;--g:#ea580c;--btn:#c2410c;--tx:#1c1917;--mu:#6b625c}
*{box-sizing:border-box;margin:0}html{scroll-behavior:smooth}
body{font:16px/1.65 system-ui,-apple-system,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--tx);-webkit-text-size-adjust:100%}
a{color:inherit}.w{max-width:1120px;margin:auto;padding:0 20px}.muted{color:var(--mu)}.small{font-size:13px;margin-top:14px}.center{text-align:center}
header{position:sticky;top:0;z-index:20;background:rgba(255,250,245,.95);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.bar{display:flex;align-items:center;justify-content:space-between;height:64px}
.logo{font-weight:800;letter-spacing:.04em;text-decoration:none;font-size:15px}.logo b{color:var(--g)}
nav{display:none;position:absolute;top:64px;left:0;right:0;background:var(--bg);padding:8px 20px 16px;border-bottom:1px solid var(--line);flex-direction:column}nav.open{display:flex}
nav a{padding:12px 0;text-decoration:none;font-size:14px;font-weight:600;color:var(--mu)}nav a.on,nav a:hover{color:var(--g)}
.tools{display:flex;gap:8px}.tools button{background:#fff;border:1px solid var(--line);color:var(--tx);border-radius:999px;padding:8px 14px;font:inherit;font-size:14px;cursor:pointer}
@media(min-width:1120px){nav{display:flex;position:static;flex-direction:row;gap:16px;padding:0;border:0;background:none}nav a{padding:0;font-size:12px}.burger{display:none}}
.hero{padding:40px 0 56px;background:linear-gradient(180deg,var(--alt),var(--bg))}.hg{display:grid;gap:32px;align-items:center}
@media(min-width:900px){.hg{grid-template-columns:1.1fr .9fr}.hero{padding:72px 0}}
.brandline{color:var(--g);font-weight:700;letter-spacing:.05em;margin-bottom:10px}.kick{color:var(--mu);margin-bottom:8px;font-weight:600}
h1{font-size:clamp(32px,6vw,56px);line-height:1.1;letter-spacing:-.025em;font-weight:800}
h2{font-size:clamp(24px,4vw,34px);letter-spacing:-.015em;margin-bottom:24px}h3{font-size:18px;margin-bottom:6px}.sub{margin:24px 0 10px}h4{margin:28px 0 10px}
.lead{color:var(--mu);font-size:18px;max-width:36em;margin-top:16px}.row{display:flex;flex-wrap:wrap;gap:12px;margin-top:28px}
.btn{display:inline-block;background:var(--btn);color:#fff;font-weight:700;border:0;border-radius:12px;padding:14px 22px;font-size:16px;text-decoration:none;cursor:pointer;font-family:inherit;min-height:48px}
.btn:hover{background:#9a3412}.btn.ghost{background:#fff;color:var(--tx);border:1px solid var(--line)}
.ph{position:relative;aspect-ratio:4/3;border-radius:22px;overflow:hidden;background:#ffe8d4;color:#ea580c;display:grid;place-items:center;border:1px solid var(--line)}
.ph svg{width:46%;opacity:.6}.ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.gal{margin-top:20px}
.sec{padding:60px 0}.sec.alt{background:var(--alt);border-block:1px solid var(--line)}
.grid{display:grid;gap:16px}.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:22px;border-top:3px solid var(--g)}.card .btn{margin-top:16px}
@media(min-width:700px){.grid{grid-template-columns:repeat(2,1fr)}.g4{grid-template-columns:repeat(2,1fr)}}
@media(min-width:960px){.grid{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}}
.chips{display:flex;flex-wrap:wrap;gap:10px}.chip{background:#fff;border:1px solid var(--line);border-radius:999px;padding:8px 16px;font-size:14px;text-decoration:none;color:var(--mu)}a.chip:hover{border-color:var(--g);color:var(--g)}
.form{max-width:640px;display:grid;gap:16px;border-top-color:var(--g)}.field label{display:block;font-size:14px;font-weight:600;margin-bottom:6px}.field em{color:var(--mu);font-style:normal;font-weight:400}
input,select,textarea{width:100%;background:#fff;color:var(--tx);border:1px solid #d9c7b8;border-radius:12px;padding:13px 14px;font:inherit;font-size:16px}
input:focus,select:focus,textarea:focus,a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid var(--g);outline-offset:2px}
.err{color:#b91c1c;font-size:13px;display:block}.ok{border:1px solid var(--g);background:var(--alt);border-radius:14px;padding:16px}.ok[hidden]{display:none}
details.card{margin-bottom:12px}summary{cursor:pointer;font-weight:600}details p{margin-top:10px}
footer{background:#1c1917;color:#f5f5f4;padding:48px 0 110px}footer .muted{color:#a8a29e}footer .chip{background:none;border-color:#44403c;color:#d6d3d1}footer .btn.ghost{background:none;color:#f5f5f4;border-color:#57534e}
.fab{position:fixed;right:16px;bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:30;background:var(--btn);color:#fff;font-weight:800;text-decoration:none;border-radius:999px;padding:15px 22px;box-shadow:0 6px 20px rgba(0,0,0,.25)}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}''')
urls=[f for f,_ in MAIN]+[s+'.html' for s in SEO]+[SV[k][0] for k in ()]
open(f'{O}/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{SITE}{u}</loc></url>' for u in urls)+'</urlset>')
open(f'{O}/robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
