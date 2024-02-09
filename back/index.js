import express from "express";
import { Sequelize, DataTypes } from "sequelize";
import cors from "cors";
import "http-status";
import httpStatus from "http-status";
import { config } from "dotenv";

config();

const sequelize = new Sequelize(
  `postgres://${process.env.POSTGRES_USER}:${process.env.POSTGRES_PASSWORD}@${process.env.POSTGRES_HOST}:5432/${process.env.POSTGRES_DB}`,
  {
    host: process.env.POSTGRES_HOST,
    dialect: "postgres",
  }
);

try {
  await sequelize.authenticate();
  console.log("Connection has been established successfully.");
} catch (error) {
  console.error("Unable to connect to the database:", error);
}

const Recipe = sequelize.define("recipe", {
  name: {
    type: DataTypes.TEXT,
    allowNull: false,
  },
});

await Recipe.sync();

const app = express();
const port = 3000;

app.use(cors({ origin: "http://localhost:5173" }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get("/api/recipes", async (req, res) => {
  const recipes = await Recipe.findAll({
    attributes: ["id", "name"],
    order: [["name", "ASC"]],
  });

  res.status(httpStatus.OK).send(recipes);
});

app.post("/api/recipes", async (req, res) => {
  try {
    const recipe = await Recipe.create({ name: req.body.name });
    await recipe.save();
    res.sendStatus(httpStatus.CREATED);
  } catch (error) {
    console.error("Error saving new recipe", error);
    res.sendStatus(httpStatus.INTERNAL_SERVER_ERROR);
  }
});

app.put("/api/recipes/:id", async (req, res) => {
  await Recipe.update(
    { name: req.body.name },
    {
      where: {
        id: req.params.id,
      },
    }
  );
});

app.delete("/api/recipes/:id", async (req, res) => {
  await Recipe.destroy({
    where: {
      id: req.params.id,
    },
  });

  res.sendStatus(httpStatus.NO_CONTENT);
});

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
