<script lang="ts">
    import Loader from "./Loader.svelte";
    import Track from "./Track.svelte";
    import { onMount } from "svelte";

    let radar_playlist
    let loaded = false

    onMount(async() => {
        await getRadarPlaylist()
    })

    async function getRadarPlaylist() {
        let response = await fetch('./radar_playlist_tracks', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })

        let result = await response.json()
        radar_playlist = result.radar_playlist
        loaded = true
    }

    function open_url(url) {
        window.open(url, '_blank')
    }
</script>

<main class="col-group">
    <div class="heading">
        Newest Releases
        <div class="actions">
            <svg xmlns="http://www.w3.org/2000/svg" 
                class="icon icon-tabler icon-tabler-refresh" 
                width="24" height="24" viewBox="0 0 24 24" 
                stroke-width="1.5" stroke="#ffffff" fill="none" 
                stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                <path d="M20 11a8.1 8.1 0 0 0 -15.5 -2m-.5 -4v4h4" />
                <path d="M4 13a8.1 8.1 0 0 0 15.5 2m.5 4v-4h-4" />
            </svg>
            <button on:click={() => open_url(radar_playlist.url)}>
                <svg xmlns="http://www.w3.org/2000/svg" 
                    class="icon icon-tabler icon-tabler-brand-spotify" 
                    width="24" height="24" viewBox="0 0 24 24" 
                    stroke-width="1.5" stroke="#191414" fill="none" 
                    stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                    <circle cx="12" cy="12" r="9" />
                    <path d="M8 11.973c2.5 -1.473 5.5 -.973 7.5 .527" />
                    <path d="M9 15c1.5 -1 4 -1 5 .5" />
                    <path d="M7 9c2 -1 6 -2 10 .5" />
                  </svg>
                  &nbsp;Spotify
            </button>
        </div>
    </div>
    <div class="col">
        {#if loaded}
            {#each radar_playlist.tracks as track}
                <Track 
                    url={track.url}
                    image={track.image}
                    name={track.name}
                    album={track.album}
                    album_url={track.album_url}
                    artists={track.artists}
                />
            {/each}
        {:else}
            <div class="center"><Loader/></div>
        {/if}
    </div>
</main>

<style>
    .icon-tabler-refresh {
        margin-right: .5em;
        transition: stroke 0.25s;
    }
    .icon-tabler-refresh:hover {
        stroke: #0bc84d;
        cursor: pointer;
    }
    .icon-tabler-refresh:active {
        stroke: #179b45;
    }
</style>