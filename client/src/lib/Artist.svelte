<script lang="ts">
    // export let artist_uri
    export let name
    export let image
    export let num_followers
    export let genres

    let formatted_num_followers = num_followers.toLocaleString("en-US")

    let genres_string
    if (genres.length !== 0) {
        genres_string = genres.join(', ')
    } else {
        genres_string = 'n/a'
    }
    
</script>

<!-- TODO: Make card clickable and open specific artist on Spotify -->
<main class="card">
    <div class="img-container">
        <img src={image} alt=""/>
    </div>
    <div class="card-info-layout">
        <div class="card-info">
            <div class="name">{name}</div>
            <div class="card-subtext"><span class="tag">Followers:</span> {formatted_num_followers}</div>
            <div class="card-subtext"><span class="tag">Genres:</span> {genres_string}</div>
        </div>
        <span>
            <svg on:click={/* TODO: Remove artist from radar*/ null} 
                xmlns="http://www.w3.org/2000/svg" 
                class="icon icon-tabler icon-tabler-x" 
                width="32" height="32" viewBox="0 0 24 24" 
                stroke-width="0.75" stroke="#ffffff" fill="none" 
                stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                <line x1="18" y1="6" x2="6" y2="18" />
                <line x1="6" y1="6" x2="18" y2="18" />
            </svg>
        </span>
    </div>
</main>

<style>
    .card img {
        border-radius: 100%;
    }
    .card-subtext {
        font-size: 0.8em;
    }
    .icon-tabler-x {
        visibility: hidden;
        transition: stroke 0.25s;
    }
    .icon-tabler-x:hover {
        stroke: #f74848;
        cursor: pointer;
    }
    .icon-tabler-x:active {
        stroke: #c65d5d;
    }
    .card:hover .icon-tabler-x {
        visibility: visible;
    }
</style>