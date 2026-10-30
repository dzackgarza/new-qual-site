---
schema: qual/card@1
id: P-TIE-F09-14
kind: problem
title: Entire functions with $\abs{f(z)}\le M\abs{z}^2$ are quadratic polynomials
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 14.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the LaTeX against Fall 2009, question 14, page 3 of Questions_from_Tie.pdf, which prints f(z) <= M|z|^2 without the modulus, and added an erratum remark giving the intended hypothesis |f(z)| <= M|z|^2.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Questions_from_Tie.pdf prints the hypothesis as f(z) <= M|z|^2; the statement now reads |f(z)| <= M|z|^2.
---

::: {.problem}
Let $f(z)$ be entire and assume that $\abs{f(z)} \le M\abs{z}^2$ outside some disk for some constant $M$. Show that $f(z)$ is a polynomial in $z$ of degree $\le 2$.
:::

::: {.solution}

By hypothesis there exists $R_0>0$ such that
$$
\abs{f(z)}\le M\abs{z}^2
\qquad
\text{whenever }\abs{z}\ge R_0.
$$
Write the entire power series
$$
f(z)=\sum_{n=0}^{\infty}a_nz^n.
$$

::: pf

::: {.pf-step #s1-1}

For every $r\ge R_0$ and every $n\ge0$,
$$
\abs{a_n}
\le
Mr^{2-n}.
$$


::: pf-proof

On the circle $\abs{z}=r$ the hypothesis gives
$$
\max_{\abs{z}=r}\abs{f(z)}\le Mr^2.
$$
Cauchy's coefficient formula gives
$$
a_n
=
\frac1{2\pi i}
\int_{\abs{z}=r}\frac{f(z)}{z^{n+1}}\,dz.
$$
Therefore
$$
\abs{a_n}
\le
\frac1{2\pi}(2\pi r)\frac{Mr^2}{r^{n+1}}
=
Mr^{2-n}.
$$

:::

:::

::: {.pf-step #s1-2}

For every $n\ge3$,
$$
a_n=0.
$$


::: pf-proof

Fix $n\ge3$. Step [](#s1-1){.pf-ref} holds for every arbitrarily large $r$, so
$$
\abs{a_n}
\le
Mr^{2-n}.
$$
Since $2-n<0$, the right-hand side tends to $0$ as $r\to\infty$. Hence $a_n=0$.

:::

:::

::: {.pf-step #s1-3}

Thus
$$
\boxed{f(z)=a_0+a_1z+a_2z^2},
$$
so $f$ is a polynomial of degree at most $2$.


::: pf-proof

Step [](#s1-2){.pf-ref} shows that every coefficient of degree at least $3$ vanishes.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
