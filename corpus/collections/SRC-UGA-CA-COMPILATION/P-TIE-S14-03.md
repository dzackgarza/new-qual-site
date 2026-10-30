---
schema: qual/card@1
id: P-TIE-S14-03
kind: problem
title: $\int_{\abs{z}=r}\frac{dz}{(z-a)(z-b)}$ for $\abs{a}<r<\abs{b}$ without Cauchy's theorem
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2014, question 3.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Separated part 3 of Spring 2014 question 1 from questions 2 and 3, which had been merged into this card, against page 7 of Questions_from_Tie.pdf; questions 2 and 3 are carried by their existing cards.
---

::: {.problem}
Solve the problem without using the Cauchy theorem.

Show that if $\abs{a} < r < \abs{b}$, then
$$
\int_\gamma \frac{dz}{(z-a)(z-b)}\,dz = \frac{2\pi i}{a-b}.
$$
Here $\gamma$ denotes the circle centered at the origin, of radius $r$, with the positive orientation.
:::

::: {.remark}
The source prints $dz$ twice in the integral.
:::

::: {.solution}

Use the intended integral with a single differential,
$$
I
\coloneqq
\int_\gamma
\frac{1}{(z-a)(z-b)}\,dz.
$$

::: pf

::: {.pf-step #s1-1}

One has the partial-fraction identity
$$
\frac{1}{(z-a)(z-b)}
=
\frac1{a-b}
\left(
\frac1{z-a}-\frac1{z-b}
\right).
$$


::: pf-proof

The right-hand side equals
$$
\frac1{a-b}
\frac{(z-b)-(z-a)}{(z-a)(z-b)}
=
\frac1{(z-a)(z-b)}.
$$

:::

:::

::: {.pf-step #s1-2}

On $\abs{z}=r$,
$$
\frac1{z-a}
=
\sum_{k=0}^{\infty}a^kz^{-k-1},
$$
and the series converges uniformly on $\gamma$.


::: pf-proof

Since $\abs{a}<r=\abs{z}$,
$$
\abs{\frac{a}{z}}<1.
$$
Therefore
$$
\frac1{z-a}
=
\frac1z\frac1{1-a/z}
=
\frac1z
\sum_{k=0}^{\infty}
\left(\frac{a}{z}\right)^k
=
\sum_{k=0}^{\infty}a^kz^{-k-1}.
$$
The ratio has constant modulus $\abs{a}/r<1$ on the circle, so the convergence is uniform.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\int_\gamma\frac{dz}{z-a}
=
2\pi i.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, uniform convergence permits termwise integration:
$$
\int_\gamma\frac{dz}{z-a}
=
\sum_{k=0}^{\infty}
a^k
\int_\gamma z^{-k-1}\,dz.
$$
Parametrizing $\gamma$ by $z=re^{it}$ gives
$$
\int_\gamma z^m\,dz
=
\begin{cases}
2\pi i,&m=-1,\\
0,&m\ne-1,
\end{cases}
$$
for every integer $m$. Hence only the term $k=0$ survives, giving $2\pi i$.

:::

:::

::: {.pf-step #s1-4}

On $\abs{z}=r$,
$$
\frac1{z-b}
=
-\sum_{k=0}^{\infty}\frac{z^k}{b^{k+1}},
$$
and the series converges uniformly on $\gamma$.


::: pf-proof

Since $r<\abs{b}$,
$$
\abs{\frac{z}{b}}<1
$$
on $\gamma$. Thus
$$
\frac1{z-b}
=
-\frac1b
\frac1{1-z/b}
=
-\sum_{k=0}^{\infty}\frac{z^k}{b^{k+1}}.
$$
The ratio has constant modulus $r/\abs{b}<1$, so the convergence is uniform.

:::

:::

::: {.pf-step #s1-5}

One has
$$
\int_\gamma\frac{dz}{z-b}
=0.
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, integrate term by term:
$$
\int_\gamma\frac{dz}{z-b}
=
-\sum_{k=0}^{\infty}
\frac1{b^{k+1}}
\int_\gamma z^k\,dz.
$$
For every $k\ge0$, direct parametrization of the circle gives
$$
\int_\gamma z^k\,dz=0.
$$
Therefore the whole sum is $0$.

:::

:::

::: pf-step

Therefore
$$
\boxed{
I
=
\frac{2\pi i}{a-b}.
}
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
I
=
\frac1{a-b}
\left(
\int_\gamma\frac{dz}{z-a}
-
\int_\gamma\frac{dz}{z-b}
\right).
$$
Substituting steps [](#s1-3){.pf-ref} and [](#s1-5){.pf-ref} gives
$$
I
=
\frac1{a-b}(2\pi i-0)
=
\frac{2\pi i}{a-b}.
$$

:::

:::

:::

:::
