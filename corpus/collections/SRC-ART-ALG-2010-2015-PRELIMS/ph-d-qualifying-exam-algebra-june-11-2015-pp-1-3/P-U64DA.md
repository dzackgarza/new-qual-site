---
schema: qual/card@1
id: P-U64DA
kind: problem
title: Galois group of irreducible $X^p-a$ over $\QQ$ is the group of maps
  $y\mapsto ky+l$ on $\ZZ/p\ZZ$ with $k\neq 0$
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
Assume that $p$ is prime and $X^p - a$ is irreducible in $\QQ[X]$.
Show that the Galois group of $X^p - a$ over $\QQ$ is isomorphic to the group (with respect to composition) of all functions $f : \ZZ/p\ZZ \to \ZZ/p\ZZ$ such that for some $k, l \in \ZZ/p\ZZ$ with $k \neq 0$, $$f(y) = ky + l \text{ for all } y \in \ZZ/p\ZZ.$$
:::

::: {.solution}
Choose a root $\alpha\in\CC$ of $X^p-a$ and a primitive
$p$th root of unity $\zeta$. Irreducibility implies $a\ne0$,
since $X^p$ is reducible for $p\geq2$.

::: pf

::: {.pf-step #s1}

The splitting field is $K=\QQ(\alpha,\zeta)$ and
$[K:\QQ]=p(p-1)$.

::: pf-proof

The roots are the $p$ distinct numbers $\alpha\zeta^j$ for
$j\in\ZZ/p\ZZ$. They lie in $K$, and the field
they generate contains $\alpha$ and
$\zeta=(\alpha\zeta)/\alpha$. Thus $K$ is exactly the splitting field.

Let $F=\QQ(\zeta)$. The polynomial
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
$[F:\QQ]=p-1$.

Put $d=[K:F]$. Since $K=F(\alpha)$ and $\alpha$ satisfies a
degree-$p$ polynomial over $F$, we have $1\leq d\leq p$.
The original irreducibility gives
$[\QQ(\alpha):\QQ]=p$. Applying the tower law through
this subfield and through $F$ yields
$$
p\mid[K:\QQ]=(p-1)d.
$$
As $p$ is relatively prime to $p-1$, it divides $d$. The bounds
on $d$ force $d=p$, giving the asserted total degree.
For $p=2$ the cyclotomic field is $\QQ$ and the same
argument applies.

:::

:::

::: {.pf-step #s2}

Every Galois automorphism acts affinely on the root labels.

::: pf-proof

Let $\sigma\in\operatorname{Gal}(K/\QQ)$. It preserves
the multiplicative order of $\zeta$, so
$\sigma(\zeta)=\zeta^k$ for a unique
$k\in(\ZZ/p\ZZ)^\times$. It sends $\alpha$ to a
root of $X^p-a$, so $\sigma(\alpha)=\alpha\zeta^l$ for a unique
$l\in\ZZ/p\ZZ$. Consequently
$$
\sigma(\alpha\zeta^j)=\alpha\zeta^{kj+l}.
$$
Thus the permutation of the labels is $j\mapsto kj+l$.
The root action is a homomorphism into the permutation group,
and is faithful because the roots generate $K$.

:::

:::

::: {.pf-step #s3}

Every affine permutation occurs, proving the isomorphism.

::: pf-proof

The affine maps form a group: composition and inversion are
$$
f_{k,l}\circ f_{u,v}=f_{ku,kv+l},\qquad
f_{k,l}^{-1}=f_{k^{-1},-k^{-1}l}.
$$
Their number is $p(p-1)$, because $l=f(0)$ and
$k=f(1)-f(0)$ determine the map uniquely, with $p$ choices for
$l$ and $p-1$ nonzero choices for $k$.

The splitting field $K/\QQ$ is Galois in characteristic
zero, so its automorphism group has order $[K:\QQ]$
[@DF04], which is $p(p-1)$ by step [](#s1){.pf-ref}.
The injective homomorphism in step [](#s2){.pf-ref} is therefore a bijection
onto this affine group, as required.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} identify the Galois group with the full affine group on
$\ZZ/p\ZZ$.

:::

:::

:::
