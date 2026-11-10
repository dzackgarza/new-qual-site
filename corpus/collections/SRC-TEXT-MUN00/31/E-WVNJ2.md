---
schema: qual/card@1
id: E-WVNJ2
kind: problem
title: Orbit spaces of compact group actions inherit separation properties
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 31 Exercise 8, printed p. 200,
    and its hint to Exercise 13 of Section 26, together with Theorem 26.6 (if Y is compact the
    projection X x Y -> X is closed) and Theorem 18.4. The proof is the standard reduction of the
    orbit map to a perfect map: x -> g.x is a homeomorphism, so p is open; (g,x) -> (g, g.x) is a
    homeomorphism and G x C is compact, so p is closed; the fibres are orbits, continuous images
    of the compact G. Normality is then the closed-image argument of Exercise 31.6, which the
    card repeats because the perfect-map exercise does not include it. No published solution was
    located: "Doug's World" (printed pp. 4-6) ends at Problem 31.7, Orellana's Section 31 stops at
    Exercise 6, Rajaraman's notes have no Section 31, and Whitman, positron0802, shenapse and
    9beach stop before Chapter 4. A set covering it exists in the course notes of Morten Poulsen,
    "Solutions to exercises in Munkres", Section 31, at web.math.ku.dk/~moller/e02/3gt/opg/S31.pdf,
    but that host refused every connection from this machine, so it could not be downloaded,
    paginated or cited. The search is recorded in the COMPLAINTS.md entry for this batch.
---

::: {.exercise}

Let $X$ be a space; let $G$ be a topological group.
An action of $G$ on $X$ is a continuous map $\alpha: G \times X \to X$ such that, denoting $\alpha(g \times x)$ by $g \cdot x$, one has:

(i) $e \cdot x = x$ for all $x \in X$.

(ii) $g_1 \cdot (g_2 \cdot x) = (g_1 \cdot g_2) \cdot x$ for all $x \in X$ and $g_1, g_2 \in G$.

Define $x \sim g \cdot x$ for all $x$ and $g$; the resulting quotient space is denoted $X/G$ and called the orbit space of the action $\alpha$.

Theorem.
Let $G$ be a compact topological group; let $X$ be a topological space; let $\alpha$ be an action of $G$ on $X$.
If $X$ is Hausdorff, or regular, or normal, or locally compact, or second-countable, so is $X/G$.

[Hint: See Exercise 13 of §26.]
:::

::: {.solution}
Let $p:X\to X/G$ be the orbit projection.

For each $g\in G$, the map $x\mapsto g\cdot x$ is a homeomorphism. Hence for every open $U\subset X$,
$$
p^{-1}(p(U))=G\cdot U=\bigcup_{g\in G}gU
$$
is open. Thus $p$ is an open quotient map.

If $C\subset X$ is closed, then $G\cdot C$ is closed. Indeed, the map
$$
\Phi:G\times X\to G\times X,\qquad \Phi(g,x)=(g,g\cdot x)
$$
is a homeomorphism, and
$$
G\cdot C=\pi_X(\Phi(G\times C)).
$$
Since $G$ is compact, the projection $G\times X\to X$ is closed. Therefore $G\cdot C$ is closed. Since
$$
p^{-1}(p(C))=G\cdot C,
$$
the quotient criterion implies $p(C)$ is closed. Thus $p$ is closed. Its fibers are the orbits $G\cdot x$, continuous images of compact $G$, hence compact. Therefore $p$ is a perfect map.

The preceding perfect-map exercise now gives immediately:

- if $X$ is Hausdorff, then $X/G$ is Hausdorff;
- if $X$ is regular, then $X/G$ is regular;
- if $X$ is locally compact, then $X/G$ is locally compact;
- if $X$ is second countable, then $X/G$ is second countable.

It remains only normality. Let $A,B\subset X/G$ be disjoint closed sets. Their inverse images $p^{-1}(A)$ and $p^{-1}(B)$ are disjoint closed subsets of normal $X$, so choose disjoint open sets $U,V\subset X$ containing them. Since $p$ is closed, the sets
$$
U'= (X/G)\setminus p(X\setminus U),\qquad
V'= (X/G)\setminus p(X\setminus V)
$$
are open. They contain $A$ and $B$, respectively, and satisfy
$$
p^{-1}(U')\subset U,\qquad p^{-1}(V')\subset V.
$$
Hence $U'\cap V'=\varnothing$. Thus $X/G$ is normal.
:::
