<template>
  <div class="page2">
    <table border="1">
      <tr>
        <th>Id</th>
        <th>Value</th>
      </tr>
      <tr v-for="(item, index) in data" :key="index">
        <td>{{ item.id }}</td>
        <td>{{ item.data }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'page2',
  data () {
    return {
      data: []
    }
  },
  created () {
    this.$http({
      method: 'get',
      url: '/api/save-data'
    }).then((response) => {
      this.data = response.data.data.values
    })
  }
}
</script>
