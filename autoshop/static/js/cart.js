/**
 * Created by pythoneast on 5/31/17.
 */

/* Корзина */

function checkCart() {
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
                    return false;
                }

                var out='';
                for (var i = 0; i < products.length; i++ ){
                    out += createDiv(products[i], cart);
                }
                $('#my-cart').html(out);
                $('#btn-checkout').show();
            }
        });
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
                        +'<div class="col-xs-12 col-sm-4 opisanie" style="border: none"><p style="margin-top: 30px"><b>'+ product.title +'</b></p></div>'
                        +'<div class="col-xs-12 col-sm-4" style="text-align: center; margin-top: 48px; font-size: 20px;"><b>'
                            + product.price + ' ' + 'x' + ' ' + cart[product.id] + ' ' + '=' + ' ' + product.price*cart[product.id]
                            +'</b><button class="btn btn-delete btn-danger" style="position: absolute; right: -30px; top: -40px ">x</button>'
                        +'</div>'
                    +'</div>'
                +'</div>'
            +'</div>';
    return out;
}

checkCart();