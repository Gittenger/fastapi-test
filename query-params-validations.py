from enum import Enum

from typing import Union
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

# multiple validations, incl. regex
#
# @app.get("/items/")
# async def read_items(q: str | None = Query(default=None, min_length=3,  max_length=50, regex='^fixedquery$')):
#     results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# set default value
#


@app.get("/items/")
async def read_items(q: str | None = Query(default="fixedquery", min_length=3)):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results

# required field with ellipsis
# @app.get("/items/")
# async def read_items(q: str = Query(default=..., min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# typed list of queries with default
#
# @app.get("/items/")
# async def read_items(q: List[str] = Query(default=["foo", "bar"])):
#     query_items = {"q": q}
#     return query_items

# add metadata for openAPI tools and features such as auto-gen docs
#
# @app.get("/items/")
# async def read_items(
#     q: str
#     | None = Query(
#         default=None,
#         title="Query string",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3,
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# alias incoming query "item-query" as valid python variable name "q"
@app.get("/items/")
async def read_items(q: str | None = Query(default=None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# show as deprecated, or mark as excluded from openAPI
# @app.get("/items/")
# async def read_items(
#     q: str
#     | None = Query(
#         default=None,
#         alias="item-query",
#         title="Query string",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3,
#         max_length=50,
# 			 regex="^fixedquery$",
# *		 include_in_schema=False,
# !		 deprecated=True,
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
