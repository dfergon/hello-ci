import { greet } from "../src/index.js";

test("saludo vacío", () => {
  expect(greet("")).toBe("Hola!");
});

test("saludo con nombre", () => {
  expect(greet("Diego")).toBe("Hola, Diego!");
});
