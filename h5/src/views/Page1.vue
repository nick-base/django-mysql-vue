<template>
  <div class="page1">
    page 1
  </div>
</template>

<script>
export default {
  name: 'page1',
  created () {
    this.show()
  },
  methods: {
    show () {
      this.$http({
        method: 'get',
        url: '/api/hello'
      }).then(function (response) {
        console.log(response.data)
      })
    }
  }
}
</script>
