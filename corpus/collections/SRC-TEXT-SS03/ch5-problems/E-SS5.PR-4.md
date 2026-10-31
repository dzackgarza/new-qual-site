---
schema: qual/card@1
id: E-SS5.PR-4
kind: problem
title: Growth order of an entire function from its Taylor coefficients
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
Let

$$
F(z)=\sum_{n=0}^{\infty}a_nz^n
$$

be an entire function of finite order.
The growth order of $F$ is linked with the growth of the coefficients $a_n$ as $n\to\infty$.

(a) Suppose that

$$
\abs{F(z)}\leq Ae^{a\abs{z}^\rho}.
$$

Show that

$$
\limsup_{n\to\infty}\abs{a_n}^{1/n}n^{1/\rho}<\infty.
\tag{8}
$$

(b) Conversely, if (8) holds, show that

$$
\abs{F(z)}\leq A_\varepsilon e^{a_\varepsilon\abs{z}^{\rho+\varepsilon}}
$$

for every $\varepsilon>0$.

*Hint.* For part (a), use Cauchy's inequality

$$
\abs{a_n}\leq \frac{A}{r^n}e^{ar^\rho}
$$

and the fact that $u^{-n}e^{u^\rho}$, for $u>0$, has minimum

$$
e^{n/\rho}\left(\frac{\rho}{n}\right)^{n/\rho}
$$

at $u=n^{1/\rho}/\rho^{1/\rho}$.
Choose $r$ in terms of $n$ to attain this minimum.

For part (b), note that for $\abs{z}=r$,

$$
\abs{F(z)}
\leq \sum_n\frac{c^nr^n}{n^{n/\rho}}
\leq \sum_n\frac{c^nr^n}{(n!)^{1/\rho}}
$$

for some constant $c$, since $n^n\geq n!$.
This reduces the problem to Problem 3.
:::

::: {.solution}
For part (a), Cauchy's inequality gives, for every $r>0$,
$$
\abs{a_n}\le \frac{A}{r^n}e^{ar^\rho}.
$$
Choose
$$
r=\left(\frac{n}{a\rho}\right)^{1/\rho}.
$$
Then $ar^\rho=n/\rho$, and therefore
$$
\abs{a_n}^{1/n}
\le A^{1/n}e^{1/\rho}\left(\frac{a\rho}{n}\right)^{1/\rho}.
$$
Hence
$$
\limsup_{n\to\infty}\abs{a_n}^{1/n}n^{1/\rho}
\le e^{1/\rho}(a\rho)^{1/\rho}<\infty.
$$

Conversely, assume (8). Then there is $c>0$ such that, for all sufficiently large $n$,
$$
\abs{a_n}\le \frac{c^n}{n^{n/\rho}}.
$$
After increasing a constant to absorb finitely many initial terms,
$$
\abs{F(z)}\le C\sum_{n=0}^\infty \frac{(c\abs{z})^n}{n^{n/\rho}}.
$$
Since $n!\le n^n$,
$$
\frac1{n^{n/\rho}}\le \frac1{(n!)^{1/\rho}}.
$$
Thus
$$
\abs{F(z)}\le C\sum_{n=0}^\infty\frac{(c\abs{z})^n}{(n!)^{1/\rho}}.
$$
By Problem 3, the entire function on the right has order $\rho$. Hence for every $\varepsilon>0$ there are constants $A_\varepsilon,a_\varepsilon>0$ such that
$$
\abs{F(z)}\le A_\varepsilon e^{a_\varepsilon\abs{z}^{\rho+\varepsilon}}.
$$
This proves the converse.
:::
