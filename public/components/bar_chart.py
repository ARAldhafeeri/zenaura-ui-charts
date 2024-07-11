from public.components.common import *
from zenaura.client.component import Component
from public.constants import bar_chart_code
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class
from public.utils import ChartThis, Canvas

# Data for the chart
labels = ["January", "February", "March", "April", "May", "June", "July"]
data = {
    "labels": labels,
    "datasets": [{
        "label": "My First Dataset",
        "backgroundColor": "rgba(255, 99, 132, 0.2)",
        "borderColor": "rgb(255, 99, 132)",
        "data": [65, 59, 80, 81, 56, 55, 40],
    }]
}

# Configuration options
config = {
    "type": "bar",
    "data": data,
    "options": {}
}

class BarChart(Component):
  def __init__(self):
    self.active_tab = "1"
    self.chart_name = "barchart"


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
        "Bar",
        "Displays a bar chart from config",
        "https://araldhafeeri.github.io/Zenaura/api/ui/badge/",
        chart,
        bar_chart_code,
        self.active_tab,
        "bar.toggle_tabs"
      )
    ])


