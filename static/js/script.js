console.log('JavaScript Working')
let btn = document.querySelector('button');
btn.onclick = document.addEventListener('click', ()=>{
    document.getElementById('showTODOs').style.display = 'block';
})