---
schema: qual/card@1
id: P-H3PWT
kind: problem
title: Degree of a compositum when the factors have coprime degrees, and a counterexample
  without coprimeness
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Degree
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the coprime-degree assertion and displayed counterexample conditions with Summer 2007 Fields 4 in the retained extraction; made the common-overfield convention explicit."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the finite-dimensional span is a field without separability assumptions, both degree divisibilities, and the distinct cubic fields giving intersection Q and compositum degree six."
---

::: problem
a. Let $F$ be a field, and let $K, L$ be finite dimensional extensions of $F$ inside a common overfield.
Suppose $[K : F]$ and $[L : F]$ are relatively prime.
Prove that $[KL : F] = [K : F][L : F]$.
Here $KL$ is the compositum of $K$ and $L$.

b. Give an example of fields $F, K, L$ such that $K \cap L = F$ and $[KL : F] < [K : F][L : F]$.
:::

::: solution
<1>1. For any two finite extensions in a common overfield,
$$
[KL:F]\leq[K:F][L:F].
$$

::: proof
Put $m=[K:F]$ and $n=[L:F]$, and choose an $F$-basis
$\ell_1,\ldots,\ell_n$ of $L$ with $\ell_1=1$.
Inside the common overfield, let
$$
S=K\ell_1+\cdots+K\ell_n.
$$
This is a $K$-vector space of dimension at most $n$, containing both
$K$ and $L$. For every $i,j$, the product $\ell_i\ell_j$ is an
$F$-linear combination of the basis elements. Consequently $S$ is
closed under multiplication, and it contains $1$.

For nonzero $s\in S$, multiplication by $s$ is an injective
$K$-linear map $S\to S$, since the ambient ring is a field.
Finite dimension makes this map surjective. In particular, $st=1$
for some $t\in S$, so $S$ is a field. It contains $K$ and $L$ and
is contained in their compositum, hence $S=KL$.
Therefore $[KL:K]\leq n$, and the tower law gives
$[KL:F]=[KL:K]m\leq mn$.
:::

<1>2. Coprimeness forces equality, proving part (a).

::: proof
Write $d=[KL:F]$. The tower law applied through $K$ and through $L$
shows that $m\mid d$ and $n\mid d$. If $\gcd(m,n)=1$, then
$mn\mid d$. Since $d>0$, we have $d\geq mn$; the opposite
inequality is step <1>1. Thus $[KL:F]=mn$.
:::

<1>3. For part (b), take two different cubic subfields of the
splitting field of $x^3-2$.

::: proof
Let $\alpha=\sqrt[3]{2}$ be real and let $\zeta$ be a primitive
cube root of unity. Inside $\mathbb C$, set
$$
F=\mathbb Q,\qquad K=\mathbb Q(\alpha),\qquad
L=\mathbb Q(\zeta\alpha).
$$
Both displayed generators have minimal polynomial $x^3-2$, which
is irreducible by Eisenstein's criterion at $2$ [@DF04]. Thus
$[K:\mathbb Q]=[L:\mathbb Q]=3$. The fields are different because
$K\subseteq\mathbb R$, whereas $\zeta\alpha$ is nonreal.

The degree $[K\cap L:\mathbb Q]$ divides $3$ by the tower law.
If it were $3$, then $K\cap L=K=L$, contrary to distinctness.
Hence it is $1$ and $K\cap L=\mathbb Q$.

The compositum contains
$\zeta=(\zeta\alpha)/\alpha$, so
$$
KL=\mathbb Q(\alpha,\zeta)=K(\zeta).
$$
The element $\zeta$ satisfies $x^2+x+1$ and does not belong to
the real field $K$, so $[K(\zeta):K]=2$. Consequently
$$
[KL:F]=2\cdot3=6<9=[K:F][L:F].
$$
This verifies both conditions in part (b).
:::
:::
