<template>
    <div class="player-container">
        <div class="player">
            <div class="progressbar-container">
                <KProgress
                    v-if="currentSong"
                    :percent="percent || 0"
                    :show-text="false"
                    :color="'#df83f1'"
                    :flow-second="6"
                    class="progressbar"
                />
                <div class="progressbar-time" v-if="player.src">
                    {{ player.currentTime || 0 | formatTime }} /
                    {{ player.duration || 0 | formatTime }}
                </div>
            </div>

            <div class="player__info">
                <h2 class="song-name">{{ currentSong.name }}</h2>
                <p class="song-artist">{{ currentSong.artist }}</p>
            </div>

            <div class="player__control">
                <button class="prev-btn">
                    <ion-icon name="play-skip-back"></ion-icon>
                </button>
                <button class="play-btn" v-if="!isPlaying" @click="play">
                    <ion-icon name="play"></ion-icon>
                </button>
                <button class="pause-btn" v-else @click="pause">
                    <ion-icon name="pause"></ion-icon>
                </button>
                <button class="next-btn">
                    <ion-icon name="play-skip-forward"></ion-icon>
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";

export default {
    data() {
        return {};
    },
    computed: {
        ...mapState({
            currentSong: "currentSong",
            isPlaying: "isPlaying",
        }),
    },
    methods: {
        play() {
            this.$store.dispatch("play");
        },
        pause() {
            this.$store.dispatch("pause");
        },
    },
};
</script>

<style lang="scss">
@import "../../assets/style/variables";

.player-container {
    position: fixed;
    bottom: 0;
    height: fit-content;
    width: 100%;

    .player {
        margin: 0 auto;
        padding: 2rem 6rem 1.5rem 6rem;
        max-width: 60rem;
        border-radius: 2rem 2rem 0 0;

        background-color: $color-purple-dark;
        box-shadow: 0 0 3rem rgba($color-black, 0.3);

        &__header {
            margin-right: auto;
        }

        &__control {
            display: flex;
            justify-content: center;

            button {
                appearance: none;
                outline: none;
                border: none;
                background: none;

                cursor: pointer;

                ion-icon {
                    transition: opacity 0.2s;
                    color: #ccc;
                }

                &:active > * {
                    opacity: 0.4;
                }
            }

            .prev-btn,
            .next-btn {
                margin: 0 2rem;
                ion-icon {
                    height: 3rem;
                    width: 3rem;
                }
            }

            .play-btn,
            .pause-btn {
                margin: 0 2rem;
                ion-icon {
                    height: 4rem;
                    width: 4rem;
                }
            }
        }
    }
}
</style>