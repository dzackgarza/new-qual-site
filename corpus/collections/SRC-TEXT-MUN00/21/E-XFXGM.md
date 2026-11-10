---
schema: qual/card@1
id: E-XFXGM
kind: problem
title: Product metrics, finite and countable
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 3, printed p. 133, with Theorem 20.5
    for the comparison; both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.3, PDF pp. 23-24. The maximum metric on a
    finite product and the supremum of the truncated metrics divided by the index on a
    countable one both induce the product topology, by the two ball inclusions in each case
    and the choice of a finite initial segment where 1/N is below the radius.
    (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $X_n$ be a metric space with metric $d_n$, for $n \in \ZZ_+$.

(a) Show that

$$
\rho(x, y) = \max\theset{d_1(x_1, y_1), \dots, d_n(x_n, y_n)}
$$

is a metric for the product space $X_1 \times \cdots \times X_n$.

(b) Let $\bar{d}_i = \min\theset{d_i, 1}$.
Show that

$$
D(x, y) = \sup\theset{\bar{d}_i(x_i, y_i)/i}
$$

is a metric for the product space $\prod X_i$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.3, PDF pp. 23--24** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both parts are theirs.

(a) Let $X_{i}$ have metric $d_{i}$ and put $\rho(\mathbf{x},\mathbf{y})=\max\{d_{1}(x_{1},y_{1}),\dots,d_{n}(x_{n},y_{n})\}$ on $X_{1}\times\cdots\times X_{n}$.

$\rho$ is a metric: nonnegativity, symmetry and $\rho=0\iff\mathbf{x}=\mathbf{y}$ are clear, and $\rho(\mathbf{x},\mathbf{y})+\rho(\mathbf{y},\mathbf{z})\ge d_{i}(x_{i},y_{i})+d_{i}(y_{i},z_{i})\ge d_{i}(x_{i},z_{i})$ for each $i$, so the left side is at least $\rho(\mathbf{x},\mathbf{z})$.

$\rho$ induces the product topology: if $B_{d_{1}}(x_{1},r_{1})\times\cdots\times B_{d_{n}}(x_{n},r_{n})$ is a product basis element and $r=\min r_{i}$, then $B_{\rho}(\mathbf{x},r)\subset\prod B_{d_{i}}(x_{i},r_{i})$; conversely $B_{d_{1}}(x_{1},\delta)\times\cdots\times B_{d_{n}}(x_{n},\delta)\subset B_{\rho}(\mathbf{x},\delta)$.

(b) Let $\bar d_{i}=\min\{d_{i},1\}$ and $D(\mathbf{x},\mathbf{y})=\sup_{i}\bar d_{i}(x_{i},y_{i})/i$ on $\prod_{i\in\ZZ_{+}}X_{i}$.

$D$ is a metric: the three axioms hold coordinatewise and pass to the supremum, and for each $i$
$$
\frac{\bar d_{i}(x_{i},z_{i})}{i}\le\frac{\bar d_{i}(x_{i},y_{i})}{i}+\frac{\bar d_{i}(y_{i},z_{i})}{i}\le D(\mathbf{x},\mathbf{y})+D(\mathbf{y},\mathbf{z}),
$$
so $D(\mathbf{x},\mathbf{z})\le D(\mathbf{x},\mathbf{y})+D(\mathbf{y},\mathbf{z})$.

$D$ induces the product topology, as in Theorem 20.5. If $B_{D}(\mathbf{x},\varepsilon)$ is a ball, choose $N$ with $1/N<\varepsilon$ and let $U=\prod_{i}U_{i}$ with $U_{i}=B_{d_{i}}(x_{i},\varepsilon)$ for $i<N$ and $U_{i}=X_{i}$ for $i\ge N$; then $U$ is a product neighbourhood of $\mathbf{x}$, and for $\mathbf{y}\in U$,
$$
D(\mathbf{x},\mathbf{y})\le\max\Big\{\frac{\bar d_{1}(x_{1},y_{1})}{1},\dots,\frac{\bar d_{N-1}(x_{N-1},y_{N-1})}{N-1},\frac1N\Big\}<\varepsilon .
$$
Conversely let $\prod U_{i}$ be a product basis element containing $\mathbf{x}$, with $U_{i}=X_{i}$ except for $i_{1}<\cdots<i_{N}$; choose $0<r<1$ with $x_{i_{k}}\in B_{d_{i_{k}}}(x_{i_{k}},r)\subset U_{i_{k}}$ for each $k$, and put $\varepsilon=r/i_{N}$. If $D(\mathbf{x},\mathbf{y})<\varepsilon$ then for $k=1,\dots,N$, $\bar d_{i_{k}}(x_{i_{k}},y_{i_{k}})<i_{k}\varepsilon\le r<1$, so $\bar d_{i_{k}}=d_{i_{k}}$ there and $y_{i_{k}}\in U_{i_{k}}$; for other $i$ it is automatic. So $B_{D}(\mathbf{x},\varepsilon)\subset\prod U_{i}$.
:::
