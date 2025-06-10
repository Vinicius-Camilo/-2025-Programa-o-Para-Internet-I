const pokemonImg = document.getElementById('pokemon-image');

function getRandomId() {
    return Math.floor(Math.random() * 250) + 1;
}

function carregarPokemon() {
    const id = getRandomId();
    const imageUrl = `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${id}.png`;
    pokemonImg.src = imageUrl;
}

carregarPokemon();