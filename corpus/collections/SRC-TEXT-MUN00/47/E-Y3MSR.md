---
schema: qual/card@1
id: E-Y3MSR
kind: problem
title: Compact closures in the topology of compact convergence
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §47 Exercise 2 (printed p. 293) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against the book's Theorem 46.7, Theorem 29.2,
    Lemma 45.2, Theorem 45.4, Theorem 37.3 and Lemma 46.4. What was corrected: the "only if" direction had
    proved equicontinuity with nets, a technique the book does not use and does not define; it now restricts
    the compact family to a compact neighbourhood K of the point (Theorem 29.2), where compact convergence is
    the uniform topology (Theorem 46.7), and applies Lemma 45.2 to get equicontinuity on K, hence at the point.
    The "converse" embeds C(X,R^n) by restriction into the product over the compact subspaces of X, applies
    Ascoli (Theorem 45.4) in each factor, Tychonoff (Theorem 37.3) to the product of the closures, and Lemma
    46.4 for the continuity of the compatible function, with every point of X having a compact neighbourhood by
    Theorem 29.2. The last sentence records that the square and euclidean metrics on R^n are uniformly
    equivalent, so neither boundedness nor equicontinuity depends on which is used.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The AoPS blog post by cinnamon_e, "Topology by
    Munkres Chapter 7 | Day 17" (2025-09-10,
    https://artofproblemsolving.com/community/c3401823h3646977, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day17.md), answers this exercise at its item 2 of
    §47, and the extraction dropped every inline formula, so the answer cannot be transcribed; the
    site answers an automated request with a Cloudflare human check, which is not worked around.
    Murayama's selection stops at Chapter 4, dbFin has no chapter-7 page, and the Math StackExchange
    searches of this pass for compact closure under pointwise boundedness and equicontinuity,
    recorded in the COMPLAINTS.md entry for §43--§50, returned nothing on the theorem. The card
    keeps its own proof.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the argument already on the card, which is correct in
    outline and in its citations (Theorem 29.2 for compact neighbourhoods, Theorem 46.7 for the
    topology of compact convergence, Lemma 45.2 for totally bounded families being
    equicontinuous, Ascoli and Tychonoff). Added: the continuity of restriction as its own step,
    the reason the compact-neighbourhood set U is a neighbourhood in X, the net characterisation
    that identifies the topology of compact convergence with the initial topology of the
    restrictions, the closedness of the compatibility conditions via agreement of continuous
    maps into a Hausdorff space, and the gluing step in which local compactness is what makes
    the glued function continuous. No statement was changed. Not claimed: a retained solution
    set; the collection's provenance is the Munkres textbook, whose text is not retained here.
---

::: {.exercise}

Prove the following.

Theorem.
If $X$ is a locally compact Hausdorff space, then a subspace $\mathcal{F}$ of $\mathcal{C}(X, \RR^n)$ in the topology of compact convergence has compact closure if and only if $\mathcal{F}$ is pointwise bounded and equicontinuous under either of the standard metrics on $\RR^n$.
:::

::: {.solution}
Throughout $X$ is a locally compact Hausdorff space, $\mathcal{C}(X,\RR^{n})$ carries the topology of compact convergence, and $\mathcal{F}$ is a subspace of it: pointwise bounded means that for each $x \in X$ the set $\theset{f(x) \mid f \in \mathcal{F}}$ is bounded in $\RR^{n}$, and equicontinuous means that for each $x$ and each $\varepsilon > 0$ there is a neighbourhood $U$ of $x$ with $d\bigl(f(y),f(x)\bigr) < \varepsilon$ for every $y \in U$ and every $f \in \mathcal{F}$, where $d$ is either of the standard metrics on $\RR^{n}$. For a compact subspace $K$ write $\rho_{K}\colon\mathcal{C}(X,\RR^{n}) \to \mathcal{C}(K,\RR^{n})$ for restriction, the target carrying the uniform metric. The exercise is Munkres, *Topology* (2000), §47.

::: pf

::: {.pf-step #evaluation}
If $\overline{\mathcal{F}}$ is compact in the topology of compact convergence, then $\mathcal{F}$ is pointwise bounded.

::: pf-proof
For fixed $x$ the evaluation $\operatorname{ev}_{x}\colon\mathcal{C}(X,\RR^{n}) \to \RR^{n}$, $f \mapsto f(x)$, is continuous in the topology of compact convergence, because that topology is finer than the topology of pointwise convergence, which is the initial topology of all the evaluations. Hence $\operatorname{ev}_{x}(\overline{\mathcal{F}})$ is compact, and a compact subset of $\RR^{n}$ is bounded, so it contains $\theset{f(x) \mid f \in \mathcal{F}}$ inside a bounded set.

:::

:::

::: {.pf-step #restriction-continuous}
For every compact $K \subseteq X$ the map $\rho_{K}$ is continuous.

::: pf-proof
A basic neighbourhood in the uniform topology of $\mathcal{C}(K,\RR^{n})$ is determined by $\varepsilon > 0$ and asks that the supremum of $d$ over $K$ be small; the corresponding condition on $\mathcal{C}(X,\RR^{n})$, uniformity on the compact set $K$ within $\varepsilon$, is one of the defining conditions of the topology of compact convergence.

:::

:::

::: {.pf-step #equicontinuous}
If $\overline{\mathcal{F}}$ is compact then $\mathcal{F}$ is equicontinuous.

::: pf-proof
Let $x \in X$. Since $X$ is locally compact and Hausdorff, $x$ has a compact neighbourhood $K$: the compact neighbourhoods form a base of neighbourhoods at each point, as in §29 of the book. By step [](#restriction-continuous){.pf-ref} the image $\rho_{K}(\overline{\mathcal{F}})$ is compact in $\mathcal{C}(K,\RR^{n})$ with the uniform metric, which is the topology of compact convergence there because $K$ is itself compact. A compact subset of a metric space is totally bounded, so $\rho_{K}(\overline{\mathcal{F}})$ is totally bounded; by the equicontinuity half of Ascoli's theorem (Lemma 45.2 of the book), a totally bounded family in $\mathcal{C}(K,\RR^{n})$ is equicontinuous. Hence for $\varepsilon > 0$ there is a set $U$, open in $K$ and containing $x$, with $d(f(y),f(x)) < \varepsilon$ for all $y \in U$ and $f \in \mathcal{F}$; and $U$ is a neighbourhood of $x$ in $X$ because $K$ is one.

:::

:::

::: {.pf-step #initial}
The topology of compact convergence on $\mathcal{C}(X,\RR^{n})$ is the initial topology of the family $\theset{\rho_{K}}$ over all compact $K \subseteq X$.

::: pf-proof
A net $f_{\alpha}$ converges to $f$ in the topology of compact convergence exactly when the numbers $\sup_{y \in K}d(f_{\alpha}(y),f(y))$ tend to $0$ for every compact $K$, that is exactly when $\rho_{K}(f_{\alpha}) \to \rho_{K}(f)$ in the uniform metric for every compact $K$. Agreement of the convergent nets is agreement of the topologies, so the given topology is the initial one; this is the book's Theorem 46.7.

:::

:::

::: {.pf-step #factor}
Conversely, if $\mathcal{F}$ is pointwise bounded and equicontinuous, then $\rho_{K}(\mathcal{F})$ has compact closure in $\mathcal{C}(K,\RR^{n})$ for every compact $K$.

::: pf-proof
The restricted family is pointwise bounded, because $\rho_{K}(f)(x) = f(x)$ and $\mathcal{F}$ is pointwise bounded at each $x \in K$; and it is equicontinuous, because the neighbourhoods witnessing equicontinuity of $\mathcal{F}$ serve their restrictions. Ascoli's theorem for the compact space $K$ then gives that its closure is compact in the uniform topology.

:::

:::

::: {.pf-step #product}
The image of $\mathcal{F}$ under $\rho \coloneqq \prod_{K}\rho_{K}$ has compact closure in $\prod_{K}\mathcal{C}(K,\RR^{n})$, and the space of compatible families is a closed subset of that product.

::: pf-proof
By step [](#factor){.pf-ref} the closure of the image lies in $\prod_{K}\overline{\rho_{K}(\mathcal{F})}$, a product of compact spaces, which is compact by Tychonoff's theorem; a closed subset of a compact space is compact, so the closure of the image is compact. A family $(g_{K})$ is compatible when $g_{K}$ and $g_{K'}$ agree on $K \cap K'$ for all compact $K, K'$. Each condition is the equality of two continuous maps on the whole product, and the product is Hausdorff, so the set where two continuous maps agree is closed; the compatible families are the intersection of these closed sets, hence closed.

:::

:::

::: {.pf-step #glue}
Gluing gives an inverse: a compatible family $(g_{K})$ is the family of restrictions of exactly one continuous $g \in \mathcal{C}(X,\RR^{n})$, and $\rho$ is a homeomorphism of $\mathcal{C}(X,\RR^{n})$ onto the compatible families.

::: pf-proof
Given a compatible family, define $g(x) \coloneqq g_{K}(x)$ for any compact $K$ containing $x$; compatibility makes this independent of $K$, and any two choices agree. For continuity at $x$ take a compact neighbourhood $N$ of $x$; on $N$ the function $g$ equals $g_{N}$, which is continuous, so $g$ is continuous at $x$. Uniqueness is clear, and every continuous $g$ gives a compatible family, so $\rho$ is a bijection onto the compatible families. It is continuous because each $\rho_{K}$ is, by definition of the initial topology; a continuous bijection onto its image that is an initial map has continuous inverse, so $\rho$ is a homeomorphism onto that image.

:::

:::

::: {.pf-step #converse}
If $\mathcal{F}$ is pointwise bounded and equicontinuous then $\overline{\mathcal{F}}$ is compact in the topology of compact convergence.

::: pf-proof
$\rho$ is a homeomorphism by step [](#glue){.pf-ref}, so $\rho(\overline{\mathcal{F}})$ is the closure in the compatible families of $\rho(\mathcal{F})$, hence closed in the compact space of step [](#product){.pf-ref} intersected with the compatible families; a closed subset of a compact space is compact. Therefore $\overline{\mathcal{F}}$, its homeomorphic preimage, is compact.

:::

:::

::: pf-step
The theorem holds: $\overline{\mathcal{F}}$ is compact in the topology of compact convergence if and only if $\mathcal{F}$ is pointwise bounded and equicontinuous.

::: pf-proof
Steps [](#evaluation){.pf-ref} and [](#equicontinuous){.pf-ref} give the two conditions under the hypothesis of compact closure, and step [](#converse){.pf-ref} gives compact closure under the two conditions. Replacing the metric on $\RR^{n}$ by the other standard one changes neither pointwise boundedness nor equicontinuity, since the two metrics are uniformly equivalent, so the criterion is the same for either.

:::

:::

:::
:::
