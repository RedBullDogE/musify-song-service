<template>
    <div class="artist-card" v-if="artist">
        <div class="artist-image">
            <img :src="artist.picture" alt="Artist Picture" draggable="false" />
        </div>
        <div class="artist-info">
            <h3 class="artist-info__name">
                <router-link
                    :to="{ name: 'ArtistHome', params: { id: artist.id } }"
                >{{ artist.name }}</router-link>
            </h3>
            <p class="artist-info__genre">{{ artist.genre }}</p>
        </div>
    </div>
</template>

<script>
export default {
    props: ["artist"],
};
</script>

<style lang="scss">
@import "../../../src/assets/style/variables";

.artist-card {
    overflow: hidden;
    height: 25rem;
    width: 19rem;
    margin: 1rem;
    max-width: max-content;
    border-radius: 1rem;
    box-shadow: 0 1rem 2rem rgba($color-black, 0.5);

    display: flex;
    flex-direction: column;
    background-color: #444;

    .artist-image {
        height: 15rem;
        width: 15rem;
        border-radius: 1rem;
        margin: 2rem 2rem 1.5rem 2rem;
        overflow: hidden;

        img {
            height: 100%;
            margin-left: 50%;
            transform: translateX(-50%);
        }
    }

    .artist-info {
        margin: 2rem;
        margin-top: 0rem;
        color: $color-purple-light-2;

        &__name {
            font-size: 1.6rem;
            text-overflow: ellipsis;
            overflow: hidden;
            white-space: nowrap;
            margin-bottom: 0.5rem;

            a:link,
            a:visited {
                text-decoration: none;
                color: currentColor;
            }

            a:hover {
                text-decoration: underline;
            }
        }

        &__genre {
            font-size: 1.4rem;
            font-weight: 300;
            text-transform: capitalize;
        }
    }
}
</style>