function updatePrice() {
    var total = 0.00;
    for (var servico in servicePrices) {
        if (document.getElementById(servico).checked) {
            total += servicePrices[servico];
        }
    }
    document.getElementById('totalPrice').innerText = total.toFixed(2);
}

function maskPhone(event) {
    var input = event.target;
    var value = input.value.replace(/\D/g, '');
    var length = value.length;

    if (length > 11) {
        value = value.slice(0, 11);
    }

    if (length > 0) {
        value = '(' + value;
    }
    if (length > 2) {
        value = value.slice(0, 3) + ') ' + value.slice(3);
    }
    if (length > 7) {
        value = value.slice(0, 10) + '-' + value.slice(10);
    }

    input.value = value;
}
