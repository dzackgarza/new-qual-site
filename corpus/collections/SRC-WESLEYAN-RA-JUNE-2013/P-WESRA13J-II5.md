---
schema: qual/card@1
id: P-WESRA13J-II5
kind: problem
title: 'Bounded convergence in measure implies $L^1$ convergence on finite measure spaces'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $(X,\mathcal B,\mu)$ satisfy $\mu(X)<\infty$.
Let $(f_n)$ be a uniformly bounded sequence of measurable functions and suppose $f_n\to0$ in measure.
Prove
\[
\int_X|f_n|\,d\mu\to0.
\]
:::

::: {.solution}
Choose $M<\infty$ such that
$$
\abs{f_n(x)}\leq M
$$
for almost every $x\in X$ and every $n$.

<1>1. For every $\varepsilon>0$, if
$$
E_{n,\varepsilon}=\{x:\abs{f_n(x)}>\varepsilon\},
$$
then
$$
\int_X\abs{f_n}\,d\mu
\leq
\varepsilon\mu(X)+M\mu(E_{n,\varepsilon}).
$$

::: {.proof}
Split the integral over $E_{n,\varepsilon}$ and its complement. On $X\setminus E_{n,\varepsilon}$ one has $\abs{f_n}\leq\varepsilon$, while on $E_{n,\varepsilon}$ one has $\abs{f_n}\leq M$ almost everywhere. Thus
$$
\begin{aligned}
\int_X\abs{f_n}\,d\mu
&=\int_{X\setminus E_{n,\varepsilon}}\abs{f_n}\,d\mu
+\int_{E_{n,\varepsilon}}\abs{f_n}\,d\mu\\
&\leq\varepsilon\mu(X\setminus E_{n,\varepsilon})
+M\mu(E_{n,\varepsilon})\\
&\leq\varepsilon\mu(X)+M\mu(E_{n,\varepsilon}).
\end{aligned}
$$
:::

<1>2. For every $\varepsilon>0$,
$$
\limsup_{n\to\infty}\int_X\abs{f_n}\,d\mu
\leq
\varepsilon\mu(X).
$$

::: {.proof}
Because $f_n\to0$ in measure,
$$
\mu(E_{n,\varepsilon})\longrightarrow0
$$
for every fixed $\varepsilon>0$. Taking the upper limit in the estimate from step <1>1 therefore gives
$$
\limsup_{n\to\infty}\int_X\abs{f_n}\,d\mu
\leq\varepsilon\mu(X).
$$
:::

<1>3. One has
$$
\boxed{\int_X\abs{f_n}\,d\mu\longrightarrow0}.
$$

::: {.proof}
The quantity
$$
L=\limsup_{n\to\infty}\int_X\abs{f_n}\,d\mu
$$
is nonnegative. Step <1>2 gives
$$
0\leq L\leq\varepsilon\mu(X)
$$
for every $\varepsilon>0$. Since $\mu(X)<\infty$, letting $\varepsilon\downarrow0$ yields $L=0$. Nonnegativity of the integrals then implies their limit is zero.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
