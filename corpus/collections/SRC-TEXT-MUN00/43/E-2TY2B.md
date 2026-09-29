---
schema: qual/card@1
id: E-2TY2B
kind: problem
title: Completion via Cauchy sequences
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $(X, d)$ be a metric space.
Show that there is an isometric imbedding $h$ of $X$ into a complete metric space $(Y, D)$, as follows.
Let $\tilde{X}$ denote the set of all Cauchy sequences

$$
\mathbf{x} = (x_1, x_2, \dots)
$$

of points of $X$.
Define $\mathbf{x} \sim \mathbf{y}$ if

$$
d(x_n, y_n) \to 0.
$$

Let $[\mathbf{x}]$ denote the equivalence class of $\mathbf{x}$; and let $Y$ denote the set of these equivalence classes.
Define a metric $D$ on $Y$ by the equation

$$
D([\mathbf{x}], [\mathbf{y}]) = \lim_{n \to \infty} d(x_n, y_n).
$$

(a) Show that $\sim$ is an equivalence relation, and show that $D$ is a well-defined metric.

(b) Define $h: X \to Y$ by letting $h(x)$ be the equivalence class of the constant sequence $(x, x, \ldots)$:

$$
h(x) = [(x, x, \dots)].
$$

Show that $h$ is an isometric imbedding.

(c) Show that $h(X)$ is dense in $Y$; indeed, given $\mathbf{x} = (x_1, x_2, \ldots) \in \tilde{X}$, show the sequence $h(x_n)$ of points of $Y$ converges to the point $[\mathbf{x}]$ of $Y$.

(d) Show that if $A$ is a dense subset of a metric space $(Z, \rho)$, and if every Cauchy sequence in $A$ converges in $Z$, then $Z$ is complete.

(e) Show that $(Y, D)$ is complete.
:::

::: {.solution}

::: pf

::: pf-step
Part (a): Equivalence relation and well-defined metric $D$.

::: pf-proof

::: pf-step
**Equivalence relation:**
- Reflexivity: $d(x_n, x_n) = 0 \to 0$.
- Symmetry: $d(x_n, y_n) = d(y_n, x_n) \to 0$.
- Transitivity: $d(x_n, z_n) \le d(x_n, y_n) + d(y_n, z_n) \to 0 + 0 = 0$.
:::

::: pf-step
**Limit existence in $\mathbb{R}$:** For Cauchy sequences $\mathbf{x}, \mathbf{y}$, the triangle inequality gives $|d(x_n, y_n) - d(x_m, y_m)| \le d(x_n, x_m) + d(y_n, y_m) \to 0$. Thus $(d(x_n, y_n))_{n=1}^\infty$ is a Cauchy sequence in $\mathbb{R}$, hence converges to a unique real limit.
:::

::: pf-step
**Independence of representatives:** If $\mathbf{x} \sim \mathbf{x}'$ and $\mathbf{y} \sim \mathbf{y}'$, then $|d(x_n, y_n) - d(x'_n, y'_n)| \le d(x_n, x'_n) + d(y_n, y'_n) \to 0$, so $\lim d(x_n, y_n) = \lim d(x'_n, y'_n)$.
:::

::: pf-step
**Metric axioms:**
- $D([\mathbf{x}], [\mathbf{y}]) \ge 0$ and $D([\mathbf{x}], [\mathbf{y}]) = 0 \iff \lim d(x_n, y_n) = 0 \iff \mathbf{x} \sim \mathbf{y} \iff [\mathbf{x}] = [\mathbf{y}]$.
- Symmetry: $D([\mathbf{x}], [\mathbf{y}]) = D([\mathbf{y}], [\mathbf{x}])$.
- Triangle inequality: $D([\mathbf{x}], [\mathbf{z}]) = \lim d(x_n, z_n) \le \lim (d(x_n, y_n) + d(y_n, z_n)) = D([\mathbf{x}], [\mathbf{y}]) + D([\mathbf{y}], [\mathbf{z}])$.
:::

:::

:::

::: pf-step
Part (b): Isometric embedding $h: X \to Y$.

::: pf-proof

::: pf-step
For $x, y \in X$, $D(h(x), h(y)) = \lim_{n \to \infty} d(x, y) = d(x, y)$.
:::

::: pf-step
Thus $h$ preserves all pairwise distances, which proves $h$ is an isometric embedding (injective and topological embedding).
:::

:::

:::

::: {.pf-step #part-c}
Part (c): Density of $h(X)$ in $Y$.

::: pf-proof

::: pf-step
Let $[\mathbf{x}] \in Y$ where $\mathbf{x} = (x_1, x_2, \dots) \in \tilde{X}$.
:::

::: pf-step
For each fixed $k \in \mathbb{Z}_+$, $D(h(x_k), [\mathbf{x}]) = \lim_{n \to \infty} d(x_k, x_n)$.
:::

::: pf-step
Given $\varepsilon > 0$, choose $N$ such that $d(x_k, x_n) < \varepsilon$ for all $k, n \ge N$.
:::

::: pf-step
Taking $n \to \infty$ yields $D(h(x_k), [\mathbf{x}]) \le \varepsilon$ for all $k \ge N$.
:::

::: pf-step
Hence $\lim_{k \to \infty} h(x_k) = [\mathbf{x}]$ in $(Y, D)$, proving $h(X)$ is dense in $Y$.
:::

:::

:::

::: pf-step
Part (d): Density criterion for completeness.

::: pf-proof

::: pf-step
Let $(z_k)$ be a Cauchy sequence in $(Z, \rho)$.
:::

::: pf-step
Since $A$ is dense, for each $k$ choose $a_k \in A$ with $\rho(a_k, z_k) < \frac{1}{k}$.
:::

::: pf-step
Then $\rho(a_j, a_k) \le \rho(a_j, z_j) + \rho(z_j, z_k) + \rho(z_k, a_k) < \frac{1}{j} + \rho(z_j, z_k) + \frac{1}{k} \to 0$, so $(a_k)$ is Cauchy in $A$.
:::

::: pf-step
By hypothesis, $(a_k)$ converges to some $z \in Z$.
:::

::: pf-step
Then $\rho(z_k, z) \le \rho(z_k, a_k) + \rho(a_k, z) < \frac{1}{k} + \rho(a_k, z) \to 0$, so $z_k \to z$, proving $Z$ is complete.
:::

:::

:::

::: pf-step
Part (e): Completeness of $(Y, D)$.

::: pf-proof

::: pf-step
Let $(h(x_k))_{k=1}^\infty$ be a Cauchy sequence in $h(X)$.
:::

::: pf-step
Since $h$ is an isometry, $d(x_j, x_k) = D(h(x_j), h(x_k)) \to 0$, so $\mathbf{x} = (x_1, x_2, \dots) \in \tilde{X}$.
:::

::: pf-step
By step [](#part-c){.pf-ref}, $h(x_k) \to [\mathbf{x}] \in Y$.
:::

::: pf-step
Since $h(X)$ is dense in $Y$ and every Cauchy sequence in $h(X)$ converges in $Y$, part (d) implies $(Y, D)$ is complete. Q.E.D.
:::

:::

:::

:::

:::
