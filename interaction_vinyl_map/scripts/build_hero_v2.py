"""Build hero-real-data.html v2 — genre colors + proportional map."""
import json

with open('api/hero_data_v2.json', 'r', encoding='utf-8') as f:
    data_json = f.read().strip()

html = r'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Urban Music Pulse</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,700&family=Syne:wght@400;600;700;800&display=swap');
*{margin:0;padding:0;box-sizing:border-box}html,body{width:100%;height:100%;overflow:hidden}
body{background:#08080d;color:#e8e4dc;font-family:'DM Sans',sans-serif}
canvas#discC{position:fixed;inset:0;z-index:0}
canvas#mapC{position:fixed;inset:0;z-index:1}
canvas#dotC{position:fixed;inset:0;z-index:2}
.topbar{position:fixed;top:0;left:0;right:0;display:flex;justify-content:space-between;align-items:center;padding:18px 24px;z-index:50;pointer-events:none}.topbar>*{pointer-events:auto}
.logo{font-family:'Syne',sans-serif;font-weight:800;font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:rgba(232,228,220,.25)}
.bt{display:flex;align-items:center;gap:9px;cursor:pointer;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:100px;padding:7px 16px;font-size:11px;font-weight:500;color:rgba(232,228,220,.45);letter-spacing:.07em;text-transform:uppercase;transition:all .3s;font-family:'DM Sans',sans-serif}
.bt:hover{background:rgba(255,255,255,.08);color:rgba(232,228,220,.8)}.bt.on{border-color:rgba(175,169,236,.45);color:#c8c4f8}
.bd{width:6px;height:6px;border-radius:50%;background:rgba(232,228,220,.25);transition:all .3s}.bt.on .bd{background:#c8c4f8;box-shadow:0 0 10px rgba(175,169,236,.6)}
.home{position:fixed;top:56px;left:24px;z-index:5;text-align:left;pointer-events:none;transition:opacity .5s;max-width:260px}.home.hid{opacity:0}
.ht{font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(18px,1.8vw,26px);line-height:1.1;letter-spacing:-.02em;color:#e8e4dc;margin-bottom:6px}
.ht em{font-style:italic;background:linear-gradient(135deg,#e24b4a,#ed93b1,#ef9f27,#85b7eb,#afa9ec);background-size:300% 300%;animation:gS 8s ease-in-out infinite;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
@keyframes gS{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
.hs{font-size:10px;color:rgba(232,228,220,.35);line-height:1.55;max-width:240px}
.cm{position:fixed;transform:translate(-50%,-50%);cursor:pointer;z-index:6;pointer-events:auto;transition:transform .3s cubic-bezier(.16,1,.3,1),opacity .4s}
.cm:hover{transform:translate(-50%,-50%) scale(1.12);z-index:10}.cm:hover .cg{opacity:.5}.cm:hover .cn{color:#e8e4dc}
.cg{position:absolute;top:50%;left:50%;width:100px;height:100px;transform:translate(-50%,-50%);border-radius:50%;opacity:.18;transition:opacity .4s;pointer-events:none;filter:blur(20px)}
.cd{position:relative;width:48px;height:48px;border-radius:50%;display:flex;align-items:center;justify-content:center;border:2px solid;box-shadow:0 0 16px rgba(0,0,0,.5)}
.cgs{position:absolute;inset:0;border-radius:50%;overflow:hidden}.cgr{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);border-radius:50%;border:1px solid rgba(255,255,255,.06)}
.cc{width:11px;height:11px;border-radius:50%;background:rgba(8,8,13,.8);border:1px solid rgba(255,255,255,.08);z-index:2}
.ccd{width:4px;height:4px;border-radius:50%;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)}
.cr{position:absolute;top:50%;left:50%;width:60px;height:60px;transform:translate(-50%,-50%);border-radius:50%;border:1px solid;opacity:.2;animation:rP 2.5s ease-in-out infinite}
@keyframes rP{0%,100%{transform:translate(-50%,-50%) scale(1);opacity:.18}50%{transform:translate(-50%,-50%) scale(1.35);opacity:.04}}
.cl{position:absolute;top:100%;left:50%;transform:translateX(-50%);padding-top:6px;text-align:center;white-space:nowrap}
.cn{font-family:'Syne',sans-serif;font-weight:700;font-size:10px;color:rgba(232,228,220,.55);transition:all .3s}.cme{font-size:8px;color:rgba(232,228,220,.2);margin-top:1px}
.qp{position:fixed;z-index:100;width:240px;padding:14px;background:rgba(14,14,22,.96);border:1px solid rgba(255,255,255,.08);border-radius:14px;backdrop-filter:blur(20px);opacity:0;pointer-events:none;transform:translateY(6px);transition:opacity .25s,transform .25s}.qp.show{opacity:1;pointer-events:auto;transform:translateY(0)}
.qpg{display:inline-block;padding:2px 10px;border-radius:100px;font-size:9px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;margin-bottom:6px}
.qpa{font-family:'Syne',sans-serif;font-weight:700;font-size:15px;line-height:1.2;margin-bottom:2px;color:#e8e4dc}.qpv{font-size:10px;color:rgba(232,228,220,.3);margin-bottom:8px}
.qpr{display:flex;justify-content:space-between;font-size:10px;padding:3px 0;color:rgba(232,228,220,.22)}.qpr span:last-child{color:rgba(232,228,220,.55);font-weight:500}
.qpb{display:block;text-align:center;margin-top:8px;padding:6px;border-radius:8px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.06);font-size:9px;font-weight:500;color:rgba(232,228,220,.4);letter-spacing:.06em;text-transform:uppercase;cursor:pointer;transition:all .3s;font-family:'DM Sans',sans-serif}.qpb:hover{background:rgba(255,255,255,.08);color:rgba(232,228,220,.8)}
.fn{position:fixed;z-index:100;font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(48px,10vw,90px);line-height:1;letter-spacing:-.03em;white-space:nowrap;pointer-events:none;opacity:0}.fn.go{transition:all .7s cubic-bezier(.16,1,.3,1)}
.lg{position:fixed;bottom:20px;left:20px;z-index:12;display:flex;flex-direction:column;gap:10px;padding:14px 16px;background:rgba(8,8,13,.7);border:1px solid rgba(255,255,255,.06);border-radius:12px;backdrop-filter:blur(16px);max-width:210px;transition:opacity .4s;pointer-events:auto}.lg.hid{opacity:0;pointer-events:none}
.lgt{font-family:'Syne',sans-serif;font-weight:700;font-size:8px;color:rgba(232,228,220,.22);letter-spacing:.12em;text-transform:uppercase}
.lgi{display:flex;flex-wrap:wrap;gap:4px 8px;margin-top:4px}.lgd{display:flex;align-items:center;gap:5px;font-size:9px;color:rgba(232,228,220,.4)}.lgc{width:7px;height:7px;border-radius:50%;flex-shrink:0}
.lgn{font-size:8px;color:rgba(232,228,220,.15);line-height:1.4;margin-top:2px}
.cp{position:fixed;inset:0;z-index:20;display:flex;flex-direction:column;background:rgba(8,8,13,.96);backdrop-filter:blur(50px);opacity:0;pointer-events:none;transition:opacity .4s;overflow-y:auto;overflow-x:hidden}.cp.open{opacity:1;pointer-events:auto}
.pb{display:flex;align-items:center;gap:8px;cursor:pointer;font-size:12px;color:rgba(232,228,220,.35);letter-spacing:.07em;text-transform:uppercase;background:none;border:none;font-family:'DM Sans',sans-serif;transition:color .3s;padding:22px 32px;z-index:5}.pb:hover{color:rgba(232,228,220,.8)}.pb svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2}
.ch{position:relative;padding:0 32px 32px;min-height:220px;display:flex;flex-direction:column;justify-content:flex-end;overflow:hidden}
.eqw{position:absolute;bottom:0;right:32px;display:flex;align-items:flex-end;gap:3px;height:140px;z-index:1;opacity:.28}.eqb{width:4px;border-radius:2px;transition:height .12s ease}
.chc{position:relative;z-index:2}
.chn{font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(48px,10vw,80px);line-height:1;letter-spacing:-.03em;margin-bottom:8px;opacity:0;transform:translateY(30px);transition:all .6s cubic-bezier(.16,1,.3,1)}.chn.in{opacity:1;transform:translateY(0)}
.chv{font-size:14px;color:rgba(232,228,220,.35);line-height:1.6;max-width:560px;opacity:0;transition:opacity .5s .3s}.chv.in{opacity:1}
.sr{display:flex;gap:0;border-top:1px solid rgba(255,255,255,.04);border-bottom:1px solid rgba(255,255,255,.04);overflow-x:auto;width:100%}
.ss{flex:1;min-width:90px;padding:20px 24px;border-right:1px solid rgba(255,255,255,.04)}.ss:last-child{border-right:none}
.sl{font-size:10px;color:rgba(232,228,220,.22);letter-spacing:.08em;text-transform:uppercase;margin-bottom:4px}.sv{font-family:'Syne',sans-serif;font-weight:700;font-size:22px;color:#e8e4dc}
.tc{display:flex;gap:40px;padding:32px 32px 0;width:100%}.tc>.col{flex:1;min-width:0}@media(max-width:700px){.tc{flex-direction:column;gap:24px}}
.st{font-family:'Syne',sans-serif;font-weight:700;font-size:13px;color:rgba(232,228,220,.3);letter-spacing:.1em;text-transform:uppercase;margin-bottom:18px}
.gb{display:flex;flex-direction:column;gap:8px}.gr{display:flex;align-items:center;gap:12px;opacity:0;transform:translateX(-30px);transition:opacity .6s,transform .6s cubic-bezier(.16,1,.3,1)}.gr.in{opacity:1;transform:translateX(0)}
.gn{width:74px;font-family:'Syne',sans-serif;font-size:13px;font-weight:600;text-align:right;flex-shrink:0}
.gtr{flex:1;height:34px;background:rgba(255,255,255,.025);border-radius:8px;overflow:hidden}
.gf{height:100%;border-radius:8px;display:flex;align-items:center;padding-left:12px;font-size:12px;font-weight:700;color:rgba(0,0,0,.5);transition:width 1.2s cubic-bezier(.16,1,.3,1);width:0}
.gp{font-size:12px;color:rgba(232,228,220,.25);width:38px;text-align:right;flex-shrink:0}
.vbs{display:flex;flex-wrap:wrap;align-items:flex-end;gap:14px;padding-top:8px}
.vb{display:flex;flex-direction:column;align-items:center;gap:6px;opacity:0;transform:scale(.4);transition:all .5s cubic-bezier(.16,1,.3,1);cursor:default}
.vb.in{opacity:1;transform:scale(1)}.vb:hover .vc{transform:scale(1.08);box-shadow:0 0 30px var(--gw)}
.vc{border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;transition:all .3s;position:relative;border:1.5px solid}
.vn{font-family:'Syne',sans-serif;font-weight:800;line-height:1}.ve{font-size:7px;letter-spacing:.06em;text-transform:uppercase;opacity:.45;margin-top:1px}
.vl{font-size:10px;color:rgba(232,228,220,.5);text-align:center;max-width:90px;line-height:1.2}.vr{font-family:'Syne',sans-serif;font-weight:800;font-size:9px;color:rgba(232,228,220,.15)}
.es{padding:32px 32px 40px;width:100%}.ew{display:flex;flex-wrap:wrap;gap:5px}
.ed{width:28px;height:28px;border-radius:50%;cursor:pointer;transition:all .25s cubic-bezier(.16,1,.3,1);opacity:.7;position:relative}
.ed:hover{transform:scale(1.6);opacity:1;z-index:5;box-shadow:0 0 22px var(--gw)}
.ed::after{content:attr(data-t);position:absolute;bottom:calc(100% + 6px);left:50%;transform:translateX(-50%);font-size:10px;white-space:nowrap;color:rgba(232,228,220,.7);background:rgba(11,11,16,.92);padding:3px 8px;border-radius:6px;opacity:0;pointer-events:none;transition:opacity .2s;border:1px solid rgba(255,255,255,.06)}.ed:hover::after{opacity:1}
.eo{position:fixed;inset:0;z-index:25;background:rgba(0,0,0,.5);opacity:0;pointer-events:none;transition:opacity .3s}.eo.open{opacity:1;pointer-events:auto}
.em{position:fixed;z-index:30;top:50%;left:50%;transform:translate(-50%,-50%) scale(.9);width:92%;max-width:420px;background:rgba(16,16,24,.97);border:1px solid rgba(255,255,255,.07);border-radius:20px;overflow:hidden;opacity:0;pointer-events:none;transition:all .4s cubic-bezier(.16,1,.3,1);backdrop-filter:blur(30px)}.em.open{opacity:1;pointer-events:auto;transform:translate(-50%,-50%) scale(1)}
.emh{padding:22px 22px 0;position:relative}.emx{position:absolute;top:14px;right:14px;width:30px;height:30px;border-radius:50%;background:rgba(255,255,255,.05);border:none;color:rgba(232,228,220,.4);font-size:16px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .3s;z-index:5}.emx:hover{background:rgba(255,255,255,.1);color:#e8e4dc}
.etg{display:inline-block;padding:3px 12px;border-radius:100px;font-size:10px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;margin-bottom:10px}
.ett{font-family:'Syne',sans-serif;font-weight:700;font-size:20px;line-height:1.2;margin-bottom:2px;color:#e8e4dc}.ets{font-size:12px;color:rgba(232,228,220,.38)}
.emb{padding:16px 22px 22px}.emd{display:flex;flex-direction:column;margin-bottom:16px}
.emr{display:flex;justify-content:space-between;font-size:12px;padding:8px 0;border-bottom:1px solid rgba(255,255,255,.03)}.emr:last-child{border:none}
.eml{color:rgba(232,228,220,.28)}.emv{color:rgba(232,228,220,.65);font-weight:500}
.emw{width:100%;height:48px;background:rgba(255,255,255,.02);border-radius:10px;overflow:hidden;position:relative;display:flex;align-items:center;justify-content:center;gap:1.5px;padding:0 12px}
.wb{width:3px;border-radius:2px}.ewl{position:absolute;font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:rgba(232,228,220,.2);bottom:4px;right:12px}
.cp::-webkit-scrollbar{width:4px}.cp::-webkit-scrollbar-thumb{background:rgba(255,255,255,.08);border-radius:2px}
</style></head><body>
<canvas id="discC"></canvas><canvas id="mapC"></canvas><canvas id="dotC"></canvas>
<div class="topbar"><div class="logo">Urban Music Pulse</div><button class="bt on" id="beatBtn"><span class="bd"></span><span id="bL">Beat on</span></button></div>
<div class="home" id="homeUI"><div class="ht">Drop the Needle,<br><em>Hear the City</em></div><div class="hs">56,000+ live events across 13 North American cities. Click any dot to preview a concert — tap a city to dive in.</div></div>
<div class="lg" id="legend"><div><div class="lgt">Color = Genre</div><div class="lgi">
<div class="lgd"><div class="lgc" style="background:#e24b4a"></div>Rock</div>
<div class="lgd"><div class="lgc" style="background:#ed93b1"></div>Pop</div>
<div class="lgd"><div class="lgc" style="background:#ef9f27"></div>Hip-Hop</div>
<div class="lgd"><div class="lgc" style="background:#85b7eb"></div>Jazz</div>
<div class="lgd"><div class="lgc" style="background:#afa9ec"></div>EDM</div>
<div class="lgd"><div class="lgc" style="background:#9fe1cb"></div>Classical</div>
<div class="lgd"><div class="lgc" style="background:#f5c4b3"></div>Country</div>
<div class="lgd"><div class="lgc" style="background:#fac775"></div>R&B</div>
</div></div><div class="lgn">Each dot = 1 event · Click to preview</div></div>
<div class="qp" id="qp"></div><div class="fn" id="fn"></div><div class="cp" id="cp"></div><div class="eo" id="eo"></div><div class="em" id="emM"></div>
<script>
const DATA = ''' + data_json + r''';

const GC={Rock:{f:'#e24b4a',g:'rgba(226,75,74,.4)',d:'#7a1f1f'},Pop:{f:'#ed93b1',g:'rgba(237,147,177,.4)',d:'#72243e'},'Hip-Hop':{f:'#ef9f27',g:'rgba(239,159,39,.4)',d:'#633806'},Jazz:{f:'#85b7eb',g:'rgba(133,183,235,.4)',d:'#0c447c'},Classical:{f:'#9fe1cb',g:'rgba(159,225,203,.4)',d:'#085041'},EDM:{f:'#afa9ec',g:'rgba(175,169,236,.4)',d:'#3c3489'},Country:{f:'#f5c4b3',g:'rgba(245,196,179,.4)',d:'#712b13'},'R&B':{f:'#fac775',g:'rgba(250,199,117,.4)',d:'#633806'}};
const gN=Object.keys(GC);

const CV={
  'Toronto':"Canada's largest music market — multicultural hub where hip-hop, R&B, and pop thrive alongside indie rock and electronic.",
  'Montreal':'Jazz capital meets francophone indie rock. Festival city with genre diversity unmatched in North America.',
  'Vancouver':'West Coast electronic and pop hub. Year-round outdoor shows and a surprisingly deep live calendar.',
  'Calgary':'Prairie powerhouse where country and rock share the stage with a growing indie and hip-hop scene.',
  'Ottawa':'The capital blends bilingual indie with classical and jazz, powered by national festivals and intimate clubs.',
  'New York':'The undisputed live music capital. Every genre, every night — arenas to basement jazz clubs.',
  'Los Angeles':'Pop and hip-hop powerhouse backed by legendary rock. Industry town meets thriving underground.',
  'Chicago':'Blues and jazz DNA meet ferocious hip-hop and house. Punches above its weight in diversity.',
  'Detroit':'Motown soul, techno birthplace, and garage rock grit — a city that never stopped making music.',
  'Las Vegas':'Beyond the Strip residencies: EDM temples, pop spectacles, and a surprisingly vibrant local rock scene.',
  'Miami':'Latin beats collide with electronic heat and R&B soul — the sound of the tropics after dark.',
  'San Francisco':'Psychedelic roots meet Silicon Valley creativity — rock, electronic, and jazz thrive in Bay Area clubs.',
  'Washington':'From the 9:30 Club to the Kennedy Center — punk, go-go, jazz, and classical coexist in the capital.'
};

const cityTopGenre=city=>Object.entries(DATA[city].gd).sort((a,b)=>b[1]-a[1])[0][0];
const cityColor=city=>GC[cityTopGenre(city)].f;
const cityGlow=city=>GC[cityTopGenre(city)].g;
const cityDark=city=>GC[cityTopGenre(city)].d;

const cityMarkerOffsets={
  'Vancouver':{x:-8,y:-18},'Calgary':{x:-6,y:-22},'Ottawa':{x:14,y:-26},
  'Toronto':{x:6,y:-6},'Montreal':{x:20,y:-20},
  'New York':{x:34,y:18},'Los Angeles':{x:-10,y:12},'Chicago':{x:0,y:-10},
  'Detroit':{x:10,y:-14},'Las Vegas':{x:-16,y:6},'Miami':{x:20,y:12},
  'San Francisco':{x:-18,y:2},'Washington':{x:28,y:4}
};

const ALL=[];let eid=0;
Object.keys(DATA).forEach(city=>{
  DATA[city].s.forEach(ev=>{
    ALL.push({id:eid++,city,artist:ev[0],venue:ev[1],date:ev[2],genre:ev[3]});
  });
});

// ── PROPORTIONAL PROJECTION ──
// Maintains aspect ratio, centers map in viewport
const MAP_LON_MIN=-130, MAP_LON_MAX=-68, MAP_LAT_MIN=24, MAP_LAT_MAX=55;
const MAP_W=MAP_LON_MAX-MAP_LON_MIN, MAP_H=MAP_LAT_MAX-MAP_LAT_MIN;
// Apply cos correction for mid-latitude
const MID_LAT_RAD=(MAP_LAT_MIN+MAP_LAT_MAX)/2*Math.PI/180;
const ASPECT=(MAP_W*Math.cos(MID_LAT_RAD))/MAP_H;

let mapScale,mapOX,mapOY;
function calcProj(){
  const pad=40;
  const aw=W-pad*2, ah=H-pad*2;
  const viewAspect=aw/ah;
  if(viewAspect>ASPECT){
    // viewport wider than map: fit height
    mapScale=ah/MAP_H;
    mapOX=(W-(MAP_W*Math.cos(MID_LAT_RAD)*mapScale))/2;
    mapOY=pad;
  } else {
    // viewport taller than map: fit width
    mapScale=aw/(MAP_W*Math.cos(MID_LAT_RAD));
    mapOX=pad;
    mapOY=(H-MAP_H*mapScale)/2;
  }
}
function proj(lon,lat){
  const x=mapOX+(lon-MAP_LON_MIN)*Math.cos(MID_LAT_RAD)*mapScale;
  const y=mapOY+(MAP_LAT_MAX-lat)*mapScale;
  return [x,y];
}

// ── STATE/PROVINCE POLYGONS ──
const STATES=[
{n:'BC',p:[[-130,60],[-120,60],[-120,49],[-114.1,49],[-120,53],[-124,54],[-128,56],[-130,58]]},
{n:'AB',p:[[-120,60],[-110,60],[-110,49],[-114.1,49],[-120,49]]},
{n:'SK',p:[[-110,60],[-102,60],[-102,49],[-110,49]]},
{n:'MB',p:[[-102,60],[-89,60],[-89,49],[-95.2,49],[-102,49]]},
{n:'ON',p:[[-89,56],[-80,56],[-75,46],[-74.3,45],[-76,44],[-79.8,43],[-82.4,41.7],[-84,46],[-85,47],[-89,48]]},
{n:'QC',p:[[-80,62],[-68,62],[-66,48],[-68,47],[-71.1,45],[-74.3,45],[-75,46],[-80,56]]},
{n:'WA',p:[[-124.7,49],[-117,49],[-117,46],[-124.6,46]]},
{n:'OR',p:[[-124.6,46],[-117,46],[-117,42],[-124.4,42]]},
{n:'CA',p:[[-124.4,42],[-120,42],[-119.5,39],[-117.5,36],[-117,34],[-115.5,33],[-117.2,32.5],[-118.5,34],[-120.5,35],[-122,37],[-123.8,40],[-124.4,42]]},
{n:'NV',p:[[-120,42],[-114,42],[-114,35],[-119.5,39]]},
{n:'ID',p:[[-117,49],[-111.1,49],[-111.1,42],[-114,42],[-117,46]]},
{n:'MT',p:[[-116,49],[-104.1,49],[-104.1,45],[-111.1,45],[-111.1,49],[-116,49]]},
{n:'WY',p:[[-111.1,45],[-104.1,45],[-104.1,41],[-111.1,41]]},
{n:'UT',p:[[-114,42],[-109.1,42],[-109.1,37],[-114,37]]},
{n:'CO',p:[[-109.1,41],[-102,41],[-102,37],[-109.1,37]]},
{n:'AZ',p:[[-114.8,37],[-109.1,37],[-109.1,31.3],[-114.7,32.7]]},
{n:'NM',p:[[-109.1,37],[-103,37],[-103,32],[-109.1,32]]},
{n:'ND',p:[[-104.1,49],[-97,49],[-97,46],[-104.1,46]]},
{n:'SD',p:[[-104.1,46],[-97,46],[-96.5,43],[-104.1,43]]},
{n:'NE',p:[[-104.1,43],[-95.3,43],[-95.3,40],[-104.1,40]]},
{n:'KS',p:[[-102,40],[-94.6,40],[-94.6,37],[-102,37]]},
{n:'OK',p:[[-103,37],[-94.4,37],[-94.4,33.9],[-100,33.9],[-100,36.5],[-103,36.5]]},
{n:'TX',p:[[-103.1,32],[-103.1,36.5],[-100,36.5],[-100,33.9],[-94.4,33.9],[-94,30],[-97,26],[-99.5,26.5],[-103,29],[-106.5,32]]},
{n:'MN',p:[[-97.2,49],[-89.5,49],[-89.5,43.5],[-96.5,43.5]]},
{n:'IA',p:[[-96.5,43.5],[-90.1,43.5],[-90.1,40.4],[-96,40.4]]},
{n:'MO',p:[[-95.8,40.6],[-89,40.6],[-89,36],[-95.8,36]]},
{n:'AR',p:[[-94.5,36.5],[-89.6,36.5],[-89.6,33],[-94.5,33]]},
{n:'LA',p:[[-94.1,33],[-89,33],[-89,29],[-91,29],[-93.5,29.5],[-94.1,30]]},
{n:'WI',p:[[-92.9,47],[-87,47],[-87,42.5],[-90.6,42.5],[-92.9,44]]},
{n:'IL',p:[[-91.5,42.5],[-87.5,42.5],[-87.5,37],[-91.5,37]]},
{n:'MI',p:[[-87.6,46],[-82.5,46],[-82.5,42],[-84.4,41.7],[-86,43.5],[-87.6,44]]},
{n:'IN',p:[[-88,41.8],[-84.8,41.8],[-84.8,37.8],[-88,37.8]]},
{n:'OH',p:[[-84.8,42],[-80.5,42],[-80.5,38.4],[-84.8,38.4]]},
{n:'PA',p:[[-80.5,42],[-75,42],[-75,39.7],[-80.5,39.7]]},
{n:'NY',p:[[-79.8,45],[-73.7,45],[-72,41],[-74,40.5],[-79.8,42.3]]},
{n:'VT',p:[[-73.4,45],[-72.5,45],[-72.5,42.7],[-73.4,42.7]]},
{n:'NH',p:[[-72.5,45],[-71,45],[-71,42.7],[-72.5,42.7]]},
{n:'MA',p:[[-73.4,42.7],[-70,42.7],[-70,41.2],[-71.4,41.2],[-73.4,42]]},
{n:'CT',p:[[-73.7,42],[-72,42],[-72,41],[-73.7,41]]},
{n:'NJ',p:[[-75.6,41.4],[-74,41.4],[-74,39],[-75.6,39]]},
{n:'DE',p:[[-75.8,39.8],[-75.1,39.8],[-75.1,38.5],[-75.8,38.5]]},
{n:'MD',p:[[-79.5,39.7],[-75.1,39.7],[-75.8,38.3],[-76.2,38],[-79.5,39.2]]},
{n:'VA',p:[[-83.7,39.5],[-75.2,38.3],[-75.5,37],[-76.5,37],[-80,37],[-83.7,37.5]]},
{n:'WV',p:[[-82.6,40.6],[-80.5,40.6],[-80.5,39.7],[-79.5,39.2],[-80,37.8],[-82.6,37.8]]},
{n:'KY',p:[[-89.6,37],[-82,38.5],[-82.6,37.8],[-84,37],[-89.6,37]]},
{n:'TN',p:[[-90,36.7],[-82,36.6],[-82,35],[-90,35]]},
{n:'NC',p:[[-84.3,36.6],[-75.5,36.5],[-75.5,34],[-78.5,34],[-84.3,35]]},
{n:'SC',p:[[-83.4,35],[-79,35],[-79,32],[-81,32],[-83.4,34.8]]},
{n:'GA',p:[[-85.6,35],[-81,35],[-80.9,30.5],[-82,30.3],[-85.6,31]]},
{n:'FL',p:[[-87.6,31],[-80,31],[-80,27],[-80.5,25.5],[-82,25],[-83,27],[-85,29],[-87.6,30.5]]},
{n:'AL',p:[[-88.5,35],[-85,35],[-85,31],[-88.5,30.2]]},
{n:'MS',p:[[-91.6,35],[-88.5,35],[-88.5,30.2],[-89.5,30],[-91.6,31]]}
];

// ── CANVAS SETUP ──
const discCV=document.getElementById('discC'),discX=discCV.getContext('2d');
const mapCV=document.getElementById('mapC'),mapX=mapCV.getContext('2d');
const dotCV=document.getElementById('dotC'),dotX=dotCV.getContext('2d');
let W,H,dpr,discs=[],dots=[];
let beatOn=true,bK=0,bH=0,bS=0,bC=0,aC=null,bI;
let mapAlpha=1;

function resize(){dpr=window.devicePixelRatio||1;W=innerWidth;H=innerHeight;[discCV,mapCV,dotCV].forEach(c=>{c.width=Math.round(W*dpr);c.height=Math.round(H*dpr);c.style.width=W+'px';c.style.height=H+'px';c.getContext('2d').setTransform(dpr,0,0,dpr,0,0)});calcProj()}

// ── MAP DRAWING ──
function drawMap(){
  mapX.clearRect(0,0,W,H);mapX.globalAlpha=mapAlpha;
  mapX.strokeStyle='rgba(255,255,255,.10)';mapX.lineWidth=1;mapX.lineJoin='round';mapX.lineCap='round';
  STATES.forEach(s=>{mapX.beginPath();s.p.forEach(([lon,lat],i)=>{const [x,y]=proj(lon,lat);i===0?mapX.moveTo(x,y):mapX.lineTo(x,y)});mapX.closePath();mapX.stroke()});
  const coast=[[-130,60],[-120,60],[-110,60],[-102,60],[-89,60],[-80,62],[-68,62],[-66,48],[-68,47],[-71,45],[-73.7,45],[-72,41],[-74,40.5],[-75.6,39],[-75.8,38.5],[-76.2,38],[-75.5,37],[-75.5,34],[-79,32],[-80.9,30.5],[-80,27],[-80.5,25.5],[-82,25],[-83,27],[-85,29],[-87.6,30.5],[-89.5,30],[-91,29],[-93.5,29.5],[-94.1,30],[-94,30],[-97,26],[-99.5,26.5],[-103,29],[-106.5,32],[-109.1,31.3],[-114.7,32.7],[-117.2,32.5],[-118.5,34],[-120.5,35],[-122,37],[-123.8,40],[-124.4,42],[-124.6,46],[-124.7,49],[-128,56],[-130,58],[-130,60]];
  mapX.beginPath();coast.forEach(([lon,lat],i)=>{const [x,y]=proj(lon,lat);i===0?mapX.moveTo(x,y):mapX.lineTo(x,y)});mapX.closePath();mapX.strokeStyle='rgba(255,255,255,.20)';mapX.lineWidth=1.6;mapX.stroke();
  const lakes=[[[-88,46.5],[-86,46],[-84.5,46],[-82.5,43.5],[-84,42],[-86.5,44],[-88,45.5]],[[-84,46.5],[-82,46.5],[-79.5,43.5],[-80,42.5],[-82,42],[-84,43]],[[-79,44],[-76.5,44],[-76,43.5],[-79,43]],[[-92,49],[-89,48.5],[-87,47],[-87.5,46],[-89,46.5],[-92,47.5]],[[-88,43],[-86.5,42],[-87,41.5],[-88,42]]];
  lakes.forEach(lk=>{mapX.beginPath();lk.forEach(([lon,lat],i)=>{const [x,y]=proj(lon,lat);i===0?mapX.moveTo(x,y):mapX.lineTo(x,y)});mapX.closePath();mapX.fillStyle='rgba(40,100,170,.05)';mapX.fill();mapX.strokeStyle='rgba(133,183,235,.18)';mapX.lineWidth=1;mapX.stroke()});
  mapX.beginPath();mapX.setLineDash([12,8]);
  [[-130,49],[-120,49],[-95.2,49],[-89,49],[-84,46],[-82.5,43],[-79,43.5],[-76,44],[-75,45],[-71,45],[-68,47]].forEach(([lon,lat],i)=>{const [x,y]=proj(lon,lat);i===0?mapX.moveTo(x,y):mapX.lineTo(x,y)});
  mapX.strokeStyle='rgba(255,255,255,.26)';mapX.lineWidth=1.7;mapX.stroke();mapX.setLineDash([]);
  mapX.font='700 18px "Syne"';mapX.textAlign='center';
  mapX.fillStyle='rgba(255,255,255,.12)';const [cx1,cy1]=proj(-106,54);mapX.fillText('CANADA',cx1,cy1);
  mapX.fillStyle='rgba(255,255,255,.10)';const [cx2,cy2]=proj(-100,35);mapX.fillText('UNITED STATES',cx2,cy2);
  mapX.globalAlpha=1;
}

// ── DISCS ──
function initDiscs(){const cs=['rgba(226,75,74,','rgba(133,183,235,','rgba(175,169,236,','rgba(237,147,177,','rgba(239,159,39,','rgba(159,225,203,'];discs=[{x:W*.08,y:H*.15,r:160,rot:0,sp:.007,c:cs[0],rn:6,p:0},{x:W*.9,y:H*.1,r:130,rot:2,sp:-.005,c:cs[1],rn:5,p:0},{x:W*.8,y:H*.85,r:180,rot:1,sp:.004,c:cs[2],rn:7,p:0},{x:W*.12,y:H*.88,r:120,rot:3,sp:-.008,c:cs[3],rn:4,p:0},{x:W*.5,y:H*.5,r:210,rot:0,sp:.003,c:cs[4],rn:8,p:0},{x:W*.95,y:H*.55,r:100,rot:1,sp:-.01,c:cs[5],rn:3,p:0}]}
function drawDiscs(){discX.clearRect(0,0,W,H);discX.fillStyle='#08080d';discX.fillRect(0,0,W,H);discs.forEach(d=>{const pf=beatOn?1+d.p*.16:1;d.rot+=d.sp*(beatOn?1+bK:1);d.p*=.86;discX.save();discX.translate(d.x,d.y);discX.rotate(d.rot);const r=d.r*pf;const g=discX.createRadialGradient(0,0,r*.2,0,0,r*1.3);g.addColorStop(0,d.c+'.08)');g.addColorStop(.6,d.c+'.035)');g.addColorStop(1,'rgba(0,0,0,0)');discX.fillStyle=g;discX.fillRect(-r*1.4,-r*1.4,r*2.8,r*2.8);discX.beginPath();discX.arc(0,0,r,0,Math.PI*2);discX.fillStyle=d.c+'.12)';discX.fill();discX.strokeStyle=d.c+'.15)';discX.lineWidth=1.2;discX.stroke();for(let i=1;i<=d.rn;i++){discX.beginPath();discX.arc(0,0,r*(i/(d.rn+1)),0,Math.PI*2);discX.strokeStyle=d.c+'.07)';discX.lineWidth=.8;discX.stroke()}discX.beginPath();discX.arc(0,0,r*.14,0,Math.PI*2);discX.fillStyle='rgba(8,8,13,.7)';discX.fill();discX.restore()})}

// ── DOTS ──
// Store ANGLE and DIST_FRACTION so positions can be recomputed each frame
// from the CURRENT marker position. This guarantees dots always stay aligned
// with city markers regardless of viewport resizes, font loading, etc.
function initDots(){dots=[];ALL.forEach(ev=>{const a=Math.random()*Math.PI*2,df=Math.random();const r=2.5+Math.random()*2.8;const gc=GC[ev.genre]||GC.Rock;dots.push({angle:a,distFrac:df,x:0,y:0,r,bR:r,genre:ev.genre,city:ev.city,evId:ev.id,color:gc.f,glow:gc.g,a:.6,tA:.6,ph:Math.random()*Math.PI*2,sp:Math.random()*.4+.2})})}
function updateDots(){const t=Date.now()*.001,kick=beatOn?bK:0,snare=beatOn?bS:0,pu=1+kick*.16+snare*.08;
// Annular scatter: dots live in a ring from minR to maxR around the marker,
// so they never overlap the vinyl disc (~60px) and stay clickable.
const minR=44,maxR=Math.max(110,Math.min(W,H)*.095);
// Read marker centers via a tiny pixel-precise anchor inside each marker.
// This is resilient to ANY CSS transform / zoom / browser chrome weirdness.
const centers={};Object.keys(DATA).forEach(name=>{const anchor=document.getElementById('anc-'+name.replace(/\s/g,''));if(anchor){const r=anchor.getBoundingClientRect();centers[name]={x:r.left+r.width/2,y:r.top+r.height/2}}else{const c=DATA[name],ofs=cityMarkerOffsets[name]||{x:0,y:0},base=proj(c.o,c.a);centers[name]={x:base[0]+ofs.x,y:base[1]+ofs.y}}});
dots.forEach(p=>{const c=centers[p.city];if(!c)return;
// sqrt(distFrac) gives uniform area distribution in the annulus
const dist=minR+Math.sqrt(p.distFrac)*(maxR-minR);
const hx=c.x+Math.cos(p.angle)*dist;const hy=c.y+Math.sin(p.angle)*dist;
p.x=hx+Math.sin(t*2+p.ph)*(1.2+kick*5);p.y=hy+Math.cos(t*2.3+p.ph)*(1.2+snare*4);
p.r=p.bR*pu+Math.sin(t*1.5+p.ph)*.2;p.a+=(p.tA-p.a)*.04})}
function drawDots(){dotX.clearRect(0,0,W,H);dots.forEach(p=>{if(p.a<.02)return;dotX.save();dotX.globalAlpha=p.a;if(p.a>.15){dotX.shadowColor=p.glow;dotX.shadowBlur=p.r*2}dotX.beginPath();dotX.arc(p.x,p.y,p.r,0,Math.PI*2);dotX.fillStyle=p.color;dotX.fill();dotX.shadowBlur=0;dotX.restore()})}

let qpT;
document.addEventListener('click',e=>{if(e.target.closest('.cm,.bt,.pb,.ed,.emx,.eo,.qpb,.lg,.cp,.em'))return;const mx=e.clientX,my=e.clientY;let best=null,bd=28;dots.forEach(p=>{if(p.a<.1)return;const d=Math.hypot(p.x-mx,p.y-my);if(d<bd){bd=d;best=p}});if(!best){hQ();return}const ev=ALL.find(a=>a.id===best.evId);if(ev)sQ(ev,mx,my);else hQ()});
document.addEventListener('mousemove',e=>{if(e.target.closest('.cm,.qp,.lg,.cp,.em'))return;let f=false;const mx=e.clientX,my=e.clientY;for(let i=0;i<dots.length;i++){if(dots[i].a<.1)continue;if(Math.hypot(dots[i].x-mx,dots[i].y-my)<16){f=true;break}}document.body.style.cursor=f?'pointer':'default'});
function sQ(ev,mx,my){const qp=document.getElementById('qp'),g=GC[ev.genre]||GC.Rock;let l=mx+14,t=my-50;if(l+250>W)l=mx-256;if(t<10)t=10;qp.style.left=l+'px';qp.style.top=t+'px';qp.innerHTML='<div class="qpg" style="background:'+g.f+';color:'+g.d+'">'+ev.genre+'</div><div class="qpa">'+ev.artist+'</div><div class="qpv">'+ev.venue+', '+ev.city+'</div><div class="qpr"><span>Date</span><span>'+ev.date+' / 2025</span></div><div class="qpb" onclick="event.stopPropagation();hQ();flyToCityByName(\''+ev.city.replace(/'/g,"\\'")+'\')">'+'Explore '+ev.city+' &rarr;</div>';qp.classList.add('show');clearTimeout(qpT);qpT=setTimeout(hQ,5000)}
function hQ(){document.getElementById('qp').classList.remove('show')}

// audio
function iA(){aC=new(window.AudioContext||window.webkitAudioContext)()}
function pK(){if(!aC)return;const o=aC.createOscillator(),g=aC.createGain();o.type='sine';o.frequency.setValueAtTime(160,aC.currentTime);o.frequency.exponentialRampToValueAtTime(28,aC.currentTime+.14);g.gain.setValueAtTime(.38,aC.currentTime);g.gain.exponentialRampToValueAtTime(.001,aC.currentTime+.16);o.connect(g);g.connect(aC.destination);o.start();o.stop(aC.currentTime+.16);bK=1;discs.forEach(d=>d.p=1)}
function pH(){if(!aC)return;const sz=aC.sampleRate*.03,buf=aC.createBuffer(1,sz,aC.sampleRate),dd=buf.getChannelData(0);for(let i=0;i<sz;i++)dd[i]=(Math.random()*2-1)*Math.pow(1-i/sz,8);const s=aC.createBufferSource(),g=aC.createGain(),hp=aC.createBiquadFilter();hp.type='highpass';hp.frequency.value=8000;s.buffer=buf;g.gain.setValueAtTime(.08,aC.currentTime);g.gain.exponentialRampToValueAtTime(.001,aC.currentTime+.03);s.connect(hp);hp.connect(g);g.connect(aC.destination);s.start();bH=1}
function pS(){if(!aC)return;const o=aC.createOscillator(),g=aC.createGain();o.type='triangle';o.frequency.setValueAtTime(180,aC.currentTime);o.frequency.exponentialRampToValueAtTime(60,aC.currentTime+.08);g.gain.setValueAtTime(.15,aC.currentTime);g.gain.exponentialRampToValueAtTime(.001,aC.currentTime+.1);o.connect(g);g.connect(aC.destination);o.start();o.stop(aC.currentTime+.1);const sz=aC.sampleRate*.05,buf=aC.createBuffer(1,sz,aC.sampleRate),dd=buf.getChannelData(0);for(let i=0;i<sz;i++)dd[i]=(Math.random()*2-1)*Math.pow(1-i/sz,4);const s=aC.createBufferSource(),g2=aC.createGain();s.buffer=buf;g2.gain.setValueAtTime(.1,aC.currentTime);g2.gain.exponentialRampToValueAtTime(.001,aC.currentTime+.05);s.connect(g2);g2.connect(aC.destination);s.start();bS=1;discs.forEach(d=>d.p=Math.max(d.p,.5))}
function startB(){if(!aC)iA();if(bI)clearInterval(bI);beatOn=true;bC=0;bI=setInterval(()=>{if(!beatOn){clearInterval(bI);bI=null;return}const p=bC%8;if(p===0||p===4)pK();if(p===2||p===6)pS();if(p%2===1)pH();bC++},60000/118/2);document.getElementById('beatBtn').classList.add('on');document.getElementById('bL').textContent='Beat on'}
function stopB(){beatOn=false;if(bI){clearInterval(bI);bI=null}document.getElementById('beatBtn').classList.remove('on');document.getElementById('bL').textContent='Start beat'}
document.getElementById('beatBtn').addEventListener('click',()=>{beatOn?stopB():startB()});

function loop(){drawDiscs();drawMap();bK*=.87;bH*=.84;bS*=.86;updateDots();drawDots();requestAnimationFrame(loop)}

// ── CITY MARKERS ──
function buildMarkers(){
  Object.keys(DATA).forEach(name=>{
    const c=DATA[name],clr=cityColor(name),ofs=cityMarkerOffsets[name]||{x:0,y:0},base=proj(c.o,c.a),cx=base[0]+ofs.x,cy=base[1]+ofs.y;
    const mk=document.createElement('div');mk.className='cm';mk.id='cm-'+name.replace(/\s/g,'');
    mk.style.left=cx+'px';mk.style.top=cy+'px';
    const gd=c.gd;let arcs='',cum=-90;
    Object.entries(gd).sort((a,b)=>b[1]-a[1]).forEach(([g,pct])=>{const r=32,ci=2*Math.PI*r;arcs+='<circle cx="32" cy="32" r="'+r+'" fill="none" stroke="'+GC[g].f+'" stroke-width="4" stroke-dasharray="'+(ci*pct)+' '+(ci*(1-pct))+'" stroke-dashoffset="'+(-ci*cum/360)+'" opacity=".5" transform="rotate(-90 32 32)"/>';cum+=pct*360});
    let gr='';for(let i=1;i<=3;i++){const s=48*(i/4);gr+='<div class="cgr" style="width:'+s+'px;height:'+s+'px"></div>'}
    mk.innerHTML='<div class="cg" style="background:'+clr+'"></div><svg class="cj" viewBox="0 0 64 64" style="position:absolute;top:50%;left:50%;width:64px;height:64px;transform:translate(-50%,-50%)">'+arcs+'</svg><div class="cr" style="border-color:'+clr+'"></div><div class="cd" style="border-color:'+clr+';background:radial-gradient(circle at 35% 35%,'+clr+'22,'+clr+'08)"><div class="cgs">'+gr+'</div><div class="cc"><div class="ccd" style="background:'+clr+'"></div></div></div><div class="cl"><div class="cn">'+name+'</div><div class="cme">'+c.e.toLocaleString()+' events</div></div><div id="anc-'+name.replace(/\s/g,'')+'" style="position:absolute;top:50%;left:50%;width:0;height:0;transform:translate(-50%,-50%);pointer-events:none"></div>';
    mk.addEventListener('click',e=>{e.stopPropagation();hQ();flyTo(name,cx,cy)});
    document.body.appendChild(mk);
  });
}
function repositionMarkers(){
  Object.keys(DATA).forEach(name=>{
    const c=DATA[name],ofs=cityMarkerOffsets[name]||{x:0,y:0},base=proj(c.o,c.a),cx=base[0]+ofs.x,cy=base[1]+ofs.y;
    const mk=document.getElementById('cm-'+name.replace(/\s/g,''));
    if(mk){mk.style.left=cx+'px';mk.style.top=cy+'px'}
  });
}

function flyTo(city,fx,fy){
  const fn=document.getElementById('fn');fn.textContent=city;fn.style.color=cityColor(city);
  fn.style.left=fx+'px';fn.style.top=fy+'px';fn.style.transform='translate(-50%,-50%) scale(.2)';fn.style.opacity='1';
  fn.classList.remove('go');void fn.offsetWidth;fn.classList.add('go');
  fn.style.left='50%';fn.style.top='42%';fn.style.transform='translate(-50%,-50%) scale(1)';
  setTimeout(()=>{fn.style.top='12%';fn.style.transform='translate(-50%,-50%) scale(.45)';fn.style.opacity='0'},600);
  setTimeout(()=>{fn.classList.remove('go');fn.style.opacity='0';openCity(city)},1000);
  document.getElementById('homeUI').classList.add('hid');document.getElementById('legend').classList.add('hid');
  mapAlpha=.15;
  document.querySelectorAll('.cm').forEach(m=>{m.style.opacity='0';m.style.pointerEvents='none'});
  dots.forEach(p=>{p.tA=p.city===city?.7:.02});
}
window.flyToCityByName=function(city){const c=DATA[city],ofs=cityMarkerOffsets[city]||{x:0,y:0},base=proj(c.o,c.a);flyTo(city,base[0]+ofs.x,base[1]+ofs.y)};

let eqA;
function openCity(city){
  const c=DATA[city],cc=cityColor(city),sorted=Object.entries(c.gd).sort((a,b)=>b[1]-a[1]);
  const cE=ALL.filter(e=>e.city===city);
  const vc={};cE.forEach(e=>{vc[e.venue]=(vc[e.venue]||0)+1});

  let eqH='';for(let i=0;i<36;i++){const h=6+Math.random()*55;eqH+='<div class="eqb" data-b="'+h+'" style="height:'+h+'px;background:'+cc+';opacity:.6"></div>'}

  // Genre DNA bars
  let gbH='';sorted.forEach(([g,p],i)=>{gbH+='<div class="gr" data-i="'+i+'"><div class="gn" style="color:'+GC[g].f+'">'+g+'</div><div class="gtr"><div class="gf" style="background:'+GC[g].f+'" data-w="'+(p*100)+'%">'+Math.round(p*100)+'%</div></div><div class="gp">'+Math.round(p*100)+'%</div></div>'});

  // Top Venues
  const vs=c.tv,vmx=vs[0]?vs[0][1]:1;
  let vbH='';vs.forEach(([v,n],i)=>{const sz=38+Math.round((n/vmx)*42),fs=sz>55?18:sz>45?14:11;vbH+='<div class="vb" data-i="'+i+'" style="--gw:'+cc+'44"><div class="vr">#'+(i+1)+'</div><div class="vc" style="width:'+sz+'px;height:'+sz+'px;background:'+cc+'12;border-color:'+cc+'35"><div class="vn" style="font-size:'+fs+'px;color:'+cc+'">'+n+'</div><div class="ve" style="color:'+cc+'">shows</div></div><div class="vl">'+v+'</div></div>'});

  // Event dots — sorted by genre frequency (most common first)
  const gOrder=sorted.map(s=>s[0]);
  cE.sort((a,b)=>gOrder.indexOf(a.genre)-gOrder.indexOf(b.genre));
  let doH='';cE.forEach(ev=>{const gc=GC[ev.genre]||GC.Rock;doH+='<div class="ed" data-id="'+ev.id+'" data-t="'+ev.artist+' — '+ev.venue+'" style="background:'+gc.f+';--gw:'+gc.g+'"></div>'});

  const pan=document.getElementById('cp');
  pan.innerHTML='<button class="pb" id="pBack"><svg viewBox="0 0 24 24"><path d="M19 12H5M12 5l-7 7 7 7"/></svg>All cities</button>'+
    '<div class="ch"><div class="eqw" id="eqC">'+eqH+'</div><div class="chc"><div class="chn" id="cN" style="color:'+cc+'">'+city+'</div><div class="chv" id="cV">'+(CV[city]||'')+'</div></div></div>'+
    '<div class="sr"><div class="ss"><div class="sl">Events</div><div class="sv">'+c.e.toLocaleString()+'</div></div><div class="ss"><div class="sl">Venues</div><div class="sv">'+c.v+'</div></div><div class="ss"><div class="sl">Artists</div><div class="sv">'+c.r.toLocaleString()+'</div></div><div class="ss"><div class="sl">Top genre</div><div class="sv" style="color:'+GC[sorted[0][0]].f+'">'+sorted[0][0]+'</div></div></div>'+
    '<div class="tc"><div class="col"><div class="st">Genre DNA</div><div class="gb">'+gbH+'</div></div><div class="col"><div class="st">Top Venues</div><div class="vbs">'+vbH+'</div></div></div>'+
    '<div class="es"><div class="st">All '+cE.length+' events — hover & click</div><div class="ew">'+doH+'</div></div>';

  pan.classList.add('open');
  setTimeout(()=>{document.getElementById('cN').classList.add('in')},100);
  setTimeout(()=>{document.getElementById('cV').classList.add('in')},300);
  setTimeout(()=>{pan.querySelectorAll('.gr').forEach((r,i)=>{setTimeout(()=>{r.classList.add('in');const f=r.querySelector('.gf');if(f)setTimeout(()=>{f.style.width=f.dataset.w},80)},i*150)})},500);
  setTimeout(()=>{pan.querySelectorAll('.vb').forEach((b,i)=>{setTimeout(()=>{b.classList.add('in')},i*120)})},500+sorted.length*150);
  const eqB=[...document.querySelectorAll('#eqC .eqb')];if(eqA)cancelAnimationFrame(eqA);
  (function aE(){if(!pan.classList.contains('open'))return;const t=Date.now()*.001;eqB.forEach((b,i)=>{const base=parseFloat(b.dataset.b),w=Math.sin(t*3.5+i*.5)*14,bb=beatOn?bK*50+bS*30:0;b.style.height=Math.max(4,base+w+bb*(Math.random()*.6+.4))+'px'});eqA=requestAnimationFrame(aE)})();
  pan.querySelectorAll('.ed').forEach(d=>{d.addEventListener('click',()=>{const ev=ALL.find(e=>e.id===parseInt(d.dataset.id));if(ev)openEv(ev)})});
  pan.querySelector('#pBack').addEventListener('click',closeCity);
}

function closeCity(){document.getElementById('cp').classList.remove('open');document.getElementById('homeUI').classList.remove('hid');document.getElementById('legend').classList.remove('hid');mapAlpha=1;document.querySelectorAll('.cm').forEach(m=>{m.style.opacity='1';m.style.pointerEvents='auto'});dots.forEach(p=>{p.tA=.6});if(eqA)cancelAnimationFrame(eqA)}

function openEv(ev){
  const g=GC[ev.genre]||GC.Rock;
  let bars='';for(let i=0;i<55;i++){const h=4+Math.random()*32;bars+='<div class="wb" style="height:'+h+'px;background:'+g.f+';opacity:'+(0.2+Math.random()*.55)+'"></div>'}
  const m=document.getElementById('emM');
  m.innerHTML='<button class="emx" id="emX">&times;</button><div class="emh"><div class="etg" style="background:'+g.f+';color:'+g.d+'">'+ev.genre+'</div><div class="ett">'+ev.artist+'</div><div class="ets">Live at '+ev.venue+'</div></div><div class="emb"><div class="emd"><div class="emr"><span class="eml">Date</span><span class="emv">'+ev.date+' / 2025</span></div><div class="emr"><span class="eml">City</span><span class="emv">'+ev.city+'</span></div><div class="emr"><span class="eml">Genre</span><span class="emv" style="color:'+g.f+'">'+ev.genre+'</span></div></div><div class="emw">'+bars+'<span class="ewl">setlist.fm</span></div></div>';
  m.classList.add('open');document.getElementById('eo').classList.add('open');
  m.querySelector('#emX').addEventListener('click',closeEv);
}
function closeEv(){document.getElementById('emM').classList.remove('open');document.getElementById('eo').classList.remove('open')}
document.getElementById('eo').addEventListener('click',closeEv);

window.addEventListener('resize',()=>{resize();initDiscs();repositionMarkers()});
resize();initDiscs();initDots();buildMarkers();loop();
console.log('[UMP v5]','innerW='+innerWidth,'innerH='+innerHeight,'clientW='+document.documentElement.clientWidth,'clientH='+document.documentElement.clientHeight,'dpr='+dpr,'screenW='+screen.width,'screenH='+screen.height,'mapScale='+mapScale.toFixed(2));
// Compare marker rendered pos to dot rendered pos for Calgary
setTimeout(()=>{const mk=document.getElementById('cm-Calgary');if(mk){const r=mk.getBoundingClientRect();const sl=parseFloat(mk.style.left);const st=parseFloat(mk.style.top);const anc=document.getElementById('anc-Calgary');const ar=anc?anc.getBoundingClientRect():null;const cDots=dots.filter(p=>p.city==='Calgary');const dAvg=cDots.reduce((s,p)=>({x:s.x+p.x,y:s.y+p.y}),{x:0,y:0});dAvg.x/=cDots.length;dAvg.y/=cDots.length;console.log('[UMP v5 Calgary]','marker style=('+sl.toFixed(1)+','+st.toFixed(1)+')','marker bRect=('+(r.left+r.width/2).toFixed(1)+','+(r.top+r.height/2).toFixed(1)+')','marker size='+r.width.toFixed(0)+'x'+r.height.toFixed(0),'anchor=('+(ar?(ar.left+ar.width/2).toFixed(1)+','+(ar.top+ar.height/2).toFixed(1):'null')+')','dotAvg=('+dAvg.x.toFixed(1)+','+dAvg.y.toFixed(1)+')','canvasSize='+dotCV.width+'x'+dotCV.height,'cssSize='+dotCV.style.width+'x'+dotCV.style.height)}},800);
document.addEventListener('click',function f(){startB();document.removeEventListener('click',f)},{once:true});
try{iA();startB()}catch(e){}
</script></body></html>'''

with open('hero-real-data.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Written hero-real-data.html ({len(html)/1024:.1f} KB)')
