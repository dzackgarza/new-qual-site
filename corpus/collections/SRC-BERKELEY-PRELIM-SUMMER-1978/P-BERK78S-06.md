---
schema: qual/card@1
id: P-BERK78S-06
kind: problem
title: Polynomial-growth bounds on an entire function
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Applied Cauchy's coefficient estimate on circles of radius R. Under
    growth O(R^{1/2}), every positive-degree Taylor coefficient tends to
    zero. Under growth O(R^{5/2}), every coefficient of degree at least
    three tends to zero, so the entire function is a polynomial of degree
    at most two.
---

::: {.problem}
Let $f:\mathbb C\to\mathbb C$ be entire, and let $a,b>0$.

1. If
   \[
   |f(z)|\le a\sqrt{|z|}+b
   \]
   for all $z$, prove that $f$ is constant.
2. What can one prove about $f$ if
   \[
   |f(z)|\le a|z|^{5/2}+b
   \]
   for all $z$?
:::

::: {.solution}
Write the Taylor expansion at the origin as
$$
f(z)=\sum_{n=0}^{\infty}c_nz^n.
$$

<1>1. If
$$
\abs{f(z)}
\leq
a\sqrt{\abs{z}}+b
$$
for every $z$, then for every $R>0$ and every integer $n\geq1$,
$$
\abs{c_n}
\leq
\frac{aR^{1/2}+b}{R^n}.
$$

::: {.proof}
Cauchy's coefficient formula on the circle $\abs{\zeta}=R$ gives
$$
c_n
=
\frac{1}{2\pi i}
\int_{\abs{\zeta}=R}
\frac{f(\zeta)}{\zeta^{n+1}}
\,d\zeta.
$$
On that circle,
$$
\abs{f(\zeta)}
\leq
aR^{1/2}+b.
$$
Since the circle has length $2\pi R$,
$$
\begin{aligned}
\abs{c_n}
&\leq
\frac1{2\pi}
(2\pi R)
\frac{aR^{1/2}+b}{R^{n+1}}\\
&=
\frac{aR^{1/2}+b}{R^n}.
\end{aligned}
$$
:::

<1>2. Under the hypothesis of part (1),
$$
c_n=0
$$
for every $n\geq1$.

::: {.proof}
Fix $n\geq1$. Step <1>1 gives
$$
\abs{c_n}
\leq
aR^{1/2-n}+bR^{-n}
$$
for every $R>0$. Since
$$
\frac12-n<0,
$$
both terms on the right tend to zero as $R\to\infty$. Therefore
$$
\abs{c_n}=0.
$$
:::

<1>3. Under the hypothesis of part (1),
$$
\boxed{f\text{ is constant}.}
$$

::: {.proof}
By step <1>2, every Taylor coefficient of positive degree vanishes. Hence
$$
f(z)=c_0
$$
for every $z\in\CC$.
:::

<1>4. If
$$
\abs{f(z)}
\leq
a\abs{z}^{5/2}+b
$$
for every $z$, then for every $R>0$ and every integer $n\geq0$,
$$
\abs{c_n}
\leq
\frac{aR^{5/2}+b}{R^n}.
$$

::: {.proof}
The proof is identical to step <1>1, with the new growth bound replacing
the old one in Cauchy's coefficient estimate.
:::

<1>5. Under the hypothesis of part (2),
$$
c_n=0
$$
for every $n\geq3$.

::: {.proof}
Fix $n\geq3$. Step <1>4 gives
$$
\abs{c_n}
\leq
aR^{5/2-n}+bR^{-n}.
$$
Since
$$
\frac52-n<0,
$$
the right-hand side tends to zero as $R\to\infty$. Therefore
$$
c_n=0.
$$
:::

<1>6. Under the hypothesis of part (2),
$$
\boxed{
f\text{ is a polynomial of degree at most }2.
}
$$

::: {.proof}
Step <1>5 shows that every Taylor coefficient of degree at least $3$
vanishes. Thus
$$
f(z)=c_0+c_1z+c_2z^2.
$$
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>3 proves part (1), and step <1>6 gives the conclusion for part
(2).
:::
:::
