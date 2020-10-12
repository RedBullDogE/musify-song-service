import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        playlist: {},
        currentSong: {
            isPlaying: false,
            currentTime: 0,
            artist: null,
            name: null,
            src: null,
        },
        player: new Audio(),
    },
    mutations: {
        play(state) {
            state.currentSong.isPlaying = true
        },
        pause(state) {
            state.currentSong.isPlaying = false
        },
        changeVolume(state, volume) {
            state.player.volume = volume
        },
        slideSong(state, newTime) {
            state.player.currentTime = newTime
        },
        hidePlayer(state) {
            state.currentSong.isPlaying = false
            state.currentSong.currentTime = 0

            state.currentSong.artist = null
            state.currentSong.name = null
            state.currentSong.src = null

            state.player = new Audio()
        },
        setSong(state, song) {
            state.currentSong.name = song.name
            state.currentSong.artist = song.artist
            state.currentSong.src = song.src

            state.currentSong.currentTime = 0
            state.player.src = song.src
        }
    },
    actions: {
        async play({ commit, state, dispatch }, song) {
            if (typeof song !== 'undefined') {
                commit('setSong', song)

                state.player.addEventListener("timeupdate", () => {
                    state.currentSong.currentTime = state.player.currentTime;
                });

                state.player.addEventListener("ended", () => {
                    dispatch('pause');
                });
            }

            try {
                await state.player.play()
                commit('play')
            } catch (error) {
                console.log(`DEBUG: there is some problem in store: play()\n payload:`)
                console.log(song);
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
            if (state.currentSong.isPlaying) {
                dispatch('pause')
            }

            commit('hidePlayer')
        }
    }
})