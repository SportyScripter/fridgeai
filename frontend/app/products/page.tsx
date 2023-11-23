'use client';
import { useEffect, useState } from "react";
import { Product } from "@/app/index";
import ListOfProducts from "@/components/ListOfProducts";

export default function Products() {
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
  return (
    <>
    {items.length === 0 && <div>Brak produktów</div>}
    {items.length > 0 && <ListOfProducts items={items} />}
    </>
  )
}
