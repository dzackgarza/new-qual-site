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
Let \(p:X\to X/G\) be the orbit projection.

For each \(g\in G\), the map \(x\mapsto g\cdot x\) is a homeomorphism. Hence for every open \(U\subset X\),
\[
p^{-1}(p(U))=G\cdot U=\bigcup_{g\in G}gU
\]
is open. Thus \(p\) is an open quotient map.

If \(C\subset X\) is closed, then \(G\cdot C\) is closed. Indeed, the map
\[
\Phi:G\times X\to G\times X,\qquad \Phi(g,x)=(g,g\cdot x)
\]
is a homeomorphism, and
\[
G\cdot C=\pi_X(\Phi(G\times C)).
\]
Since \(G\) is compact, the projection \(G\times X\to X\) is closed. Therefore \(G\cdot C\) is closed. Since
\[
p^{-1}(p(C))=G\cdot C,
\]
the quotient criterion implies \(p(C)\) is closed. Thus \(p\) is closed. Its fibers are the orbits \(G\cdot x\), continuous images of compact \(G\), hence compact. Therefore \(p\) is a perfect map.

The preceding perfect-map exercise now gives immediately:

- if \(X\) is Hausdorff, then \(X/G\) is Hausdorff;
- if \(X\) is regular, then \(X/G\) is regular;
- if \(X\) is locally compact, then \(X/G\) is locally compact;
- if \(X\) is second countable, then \(X/G\) is second countable.

It remains only normality. Let \(A,B\subset X/G\) be disjoint closed sets. Their inverse images \(p^{-1}(A)\) and \(p^{-1}(B)\) are disjoint closed subsets of normal \(X\), so choose disjoint open sets \(U,V\subset X\) containing them. Since \(p\) is closed, the sets
\[
U'= (X/G)\setminus p(X\setminus U),\qquad
V'= (X/G)\setminus p(X\setminus V)
\]
are open. They contain \(A\) and \(B\), respectively, and satisfy
\[
p^{-1}(U')\subset U,\qquad p^{-1}(V')\subset V.
\]
Hence \(U'\cap V'=\varnothing\). Thus \(X/G\) is normal.
:::
