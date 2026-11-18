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

The contradiction is that of **"positron0802"**, *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.4, PDF p. 22 (`tmp/sources/munkres-solutions-positron-ch3.pdf`); two points of it are sharpened here. That solution writes $B=[0,\varepsilon]^{\omega}$ for the open ball, which is $[0,\varepsilon)^{\omega}$, and it uses the closed box without saying why the box lies in $C$ — the reason is that $C$ is closed. It also leaves the witness of Exercise 28.1 unnamed; the points $\varepsilon\mathbf{e}_{n}$ are used below. The statement was checked against Munkres, *Topology* (2000), §29 Exercise 4, printed p. 186, with §28 Exercise 1 on printed p. 181, Theorem 28.1 on printed p. 179, and Theorems 26.2 and 26.3 on printed p. 165.

Throughout, $X\coloneqq[0,1]^{\omega}$ carries the uniform metric $\bar\rho$, $\mathbf{0}$ is the zero sequence, and $\mathbf{e}_{n}$ is the sequence with $n$-th coordinate $1$ and all others $0$.

::: pf

::: {.pf-step #sup-metric}
On $X$ the uniform metric is the supremum metric, $\bar\rho(\mathbf{x},\mathbf{y})=\sup_{i}\abs{x_{i}-y_{i}}$.

::: pf-proof
For $\mathbf{x},\mathbf{y}\in X$ each difference $\abs{x_{i}-y_{i}}$ lies in $[0,1]$, so $\min\theset{\abs{x_{i}-y_{i}},1}=\abs{x_{i}-y_{i}}$ and the two formulas agree.
:::

:::

::: {.pf-step #ball-and-closure}
$B_{\bar\rho}(\mathbf{0},\varepsilon)\cap X=[0,\varepsilon)^{\omega}$, and its closure in $X$ is $[0,\varepsilon]^{\omega}$.

:::: pf-proof

::: {.pf-step #ball}
$B_{\bar\rho}(\mathbf{0},\varepsilon)\cap X=\theset{\mathbf{x}\in X\mid x_{i}<\varepsilon\text{ for every }i}=[0,\varepsilon)^{\omega}$.

::: pf-proof
By step [](#sup-metric){.pf-ref}, $\bar\rho(\mathbf{0},\mathbf{x})=\sup_{i}x_{i}$ for $\mathbf{x}\in X$ with $x_{i}\geq0$, and a supremum of nonnegative numbers is $<\varepsilon$ exactly when all of them are.
:::

:::

::: {.pf-step #closure}
The closure of $[0,\varepsilon)^{\omega}$ in $X$ is $[0,\varepsilon]^{\omega}$.

::: pf-proof
$[0,\varepsilon]^{\omega}$ is closed in $X$: if a sequence of points of it converges in $X$, each coordinate converges in $[0,\varepsilon]$, which is closed in $\RR$, so the limit has all coordinates in $[0,\varepsilon]$. It contains $[0,\varepsilon)^{\omega}$, so it contains the closure. Conversely a point $\mathbf{x}$ of $[0,\varepsilon]^{\omega}$ is a limit of points of $[0,\varepsilon)^{\omega}$: if $s\coloneqq\sup_{i}x_{i}<\varepsilon$ then $\mathbf{x}$ itself lies in $[0,\varepsilon)^{\omega}$, and otherwise the points $(1-1/k)\mathbf{x}$ lie in $[0,\varepsilon)^{\omega}$ and converge to $\mathbf{x}$ because $\bar\rho(\mathbf{x},(1-1/k)\mathbf{x})=\sup_{i}x_{i}/k\leq\varepsilon/k\to0$.
:::

:::

::::

:::

::: {.pf-step #compact-box}
If $X$ were locally compact at $\mathbf{0}$, then $[0,\varepsilon]^{\omega}$ is compact for some $\varepsilon>0$.

::: pf-proof
Local compactness at $\mathbf{0}$ gives a compact subspace $C$ of $X$ containing a neighbourhood $U$ of $\mathbf{0}$ (printed p. 182). Since the balls form a basis for the metric topology (§20, printed p. 119), there is $\varepsilon>0$ with $B_{\bar\rho}(\mathbf{0},\varepsilon)\subset U\subset C$. A compact subspace of the metric space $X$ is closed by Theorem 26.3 (printed p. 165), so $C$ contains the closure of anything it contains; by step [](#ball-and-closure){.pf-ref} it therefore contains $[0,\varepsilon]^{\omega}$. That box is closed in $X$ and lies in the compact space $C$, so it is compact by Theorem 26.2 (printed p. 165).
:::

:::

::: {.pf-step #no-limit-point}
No $\varepsilon>0$ makes $[0,\varepsilon]^{\omega}$ limit point compact.

:::: pf-proof

::: {.pf-step #separated}
The points $\varepsilon\mathbf{e}_{n}$, for $n\geq1$, lie in $[0,\varepsilon]^{\omega}$ and satisfy $\bar\rho(\varepsilon\mathbf{e}_{n},\varepsilon\mathbf{e}_{m})=\varepsilon$ whenever $n\neq m$.

::: pf-proof
Each $\varepsilon\mathbf{e}_{n}$ has coordinates in $\theset{0,\varepsilon}\subset[0,\varepsilon]$. The difference at the $n$-th coordinate is $\varepsilon$ and at the $m$-th coordinate is $-\varepsilon$, and the two sequences agree elsewhere, so the supremum of the coordinatewise differences is $\varepsilon$ by step [](#sup-metric){.pf-ref}.
:::

:::

::: {.pf-step #no-accumulation}
The infinite set $E\coloneqq\theset{\varepsilon\mathbf{e}_{n}\mid n\geq1}$ has no limit point in $[0,\varepsilon]^{\omega}$.

::: pf-proof
Let $\mathbf{y}\in[0,\varepsilon]^{\omega}$ and suppose $\varepsilon\mathbf{e}_{n}$ and $\varepsilon\mathbf{e}_{m}$ with $n\neq m$ both lay in the ball $B_{\bar\rho}(\mathbf{y},\varepsilon/2)$. Then $\bar\rho(\varepsilon\mathbf{e}_{n},\varepsilon\mathbf{e}_{m})\leq\bar\rho(\varepsilon\mathbf{e}_{n},\mathbf{y})+\bar\rho(\mathbf{y},\varepsilon\mathbf{e}_{m})<\varepsilon$, contradicting step [](#separated){.pf-ref}. So that ball contains at most one point of $E$, and since it is a neighbourhood of $\mathbf{y}$, the point $\mathbf{y}$ is not a limit point of $E$.
:::

:::

::::

:::

::: pf-step
Therefore $[0,1]^{\omega}$ is not locally compact in the uniform topology.

::: pf-proof
If it were locally compact at $\mathbf{0}$, step [](#compact-box){.pf-ref} would make $[0,\varepsilon]^{\omega}$ compact for some $\varepsilon>0$; but a compact space is limit point compact by Theorem 28.1 (printed p. 179), that is, every infinite subset of it has a limit point, whereas step [](#no-limit-point){.pf-ref} exhibits the infinite subset $E$ with none. This contradiction shows that $X$ is not locally compact at $\mathbf{0}$, hence not locally compact.
:::

:::

:::

:::
