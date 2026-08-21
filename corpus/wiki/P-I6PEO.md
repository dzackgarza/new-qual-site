---
schema: qual/card@1
id: P-I6PEO
kind: problem
title: $1/f$ has bounded variation on $[a,b]$ when $f$ does and $|f|\ge c>0$
classification:
  areas:
  - real-analysis
  topics:
  - Variation
relations: []
review: draft
solved: true
---

::: problem
Let $f$ be a function of bounded variation on $[a,b]$.
Furthermore, assume that for some $c>0$, $|f(x)| \geq c$ on $[a,b]$.
Show that $g(x) = 1/f(x)$ is of bounded variation on $[a,b]$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. For $x, y \in [a,b]$: $\left|\frac{1}{f(x)} - \frac{1}{f(y)}\right| = \frac{|f(x) - f(y)|}{|f(x)f(y)|} \le \frac{1}{c^2}|f(x) - f(y)|$.
Proof: $\frac{1}{f(x)} - \frac{1}{f(y)} = \frac{f(y) - f(x)}{f(x)f(y)}$; and $|f(x)f(y)| \ge c^2$ by the hypothesis $|f| \ge c > 0$.

<1>2. For any partition $a = x_0 < \cdots < x_n = b$: $\sum_{i=1}^n \left|\frac{1}{f(x_i)} - \frac{1}{f(x_{i-1})}\right| \le \frac{1}{c^2}\sum_{i=1}^n |f(x_i) - f(x_{i-1})| \le \frac{1}{c^2}V_{[a,b]}(f)$.
Proof: <1>1 applied term by term; the last inequality is the definition of total variation.

<1>3. Q.E.D.: $g = 1/f$ is of bounded variation on $[a,b]$, with $V(g) \le V(f)/c^2$.
Proof: <1>2 bounds every partition sum of $g$ uniformly, so the total variation of $g$ is finite.
:::
