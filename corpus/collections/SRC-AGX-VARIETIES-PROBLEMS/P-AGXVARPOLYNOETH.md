---
schema: qual/card@1
id: P-AGXVARPOLYNOETH
kind: problem
title: The polynomial ring on affine space is Noetherian
classification:
  areas:
  - algebraic-geometry
  topics:
  - Noetherian Rings
  - Hilbert Basis Theorem
  - Coordinate Rings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Theorem 1.6, Definition 1.7, and Example 1.8 in the
    recorded source. Example 1.8 states that the coordinate ring O(A^n) is
    Noetherian by the Hilbert Basis Theorem.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Replaced structure-sheaf-looking notation O_{A^n} by the source's global
    coordinate ring O(A^n)=k[x_1,...,x_n], and made the ground field explicit.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked that a field is Noetherian, iterated Hilbert basis theorem through
    n polynomial variables, and identified the result with the affine-space
    coordinate ring.
---

::: {.problem}
Let $k$ be a field. Show that
$$
\mco(\AA^n_k)
=
k[x_1,\ldots,x_n]
$$
is a Noetherian ring.
:::

::: {.solution}
<1>1. The field $k$ is Noetherian.

::: {.proof}
The only ideals of a field are
$$
(0)
\qquad\text{and}\qquad
(1)=k.
$$
Both are finitely generated, so every ideal of $k$ is finitely generated.
Thus $k$ is Noetherian.
:::

<1>2. For every integer $r$ with $0\leq r\leq n$, the polynomial ring
$$
k[x_1,\ldots,x_r]
$$
is Noetherian.

::: {.proof}
We argue by induction on $r$. The case $r=0$ is step <1>1.

Assume
$$
k[x_1,\ldots,x_r]
$$
is Noetherian. By the Hilbert basis theorem
[[T-YYLPH]], if a commutative ring $R$ is Noetherian, then
$$
R[x]
$$
is Noetherian. Applying it to
$$
R=k[x_1,\ldots,x_r]
$$
gives that
$$
k[x_1,\ldots,x_r][x_{r+1}]
=
k[x_1,\ldots,x_{r+1}]
$$
is Noetherian. This completes the induction.
:::

<1>3. The coordinate ring of affine $n$-space is Noetherian:
$$
\boxed{
\mco(\AA^n_k)=k[x_1,\ldots,x_n]
\text{ is Noetherian}.
}
$$

::: {.proof}
By definition,
$$
\mco(\AA^n_k)=k[x_1,\ldots,x_n].
$$
Step <1>2 with $r=n$ shows that this polynomial ring is Noetherian.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove the stated Noetherianity of the affine-space
coordinate ring.
:::
:::
