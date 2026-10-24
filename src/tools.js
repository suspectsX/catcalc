(function () {
  'use strict';
  const $ = id => document.getElementById(id);
  const kitten = [[0,0],[1,1],[2,2],[3,4],[4,6],[6,10],[8,12],[12,15]];
  function interp(m) {
    for (let i=1; i<kitten.length; i++) {
      const [a,x]=kitten[i-1], [b,y]=kitten[i];
      if (m<=b) return x+(y-x)*(m-a)/(b-a);
    }
    return 15;
  }
  const stage = y => y<1 ? 'Kitten' : y<7 ? 'Young adult' : y<=10 ? 'Mature adult' : 'Senior';
  function number(id, label, min, max, whole=false, optional=false) {
    const el=$(id), raw=el.value.trim(), value=Number(raw);
    let message='';
    if (el.validity.badInput) message=`${label}: enter a finite number.`;
    else if (!raw && optional) return null;
    else if (!raw || !Number.isFinite(value)) message=`${label}: enter a finite number.`;
    else if (value<min || value>max) message=`${label}: enter ${min} to ${max}.`;
    else if (whole && !Number.isInteger(value)) message=`${label}: enter a whole number.`;
    el.setCustomValidity(message);
    if (message) throw {element:el, message};
    return value;
  }
  function calculator(formId, resultId, errorId, calculate) {
    const form=$(formId), result=$(resultId), error=$(errorId);
    if (!form) return;
    const status=document.createElement('p');
    status.className='small'; status.setAttribute('role','status');
    result.after(status);
    const markStale=()=>{
      form.querySelectorAll('input,select').forEach(el=>{el.setCustomValidity('');el.removeAttribute('aria-invalid')});
      error.textContent=''; result.hidden=true;
      status.textContent='Inputs changed — calculate again.';
    };
    form.addEventListener('input',markStale);
    form.addEventListener('change',markStale);
    const run=(event)=>{
      if(event) event.preventDefault();
      error.textContent='';
      form.querySelectorAll('input,select').forEach(el=>{el.setCustomValidity('');el.removeAttribute('aria-invalid')});
      try {
        const output=calculate();
        if(!form.reportValidity()) return;
        result.innerHTML=output; result.hidden=false; status.textContent='';
      } catch(problem) {
        if(!problem.element) throw problem;
        error.textContent=problem.message;
        problem.element.setAttribute('aria-invalid','true');
        problem.element.reportValidity(); problem.element.focus();
      }
    };
    form.addEventListener('submit',run); run();
  }
  calculator('age-tool','ares','aerror',()=>{
    const y=number('ay','Years',0,35,true), m=number('am','Months',0,11,true), t=y+m/12;
    const h=t<1 ? interp(t*12) : t<2 ? 15+9*(t-1) : 24+4*(t-2);
    return `For ${y} years and ${m} months: about <strong>${Math.round(h)}</strong> human years.<br>Life stage: <b>${stage(t)}</b>.`;
  });
  const poundsToKg=0.45359237;
  const foodLimits={kg:10000,cup:2000,can:2000};
  function units() {
    if(!$('cw')) return;
    const lb=$('cu').value==='lb', min=lb?0.3/poundsToKg:0.3, max=lb?15/poundsToKg:15;
    $('cw').min=String(min); $('cw').max=String(max);
    $('weight-range').textContent=`Supported range: ${lb?'about 0.662–33.069 lb':'0.3–15 kg'} (0.3–15 kg). Ask your vet about weights outside this calculator's range.`;
    const unit=$('ckunit').value;
    $('ck').max=String(foodLimits[unit]);
    $('food-range').textContent=`Copy the label: 1–${foodLimits[unit]} kcal/${unit}, whole numbers. Leave blank to skip food conversion.`;
  }
  if($('cu')) {
    $('cu').addEventListener('change',units); $('ckunit').addEventListener('change',units); units();
  }
  calculator('cal-tool','cres','cerror',()=>{
    const unit=$('cu').value, foodUnit=$('ckunit').value;
    if(!['kg','lb'].includes(unit) || !(foodUnit in foodLimits)) throw new Error('Unknown unit');
    const entered=number('cw','Weight',Number($('cw').min),Number($('cw').max));
    const kg=unit==='lb'?entered*poundsToKg:entered;
    const factor=Number($('cf').value);
    if(![0.8,1,1.2,1.4,2.5].includes(factor)) throw new Error('Unknown cat type');
    const food=number('ck','Food calories',1,foodLimits[foodUnit],true,true);
    const rer=70*Math.pow(kg,0.75), kcal=rer*factor;
    let out=`For ${entered} ${unit} (${kg.toFixed(2)} kg): daily starting estimate <strong>${Math.round(kcal)} kcal</strong> <span class="small">(RER ${Math.round(rer)} kcal × ${factor})</span>.`;
    if(food!==null) {
      const amount=foodUnit==='kg'?`${Math.round(kcal/food*1000)} g`:foodUnit==='cup'?`${(kcal/food).toFixed(2)} cups`:`${(kcal/food).toFixed(2)} cans`;
      out+=`<br>Food-only allowance: <strong>${amount}</strong> (split into 2+ meals). Reduce this allowance for any treats.`;
    }
    return out+`<br><span class="small">Treats: under about ${Math.round(kcal*0.1)} kcal within this total, never added on top. Adjust with your vet using body condition.</span>`;
  });
  if($('fsearch')) $('fsearch').addEventListener('input',event=>{
    const q=event.target.value.toLowerCase().trim(); let total=0;
    document.querySelectorAll('.food-group').forEach(group=>{
      let matches=0;
      group.querySelectorAll('li').forEach(li=>{
        li.hidden=!!q&&!li.textContent.toLowerCase().includes(q);
        if(!li.hidden) matches++;
      });
      group.hidden=matches===0; total+=matches;
    });
    $('fstatus').textContent=total?`${total} food${total===1?'':'s'} found`:'No foods found. Try another food name.';
  });
  if($('ngo')&&window.CAT_NAMES) {
    const run=()=>{
      const names=[...window.CAT_NAMES[$('nstyle').value]];
      for(let i=names.length-1;i>0;i--) {const j=Math.floor(Math.random()*(i+1));[names[i],names[j]]=[names[j],names[i]]}
      $('nres').innerHTML=names.slice(0,8).map(name=>`<li>${name}</li>`).join('');
    };
    $('ngo').addEventListener('click',run); $('nstyle').addEventListener('change',run); run();
  }
  const header=document.querySelector('.top'), buy=document.querySelector('.buy');
  function stickyOffset() {
    const height=header?header.getBoundingClientRect().height:0;
    document.documentElement.style.setProperty('--header-height',`${height}px`);
    if(buy) buy.classList.toggle('no-sticky',window.innerWidth<=760 || buy.getBoundingClientRect().height+height+28>window.innerHeight);
  }
  window.addEventListener('resize',stickyOffset);
  if(window.ResizeObserver) {
    const observer=new ResizeObserver(stickyOffset);
    if(header) observer.observe(header);
    if(buy) observer.observe(buy);
  }
  stickyOffset();
})();
