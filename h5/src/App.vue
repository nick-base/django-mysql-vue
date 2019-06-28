<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Page1</router-link>
      <router-link to="/page2">Page2</router-link>
    </div>
    <router-view/>
  </div>
</template>
<style lang="stylus">
html
  margin 0
  padding 0
body
  margin 0
  padding 0
#app
  font-family 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
  color #2c3e50

#nav
  box-shadow 0 1px 2px 0 rgba(0, 0, 0, .15)
  padding 20px 30px
  a
    margin-right 30px
    font-weight bold
    color #66b1ff
    text-decoration none
    &.router-link-exact-active
      color #409EFF
      text-decoration underline
</style>
