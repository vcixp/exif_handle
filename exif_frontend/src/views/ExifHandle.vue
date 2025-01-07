<script>
import axios from 'axios';

export default {
  name: 'ExifHandle',
  data() {
    return {
      btnText: 'upload & start',
      btnClass: 'bi bi-cloud-upload',
      imgSrc: '',
      btnDisable: false,
      point: 0,
      prompt: '这会需要一些时间，请耐心等待!',
      promptShow: false
    }
  }, mounted() {
  }, methods: {
    choiceImg: function () {
      this.$refs.filElem.dispatchEvent(new MouseEvent('click'))
    }, getFile: function (event) {
      const file = event.target.files[0];
      this.uploadFile(file);
    }, uploadFile: function (file) {
      this.btnClass = "bi bi-hypnotize"
      this.point = 0
      this.btnText = "loading..."
      this.btnDisable = true
      let that = this
      let timer = setInterval(() => {
        let str = 'loading'
        this.promptShow = true
        let i = 0
        for (; i <= that.point % 3; i++) {
          str += '.'
        }
        for (; i <= 2; i++) {
          str += ' '
        }
        that.btnText = str
        that.point++;
      }, 300)
      const formData = new FormData();
      formData.append('file', file);
      axios.post('/api/getExifPhoto', formData)
          .then(response => {
// 处理上传成功的逻辑
            that.imgSrc = "/api/download/" + response.data
            that.btnClass = 'bi bi-cloud-upload'
            clearInterval(timer)
            timer = null
            that.btnText = 'upload & start'
            that.btnDisable = false
            that.$refs.filElem.value = ''
            this.promptShow = false
          })
          .catch(() => {
// 处理上传失败的逻辑
          });
    }
  }
}
</script>

<template>
  <div class="container">
    <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
      <router-link to="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
        <svg class="bi me-2" width="40" height="32">
          <use xlink:href="#bootstrap"/>
        </svg>
        <span class="fs-4">ImageBorder</span>
      </router-link>

      <ul class="nav nav-pills">
        <li class="nav-item"><a href="#uc" class="nav-link">Use Cases</a></li>
        <li class="nav-item"><a href="#faq" class="nav-link">FAQ</a></li>
      </ul>
    </header>
    <div class="px-4 py-5 my-5 text-center">
      <h1 class="display-5 fw-bold">Make Your Photos Pop and Professional: Add Beautiful EXIF borders Easily! </h1>
      <div class="col-lg-8 mx-auto">
        <p class="lead mb-4" style="font-size: 1.1rem">The content within the borders is derived from the photo's EXIF
          information (typically
          including details such as camera make, lens information). Some photos may lack EXIF data; we recommend
          uploading the original photo files for the best results.</p>
        <p class="uploadImg">
          <input ref="filElem" type="file" multiple accept="image/*,.heic" @change="getFile"/>
        </p>
        <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">

          <button type="button" class="btn btn-primary btn-lg px-4 gap-3" @click="choiceImg"  style="width: 200px" :disabled="btnDisable" >
            <i :class="btnClass"></i>
            {{ btnText }}
          </button>
        </div>
        <br>
        <p class="lead mb-4" style="font-size: 1.1rem" v-if="promptShow">{{prompt}}</p>
        <p class="lead mb-4" style="font-size: 1.1rem" v-else>&nbsp;</p>
      </div>
    </div>
    <div class="px-4 py-5 my-5 text-center" v-if="imgSrc!==''">
      <img :src="imgSrc" style="max-width:100%;" alt="not found image" width="90%"/>
    </div>
    <div class="px-4 py-5 my-5 text-center" v-else>
      <img src="/first.jpg" style="max-width:100%;" alt="not found image" width="90%"/>
    </div>
    <br>
    <div class="px-4 py-5 my-2 text-center" id="uc">
      <h1 class="display-5 fw-bold" id="faq">Example</h1>
      <p class="lead mb-2" style="font-size: 1.5rem">Before&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;After</p>
      <div class="px-4 py-5 my-1 text-center" >
        <img src="/effect.jpg" style="max-width:100%;" width="90%" alt="not found image"/>
      </div>
    </div>

    <div class="px-4 py-5 my-2 text-center">
      <h1 class="display-5 fw-bold" id="faq">Frequently Asked Questions</h1>
      <div class="col-lg-6 mx-auto">
        <p class="lead mb-4" style="font-size: 0.9rem">Here are some of the most frequently asked questions about our
          services.</p>
      </div>

      <div class="accordion accordion-flush" id="accordionFlushExample">
        <div class="accordion-item">
          <h2 class="accordion-header" id="flush-headingOne">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                    style="font-size: 20px;font-weight: bold"
                    data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
              1.What information can ImageBorder add to photos?
            </button>
          </h2>
          <div id="flush-collapseOne" class="accordion-collapse collapse" aria-labelledby="flush-headingOne"
               data-bs-parent="#accordionFlushExample">
            <div class="accordion-body" style="text-align: left">ImageBorder can add information such as camera make,
              lens, aperture, ISO, shooting date, and more.
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header" id="flush-headingTwo">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                    style="font-size: 20px;font-weight: bold"
                    data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
              2.How does ImageBorder retrieve information?
            </button>
          </h2>
          <div id="flush-collapseTwo" class="accordion-collapse collapse" aria-labelledby="flush-headingTwo"
               data-bs-parent="#accordionFlushExample">
            <div class="accordion-body" style="text-align: left">We extract details like camera make, lens, aperture,
              ISO, shooting date, and more from the EXIF data of the photos.
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header" id="flush-headingThree">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                    style="font-size: 20px;font-weight: bold"
                    data-bs-target="#flush-collapseThree" aria-expanded="false" aria-controls="flush-collapseThree">
              3.What is EXIF?
            </button>
          </h2>
          <div id="flush-collapseThree" class="accordion-collapse collapse" aria-labelledby="flush-headingThree"
               data-bs-parent="#accordionFlushExample">
            <div class="accordion-body" style="text-align: left">EXIF (Exchangeable Image File Format) is a standard for
              storing metadata in image files, which includes information about the camera settings, shooting
              conditions, and other details related to the photo.
            </div>
          </div>
        </div>

        <div class="accordion-item">
          <h2 class="accordion-header" id="flush-headingThree">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                    style="font-size: 20px;font-weight: bold"
                    data-bs-target="#flush-collapseFour" aria-expanded="false" aria-controls="flush-collapseFour">
              4.Why am I being told that my photo lacks EXIF information?
            </button>
          </h2>
          <div id="flush-collapseFour" class="accordion-collapse collapse" aria-labelledby="flush-headingThree"
               data-bs-parent="#accordionFlushExample">
            <div class="accordion-body" style="text-align: left">Not all photos contain EXIF data. Photos in formats
              such as JPEG (.jpg, .jpeg), TIFF (.tiff, .tif), or RAW (.cr2, .nef, .arw) typically include EXIF
              information. Ensure that the photos you upload have not been compressed, as compression software often
              removes EXIF data to reduce file size.
            </div>
          </div>
        </div>

        <div class="accordion-item">
          <h2 class="accordion-header" id="flush-headingThree">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                    style="font-size: 20px;font-weight: bold"
                    data-bs-target="#flush-collapseFive" aria-expanded="false" aria-controls="flush-collapseFive">
              5.Why can't the brand logo of my camera/phone be displayed in the photos I upload?
            </button>
          </h2>
          <div id="flush-collapseFive" class="accordion-collapse collapse" aria-labelledby="flush-headingThree"
               data-bs-parent="#accordionFlushExample">
            <div class="accordion-body" style="text-align: left">We are gradually adding logos of all brands available
              on the market, and currently, we have not fully covered them. We apologize for any inconvenience.
            </div>
          </div>
        </div>
      </div>


    </div>
    <footer class="py-3 my-4">
      <p class="text-center text-muted" style="font-size: 20px;font-weight: bolder">ImageBorer</p>
      <p class="text-center text-muted">Make Your Photos Pop and Professional: Add Beautiful EXIF borders Easily! </p>

      <ul class="nav justify-content-center">
        <li class="nav-item">
          <router-link to="/terms" class="nav-link px-2 text-muted">Terms of Services</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/policy" class="nav-link px-2 text-muted"> Privacy Policy</router-link>
        </li>
      </ul>
      <p class="text-center text-muted">&copy; ImageBorder 2024. All rights reserved.</p>
    </footer>

  </div>
</template>

<style scoped>
.bd-placeholder-img {
  font-size: 1.125rem;
  text-anchor: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
}

@media (min-width: 768px) {
  .bd-placeholder-img-lg {
    font-size: 3.5rem;
  }
}

.b-example-divider {
  height: 3rem;
  background-color: rgba(0, 0, 0, .1);
  border: solid rgba(0, 0, 0, .15);
  border-width: 1px 0;
  box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
}

.b-example-vr {
  flex-shrink: 0;
  width: 1.5rem;
  height: 100vh;
}

.bi {
  vertical-align: -.125em;
  fill: currentColor;
}

.nav-scroller {
  position: relative;
  z-index: 2;
  height: 2.75rem;
  overflow-y: hidden;
}

.nav-scroller .nav {
  display: flex;
  flex-wrap: nowrap;
  padding-bottom: 1rem;
  margin-top: -1px;
  overflow-x: auto;
  text-align: center;
  white-space: nowrap;
  -webkit-overflow-scrolling: touch;
}

.form-control-dark {
  border-color: var(--bs-gray);
}

.form-control-dark:focus {
  border-color: #fff;
  box-shadow: 0 0 0 .25rem rgba(255, 255, 255, .25);
}

.text-small {
  font-size: 85%;
}

.dropdown-toggle {
  outline: 0;
}

.uploadImg {
  width: 100%;
  height: 1.46rem;
  position: relative;

  input {
    width: 1.46rem;
    height: 100%;
    z-index: 1;
    opacity: 0;
    position: absolute;
    cursor: pointer;
  }
}

.sp {
  width: 32px;
  height: 32px;
  clear: both;
  margin: 20px auto;
}

/* Spinner Circle Rotation */
.sp-circle {
  border: 4px rgba(0, 0, 0, 0.25) solid;
  border-top: 4px black solid;
  border-radius: 50%;
  -webkit-animation: spCircRot .6s infinite linear;
  animation: spCircRot .6s infinite linear;
}
</style>