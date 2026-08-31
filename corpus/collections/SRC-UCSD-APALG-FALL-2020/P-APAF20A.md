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

::: problem
A linear map $\phi\colon\mathbb{C}^{20}\to\mathbb{C}^{20}$ has the property that $\phi^3=\phi^2$.

(a) Show that if $\lambda$ is an eigenvalue of $\phi$ then $\lambda=0$ or $\lambda=1$.

Now suppose furthermore that $\dim E(0,\phi)=\dim E(1,\phi)=8$.
[Here $E(\lambda,\phi)\subseteq\mathbb{C}^{20}$ denotes the eigenspace of $\phi$ with eigenvalue $\lambda$.]

(b) Find, with justification, the Jordan Normal Form of $\phi$.

[For this question, “find the Jordan Normal form” means you should determine the sizes and multiplicities of the Jordan blocks. You should not attempt to describe a basis that puts $\phi$ in Jordan Normal Form.]
:::

::: {.solution}
**(a).**

<1>1. $\phi$ satisfies the polynomial $p(x) = x^3 - x^2 = x^2(x - 1)$.
::: {.proof}
$\phi^3 = \phi^2$ means $\phi^3 - \phi^2 = 0$, i.e. $p(\phi) = 0$.
:::

<1>2. Hence the minimal polynomial of $\phi$ divides $x^2(x-1)$.
::: {.proof}
<1>1 (the minimal polynomial divides any annihilating polynomial).
:::

<1>3. Therefore the only possible eigenvalues are the roots of $x^2(x-1)$, namely $0$ and $1$.
::: {.proof}
<1>2 (eigenvalues are roots of the minimal polynomial).
:::

**(b).**

<1>1. $\dim E(0, \phi) = 8$ means there are $8$ Jordan blocks for eigenvalue $0$.
::: {.proof}
the dimension of the eigenspace equals the number of Jordan blocks for that eigenvalue.
:::

<1>2. $\dim E(1, \phi) = 8$ means there are $8$ Jordan blocks for eigenvalue $1$.
::: {.proof}
same as <1>1.
:::

<1>3. The minimal polynomial divides $x^2(x-1)$, so the Jordan blocks for eigenvalue $0$ have size at most $2$, and the blocks for eigenvalue $1$ have size $1$.
::: {.proof}
<1>2 (a) (the exponent of $x$ in the minimal polynomial is the size of the largest Jordan block for $0$, and the exponent of $(x-1)$ is the size of the largest block for $1$).
:::

<1>4. The total dimension is $20$, and the eigenvalue $1$ contributes $8$ blocks of size $1$, i.e. $8$ dimensions.
::: {.proof}
<1>2 and <1>3.
:::

<1>5. Hence the eigenvalue $0$ contributes $20 - 8 = 12$ dimensions, split among $8$ Jordan blocks each of size $1$ or $2$.
::: {.proof}
<1>1 and <1>4.
:::

<1>6. Let $k$ be the number of size-$2$ blocks for eigenvalue $0$; then $2k + (8 - k) = 12$, so $k = 4$.
::: {.proof}
<1>5 (the $8$ blocks for $0$ consist of $k$ blocks of size $2$ and $8 - k$ blocks of size $1$, totaling $2k + (8-k) = 8 + k = 12$ dimensions).
:::

<1>7. Hence the Jordan form has: $4$ blocks of size $2$ for eigenvalue $0$, $4$ blocks of size $1$ for eigenvalue $0$, and $8$ blocks of size $1$ for eigenvalue $1$.
::: {.proof}
<1>6 and <1>2.
:::

<1>8. Q.E.D.
::: {.proof}
<1>3 (a) and <1>7 (b).
:::
:::
