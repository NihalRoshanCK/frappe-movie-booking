<template>
  <div>
    <Nav/>
    <Home/>
  </div>
</template>

<script>

import Home from '../../components/home/index.vue';
import Nav from '../../components/navbar/index.vue';
export default {
  components: {
    Nav,
    Home,
  }
}
</script>
