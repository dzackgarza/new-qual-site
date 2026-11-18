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
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S31.pdf, Exercise 31.8, page 3 of the file
    (tmp/sources/munkres-solutions-poulsen-S31.pdf, Internet Archive snapshot 20191101081351 of
    web.math.ku.dk/~moller/e02/3gt/opg/S31.pdf), checked against Munkres, Topology (2000), Section
    31 Exercise 8, printed p. 200, Theorem 26.5 and Exercise 26.13. Moller's route is the one on the
    card: the orbit map is perfect, which he proves by showing that the saturation GA of a closed A
    is closed -- for y outside GA and each g in G there are open U_g containing g and V_g containing
    y with U_g^{-1}V_g inside X - A, finitely many U_g cover the compact G, and the intersection of
    the corresponding V_g is a neighbourhood of y inside X - GA -- and that the orbits are compact
    images of G. The five properties then follow from Exercises 31.6 and 31.7, which the card
    repeats for normality because that exercise does not include it. This supersedes the previous
    note, which recorded that no published solution had been found.
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

No complete published solution of Munkres §31 Exercise 8, printed p. 200, was located; the argument is the card's own, following the hint there to Exercise 13 of §26, and the sets searched are recorded in the audit trail.

Let $G$ be a compact topological group acting continuously on $X$, let $p:X\to X/G$ be the quotient map, and for $S\subset X$ write $G\cdot S=\{g\cdot x:g\in G,\ x\in S\}$.

::: pf

::: {.pf-step #open}
$p$ is open.

::: pf-proof
For $g\in G$ the map $x\mapsto g\cdot x$ is a homeomorphism of $X$, being the restriction of the continuous action to $\{g\}\times X$ with inverse $x\mapsto g^{-1}\cdot x$; so $gU$ is open for open $U$. Hence $p^{-1}\big(p(U)\big)=G\cdot U=\bigcup_{g\in G}gU$ is open, and $p(U)$ is open because $p$ is a quotient map (§22, printed p. 137).
:::

:::

::: {.pf-step #closed}
$p$ is closed.

::: pf-proof

::: {.pf-step #orbit-closed}
$G\cdot C$ is closed for every closed $C\subset X$.

::: pf-proof
The map $\Phi:G\times X\to G\times X$, $\Phi(g,x)=(g,g\cdot x)$, is a homeomorphism, with inverse $(g,y)\mapsto(g,g^{-1}\cdot y)$, continuous because the action and the inversion of $G$ are continuous. So $\Phi(G\times C)$ is closed. The projection $\pi_{X}:G\times X\to X$ is closed because $G$ is compact: if $A\subset G\times X$ is closed and $x\notin\pi_{X}(A)$, then $(G\times X)\setminus A$ is an open set containing the slice $G\times\{x\}$, so by the tube lemma it contains a tube $G\times W$ with $W$ a neighbourhood of $x$, and then $W\cap\pi_{X}(A)=\varnothing$ (Lemma 26.8 and its use, printed p. 167). Hence $G\cdot C=\pi_{X}\big(\Phi(G\times C)\big)$ is closed.
:::

:::

::: {.pf-step #closed-quotient}
$p(C)$ is closed for every closed $C\subset X$.

::: pf-proof
$p^{-1}\big(p(C)\big)=G\cdot C$ is closed by step [](#orbit-closed){.pf-ref}, and a quotient map is closed exactly when the image of every closed saturated set is closed (§22, printed p. 137).
:::

:::

::: {.pf-qed}
Steps [](#open){.pf-ref} and [](#closed-quotient){.pf-ref} show that $p$ is a continuous open and closed surjection.
:::

:::

:::

::: {.pf-step #perfect}
$p$ is a perfect map.

::: pf-proof
$p$ is continuous and surjective as a quotient map, and closed by step [](#closed){.pf-ref}. For $y\in X/G$ the fibre $p^{-1}(y)$ is the orbit $G\cdot x$ of a point $x$ with $p(x)=y$, which is the continuous image of the compact space $G$ under $g\mapsto g\cdot x$, hence compact (Theorem 26.5). A closed continuous surjection with compact fibres is a perfect map (§26, Exercise 13).
:::

:::

::: {.pf-step #four-properties}
If $X$ is Hausdorff, regular, locally compact, or second countable, then so is $X/G$.

::: pf-proof
The image of a space with each of these four properties under a perfect map has it (Exercise 13 of §26), and $p$ is perfect by step [](#perfect){.pf-ref}.
:::

:::

::: {.pf-step #normal}
If $X$ is normal, then $X/G$ is normal.

::: pf-proof
Let $A,B\subset X/G$ be disjoint closed sets; then $p^{-1}(A)$ and $p^{-1}(B)$ are disjoint closed subsets of the normal space $X$, so there are disjoint open $U,V\subset X$ with $p^{-1}(A)\subset U$ and $p^{-1}(B)\subset V$. Put
$$
U'=(X/G)\setminus p(X\setminus U),\qquad V'=(X/G)\setminus p(X\setminus V).
$$
These are open because $p$ is closed by step [](#closed){.pf-ref}. They contain $A$ and $B$: if $a\in A$ and $a=p(x)$ with $x\notin U$, then $x\in p^{-1}(A)\subset U$, a contradiction. And $p^{-1}(U')\subset U$ and $p^{-1}(V')\subset V$, since $p^{-1}\big(p(X\setminus U)\big)\supset X\setminus U$; so $p^{-1}(U'\cap V')\subset U\cap V=\varnothing$, and $p$ being onto gives $U'\cap V'=\varnothing$. Hence $X/G$ is normal.
:::

:::

:::
:::
