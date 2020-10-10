<template>
    <div class="album-card" v-if="album">
        <div class="album-image">
            <img :src="album.cover" alt="Album Cover" draggable="false" />
        </div>
        <div class="album-info">
            <h3 class="album-info__name">
                <router-link
                    :to="{ name: 'Album', params: { albumId: album.id } }"
                >{{ album.name }}</router-link>
            </h3>
            <p class="album-info__genre">{{ album.pub_year }}</p>
        </div>
    </div>
</template>

<script>
export default {
    props: ["album"],
};
</script>

<style lang="scss">
@import "../../../src/assets/style/variables";

.album-card {
    overflow: hidden;
    height: 25rem;
    width: 19rem;
    margin: 1rem;
    margin-left: 0;
    max-width: max-content;
    border-radius: 1rem;
    box-shadow: 0 1rem 2rem rgba($color-black, 0.5);

    display: flex;
    flex-direction: column;
    background-color: #444;

    .album-image {
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

    .album-info {
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