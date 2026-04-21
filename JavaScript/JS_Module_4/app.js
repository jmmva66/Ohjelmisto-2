'use strict';

const searchForm = document.querySelector('#searchForm');
const resultsContainer = document.querySelector('#results');

searchForm.addEventListener('submit', async function(event) {
    event.preventDefault();

    const query = document.querySelector('#query').value;

    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
        const tvShows = await response.json();

        console.log(tvShows);

        resultsContainer.innerHTML = '';

        tvShows.forEach(tvShow => {
            const show = tvShow.show;

            const article = document.createElement('article');

            const name = show.name;
            const url = show.url;
            const image = show.image?.medium;
            const summary = show.summary;

            article.innerHTML = `
                <h2>${name}</h2>
                <a href="${url}" target="_blank">View Details</a>
                <br>
                ${image ? `<img src="${image}" alt="${name}">` : '<p>No image available</p>'}
                <div>${summary}</div>
            `;

            resultsContainer.appendChild(article);
        });

    } catch (error) {
        console.error("Something went wrong:", error);
    }
});