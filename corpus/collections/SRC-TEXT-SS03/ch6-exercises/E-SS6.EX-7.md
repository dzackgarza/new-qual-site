---
schema: qual/card@1
id: E-SS6.EX-7
kind: problem
title: The Beta function and $B(\alpha,\beta)=\frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose argument into numbered steps without changing the mathematics, and
    re-checked each step against the definitions and theorems it invokes. What was not checked: no
    copy of Stein and Shakarchi and no solution set for it is retained in tmp/sources (the
    collection provenance is the Google Books ISBN link), so the printed statement and page were
    not re-read; the exercise number is the one the collection index records. No published
    solution is transcribed; the argument remains the card's own, as its solution section says.
---

::: {.exercise}
The Beta function is defined for $\Re(\alpha) > 0$ and $\Re(\beta) > 0$ by
$$
B(\alpha, \beta) = \int_0^1 (1 - t)^{\alpha - 1} t^{\beta - 1}\, dt.
$$

(a) Prove that $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}$.

(b) Show that $B(\alpha, \beta) = \int_0^{\infty} \frac{u^{\alpha - 1}}{(1 + u)^{\alpha + \beta}}\, du$.

[Hint: For part (a), note that
$$
\Gamma(\alpha)\Gamma(\beta) = \int_0^{\infty} \int_0^{\infty} t^{\alpha - 1} s^{\beta - 1} e^{-t-s}\, dt\, ds,
$$
and make the change of variables $s = ur$, $t = u(1 - r)$.]
:::

::: {.solution}

The argument is the card's own: the book is retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, and no published solution set of this exercise is retained, so nothing below is transcribed. The statement is the exercise the collection index records as Stein and Shakarchi, *Complex Analysis* (2003), Ch. 6, Exercise 7. Here $B(\alpha,\beta)=\int_{0}^{1}(1-t)^{\alpha-1}t^{\beta-1}\,dt$ and $\Gamma(\alpha)=\int_{0}^{\infty}t^{\alpha-1}e^{-t}\,dt$ for $\Re\alpha,\Re\beta>0$.

::: pf

::: {.pf-step #product}

$\Gamma(\alpha)\Gamma(\beta)=\int_{0}^{\infty}\int_{0}^{\infty}t^{\alpha-1}s^{\beta-1}e^{-t-s}\,dt\,ds$.

::: pf-proof

The double integral is a product of two absolutely convergent integrals, by Fubini and the integrability of $t^{\Re\alpha-1}e^{-t}$ on $(0,\infty)$.

:::

:::

::: {.pf-step #a}

(a) With $t=u(1-r)$, $s=ur$, the double integral equals $\Gamma(\alpha+\beta)B(\alpha,\beta)$.

::: pf-proof

The map $(u,r)\mapsto(t,s)=(u(1-r),ur)$ takes $(0,\infty)\times(0,1)$ bijectively onto $(0,\infty)^{2}$, with Jacobian determinant $u$. Substituting, $t^{\alpha-1}s^{\beta-1}e^{-t-s}\,dt\,ds=u^{\alpha+\beta-1}e^{-u}(1-r)^{\alpha-1}r^{\beta-1}\,du\,dr$, and the double integral factors as $\int_{0}^{\infty}u^{\alpha+\beta-1}e^{-u}\,du\cdot\int_{0}^{1}(1-r)^{\alpha-1}r^{\beta-1}\,dr=\Gamma(\alpha+\beta)B(\alpha,\beta)$.

:::

:::

::: {.pf-step #a2}

(a) $B(\alpha,\beta)=\Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha+\beta)$.

::: pf-proof

Divide step [](#a){.pf-ref} by $\Gamma(\alpha+\beta)$, which is nonzero for $\Re(\alpha+\beta)>0$.

:::

:::

::: {.pf-step #b}

(b) $B(\alpha,\beta)=\int_{0}^{\infty}\frac{u^{\alpha-1}}{(1+u)^{\alpha+\beta}}\,du$.

::: pf-proof

Substitute $u=\frac{1-t}{t}$, so $t=\frac{1}{1+u}$, $1-t=\frac{u}{1+u}$ and $dt=-\frac{du}{(1+u)^{2}}$. Then $(1-t)^{\alpha-1}t^{\beta-1}dt=\frac{u^{\alpha-1}}{(1+u)^{\alpha+\beta}}\,du$ up to the sign, and the limits $t:0\to1$ become $u:\infty\to0$, so the two sign changes cancel.

:::

:::

:::

:::
