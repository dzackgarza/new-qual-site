---
schema: qual/card@1
id: E-SS2.PR-5
kind: problem
title: A universal entire function under translation
classification:
  areas:
  - complex-analysis
  topics:
  - Runge
  - Entire Functions
relations: []
review: draft
---

::: {.exercise}
There exists an entire function $F$ with the following "universal" property: given any entire function $h$, there is an increasing sequence $\{N_k\}_{k=1}^\infty$ of positive integers, so that
$$
\lim_{k \to \infty} F(z + N_k) = h(z)
$$
uniformly on every compact subset of $\CC$.

(a) Let $p_1, p_2, \ldots$ denote an enumeration of the collection of polynomials whose coefficients have rational real and imaginary parts. Show that it suffices to find an entire function $F$ and an increasing sequence $\{M_n\}$ of positive integers, such that
$$
\abs{F(z) - p_n(z - M_n)} < \frac{1}{n} \quad \text{whenever } z \in D_n, \tag{17}
$$
where $D_n$ denotes the disc centered at $M_n$ and of radius $n$.
[Hint: Given $h$ entire, there exists a sequence $\{n_k\}$ such that $\lim_{k \to \infty} p_{n_k}(z) = h(z)$ uniformly on every compact subset of $\CC$.]

(b) Construct $F$ satisfying (17) as an infinite series
$$
F(z) = \sum_{n=1}^\infty u_n(z)
$$
where $u_n(z) = p_n(z - M_n) e^{-c_n (z - M_n)^2}$, and the quantities $c_n > 0$ and $M_n > 0$ are chosen appropriately with $c_n \to 0$ and $M_n \to \infty$.
[Hint: The function $e^{-z^2}$ vanishes rapidly as $\abs{z} \to \infty$ in the sectors $\{\abs{\arg z} < \pi/4 - \delta\}$ and $\{\abs{\pi - \arg z} < \pi/4 - \delta\}$.]

In the same spirit, there exists an alternate "universal" entire function $G$ with the following property: given any entire function $h$, there is an increasing sequence $\{N_k\}_{k=1}^\infty$ of positive integers, so that
$$
\lim_{k \to \infty} D^{N_k} G(z) = h(z)
$$
uniformly on every compact subset of $\CC$. Here $D^j G$ denotes the $j$th (complex) derivative of $G$.
:::

::: {.remark}
The book marks this problem with an asterisk. It writes the first limit as $n \to \infty$; the index of the sequence is $k$.
:::
