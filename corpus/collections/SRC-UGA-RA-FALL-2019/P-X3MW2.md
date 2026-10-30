---
schema: qual/card@1
id: P-X3MW2
kind: problem
title: Bessel's inequality and Riesz–Fischer for orthonormal sequences
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - L²
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 4 of the official UGA August 2019 Real Analysis qualifying examination DOCX.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Reviewed Bessel's inequality and the orthogonal-series construction for arbitrary ell2 coefficients; completeness and the norm identity are used correctly.
---

::: {.problem}
Let $\{u_n\}_{n=1}^\infty$ be an orthonormal sequence in a Hilbert space $\mathcal{H}$.

(a) Prove that for every $x \in \mathcal{H}$, Bessel's inequality holds:
$$
\sum_{n=1}^{\infty} \abs{\langle x, u_n \rangle}^2 \le \norm{x}^2.
$$

(b) Prove that for any sequence $(a_n)_{n=1}^\infty \in \ell^2(\NN)$, there exists an element $x \in \mathcal{H}$ such that
$$
a_n = \langle x, u_n \rangle \quad \text{for all } n \in \NN,
$$
and
$$
\norm{x}^2 = \sum_{n=1}^{\infty} \abs{\langle x, u_n \rangle}^2.
$$
:::

::: {.solution}
**Goal:** Prove Bessel's inequality in (a) by expanding the norm of orthogonal projections, and prove the Riesz–Fischer theorem in (b) by establishing convergence of orthogonal series in complete inner product spaces.

::: pf

::: pf-step
Part (a): Bessel's inequality $\sum_{n=1}^\infty \abs{\langle x, u_n \rangle}^2 \le \norm{x}^2$.

::: pf-proof

::: pf-step
Let $N \in \NN$ and consider the $N$-th partial sum $S_N = \sum_{n=1}^N \langle x, u_n \rangle u_n \in \mathcal{H}$.

:::

::: pf-step
Expand the squared norm of $x - S_N$:
$$\norm{x - S_N}^2 = \langle x - S_N, x - S_N \rangle = \norm{x}^2 - \langle x, S_N \rangle - \langle S_N, x \rangle + \norm{S_N}^2.$$

:::

::: pf-step
Compute $\langle x, S_N \rangle$:
$$\langle x, S_N \rangle = \left\langle x, \sum_{n=1}^N \langle x, u_n \rangle u_n \right\rangle = \sum_{n=1}^N \overline{\langle x, u_n \rangle} \langle x, u_n \rangle = \sum_{n=1}^N \abs{\langle x, u_n \rangle}^2.$$
Similarly, $\langle S_N, x \rangle = \overline{\langle x, S_N \rangle} = \sum_{n=1}^N \abs{\langle x, u_n \rangle}^2$.

:::

::: pf-step
Compute $\norm{S_N}^2$ using orthonormality $\langle u_n, u_m \rangle = \delta_{n, m}$:
$$\norm{S_N}^2 = \left\langle \sum_{n=1}^N \langle x, u_n \rangle u_n, \sum_{m=1}^N \langle x, u_m \rangle u_m \right\rangle = \sum_{n=1}^N \sum_{m=1}^N \langle x, u_n \rangle \overline{\langle x, u_m \rangle} \langle u_n, u_m \rangle = \sum_{n=1}^N \abs{\langle x, u_n \rangle}^2.$$

:::

::: pf-step
Substitute into the expansion:
$$\norm{x - S_N}^2 = \norm{x}^2 - 2 \sum_{n=1}^N \abs{\langle x, u_n \rangle}^2 + \sum_{n=1}^N \abs{\langle x, u_n \rangle}^2 = \norm{x}^2 - \sum_{n=1}^N \abs{\langle x, u_n \rangle}^2.$$

:::

::: pf-step
Since the norm on $\mathcal{H}$ is non-negative, $\norm{x - S_N}^2 \ge 0$, which yields
$$\sum_{n=1}^N \abs{\langle x, u_n \rangle}^2 \le \norm{x}^2.$$

:::

::: pf-step
Since this holds for every $N \in \NN$ and the sequence of partial sums of non-negative terms is non-decreasing, taking the limit as $N \to \infty$ gives
$$\sum_{n=1}^\infty \abs{\langle x, u_n \rangle}^2 \le \norm{x}^2.$$

:::

:::

:::

::: pf-step
Part (b): Existence of $x \in \mathcal{H}$ with $\langle x, u_n \rangle = a_n$ and $\norm{x}^2 = \sum \abs{a_n}^2$.

::: pf-proof

::: pf-step
Let $(a_n)_{n=1}^\infty \in \ell^2(\NN)$, so $\sum_{n=1}^\infty \abs{a_n}^2 < \infty$.

:::

::: pf-step
Define the sequence of partial sums $s_N = \sum_{n=1}^N a_n u_n \in \mathcal{H}$.

:::

::: pf-step
For any $M > N \ge 1$, by the Pythagorean theorem for orthonormal systems:
$$\norm{s_M - s_N}^2 = \norm{ \sum_{n=N+1}^M a_n u_n }^2 = \sum_{n=N+1}^M \abs{a_n}^2.$$

:::

::: pf-step
Since the series $\sum_{n=1}^\infty \abs{a_n}^2$ converges in $\RR$, its tail sum $\sum_{n=N+1}^M \abs{a_n}^2 \to 0$ as $N, M \to \infty$.

:::

::: pf-step
Thus $(s_N)_{N=1}^\infty$ is a Cauchy sequence in the Hilbert space $\mathcal{H}$.

:::

::: pf-step
By completeness of $\mathcal{H}$, there exists a limit element $x = \lim_{N \to \infty} s_N = \sum_{n=1}^\infty a_n u_n \in \mathcal{H}$.

:::

::: pf-step
Coefficients of $x$: For each fixed $m \in \NN$, by the continuity of the inner product in $\mathcal{H}$:
$$\langle x, u_m \rangle = \left\langle \lim_{N \to \infty} s_N, u_m \right\rangle = \lim_{N \to \infty} \langle s_N, u_m \rangle = \lim_{N \to \infty} \sum_{n=1}^N a_n \langle u_n, u_m \rangle.$$
For all $N \ge m$, $\sum_{n=1}^N a_n \delta_{n, m} = a_m$. Thus $\langle x, u_m \rangle = a_m$ for all $m \in \NN$.

:::

::: pf-step
Norm of $x$: By the continuity of the Hilbert space norm:
$$\norm{x}^2 = \lim_{N \to \infty} \norm{s_N}^2 = \lim_{N \to \infty} \sum_{n=1}^N \abs{a_n}^2 = \sum_{n=1}^\infty \abs{a_n}^2 = \sum_{n=1}^\infty \abs{\langle x, u_n \rangle}^2.$$

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
Bessel's inequality holds for all $x \in \mathcal{H}$, and every $\ell^2$ sequence corresponds to an element $x \in \mathcal{H}$ satisfying Parseval's equality.
:::

:::

:::

:::
