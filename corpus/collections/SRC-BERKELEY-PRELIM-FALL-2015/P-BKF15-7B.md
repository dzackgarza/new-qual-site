---
schema: qual/card@1
id: P-BKF15-7B
kind: problem
title: Order of $\operatorname{GL}_n(\mathbb F_2)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2015 solution packet: the count
    is the number of ordered bases of an n-dimensional vector space over
    F_2.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked equivalence of surjectivity and invertibility and every factor
    in the sequential basis-vector count.
---

::: {.problem}
Find the number of surjective linear maps from an $n$-dimensional vector space over the field with $2$ elements to itself.
:::

::: {.solution}
Let $V$ be an $n$-dimensional vector space over $\FF_2$, and fix a
basis
$$
e_1,\ldots,e_n.
$$

<1>1. A linear map
$$
T:V\to V
$$
is surjective if and only if
$$
T(e_1),\ldots,T(e_n)
$$
is a basis of $V$.

::: {.proof}
The image of $T$ is the span of the images of a basis:
$$
\operatorname{im}T
=
\operatorname{span}
\{T(e_1),\ldots,T(e_n)\}.
$$
Thus $T$ is surjective exactly when these $n$ vectors span $V$.
Since $V$ has dimension $n$, a spanning family of $n$ vectors is a
basis.
:::

<1>2. There are
$$
2^n-1
$$
choices for $T(e_1)$ in a surjective map.

::: {.proof}
The first image vector must be nonzero. The vector space $V$ has
$2^n$ elements, exactly one of which is $0$.
:::

<1>3. After linearly independent vectors
$$
T(e_1),\ldots,T(e_j)
$$
have been chosen, with $0\le j<n$, there are
$$
2^n-2^j
$$
choices for $T(e_{j+1})$.

::: {.proof}
The span
$$
\operatorname{span}
\{T(e_1),\ldots,T(e_j)\}
$$
has dimension $j$, hence contains exactly $2^j$ vectors. The next
image vector must lie outside this span in order to preserve linear
independence. Since $V$ has $2^n$ vectors, there are
$$
2^n-2^j
$$
choices.
:::

<1>4. The number of surjective linear maps $V\to V$ is
$$
\boxed{
\prod_{j=0}^{n-1}(2^n-2^j)
=
(2^n-1)(2^n-2)\cdots(2^n-2^{n-1}).
}
$$

::: {.proof}
By step <1>1, choosing a surjective linear map is equivalent to
choosing an ordered basis
$$
T(e_1),\ldots,T(e_n).
$$
Step <1>2 gives the first factor, and step <1>3 gives each subsequent
factor. The choices are sequential and independent once the preceding
vectors have been fixed, so multiplication gives the displayed
product.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required count.
:::
:::
