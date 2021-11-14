<template>
  <div class="web-container">
    <Title/>
    <div class="settings">
      <h2>Input your image</h2>
      <div class="file-input-container">
        <input @change="uploadImage"
               type="file"
               accept="image/jpeg, image/png, image/bmp, image/webp"
               class="sm-input-file"
               id="sm-ip-1"/>
        <div class="input-wrapper">
          <label class="for-sm-input-file" for="sm-ip-1">Add File</label>
          <span class="span-text" id="file-name">{{ imgName }}</span>
        </div>
      </div>
      <div class="rate">
        <p>Image compress rate: </p>
        <input class="input-rate" type="number" v-model="rate">
        <p>%</p>
      </div>
    </div>
    <div class="content-wrapper">
      <Image
          v-bind:img-data="imgData"
          title="Before"/>
      <div class="compress-container" v-if="imgData.length && Number.isInteger(rate)">
        <button @click="compress" class="compress">Compress</button>
        <div id="loader" v-if="isLoading"></div>
      </div>
      <Image
          v-bind:img-data="imgResult"
          title="After"/>
    </div>
    <Output
        v-bind:img-name="imgName"
        v-bind:img-result="imgResult"
        v-bind:diff="diff"
        v-bind:time="time"/>
    <transition name="fade" appear>
      <div class="modal-overlay" v-if="showModal" @click="showModal = false"></div>
    </transition>
    <transition name="pop" appear>
      <div class="modal" role="dialog" v-if="showModal">
        <h3>Error</h3>
        <p>{{ message }}</p>
      </div>
    </transition>
  </div>
</template>

<script>
import Image from "@/components/Image";
import Title from "@/components/Title";
import Output from "@/components/Output";
import axios from "axios";

export default {
  name: 'App',
  components: {
    Image,
    Output,
    Title
  },
  data() {
    return {
      diff: 0,
      imgData: "",
      imgName: null,
      imgResult: "",
      isLoading: false,
      message: "",
      time: 0,
      rate: 0,
      showModal: false,
    }
  },
  methods: {
    uploadImage: function (ev) {
      let input = ev.target;
      if (input.files && input.files[0]) {
        this.imgName = input.files[0].name;
        let reader = new FileReader();
        reader.onload = (e) => {
          this.imgData = e.target.result;
        }
        reader.readAsDataURL(input.files[0]);
      }
    },
    compress() {
      this.isLoading = true;
      axios.post("http://localhost:5000/api/compress", {image: this.imgData, ratio: this.rate})
          .then(res => {
            this.isLoading = false;
            if (res.data.success) {
              this.imgResult = res.data.image;
              this.time = res.data.time;
              this.diff =  res.data.diff;
            } else {
              this.showModal = true;
              this.message = res.data.message;
            }
          })
          .catch(err => {
            console.log("Error: " + err.message);
          });
    },
  },
  watch: {
    rate: {
      handler(val) {
        if (val < 0 || val > 99) {
          this.rate = 99;
        }
      }
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Glory:wght@300;400;500;700&display=swap');

body {
  background-color: #222831;
}

#app {
  font-family: Glory, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #d7cfcf;
  margin-top: 1.5em;
  display: flex;
  align-items: center;
  justify-content: center;
}

.web-container {
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0.5em 4em 1.25em;
  width: 70vw;
  border: 1px solid wheat;
  border-radius: 0.5em;
}

.web-container p {
  font-size: 1.10em;
}

.content-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.settings {
  min-width: 50%;
  max-width: 100%;
  margin: 0 0;
  text-align: left;
}

.sm-input-file {
  display: none;
}

.file-input-container {
  height: 2em;
}

.for-sm-input-file {
  width: 90px;
  min-height: 24px;
  border: 1px solid #ea40ad;
  font-weight: bold;
  cursor: pointer;
  text-align: center;
  font-family: consolas, serif;
  color: #ea40ad;
  padding: 10px 6px 6px;
  border-radius: 2px 0 0 2px;
}

.for-sm-input-file:hover {
  background: #ea40ad44;
}

.input-wrapper {
  display: flex;
  align-items: center;
}

.span-text {
  margin-left: 1em;
}

.rate {
  display: flex;
  align-items: center;
  margin-top: 1em;
}

.input-rate {
  width: 2em;
  height: 1.75em;
  margin: 0.5em 0.5em;
  border: 1px solid #ea40ad;
  background: #222831;
  color: #fff;
  font-weight: bold;
  text-align: center;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.compress-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.compress {
  font-family: Glory, sans-serif;
  font-size: 1em;
  border-radius: 0.5em;
  background-color: #222831;
  color: #ea40ad;
  font-weight: bold;
  margin-top: 8px;
  height: 2.5em;
  width: 5em;
  border: 2px solid #ea40ad;
  cursor: pointer;
  transition: .2s ease-in;
}

.compress:hover {
  background-color: #e254ae;
  color: #f3f3f3;
  transform: translateY(2px)
}

@media only screen and (max-width: 1280px) {
  .web-container {
    width: 90vw;
    padding: 0.5em 4em 0.5em;
  }
}

@media only screen and (max-width: 1000px) {
  .web-container {
    align-items: center;
  }

  .content-wrapper {
    flex-direction: column;
  }

  .settings {
    width: 50%;
    margin: 0 auto;
  }
}

@keyframes animate {
  0% {
    background-position: 0 100%;
  }
  50% {
    background-position: 100% 0;
  }
  100% {
    background-position: 0 100%;
  }
}

#loader {
  z-index: 1;
  width: 40px;
  height: 40px;
  border: 8px solid #f3f3f3;
  border-radius: 50%;
  border-top: 8px solid #09c7e8;
  -webkit-animation: spin 2s linear infinite;
  animation: spin 2s linear infinite;
  margin-top: 2em;
}

@-webkit-keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
  }
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.modal {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  margin: auto;
  text-align: center;
  width: 50vw;
  height: fit-content;
  max-width: 22em;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.2);
  background: #FFF;
  z-index: 999;
  transform: none;
}
.modal h3 {
  color: #2c3e50;
}
.modal p {
  color: #2c3e50;
}
.modal-overlay {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 998;
  background: #2c3e50;
  opacity: 0.6;
}
</style>
