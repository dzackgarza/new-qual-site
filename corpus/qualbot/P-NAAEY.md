---
schema: qual/card@1
id: P-NAAEY
kind: problem
title: $\lim_{n\to\infty}\|f+g(\,\cdot\,-n)\|_1=\|f\|_1+\|g\|_1$ for $f,g\in L^1(\mathbb{R})$
classification:
  areas:
  - real-analysis
  topics:
  - l1
  - small-tails
  - norms
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $f$ and $g$ be Lebesgue integrable on $\mathbb{R}$.
Let $g_n(x) = g(x - n)$.
Prove that $$\lim_{n \to \infty} \|f + g_n\|_1 = \|f\|_1 + \|g\|_1.$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

By the triangle inequality for the $L^1$ norm, for all $n$:
$$
\|f + g_n\|_1 \leq \|f\|_1 + \|g_n\|_1 = \|f\|_1 + \|g\|_1,
$$
since translation is an isometry on $L^1(\RR)$: $\|g_n\|_1 = \int_\RR |g(x-n)|\, dx = \int_\RR |g(y)|\, dy = \|g\|_1$.
Thus $\limsup_{n \to \infty} \|f + g_n\|_1 \leq \|f\|_1 + \|g\|_1$.

To establish the reverse inequality for the $\liminf$: Let $\varepsilon > 0$.
Since continuous functions with compact support $C_c(\RR)$ are dense in $L^1(\RR)$, there exist $f_0, g_0 \in C_c(\RR)$ such that:
$$
\|f - f_0\|_1 < \varepsilon, \qquad \|g - g_0\|_1 < \varepsilon.
$$
Let $\operatorname{supp}(f_0) \subseteq [-M, M]$ and $\operatorname{supp}(g_0) \subseteq [-M, M]$ for some $M > 0$.
Define $g_{0, n}(x) = g_0(x - n)$.
Then $\operatorname{supp}(g_{0, n}) \subseteq [n - M, n + M]$.

For all $n > 2M$, the supports of $f_0$ and $g_{0, n}$ are completely disjoint:
$$
[-M, M] \cap [n - M, n + M] = \emptyset.
$$
For disjointly supported functions in $L^1$:
$$
\|f_0 + g_{0, n}\|_1 = \int_\RR |f_0(x) + g_0(x - n)|\, dx = \int_\RR |f_0(x)|\, dx + \int_\RR |g_0(x - n)|\, dx = \|f_0\|_1 + \|g_0\|_1.
$$

Now compare $\|f + g_n\|_1$ and $\|f_0 + g_{0, n}\|_1$:
$$
\big| \|f + g_n\|_1 - \|f_0 + g_{0, n}\|_1 \big| \leq \|(f + g_n) - (f_0 + g_{0, n})\|_1 \leq \|f - f_0\|_1 + \|g_n - g_{0, n}\|_1 < 2\varepsilon.
$$
Therefore, for all $n > 2M$:
$$
\|f + g_n\|_1 \geq \|f_0 + g_{0, n}\|_1 - 2\varepsilon = \|f_0\|_1 + \|g_0\|_1 - 2\varepsilon.
$$
Since $|\|f\|_1 - \|f_0\|_1| \leq \|f - f_0\|_1 < \varepsilon$ and $|\|g\|_1 - \|g_0\|_1| < \varepsilon$, we have:
$$
\|f + g_n\|_1 \geq \|f\|_1 + \|g\|_1 - 4\varepsilon.
$$
Taking $\liminf_{n \to \infty}$:
$$
\liminf_{n \to \infty} \|f + g_n\|_1 \geq \|f\|_1 + \|g\|_1 - 4\varepsilon.
$$
Since $\varepsilon > 0$ was arbitrary, $\liminf_{n \to \infty} \|f + g_n\|_1 \geq \|f\|_1 + \|g\|_1$.

Combining with the upper bound:
$$
\lim_{n \to \infty} \|f + g_n\|_1 = \|f\|_1 + \|g\|_1.
$$
:::
