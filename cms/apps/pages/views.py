"""Views used by the pages app."""

from cms.views import CacheMixin
from django.contrib.contenttypes.models import ContentType
from django.views.generic import TemplateView


class ContentIndexView(CacheMixin, TemplateView):

    """Displays the index page for a page."""

    def get_template_names(self):
        """Returns the list of template names."""
        content_cls = ContentType.objects.get_for_model(self.request.pages.current.content).model_class()
        params = {
            "model_name": content_cls.__name__.lower(),
            "app_label": content_cls._meta.app_label,
        }

        return (
            "{app_label}/{model_name}.html".format(**params),
            "{app_label}/base.html".format(**params),
            "base.html",
        )
