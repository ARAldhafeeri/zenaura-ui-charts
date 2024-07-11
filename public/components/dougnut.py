from public.components.common import *
from zenaura.client.component import Component
from public.constants import doughnut_chart_code 
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class
from public.utils import ChartThis, Canvas

# Data for the chart
data = {
    "labels": ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    "datasets": [{
        "label": "My First Dataset",
        "data": [300, 50, 100, 40, 120, 75],
        "backgroundColor": [
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)"
        ],
        "borderColor": [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)"
        ],
        "borderWidth": 1
    }]
}

# Configuration options
config = {
    "type": "doughnut",
    "data": data,
    "options": {}
}

class DoughnutChart(Component):
  def __init__(self):
    self.active_tab = "1"
    self.chart_name = "doughnutchart"

  @mutator
  async def toggle_tabs(self, _):
    self.active_tab = "2" if self.active_tab == "1" else "1"

  @mutator
  async def attached(self):
    ChartThis(config, self.chart_name)

  def render(self):
    chart = Canvas(self.chart_name)
    return Div(main_content, [
      StyledComponentPresentation(
        "Doughnut",
        "Displays a doughnut chart from config",
        "https://araldhafeeri.github.io/Zenaura/api/ui/badge/",
        chart,
        doughnut_chart_code,
        self.active_tab,
        "doughnut.toggle_tabs"
      )
    ])
