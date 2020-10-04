<template>
    <div class="song" v-if="song">
        <button
            class="pause"
            @click="pauseSong"
            v-if="isCurrentSongInPlayer && isPlaying"
        >
            <ion-icon name="pause"></ion-icon>
        </button>
        <button class="play" @click="playSong" v-else>
            <ion-icon name="play"></ion-icon>
        </button>
        <div>
            <p class="title">{{ song.name }}</p>
            <p class="album-title">{{ song.album }}</p>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";

export default {
    props: ["song"],
    computed: {
        ...mapState(["currentSong", "isPlaying"]),
        isCurrentSongInPlayer() {
            return (
                this.currentSong.length === this.song.length &&
                this.currentSong.name === this.song.name &&
                this.currentSong.artist === this.song.artist &&
                this.currentSong.src === this.song.src
            );
        },
    },
    methods: {
        playSong() {
            if (this.isCurrentSongInPlayer) {
                this.$store.dispatch("play");
                return;
            }
            this.$store.dispatch("play", this.song);
        },
        pauseSong() {
            this.$store.dispatch("pause");
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

    .play,
    .pause {
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