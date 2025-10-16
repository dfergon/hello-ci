export function greet(name) {
  const n = (name || "").trim();
  return n ? `Hola, ${n}!` : "Hola!";
}
