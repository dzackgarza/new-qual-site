---
schema: qual/card@1
id: E-SS6.EX-15
kind: problem
title: $\zeta(s)=\frac1{\Gamma(s)}\int_0^\infty\frac{x^{s-1}}{e^x-1}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
  - Gamma Function
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    No text of Stein and Shakarchi is in this checkout, so the stored statement was not re-read
    against the printed book in this pass; it is the identity the exercise number in the collection
    index names (Chapter 6, Exercise 15), and the identity itself is checked below by the argument.
    No retained solution set for the book is held here either, so the argument is the card's own.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the prose solution into a Lamport proof and repaired one gap. The prose compared
    sum of integrals of the moduli but wrote the geometric series without recording that the
    integrand is nonnegative, which is what licenses Tonelli; the card now states the series
    identity as the geometric series with ratio e^{-x} < 1, records that the summands are nonnegative
    so the interchange is Tonelli's theorem rather than Fubini's, and keeps the finiteness of
    Gamma(sigma) zeta(sigma) as the check that makes the interchange legitimate. The substitution is
    made a step of its own, and the closing step divides by Gamma(s), which is nonzero and finite for
    Re(s) > 0.
---

::: {.exercise}
Prove that for $\Re(s) > 1$,
$$
\zeta(s) = \frac{1}{\Gamma(s)} \int_0^{\infty} \frac{x^{s-1}}{e^x - 1}\, dx.
$$
[Hint: Write $1/(e^x - 1) = \sum_{n=1}^{\infty} e^{-nx}$.]
:::

::: {.solution}
No retained solution set covers this exercise and no text of Stein and Shakarchi is in this checkout, so the argument is the card's own; it does not use a contour, only the geometric series the hint names. Write $s=\sigma+i\tau$ with $\sigma>1$, and $\Gamma(s)=\int_{0}^{\infty}e^{-u}u^{s-1}\,du$ for $\sigma>0$.

::: pf

::: {.pf-step #series}
For $x>0$, $\displaystyle\frac{1}{e^{x}-1}=\sum_{n=1}^{\infty}e^{-nx}$.

::: pf-proof
Since $e^{x}>1$ for $x>0$, the ratio $r=e^{-x}$ satisfies $0<r<1$, so the geometric series $\sum_{n\ge1}r^{n}$ converges with sum $r/(1-r)$. Multiplying numerator and denominator of $e^{-x}/(1-e^{-x})$ by $e^{x}$ gives $1/(e^{x}-1)$, so that is the sum.
:::

:::

::: {.pf-step #interchange}
$\displaystyle\int_{0}^{\infty}\frac{x^{s-1}}{e^{x}-1}\,dx=\sum_{n=1}^{\infty}\int_{0}^{\infty}e^{-nx}x^{s-1}\,dx$.

::: pf-proof
By step [](#series){.pf-ref} the integrand is the pointwise sum of the functions $x\mapsto e^{-nx}x^{\sigma-1}$ on $(0,\infty)$, since $\abs{x^{s-1}}=x^{\sigma-1}$, and each is nonnegative. For sums of nonnegative functions Tonelli's theorem gives $\int\sum_{n}=\sum_{n}\int$ whether or not the total is finite, and here it is finite: $\sum_{n}\int_{0}^{\infty}e^{-nx}x^{\sigma-1}dx=\Gamma(\sigma)\sum_{n}n^{-\sigma}=\Gamma(\sigma)\zeta(\sigma)$, finite for $\sigma>1$. So the interchange is legitimate and both sides are finite.
:::

:::

::: {.pf-step #term}
$\displaystyle\int_{0}^{\infty}e^{-nx}x^{s-1}\,dx=n^{-s}\Gamma(s)$ for every $n\ge1$.

::: pf-proof
Substitute $u=nx$, so that $x=u/n$, $dx=du/n$ and $x^{s-1}=(u/n)^{s-1}=u^{s-1}n^{1-s}$; the integral becomes $n^{1-s}n^{-1}\int_{0}^{\infty}e^{-u}u^{s-1}du=n^{-s}\Gamma(s)$. The substitution is legitimate because the integral converges absolutely, $\int_{0}^{\infty}e^{-u}u^{\sigma-1}du$ being finite for $\sigma>0$.
:::

:::

::: {.pf-step #sum}
$\displaystyle\int_{0}^{\infty}\frac{x^{s-1}}{e^{x}-1}\,dx=\Gamma(s)\zeta(s)$.

::: pf-proof
Insert step [](#term){.pf-ref} into step [](#interchange){.pf-ref}: the right side is $\sum_{n\ge1}n^{-s}\Gamma(s)=\Gamma(s)\sum_{n\ge1}n^{-s}$, since $\Gamma(s)$ does not depend on $n$, and $\sum_{n\ge1}n^{-s}=\zeta(s)$ converges absolutely for $\sigma>1$.
:::

:::

::: {.pf-step #answer}
$\displaystyle\zeta(s)=\boxed{\frac{1}{\Gamma(s)}\int_{0}^{\infty}\frac{x^{s-1}}{e^{x}-1}\,dx}$ for $\Re(s)>1$.

::: pf-proof
By step [](#sum){.pf-ref} the integral equals $\Gamma(s)\zeta(s)$. The function $\Gamma$ has no zeros and is finite on $\sigma>0$, in particular for $\sigma>1$, so dividing by $\Gamma(s)$ gives the displayed identity.
:::

:::

:::
:::
