---
schema: qual/card@1
id: E-ESQ3V
kind: problem
title: The Hilbert cube is not locally compact in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 4, printed p. 186, with Exercise
    28.1 and Theorem 26.2; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.4, PDF p. 22. A uniform ball at the origin is a
    closed box of sequences, compact if the Hilbert cube were locally compact there, but
    homeomorphic to the cube, which has an infinite set without limit points.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that $[0, 1]^\omega$ is not locally compact in the uniform topology.
:::

::: {.solution}

The contradiction is that of **"positron0802"**, *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.4 (`tmp/sources/munkres-solutions-positron-ch3.pdf`), and this card's earlier version followed it. One step of that argument is false and is replaced here: the open ball $B_{\bar\rho}(\mathbf{0},\varepsilon)\cap X$ is not the half-open box $[0,\varepsilon)^{\omega}$. A point of that box may have $\sup_{i}x_{i}=\varepsilon$ — for instance $x_{i}=\varepsilon\big(1-\frac{1}{i+1}\big)$ — and such a point is at distance exactly $\varepsilon$ from $\mathbf{0}$, hence outside the open ball. What is needed, and what is used below, is a strictly smaller closed box: for $0<\eta<\varepsilon$ the box $[0,\eta]^{\omega}$ does lie in the ball, so it lies in any compact set containing that ball. The statement was checked against Munkres, *Topology* (2000), §29 Exercise 4, with §28 Exercise 1, Theorem 28.1, and Theorems 26.2 and 26.3 on printed p. 165.

Throughout, $X\coloneqq[0,1]^{\omega}$ carries the uniform metric $\bar\rho$, $\mathbf{0}$ is the zero sequence, and $\mathbf{e}_{n}$ is the sequence with $n$-th coordinate $1$ and all others $0$.

::: pf

::: {.pf-step #sup-metric}
On $X$ the uniform metric is the supremum metric, $\bar\rho(\mathbf{x},\mathbf{y})=\sup_{i}\abs{x_{i}-y_{i}}$.

::: pf-proof
For $\mathbf{x},\mathbf{y}\in X$ each difference $\abs{x_{i}-y_{i}}$ lies in $[0,1]$, so $\min\theset{\abs{x_{i}-y_{i}},1}=\abs{x_{i}-y_{i}}$ and the two formulas agree.
:::

:::

::: {.pf-step #box-in-ball}
For $0<\eta<\varepsilon$ the closed box $[0,\eta]^{\omega}$ lies in $B_{\bar\rho}(\mathbf{0},\varepsilon)\cap X$ and is closed in $X$.

:::: pf-proof

::: {.pf-step #in-ball}
$[0,\eta]^{\omega}\subset B_{\bar\rho}(\mathbf{0},\varepsilon)\cap X$.

::: pf-proof
For $\mathbf{x}\in[0,\eta]^{\omega}$ every coordinate lies in $[0,\eta]$, so by step [](#sup-metric){.pf-ref} $\bar\rho(\mathbf{0},\mathbf{x})=\sup_{i}x_{i}\leq\eta<\varepsilon$, which is what membership in the open ball requires.
:::

:::

::: {.pf-step #box-closed}
$[0,\eta]^{\omega}$ is closed in $X$.

::: pf-proof
If a sequence of points of the box converges in $X$ with the uniform metric, then each coordinate sequence converges, because $\abs{x_{i}^{(k)}-x_{i}}\leq\bar\rho(\mathbf{x}^{(k)},\mathbf{x})$; each coordinate limit lies in the closed interval $[0,\eta]$, so the limit point lies in the box. A set containing the limit of every convergent sequence from it is closed in a metric space (Lemma 21.2).
:::

:::

::::

:::

::: {.pf-step #compact-box}
If $X$ were locally compact at $\mathbf{0}$, then $[0,\eta]^{\omega}$ is compact for some $\eta>0$.

::: pf-proof
Local compactness at $\mathbf{0}$ gives a compact subspace $C$ of $X$ containing a neighbourhood $U$ of $\mathbf{0}$ (printed p. 182). Since the balls form a basis for the metric topology (§20), there is $\varepsilon>0$ with $B_{\bar\rho}(\mathbf{0},\varepsilon)\subset U\subset C$; choose $\eta$ with $0<\eta<\varepsilon$, and note $\eta<1$. Step [](#box-in-ball){.pf-ref} then gives $[0,\eta]^{\omega}\subset C$. A compact subspace of the metric space $X$ is closed by Theorem 26.3, so $C$ is closed; $[0,\eta]^{\omega}$ is closed by step [](#box-in-ball){.pf-ref} and lies in the compact space $C$, so it is compact by Theorem 26.2.
:::

:::

::: {.pf-step #no-limit-point}
No $\eta>0$ makes $[0,\eta]^{\omega}$ limit point compact.

:::: pf-proof

::: {.pf-step #separated}
The points $\eta\mathbf{e}_{n}$, for $n\geq1$, lie in $[0,\eta]^{\omega}$ and satisfy $\bar\rho(\eta\mathbf{e}_{n},\eta\mathbf{e}_{m})=\eta$ whenever $n\neq m$.

::: pf-proof
Each $\eta\mathbf{e}_{n}$ has coordinates in $\theset{0,\eta}\subset[0,\eta]$. The difference at the $n$-th coordinate is $\eta$ and at the $m$-th coordinate is $-\eta$, the two sequences agree elsewhere, and $\eta<1$, so the supremum of the coordinatewise differences is $\eta$ by step [](#sup-metric){.pf-ref}.
:::

:::

::: {.pf-step #no-accumulation}
The infinite set $E\coloneqq\theset{\eta\mathbf{e}_{n}\mid n\geq1}$ has no limit point in $[0,\eta]^{\omega}$.

::: pf-proof
Let $\mathbf{y}\in[0,\eta]^{\omega}$ and suppose $\eta\mathbf{e}_{n}$ and $\eta\mathbf{e}_{m}$ with $n\neq m$ both lay in the ball $B_{\bar\rho}(\mathbf{y},\eta/2)$. Then $\bar\rho(\eta\mathbf{e}_{n},\eta\mathbf{e}_{m})\leq\bar\rho(\eta\mathbf{e}_{n},\mathbf{y})+\bar\rho(\mathbf{y},\eta\mathbf{e}_{m})<\eta$, contradicting step [](#separated){.pf-ref}. So that ball, a neighbourhood of $\mathbf{y}$, contains at most one point of $E$, and $\mathbf{y}$ is not a limit point of $E$.
:::

:::

::::

:::

::: pf-step
Therefore $[0,1]^{\omega}$ is not locally compact in the uniform topology.

::: pf-proof
If it were locally compact at $\mathbf{0}$, step [](#compact-box){.pf-ref} would make $[0,\eta]^{\omega}$ compact for some $\eta>0$; but a compact space is limit point compact by Theorem 28.1, that is, every infinite subset of it has a limit point, whereas step [](#no-limit-point){.pf-ref} exhibits the infinite subset $E$ with none. This contradiction shows that $X$ is not locally compact at $\mathbf{0}$, hence not locally compact.
:::

:::

:::

:::
