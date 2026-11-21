---
schema: qual/card@1
id: E-T8UBC
kind: problem
title: Graphs as an imbedding of the function space into the hyperspace
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The source defines the Hausdorff space using nonempty closed bounded sets, but a graph need not be bounded and an empty domain gives an empty graph. The graph map is defined here on bounded functions from a nonempty bounded domain.'
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §45 Exercise 8 (printed p. 281) was located; the sets searched are listed in
    the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. The defect recorded in the source-corrected
    event above is real, and the printed statement is now restored on the card (the earlier repair had
    replaced the exercise by a restatement for bounded functions on a bounded domain, which is not the
    printed text). The counterexample is checked against the book's definitions: X = Y = R, f = id, G_f
    the diagonal, closed as the preimage of {0} under the continuous (x,y) -> x - y (Theorem 18.1) and
    unbounded because a ball of radius r about u x u meets it only in points x x x with |x| <= |u| + r,
    so G_f is not in H although f is continuous. Parts (a)--(c) are then proved for the bounded
    continuous functions, the least repair, and part (d) as printed, compactness of X making every
    continuous function bounded (Theorem 26.5) and every graph compact hence closed and bounded. Checked
    against Munkres, Topology (2000), §45 Exercise 8, printed p. 281, with Theorem 18.1, Theorem 18.4,
    Theorem 26.5, Theorem 27.6 and the Hausdorff metric of Exercise 45.7 on the same page. Two further
    corrections: part (a) claimed only that gr is 1-Lipschitz and now states that this is uniform
    continuity; part (c)'s distance estimate, printed as "within 1/n^2", is now the exact value
    1/(k(k+1)) with the bound 1/((n+1)(n+2)), and the example's two functions are checked to be bounded
    with closed graphs, which is what membership in H requires.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout for a published solution of this exercise and found none
    (issue #144). Math StackExchange through the API, site math, with the queries "graph of
    continuous function Hausdorff distance", "Hausdorff distance complete", "hyperspace closed
    bounded sets complete" and "evaluation map uniform topology function space" returns no page
    on graphs of functions as points of a hyperspace; 1309827, 2909498 and 4552398 concern the
    Hausdorff and Gromov--Hausdorff distances themselves. dbFin has no chapter-7 page (404,
    checked 2026-11-15), and no GitHub Munkres repository named in the COMPLAINTS.md entry for
    §30--§36 reaches Chapter 7. The card keeps its own proof, which this pass did not re-read; the
    search is recorded in the COMPLAINTS.md entry for §43--§50 with every query.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    The AoPS blog post by cinnamon_e, "Topology by Munkres Chapter 7 | Day 16" (2025-09-09, listed
    on the blog's topology tag page
    https://artofproblemsolving.com/community/c3401823t440f3401823_topology, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day16.md), also answers this exercise, at its item 8
    of §45. The text is held, but the formulas are not: the extraction drops every inline formula,
    so the answer reads as the words between blanks and cannot be transcribed or checked. It is
    recorded here and in the COMPLAINTS.md entry for §43--§50 as located with its formulas
    unreadable, the site answering an automated request with a Cloudflare human check, which is not
    worked around.

- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; re-checked the repair and all four parts. The repair
    stands: the graph of a continuous f: R -> R need not be bounded, so gr does not map into
    the set of closed bounded subsets, and (a)-(c) are for bounded continuous functions with
    X nonempty, while (d) is unaffected because a compact X has bounded continuous image.
    Checked (a) injectivity and the 1-Lipschitz bound d_H <= sup norm; (b) the epsilon/3
    argument through the definition of Hausdorff distance; (c) that the functions on the
    discrete set {1/k} are continuous and bounded, that the two graphs are within
    1/((n+1)(n+2)) in the Hausdorff metric while sup norm is 2 at the point 1/(n+1), and
    that this f is not uniformly continuous, consistent with (b); (d) compactness of the
    graph and uniform continuity on a compact metric space (Theorem 27.6). No further repair
    needed.
---

::: {.exercise}

Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces; give $X \times Y$ the corresponding square metric; let $\mathcal{H}$ denote the collection of all nonempty closed, bounded subsets of $X \times Y$ in the resulting Hausdorff metric.
Consider the space $\mathcal{C}(X, Y)$ in the uniform metric; let $\operatorname{gr}: \mathcal{C}(X, Y) \to \mathcal{H}$ be the function that assigns, to each continuous function $f: X \to Y$, its graph

$$
G_f = \theset{x \times f(x) \mid x \in X}.
$$

(a) Show that the map $\operatorname{gr}$ is injective and uniformly continuous.

(b) Let $\mathcal{H}_0$ denote the image set of the map $\operatorname{gr}$; let $g: \mathcal{C}(X, Y) \to \mathcal{H}_0$ be the surjective map obtained from $\operatorname{gr}$. Show that if $f: X \to Y$ is uniformly continuous, then the map $g^{-1}$ is continuous at the point $G_f$.

(c) Give an example where $g^{-1}$ is not continuous at the point $G_f$.

(d) Theorem. If $X$ is compact, then $\operatorname{gr}: \mathcal{C}(X, Y) \to \mathcal{H}$ is an imbedding.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. Write $d_{\square}\big((x,y),(x',y')\big)=\max\{d_{X}(x,x'),d_{Y}(y,y')\}$ for the square metric and $d_{H}$ for the Hausdorff metric on $\mathcal{H}$.

::: pf

::: {.pf-step #defect}
As printed, $\operatorname{gr}$ is not a map into $\mathcal{H}$, and the corrected statement restricts it to the bounded continuous functions.

::: pf-proof
Take $X=Y=\RR$ with the usual metric and $f=\operatorname{id}$. Its graph $G_{f}=\{x\times x\}$ is closed, being the preimage of $\{0\}$ under the continuous map $(x,y)\mapsto x-y$ (Theorem 18.1), but it is not bounded: a ball of square radius $r$ about $u\times u$ meets $G_{f}$ only in points $x\times x$ with $\abs{x}\le\abs{u}+r$, so no ball contains $G_{f}$. Hence $G_{f}\notin\mathcal{H}$ although $f$ is continuous. So parts (a)--(c) are proved for
$$
\mathcal{C}_{b}(X,Y)=\{f\in\mathcal{C}(X,Y)\mid f(X)\text{ is bounded in }Y\}
$$
with $X$ nonempty: the graph of a continuous map into a metric space is closed, and boundedness of $f(X)$ is boundedness of the graph, so $\operatorname{gr}$ does land in $\mathcal{H}$. Part (d) needs no repair, because a continuous image of a compact space is compact (Theorem 26.5) and hence bounded, so $\mathcal{C}(X,Y)=\mathcal{C}_{b}(X,Y)$ there.
:::

:::

::: {.pf-step #part-a}
(a) $\operatorname{gr}:\mathcal{C}_{b}(X,Y)\to\mathcal{H}$ is injective and $1$-Lipschitz, hence uniformly continuous.

::: pf-proof
If $G_{f}=G_{h}$ then for every $x$ the point $x\times f(x)$ equals $x\times h(x)$, so $f=h$; that is injectivity. For the estimate, each point $x\times f(x)$ of $G_{f}$ lies at square distance $d_{Y}\big(f(x),h(x)\big)\le\norm{f-h}_{\infty}$ from the point $x\times h(x)$ of $G_{h}$, and symmetrically; so every point of either graph is within $\norm{f-h}_{\infty}$ of the other graph, that is $d_{H}(G_{f},G_{h})\le\norm{f-h}_{\infty}$. A Lipschitz map is uniformly continuous.
:::

:::

::: {.pf-step #part-b}
(b) If $f$ is uniformly continuous, then $g^{-1}$ is continuous at $G_{f}$.

::: pf-proof
Let $\varepsilon>0$ and choose $\delta>0$ with $\delta<\varepsilon/3$ such that $d_{X}(x,x')<\delta$ implies $d_{Y}\big(f(x),f(x')\big)<\varepsilon/3$. Suppose $d_{H}(G_{f},G_{h})<\delta$. For each $x\in X$ the point $x\times f(x)\in G_{f}$ is within $\delta$ of some point $x'\times h(x')\in G_{h}$, so $d_{X}(x,x')<\delta$ and $d_{Y}\big(f(x),h(x')\big)<\delta$. Then
$$
d_{Y}\big(h(x),f(x)\big)\le d_{Y}\big(h(x),f(x')\big)+d_{Y}\big(f(x'),f(x)\big)<\delta+\varepsilon/3<2\varepsilon/3,
$$
so $\norm{h-f}_{\infty}\le2\varepsilon/3<\varepsilon$, the supremum being finite because both functions are bounded. Hence $d_{H}(G_{f},G_{h})<\delta$ forces $d_{\infty}(f,h)<\varepsilon$, which is continuity of $g^{-1}$ at $G_{f}$.
:::

:::

::: {.pf-step #part-c}
(c) There is a case in which $g^{-1}$ is not continuous at $G_{f}$.

:::: pf-proof

::: {.pf-step #c-setup}
Let $X=\{1/k\mid k\in\ZZ_{+}\}$ and $Y=\RR$ with the usual metrics, let $f(1/k)=(-1)^{k}$, and let $h_{n}(1/k)=(-1)^{k}$ for $k\le n$ and $(-1)^{k+1}$ for $k>n$. All these functions are continuous, bounded, and have graphs in $\mathcal{H}$.

::: pf-proof
$X$ is a discrete subspace of $\RR$ (its points are isolated), so every function on it is continuous; $X$ is nonempty and bounded, and all the functions take values in $\{-1,1\}$, so all are bounded. The graph of a continuous map into the metric space $\RR$ is closed (Theorem 18.1), and bounded because $X$ and the values are bounded.
:::

:::

::: {.pf-step #c-distance}
$d_{H}(G_{f},G_{h_{n}})\le1/((n+1)(n+2))$.

::: pf-proof
For $k\le n$ the two functions agree at $1/k$. For $k>n$ one has $h_{n}(1/j)=(-1)^{j+1}=f\big(1/(j+1)\big)$ whenever $j>n$, so the point $1/k\times h_{n}(1/k)$ of $G_{h_{n}}$ equals $1/k\times f\big(1/(k+1)\big)$, which lies at square distance $1/k-1/(k+1)=1/(k(k+1))$ from the point $1/(k+1)\times f\big(1/(k+1)\big)$ of $G_{f}$; symmetrically each point $1/k\times f(1/k)$ of $G_{f}$ with $k>n$ lies at that distance from the point $1/(k+1)\times h_{n}\big(1/(k+1)\big)$ of $G_{h_{n}}$. The values $1/(k(k+1))$ decrease in $k$, so the Hausdorff distance is at most $1/((n+1)(n+2))$.
:::

:::

::: {.pf-step #c-norm}
$\norm{h_{n}-f}_{\infty}=2$ for every $n$, so $g^{-1}$ is not continuous at $G_{f}$.

::: pf-proof
At the point $1/(n+1)$, which lies beyond the first $n$ points, $h_{n}\big(1/(n+1)\big)=(-1)^{n+2}$ and $f\big(1/(n+1)\big)=(-1)^{n+1}$, so $\abs{h_{n}-f}=2$ there and the supremum is $2$. Together with step [](#c-distance){.pf-ref}, graphs arbitrarily close to $G_{f}$ correspond to functions at distance $2$ from $f$, so $g^{-1}$ is not continuous at $G_{f}$. Note also that this $f$ is not uniformly continuous, since $\abs{f(1/k)-f(1/(k+1))}=2$ while $1/k-1/(k+1)\to0$, which is consistent with (b).
:::

:::

::: {.pf-step}
(c) holds.

::: pf-proof
Steps [](#c-setup){.pf-ref}, [](#c-distance){.pf-ref} and [](#c-norm){.pf-ref} give the example.
:::

:::

:::

:::

::: {.pf-step #part-d}
(d) If $X$ is compact, then $\operatorname{gr}:\mathcal{C}(X,Y)\to\mathcal{H}$ is an imbedding.

::: pf-proof
For compact $X$ one has $\mathcal{C}(X,Y)=\mathcal{C}_{b}(X,Y)$ by step [](#defect){.pf-ref}, and each $G_{f}$ is the image of the compact space $X$ under the continuous map $x\mapsto x\times f(x)$ (Theorem 18.4), hence compact (Theorem 26.5) and so an element of $\mathcal{H}$. A continuous map on a compact metric space is uniformly continuous (Theorem 27.6), so step [](#part-b){.pf-ref} applies at every $f$: $g^{-1}$ is continuous on all of $\mathcal{H}_{0}$. With the continuity of $\operatorname{gr}$ from step [](#part-a){.pf-ref}, $\operatorname{gr}$ is a homeomorphism onto its image, that is an imbedding.
:::

:::

::: {.pf-step}
Parts (a)--(d) hold, with (a)--(c) for bounded continuous functions.

::: pf-proof
Steps [](#part-a){.pf-ref}, [](#part-b){.pf-ref}, [](#part-c){.pf-ref} and [](#part-d){.pf-ref} are the four assertions, under the correction recorded in step [](#defect){.pf-ref}.
:::

:::

:::
:::
