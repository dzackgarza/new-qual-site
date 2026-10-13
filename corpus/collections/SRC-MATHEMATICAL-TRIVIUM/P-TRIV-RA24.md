---
schema: qual/card@1
id: P-TRIV-RA24
kind: problem
title: $\int_{-\infty}^\infty e^{-x^{-4}-x^4}\sin^5x\,dx$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 24, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find $\int _ { - \infty } ^ { \infty } e ^ { - x ^ { - 4 } - x ^ { 4 } } \sin ^ { 5 } x d x .$
:::

::: {.solution}
Define the integrand for $x\neq0$ by
$$
F(x)
=
e^{-x^{-4}-x^4}\sin^5x.
$$

<1>1. The exponential factor is even:
$$
e^{-(-x)^{-4}-(-x)^4}
=
e^{-x^{-4}-x^4}.
$$

::: {.proof}
Both powers $x^{-4}$ and $x^4$ are even functions on $\mathbb R\setminus\{0\}$.
:::

<1>2. The factor $\sin^5x$ is odd:
$$
\sin^5(-x)=-\sin^5x.
$$

::: {.proof}
Since $\sin(-x)=-\sin x$ and the exponent $5$ is odd, the identity follows.
:::

<1>3. Therefore
$$
F(-x)=-F(x)
$$
for every $x\neq0$.

::: {.proof}
Multiply the parity statements in steps <1>1--<1>2.
:::

<1>4. The integrand extends continuously to $x=0$ by setting
$$
F(0)=0.
$$

::: {.proof}
As $x\to0$,
$$
0\leq
e^{-x^{-4}-x^4}|\sin^5x|
\leq
e^{-x^{-4}}.
$$
Since
$$
e^{-x^{-4}}\to0,
$$
the squeeze theorem gives $F(x)\to0$.
:::

<1>5. The improper integral is absolutely convergent.

::: {.proof}
Near $0$, step <1>4 gives boundedness of the continuous extension.
For $|x|\geq1$,
$$
|F(x)|
\leq
e^{-x^4},
$$
and
$$
\int_1^\infty e^{-x^4}\,dx<\infty.
$$
Thus the integral over $\mathbb R$ converges absolutely.
:::

<1>6. Hence
$$
\boxed{
\int_{-\infty}^{\infty}
e^{-x^{-4}-x^4}\sin^5x\,dx
=0.
}
$$

::: {.proof}
By steps <1>3--<1>5, $F$ is an absolutely integrable odd function on
$\mathbb R$. Therefore its integral over the symmetric domain $\mathbb R$ is
zero.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required value.
:::
:::
