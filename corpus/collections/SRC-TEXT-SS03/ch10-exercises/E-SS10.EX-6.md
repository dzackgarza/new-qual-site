---
schema: qual/card@1
id: E-SS10.EX-6
kind: problem
title: Bounds $e^{c_1\sqrt n}\le p(n)\le e^{c_2\sqrt n}$ for the partition function
classification:
  areas:
  - complex-analysis
  topics:
  - Partitions
  - Generating Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
6. Show as a consequence of Exercise 5 that
$$
e^{c_1 n^{1/2}} \leq p(n) \leq e^{c_2 n^{1/2}}
$$
for two positive constants $c_1$ and $c_2$.

[Hint: $F(e^{-y}) = \sum p(n) e^{-ny} \le C e^{c/y}$ as $y \to 0$. So $p(n) e^{-ny} \leq C e^{c/y}$. Take $y = 1/n^{1/2}$ to get $p(n) \leq c' e^{c' n^{1/2}}$. In the opposite direction,
$$
\sum_{n=0}^m p(n) e^{-ny} \geq C(e^{c/y} - \sum_{n=m+1}^\infty e^{c n^{1/2}} e^{-ny}),
$$
and it suffices to take $y = A m^{-1/2}$ where $A$ is a large constant, and use the fact that the sequence $p(n)$ is increasing.]
:::

::: {.solution}
Let $F(e^{-y}) = \sum_{k\ge0} p(k) e^{-ky}$ for $y > 0$. By [[E-SS10.EX-5]], $\log F(e^{-y})\sim\frac{\pi^2}{6(1-e^{-y})}\sim\frac{\pi^2}{6y}$ as $y\to0^+$, so there are constants $C,c,C_0,c_0>0$ with
$$C_0e^{c_0/y}\le F(e^{-y})\le Ce^{c/y}\qquad(0<y\le1).$$

::: pf

::: {.pf-step #s1}

There is $c_2>0$ with $p(n) \le e^{c_2 \sqrt{n}}$ for all $n\ge1$.

::: pf-proof

Since $p(k)\ge0$, for $n\ge1$ and $0<y\le1$ we have $p(n) e^{-ny} \le F(e^{-y}) \le C e^{c/y}$, so $p(n) \le C e^{c/y + ny}$. Taking $y = \sqrt{c/n}$ when $c\le n$ gives $c/y + ny = 2\sqrt{cn}$, hence $p(n) \le C e^{2\sqrt{c n}}\le e^{c_2\sqrt n}$ with $c_2 = 2\sqrt{c} + \max(0, \log C)$. Enlarging $c_2$ covers the finitely many $n<c$.

:::

:::

::: {.pf-step #s2}

There are $c_1'>0$ and $M$ with $p(m) \ge e^{c_1' \sqrt{m}}$ for all $m\ge M$.

::: pf-proof

Fix $A > c_2$ and put $y = A/\sqrt{m}$, with $m\ge A^2$ so that $y\le1$. Since $p$ is nondecreasing,
$$\frac{p(m)}{1 - e^{-y}} > \sum_{k=0}^m p(k) e^{-ky} \ge C_0 e^{c_0/y} - \sum_{k=m+1}^\infty p(k) e^{-ky}.$$
For $k \ge m+1$, $\sqrt{k} \le k/\sqrt{m}$, so step [](#s1){.pf-ref} gives $p(k)e^{-ky}\le e^{-(A - c_2)k/\sqrt{m}}$ and
$$\sum_{k=m+1}^\infty p(k) e^{-ky} \le \frac{e^{-(A - c_2)(m+1)/\sqrt{m}}}{1 - e^{-(A - c_2)/\sqrt{m}}} \le \frac{2\sqrt{m}}{A - c_2} e^{-(A - c_2)\sqrt{m}}$$
for $m$ large. The main term is $C_0 e^{c_0/y} = C_0 e^{(c_0/A)\sqrt{m}}\to\infty$ while the tail tends to $0$, so for $m\ge M$ the right side is at least $\frac12C_0 e^{(c_0/A)\sqrt{m}}$. Using $1 - e^{-y}\ge y/2$ for $0<y\le1$,
$$p(m) \ge \frac{C_0 A}{4\sqrt{m}} e^{(c_0/A)\sqrt{m}} \ge e^{c_1' \sqrt{m}}$$
for any $c_1'\in(0,c_0/A)$, after enlarging $M$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} is the upper bound. For the lower bound, step [](#s2){.pf-ref} covers $n\ge M$. For $2\le n<M$ we have $p(n)\ge2$, so decreasing $c_1\le c_1'$ gives $e^{c_1\sqrt n}\le p(n)$ for these finitely many $n$; hence $e^{c_1 \sqrt{n}} \le p(n)$ for all $n \ge 2$. The lower bound cannot hold at $n=1$ for any $c_1>0$, since $p(1)=1<e^{c_1}$.

:::

:::

:::
