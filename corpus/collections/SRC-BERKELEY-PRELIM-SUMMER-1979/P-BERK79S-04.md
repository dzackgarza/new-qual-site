---
schema: qual/card@1
id: P-BERK79S-04
kind: problem
title: Automorphism group of a cyclic group of prime order
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Identified Aut(C_p) with F_p^× by sending an automorphism to the
    exponent of the image of a fixed generator. Proved the standard lemma
    that every finite subgroup of a field's multiplicative group is cyclic:
    if m is its exponent, all elements are roots of x^m-1, so the group
    order is at most m; Lagrange gives m dividing the group order, hence
    equality, and a commuting product of prime-power-order elements realizes
    the exponent.
---

::: {.problem}
Let $p$ be prime.
Prove that the automorphism group of a cyclic group of order $p$ is cyclic, and determine its order.
:::

::: {.solution}
Let
$$
C_p=\langle g\rangle.
$$

<1>1. Every automorphism of $C_p$ is uniquely determined by
$$
g\longmapsto g^a
$$
for some
$$
a\in\{1,\ldots,p-1\}.
$$

::: {.proof}
An automorphism is determined by the image of the generator $g$. Its image
must again generate $C_p$. Since $p$ is prime, every nonidentity element
$$
g^a,
\qquad
1\leq a\leq p-1,
$$
has order $p$ and hence is a generator. Conversely, assigning $g$ to any
such generator extends uniquely to an automorphism.
:::

<1>2. The map
$$
\Psi:\operatorname{Aut}(C_p)
\longrightarrow
\FF_p^\times
$$
defined by
$$
\Psi(\varphi)=a
\quad\text{when}\quad
\varphi(g)=g^a
$$
is a group isomorphism.

::: {.proof}
Step <1>1 shows that $\Psi$ is a bijection. If
$$
\varphi(g)=g^a
\qquad\text{and}\qquad
\psi(g)=g^b,
$$
then
$$
(\varphi\circ\psi)(g)
=
\varphi(g^b)
=
\varphi(g)^b
=
g^{ab}.
$$
Thus
$$
\Psi(\varphi\circ\psi)
=
\Psi(\varphi)\Psi(\psi)
$$
in $\FF_p^\times$.
:::

<1>3. Let $H$ be a finite subgroup of the multiplicative group of a field,
and let
$$
m
$$
be the least common multiple of the orders of the elements of $H$.
Then
$$
\abs{H}\leq m.
$$

::: {.proof}
For every $h\in H$, the order of $h$ divides $m$, so
$$
h^m=1.
$$
Thus every element of $H$ is a root of
$$
x^m-1.
$$
A nonzero polynomial of degree $m$ over a field has at most $m$ roots.
Hence
$$
\abs{H}\leq m.
$$
:::

<1>4. With $H$ and $m$ as in step <1>3,
$$
m\mid\abs{H}.
$$

::: {.proof}
By Lagrange's theorem, the order of every element of $H$ divides
$\abs{H}$. The least common multiple of those orders therefore also
divides $\abs{H}$.
:::

<1>5. The group $H$ contains an element of order $m$.

::: {.proof}
Factor
$$
m=\prod_{j=1}^r\ell_j^{e_j}
$$
into distinct prime powers. For each $j$, the definition of $m$ as a least
common multiple implies that some element $h_j\in H$ has order divisible
by
$$
\ell_j^{e_j}.
$$
If
$$
\operatorname{ord}(h_j)
=
\ell_j^{e_j}c_j
$$
with $\ell_j\nmid c_j$, then
$$
k_j=h_j^{c_j}
$$
has order exactly $\ell_j^{e_j}$.

The group $H$ is abelian because it lies in the multiplicative group of a
field. The elements $k_j$ therefore commute, and their orders are pairwise
coprime. Hence
$$
k=k_1\cdots k_r
$$
has order
$$
\prod_{j=1}^r\ell_j^{e_j}
=
m.
$$
:::

<1>6. Every finite subgroup of the multiplicative group of a field is
cyclic.

::: {.proof}
Steps <1>3--<1>4 give
$$
\abs{H}\leq m\leq\abs{H},
$$
so
$$
m=\abs{H}.
$$
By step <1>5, $H$ contains an element of order $m=\abs{H}$. Such an
element generates all of $H$.
:::

<1>7. The automorphism group of $C_p$ is cyclic of order
$$
\boxed{p-1}.
$$

::: {.proof}
By step <1>2,
$$
\operatorname{Aut}(C_p)
\cong
\FF_p^\times.
$$
The multiplicative group $\FF_p^\times$ has $p-1$ elements, and step
<1>6 shows that it is cyclic. Therefore the same is true of
$\operatorname{Aut}(C_p)$.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 gives both the cyclicity and the order.
:::
:::
