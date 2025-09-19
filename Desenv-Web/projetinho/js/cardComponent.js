const cardProduto = ({ image, altImage,preco, titulo, descricao }) =>{
    return`
        <div class="card">
            <img class="photoCard" src="${image}" alt="${altImage}">
            <h2>${titulo}</h2>
            <h3>${preco}</h3>
            <p>${descricao}</p>
        </div>
    
    `

}
export default cardProduto;