'use client';
import ListOfProducts from "@/components/ListOfProducts";
import { Product } from "@/index";
import { useEffect, useState } from "react";

export default function Products() {
  const [items, setItems] = useState<Product[]>([]);

  useEffect(() => {
    fetch('http://localhost:8008/products')
    .then((response) => response.json())
    .then(setItems)
    .catch(console.error);
  }, []);

  return (
    <>
    {items.length === 0 && <div>Brak produktów</div>}
    {items.length > 0 && <ListOfProducts items={items} />}
    </>
  )
}
