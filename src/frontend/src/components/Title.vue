<template>
  <div class="title">
    <h1>
      <span>I</span>
      <span>m</span>
      <span>a</span>
      <span>g</span>
      <span>e</span>
      <span> C</span>
      <span>o</span>
      <span>m</span>
      <span>p</span>
      <span>r</span>
      <span>e</span>
      <span>s</span>
      <span>s</span>
      <span>i</span>
      <span>o</span>
      <span>n</span>
    </h1>
    <div class="hl"></div>
  </div>
</template>

<script>
export default {
  name: "Title"
}
</script>

<style scoped>
.title h1 {
  user-select: none;
  font-size: 2em;
  font-weight: bold;
  color: transparent;
  text-transform: uppercase;
  -webkit-background-clip: text;
  animation: animate 5s linear infinite;
  background-size: 500%;
  background-image: linear-gradient(to left, #f6a8fd, #e13d7c, #f6a4fd, #ea40ad);
}

.title h1 span {
  transition: 0.25s ease-out 0.5s;
}

.title h1 span:hover {
  transition: 0.25s ease-out 0s;
  font-size: 1.25em;
}

.hl {
  border-top: 1px solid #09c7e8;
  margin: 0 6em;
  height: 0;
}
</style>