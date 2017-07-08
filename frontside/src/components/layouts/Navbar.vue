<template>
  <div>
    <div class="title-bar" data-responsive-toggle="top-bar" data-hide-for="medium">
      <button class="menu-icon" type="button" data-toggle="top-bar"></button>
    </div>
    <div class="top-bar" id="top-bar">
      <div class="top-bar-left">
        <ul class="menu dropdown" data-dropdown-menu>
          <li><router-link to="/">Liberain</router-link></li>
        </ul>
      </div>
      <div class="top-bar-right">
        <ul class="menu">
          <li><router-link to="/sign-in">Sign In</router-link></li>
        </ul>
      </div>
    </div>
  </div>
</template>


<script>
  export default {
    name: 'Navbar'
  }
</script>


<style lang="scss" scoped>
  $background-color: #333;
  $text-color: $white;

  .top-bar {
    background: $background-color;
    color: $text-color;

    a {
      color: $text-color;
      font-weight: 600;
    }

    .menu {
      background: $background-color;
    }
  }
</style>
