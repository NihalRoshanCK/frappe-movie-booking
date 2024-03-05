<template>
  <div>
  <HomeBanner/>
  <div style="padding:0 15%; margin-top:1%;" class="bg-gray-200"> 
    <CardCollection/>
  </div>
  </div>
</template>

<script>
import HomeBanner from './banner.vue'
import CardCollection from './cardCollection.vue'

export default {
  components: { HomeBanner, CardCollection },

}
</script>

<style>

</style>