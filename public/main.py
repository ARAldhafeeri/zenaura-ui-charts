import asyncio
from zenaura.client.app import Route, App, HistoryNode
from zenaura.client.page import Page
from public.routes import ClientRoutes
from zenaura.client.layout import Layout
from zenaura.client.dom import zenaura_dom
from public.styles import main_content
from public.routes import ClientRoutes
from public.components.sidebar import Sidebar
# styled charts in component page
from public.components.bar_chart import BarChart
from public.components.line_chart import LineChart
from public.components.bubble_chart import BubbleChart
from public.components.dougnut import DoughnutChart
from public.components.pie import PieChart
from public.components.area import AreaChart
from public.components.scatter import ScatterChart


try :
    from pyscript import window, document
except ImportError:
    from zenaura.client.mocks import MockWindow
    window = MockWindow()

event_loop = asyncio.get_event_loop()

import asyncio

router = App()

# Instantiate components
side_nav_bar = Sidebar(router)

# styled charts page
bar = BarChart()
line = LineChart()
bubble = BubbleChart()
dougnut = DoughnutChart()
pie = PieChart()
area = AreaChart() 
scatter = ScatterChart()

routes = [
  (
    "line chart",
    ClientRoutes.bar.value,
    Page([bar])
  ),
  (
    "line chart",
    ClientRoutes.line.value,
    Page([line])
  ),
  (
    "bubble chart",
    ClientRoutes.bubble.value,
    Page([bubble])
  ),
  (
    "donught chart",
    ClientRoutes.dougnut.value,
    Page([dougnut])
  ),
  (
    "pi chart",
    ClientRoutes.pie.value,
    Page([pie])
  ), 
  (
    "area chart",
    ClientRoutes.area.value,
    Page([area])
  ), 
  (
    "scatter chart",
    ClientRoutes.scatter.value,
    Page([scatter])
  )
]

for title, path, page in routes:
  router.add_route(Route(
      title=title,
      path=path,
      page=page
  ))

my_app_layout = Layout(
  top= [side_nav_bar], 
  routes=router.routes,
  bottom=[]
)


# sync layout component lifecycle methods
router.layout = my_app_layout

event_loop.run_until_complete(router.navigate(ClientRoutes.bar.value))

