Create TABLE models (
id SERIAL PRIMARY KEY,
name TEXT NOT NULL
);

Create TABLE datasets (
    id SERIAL PRIMARY KEY,
    filename TEXT NOT NULL
); 

Create TABLE experiments (
    id SERIAL PRIMARY KEY, 
    description TEXT NOT NULL
);