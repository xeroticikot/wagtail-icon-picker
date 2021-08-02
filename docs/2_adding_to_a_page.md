# Adding panel to a page

### First create a page

```python
from wagtail.core.models import Page

class MyPage(Page):
    ...
```


### Create a field that represents your data

Define a IconField that represents your icon type, in this example we call it `icon`.

```python
from wagtail.core.models import Page
from wagtail_icon_picker.fields import IconField

class MyPage(Page):
    icon = IconField()
```

Note: IconField is built on top of CharField, so its also possible to use `CharField(max_length=7, default="bi-alarm")`.`


### Add a content panel to represent the field in the admin

```python
from wagtail.core.models import Page
from wagtail_icon_picker.edit_handlers import BoxiconsPickerPanel


class MyPage(Page):
    icon = IconField(default="bx-mask")

    content_panels = Page.content_panels + [
        BoxiconsPickerPanel('icon'),
    ]
```

We're done! After migration an icon picker should appear.


### Full example

```python
from wagtail.core.models import Page

from wagtail_icon_picker.fields import IconField
from wagtail_icon_picker.edit_handlers import BoxiconsPickerPanel


class MyPage(Page):
    icon = IconField()

    content_panels = Page.content_panels + [
        BoxiconsPickerPanel('icon'),
    ]
```
