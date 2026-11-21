---
schema: qual/card@1
id: P-CASNS
kind: problem
title: Degree of $\QQ(7^{1/5},5^{1/4})$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the numbered list the card carried. The source is a course
    examination, so there is no retained solution set behind the card and the problem statement is
    the source. Each step re-read: Eisenstein at 7 for x^5 - 7 and at 5 for x^4 - 5, both checked
    against the criterion's two conditions; the tower law in the two orders gives that both 5 and 4
    divide the degree, hence 20; and x^4 - 5 is a polynomial over Q(alpha) of degree 4 with beta as
    a root, giving the upper bound. Equality of the bounds settles the question. Not claimed: that
    x^4 - 5 is irreducible over Q(alpha), which is not needed.
---

::: {.problem}
Let $\alpha,\beta$ denote the unique positive real $5^{\text{th}}$ root of 7 and $4^{\text{th}}$ root of 5, respectively.
Determine the degree of $\QQ[\alpha,\beta]$ over $\QQ$.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #alpha}
$[\QQ(\alpha):\QQ]=5$.

::: pf-proof
$\alpha=7^{1/5}$ is a root of $x^{5}-7$, which is irreducible over $\QQ$ by Eisenstein's criterion at the prime $7$ ($7$ divides all coefficients but the leading one, and $7^{2}=49$ does not divide $7$). The minimal polynomial is therefore $x^{5}-7$ and the degree of the extension is its degree, $5$.
:::

:::

::: {.pf-step #beta}
$[\QQ(\beta):\QQ]=4$.

::: pf-proof
$\beta=5^{1/4}$ is a root of $x^{4}-5$, irreducible over $\QQ$ by Eisenstein's criterion at the prime $5$ (the constant term $5$ is not divisible by $25$). The minimal polynomial is $x^{4}-5$ and the degree is $4$.
:::

:::

::: {.pf-step #divisible}
$20$ divides $[\QQ(\alpha,\beta):\QQ]$.

::: pf-proof
By the tower law applied to $\QQ\subseteq\QQ(\alpha)\subseteq\QQ(\alpha,\beta)$, the degree is $[\QQ(\alpha,\beta):\QQ(\alpha)]\cdot5$, so $5$ divides it; applying the tower law with $\QQ(\beta)$ in place of $\QQ(\alpha)$ shows $4$ divides it. Since $\gcd(4,5)=1$, the product $20$ divides it.
:::

:::

::: {.pf-step #atmost}
$[\QQ(\alpha,\beta):\QQ]\le20$.

::: pf-proof
$\beta$ is a root of $x^{4}-5\in\QQ(\alpha)[x]$, so the minimal polynomial of $\beta$ over $\QQ(\alpha)$ divides $x^{4}-5$ and has degree at most $4$; hence $[\QQ(\alpha,\beta):\QQ(\alpha)]\le4$ and the tower law gives $[\QQ(\alpha,\beta):\QQ]\le4\cdot5=20$.
:::

:::

::: {.pf-step}
$[\QQ(\alpha,\beta):\QQ]=20$.

::: pf-proof
Steps [](#divisible){.pf-ref} and [](#atmost){.pf-ref} bound the degree from below and above by $20$:
$$
\boxed{[\QQ(7^{1/5},5^{1/4}):\QQ]=20.}
$$
Equivalently, the polynomial $x^{4}-5$ remains irreducible over $\QQ(7^{1/5})$, which the equality of the two bounds establishes without a separate argument.
:::

:::

:::
:::
