import sublime
import sublime_plugin


class FindInUnfoldedTextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        folded_regions = self.view.folded_regions()
        self.view.sel().clear()
        self.view.sel().add_all(folded_regions)
        self.view.run_command('invert_selection')
        self.view.window().run_command('show_panel', { "panel": "find", "reverse": False, "in_selection": True })