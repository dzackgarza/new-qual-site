---
schema: qual/card@1
id: P-CAS24E
kind: problem
title: "Polynomials with $p_n(0)=1$, $p_n'(0)=0$, pointwise tending to $0$ off $0$"
classification:
  areas:
  - complex-analysis
  topics:
  - Polynomials
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Show that there exist polynomials $p_n$ such that

(i) $p_n(0) = 1$, $p_n'(0) = 0$,

(ii) $p_n(z) \to 0$ as $n \to \infty$ for all fixed $z \in \CC \setminus \{0\}$.
:::

::: {.solution}

The construction is the card's own: a Mergelyan approximation to a step function on a compact set with connected complement, normalised so that $p_{n}(0)=1$ and $p_{n}'(0)=0$. No retained set solves this exercise, and the sets searched are recorded in the audit trail.

Choose pairwise disjoint open arcs $I_{n}\subset\circlegroup$, for instance $I_{n}$ of length $2^{-n}$ about the point $e^{i/n}$; then no direction lies in two of them. Put
$$
K_{n}=\Big\{z:\tfrac1n\le\abs{z}\le n,\ \tfrac{z}{\abs{z}}\notin I_{n}\Big\},\qquad L_{n}=K_{n}\cup\overline{D\Big(0,\tfrac{1}{2n}\Big)}.
$$

::: pf

::: {.pf-step #compact}
$L_{n}$ is compact and its complement in $\CC$ is connected, and the function $h_{n}$ equal to $0$ on $K_{n}$ and to $1$ on $\overline{D(0,\frac{1}{2n})}$ is continuous on $L_{n}$ and holomorphic on its interior.

::: pf-proof
$K_{n}$ is closed and bounded, being the intersection of the closed annulus $\{1/n\le\abs z\le n\}$ with the preimage of the closed set $\circlegroup\setminus I_{n}$ under $z\mapsto z/\abs z$, which is continuous off $0$; the closed disc is compact; so $L_{n}$ is compact. The two pieces are disjoint because $\frac{1}{2n}<\frac1n$, so a function defined by different constants on them is continuous. The complement of $L_{n}$ is the union of $\{1/(2n)<\abs z<1/n\}$, of $\{\abs z>n\}$ and of the sector $\{z:\abs z\ge0,\ z/\abs z\in I_{n}\}$; the first two are connected pieces and the sector meets both — it contains points of modulus between $1/(2n)$ and $1/n$ and points of modulus greater than $n$ — so the complement is connected. The interior of $L_{n}$ is the disjoint union of $\{1/n<\abs z<n,\ z/\abs z\notin\overline{I_{n}}\}$ and $D(0,\frac{1}{2n})$, on each of which $h_{n}$ is constant, hence holomorphic.
:::

:::

::: {.pf-step #mergelyan}
For every $\varepsilon>0$ there is a polynomial $q_{n}$ with $\sup_{L_{n}}\abs{q_{n}-h_{n}}<\varepsilon$.

::: pf-proof
$L_{n}$ is compact with connected complement and $h_{n}$ is continuous on $L_{n}$ and holomorphic on its interior, which is exactly the hypothesis of Mergelyan's theorem; that theorem then gives a polynomial uniformly within $\varepsilon$ of $h_{n}$ on $L_{n}$.
:::

:::

::: {.pf-step #estimates}
Choosing $0<\varepsilon_{n}$ with $\varepsilon_{n}\to0$ and $n^{2}\varepsilon_{n}\to0$ and a polynomial $q_{n}$ as in step [](#mergelyan){.pf-ref}, one has $\abs{q_{n}(0)-1}\le\varepsilon_{n}$ and $\abs{q_{n}'(0)}\le2n\varepsilon_{n}$.

::: pf-proof
On the disc $\abs z\le\frac{1}{2n}$, which is contained in $L_{n}$, one has $h_{n}=1$, so $\abs{q_{n}(z)-1}<\varepsilon_{n}$ there and in particular at $0$. The function $q_{n}-1$ is entire and bounded by $\varepsilon_{n}$ on the circle $\abs z=\frac{1}{2n}$, so Cauchy's estimate gives
$$
\abs{q_{n}'(0)}=\abs{(q_{n}-1)'(0)}\le\frac{\varepsilon_{n}}{1/(2n)}=2n\varepsilon_{n}.
$$
:::

:::

::: {.pf-step #polynomials}
For large $n$, $q_{n}(0)\ne0$ and
$$
p_{n}(z)=\frac{q_{n}(z)-q_{n}'(0)z}{q_{n}(0)}
$$
is a polynomial with $p_{n}(0)=1$ and $p_{n}'(0)=0$.

::: pf-proof
$\abs{q_{n}(0)-1}\le\varepsilon_{n}<1$ for large $n$, so $q_{n}(0)\ne0$ and $p_{n}$ is a polynomial, being a polynomial divided by a nonzero constant. Then $p_{n}(0)=\big(q_{n}(0)-0\big)/q_{n}(0)=1$, and differentiating gives $p_{n}'(z)=\big(q_{n}'(z)-q_{n}'(0)\big)/q_{n}(0)$, so $p_{n}'(0)=0$. That is (i).
:::

:::

::: {.pf-step #convergence}
For every fixed $z\ne0$, $p_{n}(z)\to0$.

::: pf-proof
Fix $z\ne0$. For all large $n$ one has $\frac1n\le\abs z\le n$. The direction $z/\abs z$ lies in at most one of the pairwise disjoint arcs $I_{n}$, so for all but at most one $n$ one has $z/\abs z\notin I_{n}$ and hence $z\in K_{n}$, where $\abs{q_{n}(z)}\le\varepsilon_{n}$. Therefore, for all large $n$,
$$
\abs{p_{n}(z)}\le\frac{\abs{q_{n}(z)}+\abs{q_{n}'(0)}\abs z}{\abs{q_{n}(0)}}\le\frac{\varepsilon_{n}+2n\varepsilon_{n}\abs z}{\abs{q_{n}(0)}},
$$
and the numerator tends to $0$ because $\varepsilon_{n}\to0$ and $n\varepsilon_{n}\le n^{2}\varepsilon_{n}\to0$ for $n\ge1$, while $\abs{q_{n}(0)}\to1$. So $p_{n}(z)\to0$, which is (ii).
:::

:::

:::
:::
