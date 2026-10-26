---
schema: qual/card@1
id: P-TIE-F11-16
kind: problem
title: Entire functions with $|f(z)|\le M|z|^2$ are quadratic polynomials
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2011, question 16.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the LaTeX against Fall 2011, question 16, page 6 of Questions_from_Tie.pdf, which prints f(z) <= M|z|^2 without the modulus, and added an erratum remark giving the intended hypothesis |f(z)| <= M|z|^2.
---

::: {.problem}
Let $f(z)$ be entire and assume that $f(z) \le M\abs{z}^2$ outside some disk for some constant $M$. Show that $f(z)$ is a polynomial in $z$ of degree $\le 2$.
:::

::: {.remark}
Erratum: the source writes the hypothesis as $f(z) \le M\abs{z}^2$, which has no meaning for complex values of $f$.
The intended hypothesis is $\abs{f(z)} \le M\abs{z}^2$ outside some disk.
:::

Use the intended hypothesis from the remark: there exists $R_0>0$ such that
$$
\abs{f(z)}\le M\abs{z}^2
$$
whenever $\abs{z}\ge R_0$.

::: pf

::: pf-step

For every integer $n\ge0$ and every $R\ge R_0$,
$$
\frac{\abs{f^{(n)}(0)}}{n!}
\le
M R^{2-n}.
$$


::: pf-proof

Since $f$ is entire, Cauchy's integral formula for derivatives on the circle $\abs{z}=R$ gives
$$
f^{(n)}(0)
=
\frac{n!}{2\pi i}
\int_{\abs{z}=R}\frac{f(z)}{z^{n+1}}\,dz.
$$
Hence
$$
\begin{aligned}
\frac{\abs{f^{(n)}(0)}}{n!}
&\le
\frac1{2\pi}
\left(2\pi R\right)
\frac{\max_{\abs{z}=R}\abs{f(z)}}{R^{n+1}}\\
&=
\frac{\max_{\abs{z}=R}\abs{f(z)}}{R^n}.
\end{aligned}
$$
For $R\ge R_0$, the intended growth hypothesis gives
$$
\max_{\abs{z}=R}\abs{f(z)}
\le
MR^2.
$$
Substitution yields the stated estimate.

:::

:::

::: pf-step

For every $n\ge3$,
$$
f^{(n)}(0)=0.
$$


::: pf-proof

Fix $n\ge3$. By step <1>1,
$$
\frac{\abs{f^{(n)}(0)}}{n!}
\le
MR^{2-n}
$$
for every $R\ge R_0$. Since $2-n<0$, the right-hand side tends to $0$ as $R\to\infty$. Therefore $f^{(n)}(0)=0$.

:::

:::

::: pf-step

The function $f$ is a polynomial of degree at most $2$.


::: pf-proof

Because $f$ is entire, its Taylor series at $0$ converges to $f$ on all of $\CC$:
$$
f(z)
=
\sum_{n=0}^\infty
\frac{f^{(n)}(0)}{n!}z^n.
$$
By step <1>2, every coefficient with $n\ge3$ vanishes. Hence
$$
\boxed{
f(z)
=
f(0)+f'(0)z+\frac{f''(0)}2z^2,
}
$$
so $f$ has degree at most $2$.

:::

:::

::: pf-qed

Step <1>3 proves the required conclusion.

:::

:::
