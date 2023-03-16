from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class BasePageNumberPagination(PageNumberPagination):
    page_size = 7
    page_query_param = "page"
    max_page_size = 1000
    page_size_query_param = "page_size"
