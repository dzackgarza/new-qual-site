---
schema: qual/card@1
id: E-HAT-4.K-5
kind: problem
title: Quasifibrations
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.K, Exercise 5 and the corrected current statement of Lemma 4K.3 where relevant; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, and the three parts of Lemma 4K.3 read
    against the book's own statement of the lemma (printed p. 480: (a) B = V_1 union V_2 with the
    three restrictions quasifibrations, (b) B = union B_n with every compact set in some B_n and
    each restriction a quasifibration, (c) a deformation of E into E' covering one of B into B'
    with the restriction over B' a quasifibration and F_1 a weak equivalence on each fiber) and
    against Proposition 4K.1 (printed p. 479), which the printed proof of (a) uses. The card's
    sketch is kept and made explicit: (a) is proved by intersecting with the path component, where
    the printed five-lemma argument applies and the pi_0 clause of condition (i) replaces the
    printed proof's assumption of path-connected fibers; (b) is proved by compactness, giving the
    two colimit identifications and passing the stagewise isomorphisms to the limit; (c) notes that
    the path t -> F-bar_t(b) lies in the component of b, so the configuration is read there. The
    statement and its three conditions are unchanged; the card says the argument is its own.
---

::: {.problem}
A map $p: E \to B$ with $B$ not necessarily path-connected is defined to be a quasifibration if the following equivalent conditions are satisfied:

(i) For all $b \in B$ and $x_0 \in p^{-1}(b)$, the map $p_*: \pi_i(E, p^{-1}(b), x_0) \to \pi_i(B, b)$ is an isomorphism for $i > 0$ and $\pi_0(p^{-1}(b), x_0) \to \pi_0(E, x_0) \to \pi_0(B, b)$ is exact.

(ii) The inclusion of the fiber $p^{-1}(b)$ into the homotopy fiber $F_b$ of $p$ over $b$ is a weak homotopy equivalence for all $b \in B$.

(iii) The restriction of $p$ over each path-component of $B$ is a quasifibration according to the definition in this section.

Show these three conditions are equivalent, and prove Lemma 4K.3 for quasifibrations over non-path-connected base spaces.
:::

::: {.solution}
Fix $b$ and $x_0\in p^{-1}(b)$ and let $F_b$ be the homotopy fiber. Condition (ii) says the inclusion $j\colon p^{-1}(b)\to F_b$, made by the constant path at $b$, is a weak equivalence; comparing the long exact sequences of $(E,p^{-1}(b))$ and $(E_p,F_b)$ through the fibration sequence of \S4.3, with $E_p\simeq E$, turns that into condition (i) with the five lemma, the $\pi_0$ clause included. Conditions (i) and (ii) mention only homotopy classes of maps from spheres and disks based at $b$, so they are conditions on the path component of $b$ alone, which is (iii). The three parts of Lemma 4K.3 are then checked part by part on a path component, the printed proofs being available verbatim there. The argument is this card's own: no retained solution set covers this exercise.

::: pf

::: {.pf-step #setup}
There is an inclusion $j\colon p^{-1}(b)\hookrightarrow F_b$ given by the constant path at $b$, and a fibration sequence $F_b\to E_p\to B$ with $E_p\simeq E$ and $E_p\to B$ a fibration extending $p$.

::: pf-proof
The homotopy fiber of $p$ over $b$ is $F_b=\{(e,\gamma):\gamma$ a path in $B$ from $p(e)$ to $b\}$, and the map $j$ sends $e$ to $(e,c_b)$ with $c_b$ the constant path. The path space replacement $E_p=\{(e,\gamma):\gamma(0)=p(e)\}$ fibres over $B$ by $(e,\gamma)\mapsto\gamma(1)$, this map is a fibration, its fiber over $b$ is $F_b$, and $E\to E_p$, $e\mapsto(e,c_{p(e)})$, is a homotopy equivalence (Proposition 4.65, printed p.~407, in the form that the fiber is the homotopy fiber).
:::

:::


::: {.pf-step #iff-i-ii}
(i) and (ii) are equivalent, for every $b$ and $x_0$.

::: pf-proof
Consider the map of pairs $(E,p^{-1}(b))\to(E_p,F_b)$ induced by the homotopy equivalence $E\to E_p$, and compare the long exact homotopy sequences
$$
\pi_i(p^{-1}(b))\to\pi_i(E)\to\pi_i(E,p^{-1}(b))\xrightarrow{\partial}\pi_{i-1}(p^{-1}(b))\to\cdots
$$
with the corresponding sequence for $(E_p,F_b)$, whose $\pi_i(E_p)=\pi_i(E)$ and whose next-to-last terms are connected by the fibration sequence of $F_b\to E_p\to B$. The map $j$ induces the comparison on the fiber terms, and the five lemma gives that $\pi_i(E,p^{-1}(b),x_0)\to\pi_i(E_p,F_b,x_0)$ is an isomorphism for all $i>0$ exactly when $j_*\colon\pi_i(p^{-1}(b))\to\pi_i(F_b)$ is, i.e. exactly when $j$ is a weak equivalence. Composing with the isomorphisms $\pi_i(E_p,F_b)\cong\pi_i(B,b)$ supplied by the fibration sequence identifies the first condition with (i) for $i>0$; and the exactness of $\pi_0(p^{-1}(b),x_0)\to\pi_0(E,x_0)\to\pi_0(B,b)$, whose last term is a point when $B$ is path-connected, is exactly the $\pi_0$ clause of the fibration sequence at $b$, so the same comparison handles it.
:::

:::


::: {.pf-step #iff-ii-iii}
(ii) and (iii) are equivalent.

::: pf-proof
Condition (ii) at a point $b$ involves the fiber $p^{-1}(b)$, the homotopy fiber $F_b$, and homotopy groups based at points of $p^{-1}(b)$; all of these depend only on the path component $B_b$ of $b$ and on $p^{-1}(B_b)$, because a path in $B$ from $p(e)$ to $b$ stays in $B_b$ and any such path lies entirely in the component. Hence (ii) holds for every $b\in B$ if and only if, for each path component $B_b$, the restriction $p^{-1}(B_b)\to B_b$ satisfies (ii) at each of its points; and by step [](#iff-i-ii){.pf-ref} that is (iii), the restriction over each path component being a quasifibration in the path-connected sense.
:::

:::


::: {.pf-step #lemma-a}
Lemma 4K.3(a) holds for an arbitrary base: if $B=V_1\cup V_2$ with the three restrictions quasifibrations, then $p$ is a quasifibration.

::: pf-proof
Let $b\in B$ and let $B_b$ be its path component. Put $V_k'=V_k\cap B_b$, which are open in $B_b$ and cover it, and let $p_b$ be the restriction of $p$ over $B_b$. By step [](#iff-ii-iii){.pf-ref} each restriction of $p_b$ over $V_k'$ and over $V_1'\cap V_2'$ is a quasifibration, since it is the restriction of $p$ over the corresponding open subset of $B$. The printed proof of (a) now applies inside the path-connected space $B_b$: the five lemma for the triples $(p_b^{-1}(V_k'),p_b^{-1}(V_1'\cap V_2'),p^{-1}(b))$ over $(V_k',V_1'\cap V_2',b)$ makes $\pi_i$ of the pairs $(p_b^{-1}(V_k'),p_b^{-1}(V_1'\cap V_2'))\to(V_k',V_1'\cap V_2')$ an isomorphism, Proposition 4K.1 (printed p.~479) then makes $\pi_i(E_b,p_b^{-1}(V_k'))\to\pi_i(B_b,V_k')$ an isomorphism, and a second five-lemma gives $\pi_i(E_b,p^{-1}(b))\to\pi_i(B_b,b)$ an isomorphism for $i>0$, together with the $\pi_0$ exactness. So $p_b$ is a quasifibration, and by step [](#iff-ii-iii){.pf-ref} $p$ is one. The printed proof's assumption that fibers are path-connected is not needed here, because condition (i) carries the $\pi_0$ clause that the usual argument reads off from that assumption.
:::

:::


::: {.pf-step #lemma-b}
Lemma 4K.3(b) holds for an arbitrary base: if $B=\bigcup_nB_n$ with every compact set in some $B_n$ and each $p^{-1}(B_n)\to B_n$ a quasifibration, then $p$ is a quasifibration.

::: pf-proof
Fix $b$ and $i\ge1$. A class in $\pi_i(E,p^{-1}(b))$ is represented by a map of the disk $D^i$ into $E$ carrying $\partial D^i$ into $p^{-1}(b)$, and a homotopy between two such classes is represented by a map of $D^i\times I$; these domains are compact, so their images in $B$ are compact and hence lie in some $B_n$. Therefore the natural maps
$$
\varinjlim_n\pi_i(p^{-1}(B_n),p^{-1}(b))\to\pi_i(E,p^{-1}(b))
$$
are bijections, and the same compactness gives $\varinjlim_n\pi_i(B_n,b)=\pi_i(B,b)$. For each $n$ the restriction over $B_n$ is a quasifibration, so $\pi_i(p^{-1}(B_n),p^{-1}(b))\cong\pi_i(B_n,b)$, and passing to the colimit gives the isomorphism of condition (i) at $b$. For $\pi_0$: a point of $E$ lies in some $p^{-1}(B_n)$ and a path in $B$ from $p(e)$ to $b$ has compact image in some $B_m$, so the exactness clause also reduces to the finite stages, where it holds. As $b$ was arbitrary, $p$ is a quasifibration.
:::

:::


::: {.pf-step #lemma-c}
Lemma 4K.3(c) holds for an arbitrary base: if $F_t$ is a deformation of $E$ into $E'$ covering a deformation $\overline F_t$ of $B$ into $B'$, the restriction over $B'$ is a quasifibration, and $F_1\colon p^{-1}(b)\to p^{-1}(\overline F_1(b))$ is a weak equivalence for every $b$, then $p$ is a quasifibration.

::: pf-proof
For $b\in B$ the path $t\mapsto\overline F_t(b)$ lies in the path component $B_b$ of $b$, so $\overline F_1(b)\in B_b$ and $E'$ meets $p^{-1}(B_b)$; thus the whole configuration can be read inside the path component of $b$, which is where the printed proof of (c) takes place. There, the deformation gives a homotopy equivalence of pairs $(E,p^{-1}(b))\to(E',p^{-1}(\overline F_1(b)))$, hence isomorphisms $\pi_i(E,p^{-1}(b))\cong\pi_i(E',p^{-1}(\overline F_1(b)))$; the hypothesis that $F_1$ on the fiber is a weak equivalence identifies $p^{-1}(b)$ with the fiber of $E'$ over $\overline F_1(b)$ up to homotopy; and the quasifibration property of $E'\to B'$ supplies $\pi_i(E',p^{-1}(\overline F_1(b)))\cong\pi_i(B',\overline F_1(b))$, which is $\pi_i(B,b)$ because $\overline F_t$ is a deformation retraction. The $\pi_0$ exactness follows from the same chain of identifications. So condition (i) holds at every $b$, and $p$ is a quasifibration.
:::

:::


::: {.pf-step #conclusion}
Conditions (i), (ii) and (iii) are equivalent, and the three criteria of Lemma 4K.3 hold for quasifibrations over non-path-connected bases.

::: pf-proof
Step [](#iff-i-ii){.pf-ref} gives (i) $\Leftrightarrow$ (ii) and step [](#iff-ii-iii){.pf-ref} adds (iii); steps [](#lemma-a){.pf-ref}, [](#lemma-b){.pf-ref} and [](#lemma-c){.pf-ref} extend the three printed criteria, each by the reduction of the problem to a single path component, where the printed proof applies unchanged.
:::

:::

:::
:::
