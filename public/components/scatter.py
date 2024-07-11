from public.components.common import *
from zenaura.client.component import Component
from public.constants import scatter_chart_code
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class
from public.utils import ChartThis, Canvas

# Data for the chart
data = {
    "datasets": [{
        "label": "My First Dataset",
        "backgroundColor": "rgba(75, 192, 192, 0.2)",
        "borderColor": "rgb(75, 192, 192)",
        "data": [
            {"x": -10, "y": 0},
            {"x": 0, "y": 10},
            {"x": 10, "y": 5},
            {"x": 20, "y": 20},
            {"x": 30, "y": 10},
            {"x": 40, "y": 60}
        ],
    }]
}

# Configuration options
config = {
    "type": "scatter",
    "data": data,
    "options": {}
}

class ScatterChart(Component):
  def __init__(self):
    self.active_tab = "1"
    self.chart_name = "scatterchart"

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
        "Scatter",
        "Displays a scatter chart from config",
        "https://araldhafeeri.github.io/Zenaura/api/ui/badge/",
        chart,
        scatter_chart_code,
        self.active_tab,
        "scatter.toggle_tabs"
      )
    ])
