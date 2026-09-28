---
schema: qual/card@1
id: E-F6IXU
kind: problem
title: Translation is continuous in $L^1$
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Continuity
  - Density
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- $\star$: Prove continuity in $L^1$, i.e.
  \[
  f \in L^{1} \Longrightarrow \lim _{h \rightarrow 0} \int|f(x+h)-f(x)|=0
  .\]
:::


::: {.solution}
<1>1. For a bounded interval $I$ and $h \in \RR$, $\int |\chi_{I}(x+h) - \chi_{I}(x)|\,dx \leq 2|h|$.

::: {.proof}
The integral is the measure of the symmetric difference of $I$ and $I - h$, and each endpoint of $I$ contributes a set of measure at most $|h|$ to it.
:::

<1>2. For every step function $s = \sum_{i=1}^k c_i \chi_{I_i}$ with bounded intervals $I_i$, $\lim_{h\to0}\int |s(x+h) - s(x)|\,dx = 0$.

::: {.proof}
By the triangle inequality and step <1>1, $\int |s(x+h) - s(x)|\,dx \leq \sum_i |c_i| \int |\chi_{I_i}(x+h) - \chi_{I_i}(x)|\,dx \leq 2|h|\sum_i |c_i|$.
:::

<1>3. Step functions are dense in $L^1(\RR)$.

::: {.proof}
Simple functions $\sum_i c_i\chi_{E_i}$ with $m(E_i)<\infty$ are dense in $L^1(\RR)$, so it suffices to approximate $\chi_E$ for $m(E) < \infty$. By outer regularity there is an open $U \supseteq E$ with $m(U \setminus E) < \eps/2$. $U$ is a countable disjoint union of open intervals $J_k$ with $\sum_k m(J_k) = m(U) < \infty$, so for some $N$, $A = \bigcup_{k\le N} J_k$ satisfies $m(U \setminus A) < \eps/2$. Then $\norm{\chi_E - \chi_A}_1 = m(E \triangle A) < \eps$.
:::

<1>4. For every $f \in L^1(\RR)$ and $\eps > 0$ there is $\delta > 0$ with $\int |f(x+h) - f(x)|\,dx < \eps$ for $|h| < \delta$.

::: {.proof}
By step <1>3 choose a step function $s$ with $\norm{f - s}_1 < \eps/3$, and by step <1>2 choose $\delta > 0$ with $\int |s(x+h) - s(x)|\,dx < \eps/3$ for $|h| < \delta$. By the triangle inequality and translation invariance of Lebesgue measure,
$$
\int |f(x+h) - f(x)|\,dx \leq \int |f(x+h) - s(x+h)|\,dx + \int |s(x+h) - s(x)|\,dx + \int |s(x) - f(x)|\,dx < \eps.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the definition of $\lim_{h \to 0} \int|f(x+h)-f(x)|\,dx = 0$.
:::
:::
