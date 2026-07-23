---
schema: qual/card@1
id: P-6LR5U
kind: problem
title: "Let $X$ be a complete metric space and define a norm"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let $X$ be a complete metric space and define a norm
$$
\|f\|:=\max \{|f(x)|: x \in X\}.
$$

Show that $(C^0(\RR), \norm{\wait} )$ (the space of continuous functions $f: X\to \RR$) is complete.

:::{.remark}
Shouldn't this be a supremum? The max may not exist?
:::

:::{.solution}
\hfill

Let $\theset{f_k}$ be a Cauchy sequence, so $\norm{f_k} < \infty$ for all $k$.
Then for a fixed $x$, the sequence $f_k(x)$ is Cauchy in $\RR$ and thus converges to some $f(x)$, so define $f$ by $f(x) \definedas \lim_{k\to\infty} f_k(x)$.

Then $\norm{f_k - f} = \max_{x\in X}\abs{f_k(x) - f(x)} \converges{k\to\infty}\to 0$, and thus $f_k \to f$ uniformly and thus $f$ is continuous. It just remains to show that $f$ has bounded norm.

Choose $N$ large enough so that $\norm{f - f_N} < \varepsilon$, and write $\norm{f_N} \definedas M < \infty$

\[
\norm{f} \leq \norm{f - f_N} + \norm{f_N} < \varepsilon + M < \infty
.\]
:::

