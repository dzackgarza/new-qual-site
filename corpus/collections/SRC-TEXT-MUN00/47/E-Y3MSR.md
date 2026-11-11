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
---

::: {.exercise}

Prove the following.

Theorem.
If $X$ is a locally compact Hausdorff space, then a subspace $\mathcal{F}$ of $\mathcal{C}(X, \RR^n)$ in the topology of compact convergence has compact closure if and only if $\mathcal{F}$ is pointwise bounded and equicontinuous under either of the standard metrics on $\RR^n$.
:::

::: {.solution}
Suppose first that $\overline{\mathcal F}$ is compact in compact convergence. Evaluation at each $x$ is continuous in that topology, since the topology of compact convergence contains the topology of pointwise convergence (Theorem 46.7), so $\{f(x):f\in\mathcal F\}$ has compact, hence bounded, closure. Thus $\mathcal F$ is pointwise bounded.

For equicontinuity, let $x\in X$ and let $K$ be a compact subspace of $X$ containing $x$ in its interior (Theorem 29.2: a locally compact Hausdorff space has a basis of compact neighbourhoods). Restriction to $K$ is a continuous map
$$
\mathcal{C}(X,\RR^n)\longrightarrow \mathcal{C}(K,\RR^n)
$$
from the topology of compact convergence on $X$ to the topology of compact convergence on $K$, which is the uniform topology because $K$ is compact (Theorem 46.7). Hence the image of the compact set $\overline{\mathcal F}$ is compact in $\mathcal{C}(K,\RR^n)$, so totally bounded, so equicontinuous under $d$ by Lemma 45.2. Therefore for $\varepsilon>0$ there is a neighbourhood $U$ of $x$ inside $K$ with $d(f(y),f(x))<\varepsilon$ for all $y\in U$ and all $f\in\mathcal F$. So $\mathcal F$ is equicontinuous.

Conversely assume pointwise boundedness and equicontinuity. Embed $C(X,\RR^n)$ by restriction into the product
$$
\prod_{K} C(K,\RR^n),
$$
where $K$ ranges over compact subsets and each factor has the uniform topology. For each $K$, Ascoli says the restricted family has compact closure. Hence the closure of the image of $\mathcal F$ lies in a product of compact spaces, so is compact by Tychonoff. The compatibility conditions on overlaps are closed. A compatible family defines a function on $X$ whose restriction to every compact set is continuous; since every point of the locally compact Hausdorff space $X$ has a compact neighborhood, that function is continuous. So the compatible families are exactly the restrictions of continuous functions, and restriction is a homeomorphism of $C(X,\RR^n)$, in the topology of compact convergence, onto them. Thus $\overline{\mathcal F}$ is compact in compact convergence.

The two standard metrics on $\RR^n$ are uniformly equivalent, so pointwise boundedness and equicontinuity are unchanged by choosing either one.
:::
