---
schema: qual/card@1
id: P-U64DA
kind: problem
title: Galois group of irreducible $X^p-a$ over $\mathbb{Q}$ is the group of maps
  $y\mapsto ky+l$ on $\mathbb{Z}/p\mathbb{Z}$ with $k\neq 0$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the prime exponent, irreducibility over Q, and affine permutation group with June 2015 Fields 2 in the retained extraction; corrected the algebra classification."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified the cyclotomic degree, the coprime-degree argument over the enlarged base field, the affine action on root labels, and the endpoint p=2."
---

::: {.problem}
Assume that $p$ is prime and $X^p - a$ is irreducible in $\mathbb{Q}[X]$.
Show that the Galois group of $X^p - a$ over $\mathbb{Q}$ is isomorphic to the group (with respect to composition) of all functions $f : \mathbb{Z}/p\mathbb{Z} \to \mathbb{Z}/p\mathbb{Z}$ such that for some $k, l \in \mathbb{Z}/p\mathbb{Z}$ with $k \neq 0$, $$f(y) = ky + l \text{ for all } y \in \mathbb{Z}/p\mathbb{Z}.$$
:::

::: solution
Choose a root $\alpha\in\mathbb C$ of $X^p-a$ and a primitive
$p$th root of unity $\zeta$. Irreducibility implies $a\ne0$,
since $X^p$ is reducible for $p\geq2$.

<1>1. The splitting field is $K=\mathbb Q(\alpha,\zeta)$ and
$[K:\mathbb Q]=p(p-1)$.

::: proof
The roots are the $p$ distinct numbers $\alpha\zeta^j$ for
$j\in\mathbb Z/p\mathbb Z$. They lie in $K$, and the field
they generate contains $\alpha$ and
$\zeta=(\alpha\zeta)/\alpha$. Thus $K$ is exactly the splitting field.

Let $F=\mathbb Q(\zeta)$. The polynomial
$$
\Phi_p(X)=1+X+\cdots+X^{p-1}
$$
vanishes at $\zeta$. Its translate is
$$
\Phi_p(Y+1)=\frac{(Y+1)^p-1}{Y}
=\sum_{j=1}^p\binom pj Y^{j-1}.
$$
Every coefficient other than the leading coefficient is divisible
by $p$, and the constant coefficient is $p$, not divisible by
$p^2$. Eisenstein's criterion [@DF04] and invertibility of
translation show that $\Phi_p$ is irreducible. Hence
$[F:\mathbb Q]=p-1$.

Put $d=[K:F]$. Since $K=F(\alpha)$ and $\alpha$ satisfies a
degree-$p$ polynomial over $F$, we have $1\leq d\leq p$.
The original irreducibility gives
$[\mathbb Q(\alpha):\mathbb Q]=p$. Applying the tower law through
this subfield and through $F$ yields
$$
p\mid[K:\mathbb Q]=(p-1)d.
$$
As $p$ is relatively prime to $p-1$, it divides $d$. The bounds
on $d$ force $d=p$, giving the asserted total degree.
For $p=2$ the cyclotomic field is $\mathbb Q$ and the same
argument applies.
:::

<1>2. Every Galois automorphism acts affinely on the root labels.

::: proof
Let $\sigma\in\operatorname{Gal}(K/\mathbb Q)$. It preserves
the multiplicative order of $\zeta$, so
$\sigma(\zeta)=\zeta^k$ for a unique
$k\in(\mathbb Z/p\mathbb Z)^\times$. It sends $\alpha$ to a
root of $X^p-a$, so $\sigma(\alpha)=\alpha\zeta^l$ for a unique
$l\in\mathbb Z/p\mathbb Z$. Consequently
$$
\sigma(\alpha\zeta^j)=\alpha\zeta^{kj+l}.
$$
Thus the permutation of the labels is $j\mapsto kj+l$.
The root action is a homomorphism into the permutation group,
and is faithful because the roots generate $K$.
:::

<1>3. Every affine permutation occurs, proving the isomorphism.

::: proof
The affine maps form a group: composition and inversion are
$$
f_{k,l}\circ f_{u,v}=f_{ku,kv+l},\qquad
f_{k,l}^{-1}=f_{k^{-1},-k^{-1}l}.
$$
Their number is $p(p-1)$, because $l=f(0)$ and
$k=f(1)-f(0)$ determine the map uniquely, with $p$ choices for
$l$ and $p-1$ nonzero choices for $k$.

The splitting field $K/\mathbb Q$ is Galois in characteristic
zero, so its automorphism group has order $[K:\mathbb Q]$
[@DF04], which is $p(p-1)$ by step <1>1.
The injective homomorphism in step <1>2 is therefore a bijection
onto this affine group, as required.
:::
:::
