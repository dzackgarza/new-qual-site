---
schema: qual/card@1
id: P-CAF09A
kind: problem
title: 'Principal value of $\log\qty{e^{3+7i}}$'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Find the principal value of $\log(e^{3+7i})$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own computation follows, with the modulus, the argument reduction and the conclusion separated.

The principal logarithm is $\operatorname{Log}w=\log\abs{w}+i\operatorname{Arg}w$, where $\operatorname{Arg}w\in(-\pi,\pi]$ is the argument of $w$.

::: pf

::: {.pf-step #modulus}
$\abs{e^{3+7i}}=e^{3}$.

::: pf-proof
$e^{3+7i}=e^{3}e^{7i}$ and $\abs{e^{7i}}=1$, so $\abs{e^{3+7i}}=e^{3}\cdot1=e^{3}$; hence $\log\abs{e^{3+7i}}=3$.
:::

:::

::: {.pf-step #argument}
$\operatorname{Arg}\big(e^{3+7i}\big)=7-2\pi$.

::: pf-proof
$e^{3+7i}=e^{3}e^{7i}$ has the same argument as $e^{7i}$, whose arguments are the numbers $7-2\pi k$, $k\in\ZZ$. Since $\pi<7<3\pi$ we get $-1<\tfrac{7}{\pi}-2<1$, that is $7-2\pi\in(-\pi,\pi)$; so the number of the form $7-2\pi k$ lying in $(-\pi,\pi]$ is $7-2\pi$, and it is the principal argument.
:::

:::

::: {.pf-qed}
$\operatorname{Log}\big(e^{3+7i}\big)=\log\abs{e^{3+7i}}+i\operatorname{Arg}\big(e^{3+7i}\big)=3+i(7-2\pi)$, the modulus $3$ by step [](#modulus){.pf-ref} and the argument $7-2\pi$ by step [](#argument){.pf-ref}, and $7-2\pi\approx0.7168$.
:::

:::

:::
