<template>
    <div>
        <div class="position-relative">
            <!-- shape Hero -->
            <!-- 1st Hero Variation -->
        </div>
        <section class="section section section-shaped my-0 overflow-hidden">
            <div class="shape shape-style-1 bg-gradient-warning shape-skew">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
            <div class="container py-0">
                <div class="row row-grid align-items-center">
                    <div class="col-md-6 order-lg-2 ml-lg-auto">
                        <div class="position-relative pl-md-5">
                        </div>
                    </div>
                    <div class="col-lg-6 order-lg-1">
                        <div class="d-flex px-3">
                            <div>
                                <a href="#/landing"><icon name="ni ni-bold-left" size="lg" class="bg-gradient-white" color="primary" shadow
                                      rounded></icon></a>
                            </div>
                            <div class="pl-4">
                                <h4 class="display-3 text-white">+1 (647) 372-0627</h4>
                            </div>
                        </div>
                        <card shadow class="shadow-lg--hover mt-5" v-for="(message, index) in messages" :key="index">
                            <div class="d-flex px-3">
                                <div>
                                    <icon name="ni ni-fat-delete" gradient="success" color="white" shadow
                                          rounded></icon>
                                </div>
                                <div class="pl-4">
                                    <h5 class="title text-success">{{ message.sender }}</h5>
                                    <p>{{ message.date }}</p>
                                    <p>{{ message.body }}</p>
                                </div>
                            </div>
                        </card>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "home",
  components: {},
  data() {
      return {
          messages: [],
      };
  },
  methods: {
      getMessages() {
          const path = 'http://192.168.0.21:5000/messages';
          axios.get(path)
            .then((res) => {
                this.messages = res.data.messages;
            })
            .catch((error) => {
                console.error(error);
            });
      },
  },
  created() {
      this.getMessages();
      this.interval = setInterval(() => this.getMessages(), 1000);
  },
  beforeDestroy() {
    clearInterval(this.interval)
  },
};
</script>