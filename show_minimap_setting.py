
import sublime
import sublime_plugin

"""
Put this in your user packages:
```
mv ~/Downloads/show_minimap_setting.py ~/Library/Application\ Support/Sublime\ Text/Packages/User
```
Then add the setting to Preferences.sublime-settings:
```
{
  "show_minimap": false
}
```
I find you have to exit and restart Sublime to load the updated settings.
@see https://docs.sublimetext.io/guide/extensibility/plugins
@see https://forum.sublimetext.com/t/disable-minimap-preference/57770/4
"""
class ShowMinimapSetting(sublime_plugin.EventListener):
	def on_activated(self, view):
		show_minimap = view.settings().get("show_minimap")
		if isinstance(show_minimap, bool):
			view.window().set_minimap_visible(show_minimap)