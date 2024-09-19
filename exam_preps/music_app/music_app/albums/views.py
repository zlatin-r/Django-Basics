from django.urls import reverse_lazy
from django.views import generic as views

from music_app.albums.models import Album


class AlbumFormViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        # Can be moved a mixin
        form.fields["name"].widget.attrs["placeholder"] = "Album Name"
        form.fields["artist_name"].widget.attrs["placeholder"] = "Artist"
        form.fields["description"].widget.attrs["placeholder"] = "Description"
        form.fields["image_url"].widget.attrs["placeholder"] = "Image URL"
        form.fields["price"].widget.attrs["placeholder"] = "Price"

        return form


class CreateAlbumView(AlbumFormViewMixin, views.CreateView):
    queryset = Album.objects.all()
    fields = ("name", "artist_name", "genre", "description", "image_url", "price")
    template_name = "albums/album-add.html"
    success_url = reverse_lazy("index")
