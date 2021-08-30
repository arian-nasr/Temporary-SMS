<template>
    <div>

        <div class="position-relative">
            <!-- shape Hero -->
            <section class="section-shaped my-0">
                <div class="shape shape-style-1 shape-default shape-skew">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
                <div class="container shape-container d-flex">
                    <div class="col px-0">
                        <div class="row">
                            <div class="col-lg-6">
                                <h1 class="display-3  text-white">Canadian Numbers
                                </h1>
                                <p class="lead  text-white">Select any available number. You will be the only person with access to that phone number for 1 minute. After a minute anyone can use the number, but they won't see any messages.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <!-- 1st Hero Variation -->
        </div>
        <section class="section section-lg pt-lg-0 mt--200">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-12">
                        <div class="row row-grid">
                            <div class="col-lg-4" v-for="(number, index) in numbers" :key="index">
                                <card class="border-0" hover shadow body-classes="py-5">
                                    <h6 class="text-primary text-uppercase">{{ number.digits }}</h6>
                                    <p class="description mt-3">{{ number.region }}</p>
                                    <base-button tag="a" href="#/0e443fd" type="primary" class="mt-4">
                                        {{ number.availability }}
                                    </base-button>
                                </card>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import axios from "axios";
export default {
  name: "home",
  components: {},
  data() {
    return {
      numbers: [],
    };
  },
  methods: {
    getAvailability() {
      const path = 'http://192.168.0.21:5000/available';
      axios.get(path)
        .then((res) => {
          this.numbers = res.data.numbers;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getAvailability();
    this.interval = setInterval(() => this.getAvailability(), 1000);
  },
  beforeDestroy() {
    clearInterval(this.interval)
  },
};
</script>
