---
schema: qual/card@1
id: P-APASP08G
kind: problem
title: "Symmetric function identity involving hooks"
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked p_1 = s_(1), the iteration of the Pieri rule
    with the chain-of-partitions to standard-tableau bijection identifying the coefficient
    f^lambda, the hook-length formula f^lambda = n!/h_lambda, the term-by-term identity t^n
    p_1^n/n! = sum over lambda of n of t^n s_lambda/h_lambda, and the regrouping over shapes
    justified as a formal power series identity. The argument is the card's own; no retained
    set is cited. No repair needed.
---

::: {.problem}
Show that
$$
e^{t p_1} = \sum_\lambda t^{\multiindexsize{\lambda}}\frac{s_\lambda}{h_\lambda},
$$
where $h_\lambda$ denotes the product of the hook lengths of $\lambda$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. Everything is an identity of formal power series in $t$ with coefficients in the ring of symmetric functions, so no convergence is at issue.

::: pf

::: {.pf-step #power-sums}
$p_{1}=s_{(1)}$, and by iterating the Pieri rule,
$$
p_{1}^{n}=s_{(1)}^{n}=\sum_{\lambda\vdash n}f^{\lambda}s_{\lambda},
$$
where $f^{\lambda}$ is the number of standard Young tableaux of shape $\lambda$.

::: pf-proof
$p_{1}=x_{1}+x_{2}+\dots=s_{(1)}$. The Pieri rule says that for any partition $\mu$, $s_{\mu}s_{(1)}=\sum_{\nu}s_{\nu}$ over the partitions $\nu$ obtained from $\mu$ by adding one box; so $s_{(1)}^{n}$ is the sum, over $\lambda\vdash n$, of $s_{\lambda}$ with coefficient equal to the number of chains $\varnothing=\mu^{0}\subset\mu^{1}\subset\dots\subset\mu^{n}=\lambda$ of partitions with $\abs{\mu^{i}}=i$. Such a chain is the same thing as a standard Young tableau of shape $\lambda$: the box added at step $i$ receives the entry $i$. Hence the coefficient of $s_{\lambda}$ is $f^{\lambda}$.
:::

:::

::: {.pf-step #hook}
$f^{\lambda}=\dfrac{n!}{h_{\lambda}}$ for $\lambda\vdash n$, where $h_{\lambda}=\prod_{u\in\lambda}h(u)$ is the product of the hook lengths.

::: pf-proof
This is the hook-length formula for the number of standard Young tableaux of shape $\lambda$.
:::

:::

::: {.pf-step #each-n}
For every $n\ge0$, $\ \dfrac{t^{n}}{n!}p_{1}^{n}=\displaystyle\sum_{\lambda\vdash n}t^{n}\dfrac{s_{\lambda}}{h_{\lambda}}$.

::: pf-proof
By steps [](#power-sums){.pf-ref} and [](#hook){.pf-ref}, $p_{1}^{n}=\sum_{\lambda\vdash n}\frac{n!}{h_{\lambda}}s_{\lambda}$; dividing by $n!$ gives the equality, and when $n=0$ both sides are $1$, the empty partition contributing $s_{\varnothing}/h_{\varnothing}=1$.
:::

:::

::: {.pf-step #exponential}
$\displaystyle e^{tp_{1}}=\sum_{\lambda}t^{\abs{\lambda}}\frac{s_{\lambda}}{h_{\lambda}}$.

::: pf-proof
Expand the exponential as a formal power series and apply step [](#each-n){.pf-ref} term by term:
$$
e^{tp_{1}}=\sum_{n\ge0}\frac{t^{n}p_{1}^{n}}{n!}=\sum_{n\ge0}\sum_{\lambda\vdash n}t^{n}\frac{s_{\lambda}}{h_{\lambda}}=\sum_{\lambda}t^{\abs{\lambda}}\frac{s_{\lambda}}{h_{\lambda}},
$$
the last step regrouping by shape, which is legitimate because only finitely many $\lambda$ satisfy $\abs{\lambda}\le N$ for each $N$ and the coefficient of each $s_{\lambda}$ receives contributions from one $n$ only, namely $n=\abs{\lambda}$.
:::

:::

::: {.pf-step}
The identity holds.

::: pf-proof
Step [](#exponential){.pf-ref} is the asserted identity.
:::

:::

:::
:::
