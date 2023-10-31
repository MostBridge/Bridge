from rest_framework import pagination


class Paginator(pagination.PageNumberPagination):
    """Пагинация на страницы."""

    page_size_query_param = "limit"
