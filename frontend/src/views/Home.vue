<template>
    <div class="home">
        <h2 class="block-title">Artists</h2>

        <template v-if="!error">
            <div v-if="artists.length" class="artist-grid">
                <ArtistCard
                    v-for="artist in artists"
                    :key="artist.id"
                    :artist="artist"
                />
            </div>
        </template>
        <p class="error-info" v-else>
            Oh, some troubles with the server ;( Please, try again
            <ion-icon
                class="reload-btn"
                @click="fetchArtists"
                name="reload-sharp"
            ></ion-icon>
        </p>
    </div>
</template>

<script>
import ArtistCard from "../components/cards/ArtistCard";

export default {
    data() {
        return {
            artists: [],
            error: false,
        };
    },
    components: {
        ArtistCard,
    },
    methods: {
        async fetchArtists() {
            try {
                let response = await fetch(
                    "http://127.0.0.1:8000/api/artists/"
                );
                this.artists = await response.json();
                this.error = false;
            } catch (error) {
                this.error = true;
            }
        },
    },
    async created() {
        this.fetchArtists();
    },
};
</script>

<style lang="scss">
@import "../../src/assets/style/variables";

.block-title {
    font-size: 4rem;
    letter-spacing: 1px;
}

.artist-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(20rem, 1fr));
    grid-template-rows: 1fr 1fr;
}

// TODO: move to separate file
.error-info {
    margin: 3em;
    padding: 2rem;
    padding-right: 4rem;
    border-radius: 0 1rem;
    border-left: 2.5rem solid #ff3333;
    width: fit-content;

    font-size: 2rem;
    font-weight: 300;
    text-align: center;
    background-color: #333333;
    color: $color-white;

    position: relative;

    .reload-btn {
        position: absolute;
        top: 1rem;
        right: 1rem;
        cursor: pointer;
        transition: transform 0.3s;

        &:hover {
            transform: rotate(270deg);
        }
    }
}
</style>
