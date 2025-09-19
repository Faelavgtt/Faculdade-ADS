import cardProduto from "./cardComponent.js";


const container = document.getElementById("cardapio");

let itensProduto = [
  {
    image: "../image/caipirinha.jpg",
    altImage: "caipirinha 22,90",
    preco: "R$ 22,90",
    titulo: "Caipirinha da Casa",
    descricao: "Feita com limão siciliano, vodka ou velho barreiro e açúcar pra adoçar sua vida",
  },
  {
    image: "../image/drink.jpg",
    altImage: "Whisky do ahmed",
    preco: "R$ 29,90",
    titulo: "Whisky do ahmed",
    descricao: "sla",
  },
  {
    image: "../image/eduarda.png",
    altImage: "Paraiso-Eduarda",
    preco: "R$ 39,90",
    titulo: "Paraiso Eduarda",
    descricao: "Inspirado na crush do Raphao uma bebida quente e saborosa",
  },
  {
    image: "../image/paraiso.png",
    altImage: "Paraiso",
    preco: "R$ 39,90",
    titulo: "Paraiso Tradicional",
    descricao: "sla",
  },
];

itensProduto.map((produto) => {
  const cardHTML = cardProduto(produto);

  const temp = document.createElement("div");
  temp.innerHTML = cardHTML;
  const card = temp.firstElementChild;

  container.appendChild(card);
});
