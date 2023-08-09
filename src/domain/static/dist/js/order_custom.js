let rowCount = 1; // Start with 1 because you already have one row in the form

function addRow() {
    const rowsContainer = document.getElementById('rowsContainer');

    const newRow = document.createElement('div');
    newRow.className = "row";

    newRow.innerHTML = `
        <div class="form-group col">
            <label for="inputItem">Item</label>
            <input type="text" id="inputItem" name="item[${rowCount}]" class="form-control">
        </div>

        <div class="form-group col">
            <label for="inputPrice">Price</label>
            <input type="number" id="inputPrice" name="price[${rowCount}]" class="form-control">
        </div>

        <div class="form-group col">
            <label for="inputDiscount">Discount</label>
            <input type="number" id="inputDiscount" name="discount[${rowCount}]" class="form-control">
        </div>

        <div class="form-group col">
            <label for="inputTotalPrice">Total Price</label>
            <input type="number" id="inputTotalPrice" name="total_price[${rowCount}]" class="form-control">
        </div>
    `;

    rowsContainer.appendChild(newRow);
    rowCount++; // Increment the counter for next row
}

function removeLastRow() {
    const rowsContainer = document.getElementById('rowsContainer');
    if (rowsContainer.children.length > 1) {  // Keep the initial row, don't delete it
        rowsContainer.removeChild(rowsContainer.lastChild);
        rowCount--;
    }
}

document.addEventListener('input', function(e) {
    // Check if the event is triggered from an input with name starting with "price[" or "discount["
    if (e.target.name.startsWith('price[') || e.target.name.startsWith('discount[')) {
        // Extract row index from the input name
        const rowIndex = e.target.name.match(/\d+/)[0];

        // Get the associated price and discount inputs for this row
        const priceInput = document.querySelector(`input[name="price[${rowIndex}]"]`);
        const discountInput = document.querySelector(`input[name="discount[${rowIndex}]"]`);
        const totalPriceInput = document.querySelector(`input[name="total_price[${rowIndex}]"]`);

        // Calculate the total price: price - (price * discount / 100)
        const price = parseFloat(priceInput.value) || 0;
        const discount = parseFloat(discountInput.value) || 0;
        const totalPrice = price - (price * discount / 100);

        // Update the total price input with the calculated value
        totalPriceInput.value = totalPrice.toFixed(2);
    }
});