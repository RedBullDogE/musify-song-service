from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer
from elasticsearch_dsl.analysis import token_filter
from songs.models import Album, Artist, Song

# Filter for partial match searching, e.g.:
#   'tes' ---> tes, test, testing...
# Limiting min_gram to 3 means not matching small words like:
#   'I' -/-> icon, i love you...
edge_ngram_completion_filter = token_filter(
    "edge_ngram_completion_filter", type="edge_ngram", min_gram=3, max_gram=10
)


custom_analyzer = analyzer(
    "custom_analyzer",
    tokenizer="whitespace",
    filter=["lowercase", edge_ngram_completion_filter],
)


@registry.register_document
class SongDocument(Document):
    """
    ElasticSearch Song representation. Used for fast searching of songs.

    All original fields of related django model are used. Search is perform by
    title (name field), artist name and album title.
    """

    name = fields.TextField(analyzer=custom_analyzer)

    artist = fields.ObjectField(
        properties={
            "name": fields.TextField(analyzer=custom_analyzer),
            "description": fields.TextField(),
        }
    )

    album = fields.ObjectField(
        properties={"name": fields.TextField(analyzer=custom_analyzer)}
    )

    class Index:
        name = "songs"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Song

        fields = ["id", "genre", "pub_year", "popularity", "src"]

        related_models = [Artist, Album]

    def get_instances_from_related(self, artist):
        """
        Used to synchronizing update/delete of related songs in Django DB and ElasticSearch.
        """

        return artist.songs.all()


@registry.register_document
class AlbumDocument(Document):
    """
    ElasticSearch Album representation. Used for fast searching of albums.

    All original fields of related django model are used. Search is perform by title (name field)
    and artist name.
    """

    id = fields.TextField()

    name = fields.TextField(analyzer=custom_analyzer)

    artist = fields.ObjectField(
        properties={"name": fields.TextField(analyzer=custom_analyzer)}
    )

    def prepare_id(self, album):
        """
        Cast Album field of ID from UUID to string before migrating from Django DB to ElasticSearch index.
        """
        return str(album.id)

    class Index:
        name = "albums"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Album
        fields = ["genre", "pub_year", "cover", "description"]

        related_models = [Artist]

    def get_instances_from_related(self, artist):
        """
        Used to synchronizing update/delete of related albums in Django DB and ElasticSearch.
        """
        return artist.albums.all()


@registry.register_document
class ArtistDocument(Document):
    """
    ElasticSearch Artist representation. Used for fast searching of artists.

    All original fields of related django model are used. Search is perform by artist name.
    """

    id = fields.TextField()

    name = fields.TextField(analyzer=custom_analyzer)

    def prepare_id(self, artist):
        """
        Cast Artist field of ID from UUID to string before migrating from Django DB to ElasticSearch index.
        """
        return str(artist.id)

    class Index:
        name = "artists"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Artist
        fields = ["genre", "create_year", "picture", "description"]
