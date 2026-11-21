---
schema: qual/card@1
id: P-F06DN
kind: problem
title: Inductive formula for the derivatives of $xe^{2x}$
classification:
  areas:
  - prelim
  topics:
  - Differentiation
  - Induction
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $f(x) = xe^{2x}$.
Writing $f^{(n)}(x)$ for the $n$th derivative of $f(x)$, prove by induction that $f^{(n)}(x) = 2^n xe^{2x} + n 2^{n-1}e^{2x}$ for all $n \geq 0$.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/grad_prelim_Fall06.pdf` and no solutions sheet accompanies it, so the induction below is the card's own. The statement asks for a proof by induction and the proof is one; the only calculus used is the product rule and $(\mathrm{e}^{2x})'=2\mathrm{e}^{2x}$.

Throughout, $f(x)\coloneqq x\mathrm{e}^{2x}$, $f^{(n)}$ is the $n$-th derivative, and $P(n)$ denotes the assertion
$$
f^{(n)}(x)=2^{n}x\mathrm{e}^{2x}+n\,2^{n-1}\mathrm{e}^{2x}\qquad\text{for all }x.
$$

::: pf

::: {.pf-step #basic-derivative}
$\big(\mathrm{e}^{2x}\big)'=2\mathrm{e}^{2x}$ and $\big(x\mathrm{e}^{2x}\big)'=\mathrm{e}^{2x}+2x\mathrm{e}^{2x}$.

::: pf-proof
The first is the chain rule with inner function $2x$; the second is the product rule applied to $x$ and $\mathrm{e}^{2x}$, using $x'=1$ and the first identity.
:::

:::

::: {.pf-step #base}
$P(0)$ holds.

::: pf-proof
For $n=0$ the right-hand side of $P(0)$ is $2^{0}x\mathrm{e}^{2x}+0\cdot2^{-1}\mathrm{e}^{2x}=x\mathrm{e}^{2x}$, the second term vanishing because its coefficient is $0$, and this is $f^{(0)}=f$.
:::

:::

::: {.pf-step #step}
For every $n\geq0$, $P(n)$ implies $P(n+1)$.

:::: pf-proof

::: {.pf-step #differentiate}
Differentiating the right-hand side of $P(n)$ gives
$$
2^{n+1}x\mathrm{e}^{2x}+(n+1)2^{n}\mathrm{e}^{2x}.
$$

::: pf-proof
By step [](#basic-derivative){.pf-ref}, the sum rule and the constant multiple rule,
$$
\frac{d}{dx}\Big(2^{n}x\mathrm{e}^{2x}\Big)=2^{n}\big(\mathrm{e}^{2x}+2x\mathrm{e}^{2x}\big)=2^{n}\mathrm{e}^{2x}+2^{n+1}x\mathrm{e}^{2x},
$$
and, since $n2^{n-1}$ is a constant,
$$
\frac{d}{dx}\Big(n2^{n-1}\mathrm{e}^{2x}\Big)=n2^{n-1}\cdot2\mathrm{e}^{2x}=n2^{n}\mathrm{e}^{2x}.
$$
Adding the two, the coefficient of $\mathrm{e}^{2x}$ is $2^{n}+n2^{n}=(n+1)2^{n}$ and the coefficient of $x\mathrm{e}^{2x}$ is $2^{n+1}$.
:::

:::

::: {.pf-step}
The result is the formula $P(n+1)$.

::: pf-proof
The formula claimed for $n+1$ reads $2^{n+1}x\mathrm{e}^{2x}+(n+1)2^{(n+1)-1}\mathrm{e}^{2x}$, and $(n+1)-1=n$, so it is the displayed expression of step [](#differentiate){.pf-ref}; hence $f^{(n+1)}$ has it, since $f^{(n+1)}$ is the derivative of $f^{(n)}$ and $P(n)$ gives the value of $f^{(n)}$.
:::

:::

::::

:::

::: pf-step
Therefore $f^{(n)}(x)=2^{n}x\mathrm{e}^{2x}+n2^{n-1}\mathrm{e}^{2x}$ for every $n\geq0$.

::: pf-proof
$P(0)$ holds by step [](#base){.pf-ref}, and step [](#step){.pf-ref} carries $P(n)$ to $P(n+1)$ for every $n\geq0$; by the principle of induction $P(n)$ holds for all nonnegative integers $n$.
:::

:::

:::

:::
