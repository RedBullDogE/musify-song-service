import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        currentSong: {
            name: '',
            artist: '',
            src: '',
        },
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
        play({ commit, state }, payload) {
            if (typeof payload !== 'undefined') {
                state.currentSong.name = payload.name;
                state.currentSong.artist = payload.artist;
                state.currentSong.src = payload.song_file;

                state.player.src = payload.song_file;
            }

            state.player.play()
            commit('play')
        },
        pause({ commit, state }) {
            state.player.pause()

            commit('pause')
        }
    }
})