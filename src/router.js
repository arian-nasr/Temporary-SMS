import Vue from "vue";
import Router from "vue-router";
import AppHeader from "./layout/AppHeader";
import AppFooter from "./layout/AppFooter";
import Components from "./views/Components.vue";
import Landing from "./views/Landing.vue";
import Login from "./views/Login.vue";
import Register from "./views/Register.vue";
import Profile from "./views/Profile.vue";
import first from "./views/0e443fd.vue";
import Ping from "./views/Ping.vue";
import axios from "axios";

Vue.use(Router);
const router = new Router({
  linkExactActiveClass: "active",
  routes: [
    {
      path: "/ping",
      name: 'Ping',
      component: Ping,
    },
    {
      path: "/",
      name: "components",
      components: {
        header: AppHeader,
        default: Components,
        footer: AppFooter
      }
    },
    {
      path: "/landing",
      name: "landing",
      components: {
        header: AppHeader,
        default: Landing,
        footer: AppFooter
      }
    },
    {
      path: "/login",
      name: "login",
      components: {
        header: AppHeader,
        default: Login,
        footer: AppFooter
      }
    },
    {
      path: "/register",
      name: "register",
      components: {
        header: AppHeader,
        default: Register,
        footer: AppFooter
      }
    },
    {
      path: "/0e443fd",
      name: "0e443fd",
      components: {
        header: AppHeader,
        default: first,
        footer: AppFooter
      },
      meta: {
        requiresAuth: true
      },
    },
    {
      path: "/profile",
      name: "profile",
      components: {
        header: AppHeader,
        default: Profile,
        footer: AppFooter
      }
    }
  ],
  scrollBehavior: to => {
    if (to.hash) {
      return { selector: to.hash };
    } else {
      return { x: 0, y: 0 };
    }
  }
})
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    const path = 'http://192.168.0.21:5000/auth1'
    var authdata = axios.get(path)
        .then((res) => {
          return JSON.stringify(JSON.parse(res.data))
        })
    if (authdata === 'false') {
      next()
    } else {
      next(from)
    }
  } else next()
})
export default router
