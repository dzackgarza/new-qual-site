---
schema: qual/card@1
id: P-TRIV-RA24
kind: problem
title: $\int_{-\infty}^\infty e^{-x^{-4}-x^4}\sin^5x\,dx$
classification:
  areas: [real-analysis]
  topics:
  - Definite Integrals
  - Odd Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 24, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find $\int_{-\infty}^{\infty} e^{-x^{-4} - x^4}\sin^5 x\, dx$.
:::

::: {.solution}

Define the integrand for $x\neq0$ by
$$
F(x)
=
e^{-x^{-4}-x^4}\sin^5x.
$$

::: pf

::: {.pf-step #s1-1}

The exponential factor is even:
$$
e^{-(-x)^{-4}-(-x)^4}
=
e^{-x^{-4}-x^4}.
$$


::: pf-proof

Both powers $x^{-4}$ and $x^4$ are even functions on $\RR\setminus\{0\}$.

:::

:::

::: {.pf-step #s1-2}

The factor $\sin^5x$ is odd:
$$
\sin^5(-x)=-\sin^5x.
$$


::: pf-proof

Since $\sin(-x)=-\sin x$ and the exponent $5$ is odd, the identity follows.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
F(-x)=-F(x)
$$
for every $x\neq0$.


::: pf-proof

Multiply the parity statements in steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The integrand extends continuously to $x=0$ by setting
$$
F(0)=0.
$$


::: pf-proof

As $x\to0$,
$$
0\leq
e^{-x^{-4}-x^4}\abs{\sin^5x}
\leq
e^{-x^{-4}}.
$$
Since
$$
e^{-x^{-4}}\to0,
$$
the squeeze theorem gives $F(x)\to0$.

:::

:::

::: {.pf-step #s1-5}

The improper integral is absolutely convergent.


::: pf-proof

Near $0$, step [](#s1-4){.pf-ref} gives boundedness of the continuous extension.
For $\abs{x}\geq1$,
$$
\abs{F(x)}
\leq
e^{-x^4},
$$
and
$$
\int_1^\infty e^{-x^4}\,dx<\infty.
$$
Thus the integral over $\RR$ converges absolutely.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{
\int_{-\infty}^{\infty}
e^{-x^{-4}-x^4}\sin^5x\,dx
=0.
}
$$


::: pf-proof

By steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref}, $F$ is an absolutely integrable odd function on
$\RR$. Therefore its integral over the symmetric domain $\RR$ is
zero.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required value.

:::

:::

:::
