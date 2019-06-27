<template>
  <div>
    <div class="save">
     <span @click="save">保存</span>
    </div>
    <vue-highcharts :options="options" ref="lineCharts"></vue-highcharts>
  </div>
</template>

<script>
import VueHighcharts from 'vue2-highcharts'

export default {
  components: {
    VueHighcharts
  },
  data () {
    return {
      timer: null,
      showLast: false,
      lastData: {
        name: 'last',
        marker: {
          symbol: 'circular'
        },
        color: 'red',
        data: []
      },
      currentData: {
        name: 'current',
        marker: {
          symbol: 'square'
        },
        data: []
      },
      options: {
        chart: {
          type: 'spline'
        },
        title: {
          text: 'Gen data demo'
        },
        subtitle: {
          text: 'nick.na'
        },
        xAxis: {
          categories: [
            'Data1',
            'Data2',
            'Data3',
            'Data4',
            'Data5',
            'Data6',
            'Data7',
            'Data8',
            'Data9',
            'Data10'
          ]
        },
        yAxis: {
          title: {
            text: 'Data'
          },
          labels: {
            formatter: function () {
              return this.value
            }
          }
        },
        tooltip: {
          crosshairs: true,
          shared: true
        },
        credits: {
          enabled: false
        },
        plotOptions: {
          spline: {
            marker: {
              radius: 4,
              lineColor: '#666666',
              lineWidth: 1
            }
          }
        },
        series: []
      }
    }
  },
  mounted () {
    this.update()
    this.timer = setInterval(() => {
      this.update()
    }, 10000)
  },
  beforeRouteLeave (to, from, next) {
    clearInterval(this.timer)
    this.timer = null
    next()
  },
  methods: {
    update () {
      this.$http({
        method: 'get',
        url: '/api/data'
      }).then((response) => {
        let lineCharts = this.$refs.lineCharts
        if (lineCharts) {
          lineCharts.delegateMethod('showLoading', 'Loading...')
          lineCharts.removeSeries()
          if (this.showLast) {
            this.lastData.data = this.currentData.data
            lineCharts.addSeries(this.lastData)
          } else {
            this.showLast = true
          }
          this.currentData.data = response.data.data.values
          lineCharts.addSeries(this.currentData)
          lineCharts.hideLoading()
        }
      })
    },
    save () {
      this.$http.post('/api/save-data', {
        data: this.currentData.data
      }).then((response) => {
        console.log(response.data)
      })
    }
  }
}
</script>

<style scoped lang="stylus">
.save
  color blue
  cursor pointer
</style>
