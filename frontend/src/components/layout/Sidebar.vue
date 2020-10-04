<template>
    <header class="sidebar">
        <router-link :to="{ name: 'Home' }" tag="a" class="app-logo">
            Musify
        </router-link>

        <nav class="sidebar__nav">
            <router-link
                :to="{ name: 'Home' }"
                class="sidebar__nav-item"
                active-class="active"
                exact
            >
                <ion-icon name="home"></ion-icon>
                Home
            </router-link>

            <router-link
                :to="{ name: 'Library' }"
                class="sidebar__nav-item"
                active-class="active"
            >
                <ion-icon name="library-sharp"></ion-icon>
                Library
            </router-link>

            <router-link
                :to="{ name: 'Charts' }"
                class="sidebar__nav-item"
                active-class="active"
            >
                <ion-icon name="star-sharp"></ion-icon>
                Charts
            </router-link>
        </nav>
        <form class="searchbar">
            <input type="text" placeholder="Search" class="searchbar__input" />
        </form>

        <div class="networks">
            <a href="https://www.instagram.com/drowning.drew/" target="_blank">
                <ion-icon name="logo-instagram"></ion-icon>
            </a>
            <a href="https://twitter.com/deadbadsadmad" target="_blank">
                <ion-icon name="logo-twitter"></ion-icon>
            </a>
        </div>
        <p class="copyright">
            &copy; 2020 Musify Song Service by Drowning.Drew
        </p>
    </header>
</template>

<script>
export default {};
</script>

<style lang="scss">
@import "../../../src/assets/style/variables";

.sidebar {
    background-color: $color-purple-dark;
    color: $color-white;
    font-size: 2rem;
    font-weight: 700;
    font-family: $font-primary;

    // height: 100vh;

    // position: fixed;

    display: flex;
    flex-direction: column;
    align-items: center;

    .app-logo {
        font-size: 3.5rem;
        font-family: $font-logo;

        margin: 2rem;
        margin-bottom: 4rem;
        letter-spacing: 2px;
    }

    &__nav {
        list-style: none;

        display: flex;
        flex-direction: column;
        gap: 2rem;

        .active {
            background-color: $color-purple;
            box-shadow: 0 1rem 3rem rgba($color-black, 0.2);
        }
    }

    &__nav-item {
        padding: 1.3rem 5rem;

        transition: all 0.3s;

        display: flex;
        gap: 1.2rem;
        cursor: pointer;

        &:hover {
            background-image: linear-gradient(
                rgba($color-purple, 0.1),
                rgba($color-purple, 0.2)
            );
            box-shadow: 0 1rem 3rem rgba($color-black, 0.4);
        }
    }

    a:link,
    a:visited {
        text-decoration: none;
        color: $color-white;
    }

    .searchbar {
        display: flex;
        margin-top: 4rem;

        &__input {
            font-size: 1.6rem;
            padding: 1rem 1.5rem;
            outline: none;
            border: none;
            border-radius: 1rem;
            background-color: $color-purple-light-2;
            transition: all 0.2s;

            &:focus {
                box-shadow: 0 1rem 3rem rgba($color-black, 0.4);
                transform: scale(1.05);
            }
        }
    }

    .networks {
        margin-top: auto;
        padding: 1.5rem 0;
        display: flex;
        width: 80%;
        justify-content: space-evenly;
    }

    .copyright {
        text-align: center;
        font-weight: 300;
        font-size: 1.4rem;
        line-height: 2rem;

        margin-bottom: 2rem;
        max-width: 80%;
    }
}
</style>