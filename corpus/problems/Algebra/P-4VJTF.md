---
schema: qual/card@1
id: P-4VJTF
kind: problem
title: Centers of $\GL_n(\FF_p)$ and $\SL_n(\FF_p)$ are scalar matrices
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Centralizers and Normalizers
  - Finite Fields
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
- Let $\FF_p$ be the finite field with $p$ elements, where $p$ is a prime.
  Show that the centers of $\GL_n(\FF_p)$ and $\SL_n(\FF_p)$ consist only of scalar matrices.

  - Show that the scalars $\zeta$ that appear in scalar matrices $Z(\SL_n(\FF_p))$ are roots of unity in $\FF_p$, i.e. $\zeta^p = 1$.
:::

::: {.solution}
For $i\neq j$ let $e_{ij}$ be the matrix unit and $T_{ij}=I_n+e_{ij}$, a transvection with $\det T_{ij}=1$, so $T_{ij}\in\SL_n(\FF_p)\subseteq\GL_n(\FF_p)$.

<1>1. A matrix $A=(a_{k\ell})$ commuting with every $T_{ij}$ is scalar.

::: {.proof}
$AT_{ij}=T_{ij}A$ gives $Ae_{ij}=e_{ij}A$.
The $(k,\ell)$ entries are $a_{ki}\delta_{j\ell}$ and $\delta_{ki}a_{j\ell}$.
Taking $\ell=j$ and $k\neq i$ gives $a_{ki}=0$; taking $k=i$, $\ell=j$ gives $a_{ii}=a_{jj}$.
As $i\neq j$ vary, $A$ is diagonal with equal diagonal entries.
:::

<1>2. $Z(\GL_n(\FF_p))=\{\lambda I_n:\lambda\in\FF_p^\times\}$.

::: {.proof}
A central element commutes with every $T_{ij}$, so it is scalar by step <1>1, and every invertible scalar matrix is central.
:::

<1>3. $Z(\SL_n(\FF_p))=\{\zeta I_n:\zeta\in\FF_p,\ \zeta^n=1\}\cong\ZZ/\gcd(n,p-1)\ZZ$.

::: {.proof}
A central element of $\SL_n(\FF_p)$ commutes with every $T_{ij}\in\SL_n(\FF_p)$, so it is scalar by step <1>1; the scalar matrix $\zeta I_n$ lies in $\SL_n(\FF_p)$ exactly when $\det(\zeta I_n)=\zeta^n=1$, and it is then central.
The solutions of $\zeta^n=1$ in the cyclic group $\FF_p^\times$ of order $p-1$ form its subgroup of order $\gcd(n,p-1)$.
:::
:::

::: {.remark}
The scalars in $Z(\SL_n(\FF_p))$ are the $n$th roots of unity in $\FF_p$, $\zeta^n=1$. The condition $\zeta^p=1$ in the statement holds only for $\zeta=1$, since $\zeta^p=\zeta$ for every $\zeta\in\FF_p$.
:::
