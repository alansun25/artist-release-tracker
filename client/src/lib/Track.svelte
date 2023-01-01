<script lang="ts">
    export let url
    export let image
    export let name
    export let artists

    let num_artists = artists.length

    function open_url(url) {
        window.open(url, '_blank')
    }
</script>

<!-- TODO: Make card clickable and open specific song on Spotify -->
<main class="card">
    <div class="img-container">
        <img src={image} alt=""/>
    </div>
    <div class="card-info-layout">
        <div class="card-info">
            <a href={url} target="_blank"><div class="name">{name}</div></a>
            <div class="card-subtext">
                {#each artists as { url, name }, i}
                    <a class="tag" href={url} target="_blank">{name}</a>{#if i < num_artists - 1}
                        <span class="tag">,&nbsp;</span>
                    {/if}
                {/each}
            </div>
            
        </div>
    </div>
</main>

<style>
    .card:hover {
        cursor: auto;
    }
    .card-subtext {
        font-size: 1em;
    }
    a {
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    .name {
        color: #fff;
        transition: color 0.25s;
    }
    .name:hover {
        cursor: pointer;
        text-decoration: underline;
        color: rgb(172, 172, 172)
    }
</style>