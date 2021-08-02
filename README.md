# Wagtail-Icon-Picker

Introducing panels for selecting icons in Wagtail.

![Screen1](https://repository-images.githubusercontent.com/391852625/b04bc99e-321f-40b6-a9ce-ffe2308d3a18)


## Features

- BootstrapIconPickerPanel, BoxiconsPickerPanel, FontAwesomeIconPickerPanel, IcofontIconPickerPanel can be used in your edit handler
- BootstrapIconPickerBlock, FontAwesomeIconPickerBlock, BoxIconPickerBlock, IcofontPickerBlock for usage in a StreamField
- Includes Bootstrap Icons, FontAwesome, Boxicons & Icofont icons libraries
- A custom db field for improved validation


## Example

```python
from wagtail.core.models import Page

from wagtail_icon_picker.fields import IconField
from wagtail_icon_picker.edit_handlers import IcofontIconPickerPanel


class MyPage(Page):
    icon = IconField()

    content_panels = Page.content_panels + [
        IcofontIconPickerPanel('icon'),
    ]
```


## Documentation

- [Getting started](./docs/1_getting_started.md)
- [Adding panel to a Page](./docs/2_adding_to_a_page.md)
- [Adding to a StreamField](./docs/3_adding_to_a_streamfield.md)
- [Reference](./docs/4_reference.md)

## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtail-Icon-Picker is released under the [MIT License](http://www.opensource.org/licenses/MIT).
