---
schema: qual/card@1
id: P-SH5P6
kind: problem
title: Removing repeated roots without changing the Galois group
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Separability
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Restored the section-wide hypothesis that F is the splitting field of f over K and restored the full coefficient list v_0,...,v_k for g."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Proved F=E(u_1,...,u_k), used the distinct roots of g for separability, and showed every K-automorphism permutes the u_i and hence fixes the coefficients of g."
---

::: {.problem}
Let $F$ be a splitting field over $K$ of a polynomial $f\in K[x]$, and write in $F$
$$
f=\prod_{i=1}^k (x-u_i)^{n_i},
$$
where the $u_i$ are distinct and each $n_i\geq1$.
Let
$$
g(x)=\prod_{i=1}^k(x-u_i)=v_0+v_1x+\cdots+v_kx^k
$$
and let
$$
E=K(v_0,\ldots,v_k).
$$
Then show that the following hold:

1. $F$ is a splitting field of $g$ over $E$.

2. $F$ is Galois over $E$.

3. $\mathrm{Aut}_E(F) = \mathrm{Aut}_K(F)$.
:::

::: {.solution}
Because $F$ is the splitting field of $f$ over $K$, it is generated over $K$
by the distinct roots:
$$
F=K(u_1,\ldots,u_k).
$$
Each coefficient $v_j$ of $g$ is a symmetric polynomial in the $u_i$, so
$v_j\in F$ and therefore
$$
K\subseteq E\subseteq F.
$$

<1>1. $F$ is the splitting field of $g$ over $E$.
::: {.proof}
The polynomial $g$ belongs to $E[x]$ by definition of $E$, and in $F[x]$ it
splits as
$$
g(x)=\prod_{i=1}^k(x-u_i).
$$
Moreover,
$$
E(u_1,\ldots,u_k)
\supseteq K(u_1,\ldots,u_k)
=F.
$$
The reverse inclusion is immediate because $E\subseteq F$ and every $u_i$ is
in $F$. Hence
$$
E(u_1,\ldots,u_k)=F.
$$
Thus $F$ is generated over $E$ by the roots of $g$ and $g$ splits in $F$;
therefore $F$ is the splitting field of $g$ over $E$.
:::

<1>2. The extension $F/E$ is Galois.
::: {.proof}
The roots $u_1,\ldots,u_k$ of $g$ are pairwise distinct. Hence $g$ is
separable over $E$: equivalently, every irreducible factor of $g$ has only
simple roots in its splitting field.

By step <1>1, $F$ is the splitting field over $E$ of the separable polynomial
$g$. Therefore $F/E$ is finite, normal, and separable, hence Galois.
:::

<1>3. Every $E$-automorphism of $F$ is a $K$-automorphism.
::: {.proof}
Since $K\subseteq E$, any automorphism fixing $E$ pointwise also fixes $K$
pointwise. Thus
$$
\operatorname{Aut}_E(F)\subseteq\operatorname{Aut}_K(F).
$$
:::

<1>4. Every $K$-automorphism of $F$ fixes $E$ pointwise.
::: {.proof}
Let
$$
\sigma\in\operatorname{Aut}_K(F).
$$
For each root $u_i$ of $f$,
$$
f(\sigma(u_i))
=\sigma(f(u_i))
=0,
$$
because the coefficients of $f$ lie in $K$ and are fixed by $\sigma$.
Hence $\sigma$ permutes the finite set of distinct roots
$$
\{u_1,\ldots,u_k\}.
$$
Consequently
$$
\begin{aligned}
\sigma(g)
&=\prod_{i=1}^k(x-\sigma(u_i))\\
&=\prod_{i=1}^k(x-u_i)\\
&=g.
\end{aligned}
$$
Thus $\sigma$ fixes every coefficient $v_0,\ldots,v_k$ of $g$. It also fixes
$K$, so it fixes
$$
E=K(v_0,\ldots,v_k)
$$
pointwise. Therefore
$$
\operatorname{Aut}_K(F)\subseteq\operatorname{Aut}_E(F).
$$
:::

Combining steps <1>3 and <1>4,
$$
\boxed{\operatorname{Aut}_E(F)=\operatorname{Aut}_K(F).}
$$
:::
