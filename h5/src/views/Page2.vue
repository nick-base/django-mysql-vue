<template>
  <div class="page2">
    <div class="table">
      <div class="line table-header">
        <div class="header">Id</div>
        <div class="value">Value</div>
      </div>
      <div class="line" v-for="(item, index) in data" :key="index">
        <div class="header">{{ item.id }}</div>
        <div class="value">{{ item.data }}</div>
      </div>
    </div>
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

<style lang="stylus" scoped>
.table
  border 1px solid #aaa
  border-radius 5px
  width 600px
  margin 20px auto

.line
  height 36px
  line-height 36px
  .header
    width 100px
    text-align center
    display inline-block
  .value
    display inline-block
    border-left 1px solid #aaa
    padding-left 20px
  + .line
    border-top 1px solid #aaa
  &.table-header
    font-weight 700
</style>
