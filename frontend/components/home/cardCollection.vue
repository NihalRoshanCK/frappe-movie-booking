<template>
    <div class="card-collection">
      <button class="scroll-button left " @click="scrollLeft" v-show="showLeftButton"><span class="material-symbols-outlined">
        navigate_before
        </span></button>
      <div class="cards-wrapper">
        <div class="card" v-for="(movie) in visibleMovies" :key="movie.id">
          <img class="rounded" :src="movie.posterUrl" alt="Movie Poster" />
          <div class="movie-details">
            <h3 class="title text">{{ movie.title }}</h3>
            <p class="genre">{{ movie.genre }}</p>
          </div>
        </div>
      </div>
      <button class="scroll-button right  " @click="scrollRight" v-show="showRightButton"><span class="material-symbols-outlined">
        navigate_next
        </span></button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        movies: [
            {
id: 1,
title: 'Manjinumel Boys1',
genre: 'Adventure/Drama/Thriller',
rating: '9.7/10',
votes: '7K',
posterUrl: 'https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:l-image,i-discovery-catalog@@icons@@star-icon-202203010609.png,lx-24,ly-615,w-29,l-end:l-text,ie-OS40LzEwICA3Ny40SyBWb3Rlcw%3D%3D,fs-29,co-FFFFFF,ly-612,lx-70,pa-8_0_0_0,l-end/et00386670-epsebvgzmv-portrait.jpg'
},
{
id: 2,
title: 'Manjinumel Boys2',
genre: 'Adventure/Drama/Thriller',
rating: '9.7/10',
votes: '7K',
posterUrl: 'https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:l-image,i-discovery-catalog@@icons@@star-icon-202203010609.png,lx-24,ly-615,w-29,l-end:l-text,ie-OS40LzEwICA3Ny40SyBWb3Rlcw%3D%3D,fs-29,co-FFFFFF,ly-612,lx-70,pa-8_0_0_0,l-end/et00386670-epsebvgzmv-portrait.jpg'
},
{
id: 3,
title: 'Manjinumel Boys3',
genre: 'Adventure/Drama/Thriller',
rating: '9.7/10',
votes: '7K',
posterUrl: 'https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:l-image,i-discovery-catalog@@icons@@star-icon-202203010609.png,lx-24,ly-615,w-29,l-end:l-text,ie-OS40LzEwICA3Ny40SyBWb3Rlcw%3D%3D,fs-29,co-FFFFFF,ly-612,lx-70,pa-8_0_0_0,l-end/et00386670-epsebvgzmv-portrait.jpg'
},
{
id: 4,
title: 'Manjinumel Boys4',
genre: 'Adventure/Drama/Thriller',
rating: '9.7/10',
votes: '7K',
posterUrl: 'https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:l-image,i-discovery-catalog@@icons@@star-icon-202203010609.png,lx-24,ly-615,w-29,l-end:l-text,ie-OS40LzEwICA3Ny40SyBWb3Rlcw%3D%3D,fs-29,co-FFFFFF,ly-612,lx-70,pa-8_0_0_0,l-end/et00386670-epsebvgzmv-portrait.jpg'
},
{
id: 5,
title: 'Manjinumel Boys5',
genre: 'Adventure/Drama/Thriller',
rating: '9.7/10',
votes: '7K',
posterUrl: 'https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:l-image,i-discovery-catalog@@icons@@star-icon-202203010609.png,lx-24,ly-615,w-29,l-end:l-text,ie-OS40LzEwICA3Ny40SyBWb3Rlcw%3D%3D,fs-29,co-FFFFFF,ly-612,lx-70,pa-8_0_0_0,l-end/et00386670-epsebvgzmv-portrait.jpg'
},   
{
id: 6,
title: 'Manjinumel Boys6',
genre: 'Adventure/Drama/Thriller',
rating: '9.7/10',
votes: '7K',
posterUrl: 'https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:l-image,i-discovery-catalog@@icons@@star-icon-202203010609.png,lx-24,ly-615,w-29,l-end:l-text,ie-OS40LzEwICA3Ny40SyBWb3Rlcw%3D%3D,fs-29,co-FFFFFF,ly-612,lx-70,pa-8_0_0_0,l-end/et00386670-epsebvgzmv-portrait.jpg'
}, 
{
id: 7,
title: 'Manjinumel Boys7',
genre: 'Adventure/Drama/Thriller',
rating: '9.7/10',
votes: '7K',
posterUrl: 'https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:l-image,i-discovery-catalog@@icons@@star-icon-202203010609.png,lx-24,ly-615,w-29,l-end:l-text,ie-OS40LzEwICA3Ny40SyBWb3Rlcw%3D%3D,fs-29,co-FFFFFF,ly-612,lx-70,pa-8_0_0_0,l-end/et00386670-epsebvgzmv-portrait.jpg'
},
{
id: 8,
title: 'Manjinumel Boys8',
genre: 'Adventure/Drama/Thriller',
rating: '9.7/10',
votes: '7K',
posterUrl: 'https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:l-image,i-discovery-catalog@@icons@@star-icon-202203010609.png,lx-24,ly-615,w-29,l-end:l-text,ie-OS40LzEwICA3Ny40SyBWb3Rlcw%3D%3D,fs-29,co-FFFFFF,ly-612,lx-70,pa-8_0_0_0,l-end/et00386670-epsebvgzmv-portrait.jpg'
},
{
id: 9,
title: 'Manjinumel Boys9',
genre: 'Adventure/Drama/Thriller',
rating: '9.7/10',
votes: '7K',
posterUrl: 'https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:l-image,i-discovery-catalog@@icons@@star-icon-202203010609.png,lx-24,ly-615,w-29,l-end:l-text,ie-OS40LzEwICA3Ny40SyBWb3Rlcw%3D%3D,fs-29,co-FFFFFF,ly-612,lx-70,pa-8_0_0_0,l-end/et00386670-epsebvgzmv-portrait.jpg'
},
{
id: 10,
title: 'Manjinumel Boys10',
genre: 'Adventure/Drama/Thriller',
rating: '9.7/10',
votes: '7K',
posterUrl: 'https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC:w-400.0,h-660.0,cm-pad_resize,bg-000000,fo-top:l-image,i-discovery-catalog@@icons@@star-icon-202203010609.png,lx-24,ly-615,w-29,l-end:l-text,ie-OS40LzEwICA3Ny40SyBWb3Rlcw%3D%3D,fs-29,co-FFFFFF,ly-612,lx-70,pa-8_0_0_0,l-end/et00386670-epsebvgzmv-portrait.jpg'
},
        ],
        currentIndex: 0,
        cardsPerPage: 5
      };
    },
    computed: {
      visibleMovies() {
        const start = this.currentIndex;
        const end = start + this.cardsPerPage;
        return this.movies.slice(start, end);
      },
      showLeftButton() {
        return this.currentIndex > 0;
      },
      showRightButton() {
        return this.currentIndex + this.cardsPerPage < this.movies.length;
      }
    },
    methods: {
      scrollLeft() {
        this.currentIndex -= this.cardsPerPage;
      },
      scrollRight() {
        this.currentIndex += this.cardsPerPage;
      }
    }
  };
  </script>
  
  <style scoped>
  .card-collection {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.25rem;
  }
  
  .cards-wrapper {
    display: flex;
    flex-wrap: nowrap;
    gap: 2rem;
    overflow-x: hidden;
  }
  
  .card {

    width: 20rem;
  }
  
  .card img {
    max-width: 100%;
    height: auto;
  }
  
  .movie-details {
    margin-top: 0.75rem;
  }
  
  .scroll-button {
    display: flex;
    background-color: rgba(130, 138, 138, 0.838);
    border: none;
    position: absolute;
    height: 3rem;
    border-radius: 9999px;
    width: 3rem;
    font-size: 2rem;
    cursor: pointer;
    scroll-behavior: smooth;
    outline: none;
    justify-content: center;
    align-items: center;

  }
  .left{
    left: 15%;
  }
  .right{
    right: 15%;
  }
  .material-symbols-outlined{
    font-size: 30px;
    color: white;
  }
  .title{
    font-size: large;
    font-weight: bold;
  }
  .genre{
    font-weight: lighter;
    font-size: medium;
    margin-bottom: 10px;
  }
  </style>
  