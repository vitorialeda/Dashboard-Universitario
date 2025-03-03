// Atualiza o atributo 'concluido' para true ou false e manda pro banco de dados
function atualizaTodo(todo){
    const id = todo.id
    const status = todo.checked.toString()

    fetch('/atualizaStatus', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json'},
        body: JSON.stringify({ id, status })
    });

    attCheckboxes(id, status)
    progressBar()

}


// Setta progressBar
async function progressBar(){

  progressoI = await fetch("/progresso")
  progresso = await progressoI.json()

  total = progresso.total
  concluidas = progresso.concluidas
  porcentagem = concluidas / total * 100.0

  const progressb = document.querySelector('.progress-bar')

  progressb.setAttribute("aria-valuenow", porcentagem)
  progressb.style.setProperty("--progress", porcentagem + "%")

  total == 1 ? tqtd = "tarefa": tqtd = "tarefas"
  concluidas == 1 ? qtd = "tarefa": qtd = "tarefas"


  document.querySelector(".info").innerHTML =   "<p>Total: " +  total + " " + tqtd + "</p>" +
  "<p>Concluidas: " + concluidas + " " + qtd + "</p>"

}


// Determina atributo "checked" dos inputs com id especificado 
function attCheckboxes(id, status){
  inputs = document.querySelectorAll("input[id='"+id+"']").forEach(element => {
    if(status == 'true'){
      element.setAttribute("checked","checked")
    }
    else{
      element.removeAttribute("checked")
    }
  });
}


// Inicia Calendario
document.addEventListener('DOMContentLoaded', async function() {

  eventos = []
  await fetch("/eventos")
  .then(response => response.json())
  .then(data => data.forEach(element => {
    evento = {
      id: element.id,
      title: element.nome,
      start: element.prazo,
    }

    eventos.push(evento)
  }))

  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    headerToolbar:{
      left:   'title',
      center: '',
      right:  'prev,next'
    },
    locale:'pt-br',
    editable: true,
    selectable: true,
    businessHours: true,
    events: eventos,
    eventColor: '#FBE345',
    dayMaxEvents: true // allow "more" link when too many events
  }
);

  calendar.render();
});


// Inicia progressBar
document.addEventListener('DOMContentLoaded', progressBar)


// Ativa o primeiro item da lista de disciplinas
document.addEventListener('DOMContentLoaded',()=> document.querySelector('.carousel-item').classList.add('active'))


// Atualiza checkbox ao carregar a página
document.addEventListener('DOMContentLoaded',()=>{
  document.querySelectorAll("input").forEach(element => attCheckboxes(element.id,element.value))
})
