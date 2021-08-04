from django.forms import widgets, Media
from django.utils.safestring import mark_safe
from wagtail.admin.versioned_staticfiles import versioned_static


class BootstrapIconsInputWidget(widgets.TextInput):
    class Media:
        css = {
            "all": (
                'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.0/font/bootstrap-icons.css',
                versioned_static("wagtail_icon_picker/css/icon-picker-widget.css"),
            )
        }

        js = versioned_static("wagtail_icon_picker/iconpicker.js",)

    def render(self, name, value, attrs=None, renderer=None):
        out = super().render(name, value, attrs, renderer=renderer)
        field_id = attrs["id"]

        return mark_safe(
            out
            + """
            <script>
            (async () => {
                const response = await fetch('__ICONS_JSON__')
                const result = await response.json()
                const exValue = document.getElementById("{{ widget_id }}").value?document.getElementById("{{ widget_id }}").value.slice(3):'bi-alarm';

                const iconpicker = new Iconpicker(document.querySelector("#{{ widget_id }}"), {
                    icons: result,
                    showSelectedIn: document.querySelector("#{{ widget_id }}-icon"),
                    searchable: true,
                    selectedClass: "selected",
                    containerClass: "my-picker",
                    hideOnSelect: true,
                    fade: true,
                    defaultValue: exValue,
                    valueFormat: val => `bi ${val}`
                });

                iconpicker.set() // Set as empty
                iconpicker.set('bi-alarm') // Reset with a value
            })();
            </script>
            """.replace(
                "__ICONS_JSON__", versioned_static("wagtail_icon_picker/iconsets/bootstrap5.json",)
            )
        )


class BootstrapIconPickerWidget(widgets.TextInput):
    template_name = "wagtail_icon_picker/widgets/bootstrap-icon-picker-widget.html"

    def __init__(self, attrs=None):
        default_attrs = {
            "class": "icon-picker-widget__text-input",
        }
        attrs = attrs or {}
        attrs = {**default_attrs, **attrs}
        super().__init__(attrs=attrs)

    @property
    def media(self):
        return Media(
            css={
                "all": [
                    'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.0/font/bootstrap-icons.css',
                    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
                    versioned_static("wagtail_icon_picker/css/icon-picker-widget.css"),
                ]
            },
            js=[versioned_static("wagtail_icon_picker/iconpicker.js", )]
        )


class FontAwesomeIconsInputWidget(widgets.TextInput):
    class Media:
        css = {
            "all": (
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
                versioned_static("wagtail_icon_picker/css/icon-picker-widget.css"),
            )
        }

        js = versioned_static("wagtail_icon_picker/iconpicker.js", )

    def render(self, name, value, attrs=None, renderer=None):
        out = super().render(name, value, attrs, renderer=renderer)
        field_id = attrs["id"]

        return mark_safe(
            out
            + """
            <script>
            (async () => {
                const response = await fetch('__ICONS_JSON__')
                const result = await response.json()
                const exValue = document.getElementById("{{ widget_id }}").value?document.getElementById("{{ widget_id }}").value.slice(3):'fa-bars';

                const iconpicker = new Iconpicker(document.querySelector("#{{ widget_id }}"), {
                    icons: result,
                    showSelectedIn: document.querySelector("#{{ widget_id }}-icon"),
                    searchable: true,
                    selectedClass: "selected",
                    containerClass: "my-picker",
                    hideOnSelect: true,
                    fade: true,
                    defaultValue: exValue,
                    valueFormat: val => `fa ${val}`
                });

                iconpicker.set() // Set as empty
                iconpicker.set('bi-alarm') // Reset with a value
            })();
            </script>
            """.replace(
                "__ICONS_JSON__", versioned_static("wagtail_icon_picker/iconsets/fontawesome4.json", )
            )
        )


class FontAwesomeIconPickerWidget(widgets.TextInput):
    template_name = "wagtail_icon_picker/widgets/font-awesome-icon-picker-widget.html"

    def __init__(self, attrs=None):
        default_attrs = {
            "class": "icon-picker-widget__text-input",
        }
        attrs = attrs or {}
        attrs = {**default_attrs, **attrs}
        super().__init__(attrs=attrs)

    @property
    def media(self):
        return Media(
            css={
                "all": [
                    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
                    versioned_static("wagtail_icon_picker/css/icon-picker-widget.css"),
                ]
            },
            js=[versioned_static("wagtail_icon_picker/iconpicker.js", )]
        )


class BoxIconsInputWidget(widgets.TextInput):
    class Media:
        css = {
            "all": (
                'https://unpkg.com/boxicons@2.0.9/css/boxicons.min.css',
                versioned_static("wagtail_icon_picker/css/icon-picker-widget.css"),
            )
        }

        js = versioned_static("wagtail_icon_picker/iconpicker.js", )

    def render(self, name, value, attrs=None, renderer=None):
        out = super().render(name, value, attrs, renderer=renderer)
        field_id = attrs["id"]

        return mark_safe(
            out
            + """
            <script>
            (async () => {
                const response = await fetch('__ICONS_JSON__')
                const result = await response.json()
                const exValue = document.getElementById("{{ widget_id }}").value?document.getElementById("{{ widget_id }}").value.slice(3):'bx-mask';

                const iconpicker = new Iconpicker(document.querySelector("#{{ widget_id }}"), {
                    icons: result,
                    showSelectedIn: document.querySelector("#{{ widget_id }}-icon"),
                    searchable: true,
                    selectedClass: "selected",
                    containerClass: "my-picker",
                    hideOnSelect: true,
                    fade: true,
                    defaultValue: exValue,
                    valueFormat: val => `bx ${val}`
                });

                iconpicker.set() // Set as empty
                iconpicker.set('bx-mask') // Reset with a value
            })();
            </script>
            """.replace(
                "__ICONS_JSON__", versioned_static("wagtail_icon_picker/iconsets/boxicons.json", )
            )
        )


class BoxIconPickerWidget(widgets.TextInput):
    template_name = "wagtail_icon_picker/widgets/box-icons-picker-widget.html"

    def __init__(self, attrs=None):
        default_attrs = {
            "class": "icon-picker-widget__text-input",
        }
        attrs = attrs or {}
        attrs = {**default_attrs, **attrs}
        super().__init__(attrs=attrs)

    @property
    def media(self):
        return Media(
            css={
                "all": [
                    'https://unpkg.com/boxicons@2.0.9/css/boxicons.min.css',
                    versioned_static("wagtail_icon_picker/css/icon-picker-widget.css"),
                ]
            },
            js=[versioned_static("wagtail_icon_picker/iconpicker.js", )]
        )


class IcofontInputWidget(widgets.TextInput):
    class Media:
        css = {
            "all": (
                versioned_static("wagtail_icon_picker/css/icofont/icofont.min.css"),
                versioned_static("wagtail_icon_picker/css/icon-picker-widget.css"),
            )
        }

        js = versioned_static("wagtail_icon_picker/iconpicker.js", )

    def render(self, name, value, attrs=None, renderer=None):
        out = super().render(name, value, attrs, renderer=renderer)
        field_id = attrs["id"]

        return mark_safe(
            out
            + """
            <script>
            (async () => {
                const response = await fetch('__ICONS_JSON__')
                const result = await response.json()
                const exValue = document.getElementById("{{ widget_id }}").value?document.getElementById("{{ widget_id }}").value:'icofont-tree';

                const iconpicker = new Iconpicker(document.querySelector("#{{ widget_id }}"), {
                    icons: result,
                    showSelectedIn: document.querySelector("#{{ widget_id }}-icon"),
                    searchable: true,
                    selectedClass: "selected",
                    containerClass: "my-picker",
                    hideOnSelect: true,
                    fade: true,
                    defaultValue: exValue,
                    valueFormat: val => `${val}`
                });

                iconpicker.set() // Set as empty
                iconpicker.set('icofont-tree') // Reset with a value
            })();
            </script>
            """.replace(
                "__ICONS_JSON__", versioned_static("wagtail_icon_picker/iconsets/icofont.json", )
            )
        )


class IcofontPickerWidget(widgets.TextInput):
    template_name = "wagtail_icon_picker/widgets/icofont-picker-widget.html"

    def __init__(self, attrs=None):
        default_attrs = {
            "class": "icon-picker-widget__text-input",
        }
        attrs = attrs or {}
        attrs = {**default_attrs, **attrs}
        super().__init__(attrs=attrs)

    @property
    def media(self):
        return Media(
            css={
                "all": [
                    versioned_static("wagtail_icon_picker/css/icofont/icofont.min.css"),
                    versioned_static("wagtail_icon_picker/css/icon-picker-widget.css"),
                ]
            },
            js=[versioned_static("wagtail_icon_picker/iconpicker.js", )]
        )
