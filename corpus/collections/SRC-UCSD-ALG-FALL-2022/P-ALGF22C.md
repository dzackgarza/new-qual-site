---
schema: qual/card@1
id: P-ALGF22C
kind: problem
title: "Galois group and primitive element for Q(sqrt(2), sqrt(3), i)"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 3 of the official UCSD Algebra Qualifying Exam, Fall 2022 source; both the Galois-group and primitive-element requests agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified degree eight, the independent sign-change Galois action, and that beta = sqrt(2) + sqrt(3) + i has trivial stabilizer and therefore generates K.
---

::: problem
Let $K = \mathbb{Q}(\sqrt{2}, \sqrt{3}, i)$ as a subfield of $\mathbb{C}$, where $i = \sqrt{-1}$.

(a) Find, with proof, $\operatorname{Gal}(K/\mathbb{Q})$.

(b) Find an element $\beta \in K$ such that $K = \mathbb{Q}(\beta)$.
:::

::: {.solution}
<1>1. The real subfield
\[
L=\mathbb Q(\sqrt2,\sqrt3)
\]
has degree $4$ over $\mathbb Q$.
::: {.proof}
The field $\mathbb Q(\sqrt2)$ has degree $2$ over $\mathbb Q$.
Moreover,
\[
\sqrt3\notin\mathbb Q(\sqrt2).
\]
Indeed, if
\[
\sqrt3=a+b\sqrt2
\qquad(a,b\in\mathbb Q),
\]
then squaring gives
\[
3=a^2+2b^2+2ab\sqrt2.
\]
Hence $ab=0$.
If $b=0$, then $a^2=3$, impossible for $a\in\mathbb Q$; if $a=0$, then $b^2=3/2$, also impossible for $b\in\mathbb Q$.
Thus adjoining $\sqrt3$ gives another quadratic extension, and
\[
[L:\mathbb Q]=4.
\]
:::

<1>2. The extension $K/\mathbb Q$ has degree $8$ and is Galois.
::: {.proof}
The field $L$ from <1>1 is contained in $\mathbb R$, so
\[
i\notin L.
\]
Since $i$ satisfies $x^2+1$, one has
\[
[K:L]=2.
\]
Therefore
\[
[K:\mathbb Q]=[K:L][L:\mathbb Q]=8.
\]

The field $K$ is the splitting field over $\mathbb Q$ of
\[
(x^2-2)(x^2-3)(x^2+1).
\]
This polynomial is separable in characteristic zero, so $K/\mathbb Q$ is Galois.
:::

<1>3. The Galois group is
\[
\operatorname{Gal}(K/\mathbb Q)\cong C_2\times C_2\times C_2.
\]
::: {.proof}
Each independent choice of signs
\[
\sqrt2\longmapsto\varepsilon_2\sqrt2,
\qquad
\sqrt3\longmapsto\varepsilon_3\sqrt3,
\qquad
i\longmapsto\varepsilon_i i,
\qquad
\varepsilon_2,\varepsilon_3,\varepsilon_i\in\{\pm1\},
\]
extends to a $\mathbb Q$-automorphism of $K$.
These give eight distinct automorphisms.
By <1>2, a Galois extension of degree $8$ has exactly eight $\mathbb Q$-automorphisms, so these are all of them.

Every nonidentity sign change has order $2$, and the three elementary sign changes commute.
Hence the group is the elementary abelian group of order $8$.
This proves part (a).
:::

<1>4. Set
\[
\beta=\sqrt2+\sqrt3+i.
\]
No nonidentity element of $\operatorname{Gal}(K/\mathbb Q)$ fixes $\beta$.
::: {.proof}
Suppose the sign change $(\varepsilon_2,\varepsilon_3,\varepsilon_i)$ fixes $\beta$.
Then
\[
(\varepsilon_2-1)\sqrt2
+(\varepsilon_3-1)\sqrt3
+(\varepsilon_i-1)i=0.
\]
Taking imaginary parts gives
\[
\varepsilon_i=1.
\]
The remaining equality is
\[
(\varepsilon_2-1)\sqrt2
+(\varepsilon_3-1)\sqrt3=0.
\]
The numbers $\sqrt2$ and $\sqrt3$ are linearly independent over $\mathbb Q$, since a nontrivial rational relation would make
\[
\sqrt{3/2}
\]
rational.
Thus
\[
\varepsilon_2=\varepsilon_3=1.
\]
So the stabilizer of $\beta$ is trivial.
:::

<1>5. One has
\[
K=\mathbb Q(\beta).
\]
::: {.proof}
By the Galois correspondence, the stabilizer of $\beta$ in $\operatorname{Gal}(K/\mathbb Q)$ is
\[
\operatorname{Gal}(K/\mathbb Q(\beta)).
\]
By <1>4 this subgroup is trivial.
Hence
\[
[K:\mathbb Q(\beta)]=1,
\]
so $K=\mathbb Q(\beta)$.
This proves part (b).
:::
:::
