<template>
  <div class="before-container">
    <div class="heading">
      <h3>{{title}}</h3>
    </div>
    <div class="img-container">
      <img
          :src="imgData.length ? imgData : imgDefault"
          alt="NO IMAGE">
    </div>
  </div>
</template>

<script>
export default {
  name: "Image",
  data() {
    return {
      imgDefault: "https://content.hostgator.com/img/weebly_image_sample.png"
    }
  },
  props: {
    imgData: String,
    title: String
  }
}
</script>

<style scoped>
h3 {
  margin: 1em 0 0;
}

.heading {
  margin: 1em 0;
}

img {
  width: 25em;
  max-width: 50vw;
  max-height: 30vw;
}
</style>