---
schema: qual/card@1
id: P-TIE-F15-06
kind: problem
title: Liouville's theorem via $\int_{\abs{z}=R}\frac{f(z)}{(z-a)(z-b)}\,dz$
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 6.
---

::: {.problem}
Let $f ( z )$ be bounded and analytic in C. Let $a \neq b$ be any fixed complex numbers.
Show that the following limit exists

$$
\operatorname* { l i m } _ { R \to \infty } \int _ { \abs{ z } = R } { \frac { f ( z ) } { ( z - a ) ( z - b ) } } d z .
$$

Use this to show that $f ( z )$ must be a constant (Liouville’s theorem).
:::

::: {.solution}

Choose $M>0$ such that
$$
\abs{f(z)}\le M
$$
for all $z\in\CC$. For
$$
R>\max\{\abs{a},\abs{b}\},
$$
write
$$
I_R
\coloneqq
\int_{\abs{z}=R}
\frac{f(z)}{(z-a)(z-b)}\,dz.
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
\lim_{R\to\infty}I_R=0.
$$


::: pf-proof

On $\abs{z}=R$,
$$
\abs{z-a}\ge R-\abs{a},
\qquad
\abs{z-b}\ge R-\abs{b}.
$$
Therefore the $ML$ estimate gives
$$
\begin{aligned}
\abs{I_R}
&\le
2\pi R
\frac{M}
{(R-\abs{a})(R-\abs{b})}.
\end{aligned}
$$
The right-hand side tends to $0$ as $R\to\infty$, so the asserted limit exists and equals $0$.

:::

:::

::: {.pf-step #s1-2}

For every sufficiently large $R$,
$$
I_R
=
\frac{2\pi i}{a-b}
\left(f(a)-f(b)\right).
$$


::: pf-proof

The partial-fraction identity
$$
\frac1{(z-a)(z-b)}
=
\frac1{a-b}
\left(
\frac1{z-a}-\frac1{z-b}
\right)
$$
gives
$$
I_R
=
\frac1{a-b}
\left(
\int_{\abs{z}=R}\frac{f(z)}{z-a}\,dz
-
\int_{\abs{z}=R}\frac{f(z)}{z-b}\,dz
\right).
$$
Since both $a$ and $b$ lie inside the circle, Cauchy's integral formula yields
$$
\int_{\abs{z}=R}\frac{f(z)}{z-a}\,dz
=
2\pi i f(a)
$$
and
$$
\int_{\abs{z}=R}\frac{f(z)}{z-b}\,dz
=
2\pi i f(b).
$$
Substitution proves the formula.

:::

:::

::: {.pf-step #s1-3}

For every pair $a\ne b$ in $\CC$,
$$
f(a)=f(b).
$$


::: pf-proof

The expression in step [](#s1-2){.pf-ref} is independent of $R$, while step [](#s1-1){.pf-ref} says its limit as $R\to\infty$ is $0$. Hence
$$
\frac{2\pi i}{a-b}
\left(f(a)-f(b)\right)
=0.
$$
Since $a\ne b$, it follows that $f(a)=f(b)$.

:::

:::

::: {.pf-step #s1-4}

The function $f$ is constant on $\CC$.


::: pf-proof

The points $a\ne b$ were arbitrary. By step [](#s1-3){.pf-ref}, any two distinct points have the same image under $f$, so $f$ is constant. This is Liouville's theorem.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} establishes the requested limit, and step [](#s1-4){.pf-ref} gives the stated consequence.

:::

:::

:::
