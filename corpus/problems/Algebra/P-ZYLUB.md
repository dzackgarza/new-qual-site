---
schema: qual/card@1
id: P-ZYLUB
kind: problem
title: $4\times 4$ Jordan forms with minimal polynomial $(x-1)(x-2)^2$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
relations: []
review: draft
---

::: {.problem}
Give the $4 \times 4$ Jordan forms with minimal polynomial $(x - 1)(x - 2)^2$.
:::


::: {.solution}
The minimal polynomial
\[
m_A(x)=(x-1)(x-2)^2
\]
says exactly the following about the Jordan blocks:

- for eigenvalue $1$, every Jordan block has size $1$, and at least one such block occurs;
- for eigenvalue $2$, every Jordan block has size at most $2$, and at least one block has size exactly $2$.

Since the total dimension is $4$, enumerate the possible partitions of the generalized eigenspace dimensions subject to those constraints.

<1>1. The eigenvalue-$2$ generalized eigenspace has dimension $2$.
Then it must contribute one block $J_2(2)$, while eigenvalue $1$ contributes two $1\times1$ blocks:
\[
J_2(2)\oplus[1]\oplus[1].
\]

<1>2. The eigenvalue-$2$ generalized eigenspace has dimension $3$.
It must contain one block of size $2$ and one block of size $1$, while eigenvalue $1$ contributes one block:
\[
J_2(2)\oplus[2]\oplus[1].
\]

No other case is possible. The eigenvalue-$2$ generalized eigenspace cannot have dimension $4$, because the factor $(x-1)$ in the minimal polynomial requires eigenvalue $1$ to occur; and it cannot have dimension $1$, because $(x-2)^2$ requires a size-$2$ Jordan block.

Hence, up to permutation of Jordan blocks, the only Jordan forms are
\[
\boxed{J_2(2)\oplus[1]\oplus[1]}
\qquad\text{and}\qquad
\boxed{J_2(2)\oplus[2]\oplus[1]}.
\]
:::
