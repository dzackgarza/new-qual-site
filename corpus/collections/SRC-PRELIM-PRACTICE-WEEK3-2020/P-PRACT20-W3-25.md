---
schema: qual/card@1
id: P-PRACT20-W3-25
kind: problem
title: The integrals $\int_0^{\pi/2}(a\cos^2x+b\sin^2x)^{-n}\,dx$ by differentiating in parameters
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Differentiation Under the Integral
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 7-8 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem states the same family I_n and asks for the same identity and the same two evaluations, which the printed solution gives
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's differentiation under the integral sign, its u = tan x evaluation of I_1 and its use of the identity to get I_2 are transcribed, with the domination hypothesis for Leibniz stated.
---

::: {.problem}
For $a, b > 0$ and $n \in \NN$, define
$$
I_{n}(a, b) = \int_{0}^{\pi/2} \frac{dx}{(a \cos^{2}(x) + b \sin^{2}(x))^{n}}.
$$
(a) Show that
$$
\frac{\partial I_{n}}{\partial a} + \frac{\partial I_{n}}{\partial b} + n I_{n+1} = 0.
$$

(b) Evaluate $I_{1}(a, b)$ explicitly, and use (a) to evaluate $I_{2}(a, b)$.
:::

::: {.solution}

For $a,b>0$ and $n\ge1$ let
$I_n(a,b)=\int_0^{\pi/2}\big(a\cos^2x+b\sin^2x\big)^{-n}dx$.

::: pf

::: {.pf-step #identity}

$\displaystyle\frac{\partial I_n}{\partial a}+\frac{\partial I_n}{\partial
b}+nI_{n+1}=0$.

::: pf-proof

The integrand is differentiable in $(a,b)$ with $\partial_a$ equal to
$-n\cos^2x\,(a\cos^2x+b\sin^2x)^{-n-1}$ and $\partial_b$ to
$-n\sin^2x\,(a\cos^2x+b\sin^2x)^{-n-1}$, both bounded on the compact parameter
range $\{a,b\ge\delta\}$ by a constant times $(\delta)^{-n-1}$, so Leibniz's
rule applies and the derivatives may be taken under the integral. Adding them
gives
$-n\int_0^{\pi/2}(\cos^2x+\sin^2x)(a\cos^2x+b\sin^2x)^{-n-1}dx=-nI_{n+1}$,
since $\cos^2+\sin^2=1$.

:::

:::

::: {.pf-step #first}

$\displaystyle I_1(a,b)=\frac{\pi}{2\sqrt{ab}}$.

::: pf-proof

Divide numerator and denominator by $\cos^2x$:
$I_1=\int_0^{\pi/2}\frac{\sec^2x}{a+b\tan^2x}dx$. With $u=\tan x$,
$du=\sec^2x\,dx$ and the limits $0,\infty$ give
$I_1=\int_0^\infty\frac{du}{a+bu^2}=\frac1a\int_0^\infty\frac{du}{1+\frac ba
u^2}=\frac1a\sqrt{\frac ab}\Big[\arctan\Big(u\sqrt{\frac
ba}\Big)\Big]_0^\infty=\frac{1}{\sqrt{ab}}\cdot\frac\pi2$, using
$\int\frac{du}{1+c^2u^2}=\frac1c\arctan(cu)$ with $c=\sqrt{b/a}$.

:::

:::

::: {.pf-step #second}

$\boxed{I_2(a,b)=\frac{\pi}{4\sqrt{ab}}\Big(\frac1a+\frac1b\Big)}$.

::: pf-proof

With $n=1$ step [](#identity){.pf-ref} gives
$I_2=-\partial_aI_1-\partial_bI_1$. From $I_1=\frac\pi2(ab)^{-1/2}$,
$\partial_aI_1=-\frac{\pi}{4}a^{-3/2}b^{-1/2}$ and
$\partial_bI_1=-\frac{\pi}{4}a^{-1/2}b^{-3/2}$, so
$I_2=\frac{\pi}{4}\big(a^{-3/2}b^{-1/2}+a^{-1/2}b^{-3/2}\big)=\frac{\pi}{4\sqrt{ab}}\big(\frac1a+\frac1b\big)$,
which is the printed answer.

:::

:::

:::


:::
