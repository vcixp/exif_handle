<script>
export default {
  name: 'Policy'
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
    </header>

    <div class="px-4 py-5 my-5 text-center">
      <h1 class="display-5 fw-bold ">Privacy Policy </h1>
      <p class="lead mb-4 border-bottom">This Privacy Policy describes how we collect, use, and share information when
        you use our services.</p>
      <br><br><br>
      <h2 class="display-6 fw-bold" style="text-align: left">Information We Collect </h2>
      <p class="lead mb-6" style="text-align: left"><b class="display-7 fw-bold ">Personal Information:</b> We may
        collect personal information such as name, email address, and contact details when you register for our
        services.</p>
      <p class="lead mb-6" style="text-align: left"><b class="display-7 fw-bold ">Usage Information:</b> We may collect
        information about how you interact with our services, such as log data, device information, and cookies.</p>


      <h2 class="display-6 fw-bold" style="text-align: left">How We Use Your Information</h2>
      <p class="lead mb-6" style="text-align: left">We use the information we collect to
        provide, maintain, and improve our services, as well as to communicate with you.</p>

      <h2 class="display-6 fw-bold" style="text-align: left">Information Sharing</h2>
      <p class="lead mb-6" style="text-align: left">We do not share your personal information with third parties unless required by law or to provide our services.</p>

      <h2 class="display-6 fw-bold" style="text-align: left">Data Security</h2>
      <p class="lead mb-6" style="text-align: left">We implement security measures to protect your information from unauthorized access and maintain data accuracy.</p>

      <h2 class="display-6 fw-bold" style="text-align: left">Your Choices</h2>
      <p class="lead mb-6" style="text-align: left">You can access, update, or request deletion of your personal information by contacting us.</p>

      <h2 class="display-6 fw-bold" style="text-align: left">YChanges to This Policy</h2>
      <p class="lead mb-6" style="text-align: left">We may update this Privacy Policy from time to time. Any changes will be reflected on this page.</p>

      <h2 class="display-6 fw-bold" style="text-align: left">Contact Us</h2>
      <p class="lead mb-6" style="text-align: left">If you have any questions about this Privacy Policy, please contact us at  <a href="mailto:bngnmcm@gmail.com">bngnmcm@gmail.com</a></p>
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

</style>