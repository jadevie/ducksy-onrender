import { NavLink, useParams } from "react-router-dom";
import { useDispatch, useSelector } from 'react-redux';

import styles from "./ProductGrid.module.css";
import ProductGridItem from "./ProductGridItem/ProductGridItem";
import { getProductsByCategory } from "../../store/productsBySearch";
import { useEffect } from "react";
// import { clearProductDetails } from "../../store/productDetails";

export default function ProductGrid() {
    const dispatch = useDispatch();
    const { categoryName } = useParams();
    const productsAll = useSelector(state => Object.values(state.products));
    // either products by search and by category is selected
    const productsBySearch = useSelector(state => Object.values(state.productsBySearch));
    const products = productsBySearch.length ? productsBySearch : productsAll;

    useEffect(() => {
        if (categoryName) dispatch(getProductsByCategory(categoryName));
    }, [dispatch, categoryName])

    return (
        <div className={styles.ProductGridWrapper}>
            <div className={styles.ProductGrid}>
                {products.map((product, i) =>
                    <NavLink key={i} to={`/listing/${product.id}`} style={{ textDecoration: 'none' }}>
                        <ProductGridItem product={product} />
                    </NavLink>)
                }
            </div >
        </div>
    );
}
