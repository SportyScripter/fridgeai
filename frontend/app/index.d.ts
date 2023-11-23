export interface Product {
    id: number;
    name: string;
    quantity: number;
    unit: string;
}

export interface ListOfProductsProps { 
    items: Product[];
}
