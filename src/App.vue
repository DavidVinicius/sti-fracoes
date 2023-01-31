<script setup>
  import { RouterLink, RouterView } from 'vue-router'      
  
</script>

<template>  
  <!-- <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/about">About</RouterLink>
  </nav> -->

  <RouterView />
</template>

<script>

export default {  
  data() {
    return {      
      name: ''
      
    }
  },
  methods: {
    setUserName(event) {
      console.log("naming ..");
      
    }
  }
}
</script>

