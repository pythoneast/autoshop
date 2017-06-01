/**
 * Created by pythoneast on 5/31/17.
 */

/* Корзина */
function checkCart() {
    // проверяю наличие корзины в localStorage
    if (localStorage.getItem('cart') != null) {
        var cart = JSON.parse(localStorage.getItem('cart'));
        var urlParams = '?' +
            Object.keys(cart)
                .map(function (x) {
                    return 'ids=' + x;
                })
                .join('&')
            ;

        $.ajax({
            url: '/items/' + urlParams,
            success: function (products) {
                if (products.length < 1) {
                    $('footer.jumbotron2').addClass('nujno');
                    return false;
                }
                renderCart(products, cart);
            }



        });
    }
}

function renderCart(products, cart) {
    var out = '';
    for (var i = 0; i < products.length; i++) {
        out += createDiv(products[i], cart);
    }
    $('#my-cart').html(out);
    if (products.length < 1) {
        $('#btn-checkout').hide();
        $('footer.jumbotron2').addClass('nujno');
    }  else {
        if (products.length == 1) {
            $('footer.jumbotron2').addClass('nujno');
            $('#btn-checkout').show();
            $('.plus').on('click', function () {
                var articul = $(this).attr('data-art');
                cart[articul] = cart[articul] + 1;
                saveCartToLS(cart); // сохраняю корзину в localStorage
                renderCart(products, cart);
            });
            $('.minus').on('click', function () {
                var articul = $(this).attr('data-art');
                if (cart[articul] > 1) {
                    cart[articul] = cart[articul] - 1;
                    saveCartToLS(cart); // сохраняю корзину в localStorage
                    renderCart(products, cart);
                }
            });
            $('.delete').on('click', function () {
                var articul = $(this).attr('data-art');
                delete cart[articul];
                products = products.filter(function (x) {
                    return x.id !== +articul;
                });
                saveCartToLS(cart); // сохраняю корзину в localStorage
                renderCart(products, cart);
            });
        }
        else {
            $('footer.jumbotron2').removeClass('nujno');
            $('#btn-checkout').show();
            $('.plus').on('click', function () {
                var articul = $(this).attr('data-art');
                cart[articul] = cart[articul] + 1;
                saveCartToLS(cart); // сохраняю корзину в localStorage
                renderCart(products, cart);
            });
            $('.minus').on('click', function () {
                var articul = $(this).attr('data-art');
                if (cart[articul] > 1) {
                    cart[articul] = cart[articul] - 1;
                    saveCartToLS(cart); // сохраняю корзину в localStorage
                    renderCart(products, cart);
                }
            });
            $('.delete').on('click', function () {
                var articul = $(this).attr('data-art');
                delete cart[articul];
                products = products.filter(function (x) {
                    return x.id !== +articul;
                });
                saveCartToLS(cart); // сохраняю корзину в localStorage
                renderCart(products, cart);
            });
        }
    }
}

function createDiv(product, cart) {
    var out = '';
    out = '<div class="container-fluid obertka">'
                +'<div class="row">'
                    +'<div class="col-sm-offset-2 col-sm-8" style="background: white; padding: 0px 40px 0 40px;">'
                        +'<div class="col-xs-12 col-sm-4">'
                            +'<img src="/media/'+ product.picture + '" style="margin-top: 20px; margin-bottom: 20px; max-height: 100px; width:auto"/>'
                        +'</div>'
                        +'<div class="col-xs-12 col-sm-4 opisanie" style="border: none">'
                        +'<p style="margin-top: 30px"><b>'+ product.title +'</b>'
                        +'</p>'
                        +'</div>'
                        +'<div class="col-xs-12 col-sm-4" style="text-align: center; margin-top: 48px; font-size: 20px;"><b>'
                            + product.price + ' ' + 'x' + ' ' + cart[product.id] + ' ' + '=' + ' ' + product.price*cart[product.id]
                            +'<br><button data-art="'+ product.id +'" style="margin-left: 20px; margin-right: 5px;" class="minus btn btn-info">-</button><b>'+ cart[product.id] +'</b><button data-art="'+ product.id +'" class="plus btn btn-info" style="margin-left: 5px">+</button>'
                            +'</b><button data-art="'+ product.id +'" class="btn btn-delete btn-danger delete" style="position: absolute; right: -30px; top: -40px ">x</button>'
                        +'</div>'
                    +'</div>'
                +'</div>'
            +'</div>';
    return out;
}

checkCart();

function saveCartToLS(cart) {
    localStorage.setItem('cart', JSON.stringify(cart));
}