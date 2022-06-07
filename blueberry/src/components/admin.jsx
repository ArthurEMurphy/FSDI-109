import "./admin.css";
import { useState } from "react";

const Admin = () => {
  const [product, setProduct] = useState({});
  const [coupon, setCoupon] = useState({});
  const [allCoupons, setAllCoupons] = useState([]);
  const [allProducts, setAllProducts] = useSatet([]);

  const saveProduct = () => {
    console.log("Saving Product", product);

    let copy = [...allProducts];
    copy.push(product);
    setAllProducts(copy);
  };

  const textChanged = (e) => {
    let name = e.target.name;
    let val = e.target.value;

    let copy = { ...product };
    copy[name] = val;
    setProduct(copy);

  }

     //TODO: send the product to
  };

  const saveCoupon = () => {
    console.log("Saving Coupon", coupon);
  };

  const couponChanged = (e) => {
    let name = e.target.name;
    let val = e.target.value;

    let copy = { ...coupon };
    copy[name] = val;
    setCoupon(copy);

    // add the coupon to the allCoupons array
  };

  return (
    <div className="admin-page">
      <h4>Store Administration</h4>

      <div className="content">
        <section className="products">
          <h5>Register a new product</h5>

          <div className="field">
            <label>Title</label>
            <input
              name="title"
              onChange={textChanged}
              className="form-control"
              type="text"
            />
          </div>

          <div className="field">
            <label>Category</label>
            <input
              name="category"
              onChange={textChanged}
              className="form-control"
              type="text"
            />
          </div>

          <div className="field">
            <label>Image</label>
            <input
              name="image"
              onChange={textChanged}
              className="form-control"
              type="text"
              placeholder="image name"
            />
          </div>

          <div className="field">
            <label>Price</label>
            <input
              name="price"
              onChange={textChanged}
              className="form-control"
              type="number"
            />
          </div>

          <div className="field">
            <button onClick={saveProduct} className="btn btn-primary">
              Register Product
            </button>
          </div>
          <div>
          <ul>
            {allProducts.map((p, index) => <li key={index}>{p.title} - {p.price}</li>)};
          </ul>
          </div>
        </section>
        <section className="coupons">
          <h5>Coupon Codes</h5>

          <div className="field">
            <label>Code: </label>
            <input
              name="code"
              onChange={couponChanged}
              className="form-control"
              type="text"
            />
          </div>

          <div className="field">
            <label>Discount: </label>
            <input
              name="discount"
              onChange={couponChanged}
              className="form-control"
              type="number"
            />
          </div>
          <div className="field">
            <button onClick={saveCoupon} className="btn btn-primary">
              Register Coupon
            </button>
          </div>

          <hr />
          <ul>
            {allCoupons.map((c) => (<li key={c.code}>{c.code} - {c.discount}</li>))};
          </ul>
        </section>
      </div>
    </div>
    );
  };

export default Admin;
