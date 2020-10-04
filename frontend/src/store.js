import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        currentSong: {},
        player: new Audio(),
        isPlaying: false
    },
    mutations: {
        play(state) {
            state.isPlaying = true
        },
        pause(state) {
            state.isPlaying = false
        }
    },
    actions: {
        async play({ commit, state, dispatch }, payload) {
            if (typeof payload !== 'undefined') {
                state.currentSong = payload;

                state.player.src = payload.src;

                state.player.addEventListener("timeupdate", () => {
                    state.percent = (state.player.currentTime * 100) / state.player.duration;
                });

                state.player.addEventListener("ended", () => {
                    dispatch('pause');
                });

            }

            try {
                await state.player.play()
            } catch (error) {
                console.log(`DEBUG: there is some problem in store: play()\n payload:`)
                console.log(payload);
                console.error(error);
            }

            commit('play')
        },
        pause({ commit, state }) {
            state.player.pause()

            commit('pause')
        }
    }
})