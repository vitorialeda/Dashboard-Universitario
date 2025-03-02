// Atualiza o atributo 'concluido' para true ou false e manda pro banco de dados
function atualizaTodo(todo){
    const id = todo.id
    const status = todo.checked
    console.log(todo)

    fetch('/atualizaStatus', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json'},
        body: JSON.stringify({ id, status })
    });

    progressBar()

}

// Setta progressBar
async function progressBar(){

  progresso = await fetch("/progresso")
  progresso = await progresso.json()

  total = progresso.total
  concluidas = progresso.concluidas
  porcentagem = concluidas / total * 100.0

  const progressBar = document.querySelector('.progress-bar')

  progressBar.setAttribute("aria-valuenow", porcentagem)
  progressBar.style.setProperty("--progress", porcentagem + "%")


  document.querySelector(".info").innerHTML = "<p>Total de tarefas: "+ total + "</p><p> Tarefas concluidas: " + concluidas + "</p>"

}


// Inicia progressBar
document.addEventListener('DOMContentLoaded', progressBar())


// Ativa o primeiro item da lista de disciplinas
document.addEventListener('DOMContentLoaded',()=> document.querySelector('.carousel-item').classList.add('active'))


// Atualiza checkbox ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll("input").forEach((element)=>{

    if(element.value == 'True'){
      element.setAttribute("checked","checked")
    }
    else{
      element.removeAttribute("checked")
    }
  })
})