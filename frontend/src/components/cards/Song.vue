<template>
    <div class="song" v-if="song">
        <button class="play" @click="playSong">
            <ion-icon name="play"></ion-icon>
        </button>
        <div>
            <p class="title">{{ song.name }}</p>
            <p class="album-title">{{ song.album }}</p>
        </div>
    </div>
</template>

<script>
export default {
    props: ["song"],
    methods: {
        playSong() {
            this.$store.dispatch('play', this.song)
        },
    },
};
</script>

<style scoped lang="scss">
@import "../../../src/assets/style/variables";

.song {
    margin: 1rem 0;
    padding: 1rem 3rem;

    border-radius: 1rem;
    background-color: $color-purple-dark;
    color: #d3d3d3;

    display: flex;
    align-items: center;

    .title {
        font-weight: 600;
    }

    .album-title {
        font-weight: 200;
    }

    .play {
        appearance: none;
        outline: none;
        border: none;
        background: none;

        cursor: pointer;
        margin-right: 2rem;

        ion-icon {
            transition: opacity 0.2s;
            color: #ccc;
            height: 3rem;
            width: 3rem;
        }

        &:active > * {
            opacity: 0.4;
        }
    }
}
</style>