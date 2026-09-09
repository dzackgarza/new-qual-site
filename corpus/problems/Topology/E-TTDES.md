---
schema: qual/card@1
id: E-TTDES
kind: problem
title: Compact, limit-point compact, and sequentially compact coincide for second-countable
  Hausdorff or metric spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Countability
  - Convergence
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: exercise
Show that if $X$ is second-countable and Hausdorff (or a metric space), then the following are equivalent:
(1) $X$ is compact (every open cover has a finite subcover).
(2) $X$ is limit-point compact (every infinite subset $A \subseteq X$ has a limit point in $X$).
(3) $X$ is sequentially compact (every sequence in $X$ has a convergent subsequence in $X$).
:::

::: solution
<1>1. $(1)\Rightarrow(2)$. Suppose $X$ is compact and $A\subseteq X$ is infinite. If $A$ had no limit point, then for every $x\in X$ there would be an open neighborhood $U_x$ with
\[
U_x\cap A\subseteq\{x\}.
\]
A finite subcover $U_{x_1},\dots,U_{x_m}$ would then imply
\[
A\subseteq\{x_1,\dots,x_m\},
\]
a contradiction.

<1>2. $(2)\Rightarrow(3)$. Assume $X$ is second-countable Hausdorff; the metric case is identical because metric spaces are first-countable and Hausdorff.
<2>1. Let $(x_n)$ be a sequence. If its range is finite, some value occurs infinitely often and gives a constant convergent subsequence.
<2>2. Otherwise its range $S$ is infinite, so it has a limit point $x$.
<2>3. Second countability implies first countability, so choose a decreasing countable neighborhood basis
\[
B_1\supseteq B_2\supseteq\cdots
\]
at $x$.
<2>4. Since Hausdorff spaces are $T_1$, every neighborhood of a limit point of the infinite set $S$ contains infinitely many points of $S$: if one contained only finitely many points of $S\setminus\{x\}$, deleting those finitely many closed points would produce a neighborhood of $x$ meeting $S$ in at most $\{x\}$.
<2>5. Hence one can choose $n_1<n_2<\cdots$ with $x_{n_k}\in B_k$. Then $x_{n_k}\to x$.

<1>3. $(3)\Rightarrow(1)$. Assume first that $X$ is second-countable.
<2>1. Every open cover has a countable subcover: if $\mathcal B$ is a countable basis, for each basis element $B\in\mathcal B$ lying in some member of the cover choose one such member; these chosen sets cover $X$.
<2>2. Let $U_1,U_2,\dots$ be a countable open cover with no finite subcover. Choose
\[
x_N\in X\setminus\bigcup_{n=1}^N U_n.
\]
Sequential compactness gives a subsequence $x_{N_k}\to x$. Choose $m$ with $x\in U_m$. Eventually $x_{N_k}\in U_m$, while for large $k$ one has $N_k\ge m$ and hence $x_{N_k}\notin U_m$, a contradiction.

<1>4. For a metric space, $(3)\Rightarrow(1)$ follows by the standard metric argument: sequential compactness implies total boundedness and completeness, and every complete totally bounded metric space is compact. Equivalently, one may use the Lebesgue-number proof for an arbitrary open cover.

<1>5. Therefore compactness, limit-point compactness, and sequential compactness are equivalent in every second-countable Hausdorff space and in every metric space.
:::
