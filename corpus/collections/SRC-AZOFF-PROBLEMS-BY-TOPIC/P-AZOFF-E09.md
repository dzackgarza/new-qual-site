---
schema: qual/card@1
id: P-AZOFF-E09
kind: problem
title: Entire functions with $|f(z)|\le\sqrt{|z|}$ for large $|z|$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Liouville, FTA, and power series, Problem 9, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Cauchy's coefficient estimate on circles of radius R>10 forces every
    positive-degree Taylor coefficient to vanish. The remaining constant c
    satisfies the bound exactly when |c|<=sqrt(10).
---

::: {.problem}
Find, with proof, all entire functions satisfying $| f ( z ) | \leq \sqrt { | z | } \mathrm { ~ f o r ~ } | z | > 1 0$
:::

::: {.solution}
Write
$$
f(z)=\sum_{n=0}^{\infty}a_nz^n.
$$

<1>1. For every integer $n\geq1$ and every $R>10$,
$$
\abs{a_n}\leq R^{1/2-n}.
$$

::: {.proof}
Cauchy's coefficient formula on the circle $\abs{\zeta}=R$ gives
$$
a_n
=
\frac{1}{2\pi i}
\int_{\abs{\zeta}=R}
\frac{f(\zeta)}{\zeta^{n+1}}
\,d\zeta.
$$
Since $R>10$, the hypothesis gives
$$
\abs{f(\zeta)}\leq\sqrt R
$$
on this circle. Therefore
$$
\begin{aligned}
\abs{a_n}
&\leq
\frac{1}{2\pi}(2\pi R)
\frac{R^{1/2}}{R^{n+1}}\\
&=
R^{1/2-n}.
\end{aligned}
$$
:::

<1>2. Every Taylor coefficient $a_n$ with $n\geq1$ is zero.

::: {.proof}
Fix $n\geq1$. The estimate in step <1>1 holds for every $R>10$, and
$$
R^{1/2-n}\longrightarrow0
$$
as $R\to\infty$. Hence $\abs{a_n}=0$.
:::

<1>3. Every entire function satisfying the hypothesis is constant.

::: {.proof}
By step <1>2,
$$
f(z)=a_0
$$
for every $z\in\CC$.
:::

<1>4. If $f\equiv c$ satisfies the hypothesis, then
$$
\abs{c}\leq\sqrt{10}.
$$

::: {.proof}
For every real $R>10$, choose $z$ with $\abs{z}=R$. The hypothesis gives
$$
\abs{c}\leq\sqrt R.
$$
Letting $R\downarrow10$ yields $\abs{c}\leq\sqrt{10}$.
:::

<1>5. Conversely, every constant $c\in\CC$ with
$\abs{c}\leq\sqrt{10}$ satisfies the hypothesis.

::: {.proof}
If $\abs{z}>10$, then
$$
\abs{c}
\leq
\sqrt{10}
<
\sqrt{\abs{z}}.
$$
Thus $f\equiv c$ satisfies the required inequality.
:::

<1>6. The complete list is
$$
\boxed{
f(z)=c,
\qquad
c\in\CC,
\qquad
\abs{c}\leq\sqrt{10}.
}
$$

::: {.proof}
Steps <1>3 and <1>4 show that every solution is on the displayed list, and
step <1>5 shows that every function on the list is a solution.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the requested classification.
:::
:::
