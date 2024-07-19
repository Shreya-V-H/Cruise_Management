/**f-s */
let orderSummary = [];  
let totalAmount = 0;   

function addItem(item, price) {
  orderSummary.push({ item, price });
  totalAmount += price;
  updateSummary();
}
function updateSummary() {
  const summaryElement = document.getElementById('order-summary');
  const totalAmountElement = document.getElementById('total-amount');

  summaryElement.innerHTML = '';
  orderSummary.forEach(order => {
    const listItem = document.createElement('li');
    listItem.textContent = `${order.item} - $${order.price}`;
    summaryElement.appendChild(listItem);
  });

  totalAmountElement.textContent = `Total Amount: $${totalAmount}`;
}

function orderFood() {
  const successMessageElement = document.getElementById('order-success-message');
  successMessageElement.style.display = 'block';
}

/**f-e */