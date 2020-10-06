import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        currentSong: {},
        player: new Audio(),
        isPlaying: false,
        currentTime: 0,
        isPlayerShown: false
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
        },
        showPlayer(state) {
            state.isPlayerShown = true
        },
        hidePlayer(state) {
            state.isPlayerShown = false
            state.currentSong = {},
            state.player = new Audio()
            state.isPlaying = false
            state.currentTime = 0
        }
    },
    actions: {
        async play({ commit, state, dispatch }, payload) {
            if (typeof payload !== 'undefined') {
                state.currentSong = payload;
                state.currentTime = 0;

                state.player.src = payload.src;

                state.player.addEventListener("timeupdate", () => {
                    state.currentTime = state.player.currentTime;
                });

                state.player.addEventListener("ended", () => {
                    dispatch('pause');
                });

                commit('showPlayer');
            }

            try {
                await state.player.play()
                commit('play')
            } catch (error) {
                console.log(`DEBUG: there is some problem in store: play()\n payload:`)
                console.log(payload);
                console.error(error);
            }
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
        },
        hidePlayer({ commit, state, dispatch }) {
            if (state.isPlaying) {
                dispatch('pause')
            }

            commit('hidePlayer')
        }
    }
})