const pokemonImg = document.getElementById('pokemon-image');
const guessInput = document.getElementById('guess-input');
const submitBtn = document.getElementById('submit-btn');
const nextBtn = document.getElementById('next-btn');

let pokemonName = '';
let tentativaFeita = false;

function getRandomId() {
    return Math.floor(Math.random() * 250) + 1;
}

async function carregarPokemon() {
    // Sorteia novo Pokémon
    const id = getRandomId();
    const imageUrl = `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${id}.png`;
    pokemonImg.src = imageUrl;
    pokemonImg.classList.remove('revealed');
    // Busca nome correto na API
    try {
        const resp = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`);
        const data = await resp.json();
        pokemonName = data.name;
    } catch (e) {
        pokemonName = '';
        alert('Erro ao carregar Pokémon. Tente novamente.');
    }
    // Reset UI
    guessInput.value = '';
    guessInput.disabled = false;
    submitBtn.disabled = false;
    nextBtn.disabled = true;
    tentativaFeita = false;
}

submitBtn.addEventListener('click', () => {
    if (tentativaFeita) return;
    const resposta = guessInput.value.trim().toLowerCase();
    if (!resposta) return;
    // Desabilita campos após tentativa
    guessInput.disabled = true;
    submitBtn.disabled = true;
    nextBtn.disabled = false;
    tentativaFeita = true;
    // Revela se acertou
    if (resposta === pokemonName.toLowerCase()) {
        pokemonImg.classList.add('revealed');
    }
});

nextBtn.addEventListener('click', () => {
    if (!tentativaFeita) return;
    carregarPokemon();
});

// Permite enviar com Enter
guessInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !submitBtn.disabled) {
        submitBtn.click();
    }
});

// Inicializa o jogo
carregarPokemon();