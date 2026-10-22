(function () {
  "use strict";
  var button=document.querySelector('[data-menu-button]');
  var menu=document.querySelector('[data-menu]');
  if(button&&menu){
    function close(){menu.classList.remove('is-open');button.setAttribute('aria-expanded','false');}
    button.addEventListener('click',function(){var open=!menu.classList.contains('is-open');menu.classList.toggle('is-open',open);button.setAttribute('aria-expanded',String(open));});
    menu.addEventListener('click',function(event){if(event.target.closest('a'))close();});
    document.addEventListener('keydown',function(event){if(event.key==='Escape')close();});
    document.addEventListener('pointerdown',function(event){if(!menu.contains(event.target)&&!button.contains(event.target))close();});
    window.addEventListener('resize',function(){if(window.innerWidth>1020)close();});
  }
  var shot=document.querySelector('[data-product-shot]');
  if(shot){var missing=function(){shot.closest('.screenshot').classList.add('is-missing');};shot.addEventListener('error',missing);if(shot.complete&&shot.naturalWidth===0)missing();}
})();
