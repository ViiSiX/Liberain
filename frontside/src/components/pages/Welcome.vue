<template>
  <div class="sections">
    <section class="hero text-center">
      <h1>{{ msg }}</h1>
      <img alt="Liberain's Logo"
           src="/static/logo.png">
      <h4>{{ about }}</h4>
      <router-link to="/sign-in"
                   class="button"
      >Sign In</router-link>
      <router-link to="/sign-up"
                   class="hollow button"
      >Sign Up</router-link>
    </section>
    <section class="about">
      <div class="text-center">
        <p>
          <strong>Liberain</strong> by <a href="https://viisix.space">ViiSiX Team</a>.<br/>
          <a href="https://github.com/ViiSiX/Liberain">
            <span class="typcn typcn-size-mid typcn-social-github-circular"></span>
            &nbsp;Source code
          </a>
        </p>
      </div>
    </section>
  </div>
</template>


<script>
export default {
  name: 'Welcome',
  data () {
    return {
      msg: 'Welcome to Liberain!',
      about: 'A place to store memories together.'
    }
  }
}
</script>


<style lang="scss">
  .hero {
    padding-top: 6rem;
    padding-bottom: 3rem;

    img {
      width: 20%;
      margin: 0.5rem;
    }

    .hollow.button {
      border: 1px solid #b0db90;
      color: #4a752a;
    }

    .hollow.button:hover {
      background: #b0db90;
    }
  }

  .about {
    padding: 1rem;

    a {
      font-weight: 600;
      color: $black;
    }
  }
</style>
