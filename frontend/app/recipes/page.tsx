"use client";
import Table from "@/components/Table";
import { Recipe } from "@/index";
import { useEffect, useState } from "react";
import RecipeDetailsDialog from "./RecipeDetails";

export default function Recipes() {
  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [recipe, setRecipe] = useState<Recipe | null>(null);

  const columns = [{ id: "name", label: "Nazwa" }];

  const fetchRecipes = () => {
    fetch("http://localhost:8008/recipes")
      .then((data) => data.json())
      .then(setRecipes);
  };

  useEffect(() => {
    fetchRecipes();
  }, []);

  const handleDelete = (id: number) => {
    fetch("http://localhost:8008/recipe/delete/" + id, { method: "DELETE" })
      .then((res) => res.json())
      .then(fetchRecipes);
  };

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
        </div>
        <Table
          columns={columns}
          rows={recipes}
          handleDelete={handleDelete}
          handlePreview={(r: Recipe) => setRecipe(r)}
        />

        {recipe && (
          <RecipeDetailsDialog
            open={true}
            handleClose={() => setRecipe(null)}
            recipe={recipe}
          />
        )}
      </div>
    </div>
  );
}
