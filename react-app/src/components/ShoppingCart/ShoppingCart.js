import { NavLink } from "react-router-dom";
import { useSelector, } from 'react-redux';
import CartSummary from "./CartSummary/CartSummary";
import './ShoppingCart.css'
import { CartList } from "./CartList/CartList";
import CartCheckout from "./CartCheckout/CartCheckout";

export default function ShoppingCart() {
    const user = useSelector(state => state.session.user)
    const products = useSelector(state => state.products)
    const carts = useSelector(state => state.shoppingCarts)

    if (!carts || !Object.keys(products).length) return;
    const current_cart = user ? carts[user.id] : carts["guest"]
    const cart_items = Object.entries(current_cart).filter(([product_id, amount]) => product_id in products);

    return (
        <div>
            {cart_items.length ?
                (<div className="cartWrapper">
                    <CartSummary cart_items={cart_items} />
                    <div className="cart_grid_container">
                        <CartList cart_items={cart_items} />
                        <CartCheckout cart_items={cart_items} user={user} />
                    </div>
                </div>)
                :
                (<div className="cartWrapper">
                    <h1>Your cart is empty</h1>
                    <NavLink to={'/'}>Discover something unique to fill it up</NavLink>
                </div>)
            }
        </div>
    )
}