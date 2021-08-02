# Reference

## Panels

### BoxiconsPickerPanel

This panel uses the native `<input type="text"...` text input. You use it by adding it to your page `content_panels`.

#### How to use

```python
from wagtail.core.models import Page
from wagtail_icon_picker.edit_handlers import BoxiconsPickerPanel

class MyPage(Page):
    ...

    content_panels = Page.content_panels + [
        BoxiconsPickerPanel('my_icon_field'),
    ]
```


## Fields

### IconField

A field based on CharField , its built to be compatible with `<input type="text"`. You still needs to define a panel for icon selection.

#### How to use

```python
from wagtail.core.models import Page
from wagtail_icon_picker.fields import IconField

class MyPage(Page):
    my_icon_field = IconField()
```


## Blocks

### IcofontPickerBlock

This block uses the native `<input type="text"...` text input. You use it by adding it to your page stream field blocks.

#### How to use

```python
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail_icon_picker.blocks import IcofontPickerBlock


class MyStreamFieldPage(Page):
    body = StreamField([
        ('icon', IcofontPickerBlock(default="icofont-tree")),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
```
