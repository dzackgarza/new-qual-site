---
schema: qual/card@1
id: P-ARTALG-AL04-9
kind: problem
title: Every finite group is a Galois group over a suitable fixed field
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the unrestricted base field and Galois realization request with 2004 Fields 2 in the retained extraction, line 992."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the faithful variable-permutation action, minimal-support linear-dependence argument, embedding bound, and separability and normality via distinct orbit polynomials."
---

::: {.problem}
Given a finite group $G$, show that there are fields $K$ and $F$ such that $K$ is Galois over $F$, and $G$ is isomorphic to the Galois group of $K$ over $F$.
:::

::: {.solution}
Let $m=|G|$. Take algebraically independent indeterminates
$x_g$, indexed by $g\in G$, over $\mathbb Q$, and put
$$
K=\mathbb Q(x_g:g\in G).
$$
For $h\in G$ let $\sigma_h$ fix $\mathbb Q$ and send
$x_g$ to $x_{hg}$. Define the fixed field
$$
F=\{a\in K:\sigma_h(a)=a\text{ for every }h\in G\}.
$$

<1>1. These maps give an injective homomorphism
$G\longrightarrow\operatorname{Aut}_F(K)$.

::: {.proof}
A permutation of algebraically independent indeterminates extends
to an automorphism of the polynomial ring and its fraction field.
On the generators, $\sigma_h\sigma_k(x_g)=x_{hkg}$, so
$\sigma_h\sigma_k=\sigma_{hk}$. In particular $\sigma_{h^{-1}}$
is the inverse of $\sigma_h$. The action is faithful because
$\sigma_h(x_1)=x_h$, and different variables are different elements.
The fixed elements are closed under addition, subtraction,
multiplication, and inversion of nonzero elements; hence $F$ is a
field. Every $\sigma_h$ fixes it by definition.
:::

<1>2. The extension degree satisfies $[K:F]\leq m$.

::: {.proof}
Take any $a_1,\ldots,a_{m+1}\in K$. The homogeneous system
$$
\sum_{j=1}^{m+1}\sigma_h(a_j)c_j=0\qquad(h\in G)
$$
has $m$ equations in $m+1$ unknowns over the field $K$, so its
kernel is nonzero. Choose a nonzero kernel vector $c$ with the
smallest possible number of nonzero coordinates, and scale it so
that one such coordinate, say $c_k$, is $1$.

For $t\in G$, the vector $\sigma_t(c)$ also belongs to this
kernel. Indeed, applying $\sigma_t$ to the equation indexed by
$t^{-1}h$ gives the equation indexed by $h$ for $\sigma_t(c)$.
Thus $\sigma_t(c)-c$ is a kernel vector. Its support is contained
in the support of $c$, and its $k$th coordinate is zero. Minimality
of the support forces $\sigma_t(c)-c=0$. This holds for every $t$,
so each coefficient $c_j$ lies in $F$.

The equation for $h=1$ is now the nontrivial $F$-linear relation
$\sum_j a_jc_j=0$. Every $m+1$ elements of $K$ are therefore
linearly dependent over $F$, proving the dimension bound and
finiteness of the extension.
:::

<1>3. The extension is Galois and its full Galois group is the
displayed copy of $G$.

::: {.proof}
For any $a\in K$, let $O_a=\{\sigma_h(a):h\in G\}$, as a set
without repetitions. The polynomial
$$
p_a(T)=\prod_{b\in O_a}(T-b)
$$
has coefficients in $F$: each $\sigma_h$ permutes $O_a$.
It vanishes at $a$ and splits into distinct linear factors in $K$.
The minimal polynomial of $a$ over $F$ divides $p_a$, so it also
splits into distinct linear factors in $K$. Thus every element is
separable, and every irreducible polynomial over $F$ with a root
in $K$ splits there. These are separability and normality, so the
finite extension $K/F$ is Galois.

A finite extension of degree $d$ has at most $d$ automorphisms
fixing its base field. To see the bound, choose a finite tower
of simple adjunctions. At an adjunction of degree $e$, an embedding
of the preceding field has at most $e$ extensions, because the
new generator must map to a root of the corresponding minimal
polynomial. Multiplying these bounds along the tower gives $d$.
Apply this with $d=[K:F]$. Step <1>1 supplies $m$ distinct
automorphisms and step <1>2 gives
$$
m\leq |\operatorname{Aut}_F(K)|\leq [K:F]\leq m.
$$
Equality holds throughout. Hence the injective homomorphism of
step <1>1 is onto, proving $\operatorname{Gal}(K/F)\cong G$.
For the trivial group the construction has $F=K$, so that case
is included as well.
:::
:::
