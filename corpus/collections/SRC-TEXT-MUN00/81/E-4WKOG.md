---
schema: qual/card@1
id: E-4WKOG
kind: problem
title: Properly discontinuous actions with compactly supported interference
classification:
  areas:
  - topology
  topics:
  - Covering Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 81 Exercise 6, printed p. 494. The theorem that a fixed-point-free action whose elements move each compact set off all but finitely many of its images is properly discontinuous, proved by a compactness argument. Checked against the definition of proper discontinuity, printed p. 488. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Corrected: the definition of a properly discontinuous action is on printed p. 490, not p. 488 as the previous note said. The old solution was not a Lamport proof: its four top-level steps carried indented prose labelled "Proof:" instead of pf-proof blocks, the inner steps had no proofs at all, and a literal "Q.E.D." was typed into the last one. It is now a pf block with one step for each printed part, and every step cites Munkres by number and page: the definition of local compactness (printed p. 182), Theorem 26.3 (printed p. 165) that a compact subspace of a Hausdorff space is closed, Theorem 26.5 (printed p. 166) that a continuous image of a compact space is compact, the definition of the quotient topology (printed p. 137), and the definition of a properly discontinuous action (printed p. 490). Two things were added because the old proof asserted them in passing: that the set of indices F in part (b) is finite, which needs the hypothesis applied to K_x union K_y, and that p(U) and p(V) are disjoint, which needs the translation of an equality p(u) = p(v) into u lying in some g(V). What the certificate does not cover: part (c) is the printed assertion that the action is properly discontinuous, and its proof uses only the hypothesis and Hausdorffness, not part (a).
---

::: {.exercise}

Prove the following.

Theorem.
Let $X$ be a locally compact Hausdorff space; let $G$ be a group of homeomorphisms of $X$ such that the action of $G$ is fixed-point free.
Suppose that for each compact subspace $C$ of $X$, there are only finitely many elements $g$ of $G$ such that the intersection $C \cap g(C)$ is nonempty.
Then the action of $G$ is properly discontinuous, and $X/G$ is locally compact Hausdorff.

(a) For each compact subspace $C$ of $X$, show that the union of the sets $g(C)$, for $g \in G$, is closed in $X$.
[Hint: If $U$ is a neighborhood of $x$ with $\overline{U}$ compact, then $\overline{U} \cup C$ intersects $g(\overline{U} \cup C)$ for only finitely many $g$.]

(b) Show that $X/G$ is Hausdorff.

(c) Show the action of $G$ is properly discontinuous.

(d) Show $X/G$ is locally compact.

:::

::: {.solution}

Write $p:X\to X/G$ for the quotient map; a subset $O$ of $X/G$ is open exactly when $p^{-1}(O)$ is open in $X$ (Definition of the quotient topology, printed p. 137), and $p(W)=\{Gx\mid x\in W\}$.

::: pf

::: {.pf-step #closed}

(a) For every compact subspace $C$ of $X$ the union $\bigcup_{g\in G}g(C)$ is closed in $X$.

::: pf-proof

::: {.pf-step}

Let $x\in X$ with $x\notin\bigcup_{g\in G}g(C)$. There is an open neighbourhood $U$ of $x$ with $K=\overline{U}$ compact, and the set $F=\{g\in G\mid (K\cup C)\cap g(K\cup C)\ne\varnothing\}$ is finite.

::: {.pf-proof}

$X$ is locally compact, so $x$ lies in a compact subspace $C_x$ of $X$ that contains a neighbourhood of $x$ (definition, printed p. 182); take $U$ inside that neighbourhood, so that $K=\overline{U}$ is a closed subspace of the compact space $C_x$, hence compact (Theorem 26.2, printed p. 165). The set $K\cup C$ is compact, being a union of two compact subspaces, and the hypothesis applied to it gives that $F$ is finite.

:::

:::

::: {.pf-step}

There is an open neighbourhood $V$ of $x$ disjoint from $\bigcup_{g\in G}g(C)$.

::: {.pf-proof}

For $g\notin F$ one has $K\cap g(C)\subseteq(K\cup C)\cap g(K\cup C)=\varnothing$, hence $U\cap g(C)=\varnothing$. For $g\in F$ the set $g(C)$ is compact, being a continuous image of the compact space $C$ (Theorem 26.5, printed p. 166), hence closed in the Hausdorff space $X$ (Theorem 26.3, printed p. 165), and $x\notin g(C)$. So
$$
V=U\cap\bigcap_{g\in F}\left(X\setminus g(C)\right)
$$
is an open neighbourhood of $x$, an intersection of finitely many open sets, and it misses $g(C)$ for every $g$: for $g\in F$ by construction, for $g\notin F$ because $V\subseteq U$.

:::

:::

:::

:::

::: {.pf-step #hausdorff}

(b) $X/G$ is Hausdorff.

::: pf-proof

::: {.pf-step #openmap}

$p$ is an open map.

::: {.pf-proof}

For open $W\subseteq X$ the set $p^{-1}p(W)=\bigcup_{g\in G}g(W)$ is a union of open sets, hence open, so $p(W)$ is open by the definition of the quotient topology (printed p. 137).

:::

:::

::: {.pf-step}

The two points $p(x)\ne p(y)$ have disjoint open neighbourhoods.

::: {.pf-proof}

The orbits $Gx$ and $Gy$ are disjoint. Choose open neighbourhoods $U_x$ of $x$ and $U_y$ of $y$ with compact closures $K_x=\overline{U_x}$ and $K_y=\overline{U_y}$, possible by local compactness as in step [](#closed){.pf-ref}. The set
$$
F=\{g\in G\mid K_x\cap g(K_y)\ne\varnothing\}
$$
is finite, because $K_x\cap g(K_y)\ne\varnothing$ implies $K\cap g(K)\ne\varnothing$ for the compact set $K=K_x\cup K_y$. For $g\in F$ one has $x\ne g(y)$, since $x\in Gx$ and $g(y)\in Gy$ lie in disjoint orbits, so there are disjoint open sets $V_g\ni x$ and $W_g\ni g(y)$. Set
$$
U=U_x\cap\bigcap_{g\in F}V_g,\qquad V=U_y\cap\bigcap_{g\in F}g^{-1}(W_g),
$$
open neighbourhoods of $x$ and $y$. For $g\in F$ one has $U\subseteq V_g$ and $g(V)\subseteq W_g$, so $U\cap g(V)=\varnothing$; for $g\notin F$ one has $U\subseteq K_x$ and $g(V)\subseteq g(K_y)$, so $U\cap g(V)\subseteq K_x\cap g(K_y)=\varnothing$. Hence $U\cap g(V)=\varnothing$ for every $g\in G$. If $p(u)=p(v)$ for $u\in U$ and $v\in V$, then $u=g(v)$ for some $g\in G$, contradicting $U\cap g(V)=\varnothing$. So $p(U)$ and $p(V)$ are disjoint, and they are open neighbourhoods of $p(x)$ and $p(y)$ by step [](#openmap){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #pd}

(c) The action of $G$ is properly discontinuous.

::: pf-proof

Let $x\in X$ and choose an open neighbourhood $U_0$ of $x$ with $C=\overline{U_0}$ compact. The set
$$
F=\{g\in G\setminus\{e\}\mid C\cap g(C)\ne\varnothing\}
$$
is finite by hypothesis. For $g\in F$ the action is fixed-point free and $g$ is a homeomorphism, so $g(x)\ne x$, and by the Hausdorff condition there are disjoint open sets $V_g\ni x$ and $W_g\ni g(x)$. Put
$$
U=U_0\cap\bigcap_{g\in F}\left(V_g\cap g^{-1}(W_g)\right),
$$
an open neighbourhood of $x$. For $g\in F$ one has $U\subseteq V_g$ and $g(U)\subseteq W_g$, so $g(U)\cap U=\varnothing$; for $g\notin F$ with $g\ne e$ one has $U\subseteq C$ and $g(U)\subseteq g(C)$, so $g(U)\cap U\subseteq g(C)\cap C=\varnothing$. Hence $g(U)\cap U=\varnothing$ for every $g\ne e$, which is the definition of a properly discontinuous action (printed p. 490).

:::

:::

::: {.pf-step}

(d) $X/G$ is locally compact.

::: pf-proof

Let $p(x)\in X/G$. Since $X$ is locally compact at $x$, there is a compact subspace $K$ of $X$ containing an open neighbourhood $W$ of $x$. Then $p(K)$ is compact, being the continuous image of a compact space (Theorem 26.5, printed p. 166), and $p(W)$ is open by step [](#openmap){.pf-ref}, with $p(x)\in p(W)\subseteq p(K)$. So $p(x)$ has a compact neighbourhood, and $X/G$ is locally compact (definition, printed p. 182); it is Hausdorff by step [](#hausdorff){.pf-ref}.

:::

:::

:::

:::
