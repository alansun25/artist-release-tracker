<script lang="ts">
    import Playlist from './lib/Playlist.svelte';
    import Radar from './lib/Radar.svelte';
    import { onMount } from 'svelte';

    let user = null

    onMount(async() => {
        await getUser()
    })

    async function getUser() {
      let response = await fetch('./user', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
      })

      user = await response.json();
    }
</script>
  
<main>
    <div class="web">
        <header>
            <h1>Spotify Artist Radar</h1>
            <!-- Next to profile add the user's profile pic -->
            <div class="profile-tab">
                {#if user}
                    <img src={user.image} alt=""/>
                    <span><h2>{user.name}</h2></span>
                {/if}
            </div>
        </header>
        <div class="content">
            <Radar/>
            <Playlist/>
        </div>
        <footer>
            <h3>Made with &#128154; by <a href="https://www.linkedin.com/in/alansun25/" target="_blank">Alan Sun</a></h3>
            <h3><a href="https://github.com/alansun25/spotify-artist-radar" target="_blank">View Source Code</a></h3>    
        </footer>
    </div>

    <!-- TODO: Make app responsive -->
    <div class="mobile">
        <span>This app currently only works on larger screens.</span>    
        <span>Apologies for the inconvenience.</span>
    </div>
</main>
  
<style>
    main {
        display: flex;
        flex-flow: column;
        height: 100%;
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
    .profile-tab {
        display: flex;
        align-items: center;
        transition: color 0.25s;
    }
    .profile-tab:hover {
        cursor: pointer;
        color: #0bc84d;
    }
    .profile-tab img {
        height: 22px;
        width: 22px;
        margin-right: 0.5em;
        border-radius: 100%;
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
        justify-content: space-between;
        align-items: center;
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: fit-content;
        padding: 0 2em;
    }
</style>