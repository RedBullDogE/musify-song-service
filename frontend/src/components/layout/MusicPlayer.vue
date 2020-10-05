<template>
    <div class="player-container">
        <div class="player">
            <div class="progressbar-container">
                <!-- <KProgress
                    v-if="currentSong"
                    :percent="percent || 0"
                    :show-text="false"
                    :color="'#df83f1'"
                    :flow-second="6"
                    class="progressbar"
                /> -->

                <VueSlider
                    class="progressbar"
                    :disabled="!player.src"
                    :value="curTime || 0"
                    @change="slideSong"
                    :min="0"
                    :max="parseInt(player.duration) || 100"
                    tooltip="none"
                    :processStyle="{ backgroundColor: '#df83f1' }"
                    :dotSize="10"
                    :dotStyle="{ opacity: 0 }"
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
                <VueSlider
                    :value="player.volume * 100"
                    @change="changeVolume"
                    style="width: 100px"
                    :processStyle="{ backgroundColor: '#df83f1' }"
                    :dotSize="12"
                />
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";
// import KProgress from "k-progress";
import VueSlider from "vue-slider-component";
import "vue-slider-component/theme/default.css";

export default {
    data() {
        return {};
    },
    computed: {
        ...mapState(["currentSong", "isPlaying", "player", "curTime"]),
    },
    components: {
        // KProgress,
        VueSlider,
    },
    methods: {
        play() {
            this.$store.dispatch("play");
        },
        pause() {
            this.$store.dispatch("pause");
        },
        changeVolume(value) {
            this.$store.dispatch("changeVolume", value / 100);
        },
        slideSong(value) {
            this.$store.dispatch("slideSong", value);
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
        color: #d3d3d3;

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

        .progressbar-container {
            width: 100%;
            display: flex;

            .progressbar {
                flex-basis: auto;
                flex-grow: 1;

                .k-progress-outer {
                    padding: 0;
                }
            }

            .progressbar-time {
                margin-left: 1rem;
            }
        }
    }
}
</style>