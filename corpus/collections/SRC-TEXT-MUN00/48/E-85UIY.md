---
schema: qual/card@1
id: E-85UIY
kind: problem
title: Function spaces are Baire in the fine topology
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
  - Function Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ be a topological space; let $Y$ be a complete metric space.
Show that $\mathcal{C}(X, Y)$ is a Baire space in the fine topology (see [[E-0GM3H]]). [Hint: Given basis elements $B(f_i, \delta_i)$ such that $\delta_1 \leq 1$ and $\delta_{i+1} \leq \delta_i/3$ and $f_{i+1} \in B(f_i, \delta_i/3)$, show that

$$
\bigcap B(f_i, \delta_i) \neq \varnothing.]
$$
:::

::: {.solution}
The fine topology has as a basis the sets $B(f, \delta) = \{g \in \mathcal{C}(X, Y) : d(f(x), g(x)) < \delta(x) \text{ for all } x \in X\}$, with $f \in \mathcal{C}(X, Y)$ and $\delta: X \to (0, \infty)$ continuous. A space is a Baire space if and only if, for every nonempty open set $U_0$ and every sequence of dense open sets $D_1, D_2, \ldots$, the set $U_0 \cap \bigcap_n D_n$ is nonempty. Fix such $U_0$ and $D_n$.

::: pf

::: {.pf-step #s1}

There are $f_n \in \mathcal{C}(X, Y)$ and continuous $\delta_n: X \to (0, \infty)$ with $\delta_1 \le 1$, $B(f_1, \delta_1) \subseteq U_0 \cap D_1$, and, for $n \ge 1$, $\delta_{n+1} \le \delta_n/3$ and $B(f_{n+1}, \delta_{n+1}) \subseteq B(f_n, \delta_n/3) \cap D_{n+1}$.

::: pf-proof

Since $D_1$ is dense and open, $U_0 \cap D_1$ is a nonempty open set; it contains a basis element $B(f_1, \delta)$, and $\delta_1 = \min(\delta, 1)$ is continuous and positive. Given $f_n$ and $\delta_n$, the set $B(f_n, \delta_n/3) \cap D_{n+1}$ is open and nonempty because $D_{n+1}$ is dense; it contains a basis element $B(f_{n+1}, \delta)$, and $\delta_{n+1} = \min(\delta, \delta_n/3)$ is continuous and positive.

:::

:::

::: {.pf-step #s2}

For each $x \in X$, $f_n(x)$ converges to a point $f(x) \in Y$, and $d(f(x), f_n(x)) \le \delta_n(x)/2$ for all $n$.

::: pf-proof

By step [](#s1){.pf-ref}, $f_{k+1} \in B(f_k, \delta_k/3)$ and $\delta_k \le \delta_n/3^{k-n}$ for $k \ge n$. So for $m > n$,
$$d(f_m(x), f_n(x)) \le \sum_{k=n}^{m-1} \frac{\delta_k(x)}{3} \le \delta_n(x) \sum_{j=1}^\infty 3^{-j} = \frac{\delta_n(x)}{2}.$$
Since $\delta_n(x) \le 3^{-(n-1)}$, the sequence $(f_n(x))$ is Cauchy, and it converges because $Y$ is complete. Letting $m \to \infty$ gives the bound.

:::

:::

::: {.pf-step #s3}

$f$ is continuous.

::: pf-proof

Let $x_0 \in X$ and $\varepsilon > 0$. Since $\delta_N \le 3^{-(N-1)}$, choose $N$ with $\delta_N < \varepsilon/3$ everywhere. By continuity of $f_N$, there is a neighborhood $W$ of $x_0$ with $d(f_N(x), f_N(x_0)) < \varepsilon/3$ for $x \in W$. For $x \in W$, step [](#s2){.pf-ref} gives
$$d(f(x), f(x_0)) \le d(f(x), f_N(x)) + d(f_N(x), f_N(x_0)) + d(f_N(x_0), f(x_0)) < \frac{\varepsilon}{6} + \frac{\varepsilon}{3} + \frac{\varepsilon}{6} < \varepsilon.$$

:::

:::

::: pf-qed

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, $f \in \mathcal{C}(X, Y)$ and $d(f(x), f_n(x)) \le \delta_n(x)/2 < \delta_n(x)$, so $f \in B(f_n, \delta_n)$ for every $n$. By step [](#s1){.pf-ref}, $f \in U_0 \cap \bigcap_n D_n$.

:::

:::

:::
