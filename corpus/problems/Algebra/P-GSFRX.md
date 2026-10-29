---
schema: qual/card@1
id: P-GSFRX
kind: problem
title: Minimal and characteristic polynomials of a $5\times 5$ real matrix with eigenvalues
  $0,1\pm i,1\pm 2i$
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}

Let $L \in M_5(\RR)$ be a $5 \times 5$ real matrix with eigenvalues $0, 1 + i, 1 + 2i$.
Find the characteristic polynomial $\chi_L(x)$ and the minimal polynomial $\mu_L(x)$ of $L$ over $\RR$.

:::

::: {.solution}

::: pf

::: {.pf-step #spectrum}

The eigenvalues of $L$ are $0$, $1\pm i$, $1\pm 2i$, each with algebraic multiplicity $1$.

::: pf-proof

Because $\chi_L$ has real coefficients, nonreal eigenvalues occur in complex-conjugate pairs, so $1-i$ and $1-2i$ are also eigenvalues. These are five distinct roots of $\chi_L$, which has degree $5$.

:::

:::

::: pf-step

$$
\chi_L(x)=\boxed{x(x^2-2x+2)(x^2-2x+5)=x^5-4x^4+11x^3-14x^2+10x}.
$$

::: pf-proof

By step [](#spectrum){.pf-ref},
$$
\begin{aligned}
\chi_L(x)
&=x(x-(1+i))(x-(1-i))(x-(1+2i))(x-(1-2i))\\
&=x\bigl((x-1)^2+1\bigr)\bigl((x-1)^2+4\bigr)\\
&=x(x^2-2x+2)(x^2-2x+5),
\end{aligned}
$$
and expanding gives the quintic.

:::

:::

::: pf-step

$$
\mu_L(x)=\boxed{\chi_L(x)}.
$$

::: pf-proof

Every eigenvalue is a root of the minimal polynomial, so by step [](#spectrum){.pf-ref} $\mu_L$ has five distinct roots and $\deg\mu_L\ge5$. Since $\mu_L\mid\chi_L$ by the Cayley--Hamilton theorem and $\chi_L$ is monic of degree $5$, $\mu_L=\chi_L$.

:::

:::

:::

:::
