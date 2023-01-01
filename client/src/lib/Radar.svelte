<script lang="ts">
    import Artist from "./Artist.svelte";
    import Loader from "./Loader.svelte";
    import { onMount } from "svelte";

    let loaded = false
    let tracked_artists = []

    onMount(async() => {
        // Fetch tracked artists
        await getTrackedArtists()

        // TODO: Fetch Radar playlist details
    })

    async function getTrackedArtists() {
        let response = await fetch('./tracked_artists', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })

        let result = await response.json()
        tracked_artists = result.artists
        loaded = true
    }
</script>

<main class="col-group">
    <div class="heading">
        Artist Radar
        <button on:click={/* TODO: Open artist search */ null}>
            <svg xmlns="http://www.w3.org/2000/svg" 
                class="icon icon-tabler icon-tabler-plus" 
                width="24" height="24" viewBox="0 0 24 24" 
                stroke-width="1.5" stroke="#191414" fill="none" 
                stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                <line x1="12" y1="5" x2="12" y2="19" />
                <line x1="5" y1="12" x2="19" y2="12" />
            </svg>
            &nbsp;Add Artists
        </button>
    </div>
    <div class="col">
        {#if loaded}
            {#each tracked_artists as artist}
                <Artist 
                    id={artist.id}
                    name={artist.name}
                    image={artist.image} 
                    num_followers={artist.num_followers}
                    genres={artist.genres}
                />
            {/each}
        {:else}
            <div class="center"><Loader/></div>
        {/if}
    </div>
</main>

<style>
    .center {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
