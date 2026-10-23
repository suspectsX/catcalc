(function(){
const $=id=>document.getElementById(id);
// Age: AAHA/AAFP 2021 -> 1y=15, 2y=24, +4/yr. Under 1y approximate.
const kitten=[[0,0],[1,1],[2,2],[3,4],[4,6],[6,10],[8,12],[12,15]];
function interp(m){for(let i=1;i<kitten.length;i++){const[a,x]=kitten[i-1],[b,y]=kitten[i];if(m<=b)return x+(y-x)*(m-a)/(b-a)}return 15}
function stage(y){return y<1?"Kitten":y<7?"Young adult":y<=10?"Mature adult":"Senior"}
if($('ago')){const run=()=>{const y=Math.max(0,+$('ay').value||0),m=Math.min(11,Math.max(0,+$('am').value||0)),t=y+m/12;
let h=t<1?interp(t*12):t<2?15+9*(t-1):24+4*(t-2);
$('ares').innerHTML=`Your cat is about <strong>${Math.round(h)}</strong> in human years.<br>Life stage: <b>${stage(t)}</b>${t>=10?' (twice-yearly vet checks are often recommended for seniors)':''}.`};
$('ago').onclick=run;run();}
// Calories: RER=70*kg^0.75 * factor
if($('cgo')){const run=()=>{let w=+$('cw').value||0;if($('cu').value==='lb')w=w*0.453592;if(w<=0){$('cres').textContent='Enter a weight.';return}
const rer=70*Math.pow(w,0.75),f=+$('cf').value,k=rer*f,kc=+$('ck').value;let out=`Daily need: <strong>${Math.round(k)} kcal</strong> <span class="small">(RER ${Math.round(rer)} kcal × ${f})</span>`;
if(kc>0){const u=$('ckunit').value,amt=u==='kg'?`${Math.round(k/kc*1000)} g`:u==='cup'?`${(k/kc).toFixed(2)} cups`:`${(k/kc).toFixed(2)} cans`;out+=`<br>Food per day: <strong>${amt}</strong> (split into 2+ meals)`}
out+=`<br><span class="small">Treats: keep under ~${Math.round(k*0.1)} kcal/day (10%).</span>`;$('cres').innerHTML=out};$('cgo').onclick=run;run();}
// Food search
if($('fsearch')){$('fsearch').addEventListener('input',ev=>{const q=ev.target.value.toLowerCase().trim();document.querySelectorAll('.cols li').forEach(li=>{li.style.display=!q||li.textContent.toLowerCase().includes(q)?'':'none'})})}
// Names
if($('ngo')&&window.CAT_NAMES){const run=()=>{const l=[...CAT_NAMES[$('nstyle').value]];for(let i=l.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[l[i],l[j]]=[l[j],l[i]]}$('nres').innerHTML=l.slice(0,8).map(n=>`<li>${n}</li>`).join('')};$('ngo').onclick=run;run();}
// Ads: if AdSense loaded, fill slots with responsive units only when publisher id present (auto ads also works)
})();
