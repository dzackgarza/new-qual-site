---
schema: qual/card@1
id: E-HAT-1.3-5
kind: problem
title: "The harmonic broom has no simply-connected covering space"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Proved a compact local-injectivity lemma for maps to metric spaces, applied it to a lift of the left edge, and used an explicit circle-valued map to certify that the accumulating rectangle loops are nontrivial.
---

Let $X$ be the subspace of $\mathbb{R}^2$ consisting of the four sides of the square $[0,1] \times [0,1]$ together with the segments of the vertical lines $x = 1/2, 1/3, 1/4, \ldots$ inside the square.
Show that for every covering space $\tilde{X} \to X$ there is some neighborhood of the left edge of $X$ that lifts homeomorphically to $\tilde{X}$.
Deduce that $X$ has no simply-connected covering space.

::: {.solution}
Let
\[
L=\{0\}\times[0,1]
\]
be the left edge.

<1>1. We first prove a compact local-injectivity lemma.
Let $f:E\to M$ be continuous, where $M$ is metric.
Suppose $K\subseteq E$ is compact, $f|_K$ is injective, and every $k\in K$ has a neighborhood on which $f$ is injective.
Then there is an open neighborhood $N$ of $K$ on which $f$ is injective.
::: {.proof}
Let $d$ be a metric on $M$ and define
\[
g:E\times E\to\mathbb R,
\qquad
g(e,e')=d(f(e),f(e')).
\]
Put
\[
Z=g^{-1}(0)=\{(e,e'):f(e)=f(e')\}.
\]

For each $k\in K$, choose an open neighborhood $V_k$ on which $f$ is injective.
Then
\[
(V_k\times V_k)\cap Z
\subseteq
\Delta_E.
\]
Let
\[
V=\bigcup_{k\in K}(V_k\times V_k),
\qquad
O=(E\times E\setminus Z)\cup V.
\]
The set $O$ is open.

We claim
\[
K\times K\subseteq O.
\]
Indeed, if $k\ne k'$ lie in $K$, injectivity of $f|_K$ gives
\[
f(k)\ne f(k'),
\]
so $(k,k')\notin Z$.
If $k=k'$, then $(k,k)\in V_k\times V_k\subseteq V$.

Since $K\times K$ is compact and lies in the open set $O$, the product-neighborhood lemma for compact sets gives open neighborhoods $W,W'$ of $K$ such that
\[
W\times W'\subseteq O.
\]
For completeness, this product-neighborhood lemma follows by covering each slice $\{k\}\times K$ by finitely many product neighborhoods inside $O$, intersecting their first factors to obtain a product neighborhood of $\{k\}\times K$, then using compactness of the first copy of $K$ and intersecting finitely many corresponding second factors.

Set
\[
N=W\cap W'.
\]
If $e,e'\in N$ and $f(e)=f(e')$, then
\[
(e,e')\in (N\times N)\cap Z\subseteq O\cap Z\subseteq V.
\]
Hence $e,e'$ lie together in some $V_k$, where $f$ is injective, so $e=e'$.
Thus $f|_N$ is injective.
:::

<1>2. Let
\[
p:\widetilde X\to X
\]
be any covering space.
Choose a point $\widetilde \ell_0$ above the lower-left corner of $L$.
The inclusion path of $L$ has a unique lift beginning at $\widetilde \ell_0$; denote its image by $\widetilde L$.
Then
\[
p|_{\widetilde L}:\widetilde L\to L
\]
is a homeomorphism.
::: {.proof}
The lifted path is injective.
If two distinct parameters had the same lifted point, their images under $p$ would be the same point of the injectively parametrized left edge $L$.
Thus the lifted path is a continuous bijection from the compact interval $I$ onto $\widetilde L$.
Since $\widetilde X$ is Hausdorff locally over the metric space $X$ along each covering sheet, this map is a homeomorphism onto its image.
Equivalently, its inverse is simply the restriction of $p$ followed by the inverse parametrization of $L$.
:::

<1>3. There is an open neighborhood $N$ of $\widetilde L$ such that
\[
p|_N:N\longrightarrow p(N)
\]
is a homeomorphism, and $p(N)$ is an open neighborhood of $L$ in $X$.
::: {.proof}
The set $\widetilde L$ is compact by <1>2.
A covering map is locally a homeomorphism, hence locally injective near every point of $\widetilde L$.
Also $p$ is injective on $\widetilde L$ by <1>2.

Apply <1>1 with
\[
E=\widetilde X,
\qquad
M=X\subseteq\mathbb R^2,
\qquad
K=\widetilde L.
\]
We obtain an open neighborhood $N$ of $\widetilde L$ on which $p$ is injective.

Every covering map is open: on each covering sheet it is a homeomorphism onto an open subset of the base, and an arbitrary open set is the union of its intersections with such sheets.
Therefore $p(N)$ is open.
The continuous bijection
\[
p|_N:N\to p(N)
\]
is open, hence is a homeomorphism.
Since $p(\widetilde L)=L$, the set $p(N)$ contains $L$.
:::

<1>4. Every open neighborhood $U$ of $L$ in $X$ contains, for all sufficiently large $n$, the entire rectangular loop
\[
R_n
=
\partial\bigl([0,1/n]\times[0,1]\bigr).
\]
::: {.proof}
The complement
\[
F=X\setminus U
\]
is closed in the compact metric space $X$, hence compact.
It is disjoint from the compact set $L$.
Therefore their Euclidean distance is positive:
\[
\delta=d(L,F)>0.
\]
Choose $n$ with
\[
1/n<\delta.
\]
Every point of $R_n$ has Euclidean distance at most $1/n$ from $L$, so no point of $R_n$ lies in $F$.
Thus
\[
R_n\subseteq U.
\]
:::

<1>5. The loop $R_n$ is nontrivial in $\pi_1(X)$.
::: {.proof}
Define
\[
\varphi_n:X\to S^1
\]
to be constant equal to $1$ on all of $X$ except the vertical segment
\[
V_n=\{1/n\}\times[0,1],
\]
and on that segment set
\[
\varphi_n(1/n,t)=e^{2\pi i t}.
\]
This is continuous.
The segment $V_n$ is isolated from all the other interior vertical segments in the horizontal direction, and at its two endpoints the displayed formula equals $1$, agreeing with the constant definition on the top and bottom edges.

Orient $R_n$ so that it traverses $V_n$ from bottom to top.
All other portions of $R_n$ map constantly to $1$, while $V_n$ maps once around $S^1$.
Hence
\[
(\varphi_n)_*([R_n])=1\in\pi_1(S^1)\cong\mathbb Z.
\]
Therefore $[R_n]\ne1$ in $\pi_1(X)$.
:::

<1>6. The space $X$ has no simply connected covering space.
::: {.proof}
Suppose $p:\widetilde X\to X$ were a simply connected covering.
By <1>3, choose an open neighborhood $U=p(N)$ of $L$ that lifts homeomorphically to $N$.
By <1>4, choose $n$ with
\[
R_n\subseteq U.
\]

The loop $R_n$ therefore has the closed lift
\[
\widetilde R_n=(p|_N)^{-1}\circ R_n
\]
in $\widetilde X$.
Since $\widetilde X$ is simply connected, $\widetilde R_n$ is nullhomotopic.
Composing a nullhomotopy with $p$ shows that $R_n$ is nullhomotopic in $X$.
This contradicts <1>5.

Hence no simply connected covering of $X$ exists.
:::
:::
