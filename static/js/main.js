function addLastSeenElement(event) {
  const list = document.getElementById("last-seen");

  const item = document.createElement('li');
  item.id = `last-seen-${event.id}`;

  const p = document.createElement('p');
  p.textContent = event.location;
  item.appendChild(p);

  const button = document.createElement('input');
  button.type = 'image';
  button.src = '/static/img/delete.png';
  button.className = 'delete-button';
  button.onclick = () => {
    fetch(`/api/events/${event.id}`, {
      method: 'DELETE'
    }).then(() => item.remove());
  }
  item.append(button);

  list.appendChild(item);
}

const lastSeenForm = document.getElementById('last-seen-form');
lastSeenForm.addEventListener('submit', (e) => {
  e.preventDefault();
  console.log(e.currentTarget);
  const formData = new FormData(e.currentTarget);
  const data = Object.fromEntries(formData.entries());
  const json = JSON.stringify(data);

  fetch('/api/events', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: json
  }).then((response) => response.json())
  .then((newEvent) => addLastSeenElement(newEvent));
})

fetch('/api/events')
  .then((response) => response.json())
  .then((json) => {
    
    json.forEach((event) => {
      addLastSeenElement(event);
    });
  })