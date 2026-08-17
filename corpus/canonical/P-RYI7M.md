---
schema: qual/card@1
id: P-RYI7M
kind: problem
title: $f_n\to f$ a.e. and $\int|f_n|\to\int|f|$ imply $\int f_n\to\int f$
classification:
  areas:
  - real-analysis
  topics:
  - convergence-of-integrals
  - convergence-of-functions
  - lp-spaces
relations: []
review: draft
solved: true
---

::: problem
Suppose that

- $f_n, f \in L^1$,

- $f_n \to f$ almost everywhere, and

- $\int\left|f_{n}\right| \rightarrow \int|f|$.

Show that $\int f_{n} \rightarrow \int f$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

We will prove the stronger result that $\int |f_n - f| \to 0$ (convergence in $L^1$), which immediately implies $\left|\int f_n - \int f\right| \leq \int |f_n - f| \to 0$.

1. By the triangle inequality:
$$
|f_n - f| \leq |f_n| + |f| \implies |f_n| + |f| - |f_n - f| \geq 0.
$$
Define $g_n(x) = |f_n(x)| + |f(x)| - |f_n(x) - f(x)| \geq 0$ for all $n$.

2. Since $f_n(x) \to f(x)$ a.e., we have $|f_n(x) - f(x)| \to 0$ a.e., so:
$$
\lim_{n \to \infty} g_n(x) = |f(x)| + |f(x)| - 0 = 2|f(x)| \quad \text{almost everywhere.}
$$

3. By **Fatou's Lemma** applied to the non-negative sequence $g_n$:
$$
\int \liminf_{n \to \infty} g_n \leq \liminf_{n \to \infty} \int g_n.
$$
Computing the left-hand side:
$$
\int 2|f| = 2 \int |f|.
$$
Computing the right-hand side:
$$
\liminf_{n \to \infty} \int g_n = \liminf_{n \to \infty} \left( \int |f_n| + \int |f| - \int |f_n - f| \right) = \int |f| + \lim_{n \to \infty} \int |f_n| - \limsup_{n \to \infty} \int |f_n - f|.
$$
Using the hypothesis that $\lim_{n \to \infty} \int |f_n| = \int |f|$:
$$
\liminf_{n \to \infty} \int g_n = 2\int |f| - \limsup_{n \to \infty} \int |f_n - f|.
$$

4. Comparing the two sides:
$$
2\int |f| \leq 2\int |f| - \limsup_{n \to \infty} \int |f_n - f| \implies \limsup_{n \to \infty} \int |f_n - f| \leq 0.
$$
Since $\int |f_n - f| \geq 0$ for all $n$, we have:
$$
\lim_{n \to \infty} \int |f_n - f| = 0.
$$

5. Finally, by the triangle inequality for integrals:
$$
\left| \int f_n - \int f \right| = \left| \int (f_n - f) \right| \leq \int |f_n - f| \to 0 \quad \text{as } n \to \infty.
$$
Thus $\lim_{n \to \infty} \int f_n = \int f$.
:::
