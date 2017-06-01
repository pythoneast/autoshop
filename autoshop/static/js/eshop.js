/**
 * Created by pythoneast on 5/31/17.
 */

/* Наша корзина */

var cart = {};

$('document').ready(function () {
    addOnClick();
    checkCart();
    showMiniCart();
});

function addOnClick() {
    $('button.add-to-cart').on('click', addToCart);
}

/* Добавляем товар в корзину */

function addToCart() {
    var articul = $(this).attr('data-art');
    if (cart[articul] != undefined) {
        cart[articul] = cart[articul] + 1;
    }
    else {
        cart[articul] = 1;
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    console.log(cart);
    showMiniCart();
}

/* проверяю наличие корзины в localStorage */

function checkCart() {
    if (localStorage.getItem('cart') != null) {
        cart = JSON.parse(localStorage.getItem('cart'));
    }
}

/* Показываем содержимое корзины */

// function showMiniCart() {
//     var out = '';
//     for (var i in cart) {
//         out += i + ' --- ' + cart[i] + '<br>';
//     }
//     $('#mini-cart').html(out);
// }