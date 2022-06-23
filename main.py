from enum import Enum

from typing import Union
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()
