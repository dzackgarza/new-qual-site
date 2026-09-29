---
schema: qual/card@1
id: P-AGH27DIMPN
kind: problem
title: $\dim \PP^n = n$, and a quasi-projective variety has the dimension of its closure
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension
  - Projective Varieties
  - Quasi-Projective Varieties
relations:
- kind: uses
  target: P-AGH26HOMDIM
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared both parts and the dimension hint with the retained Hartshorne I.2.7 transcription. Replaced the proof that treated a general projective closure as affine with an argument on the standard affine charts, keeping closure and dimension comparisons on their correct spaces.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be algebraically closed and let $n\ge0$.

(a) Show that $\dim \PP_k^n = n$.

(b) If $Y \subseteq \PP_k^n$ is a quasi-projective variety, show that $\dim Y = \dim \bar{Y}$.
:::

::: {.hint}
For (b), use Exercise I.2.6 to reduce to Proposition I.1.10.
:::

::: {.solution}
Use [[D-5LJUX|dimension]] defined by lengths of strict chains of nonempty irreducible closed subsets.
Let $U_i=D_+(x_i)\subseteq\PP_k^n$ be the standard affine opens.

::: pf

::: {.pf-step #s1}

If $(V_i)$ is an open cover of a topological space $T$, then $\dim T=\sup_i\dim V_i$.

::: pf-proof

A strict chain of irreducible closed subsets of $V_i$ gives such a chain in $T$ by taking closures.
The closures remain distinct, since their intersections with $V_i$ recover the original subsets.
This proves $\dim V_i\le\dim T$.

Conversely, take a chain $Z_0\subsetneq\cdots\subsetneq Z_d$ of nonempty irreducible closed subsets of $T$.
Choose a member $V_i$ of the cover meeting $Z_0$.
It then meets every $Z_j$.
Each intersection $Z_j\cap V_i$ is nonempty, irreducible and closed in $V_i$.
It is dense in $Z_j$, because it is a nonempty open subset of an irreducible space.
Thus these intersections are distinct: equality of two would give equality of their closures in $T$.
They form a chain of the same length in $V_i$.
Taking the supremum over chains proves the reverse inequality.

:::

:::

::: {.pf-step #s2}

One has $\boxed{\dim\PP_k^n=n}$.

::: pf-proof

The ratios $x_j/x_i$, with $j\ne i$, identify $U_i$ with $\AA_k^n$.
The dimension of affine space is $n$, since its coordinate ring is a polynomial ring in $n$ algebraically independent variables [@Har10a, Proposition I.1.9].
The $U_i$ cover $\PP^n$, so step [](#s1){.pf-ref} gives the claimed dimension, including $n=0$.

:::

:::

::: {.pf-step #s3}

For a quasi-projective variety $Y$, one has $\boxed{\dim Y=\dim\overline Y}$.

::: pf-proof

Put $W=\overline Y\subseteq\PP^n$.
By the definition of a quasi-projective variety, $Y$ is a nonempty open subset of its irreducible projective closure $W$.
For every $i$ with $W_i=W\cap U_i\ne\varnothing$, the set $W_i$ is an affine variety in $U_i\cong\AA^n$.
The intersection $Y_i=Y\cap U_i$ is nonempty and dense in $W_i$, since two nonempty open subsets of the irreducible space $W$ meet.
It is a quasi-affine variety whose closure in $\AA^n$ is precisely $W_i$.
The dimension result for quasi-affine varieties therefore gives
$$
\dim Y_i=\dim W_i
$$
[@Har10a, Proposition I.1.10].
This applies the affine closure theorem only to an affine ambient space.

The $Y_i$ and $W_i$ are open covers of $Y$ and $W$, respectively.
Step [](#s1){.pf-ref} consequently yields
$$
\dim Y=\sup_i\dim Y_i=\sup_i\dim W_i=\dim W.
$$
Equivalently, every nonempty $W_i$ has the function field $k(W)$ and dimension $\operatorname{trdeg}_k k(W)$ by the affine dimension theorem; the same is then true of its dense open $Y_i$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves (a), and step [](#s3){.pf-ref} proves (b).

:::

:::

:::
