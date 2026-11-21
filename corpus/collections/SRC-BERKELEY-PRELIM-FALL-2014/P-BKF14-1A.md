---
schema: qual/card@1
id: P-BKF14-1A
kind: problem
title: Broomstick change-making generating function and asymptotics
classification:
  areas:
  - prelim
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1A and its solution in the vendored UC Berkeley Fall 2014 solution packet; repaired the malformed limit transcription in the prior card.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The pole-order argument isolates the unique cubic pole at z=1; nontrivial 29th roots contribute only O(n), so they do not affect the n^2 limit.
---

::: {.problem}
Let $a(n)$ be the number of ways that Harry Potter can buy a new broomstick valued at $n$ knuts using bronze knuts, silver sickles worth $29$ knuts, and gold galleons worth $17$ sickles.
Find
$$
\sum_{n\ge 0} a(n)z^n
$$
and
$$
\lim_{n\to\infty}\frac{a(n)}{n^2}.
$$
:::

::: {.solution}

The argument is the card's own: the count is the coefficient of a product of three geometric series, and the asymptotics of $a(n)$ are read off the triple pole at $z=1$.

::: pf

::: {.pf-step #generating}

$\displaystyle\sum_{n\ge0}a(n)z^{n}=\frac{1}{(1-z)(1-z^{29})(1-z^{493})}$.

::: pf-proof

A purchase is a triple $(r,s,g)$ of nonnegative integers with $r+29s+(17\cdot29)g=n$, since a knut is worth $1$, a sickle $29$ and a galleon $17\cdot29=493$ knuts. For fixed $(r,s,g)$ the value $r+29s+493g$ determines the exponent, so summing $z^{r}z^{29s}z^{493g}$ over all triples collects $a(n)z^{n}$:
$$
\sum_{n\ge0}a(n)z^{n}=\Bigl(\sum_{r\ge0}z^{r}\Bigr)\Bigl(\sum_{s\ge0}z^{29s}\Bigr)\Bigl(\sum_{g\ge0}z^{493g}\Bigr)=\frac{1}{(1-z)(1-z^{29})(1-z^{493})},
$$
each geometric series converging for $\abs{z}<1$.

:::

:::

::: {.pf-step #poleat1}

Near $z=1$ the generating function is $\dfrac{1}{17\cdot29^{2}}\dfrac{1}{(1-z)^{3}}+O\Bigl(\dfrac{1}{(1-z)^{2}}\Bigr)$.

::: pf-proof

For an integer $m\ge1$, $1-z^{m}=m(1-z)+O\bigl((1-z)^{2}\bigr)$ as $z\to1$, since $1-z^{m}=(1-z)(1+z+\cdots+z^{m-1})$ and the second factor tends to $m$. With $m=29$ and $m=493$,
$$
\frac{1}{(1-z)(1-z^{29})(1-z^{493})}=\frac{1}{(1-z)\cdot29(1-z)\cdot493(1-z)}\bigl(1+O(1-z)\bigr),
$$
and $29\cdot493=17\cdot29^{2}$, so the leading term is $\frac{1}{17\cdot29^{2}}(1-z)^{-3}$ and the correction is one order lower.

:::

:::

::: {.pf-step #coefficient}

$a(n)=\dfrac{n^{2}}{2\cdot17\cdot29^{2}}+O(n)$.

::: pf-proof

The coefficient of $(1-z)^{-3}$ is $\binom{n+2}{2}=\frac{(n+2)(n+1)}{2}=\frac{n^{2}}{2}+O(n)$. Every other pole of the generating function is a root of $z^{29}=1$ or $z^{493}=1$ different from $1$, and if $\zeta^{29}=1$, $\zeta\ne1$, then $\zeta^{493}=(\zeta^{29})^{17}=1$, so at such $\zeta$ exactly the two factors $1-z^{29}$ and $1-z^{493}$ vanish and the pole has order $2$; a pole of order $2$ contributes $O(n)$ to the coefficient, by the same expansion applied to $\frac{c}{(1-z/\zeta)^{2}}$. Adding the contributions gives the displayed asymptotic.

:::

:::

::: {.pf-step #limit}

$\displaystyle\lim_{n\to\infty}\frac{a(n)}{n^{2}}=\frac{1}{28594}$.

::: pf-proof

Dividing the asymptotic of step [](#coefficient){.pf-ref} by $n^{2}$ gives $\frac{1}{2\cdot17\cdot29^{2}}+O(1/n)$, and $2\cdot17\cdot29^{2}=2\cdot17\cdot841=28594$. Hence
$$
\boxed{\sum_{n\ge0}a(n)z^{n}=\frac{1}{(1-z)(1-z^{29})(1-z^{493})},\qquad \lim_{n\to\infty}\frac{a(n)}{n^{2}}=\frac{1}{28594}.}
$$

:::

:::

:::

:::
