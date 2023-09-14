

document.getElementById('createCustomerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('createName').value;
    const email = document.getElementById('createEmail').value;
    const phone = document.getElementById('createPhone').value;

    // Send data to backend (you'd need AJAX or fetch API)
});

function readCustomer() {
    const customerId = document.getElementById('readCustomerId').value;

    // Send request to backend to get customer details
    // Update the readCustomerDetails div with the response
}

function updateCustomer() {
    const customerId = document.getElementById('updateCustomerId').value;
    const name = document.getElementById('updateName').value;
    const email = document.getElementById('updateEmail').value;
    const phone = document.getElementById('updatePhone').value;

    // Send data to backend for updating customer
}

function deleteCustomer() {
    const customerId = document.getElementById('deleteCustomerId').value;

    // Send request to backend to delete customer
}
