Create table products
(
    name     varchar(255) not null,
    quantity integer      not null,
    weight   float
);

alter table products
    owner to fridgeai_user;

INSERT INTO public.products (name, quantity, weight)
VALUES ('Milk', 1, 0.7);
INSERT INTO public.products (name, quantity, weight)
VALUES ('Bread', 2, 1);
INSERT INTO public.products (name, quantity, weight)
VALUES ('Chicken', 1, 0.5);
INSERT INTO public.products (name, quantity, weight)
VALUES ('Apple', 3, 0);
INSERT INTO public.products (name, quantity, weight)
VALUES ('Potato', 5, 0.15);
INSERT INTO public.products (name, quantity, weight)
VALUES ('Lollypop', 3, 0.1);
INSERT INTO public.products (name, quantity, weight)
VALUES ('Donut', 2, 0.1);
INSERT INTO public.products (name, quantity, weight)
VALUES ('Chees', 1, 0.2);