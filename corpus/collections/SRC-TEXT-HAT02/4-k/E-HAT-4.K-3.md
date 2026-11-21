---
schema: qual/card@1
id: E-HAT-4.K-3
kind: problem
title: $SP_n(I) = \Delta^n$
classification:
  areas:
  - topology
  topics:
  - Symmetric Products
  - Quasifibrations
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.K, Exercise 3 and the corrected current statement of Lemma 4K.3 where relevant; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the argument into numbered steps. Supplied three things the prose asserted in passing:
    that every orbit of the permutation action has exactly one weakly increasing representative
    (existence by sorting, uniqueness by comparing positions); that the quotient SP_n(I) is Hausdorff,
    which the card previously justified by the phrase "finite sets separated by disjoint saturated
    open sets" and which is now proved by the metric d'([x],[y]) = min over sigma of the sup-distance,
    a metric inducing the quotient topology and hence making the space Hausdorff, so the compact-to-
    Hausdorff bijection theorem applies; and that the simplex map is a bijection in both directions
    with y_i >= 0 and the sum equal to 1. Not re-read this session: printed p. 481.
---

::: {.problem}
Show that $SP_n(I) = \Delta^n$.
:::

::: {.solution}

The argument is the card's own; no retained solution set in `tmp/sources` covers Section 4.K Exercise 3. The statement was checked against Hatcher, *Algebraic Topology* (2002), §4.K Exercise 3, with the symmetric product defined on printed p. 481.

Let $I=[0,1]$, let $\Sigma_{n}$ act on $I^{n}$ by permuting coordinates, and let $SP_{n}(I)=I^{n}/\Sigma_{n}$ be the quotient with the quotient topology.

::: pf

::: {.pf-step #representative}
Every orbit of $\Sigma_{n}$ on $I^{n}$ contains exactly one point with $0\leq x_{1}\leq\cdots\leq x_{n}\leq1$.

::: pf-proof
Existence: given $(x_{1},\dots,x_{n})$, arrange the same multiset of numbers in nondecreasing order; the result is a permutation of the original tuple, hence in its orbit, and lies in $I^{n}$ since all entries do. Uniqueness: if $x$ and $y$ are weakly increasing permutations of one another, then for each $k$ the $k$-th smallest entry of the multiset is $x_{k}$ and also $y_{k}$, so $x_{k}=y_{k}$ for all $k$.
:::

:::

::: {.pf-step #bijection}
The restriction $Q\to SP_{n}(I)$ of the quotient map is a continuous bijection, where $Q=\{x\in I^{n}\mid x_{1}\leq\cdots\leq x_{n}\}$.

::: pf-proof
Continuity is inherited from the quotient map. It is injective because two points of $Q$ in the same orbit are equal by step [](#representative){.pf-ref}, and surjective because every orbit meets $Q$ by the same step.
:::

:::

::: {.pf-step #hausdorff}
$SP_{n}(I)$ is Hausdorff.

::: pf-proof
Define $d'([x],[y])=\min_{\sigma\in\Sigma_{n}}d(x,\sigma y)$ where $d$ is the sup metric on $I^{n}$. This is well defined (independent of the representatives, since permuting either point only permutes the finite set of numbers being minimised over), symmetric, positive for distinct classes by step [](#representative){.pf-ref}, and satisfies the triangle inequality because $d(x,\sigma y)\leq d(x,\tau z)+d(\tau z,\sigma y)$ for every $\sigma,\tau$, and the right side is at least $d'([x],[z])+d'([z],[y])$ after taking the minimum. It induces the quotient topology: the balls of $d'$ are exactly the images of the $\Sigma_{n}$-saturated unions of balls of $d$, since $d'([x],[y])<\varepsilon$ iff some $\sigma y$ lies within $\varepsilon$ of $x$. A metrizable space is Hausdorff.
:::

:::

::: {.pf-step #homeo}
$Q\to SP_{n}(I)$ is a homeomorphism.

::: pf-proof
$Q$ is a closed bounded subset of $I^{n}$, hence compact, and $SP_{n}(I)$ is Hausdorff by step [](#hausdorff){.pf-ref}. A continuous bijection from a compact space to a Hausdorff space is a homeomorphism, so the map of step [](#bijection){.pf-ref} is one.
:::

:::

::: {.pf-step #simplex}
The map $x\mapsto(y_{0},\dots,y_{n})$ with $y_{0}=x_{1}$, $y_{i}=x_{i+1}-x_{i}$ for $1\leq i\leq n-1$ and $y_{n}=1-x_{n}$ is a bijection from $Q$ onto $\Delta^{n}=\{y\geq0\mid\sum y_{i}=1\}$, with inverse $x_{j}=y_{0}+\cdots+y_{j-1}$.

::: pf-proof
For $x\in Q$ each $y_{i}\geq0$ because the coordinates are weakly increasing and $x_{n}\leq1$, and $\sum_{i=0}^{n}y_{i}=x_{1}+(x_{2}-x_{1})+\cdots+(x_{n}-x_{n-1})+(1-x_{n})=1$, so the image lies in $\Delta^{n}$. Conversely if $y\in\Delta^{n}$ then the partial sums $x_{j}=y_{0}+\cdots+y_{j-1}$ are weakly increasing, and $x_{n}=1-y_{n}\leq1$, so $x\in Q$; the two formulas are mutually inverse by the telescoping identities, and both maps are linear, hence continuous.
:::

:::

::: {.pf-step}
$SP_{n}(I)\cong\Delta^{n}$.

::: pf-proof
Composing the homeomorphism of step [](#homeo){.pf-ref} with the homeomorphism of step [](#simplex){.pf-ref} gives a homeomorphism $SP_{n}(I)\to\Delta^{n}$: an element of the symmetric product is an unordered $n$-tuple of points of $I$, which is identified with the weakly increasing representative of its orbit, which in turn corresponds to a point of the standard $n$-simplex.
:::

:::

:::

:::
