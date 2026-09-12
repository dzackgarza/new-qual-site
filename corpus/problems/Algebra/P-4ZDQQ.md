---
schema: qual/card@1
id: P-4ZDQQ
kind: problem
title: Possible Galois groups of an abelian extension of degree $540$, and quadratic
  intermediate extensions $L/E$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Abelian Groups
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
- If $L/k$ is an abelian Galois extension of degree $540 = 2^2 \times 3^3\times 5$, what are the possible Galois groups $\Gal(L/k)$?

  - Are there any intermediate fields $E$ for which $L/E$ is a quadratic extension?
:::


::: {.solution}
Let
\[
G=\operatorname{Gal}(L/k).
\]
Since $L/k$ is abelian Galois and $[L:k]=540$, $G$ is a finite abelian group of order
\[
540=2^2 3^3 5.
\]

<1>1. The possible primary components are
\[
G_{(2)}\cong C_4\quad\text{or}\quad C_2\oplus C_2,
\]
\[
G_{(3)}\cong C_{27},\quad C_9\oplus C_3,\quad\text{or}\quad C_3\oplus C_3\oplus C_3,
\]
and
\[
G_{(5)}\cong C_5.
\]
::: {.proof}
These are exactly the abelian groups corresponding to the partitions of the exponents $2$, $3$, and $1$ in the primary decomposition theorem.
:::

<1>2. Hence there are exactly six possible Galois groups.
::: {.proof}
The $2$-primary and $3$-primary choices are independent, while the $5$-primary part is forced. Thus there are
\[
2\cdot3\cdot1=6
\]
isomorphism classes. In invariant-factor form they are
\[
C_{540},
\qquad C_3\oplus C_{180},
\qquad C_3\oplus C_3\oplus C_{60},
\]
\[
C_2\oplus C_{270},
\qquad C_6\oplus C_{90},
\qquad C_3\oplus C_6\oplus C_{30}.
\]
:::

<1>3. An intermediate field $E$ satisfies $[L:E]=2$ exactly when the corresponding subgroup $\operatorname{Gal}(L/E)\le G$ has order $2$.
::: {.proof}
By the fundamental theorem of Galois theory,
\[
[L:E]=|\operatorname{Gal}(L/E)|.
\]
Thus quadratic extensions $L/E$ correspond precisely to order-$2$ subgroups of $G$.
:::

<1>4. Such intermediate fields always exist.
::: {.proof}
Since $2\mid |G|$, Cauchy's theorem gives an element of order $2$, hence a subgroup of order $2$. By <1>3 this subgroup corresponds to an intermediate field $E$ with $[L:E]=2$.
:::

<1>5. The number of such fields is determined by the $2$-primary part.
::: {.proof}
If $G_{(2)}\cong C_4$, there is a unique subgroup of order $2$, hence exactly one such $E$. If $G_{(2)}\cong C_2\oplus C_2$, its three nonzero elements generate three distinct order-$2$ subgroups, hence there are exactly three such fields. In every case
\[
[E:k]=[L:k]/2=270.
\]
:::
:::
