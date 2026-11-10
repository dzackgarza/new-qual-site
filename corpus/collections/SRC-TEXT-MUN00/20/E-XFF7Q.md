---
schema: qual/card@1
id: E-XFF7Q
kind: problem
title: Uniform balls are not products of intervals
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §20 Exercise 6, printed p. 127; the three parts
    are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 20.6, PDF p. 19. (a) The point with n-th
    coordinate x_n + epsilon_n, where epsilon_n increases to epsilon, lies in the product of
    intervals but at uniform distance epsilon. (b) Every ball around that point leaves the
    product of intervals. (c) The uniform ball is the union of the products of intervals of
    smaller radius. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $\bar{\rho}$ be the uniform metric on $\RR^\omega$.
Given $\mathbf{x} = (x_1, x_2, \ldots) \in \RR^\omega$ and given $0 < \epsilon < 1$, let

$$
U(\mathbf{x}, \epsilon) = (x_1 - \epsilon, x_1 + \epsilon) \times \dots \times (x_n - \epsilon, x_n + \epsilon) \times \dots.
$$

(a) Show that $U(\mathbf{x}, \epsilon)$ is not equal to the $\epsilon$-ball $B_{\bar{\rho}}(\mathbf{x}, \epsilon)$.

(b) Show that $U(\mathbf{x}, \epsilon)$ is not even open in the uniform topology.

(c) Show that

$$
B_{\bar{\rho}}(\mathbf{x}, \epsilon) = \bigcup_{\delta < \epsilon} U(\mathbf{x}, \delta).
$$
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.6, PDF p. 19** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the three parts are theirs.

Fix $\mathbf{x}\in\RR^{\omega}$ and $0<\varepsilon<1$, and let $U(\mathbf{x},\varepsilon)=\prod_{n}(x_{n}-\varepsilon,x_{n}+\varepsilon)$.

(a) Choose positive numbers $\varepsilon_{n}\to\varepsilon$ with $\varepsilon_{n}<\varepsilon$ for all $n$ and put $\mathbf{y}=(x_{n}+\varepsilon_{n})_{n}$. Then $y_{n}\in(x_{n}-\varepsilon,x_{n}+\varepsilon)$ for every $n$, so $\mathbf{y}\in U(\mathbf{x},\varepsilon)$; but $\bar\rho(\mathbf{x},\mathbf{y})=\sup_{n}\min\{\varepsilon_{n},1\}=\varepsilon$ since $\varepsilon<1$ and $\varepsilon_{n}\to\varepsilon$, so $\mathbf{y}\notin B_{\bar\rho}(\mathbf{x},\varepsilon)$. Hence the two sets differ.

(b) With the same $\mathbf{y}$, we show no ball around $\mathbf{y}$ lies in $U(\mathbf{x},\varepsilon)$. Let $\delta>0$ and choose $N$ with $\abs{\varepsilon-\varepsilon_{n}}<\delta$ for $n\ge N$; define $\mathbf{z}$ by $z_{n}=y_{n}$ for $n<N$ and $z_{n}=x_{n}+\varepsilon$ for $n\ge N$. Then $\bar\rho(\mathbf{y},\mathbf{z})=\sup_{n\ge N}\min\{\abs{\varepsilon-\varepsilon_{n}},1\}<\delta$, so $\mathbf{z}\in B_{\bar\rho}(\mathbf{y},\delta)$; but $z_{n}=x_{n}+\varepsilon\notin(x_{n}-\varepsilon,x_{n}+\varepsilon)$ for $n\ge N$, so $\mathbf{z}\notin U(\mathbf{x},\varepsilon)$. Hence $U(\mathbf{x},\varepsilon)$ is not open in the uniform topology.

(c) If $\mathbf{y}\in B_{\bar\rho}(\mathbf{x},\varepsilon)$ then $r=\bar\rho(\mathbf{x},\mathbf{y})<\varepsilon$, and every $\delta$ with $r<\delta<\varepsilon$ gives $\mathbf{y}\in U(\mathbf{x},\delta)$. Conversely, if $\mathbf{y}\in U(\mathbf{x},\delta)$ for some $\delta<\varepsilon$, then $\bar\rho(\mathbf{x},\mathbf{y})\le\delta<\varepsilon$ and $\mathbf{y}\in B_{\bar\rho}(\mathbf{x},\varepsilon)$. Hence
$$
B_{\bar\rho}(\mathbf{x},\varepsilon)=\bigcup_{\delta<\varepsilon}U(\mathbf{x},\delta).
$$
:::
