<script lang="ts">
    import Playlist from './lib/Playlist.svelte';
    import Radar from './lib/Radar.svelte';
</script>
  
<main>
    <header>
        <h1>Spotify Artist Radar</h1>
        <!-- Next to profile add the user's profile pic -->
        <h2>Profile</h2>
    </header>
    <div class="content">
        <Radar/>
        <Playlist/>
    </div>
    <footer>
        <h3>Made with &#128154; by <a href="https://www.linkedin.com/in/alansun25/" target="_blank">Alan Sun</a></h3>
        <h3><a href="https://github.com/alansun25/spotify-artist-radar" target="_blank">View Source Code</a></h3>    
    </footer>
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