from wagtail.admin.edit_handlers import FieldPanel

from wagtail_icon_picker.widgets import BoxIconPickerWidget, BootstrapIconPickerWidget, IcofontPickerWidget, \
    FontAwesomeIconPickerWidget, BoxIconsInputWidget, BootstrapIconsInputWidget, IcofontInputWidget, \
    FontAwesomeIconsInputWidget


class BootstrapIconPickerPanel(FieldPanel):
    def widget_overrides(self):
        return {
            self.field_name: BootstrapIconPickerWidget(),
        }


class BootstrapIconInputPanel(FieldPanel):
    def widget_overrides(self):
        return {
            self.field_name: BootstrapIconsInputWidget(),
        }


class BoxiconsPickerPanel(FieldPanel):
    def widget_overrides(self):
        return {
            self.field_name: BoxIconPickerWidget(),
        }


class BoxiconsInputPanel(FieldPanel):
    def widget_overrides(self):
        return {
            self.field_name: BoxIconsInputWidget(),
        }


class FontAwesomeIconPickerPanel(FieldPanel):
    def widget_overrides(self):
        return {
            self.field_name: FontAwesomeIconPickerWidget(),
        }


class FontAwesomeIconInputPanel(FieldPanel):
    def widget_overrides(self):
        return {
            self.field_name: FontAwesomeIconsInputWidget(),
        }


class IcofontIconPickerPanel(FieldPanel):
    def widget_overrides(self):
        return {
            self.field_name: IcofontPickerWidget(),
        }


class IcofontIconInputPanel(FieldPanel):
    def widget_overrides(self):
        return {
            self.field_name: IcofontInputWidget(),
        }
