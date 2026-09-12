---
schema: qual/card@1
id: E-SMI-8000E-CY2
kind: problem
title: Disjoint cycles commute
classification:
  areas:
  - algebra
  topics:
  - Symmetric Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the statement with Smith 8000e cycles problem 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Checked the two products pointwise on the support of each cycle and outside both supports."
---

::: {.exercise}
Prove disjoint cycles commute — i.e. if no $a_i$ equals any $b_j$, then

$$
(a_1 a_2 \ldots a_r)(b_1 b_2 \ldots b_s) = (b_1 b_2 \ldots b_s)(a_1 a_2 \ldots a_r).
$$
:::

::: solution
Put
$$
\sigma=(a_1\,a_2\,\ldots\,a_r),
\qquad
\tau=(b_1\,b_2\,\ldots\,b_s).
$$
By hypothesis the supports of $\sigma$ and $\tau$ are disjoint.

<1>1. The two products agree on the support of $\sigma$.
::: proof
If $x=a_i$ for some $i$, then $x$ does not lie in the support of $\tau$, so
$$
\tau(x)=x.
$$
Also $\sigma(x)$ is another $a_j$, hence is again outside the support of
$\tau$. Therefore
$$
(\sigma\tau)(x)=\sigma(x)
$$
and
$$
(\tau\sigma)(x)=\tau(\sigma(x))=\sigma(x).
$$
Thus the products agree on every $a_i$.
:::

<1>2. The two products agree on the support of $\tau$.
::: proof
If $x=b_j$, then $\sigma(x)=x$, and $\tau(x)$ is another point in the
support of $\tau$, hence still outside the support of $\sigma$. Consequently
$$
(\sigma\tau)(x)=\sigma(\tau(x))=\tau(x)
$$
and
$$
(\tau\sigma)(x)=\tau(x).
$$
:::

<1>3. The two products agree outside both supports.
::: proof
If $x$ lies in neither support, then both cycles fix it. Hence
$$
(\sigma\tau)(x)=x=(\tau\sigma)(x).
$$
:::

<1>4. Conclude that the cycles commute.
::: proof
Every point belongs to one of the three cases above, so the permutations
$\sigma\tau$ and $\tau\sigma$ agree everywhere. Thus
$$
\boxed{
(a_1\,\ldots\,a_r)(b_1\,\ldots\,b_s)
=(b_1\,\ldots\,b_s)(a_1\,\ldots\,a_r).}
$$
:::
:::
