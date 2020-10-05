import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        currentSong: {},
        player: new Audio(),
        isPlaying: false,
        curTime: 0
    },
    mutations: {
        play(state) {
            state.isPlaying = true
        },
        pause(state) {
            state.isPlaying = false
        },
        changeVolume(state, payload) {
            state.player.volume = payload
        },
        slideSong(state, payload) {
            state.player.currentTime = payload
        }
    },
    actions: {
        async play({ commit, state, dispatch }, payload) {
            if (typeof payload !== 'undefined') {
                state.currentSong = payload;

                state.player.src = payload.src;

                state.player.addEventListener("timeupdate", () => {
                    // state.curTime = (state.player.currentTime * 100) / state.player.duration;
                    state.curTime = state.player.currentTime;
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
        },
        changeVolume({ commit }, payload) {
            commit('changeVolume', payload)
        },
        slideSong({ commit }, payload) {
            commit('slideSong', payload)
        }
    }
})