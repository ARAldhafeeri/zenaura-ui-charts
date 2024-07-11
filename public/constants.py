bar_chart_code = """
from zenaura.client.mutator import mutator
from zenaura.ui.charts import ChartThis, Canvas
from zenaura.client.component import Component

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

class Chart(Component):
  def __init__(self):
    self.chart_name = "barchart"

  @mutator
  async def attached(self):
    ChartThis(config, self.chart_name)

    
  def render(self):
    return  Canvas(self.chart_name)

"""

line_chart_code = """
from zenaura.client.mutator import mutator
from zenaura.ui.charts import ChartThis, Canvas
from zenaura.client.component import Component

# Data for the chart
labels = ["January", "February", "March", "April", "May", "June", "July"]
data = {
    "labels": labels,
    "datasets": [{
        "label": "My First Dataset",
        "backgroundColor": "rgba(75, 192, 192, 0.2)",
        "borderColor": "rgb(75, 192, 192)",
        "data": [65, 59, 80, 81, 56, 55, 40],
    }]
}

# Configuration options
config = {
    "type": "line",
    "data": data,
    "options": {}
}

class Chart(Component):
  def __init__(self):
    self.chart_name = "linechart"

  @mutator
  async def attached(self):
    ChartThis(config, self.chart_name)

    
  def render(self):
    return Canvas(self.chart_name)

"""

bubble_chart_code = """
from zenaura.client.mutator import mutator
from zenaura.ui.charts import ChartThis, Canvas
from zenaura.client.component import Component

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

class Chart(Component):
  def __init__(self):
    self.chart_name = "bubble_chart"

  @mutator
  async def attached(self):
    ChartThis(config, self.chart_name)

    
  def render(self):
    return Canvas(self.chart_name)

"""


doughnut_chart_code = """
from zenaura.client.mutator import mutator
from zenaura.ui.charts import ChartThis, Canvas
from zenaura.client.component import Component

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

class Chart(Component):
  def __init__(self):
    self.chart_name = "dougnut"

  @mutator
  async def attached(self):
    ChartThis(config, self.chart_name)

    
  def render(self):
    return Canvas(self.chart_name)

"""

pie_chart_code = """
from zenaura.client.mutator import mutator
from zenaura.ui.charts import ChartThis, Canvas
from zenaura.client.component import Component

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
    "type": "pie",
    "data": data,
    "options": {}
}

class Chart(Component):
  def __init__(self):
    self.chart_name = "pie"

  @mutator
  async def attached(self):
    ChartThis(config, self.chart_name)

    
  def render(self):
    return Canvas(self.chart_name)

"""

area_chart_code = """
from zenaura.client.mutator import mutator
from zenaura.ui.charts import ChartThis, Canvas
from zenaura.client.component import Component

# Data for the chart
labels = ["January", "February", "March", "April", "May", "June", "July"]
data = {
    "labels": labels,
    "datasets": [{
        "label": "My First Dataset",
        "backgroundColor": "rgba(75, 192, 192, 0.2)",
        "borderColor": "rgb(75, 192, 192)",
        "data": [65, 59, 80, 81, 56, 55, 40],
        "fill": True
    }]
}

# Configuration options
config = {
    "type": "line",
    "data": data,
    "options": {}
}
class Chart(Component):
  def __init__(self):
    self.chart_name = "area"

  @mutator
  async def attached(self):
    ChartThis(config, self.chart_name)

    
  def render(self):
    return Canvas(self.chart_name)

"""

scatter_chart_code = """
from zenaura.client.mutator import mutator
from zenaura.ui.charts import ChartThis, Canvas
from zenaura.client.component import Component

# Data for the chart
labels = ["January", "February", "March", "April", "May", "June", "July"]
data = {
    "labels": labels,
    "datasets": [{
        "label": "My First Dataset",
        "backgroundColor": "rgba(75, 192, 192, 0.2)",
        "borderColor": "rgb(75, 192, 192)",
        "data": [65, 59, 80, 81, 56, 55, 40],
        "fill": True
    }]
}

# Configuration options
config = {
    "type": "line",
    "data": data,
    "options": {}
}
class Chart(Component):
  def __init__(self):
    self.chart_name = "scatter"

  @mutator
  async def attached(self):
    ChartThis(config, self.chart_name)

    
  def render(self):
    return Canvas(self.chart_name)

"""