from .common import *
from public.styles import with_theme_colors, with_theme_colors_text_no_hover, main_content
from zenaura.client.component import Component

class Sidebar(Component):
  def __init__(self, router):
    self.active_comp = "menu"
    self.router = router
		
  async def set_active_comp(self, event):
    await self.router.navigate("/" + event.target.name)
		
  def render(self):
    return SidebarPresentational()

nav_item_style = with_theme_colors("px-3 py-2 text-sm")
category_class_name = with_theme_colors_text_no_hover("mb-1 rounded-md px-2 py-1 text-md font-semibold")

def GeneralCharts():
	return [
		Header1("General Charts", category_class_name),
		NavItemTextNameFactory(
         "javascript:;", 
         "Bar", 
         nav_item_style,
        "side_nav_bar.set_active_comp",
		),
    NavItemTextNameFactory(
        "javascript:;", 
        "Line", 
        nav_item_style,
      "side_nav_bar.set_active_comp",
    ),
    NavItemTextNameFactory(
        "javascript:;", 
        "Bubble", 
        nav_item_style,
      "side_nav_bar.set_active_comp",
    ),
    NavItemTextNameFactory(
        "javascript:;", 
        "Dougnut", 
        nav_item_style,
      "side_nav_bar.set_active_comp",
    ),
    NavItemTextNameFactory(
        "javascript:;", 
        "Pie", 
        nav_item_style,
      "side_nav_bar.set_active_comp",
    ),
    NavItemTextNameFactory(
        "javascript:;", 
        "Area", 
        nav_item_style,
      "side_nav_bar.set_active_comp",
    ),

    NavItemTextNameFactory(
        "javascript:;", 
        "Scatter", 
        nav_item_style,
      "side_nav_bar.set_active_comp",
    )
	]

def SidebarPresentational():
  return Div(
    "flex flex-col float-left space-y-2 w-1/5 h-screen p-2 overflow-y-scroll bg-light-white dark:bg-dark-gray1", 
    # add more nav items here
    [
      # Navigation
      *GeneralCharts(),
    ]
  )


