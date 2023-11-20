import { Product } from "@/app/products/page";

interface ProductsListProps {
    items: Product[];
}

export default function ProductsList({items}: ProductsListProps) {
    return <table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Nazwa</th>
      <th>Cena</th>
      <th>Opis</th>
    </tr>
  </thead>
  <tbody>
    {items.map((item, key) => <tr key={key}>
      <td>{item.id}</td>
      <td>{item.name}</td>
      <td>{item.price}</td>
      <td>{item.description}</td>
    </tr>)}
  </tbody>
</table>
}