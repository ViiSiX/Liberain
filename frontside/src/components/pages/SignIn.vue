<template>
  <div>
    <form class="float-center">
      <fieldset>
        <legend>Sign In</legend>
        <label>
          Email Address
          <input class="input-group-field"
                 type="email"
                 v-model="in_email"
                 placeholder="Your email address"/>
        </label>
        <label>
          Password
          <input class="input-group-field"
                 type="password"
                 placeholder="Your password"/>
        </label>
        <a class="button expanded"
           v-on:click="verifyAndSignIn"
        >Sign In</a>
        <i>Not an user? <router-link to="/sign-up">Sign Up here</router-link>.</i>
      </fieldset>
    </form>
  </div>
</template>


<script>
  export default {
    name: 'SignIn',
    data () {
      return {
        in_email: '',
        in_password: ''
      }
    },
    methods: {
      verifyAndSignIn () {
        console.log(this.in_email)
      }
    }
  }
</script>


<style lang="scss">
  form {
    max-width: 500px;
    padding: 3rem 1rem;

    legend {
      font-weight: bold;
    }

    .input-group-field {
      margin-bottom: 5px;
      border-radius: 2px;
    }

    .button {
      margin-top: 20px;
      border-radius: 2px;
    }
  }
</style>
