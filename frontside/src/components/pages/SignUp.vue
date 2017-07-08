<template>
  <div>
    <form class="float-center">
      <fieldset>
        <legend>Sign Up</legend>
        <label>
          Display Name
          <input class="input-group-field"
                 type="text"
                 v-model="in_display_name"
                 placeholder="Your display name"/>
        </label>
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
                 v-model="in_password"
                 placeholder="Your password"/>
          <input class="input-group-field"
                 type="password"
                 v-model="in_password_verify"
                 placeholder="Confirm your password"/>
        </label>
        <a class="button expanded"
           v-on:click="verifyAndSignUp"
        >Sign Up</a>
        <i>You are our user? <router-link to="/sign-in">Sign In here</router-link>.</i>
      </fieldset>
    </form>
  </div>
</template>


<script>
  import validator from 'validator'

  export default {
    name: 'SignUp',
    data () {
      return {
        in_display_name: '',
        in_email: '',
        in_password: '',
        in_password_verify: ''
      }
    },
    methods: {
      verifyAndSignUp () {
        this.in_email = validator.normalizeEmail(this.in_email)
        this.in_display_name = validator.blacklist(this.in_display_name, '<>;?\\[\\]/\\\\')

        if (validator.isEmail(this.in_email) &&
          !validator.isEmpty(this.in_display_name) &&
          !validator.isEmpty(this.in_password) &&
          validator.equals(this.in_password, this.in_password_verify)
        ) {
          console.log('Sending to server for sign up...')
        }
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
