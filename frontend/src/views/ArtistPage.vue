<template>
    <div class="artist-page" v-if="!notFound">
        <template v-if="artist">
            <div class="artist-info">
                <div class="artist-info__picture">
                    <img
                        :src="artist.picture"
                        alt="Artist Picture"
                        draggable="false"
                    />
                </div>
                <h2 class="artist-info__title">{{ artist.name }}</h2>
                <!-- <div
                    class="followed-btn"
                    @click="artistFollowed = !artistFollowed"
                >
                    <ion-icon
                        :name="artistFollowed ? 'heart-outline' : 'heart'"
                    ></ion-icon>
                </div> -->

                <!-- <p class="artist-info__desc">{{ artist.description || "-" }}</p> -->
                <p class="artist-info__desc">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    Deleniti minima, veritatis voluptas id similique aspernatur!
                    Sunt, ea magnam maxime, excepturi nam officia iste sequi
                    vitae illo quas tenetur quo! Omnis. Lorem ipsum dolor sit
                    amet consectetur adipisicing elit. Deleniti minima,
                    veritatis voluptas id similique aspernatur! Sunt, ea magnam
                    maxime, excepturi nam officia iste sequi vitae illo quas
                    tenetur quo! Omnis.
                </p>
            </div>

            <div class="artist-content">
                <section class="top-songs">
                    <h3 class="subtitle">Top Songs</h3>
                    <Song
                        v-for="song in artist.songs"
                        :key="song.id"
                        :song="song"
                    >
                    </Song>
                </section>

                <section class="albums">
                    <h3 class="subtitle">Albums</h3>
                    <ul>
                        <li v-for="album in artist.albums" :key="album.id">
                            {{ album.name }}
                            <img :src="album.cover" alt="album cover" />
                        </li>
                    </ul>
                </section>
            </div>
        </template>
    </div>
    <p v-else class="text-center">Artist is not found! Please, try again</p>
</template>

<script>
import Song from "../components/cards/Song";

export default {
    data() {
        return {
            artist: null,
            notFound: false,
        };
    },
    components: {
        Song,
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

<style scoped lang="scss">
@import "../../src/assets/style/variables";

.artist-page {
    max-width: fit-content;
    
    .artist-info {
        background-color: $color-purple-dark;
        color: #d3d3d3; // TODO:
        box-shadow: 0 1rem 3rem rgba($color-black, 0.4);
        border-radius: 1rem 0;
        padding: 3rem;

        max-width: fit-content;

        display: grid;
        grid-template-columns: max-content max-content 1fr;
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
            grid-column: 2 / 4;

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
        .top-songs {
            margin: 3rem;
            padding: 2rem;
            border-bottom: 1px solid gray;
        }

        .subtitle {
            text-transform: uppercase;
            font-size: 2.6rem;
        }

        img {
            width: 200px;
            border-radius: 50%;
            border: 3px solid #777;
        }
    }
}
</style>