const lastSeenForm = document.getElementById('last-seen-form');
lastSeenForm.addEventListener('submit', handleAddRecord);

fetchRecords();

// Helper functions
function handleAddRecord(event) {
  event.preventDefault();

  const record = getRecordFromForm(event);
  
  saveRecord(record)
    .then((newRecord) => addLastSeenElement(newRecord));

  // Clear out value from input field
  document.getElementById('last-seen-location').value="";
}

function addLastSeenElement(record) {
  const list = document.getElementById("last-seen-list");

  const item = createLastSeenItem(record);
  list.appendChild(item);
}

function createLastSeenItem(record) {
  const item = document.createElement('li');
  item.id = `last-seen-${record.id}`;

  // Add location text to item
  const p = document.createElement('p');
  p.textContent = record.location;
  item.appendChild(p);

  // Add a button to delete the item from list
  const button = document.createElement('input');
  button.type = 'image';
  button.src = '/static/img/delete.png';
  button.className = 'delete-button';
  button.onclick = () => {
    deleteRecord(record.id).then(() => item.remove());
  }
  item.append(button);

  return item;
}

function deleteRecord(recordId) {
  return fetch(`/api/records/${recordId}`, {
      method: 'DELETE'
    });
}

function saveRecord(record) {
  return fetch('/api/records', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(record)
  }).then((response) => response.json());
}

function getRecordFromForm(event) {
  const formData = new FormData(event.currentTarget);
  const data = Object.fromEntries(formData.entries());
  return data;
}

function fetchRecords() {
  fetch('/api/records')
    .then((response) => response.json())
    .then((json) => {     
      json.forEach((record) => {
        addLastSeenElement(record);
      });
    })
}