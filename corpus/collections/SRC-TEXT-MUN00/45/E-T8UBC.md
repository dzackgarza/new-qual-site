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
    No complete published solution of Munkres §45 Exercise 8 was located; the sets searched are listed in
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
Write $d_\square((x,y),(x',y'))=\max\{d_X(x,x'),d_Y(y,y')\}$ and $d_H$ for the Hausdorff metric.

**A defect in the printed statement, and the corrected statement.** As printed, $\operatorname{gr}$ is not a function into $\mathcal{H}$: boundedness of the graph does not follow from continuity. Take $X=Y=\RR$ with the usual metric and $f=\operatorname{id}$. Then $G_f=\{x\times x\mid x\in\RR\}$ is closed in $\RR^2$, being the preimage of $\{0\}$ under the continuous map $(x,y)\mapsto x-y$ (Theorem 18.1), and it is unbounded: a ball of radius $r$ about $u\times u$ meets $G_f$ only in points $x\times x$ with $\abs{x}\le\abs{u}+r$, so no ball about any point contains $G_f$. Hence $G_f\notin\mathcal{H}$ although $f$ is continuous, and the same holds for every unbounded continuous $f:\RR\to\RR$.

So parts (a)--(c) are proved for the bounded continuous functions, that is for
$$
\mathcal{C}_b(X,Y)=\{f\in\mathcal{C}(X,Y) \mid f(X) \text{ is bounded in } Y\},
$$
whose graphs are bounded, and for nonempty $X$, so that graphs are nonempty; the graph of a continuous map into a metric space is closed, so $\operatorname{gr}$ does map $\mathcal{C}_b(X,Y)$ into $\mathcal{H}$. Part (d) needs no repair: if $X$ is compact then $f(X)$ is compact (Theorem 26.5), hence bounded in $Y$, so $\mathcal{C}(X,Y)=\mathcal{C}_b(X,Y)$ and each $G_f$ is compact, hence closed and bounded, in $X\times Y$. Below, $\operatorname{gr}$ is the map on $\mathcal{C}_b(X,Y)$ in (a)--(c) and on $\mathcal{C}(X,Y)$ in (d).

(a) Distinct functions have distinct graphs, so $\operatorname{gr}$ is injective. If $\norm{f-h}_\infty<\varepsilon$, then for every $x$, $(x,f(x))$ lies within $\varepsilon$ of $(x,h(x))$, and conversely. Thus
$$
d_H(G_f,G_h)\le \norm{f-h}_\infty,
$$
so the graph map is $1$-Lipschitz, hence uniformly continuous.

(b) Fix uniformly continuous $f$ and $\varepsilon>0$. Choose $\delta<\varepsilon/3$ so that $d_X(x,x')<\delta$ implies $d_Y(f(x),f(x'))<\varepsilon/3$. If $d_H(G_f,G_h)<\delta$, then for each $x$ there is $x'$ with
$$
d_X(x,x')<\delta,\qquad d_Y(h(x),f(x'))<\delta.
$$
Hence
$$
d_Y(h(x),f(x))<\delta+\varepsilon/3<2\varepsilon/3.
$$
Taking the supremum over $x$ gives $\norm{h-f}_\infty\le 2\varepsilon/3<\varepsilon$, both functions being bounded. Thus $g^{-1}$ is continuous at $G_f$.

(c) Take $X=\{1/k:k\in\ZZ_+\}\subset\RR$ and $Y=\RR$, with the usual metrics. The space $X$ is discrete, so every function on it is continuous; it is nonempty and bounded. Let $f(1/k)=(-1)^k$, and for $n\ge1$ let $h_n(1/k)=(-1)^k$ for $k\le n$ and $h_n(1/k)=(-1)^{k+1}$ for $k>n$. Both take values in $\{-1,1\}$, so they are bounded, and their graphs are closed because the functions are continuous.

Since $h_n(1/j)=f(1/(j+1))$ for $j>n$, for $k>n$ the point $(1/k,h_n(1/k))=(1/k,f(1/(k+1)))$ of $G_{h_n}$ lies at square distance $1/k-1/(k+1)=1/(k(k+1))$ from the point $(1/(k+1),f(1/(k+1)))$ of $G_f$; and the point $(1/k,f(1/k))=(1/k,h_n(1/(k+1)))$ of $G_f$ lies at that same distance from the point $(1/(k+1),h_n(1/(k+1)))$ of $G_{h_n}$. The points with $k\le n$ are common to both graphs. Hence
$$
d_H(G_f,G_{h_n})\le\frac{1}{(n+1)(n+2)}\longrightarrow0.
$$
But $\abs{h_n(1/(n+1))-f(1/(n+1))}=2$, so $\norm{h_n-f}_\infty=2$ for every $n$. Thus $g^{-1}$ is not continuous at $G_f$. Here $f$ is not uniformly continuous, since $\abs{f(1/k)-f(1/(k+1))}=2$ while $1/k-1/(k+1)\to0$.

(d) Let $X$ be compact. Then $\mathcal{C}(X,Y)=\mathcal{C}_b(X,Y)$, as noted above, and each graph $G_f$ is the image of the compact space $X$ under the continuous map $x\mapsto x\times f(x)$ (Theorem 18.4), hence compact (Theorem 26.5) and so an element of $\mathcal{H}$. A continuous map on a compact metric space is uniformly continuous (Theorem 27.6), so (b) applies to every $f$: the inverse from the image $\mathcal{H}_0$ to $\mathcal{C}(X,Y)$ is continuous at every graph. Together with (a), $\operatorname{gr}$ is a homeomorphism onto its image, hence an imbedding.
:::
