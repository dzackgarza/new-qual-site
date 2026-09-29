---
schema: qual/card@1
id: P-AGH61RATNONSINGCURVE
kind: problem
title: A nonsingular rational curve not isomorphic to $\PP^1$ is an affine open in $\AA^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nonsingular Curves
  - Birational Geometry
  - Unique Factorization Domains
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.6.1 and the construction and projectivity theorem for the abstract nonsingular curve C_K in I.6. The proof embeds the given rational curve into the unique nonsingular projective model of k(t), moves a missing point to infinity, and identifies its affine coordinate ring as a localization of k[t].
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Recall that a curve is *rational* if it is birationally equivalent to $\PP^1$.
Let $Y$ be a nonsingular rational curve which is not isomorphic to $\PP^1$.

(a) Show that $Y$ is isomorphic to an open subset of $\AA^1$.

(b) Show that $Y$ is affine.

(c) Show that $A(Y)$ is a unique factorization domain.
:::

::: {.solution}
Let $K=K(Y)$. Since $Y$ is rational,
$$
K\cong k(t)=K(\PP^1).
$$

::: pf

::: {.pf-step #y-open-in-projective-model}
The curve $Y$ is isomorphic to an open subset of the unique nonsingular projective curve with function field $K$.

::: pf-proof
For a nonsingular curve, each local ring at a closed point is a discrete valuation ring of its function field.
The construction in Hartshorne I.6 therefore sends a point $P\in Y$ to the corresponding valuation ring $\OO_{Y,P}$ in the abstract nonsingular curve $C_K$.
The argument preceding Theorem I.6.9 identifies every nonsingular affine curve with the open subset of $C_K$ consisting of its local valuation rings.
Covering $Y$ by affine opens and using uniqueness of the valuation center shows that these identifications agree on overlaps.
Hence they glue to an open immersion
$$
Y\hookrightarrow C_K.
$$

Theorem I.6.9 identifies $C_K$ with a nonsingular projective curve, uniquely determined by $K$.
Since $K\cong K(\PP^1)$ and $\PP^1$ is nonsingular and projective, this projective model is $\PP^1$.
Thus $Y$ is isomorphic to an open subset of $\PP^1$.
:::

:::

::: {.pf-step #y-contained-in-affine-line}
After an automorphism of $\PP^1$, the image of $Y$ is contained in $\AA^1$.

::: pf-proof
If the open immersion of step [](#y-open-in-projective-model){.pf-ref} were surjective, then $Y\cong\PP^1$, contrary to the hypothesis.
Choose a point $Q\in\PP^1\setminus Y$.
An automorphism of $\PP^1$ carries $Q$ to the point at infinity $\infty=[1:0]$.
After composing the open immersion with this automorphism,
$$
Y\subseteq\PP^1\setminus\{\infty\}=\AA^1
$$
as an open subset.
This proves part (a).
:::

:::

::: {.pf-step #open-subset-of-a1-affine}
Every nonempty open subset of $\AA_k^1$ is affine.

::: pf-proof
Because $k$ is algebraically closed, every proper closed subset of $\AA^1$ is finite.
Thus the complement of the open subset representing $Y$ has the form
$$
\{a_1,\ldots,a_m\}
$$
for distinct $a_i\in k$, possibly with $m=0$.
Put
$$
q(t)=\prod_{i=1}^m(t-a_i),
$$
with $q=1$ when $m=0$.
Then
$$
Y\cong D(q)\subseteq\Spec k[t]
\cong\Spec k[t,q^{-1}].
$$
Hence $Y$ is affine, proving part (b).
:::

:::

::: {.pf-step #ay-is-ufd}
The affine coordinate ring $A(Y)$ is a unique factorization domain.

::: pf-proof
By step [](#open-subset-of-a1-affine){.pf-ref},
$$
A(Y)\cong k[t,q^{-1}].
$$
The polynomial ring $k[t]$ is a principal ideal domain and hence a [[D-INULL|unique factorization domain]].
A localization of a unique factorization domain is again a unique factorization domain: factor an element before localization and discard precisely those irreducible factors that become units.
Therefore $k[t,q^{-1}]$, and hence $A(Y)$, is a unique factorization domain.
This proves part (c).
:::

:::

::: pf-qed
Steps [](#y-open-in-projective-model){.pf-ref} and [](#y-contained-in-affine-line){.pf-ref} prove part (a), step [](#open-subset-of-a1-affine){.pf-ref} proves part (b), and step [](#ay-is-ufd){.pf-ref} proves part (c).
:::

:::
:::
