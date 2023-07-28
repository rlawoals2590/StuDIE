import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: null
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
    }
  },
  actions: {
    login({ commit }, { token }) {
      commit('setToken', token);
    },
    logout({ commit }) {
      commit('setToken', null);
    }
  }
});
