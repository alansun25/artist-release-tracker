<script lang="ts">
    export let url
    export let image
    export let name
    export let album
    export let album_url
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
            <div class="card-subtext"><a class="tag" href={album_url} target="_blank">{album}</a></div>
        </div>
    </div>
</main>

<style>
    img {
        border-radius: 8px;
    }
    .card:hover {
        cursor: auto;
    }
    a {
        text-decoration: none;
    }
    .name {
        color: #fff;
        transition: color 0.25s;
    }
    .name:hover {
        cursor: pointer;
        color: #0bc84d;
    }
</style>