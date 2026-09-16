---
schema: qual/card@1
id: P-I5GAL
kind: problem
title: Every finite group is a Galois group over some extension $E \supseteq F$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the unrestricted fields and finite-group realization request with original packet page 6, Fields 4."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked faithfulness, fixed coefficients, finite separability, and both group-order inequalities; no realization over a prescribed base field is assumed."
---

::: {.problem}
Recall that every finite group $G$ is isomorphic to a subgroup of $S_n$ for some $n > 0$.
Show that there are fields $E \supseteq F$ such that the Galois group of $E$ over $F$ is isomorphic to $G$.
:::

::: {.solution}
Let $m=|G|$, let $\{x_g:g\in G\}$ be algebraically independent
indeterminates over $\mathbb Q$, and set
$$
E=\mathbb Q(x_g:g\in G).
$$
For $h\in G$, define $\sigma_h$ on these generators by
$\sigma_h(x_g)=x_{hg}$, fixing $\mathbb Q$. Set
$$
F=\{a\in E:\sigma_h(a)=a\text{ for every }h\in G\}.
$$

<1>1. The map $h\mapsto\sigma_h$ embeds $G$ into the group of
$F$-automorphisms of $E$.

::: {.proof}
Permuting algebraically independent variables gives an automorphism
of the polynomial ring and hence of its fraction field $E$.
The permutation associated with $h^{-1}$ is its inverse. On each
generator,
$$
\sigma_h\sigma_k(x_g)=x_{hkg}=\sigma_{hk}(x_g),
$$
so this is a group homomorphism. It is injective, since
$\sigma_h(x_1)=x_h$, and distinct indeterminates are distinct elements
of $E$. Fixed elements are closed under the field operations, so $F$
is a subfield of $E$ containing $\mathbb Q$. By its definition every
$\sigma_h$ fixes $F$.
:::

<1>2. The extension $E/F$ is finite and separable, and is a splitting
field over $F$.

::: {.proof}
The polynomial
$$
p(T)=\prod_{g\in G}(T-x_g)
$$
has coefficients in $F$, because each $\sigma_h$ permutes its factors.
Thus every $x_g$ is algebraic over $F$. There are finitely many of
them, and $F(x_g:g\in G)=E$, since $\mathbb Q\subseteq F\subseteq E$.
Successively adjoining these algebraic elements therefore makes
$E/F$ finite. The displayed roots are distinct by algebraic
independence. Their minimal polynomials over $F$ divide the separable
polynomial $p$, so they are separable over $F$. Hence $E$ is precisely
the splitting field of the separable polynomial $p$ over $F$.
:::

<1>3. The displayed $m$ automorphisms are all the automorphisms of
$E/F$.

::: {.proof}
By the primitive element theorem for finite separable extensions
[@DF04], there is $u\in E$ with $E=F(u)$. The polynomial
$$
q(T)=\prod_{h\in G}(T-\sigma_h(u))
$$
also has coefficients in $F$: applying $\sigma_k$ permutes its
factors by $h\mapsto kh$. It is monic of degree $m$ and vanishes
at $u$. Therefore the minimal polynomial $\mu_u$ of $u$ over $F$
divides $q$, and
$$
[E:F]=\deg\mu_u\leq m.
$$
Conversely, an $F$-automorphism of $F(u)$ is uniquely determined by its
value on $u$, which must be a root of $\mu_u$. A degree-$\deg\mu_u$
polynomial has at most $\deg\mu_u$ roots in a field. Together with
the embedding in step <1>1 this gives
$$
m\leq |\operatorname{Aut}_F(E)|\leq\deg\mu_u\leq m.
$$
All inequalities are equalities. Thus every $F$-automorphism is one of
the $\sigma_h$, and the faithful homomorphism in step <1>1 is an
isomorphism $G\cong\operatorname{Gal}(E/F)$. Step <1>2 also shows
that the constructed extension is Galois in the finite, normal,
separable sense.
:::
:::
