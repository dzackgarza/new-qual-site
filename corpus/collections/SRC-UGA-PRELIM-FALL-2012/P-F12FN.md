---
schema: qual/card@1
id: P-F12FN
kind: problem
title: Pointwise and uniform convergence of $nx/(n+x)$ on $[0,\infty)$
classification:
  areas:
  - prelim
  topics:
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $f_n(x) = \frac{nx}{n+x}$ for $x \in [0, \infty)$ and $n \in \NN$.

(a) Find a function $f$ such that $\{f_n\}$ converges to $f$ pointwise on $[0, \infty)$.

(b) Is the convergence uniform on $[0, \infty)$?
Justify your answer.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/grad_prelim_Fall12.pdf` and no solutions sheet accompanies it, so the argument below is the card's own. Part (a) is a limit of sequences of real numbers for each fixed $x$; part (b) uses the criterion that uniform convergence is equivalent to the suprema $\sup_{x}\abs{f_{n}(x)-f(x)}$ tending to $0$.

Throughout, $f_{n}(x)\coloneqq\dfrac{nx}{n+x}$ for $x\geq0$ and $n\in\NN$.

::: pf

::: {.pf-step #limit-formula}
For fixed $x\geq0$ and $n\geq1$ one has $f_{n}(x)=\dfrac{x}{1+x/n}$.

::: pf-proof
Divide numerator and denominator of $\frac{nx}{n+x}$ by $n$, which is legitimate since $n\geq1$.
:::

:::

::: {.pf-step #pointwise}
(a) The sequence converges pointwise on $[0,\infty)$ to
$$
\boxed{f(x)=x.}
$$

:::: pf-proof

::: {.pf-step #at-zero}
$f_{n}(0)=0$ for every $n$, so $f_{n}(0)\to0=f(0)$.

::: pf-proof
Substituting $x=0$ in $f_{n}(x)=\frac{nx}{n+x}$ gives $0$ for every $n$.
:::

:::

::: {.pf-step #at-positive}
For $x>0$, $f_{n}(x)\to x$.

::: pf-proof
By step [](#limit-formula){.pf-ref}, $f_{n}(x)=\frac{x}{1+x/n}$; the sequence $x/n$ tends to $0$, so $1+x/n$ tends to $1$, a nonzero limit, and the quotient rule for limits of sequences gives $f_{n}(x)\to\frac{x}{1}=x$.
:::

:::

::: {.pf-step}
Every $x\geq0$ is covered, so the pointwise limit is $f(x)=x$.

::: pf-proof
The case $x=0$ is step [](#at-zero){.pf-ref} and the case $x>0$ is step [](#at-positive){.pf-ref}; a function is determined by its values, and the values found are those of $f(x)=x$.
:::

:::

::::

:::

::: {.pf-step #difference}
For every $x\geq0$ and $n\geq1$, $\abs{f_{n}(x)-f(x)}=\dfrac{x^{2}}{n+x}$.

::: pf-proof
$\frac{nx}{n+x}-x=\frac{nx-x(n+x)}{n+x}=\frac{-x^{2}}{n+x}$, and $n+x>0$ for $x\geq0$, so the modulus is $\frac{x^{2}}{n+x}$.
:::

:::

::: pf-step
(b) The convergence is not uniform on $[0,\infty)$.

::: pf-proof
By step [](#difference){.pf-ref}, evaluating at $x=n$ gives $\abs{f_{n}(n)-f(n)}=\frac{n^{2}}{2n}=\frac{n}{2}$. Hence $\sup_{x\geq0}\abs{f_{n}(x)-f(x)}\geq\frac{n}{2}$ for every $n$, and this supremum does not tend to $0$. Uniform convergence of $f_{n}$ to $f$ means that $\sup_{x\geq0}\abs{f_{n}(x)-f(x)}\to0$, so the convergence is not uniform; the pointwise limit is nevertheless $f(x)=x$ by step [](#pointwise){.pf-ref}, which answers (b) in the negative.
:::

:::

:::

:::
