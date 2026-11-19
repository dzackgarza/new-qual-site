---
schema: qual/card@1
id: E-SS3.EX-10
kind: problem
title: $\int_0^\infty\frac{\log x}{x^2+a^2}\,dx=\frac{\pi}{2a}\log a$
classification:
  areas:
    - complex-analysis
  topics: [Contour Integration, Logarithm, Improper Integrals]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-written
    by: claude
    date: 2026-11-19
    note: >-
      Lamport structure over the prose that was already there. The substitution and the
      splitting of log(at) are separate steps, the two standard integrals are each computed
      (int dt/(1+t^2) = pi/2 and int log t/(1+t^2) = 0, the latter by the substitution t -> 1/t
      which pairs the intervals (0,1) and (1,infinity)), and the conclusion assembles them. Not
      checked: the book's own text of the exercise, since no copy of Stein and Shakarchi is
      retained in this checkout; the statement is as transcribed on the card. No retained
      solution set covers the exercise (the collection's provenance is a Google Books record),
      so the argument is the card's own. No statement repair.
---

::: {.exercise}
Show that if $a > 0$, then
$$
\int_{0}^{\infty} \frac{\log x}{x^{2}+a^{2}}\,dx = \frac{\pi}{2a}\log a.
$$

[Hint: Use the contour in Figure 10.]
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. Let $a>0$ and
$$
I(a)=\int_0^{\infty}\frac{\log x}{x^2+a^2}\,dx,
$$
an absolutely convergent integral since $\abs{\log x}\le x^{-1/2}$ near $0$ and $\abs{\log x}\le x^{1/2}$ at infinity, while $x^2+a^2\ge a^2$.

::: pf

::: {.pf-step #substitute}
$I(a)=\dfrac1a\displaystyle\int_0^{\infty}\frac{\log a+\log t}{1+t^2}\,dt$.

::: pf-proof
Put $x=at$ with $t$ running from $0$ to $\infty$, so $dx=a\,dt$ and $x^2+a^2=a^2(t^2+1)$. Then
$$
I(a)=\int_0^\infty\frac{\log(at)}{a^2(t^2+1)}\,a\,dt=\frac1a\int_0^\infty\frac{\log a+\log t}{1+t^2}\,dt,
$$
using $\log(at)=\log a+\log t$ for $a,t>0$, and linearity of the integral.
:::

:::

::: {.pf-step #arctan}
$\displaystyle\int_0^{\infty}\frac{dt}{1+t^2}=\frac{\pi}{2}$.

::: pf-proof
$\arctan$ is an antiderivative of $1/(1+t^2)$ on $\RR$, so the integral is $\lim_{t\to\infty}\arctan t-\arctan0=\pi/2-0$.
:::

:::

::: {.pf-step #logzero}
$\displaystyle\int_0^{\infty}\frac{\log t}{1+t^2}\,dt=0$.

::: pf-proof
Split at $1$ and substitute $t=1/u$ in the first piece, so that $dt=-du/u^2$ and $t:0\to1$ corresponds to $u:\infty\to1$:
$$
\int_0^1\frac{\log t}{1+t^2}\,dt=\int_\infty^1\frac{-\log u}{1+u^{-2}}\Bigl(-\frac{du}{u^2}\Bigr)=\int_\infty^1\frac{\log u}{1+u^2}\,du=-\int_1^\infty\frac{\log u}{1+u^2}\,du,
$$
using $\log(1/u)=-\log u$ and $\frac{u^2}{1+u^2}\cdot\frac{1}{u^2}=\frac{1}{1+u^2}$. The two pieces therefore cancel, so the whole integral is $0$.
:::

:::

::: {.pf-step}
$I(a)=\dfrac{\pi}{2a}\log a$.

::: pf-proof
By steps [](#substitute){.pf-ref}, [](#arctan){.pf-ref} and [](#logzero){.pf-ref},
$$
I(a)=\frac1a\Bigl(\log a\int_0^\infty\frac{dt}{1+t^2}+\int_0^\infty\frac{\log t}{1+t^2}\,dt\Bigr)=\frac1a\Bigl(\log a\cdot\frac{\pi}{2}+0\Bigr)=\frac{\pi}{2a}\log a,
$$
which is the identity asserted, for every $a>0$.
:::

:::

:::

:::

::: {.remark title="Variations"}
At $a=1$ the main statement gives $\int_0^\infty\frac{\log x}{1+x^2}\,dx=\frac{\pi}{2}\log 1=0$.
:::
