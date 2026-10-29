---
schema: qual/card@1
id: P-UCLARA11S-05
kind: problem
title: Nonseparability of the dual of $\ell^\infty$ and nonreflexivity of $\ell^1$
classification: {areas: [real-analysis], topics: []}
relations: []
review: draft
---

::: {.problem}
(a) Show that $\ell^\infty(\ZZ)$ contains continuum many functions $x_\alpha:\ZZ\to\RR$ satisfying
$$
\|x_\alpha\|_{\ell^\infty}=1,
\qquad
\|x_\alpha-x_\beta\|_{\ell^\infty}\ge1
\quad\text{whenever }\alpha\ne\beta.
$$

(b) Deduce, assuming the axiom of choice, that the Banach-space dual of $\ell^\infty(\ZZ)$ cannot contain a countable dense subset.

(c) Deduce that $\ell^1(\ZZ)$ is not reflexive.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

There are continuum many subsets
$$
A\subset\ZZ
$$
containing $0$.


::: pf-proof

The power set of $\ZZ\setminus\{0\}$ has cardinality
$$
2^{\aleph_0}.
$$
The map
$$
B\longmapsto B\cup\{0\}
$$
is a bijection from that power set onto the family of subsets of $\ZZ$ containing $0$.

:::

:::

::: {.pf-step #s1-2}

For each subset $A\subset\ZZ$ containing $0$, let
$$
x_A(j)
=
\mathbf 1_A(j).
$$
Then
$$
\|x_A\|_\infty=1.
$$


::: pf-proof

Since $0\in A$,
$$
x_A(0)=1,
$$
while $x_A$ takes only the values $0$ and $1$. Hence its supremum norm is exactly $1$.

:::

:::

::: {.pf-step #s1-3}

If $A\ne B$, then
$$
\|x_A-x_B\|_\infty=1.
$$


::: pf-proof

Choose
$$
j\in A\triangle B.
$$
Then
$$
|x_A(j)-x_B(j)|=1.
$$
At every coordinate the difference has absolute value at most $1$, so the supremum norm is exactly $1$.

:::

:::

::: {.pf-step #s1-4}

This proves part (a).


::: pf-proof

Combine steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Let $X$ be a Banach space. If $X^*$ is separable, then $X$ is separable.


::: pf-proof

Assume $X^*$ is separable. Choose a sequence
$$
(\varphi_n)_{n\ge1}
$$
dense in the unit sphere of $X^*$.

For each $n$, by the definition of the dual norm choose
$$
x_n\in X,
\qquad
\|x_n\|=1,
$$
such that
$$
|\varphi_n(x_n)|>\frac12.
$$
Let
$$
Y
\coloneqq
\overline{\operatorname{span}}\{x_n:n\ge1\}.
$$
The space $Y$ is separable.

Suppose $Y\ne X$. Choose $x\notin Y$. By Hahn--Banach, there is
$$
\psi\in X^*,
\qquad
\|\psi\|=1,
$$
such that
$$
\psi|_Y=0.
$$
Choose $n$ with
$$
\|\psi-\varphi_n\|<\frac14.
$$
Since $x_n\in Y$,
$$
\psi(x_n)=0.
$$
Therefore
$$
|\varphi_n(x_n)|
=
|\varphi_n(x_n)-\psi(x_n)|
\le
\|\varphi_n-\psi\|\|x_n\|
<
\frac14,
$$
contradicting
$$
|\varphi_n(x_n)|>\frac12.
$$
Thus $Y=X$, so $X$ is separable.

:::

:::

::: {.pf-step #s1-6}

The dual
$$
(\ell^\infty(\ZZ))^*
$$
is not separable.


::: pf-proof

By part (a), $\ell^\infty(\ZZ)$ contains an uncountable $1$-separated set, so it is not separable.

If its dual were separable, step [](#s1-5){.pf-ref} would imply that $\ell^\infty(\ZZ)$ itself is separable, a contradiction.

:::

:::

::: {.pf-step #s1-7}

This proves part (b).


::: pf-proof

Step [](#s1-6){.pf-ref} is exactly the assertion of part (b).

:::

:::

::: {.pf-step #s1-8}

One has the canonical isometric identification
$$
(\ell^1(\ZZ))^*
\cong
\ell^\infty(\ZZ).
$$


::: pf-proof

For $a=(a_j)\in\ell^\infty$, the formula
$$
T_a(x)
=
\sum_{j\in\ZZ}x_ja_j
$$
defines a bounded linear functional on $\ell^1$ with
$$
\|T_a\|=\|a\|_\infty.
$$
Conversely, if $T\in(\ell^1)^*$, define
$$
a_j=T(e_j),
$$
where $e_j$ is the standard basis vector. Then
$$
|a_j|
\le
\|T\|,
$$
so $a\in\ell^\infty$, and density of finitely supported sequences gives $T=T_a$.

:::

:::

::: {.pf-step #s1-9}

The space $\ell^1(\ZZ)$ is not reflexive.


::: pf-proof

Suppose instead that $\ell^1$ were reflexive. Then
$$
(\ell^1)^{**}
\cong
\ell^1.
$$
By step [](#s1-8){.pf-ref},
$$
(\ell^\infty)^*
\cong
(\ell^1)^{**}.
$$
Hence
$$
(\ell^\infty)^*
\cong
\ell^1.
$$
But $\ell^1(\ZZ)$ is separable, while step [](#s1-6){.pf-ref} says $(\ell^\infty)^*$ is not separable. This contradiction proves that $\ell^1$ is not reflexive.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (a), step [](#s1-7){.pf-ref} proves part (b), and step [](#s1-9){.pf-ref} proves part (c).

:::

:::

:::
