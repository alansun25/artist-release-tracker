<script lang="ts">
    import Playlist from './lib/Playlist.svelte';
    import Radar from './lib/Radar.svelte';
    import Search from './lib/Search.svelte';
    import { onMount } from 'svelte';

    let loggedIn = false
    // let me = ''
    // let playlists = []

    // onMount(async() => {
    //     await getUserPlaylists()
    //     await getUser()
    // })

    // async function getUser() {
    //   let response = await fetch('./user', {
    //     method: 'GET'
    //   })

    //   let result = await response;
    //   result.text().then(text => (me = text))
    // }

    // async function getUserPlaylists() {
    //     let response = await fetch('./playlists', {
    //         method: 'GET',
    //         headers: {
    //             'Content-Type': 'application/json'
    //         }
    //     })

    //     let result = await response.json()
    //     playlists = result.playlists.items
    // }
</script>
  
<main>
    <header>
        <h1>Spotify Artist Radar</h1>
        <h2>Settings</h2>
    </header>
    <div class="content">
        <Radar/>
        <Playlist/>
    </div>
    <footer>
        <h3>Made with &#128154; by <a href="https://www.linkedin.com/in/alansun25/" target="_blank">Alan Sun</a></h3>
        <h3><a href="https://github.com/alansun25/spotify-artist-radar" target="_blank">View Source Code</a></h3>
    </footer>
    <!-- <div class="card">
        <p>test</p>
        <p>User ID: {me}</p>
    </div>

    <div>
        <h2>List of playlist names</h2>
        <ul>
            {#each playlists as playlist}
            <li>{playlist.name}</li>
            {/each}
        </ul>
    </div> -->
</main>
  
<style>
    main {
        display: flex;
        flex-flow: column;
        height: 100%;
    }
    h2 {
        transition: color 0.25s;
    }
    h2:hover {
        cursor: pointer;
        color: #0bc84d;
    }
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: absolute;
        left: 0;
        right: 0;
        height: fit-content;
        padding: 0 2em;
    }
    .content {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
    }
    footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
</style>