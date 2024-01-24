"use client";
import { Recipe } from "@/index";
import { useEffect, useState } from "react";
import Table from "../components/Table";

export default function Recipes() {
  const [recipes, setRecipes] = useState<Recipe[]>([]);

  const columns = [{ id: "name", label: "Nazwa" }];

  useEffect(() => {
    fetch("http://localhost:8008/recipes")
      .then((data) => data.json())
      .then(setRecipes);
  }, []);

  return (
    <div className="w-full">
      <div className=" mx-auto my-8">
        <div className="flex justify-between items-center mb-12">
          <div>
            <h1 className="text-2xl font-semibold">Przepisy</h1>
            <p className="text-sm text-gray-600">
              Tutaj znajduje się lista wygenerowanych przez Ciebie przepisów.
            </p>
          </div>
          {/* <button className="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 hover:bg-primary/90 h-10 px-4 py-2 bg-indigo-600 text-white">
            + Dodaj
          </button> */}
        </div>
        <Table columns={columns} rows={recipes} handleDelete={() => {}} />
      </div>
    </div>
  );
}
