<script>
export default {
  name: 'Terms'
}
</script>

<template>
  <div>
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
        <h1 class="display-5 fw-bold border-bottom">Terms and Conditions </h1><br><br><br>
        <h2 class="display-7 fw-bold" style="text-align: left">1.Your Stuff & Your Permissions </h2>
        <p class="lead mb-6" style="text-align: left">When you use our Services, you provide us with things like your
          files, content, email
          address, and so on (“Your Stuff”). Your Stuff is yours. These Terms don’t give us any rights to Your Stuff
          except for the limited rights that enable us to offer the Services.</p>
        <h2 class="display-7 fw-bold" style="text-align: left">2.Your Responsibilities </h2>
        <p class="lead mb-6" style="text-align: left">Please safeguard your password to the Services, make sure that
          others don’t have access to
          it, and keep your account information current. You agree not to misuse the Services. For example, you must
          not, and must not attempt to do the following:</p>
        <p class="lead mb-6" style="text-align: left">probe, scan, or test the vulnerability of any system or
          network;</p>
        <p class="lead mb-6" style="text-align: left">access, tamper with, or use non-public areas or parts of the
          Services, or shared areas of
          the Services you haven’t been invited to;</p>

        <h2 class="display-7 fw-bold" style="text-align: left">3.Software </h2>
        <p class="lead mb-6" style="text-align: left">Some of our Services allow you to download client software
          (“Software”) which may update
          automatically. So long as you comply with these Terms, we give you a limited, nonexclusive, nontransferable,
          revocable license to use the Software, solely to access the Services.</p>


        <h2 class="display-7 fw-bold" style="text-align: left">4.Accounts </h2>
        <p class="lead mb-6" style="text-align: left">We have no accounts system in the latest version. You can use our
          program without creating an account.</p>
        <p class="lead mb-6" style="text-align: left">To facilitate our Service;</p>
        <p class="lead mb-6" style="text-align: left">To perform Service-related services; or</p>
        <p class="lead mb-6" style="text-align: left">To assist us in analyzing how our Service is used.</p>

        <h2 class="display-7 fw-bold" style="text-align: left">5.Liability for our Services</h2>
        <p class="lead mb-6" style="text-align: left">When permitted by law, we will not be responsible for lost
          profits, revenues, or data, financial losses or indirect, special, consequential, exemplary, or punitive
          damages. The total liability of us is limited to the amount you paid us to use the Services.</p>

        <h2 class="display-7 fw-bold" style="text-align: left">6.Links to Other Sites</h2>
        <p class="lead mb-6" style="text-align: left">This Service may contain links to other sites. If you click on a
          third-party link, you will be directed to that site. Note that these external sites are not operated by
          us.</p>

        <h2 class="display-7 fw-bold" style="text-align: left">7.Termination</h2>
        <p class="lead mb-6" style="text-align: left">You’re free to stop using our Services at any time. We also
          reserve the right to suspend or end the Services at any time at our discretion and without notice.</p>

        <h2 class="display-7 fw-bold" style="text-align: left">8.Contact Us</h2>
        <p class="lead mb-6" style="text-align: left">If you have any questions or suggestions about our Privacy Policy,
          do not hesitate to contact us at <a href="mailto:bngnmcm@gmail.com">bngnmcm@gmail.com</a>.</p>
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
  </div>
</template>

<style scoped>

</style>