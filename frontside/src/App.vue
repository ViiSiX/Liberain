<template>
  <div id="app">
    <navbar></navbar>
    <router-view></router-view>
  </div>
</template>

<script>
  import { Navbar } from './components/layouts'

  export default {
    name: 'app',
    components: { Navbar },
    mounted () {
      this.app = $('#app').foundation()
    }
  }
</script>

<style lang="scss">
  @import "./styles/global";
</style>

<style lang="css">
  @import "~typicons.font";

  .typcn-size-mid {
    font-size: large;
  }
</style>
