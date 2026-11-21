---
schema: qual/card@1
id: E-SS5.EX-12
kind: problem
title: A zero-free entire function of finite order with zero-free derivatives is $e^{az+b}$
classification:
  areas:
  - complex-analysis
  topics:
  - Hadamard Factorization
  - Entire Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
Suppose $f$ is entire and never vanishes, and that none of the higher derivatives of $f$ ever vanish. Prove that if $f$ is also of finite order, then $f(z) = e^{az+b}$ for some constants $a$ and $b$.
:::

::: {.solution}

The argument is the card's own: Hadamard's theorem writes a finite-order never-vanishing entire function as $e^{P}$ with $P$ polynomial, and the nonvanishing of $f'$ bounds $\deg P$.

::: pf

::: {.pf-step #hadamard}

$f=e^{P}$ for a polynomial $P$.

::: pf-proof

$f$ is entire and never vanishes, so the Hadamard factorisation of $f$ has no primary factors at all: all its zeros would have to be absent, hence the genus-$0$ product is empty. A function of finite order with no zeros is therefore of the form $e^{P}$ with $P$ a polynomial, of degree at most the order of $f$; this is the standard consequence of Hadamard's theorem for functions of finite order.

:::

:::

::: {.pf-step #derivative}

$f'=P'e^{P}$, and $P'$ has no zeros.

::: pf-proof

Differentiating $f=e^{P}$ by the chain rule gives $f'=P'e^{P}$. The exponential never vanishes, so $f'(z_{0})=0$ exactly when $P'(z_{0})=0$; the hypothesis that the higher derivatives never vanish, applied to $f'$, says $f'$ has no zeros. Hence $P'$ has none.

:::

:::

::: {.pf-step #degree}

$\deg P\le1$.

::: pf-proof

If $\deg P\ge2$ then $P'$ is a nonconstant polynomial, and by the fundamental theorem of algebra a nonconstant complex polynomial has a zero; this contradicts step [](#derivative){.pf-ref}. So $\deg P\le1$, that is $P(z)=az+b$ for constants $a,b\in\CC$. Conversely any such $P$ gives $P'=a$ with no zeros when $a\ne0$.

:::

:::

::: {.pf-step #conclusion}

$f(z)=e^{az+b}$.

::: pf-proof

Steps [](#hadamard){.pf-ref} and [](#degree){.pf-ref} give
$$
\boxed{f(z)=e^{az+b}\qquad(a,b\in\CC).}
$$
If $a=0$ then $f\equiv e^{b}$ is constant and $f'\equiv0$, which violates the hypothesis that $f'$ never vanishes; so in fact $a\ne0$ under the stated hypotheses.

:::

:::

:::

:::
