'use client';
import ProductsList from "@/components/ProductsList";
import { useEffect, useState } from "react";

export interface Product {
  id: string;
  name: string;
  price: number;
  description: string;
}

export default function Products() {
  // 1. pobranie
  // 2. przechowanie
  const [items, setItems] = useState<Product[]>([]);

  useEffect(() => {
    fetch('http://localhost:8008/products')
    .then((response) => {
      return response.json();
    }).then((data) => {
      setItems(data);
    }
    ).catch((error) => {
      console.log(error);
    });
  }, []);

  // const myItems = [{
  //     id: '1',
  //     name: 'Produkt 1',
  //     price: 123,
  //     description: 'Opis produktu 1',
    
  //   }];
  // 3. wyświetlenie (jezeli są)
  // 4. wyświetlenie (jezeli nie ma)
  return (
    <>

    {items.length === 0 && <div>Brak produktów</div>}
    {items.length > 0 && <ProductsList items={items} />}

    <button onClick={() => {
      setItems([...items, {
        id: '1',
        name: 'Produkt 1',
        price: 123,
        description: 'Opis produktu 1',
      }])
    }}>Dodaj</button>
    </>
  )
}
