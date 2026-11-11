---
schema: qual/card@1
id: E-M23QZ
kind: problem
title: Uniqueness of the completion
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Transcribed from the located published solution: Aleksey Zinger, "MAT 530: Topology & Geometry, I",
    Fall 2005, Problem Set 7, "Solution to Problem p271, #10", PDF pp. 1-2
    (tmp/sources/munkres-solutions-zinger-mat530-ps7.pdf, from
    https://www.math.stonybrook.edu/~azinger/mat530/ps7sol.pdf; the sheet prints no page numbers, so the
    PDF page is the locator). Checked against Munkres, Topology (2000), §43 Exercise 10, printed p. 271,
    with the definition of completion after Theorem 43.7 and Lemma 43.1. What was adapted: Zinger states
    the theorem for the special case in which Y and Y' are the completions of X, i.e. h and h' are the
    inclusions and X is dense in both, and he proves it by sending y to the limit in Y' of a sequence
    from X converging to y; the card states the printed general form with two isometric imbeddings h, h',
    so T_0 = h' h^{-1} plays the role of Zinger's identity on X and the isometry constructed is between
    the closures h(X)-bar and h'(X)-bar. The well-definedness argument is Zinger's: two sequences from X
    with the same limit y are at distance tending to 0, and D' of their images equals D of the originals.
    The card supplies Zinger's interleaving argument in the shorter form, and proves surjectivity by
    running the construction backwards, which Zinger does in his last paragraph.
---

::: {.exercise}

Theorem (Uniqueness of the completion).
Let $h: X \to Y$ and $h': X \to Y'$ be isometric imbeddings of the metric space $(X, d)$ in the complete metric spaces $(Y, D)$ and $(Y', D')$, respectively.
Then there is an isometry of $(\overline{h(X)}, D)$ with $(\overline{h'(X)}, D')$ that equals $h' h^{-1}$ on the subspace $h(X)$.
:::

::: {.solution}
Let
$$
T_0=h'\circ h^{-1}:h(X)\longrightarrow h'(X).
$$
Because both $h$ and $h'$ are isometric embeddings, $T_0$ is an isometry.

For $y\in\overline{h(X)}$, choose a sequence $h(x_n)\to y$. Then $(h(x_n))$ is Cauchy, so
$$
D'(h'(x_m),h'(x_n))=D(h(x_m),h(x_n))\to0.
$$
Completeness of $Y'$ gives a limit of $h'(x_n)$, and since all terms lie in $h'(X)$, that limit lies in $\overline{h'(X)}$. Define
$$
T(y)=\lim_n h'(x_n).
$$

This is well defined. If also $h(z_n)\to y$, then
$$
D'(h'(x_n),h'(z_n))=D(h(x_n),h(z_n))\to0,
$$
so the two image sequences have the same limit.

For $y,z\in\overline{h(X)}$, choose $h(x_n)\to y$ and $h(z_n)\to z$. Continuity of the metrics gives
$$
D'(T(y),T(z))
 =\lim_n D'(h'(x_n),h'(z_n))
 =\lim_n D(h(x_n),h(z_n))
 =D(y,z).
$$
Thus $T$ is an isometry, hence injective.

It is surjective as well. Given $y'\in\overline{h'(X)}$, choose $h'(x_n)\to y'$. Then $(h(x_n))$ is Cauchy and therefore converges in the complete subspace $\overline{h(X)}$ to some $y$; by definition $T(y)=y'$.

Finally, if $y=h(x)\in h(X)$, the constant sequence $x_n=x$ gives
$$
T(h(x))=h'(x)=h'h^{-1}(h(x)).
$$
Hence $T$ is the required isometry extending $h'h^{-1}$.
:::
