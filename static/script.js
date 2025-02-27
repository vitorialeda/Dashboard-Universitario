
function atualizaTodo(todo){
    const id = todo.id
    const status = todo.checked

    todo.checked ? todo.setAttribute("checked", "checked") : todo.removeAttribute("checked")

    fetch('/atualizaStatus', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json'},
        body: JSON.stringify({ id, status })
    });
}

 document.addEventListener('DOMContentLoaded', async function() {
  
  // Popula array evento com objeto evento de forma que os atributos
  // correspondam ao objeto events do calendar.
    eventos = []
    await fetch("/eventos")
    .then(response => response.json())
    .then(data => data.forEach(element => {
      evento = {
        id: element.id,
        title: element.nome,
        start: element.prazo
      }
      eventos.push(evento)
    }))


    // Renderiza calendario.
    const calendarEl = document.getElementById('calendar')
    const calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      locale:'pt-br',
      events: eventos
    })

    calendar.render()
  })