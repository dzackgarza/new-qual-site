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

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.6** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the three parts are theirs.

Fix $\mathbf{x}\in\RR^{\omega}$ and $0<\varepsilon<1$, and put $U(\mathbf{x},\varepsilon)=\prod_{n}(x_{n}-\varepsilon,x_{n}+\varepsilon)$.

::: pf

::: {.pf-step #metric}
$\bar\rho(\mathbf{x},\mathbf{y})=\sup_{n}\bar d(x_{n},y_{n})$ with $\bar d(a,b)=\min\{\abs{a-b},1\}$; and $\bar\rho(\mathbf{x},\mathbf{y})=\sup_{n}\abs{x_{n}-y_{n}}$ whenever $\abs{x_{n}-y_{n}}<1$ for every $n$.

::: pf-proof
The first display is the definition of the uniform metric on $\RR^{\omega}$ (§20), and the second follows because $\bar d(a,b)=\abs{a-b}$ when $\abs{a-b}<1$, the minimum then being attained by the first entry.
:::

:::

::: {.pf-step #a}
(a) $U(\mathbf{x},\varepsilon)\ne B_{\bar\rho}(\mathbf{x},\varepsilon)$.

::: pf-proof

::: {.pf-step #a-point}
With $\varepsilon_{n}=\varepsilon\big(1-\tfrac{1}{2n}\big)$ and $\mathbf{y}=(x_{n}+\varepsilon_{n})_{n}$, one has $\mathbf{y}\in U(\mathbf{x},\varepsilon)$ and $\bar\rho(\mathbf{x},\mathbf{y})=\varepsilon$.

::: pf-proof
For every $n$ one has $0<\varepsilon_{n}<\varepsilon$ and $\varepsilon_{n}\to\varepsilon$, so $y_{n}=x_{n}+\varepsilon_{n}\in(x_{n}-\varepsilon,x_{n}+\varepsilon)$, which is $\mathbf{y}\in U(\mathbf{x},\varepsilon)$. Also $\abs{x_{n}-y_{n}}=\varepsilon_{n}<\varepsilon<1$ for every $n$, so by step [](#metric){.pf-ref} $\bar\rho(\mathbf{x},\mathbf{y})=\sup_{n}\varepsilon_{n}=\varepsilon$.
:::

:::

::: {.pf-qed}
The point $\mathbf{y}$ of step [](#a-point){.pf-ref} lies in $U(\mathbf{x},\varepsilon)$, and it does not lie in $B_{\bar\rho}(\mathbf{x},\varepsilon)$, whose members are the points at $\bar\rho$-distance strictly less than $\varepsilon$ from $\mathbf{x}$ (§20). Hence the two sets differ.
:::

:::

:::

::: {.pf-step #b}
(b) $U(\mathbf{x},\varepsilon)$ is not open in the uniform topology.

::: pf-proof

::: {.pf-step #b-ball}
For every $\delta>0$ there is $\mathbf{z}\in B_{\bar\rho}(\mathbf{y},\delta)\setminus U(\mathbf{x},\varepsilon)$, where $\mathbf{y}$ is the point of step [](#a-point){.pf-ref}.

::: pf-proof
Let $\delta>0$. Since $\varepsilon_{n}\to\varepsilon$, choose $N$ with $\abs{\varepsilon-\varepsilon_{n}}<\delta$ for all $n\ge N$, and define $\mathbf{z}$ by $z_{n}=y_{n}$ for $n<N$ and $z_{n}=x_{n}+\varepsilon$ for $n\ge N$. For $n\ge N$ one has $\bar d(y_{n},z_{n})=\min\{\abs{\varepsilon-\varepsilon_{n}},1\}<\delta$, since either $\delta\le1$, when the minimum is $\abs{\varepsilon-\varepsilon_{n}}<\delta$, or $\delta>1$, when the minimum is at most $1<\delta$; and for $n<N$ that distance is $0$. Hence $\bar\rho(\mathbf{y},\mathbf{z})<\delta$. But $z_{n}=x_{n}+\varepsilon\notin(x_{n}-\varepsilon,x_{n}+\varepsilon)$ for every $n\ge N$, so $\mathbf{z}\notin U(\mathbf{x},\varepsilon)$.
:::

:::

::: {.pf-qed}
The point $\mathbf{y}$ lies in $U(\mathbf{x},\varepsilon)$ by step [](#a-point){.pf-ref}, and step [](#b-ball){.pf-ref} produces, for each $\delta>0$, a point of $B_{\bar\rho}(\mathbf{y},\delta)$ outside $U(\mathbf{x},\varepsilon)$. So no ball about $\mathbf{y}$ is contained in $U(\mathbf{x},\varepsilon)$, and the balls of the uniform metric form a basis of the uniform topology (§20), so $U(\mathbf{x},\varepsilon)$ is not open in it.
:::

:::

:::

::: {.pf-step #c}
(c) $B_{\bar\rho}(\mathbf{x},\varepsilon)=\bigcup_{\delta<\varepsilon}U(\mathbf{x},\delta)$.

::: pf-proof

::: {.pf-step #c-in}
$B_{\bar\rho}(\mathbf{x},\varepsilon)\subset\bigcup_{\delta<\varepsilon}U(\mathbf{x},\delta)$.

::: pf-proof
Let $\mathbf{y}\in B_{\bar\rho}(\mathbf{x},\varepsilon)$ and put $r=\bar\rho(\mathbf{x},\mathbf{y})<\varepsilon$; choose $\delta$ with $r<\delta<\varepsilon$. For every $n$ one has $\min\{\abs{x_{n}-y_{n}},1\}\le r<\delta<1$, so $\abs{x_{n}-y_{n}}<\delta$ and $\mathbf{y}\in U(\mathbf{x},\delta)$.
:::

:::

::: {.pf-step #c-out}
$\bigcup_{\delta<\varepsilon}U(\mathbf{x},\delta)\subset B_{\bar\rho}(\mathbf{x},\varepsilon)$.

::: pf-proof
Let $\mathbf{y}\in U(\mathbf{x},\delta)$ with $\delta<\varepsilon$. Then $\abs{x_{n}-y_{n}}<\delta<1$ for every $n$, so by step [](#metric){.pf-ref} $\bar\rho(\mathbf{x},\mathbf{y})=\sup_{n}\abs{x_{n}-y_{n}}\le\delta<\varepsilon$, that is, $\mathbf{y}\in B_{\bar\rho}(\mathbf{x},\varepsilon)$.
:::

:::

::: {.pf-qed}
Step [](#c-in){.pf-ref} gives one inclusion and step [](#c-out){.pf-ref} the other, so the two sets are equal.
:::

:::

:::

:::
:::
