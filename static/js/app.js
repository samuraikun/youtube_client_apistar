const app = new Vue({
  el: '#app',
  delimiters: ["[[", "]]"],
  data: {
    message: 'ASMR Star',
    query: '',
    order_by: '',
    results: []
  },
  methods: {
    search_video: function () {
      axios.get('/search', {
        params: {
          query: this.query,
          order_by: this.order_by
        }
      })
      .then(response => { this.results = response.data; })
      .catch(error => { console.log(error);
      });
    }
  }
});
