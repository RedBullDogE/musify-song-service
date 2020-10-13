<template>
    <div class="album-page" v-if="album">
        <div class="album-info">
            <div class="album-info__picture">
                <img :src="album.cover" alt="album Picture" draggable="false" />
            </div>
            <h2 class="album-info__title">{{ album.name }}</h2>

            <div class="album-info__details">
                <p class="album-info__desc">{{ album.description }}</p>
                <p>Number of tracks: {{ album.songs.length }}</p>
                <p>Release year: {{ album.pub_year }}</p>
            </div>
        </div>

        <div class="album-content">
            <section class="top-songs">
                <h3 class="subtitle">Song List</h3>
                <Song
                    v-for="song in album.songs"
                    :key="song.id"
                    :song="song"
                    @setPlaylist="$store.dispatch('setPlaylist', album.songs)"
                />
            </section>
        </div>
    </div>
    <p class="text-center" v-else>Album is not found! Please, try again</p>
</template>

<script>
import Song from "../../components/cards/Song";

export default {
    data() {
        return {
            album: null,
            notFound: false,
        };
    },
    components: {
        Song,
    },
    async created() {
        let albumID = this.$route.params.albumId;
        let response = await fetch(
            `http://127.0.0.1:8000/api/albums/${albumID}`
        );
        if (response.status === 404) {
            this.notFound = true;
        } else {
            this.album = await response.json();
        }
    },
};
</script>

<style lang="scss">
@import "../../../src/assets/style/variables";

.album-page {
    .album-info {
        background-color: $color-purple-dark;
        color: #d3d3d3; // TODO:
        box-shadow: 0 1rem 3rem rgba($color-black, 0.4);
        border-radius: 1rem 0;
        padding: 3rem;

        max-width: fit-content;

        display: grid;
        grid-template-columns: max-content max-content;
        grid-template-rows: max-content;
        grid-column-gap: 4rem;
        grid-row-gap: 1rem;

        &__title {
            text-transform: uppercase;
            font-size: 4rem;
            max-width: 60rem;
            word-wrap: break-word;
        }

        &__picture {
            height: 15rem;
            width: 15rem;
            border-radius: 2rem;
            overflow: hidden;

            grid-row: 1 / 3;
            grid-column: 1 / 2;
            position: relative;

            img {
                height: 100%;
                margin-left: 50%;
                position: absolute;
                top: 0;
                left: 0;
                transform: translateX(-50%);
            }
        }

        &__details {
            grid-row: 2 / 3;
            grid-column: 2 / 4;
            max-width: 50rem;
            &__desc {
                font-size: 1.5rem;
                line-height: 2.2rem;
            }
        }

        .followed-btn {
            align-self: center;
            justify-self: start;

            &:hover ion-icon {
                color: lightgreen;
            }

            ion-icon {
                height: 3.5rem;
                width: 3.5rem;
                transition: color 0.2s;
            }
        }
    }

    .album-content {
        max-width: 94rem;

        & > section {
            margin: 3rem;
            padding: 2rem;
        }

        .top-songs {
            border-bottom: 1px solid gray;
        }

        .subtitle {
            text-transform: uppercase;
            font-size: 2.6rem;
        }

        .album-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(20rem, 1fr));
            grid-template-rows: 1fr 1fr;
        }
    }
}
</style>