"""Models used by the feeds application."""


from django.db import models

from cms.apps.pages.models import PageBase, HtmlField


class ArticleBase(PageBase):
    
    """Base class for feed articles."""
    
    content = HtmlField(blank=True)
    
    summary = HtmlField(blank=True,
                        help_text="A short summary of this article.  If not specified, then a summarized version of the content will be used.")
    
    is_featured = models.BooleanField("featured",
                                      default=False,
                                      db_index=True,
                                      help_text="Featured articles will remain at the top of any news feeds.")
    
    def get_absolute_url(self):
        """Returns the absolute URL of the article."""
        return self.feed.content.reverse("article_detail", self.publication_date.year, self.publication_date.month, self.url_title)
    
    class Meta:
        abstract = True
        unique_together = (("feed", "url_title",),)
        
        