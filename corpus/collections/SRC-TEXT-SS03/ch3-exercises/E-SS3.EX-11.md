---
schema: qual/card@1
id: E-SS3.EX-11
kind: problem
title: $\int_0^{2\pi}\log\abs{1-ae^{i\theta}}\,d\theta=0$ for $\abs a\le1$
classification:
  areas:
    - complex-analysis
  topics: [Logarithm, Mean Value Property, Definite Integrals]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Structured into Lamport steps from the card's own prose, and checked step by step:
      Log(1 - w) = -sum w^n/n converges uniformly on the closed disc of radius |a| because
      sum |a|^n/n converges, log|1 - a e^{i theta}| is the real part of that Log on the disc
      of centre 1 and radius |a|, and every exponential term integrates to zero. For |a| = 1
      the reduction to a = 1 is a translation of the periodic integrand, |1 - e^{i theta}|^2 =
      2 - 2 cos theta = 4 sin^2(theta/2) is correct, and the dominated-convergence step is now
      justified by an explicit majorant: for 1/2 <= r < 1 the squared modulus
      (1-r)^2 + 4r sin^2(theta/2) lies between 2 sin^2(theta/2) and 4, so
      |log|1 - r e^{i theta}|| is dominated by log 2 + |log(sqrt2 |sin(theta/2)|)|, which is
      integrable. The pointwise convergence fails only at theta = 0 and 2 pi, a null set. The
      statement is unchanged; the printed two-part wording (|a| < 1, then |a| <= 1) is
      represented by the two cases of the final step. No retained solution set covers the
      exercises of Stein-Shakarchi, so the card's solution states the argument is its own.
  - event: source-corrected
    by: claude
    date: 2026-11-19
    note: >-
      Notation repair after the corpus check reported raw TeX the page cannot show. The
      sentence naming the source of the logarithm's power series wrote `\S6`, a section sign
      written as a TeX command outside a math span, which the HTML writer drops; it now reads
      the character `§6`. Mathematics and wording unchanged.
---

::: {.exercise}
Show that if $\abs{a} < 1$, then
$$
\int_0^{2\pi} \log\abs{1 - ae^{i\theta}}\, d\theta = 0.
$$
Then, prove that the above result remains true if we assume only that $\abs{a} \leq 1$.
:::

::: {.solution}
For $\abs a<1$ the logarithm is expanded in a uniformly convergent power series on the circle, and every exponential term integrates to $0$; for $\abs a=1$ the integral is reduced by a rotation to $a=1$, and then obtained as the limit of the case $\abs a=r<1$ as $r\uparrow1$, the limit being taken under the integral sign by dominated convergence with an integrable majorant. The argument is this card's own: no retained solution set covers the exercises of Stein--Shakarchi.

::: pf

::: {.pf-step #series}
For $\abs a<1$ the series $\Log(1-w)=-\sum_{n\ge1}\frac{w^n}{n}$ converges uniformly on $\abs w\le\abs a$, and hence
$$
\int_0^{2\pi}\log\abs{1-ae^{i\theta}}\,\dd\theta=-\Re\sum_{n\ge1}\frac{a^n}{n}\int_0^{2\pi}e^{in\theta}\,\dd\theta .$$

::: pf-proof
Since $\abs a<1$, the point $1-ae^{i\theta}$ lies in the disc of centre $1$ and radius $\abs a<1$, on which $\Log$ is holomorphic with $\Log(1-w)=-\sum_{n\ge1}w^n/n$ (Chapter 3, §6, the power series of the principal logarithm); and $\log\abs{1-ae^{i\theta}}=\Re\Log(1-ae^{i\theta})$ there, because $\Log$ has real part $\log\abs\cdot$ wherever it is defined. The series converges uniformly on the closed disc $\abs w\le\abs a$ by the Weierstrass $M$-test with $M_n=\abs a^n/n$ and $\sum\abs a^n/n<\infty$. Uniform convergence permits termwise integration of the real parts, which gives the display.
:::

:::


::: {.pf-step #inner}
For $\abs a<1$, $\displaystyle\int_0^{2\pi}\log\abs{1-ae^{i\theta}}\,\dd\theta=0$.

::: pf-proof
For every integer $n\ge1$, $\int_0^{2\pi}e^{in\theta}\,\dd\theta=\frac{e^{2\pi in}-1}{in}=0$, since $e^{2\pi in}=1$. So every term of the series in step [](#series){.pf-ref} vanishes and the integral is $0$.
:::

:::


::: {.pf-step #boundary}
For $\abs a=1$, $\displaystyle\int_0^{2\pi}\log\abs{1-ae^{i\theta}}\,\dd\theta=\int_0^{2\pi}\log\bigl(2\abs{\sin(\theta/2)}\bigr)\dd\theta$, the value being independent of the argument of $a$.

::: pf-proof
Write $a=e^{i\varphi}$. Then $\abs{1-e^{i\varphi}e^{i\theta}}=\abs{1-e^{i(\theta+\varphi)}}$, and $\theta\mapsto\log\abs{1-e^{i(\theta+\varphi)}}$ is $2\pi$-periodic and integrable (see step [](#majorant){.pf-ref}), so its integral over any interval of length $2\pi$ equals its integral over $[0,2\pi]$; substituting $\theta'=\theta+\varphi$ gives the claimed independence of $\varphi$. Finally $\abs{1-e^{i\theta'}}^2=(1-\cos\theta')^2+\sin^2\theta'=2-2\cos\theta'=4\sin^2(\theta'/2)$, so $\abs{1-e^{i\theta'}}=2\abs{\sin(\theta'/2)}$.
:::

:::


::: {.pf-step #majorant}
For $\tfrac12\le r<1$ and every $\theta$, $\sqrt2\,\abs{\sin(\theta/2)}\le\abs{1-re^{i\theta}}\le2$, so the functions $\theta\mapsto\log\abs{1-re^{i\theta}}$ are dominated on $[0,2\pi]$ by the integrable function $\log2+\abs{\log\bigl(\sqrt2\,\abs{\sin(\theta/2)}\bigr)}$, independently of $r$.

::: pf-proof
$\abs{1-re^{i\theta}}^2=(1-r)^2+4r\sin^2(\theta/2)$. The lower bound uses $(1-r)^2\ge0$ and $4r\ge2$ for $r\ge\tfrac12$, giving $\abs{1-re^{i\theta}}^2\ge2\sin^2(\theta/2)$; the upper bound uses $(1-r)^2+4r\sin^2(\theta/2)\le(1-r)^2+4r=(1+r)^2\le4$. Hence $\abs{1-re^{i\theta}}$ lies in $[\sqrt2\abs{\sin(\theta/2)},2]$, and for $x$ in a closed interval of positive numbers, $\abs{\log x}\le\max(\abs{\log(\text{lower endpoint})},\abs{\log(\text{upper endpoint})})$. The majorant is integrable because $\log\abs{\sin(\theta/2)}$ is: near $\theta=0$ it is $\log(\theta/2)+O(\theta^2)$, whose integral converges, and it is bounded on the rest of $[0,2\pi]$ away from $\theta=2\pi$.
:::

:::


::: {.pf-step #limit}
$\displaystyle\int_0^{2\pi}\log\abs{1-e^{i\theta}}\,\dd\theta=\lim_{r\uparrow1}\int_0^{2\pi}\log\abs{1-re^{i\theta}}\,\dd\theta=0$.

::: pf-proof
For each $\theta\notin\{0,2\pi\}$ one has $\abs{1-re^{i\theta}}\to\abs{1-e^{i\theta}}>0$ as $r\uparrow1$, hence $\log\abs{1-re^{i\theta}}\to\log\abs{1-e^{i\theta}}$; the exceptional set $\{0,2\pi\}$ is null, so the convergence is almost everywhere. Step [](#majorant){.pf-ref} supplies an integrable majorant independent of $r$, so dominated convergence gives the first equality, and the limit of the integrals is $0$ by step [](#inner){.pf-ref}, whose hypothesis $\abs a=r<1$ holds along the sequence.
:::

:::


::: {.pf-step #conclusion}
For every $\abs a\le1$, $\displaystyle\int_0^{2\pi}\log\abs{1-ae^{i\theta}}\,\dd\theta=0$.

::: pf-proof
If $\abs a<1$ this is step [](#inner){.pf-ref}; if $\abs a=1$ it is step [](#boundary){.pf-ref} combined with step [](#limit){.pf-ref}. These two cases exhaust $\abs a\le1$.
:::

:::

:::
:::
