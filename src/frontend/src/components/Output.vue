<template>
  <div class="output">
    <div class="stat">
      <p>Image pixel difference percentage: <b>{{ ratio }}</b> %</p>
      <p>Image compression time: <b>{{ time }}</b> seconds</p>
    </div>
    <div class="download">
      <button class="btn-dl"
              v-bind:style="imgResult.length ? {'display': 'block'} : {'display': 'none'}"
              @click="downloadImage"
      >Download
      </button>
    </div>
  </div>
</template>

<script>

export default {
  name: "Output",
  props: {
    imgName: String,
    imgResult: String,
    ratio: Number,
    time: Number
  },
  methods: {
    downloadImage() {
      let a = document.createElement("a");
      let originalName = this.imgName.split(".");
      let newName = originalName[0] + " (compressed)." + originalName[1];
      a.href = this.imgResult;
      a.download = newName
      a.click();
    }
  }
}
</script>

<style scoped>
.output {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.stat {
  text-align: left;
  margin-left: 1em;
}

.download {
  display: flex;
  align-items: center;
  margin-right: 1em;
}

.btn-dl {
  cursor: pointer;
  font-family: Glory, sans-serif;
  font-size: 1em;
  height: 3em;
  width: 6em;
  border: transparent;
  border-radius: 0.5em;
}

@media only screen and (max-width: 600px) {
  .output {
    flex-direction: column;
    align-items: center;
  }
}
</style>