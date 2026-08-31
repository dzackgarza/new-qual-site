---
schema: qual/card@1
id: E-SS10.EX-6
kind: exercise
title: "SS 10.6: Exponential square-root bounds for the partition function"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
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

::: solution
**Goal:** Prove the asymptotic exponential bounds $e^{c_1 \sqrt{n}} \le p(n) \le e^{c_2 \sqrt{n}}$ for the partition function $p(n)$.

<1>1. Upper bound $p(n) \le e^{c_2 \sqrt{n}}$:
    *Proof:*
    <2>1. The partition generating function is $F(e^{-y}) = \sum_{k=0}^\infty p(k) e^{-ky}$ for $y > 0$.
    <2>2. From Exercise 5 (modular transformation of the Dedekind eta function / Jacobi theta function), there exist positive constants $C, c > 0$ such that $F(e^{-y}) \le C e^{c/y}$ for all $y \in (0, 1]$.
    <2>3. Because every partition count $p(k) \ge 0$, for any integer $n \ge 1$ and any $y > 0$:
    $$p(n) e^{-ny} \le \sum_{k=0}^\infty p(k) e^{-ky} = F(e^{-y}) \le C e^{c/y}.$$
    <2>4. Multiplying both sides by $e^{ny}$ yields $p(n) \le C e^{c/y + ny}$.
    <2>5. Choose $y = \sqrt{c/n} > 0$. Then $\frac{c}{y} + ny = c \sqrt{\frac{n}{c}} + n \sqrt{\frac{c}{n}} = 2\sqrt{c n}$.
    <2>6. Thus $p(n) \le C e^{2\sqrt{c n}} \le e^{c_2 \sqrt{n}}$ for all $n \ge 1$, where $c_2 = 2\sqrt{c} + \max(0, \ln C)$.

<1>2. Lower bound $p(n) \ge e^{c_1 \sqrt{n}}$:
    *Proof:*
    <2>1. From Exercise 5, the asymptotic behavior as $y \to 0^+$ gives a lower bound $F(e^{-y}) \ge C_0 e^{c_0/y}$ for constants $C_0, c_0 > 0$.
    <2>2. For any positive integer $m$, split the series into the head and tail:
    $$\sum_{k=0}^m p(k) e^{-ky} = F(e^{-y}) - \sum_{k=m+1}^\infty p(k) e^{-ky} \ge C_0 e^{c_0/y} - \sum_{k=m+1}^\infty p(k) e^{-ky}.$$
    <2>3. Since $p(k)$ is non-decreasing ($p(0) \le p(1) \le p(2) \le \cdots$), the head satisfies
    $$\sum_{k=0}^m p(k) e^{-ky} \le p(m) \sum_{k=0}^m e^{-ky} < p(m) \sum_{k=0}^\infty e^{-ky} = \frac{p(m)}{1 - e^{-y}}.$$
    <2>4. For the tail, use the upper bound $p(k) \le e^{c_2 \sqrt{k}}$ from <1>1. For $k \ge m+1$, $\sqrt{k} = \frac{k}{\sqrt{k}} \le \frac{k}{\sqrt{m+1}} \le \frac{k}{\sqrt{m}}$.
    <2>5. Set $y = \frac{A}{\sqrt{m}}$ with constant $A > c_2$. Then for each $k \ge m+1$:
    $$c_2 \sqrt{k} - ky \le \frac{c_2 k}{\sqrt{m}} - \frac{A k}{\sqrt{m}} = -\frac{(A - c_2)}{\sqrt{m}} k.$$
    <2>6. Summing this geometric tail:
    $$\sum_{k=m+1}^\infty e^{c_2 \sqrt{k} - ky} \le \sum_{k=m+1}^\infty e^{-(A - c_2) k / \sqrt{m}} = \frac{e^{-(A - c_2)(m+1)/\sqrt{m}}}{1 - e^{-(A - c_2)/\sqrt{m}}} \le \frac{2\sqrt{m}}{A - c_2} e^{-(A - c_2)\sqrt{m}}.$$
    <2>7. With $y = A/\sqrt{m}$, the main term is $C_0 e^{c_0/y} = C_0 e^{(c_0/A)\sqrt{m}}$.
    <2>8. Choose $A > c_2$. Since $e^{-(A - c_2)\sqrt{m}} \to 0$ exponentially while $e^{(c_0/A)\sqrt{m}} \to \infty$, there exists $M \in \mathbb{N}$ such that for all $m \ge M$:
    $$C_0 e^{c_0/y} - \sum_{k=m+1}^\infty p(k) e^{-ky} \ge \frac{1}{2} C_0 e^{(c_0/A)\sqrt{m}}.$$
    <2>9. Combining with <2>3, for all $m \ge M$:
    $$p(m) \ge \frac{1}{2} C_0 (1 - e^{-A/\sqrt{m}}) e^{(c_0/A)\sqrt{m}} \ge \frac{C_0 A}{4\sqrt{m}} e^{(c_0/A)\sqrt{m}} \ge e^{c_1 \sqrt{m}}$$
    for some positive constant $c_1 \in (0, c_0/A)$.

<1>3. Conclusion:
    *Proof:*
    Decreasing $c_1 > 0$ to accommodate the finitely many values $1 \le n < M$ (since $p(n) \ge 1$ for all $n \ge 1$), we obtain
    $$e^{c_1 \sqrt{n}} \le p(n) \le e^{c_2 \sqrt{n}}$$
    for all $n \ge 1$.
:::
