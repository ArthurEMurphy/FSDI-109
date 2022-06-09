import "./App.css";
import Navbar from "./components/navbar";
import Footer from "./components/footer";
//import QuantityPicker from "./components/quantityPicker";
import Catalog from "./components/catalog";
import Home from './components/home';
import About from "./components/about";
import Cart from "./components/cart";
import Admin from "./components/admin";
import Todo from "./components/todo"



import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import GlobalStoreProvider from "./context/globalStoreProvider";

function App() {
  return (
    <div className="App">
      <GlobalStoreProvider>
        <BrowserRouter>
          <Navbar />

          <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/about' element={<About />} />
            <Route path='/catalog' element={<Catalog />} />
            <Route path='/cart' element={<Cart />} />
            <Route path="/admin" element={<Admin />} />
            <Route path="/todo" element={<Todo />} />
          </Routes>

          <Footer />
        </BrowserRouter>
      </GlobalStoreProvider>
    </div>
  );
};

export default App;
