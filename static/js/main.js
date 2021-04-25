const lastSeenForm = document.getElementById('last-seen-form');
// STEP 2: Add `handleAddRecord` event listener on form's submit events
lastSeenForm.addEventListener('submit', handleAddRecord);

// Helper functions
function handleAddRecord(event) {
  event.preventDefault();

  const record = getRecordFromForm(event);
  
  // STEP 3: Replace alert function with addLastSeen
  addLastSeen(record);

  // STEP 6: Clear text input
  document.getElementById('last-seen-location').value="";
}

function addLastSeen(record) {
  const list = document.getElementById("last-seen-list");

  const item = createLastSeenItem(record);
  list.appendChild(item);
}

function createLastSeenItem(record) {
  const item = document.createElement('li');

  // STEP 4: Create paragraph element and add to list item
  const p = document.createElement('p');
  p.textContent = record.location;
  item.appendChild(p);

  // Add a button to delete the item from list
  const button = document.createElement('input');
  button.type = 'image';
  button.src = '/static/img/delete.png';
  button.className = 'delete-button';
  // STEP 5: Add onclick event to remove list item
  button.onclick = () => { item.remove() };
  item.append(button);

  return item;
}

function getRecordFromForm(event) {
  const formData = new FormData(event.currentTarget);
  const data = Object.fromEntries(formData.entries());
  return data;
}