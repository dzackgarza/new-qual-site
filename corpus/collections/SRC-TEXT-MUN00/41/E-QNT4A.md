---
schema: qual/card@1
id: E-QNT4A
kind: problem
title: Perfect maps and paracompactness
classification:
  areas:
  - topology
  topics:
  - Paracompactness
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
---

::: {.exercise}

Let $p: X \to Y$ be a perfect map.
(See Exercise 7 of §31.)

(a) Show that if $Y$ is paracompact, so is $X$.
[Hint: If $\mathcal{A}$ is an open covering of $X$, find a locally finite open covering of $Y$ by sets $B$ such that $p^{-1}(B)$ can be covered by finitely many elements of $\mathcal{A}$; then intersect $p^{-1}(B)$ with these elements of $\mathcal{A}$.]

(b) Show that if $X$ is a paracompact Hausdorff space, then so is $Y$.
[Hint: If $\mathcal{B}$ is a locally finite closed covering of $X$, then $\ts{p(B) \mid B \in \mathcal{B}}$ is a locally finite closed covering of $Y$.]
:::

::: {.solution}
Let \(p:X\to Y\) be perfect.

(a) Assume \(Y\) is paracompact, and let \(\mathcal U\) be an open cover of \(X\). For each \(y\in Y\), compactness of the fiber \(p^{-1}(y)\) gives finitely many members
\[
U_{y,1},\ldots,U_{y,r(y)}\in\mathcal U
\]
covering that fiber. Put \(O_y=\bigcup_jU_{y,j}\). Since \(p\) is closed,
\[
V_y=Y-p(X-O_y)
\]
is open, contains \(y\), and satisfies \(p^{-1}(V_y)\subset O_y\). Choose a locally finite open refinement \(\mathcal W\) of \(\{V_y\}\) covering \(Y\). For each \(W\in\mathcal W\), choose \(y(W)\) with \(W\subset V_{y(W)}\), and form
\[
\mathcal R=
\{p^{-1}(W)\cap U_{y(W),j}:W\in\mathcal W,\ 1\le j\le r(y(W))\}.
\]
This is an open refinement of \(\mathcal U\) and covers \(X\). It is locally finite: if a neighborhood \(N\) of \(p(x)\) meets only finitely many \(W\)'s, then \(p^{-1}(N)\) meets only the finitely many corresponding finite families in \(\mathcal R\). Hence \(X\) is paracompact.

(b) Assume \(X\) is paracompact Hausdorff. By the perfect-map separation results of §31, \(Y\) is regular. Let \(\mathcal U\) be an open cover of \(Y\). The pullback cover \(\{p^{-1}(U):U\in\mathcal U\}\) of \(X\) has a locally finite closed refinement \(\mathcal F\) covering \(X\) (the closed-refinement form of paracompactness).

For each \(F\in\mathcal F\), choose \(U(F)\in\mathcal U\) with
\[
F\subset p^{-1}(U(F)).
\]
Since \(p\) is closed, every \(p(F)\) is closed and \(p(F)\subset U(F)\); the family \(\{p(F):F\in\mathcal F\}\) covers \(Y\).

It is locally finite. Fix \(y\in Y\). The compact fiber \(p^{-1}(y)\) has a neighborhood \(O\subset X\) meeting only finitely many members of \(\mathcal F\): cover the fiber by finitely many neighborhoods witnessing local finiteness and take their union. Then
\[
N=Y-p(X-O)
\]
is an open neighborhood of \(y\) with \(p^{-1}(N)\subset O\). If \(N\cap p(F)\ne\varnothing\), then \(p^{-1}(N)\cap F\ne\varnothing\), so \(F\) is one of the finitely many members meeting \(O\). Thus \(\{p(F)\}\) is locally finite.

Therefore every open cover of the regular space \(Y\) has a locally finite closed refinement. By the closed-refinement characterization of paracompactness, \(Y\) is paracompact.
:::
