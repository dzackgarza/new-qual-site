---
schema: qual/card@1
id: E-L2EHD
kind: problem
title: The Stone-Cech compactification of a discrete space
classification:
  areas:
  - topology
  topics:
  - Compactness
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

Let $X$ be a discrete space; consider the space $\beta(X)$.

(a) Show that if $A \subset X$, then $\overline{A}$ and $\overline{X - A}$ are disjoint, where the closures are taken in $\beta(X)$.

(b) Show that if $U$ is open in $\beta(X)$, then $\overline{U}$ is open in $\beta(X)$.

(c) Show that $\beta(X)$ is totally disconnected.
:::

::: {.solution}
Let \(i:X\hookrightarrow\beta X\) denote the canonical dense embedding.

(a) Since \(X\) is discrete, the characteristic function
\[
\chi_A:X\longrightarrow\{0,1\}\subset[0,1]
\]
is continuous. By the defining extension property of the Stone--Čech compactification it extends to a continuous map
\[
\widetilde\chi_A:\beta X\longrightarrow[0,1].
\]
Because \(X\) is dense and \(\widetilde\chi_A(X)\subset\{0,1\}\), the whole image of \(\widetilde\chi_A\) lies in the closed set \(\{0,1\}\). Therefore
\[
\overline A\subset \widetilde\chi_A^{-1}(0),\qquad
\overline{X-A}\subset \widetilde\chi_A^{-1}(1),
\]
so these two closures are disjoint.

(b) Let \(U\subset\beta X\) be open and put \(A=U\cap X\). Since \(X\) is dense, \(A\) is dense in \(U\): every nonempty open subset of \(U\) meets \(X\). Hence
\[
\overline U=\overline A.
\]
By part (a), \(\overline A\) and \(\overline{X-A}\) are disjoint. Also
\[
X=A\cup(X-A)
\]
is dense in \(\beta X\), so
\[
\beta X=\overline A\cup\overline{X-A}.
\]
Thus
\[
\overline U=\overline A=\beta X-\overline{X-A},
\]
which is open. Hence \(\beta X\) is extremally disconnected.

(c) Let \(p\ne q\) in \(\beta X\). Since \(\beta X\) is compact Hausdorff, choose an open neighborhood \(U\) of \(p\) with \(q\notin\overline U\). By (b), \(\overline U\) is both open and closed. Thus \(p\) and \(q\) are separated by the clopen set \(\overline U\). Consequently every connected subset containing two distinct points is separated, so every connected component is a singleton. Hence \(\beta X\) is totally disconnected.
:::
