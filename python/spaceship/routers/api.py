from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get("/matrix-multiply")
def multiply_matrices():
    m_a = np.random.rand(10, 10)
    m_b = np.random.rand(10, 10)
    prod = np.dot(m_a, m_b)

    return {
        "matrix_a": m_a.tolist(),
        "matrix_b": m_b.tolist(),
        "product": prod.tolist()
    }
