<template>
    <div v-if="!notFound">
        <div class="artist-home" v-if="artist">
            <div class="artist-info">
                <div class="artist-info__picture">
                    <img
                        :src="artist.picture"
                        alt="Artist Picture"
                        draggable="false"
                    />
                </div>
                <h2 class="artist-info__title">{{ artist.name }}</h2>

                <p class="artist-info__desc">{{ artist.description || "-" }}</p>
            </div>

            <div
                class="artist-content"
                v-if="artist.songs.length || artist.albums.length"
            >
                <section class="top-songs">
                    <h3 class="subtitle">Top Songs</h3>
                    <Song
                        v-for="song in artist.songs"
                        :key="song.id"
                        :song="song"
                        @setPlaylist="$store.dispatch('setPlaylist', artist.songs)"
                    />
                </section>

                <section class="albums">
                    <h3 class="subtitle">Albums</h3>

                    <div class="album-grid">
                        <AlbumCard
                            v-for="album in artist.albums"
                            :key="album.id"
                            :album="album"
                        />
                    </div>
                </section>
            </div>
            <p class="empty-artist-message" v-else>
                The artist has not released any song yet :( Or we just do not
                know about it! You can add songs _here_
            </p>
        </div>
    </div>
    <p v-else>Sorry, this artist is not found :(</p>
</template>

<script>
import Song from "../../components/cards/Song";
import AlbumCard from "../../components/cards/AlbumCard";

export default {
    components: {
        Song,
        AlbumCard,
    },
    data() {
        return {
            artist: null,
            notFound: false,
        };
    },
    async created() {
        let artistID = this.$route.params.id;
        let response = await fetch(
            `http://127.0.0.1:8000/api/artists/${artistID}`
        );
        if (response.status === 404) {
            this.notFound = true;
        } else {
            this.artist = await response.json();
        }
    },
};
</script>

<style lang="scss">
@import "../../../src/assets/style/variables";

.artist-home {
    .artist-info {
        background-color: $color-purple-dark;
        color: #d3d3d3; // TODO:
        box-shadow: 0 1rem 3rem rgba($color-black, 0.4);
        border-radius: 1rem 0;
        padding: 3rem;

        max-width: fit-content;

        display: grid;
        grid-template-columns: 1fr 3fr;
        grid-template-rows: max-content;
        grid-column-gap: 4rem;
        grid-row-gap: 1rem;

        &__title {
            text-transform: uppercase;
            font-size: 4rem;
        }

        &__picture {
            height: 20rem;
            width: 20rem;
            border-radius: 50%;
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

        &__desc {
            max-width: 50rem;
            grid-row: 2 / 3;
            grid-column: 2 / 3;

            font-size: 1.5rem;
            line-height: 2.2rem;
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

    .artist-content {
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

.empty-artist-message {
    display: flex;
    justify-content: center;
    margin-top: 3rem;
    // text-align: center;
}
</style>