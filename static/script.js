
function atualizaTodo(todo){
    const id = todo.id
    const status = todo.checked

    fetch('/atualizaStatus', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json'},
        body: JSON.stringify({ id, status })
    });
}