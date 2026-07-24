---
schema: qual/card@1
id: E-6ULIT
kind: exercise
title: "Show that a uniform limit of continuous functions is continuous, and a\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Show that a uniform limit of continuous functions is continuous, and a uniform limit of uniformly continuous functions is uniformly continuous.
Show that this is not true if uniform convergence is weakened to pointwise convergence.

:::

:::{.solution}
Suppose $\norm{f_n - f}_\infty\to 0$, fix $\eps$, we then need to produce a $\delta$ so that
\[
\abs{z-w}\leq \delta \implies \abs{f(z) - f(w) } < \eps
.\]

Write
\[
\abs{f(z) - f(w)} \leq \abs{f(z) - f_n(z)} + \abs{f_n(z) - f_n(w)} + \abs{f_n(w) - f(w)}
.\]

- Bound the first term by $\eps/3$ using that $f_n\to f$
- Bound the second term by $\eps/3$ using that $f_n$ is continuous 
- Bound the third term by $\eps/3$ using that $f_n\to f$
- Pick $\delta$ to be the minimum $\delta$ supplied by these three bounds.

Why uniform convergence is necessary: need these bounds to holds for all $z, w$ where $\abs{z-w} < \delta$.
Why pointwise convergence doesn't work: $f_n(z) \da z^n \convergesto{n\to\infty}\chi_{z=1}$

For uniform continuity: take $\sup_{z, w}$ on both sides:
\[
\sup_{z, w} \abs{f(z) - f(w)} 
&\leq \sup_{z} \abs{f(z) - f_n(z)} + \sup_{z, w} \abs{f_n(z) - f_n(w)} + \sup_{w} \abs{f_n(w) - f(w)} \\
&\leq \norm{f - f_n}_\infty + \sup_{z, w} \abs{f_n(z) - f_n(w)} + \norm{f-f_n}_\infty 
,\]
where now the middle term is bounded by uniform continuity of $f_n$.

:::

