---
schema: qual/card@1
id: P-TRIV-PR19
kind: problem
title: Conditional expectations of sums of independent Bernoulli variables
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 19, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Let ξ and η be two independent random variables taking values 1 and 0 with the probabilities p and $q = 1 - p$ correspondingly.
Find

$$
\mathbf { E } ( \xi + \eta | \eta ) .
$$

$$
\mathbf { E } ( \xi | \xi + \eta ) .
$$
:::

::: {.solution}
Let $S=\xi+\eta$. Both $\xi$ and $\eta$ are independent Bernoulli random variables with parameter $p$.

<1>1. Independence gives
\[
\mathbf E(\xi\mid\eta)=\mathbf E\xi=p.
\]

::: {.proof}
For each possible value of $\eta$, the conditional distribution of $\xi$ equals its unconditional Bernoulli$(p)$ distribution because $\xi$ and $\eta$ are independent.
:::

<1>2. Therefore
\[
\boxed{\mathbf E(\xi+\eta\mid\eta)=p+\eta}.
\]

::: {.proof}
By linearity of conditional expectation and because $\eta$ is measurable with respect to itself,
\[
\mathbf E(\xi+\eta\mid\eta)
=\mathbf E(\xi\mid\eta)+\eta.
\]
Apply step <1>1.
:::

<1>3. Conditional on $S=0$, one has $\xi=0$, and conditional on $S=2$, one has $\xi=1$.

::: {.proof}
Since $\xi,\eta\in\{0,1\}$, the sum $0$ occurs only for $(0,0)$ and the sum $2$ only for $(1,1)$.
:::

<1>4. Conditional on $S=1$,
\[
P(\xi=1\mid S=1)=\frac12.
\]

::: {.proof}
The event $S=1$ consists of the two outcomes $(\xi,\eta)=(1,0)$ and $(0,1)$. Independence gives each probability $pq$, so after conditioning they have equal probability $1/2$.
:::

<1>5. Hence
\[
\boxed{\mathbf E(\xi\mid\xi+\eta)=\frac{\xi+\eta}{2}}.
\]

::: {.proof}
By steps <1>3--<1>4, the conditional expectation takes the values $0,1/2,1$ when $S$ equals $0,1,2$, respectively. This is exactly $S/2$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>2 and <1>5 give the two requested conditional expectations.
:::
:::
