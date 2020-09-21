let amount = {{ amount }};
const product = {{ product.id }};
const order = {{ order.id }};
const cart = {{ cart.id }};

function add_to_cart() {
    let new_amount = parseInt(document.querySelector('#amount_input').value);
    let token = document.querySelector('input[name=csrfmiddlewaretoken]').value;
    console.log(new_amount, token);
    if (amount === new_amount || new_amount < 0)
        return;
    let body;
    let method;
    let url;
    if (amount === 0) {
        method = 'POST';
        body = {
            'item': product,
            'amount': new_amount,
            'order': order
        };
        url = '/api/cart/';
    } else if (new_amount === 0) {
        method = 'DELETE';
        body = null;
        url = '/api/cart/' + cart + '/';
    } else {
        method = 'PATCH';
        body = {
            'amount': new_amount
        };
        url = '/api/cart/' + cart + '/';
    }
    if (body) {
        body = JSON.stringify(body);
    }

    console.log(method, url, body);
    let request = new XMLHttpRequest();
    request.open(method, url, false);
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('X-CSRFToken', token);
    request.send(body);
    console.log(request.response);
    amount = new_amount;
}
