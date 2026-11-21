---
schema: qual/card@1
id: P-CAF24B
kind: problem
title: Entire function with a rational Taylor coefficient at every real point is a polynomial
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Entire Functions
relations: []
review: draft
---

::: {.problem}
Let $f : \CC \to \CC$ be an entire function.
Assume that for any $a \in \RR$, at least one coefficient in the Taylor expansion of $f$ around $a$ is a rational number.
Prove that $f$ is a polynomial.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/FA24_220_Complex_Analysis_Qual.pdf` and no solutions sheet accompanies it, so the argument below is the card's own. It is a Baire category argument on $\RR$ followed by the identity theorem; the earlier version of the card used both without saying why $\RR$ is a Baire space or why vanishing on an interval triggers the identity theorem.

Throughout, $f\colon\CC\to\CC$ is entire, and for $n\geq0$ and $q\in\QQ$
$$
E_{n,q}\coloneqq\Big\{a\in\RR\ \Big|\ \frac{f^{(n)}(a)}{n!}=q\Big\}.
$$

::: pf

::: {.pf-step #covering}
Each $E_{n,q}$ is closed in $\RR$, and $\RR=\bigcup_{n\geq0}\bigcup_{q\in\QQ}E_{n,q}$.

::: pf-proof
$f^{(n)}$ is entire, hence continuous on $\RR$, and $E_{n,q}=(f^{(n)})^{-1}(\theset{n!q})$ is the preimage of a closed subset of $\CC$ intersected with $\RR$, so it is closed in $\RR$ (and in $\CC$). For the covering, let $a\in\RR$; the hypothesis gives some coefficient in the Taylor expansion of $f$ about $a$ that is rational, that is $f^{(n)}(a)/n!=q$ for some $n\geq0$ and $q\in\QQ$, which says $a\in E_{n,q}$.
:::

:::

::: {.pf-step #baire}
Some $E_{n,q}$ has nonempty interior in $\RR$.

::: pf-proof
The index set $\NN\times\QQ$ is countable, so step [](#covering){.pf-ref} exhibits $\RR$ as a countable union of closed sets. $\RR$ with its usual metric is complete, hence a Baire space; in a Baire space a countable union of closed sets with empty interior has empty interior, so not all of these closed sets can have empty interior — otherwise $\RR$ would have empty interior, which is false since $\RR$ is a nonempty open subset of itself. Hence some $E_{n,q}$ contains an interval of positive length.
:::

:::

::: {.pf-step #interval-identity}
There are $n\geq0$, $q\in\QQ$ and a nondegenerate interval $I\subset\RR$ with $f^{(n)}(a)=n!q$ for all $a\in I$.

::: pf-proof
Take $E_{n,q}$ from step [](#baire){.pf-ref} and choose $a_{0}$ in its interior; then some $I=(a_{0}-\delta,a_{0}+\delta)$ with $\delta>0$ lies in $E_{n,q}$, and on it $f^{(n)}/n!\equiv q$ by the definition of $E_{n,q}$.
:::

:::

::: pf-step
Therefore $f$ is a polynomial, of degree at most $n$.

::: pf-proof
The function $g\coloneqq f^{(n)}-n!q$ is entire and vanishes on the interval $I$, which contains infinitely many points with an accumulation point in $\CC$; by the identity theorem an entire function vanishing on a set with an accumulation point is identically zero. So $f^{(n)}\equiv n!q$ on $\CC$. Then $f^{(n+1)}\equiv0$, and an entire function with vanishing $(n+1)$-st derivative is a polynomial of degree at most $n$: its Taylor series about $0$ terminates at the $n$-th power. (For $n=0$ this says $f$ is constant.)
:::

:::

:::

:::
