---
schema: qual/card@1
id: P-XWNF6
kind: problem
title: $\pi_1(\bigvee S^1)$ is free, and $S^2\not\cong S^3$
classification:
  areas:
  - topology
  topics:
  - van Kampen
  - Fundamental Group
relations: []
review: draft
---

::: problem
7. Theorem: $\pi_1(\bigvee_{i=1}^k S^1) \cong {\Large{*}}_{i=1}^n\ZZ$, the free product of $n$ copies of $\ZZ$.

::: {.proof}
We proceed by induction on $n$, using the Seifert–van Kampen theorem.

**Base case:** Take $n=1$, then $\pi_1(S^1) = \ZZ$ as proved in Hatcher.

**Inductive step:** Suppose this holds for all $k < n$, then we have $X = \bigvee^n S^1 = \left( \bigvee^{n-1}S^1\right) \vee S^1$.
Let $p$ be the point of common intersection, then let $U = \bigvee^{n-1} S^1$ and $V = S^1 \union \theset{p}$.

Then $U\union V = X$, $U \intersect V = \theset{p}$, and both $U,V$ are path-connected.
Since we have $\pi_1(\pt) = 0$, the amalgamated free product reduces to the usual free product.
By the induction hypothesis, we have $\pi_1(U) = {\Large{*}}^{n-1}\ZZ$, so

$$\pi_1(X) = \pi_1(U\cup V) = \pi_1(U) * \pi_1(V) =_{\text{IH}} ({\Large{*}}^{n-1} \ZZ ) * \pi_1(V) = ({\Large{*}}^{n-1} \ZZ) * \ZZ = {\Large{*}}^{n} \ZZ.$$
:::

Definition: Let $F_n \definedas {\Large{*}^n} \ZZ$ be the free group on $n$ generators.
Lemma: If $n\neq m, F_n \not\cong F_m$.

::: {.proof}
If $F_n \cong F_m$, then abelianizing gives $\ZZ^n \cong \ZZ^m$.
But then tensor both sides with $\ZZ_2$ over $\ZZ$, yielding $\ZZ^n \otimes_\ZZ \ZZ_2 \cong \ZZ^m \otimes_\ZZ \ZZ_2$.
But the LHS is isomorphic to $(\ZZ/2\ZZ)^n$, while the RHS is isomorphic to $(\ZZ/2\ZZ)^m$.
These are both finite groups: there are 2 elements in $\ZZ/2\ZZ$, so the first has $2^n$ elements and the latter has $2^m$ elements.
But if $2^n=2^m$, then $n=m$.
The lemma follows from the contrapositive.
:::

Now we have all we need - let $X = S^2 - \theset{p_1, p_2}$ and $Y = S^3 - \theset{q_1, q_2}$.
Then by the previous problems, $X \homotopic S^1$ and $Y \homotopic S^2$, so if $S^2 \cong S^3$ then $X \homotopic Y$ and $S^1 \homotopic S^2$.
But $\pi_1(S^1) = \ZZ$ and $\pi_1(S^2) = 0$, so $S^1 \not\simeq S^2$, a contradiction.
:::

::: {.solution}
<1>1. For $n\ge1$,
$$\boxed{\pi_1\left(\bigvee_{i=1}^nS^1\right)\cong F_n.}$$
::: {.proof}
Apply van Kampen inductively: adjoining one circle at the common basepoint takes the free product with $\pi_1(S^1)=\mathbb Z$.
:::

<1>2. If $F_n\cong F_m$, then $n=m$.
::: {.proof}
Abelianization gives $\mathbb Z^n\cong\mathbb Z^m$, forcing equal ranks.
:::

<1>3. In particular $S^2$ and $S^3$ are not homeomorphic.
::: {.proof}
Removing two points from a sphere preserves homeomorphism type under any hypothetical homeomorphism. But
$$S^2\setminus\{p,q\}\simeq S^1,\qquad S^3\setminus\{p',q'\}\simeq S^2.$$
Their fundamental groups are $\mathbb Z$ and $0$, so the punctured spaces are not homotopy equivalent, hence cannot be homeomorphic.
:::
:::
