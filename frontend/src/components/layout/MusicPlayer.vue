<template>
    <transition name="show">
        <div class="player-container" v-show="isPlayerShown">
            <div class="player">
                <div class="progressbar-container">
                    <VueSlider
                        class="progressbar"
                        :disabled="!player.src"
                        :value="currentTime || 0"
                        @change="slideSong"
                        :min="0"
                        :max="Math.ceil(player.duration) || 100"
                        tooltip="none"
                        :processStyle="{ backgroundColor: '#df83f1' }"
                        :dotSize="10"
                    />
                    <div class="progressbar-time" v-if="player.src">
                        {{ player.currentTime || 0 | formatTime }} /
                        {{ player.duration || 0 | formatTime }}
                    </div>
                </div>

                <button class="close" @click="$store.dispatch('hidePlayer')">
                    &times;
                </button>

                <div class="player__info">
                    <h2 class="player__info__name">{{ currentSong.name }}</h2>
                    <p class="player__info__artist">{{ currentSong.artist }}</p>
                </div>

                <div class="player__control">
                    <button class="prev-btn">
                        <ion-icon name="play-skip-back"></ion-icon>
                    </button>
                    <button
                        class="play-btn"
                        v-if="!isPlaying"
                        @click="$store.dispatch('play')"
                    >
                        <ion-icon name="play"></ion-icon>
                    </button>
                    <button
                        class="pause-btn"
                        v-else
                        @click="$store.dispatch('pause')"
                    >
                        <ion-icon name="pause"></ion-icon>
                    </button>
                    <button class="next-btn">
                        <ion-icon name="play-skip-forward"></ion-icon>
                    </button>
                </div>

                <VueSlider
                    :value="player.volume * 100"
                    @change="changeVolume"
                    style="width: 10rem"
                    :processStyle="{ backgroundColor: '#df83f1' }"
                    :dotSize="12"
                />
            </div>
        </div>
    </transition>
</template>

<script>
import { mapState } from "vuex";
import VueSlider from "vue-slider-component";
import "vue-slider-component/theme/default.css";

export default {
    data() {
        return {};
    },
    computed: {
        ...mapState([
            "currentSong",
            "isPlaying",
            "player",
            "currentTime",
            "isPlayerShown",
        ]),
    },
    components: {
        VueSlider,
    },
    methods: {
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
        padding: 2rem 4rem 1.5rem 4rem;
        max-width: 80rem;
        border-radius: 2rem 2rem 0 0;

        background-color: rgba($color-purple-dark, 0.95);
        box-shadow: 0 0 3rem rgba($color-black, 0.3);
        color: #d3d3d3;

        display: grid;
        grid-template-columns: 1fr max-content 1fr min-content;
        align-items: center;
        grid-row-gap: 1.5rem;
        grid-column-gap: 1rem;

        .progressbar-container {
            grid-column: 1 / span 3;

            display: flex;
            width: 100%;

            .progressbar {
                flex-basis: auto;
                flex-grow: 1;

                .k-progress-outer {
                    padding: 0;
                }
            }

            .progressbar-time {
                margin-left: 3rem;
            }

            .vue-slider {
                cursor: pointer;

                .vue-slider-dot-handle {
                    opacity: 0;
                    transition: opacity 0.2s;
                }

                &:hover .vue-slider-dot-handle {
                    opacity: 1;
                }
            }
        }

        &__info {
            overflow: hidden;
            white-space: nowrap;
            text-overflow: ellipsis;

            &__name {
                display: inline;
            }
        }

        .vue-slider {
            justify-self: end;
        }

        &__control {
            grid-column: 2 / 3;
            grid-row: 2 / 3;

            display: flex;
            justify-content: center;
            align-items: center;

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

        .close {
            appearance: none;
            outline: none;
            border: none;
            background: none;
            
            font-size: 2rem;
            color: currentColor;

            transition: all .3s;

            cursor: pointer;

            &:hover {
                color: #999 ;
            }
        }
    }
}

.show-enter-active,
.show-leave-active {
    transition: all 0.5s ease-out;
}

.show-enter,
.show-leave-to {
    opacity: 0;
    transform: translateY(100%);
}
</style>