---
schema: qual/card@1
id: P-3EAU2
kind: problem
title: Possible holomorphic interpolations of sequences accumulating at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Zeros
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Suppose $f$ is analytic on $\DD^\circ$.
Determine with proof which of the following are possible:

(a) $f\qty{1\over n} = (-1)^n$ for each $n>1$.

(b) $f\qty{1\over n} = e^{-n}$ for each even integer $n>1$ while $f\qty{1\over n} = 0$ for each odd integer $n>1$.

(c) $f\qty{1\over n^2} = {1\over n}$ for each integer $n>1$.

(d) $f\qty{1\over n} = {n-2 \over n-1}$ for each integer $n>1$.

:::

::: {.solution}

Each sequence $1/n$, $1/n^2$ tends to $0\in\DD^\circ$, and $f$ is continuous at $0$.

::: pf

::: pf-step
(a) is $\boxed{\text{not possible}}$.

::: pf-proof
Continuity at $0$ would give $f(0)=\lim_n f(1/n)=\lim_n(-1)^n$, which does not exist.
:::

:::

::: pf-step
(b) is $\boxed{\text{not possible}}$.

::: pf-proof
The zeros $1/n$, $n$ odd, accumulate at $0\in\DD^\circ$, so the identity theorem gives $f\equiv0$ on $\DD^\circ$.
This contradicts $f(1/n)=e^{-n}\neq0$ for even $n$.
:::

:::

::: pf-step
(c) is $\boxed{\text{not possible}}$.

::: pf-proof
Continuity gives $f(0)=\lim_n 1/n=0$, and $f\not\equiv0$ because $f(1/4)=1/2$.
So $f(z)=z^mg(z)$ near $0$ with $m\geq1$, $g$ holomorphic and $g(0)\neq0$.
Then $\frac1n=f(1/n^2)=n^{-2m}g(1/n^2)$, so $\abs{g(1/n^2)}=n^{2m-1}\to\infty$, while $g(1/n^2)\to g(0)$.
:::

:::

::: pf-step
(d) is $\boxed{\text{possible}}$, by $f(z)=\dfrac{1-2z}{1-z}$.

::: pf-proof
This $f$ is holomorphic on $\DD^\circ$, since its only pole is $z=1$, and $f(1/n)=\dfrac{1-2/n}{1-1/n}=\dfrac{n-2}{n-1}$.
:::

:::

:::

:::
