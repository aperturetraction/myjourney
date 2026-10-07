(function(){
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
})();