---
schema: qual/card@1
id: P-APAF20A
kind: problem
title: Jordan form of a map on $\mathbb{C}^{20}$ with $\phi^3=\phi^2$ and eight-dimensional eigenspaces
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
A linear map $\phi\colon\mathbb{C}^{20}\to\mathbb{C}^{20}$ has the property that $\phi^3=\phi^2$.

(a) Show that if $\lambda$ is an eigenvalue of $\phi$ then $\lambda=0$ or $\lambda=1$.

Now suppose furthermore that $\dim E(0,\phi)=\dim E(1,\phi)=8$.
[Here $E(\lambda,\phi)\subseteq\mathbb{C}^{20}$ denotes the eigenspace of $\phi$ with eigenvalue $\lambda$.]

(b) Find, with justification, the Jordan Normal Form of $\phi$.

[For this question, “find the Jordan Normal form” means you should determine the sizes and multiplicities of the Jordan blocks. You should not attempt to describe a basis that puts $\phi$ in Jordan Normal Form.]
:::

::: {.solution}
**(a).**

::: pf

::: {.pf-step #phi-satisfies-cubic-minus-square}
$\phi$ satisfies the polynomial $p(x) = x^3 - x^2 = x^2(x - 1)$.

::: pf-proof
$\phi^3 = \phi^2$ means $\phi^3 - \phi^2 = 0$, i.e. $p(\phi) = 0$.
:::

:::

::: {.pf-step #minimal-poly-divides-x2-x-minus-1}
Hence the minimal polynomial of $\phi$ divides $x^2(x-1)$.

::: pf-proof
Step [](#phi-satisfies-cubic-minus-square){.pf-ref} (the minimal polynomial divides any annihilating polynomial).
:::

:::

::: {.pf-step #eigenvalues-are-0-or-1}
Therefore the only possible eigenvalues are the roots of $x^2(x-1)$, namely $0$ and $1$.

::: pf-proof
Step [](#minimal-poly-divides-x2-x-minus-1){.pf-ref} (eigenvalues are roots of the minimal polynomial).
:::

:::

:::

**(b).**

::: pf

::: {.pf-step #eight-jordan-blocks-for-zero}
$\dim E(0, \phi) = 8$ means there are $8$ Jordan blocks for eigenvalue $0$.

::: pf-proof
the dimension of the eigenspace equals the number of Jordan blocks for that eigenvalue.
:::

:::

::: {.pf-step #eight-jordan-blocks-for-one}
$\dim E(1, \phi) = 8$ means there are $8$ Jordan blocks for eigenvalue $1$.

::: pf-proof
same as step [](#eight-jordan-blocks-for-zero){.pf-ref}.
:::

:::

::: {.pf-step #block-sizes-bounded-by-minimal-poly}
The minimal polynomial divides $x^2(x-1)$, so the Jordan blocks for eigenvalue $0$ have size at most $2$, and the blocks for eigenvalue $1$ have size $1$.

::: pf-proof
Step [](#minimal-poly-divides-x2-x-minus-1){.pf-ref} (the exponent of $x$ in the minimal polynomial is the size of the largest Jordan block for $0$, and the exponent of $(x-1)$ is the size of the largest block for $1$).
:::

:::

::: {.pf-step #eigenvalue-one-contributes-eight-dimensions}
The total dimension is $20$, and the eigenvalue $1$ contributes $8$ blocks of size $1$, i.e. $8$ dimensions.

::: pf-proof
Steps [](#eight-jordan-blocks-for-one){.pf-ref} and [](#block-sizes-bounded-by-minimal-poly){.pf-ref}.
:::

:::

::: {.pf-step #eigenvalue-zero-contributes-twelve-dimensions}
Hence the eigenvalue $0$ contributes $20 - 8 = 12$ dimensions, split among $8$ Jordan blocks each of size $1$ or $2$.

::: pf-proof
Steps [](#eight-jordan-blocks-for-zero){.pf-ref} and [](#eigenvalue-one-contributes-eight-dimensions){.pf-ref}.
:::

:::

::: {.pf-step #solve-for-k-equals-four}
Let $k$ be the number of size-$2$ blocks for eigenvalue $0$; then $2k + (8 - k) = 12$, so $k = 4$.

::: pf-proof
Step [](#eigenvalue-zero-contributes-twelve-dimensions){.pf-ref} (the $8$ blocks for $0$ consist of $k$ blocks of size $2$ and $8 - k$ blocks of size $1$, totaling $2k + (8-k) = 8 + k = 12$ dimensions).
:::

:::

::: {.pf-step #jordan-form-block-counts}
Hence the Jordan form has: $4$ blocks of size $2$ for eigenvalue $0$, $4$ blocks of size $1$ for eigenvalue $0$, and $8$ blocks of size $1$ for eigenvalue $1$.

::: pf-proof
Steps [](#solve-for-k-equals-four){.pf-ref} and [](#eight-jordan-blocks-for-one){.pf-ref}.
:::

:::

::: pf-qed
Steps [](#eigenvalues-are-0-or-1){.pf-ref} and [](#jordan-form-block-counts){.pf-ref} answer parts (a) and (b).
:::

:::

:::
