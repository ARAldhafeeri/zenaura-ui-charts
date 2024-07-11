from public.components.common import *
from zenaura.client.component import Component
from public.constants import bubble_chart_code 
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class
from public.utils import ChartThis, Canvas

# Data for the chart
data = {
    "datasets": [{
        "label": "My First Dataset",
        "backgroundColor": "rgba(255, 99, 132, 0.2)",
        "borderColor": "rgb(255, 99, 132)",
        "data": [
            {"x": 20, "y": 30, "r": 15},
            {"x": 40, "y": 10, "r": 10},
            {"x": 15, "y": 20, "r": 25},
            {"x": 35, "y": 40, "r": 30},
            {"x": 50, "y": 50, "r": 20}
        ],
    }]
}

# Configuration options
config = {
    "type": "bubble",
    "data": data,
    "options": {}
}

class BubbleChart(Component):
  def __init__(self):
    self.active_tab = "1"
    self.chart_name = "bubblechart"

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
        "Bubble",
        "Displays a bubble chart from config",
        "https://araldhafeeri.github.io/Zenaura/api/ui/badge/",
        chart,
        bubble_chart_code,
        self.active_tab,
        "bubble.toggle_tabs"
      )
    ])
