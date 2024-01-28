"use client";
import ProductCreateFormDialog from "@/app/products/CreateFormDialog";
import Spinner from "@/components/Spinner";
import Table from "@/components/Table";
import { Product, ProductData } from "@/index";
import { useEffect, useState } from "react";
import { toast } from "react-toastify";

export default function Products() {
  const [products, setProducts] = useState<Product[]>([]);
  const [isDialogOpen, setIsDialogOpen] = useState<boolean>(false);
  const [isRecipeGenerating, setIsRecipeGenerating] = useState<boolean>(false);
  const [input, setInput] = useState<ProductData>({
    name: "",
    quantity: 0,
    unit: "",
  });
  const columns = [
    { id: "name", label: "Nazwa" },
    { id: "quantity", label: "Ilość" },
    { id: "unit", label: "Jednostka" },
  ];

  const fetchProducts = () => {
    fetch("http://localhost:8008/products")
      .then((data) => data.json())
      .then(setProducts);
  };

  const handleClose = () => {
    setIsDialogOpen(false);
  };

  const handleSubmit = () => {
    fetch("http://localhost:8008/product/create", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(input),
    })
      .then((data) => data.json())
      .then(() => {
        handleClose();
        fetchProducts();
      });
  };
  useEffect(() => {
    fetchProducts();
  }, []);

  const handleDelete = (id: number) => {
    fetch("http://localhost:8008/product/delete/" + id, { method: "DELETE" })
      .then((res) => res.json())
      .then(fetchProducts);
  };

  const createRecipe = () => {
    setIsRecipeGenerating(true);
    fetch("http://localhost:8008/recipe/create", { method: "POST" })
      .then((res) => res.json())
      .then((res) => {
        console.log({ res });
        if (res.detail) {
          toast.error(res.detail);
        } else {
          toast.success("Przepis utworzony pomyślnie!");
        }
        setIsRecipeGenerating(false);
      });
  };

  return (
    <div className="w-full">
      <div className=" mx-auto my-8">
        <div className="flex justify-between items-center mb-12">
          <div>
            <h1 className="text-2xl font-semibold">Produkty</h1>
            <p className="text-sm text-gray-600">
              Tutaj znajduje się lista posiadanych przez Ciebie produktów.
            </p>
          </div>
          <div className="flex align-middle items-center">
            {/* {products.length > 2 ? ( */}
            <button
              disabled={isRecipeGenerating}
              onClick={createRecipe}
              className=" mr-3 inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 hover:bg-primary/90 h-10 px-4 py-2 border-2 border-indigo-600  text-indigo-600"
            >
              <div className="flex align-middle items-center">
                {isRecipeGenerating && <Spinner />}
                <span className="ml-2">Wygeneruj przepis</span>
              </div>
            </button>
            {/* ) : null} */}
            <button
              onClick={() => setIsDialogOpen(true)}
              className="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 hover:bg-primary/90 h-10 px-4 py-2 bg-indigo-600 text-white"
            >
              Dodaj
            </button>
          </div>
        </div>
        <Table columns={columns} rows={products} handleDelete={handleDelete} />

        <ProductCreateFormDialog
          open={isDialogOpen}
          handleSubmit={handleSubmit}
          handleClose={handleClose}
          input={input}
          setInput={setInput}
        />
      </div>
    </div>
  );
}
