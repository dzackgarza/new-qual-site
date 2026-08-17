---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-HW5
kind: problem
title: 'Analyze the Babylonian square-root iteration (warm-up)'
classification:
  areas:
  - real-analysis
  topics:
  - sequences-of-numbers
  - limits
  - fixed-points
relations: []
review: draft
---

::: {.problem title="?"}
(c.f. [Abb01, Exercise 2.4.5]) Let $x_1=2$ and define
$$
x_{n+1}=\frac12\left(x_n+\frac{2}{x_n}\right).
$$
Find $\lim_{n\to\infty}x_n$.
Hint: Show that $\{x_n\}$ is decreasing.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. $x_n \ge \sqrt2$ for all $n$.
    Proof: by AM-GM, $x_{n+1} = \frac12\big(x_n + \frac{2}{x_n}\big) \ge \sqrt{x_n\cdot\frac{2}{x_n}} = \sqrt2$ for every $n$; since $x_1 = 2 \ge \sqrt2$, all $x_n \ge \sqrt2$.
<1>2. The sequence is decreasing from $x_2$ onward.
    Proof: for $n \ge 1$,
    \[\frac{x_{n+1}}{x_n} = \frac12\left(1 + \frac{2}{x_n^2}\right) \le \frac12\left(1 + \frac{2}{2}\right) = 1,\]
    using $x_n^2 \ge 2$ from <1>1; so $x_{n+1} \le x_n$ for all $n$ (including $n=1$). Thus $(x_n)$ is decreasing and bounded below.
<1>3. The sequence converges and we identify the limit.
    Proof: $(x_n)$ is decreasing and bounded below by $\sqrt2$, so it converges to some $L \ge \sqrt2$. Taking limits in the recursion (the map $x \mapsto \frac12(x + 2/x)$ is continuous on $[\sqrt2, \infty)$),
    \[L = \frac12\left(L + \frac{2}{L}\right) \implies 2L = L + \frac{2}{L} \implies L^2 = 2 \implies L = \sqrt2\]
    (as $L \ge \sqrt2 > 0$).
<1>4. Q.E.D.
:::
