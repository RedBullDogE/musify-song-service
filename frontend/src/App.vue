<template>
    <div id="app">
        <Sidebar />
        <main class="main-container">
            <router-view />
        </main>
        <MusicPlayer />
    </div>
</template>

<script>
import Sidebar from "./components/layout/Sidebar";
import MusicPlayer from "./components/layout/MusicPlayer";

export default {
    components: {
        Sidebar,
        MusicPlayer
    },
};
</script>

<style lang="scss">
@import "./assets/style/variables";

*,
*::before,
*::after {
    margin: 0;
    padding: 0;
    box-sizing: inherit;
}

html {
    box-sizing: border-box;
    font-size: 62.5%;
}

body {
    font-size: 1.6rem;
    font-family: $font-primary;
}

#app {
    display: grid;
    grid-template-columns: minmax(25rem, 1fr) 5fr;
    min-height: 100vh;

    background-color: $color-purple-light-1;
}

.main-container {
    padding: 3rem 5rem;
}
</style>
