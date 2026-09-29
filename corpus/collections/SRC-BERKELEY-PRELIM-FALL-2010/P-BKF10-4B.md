---
schema: qual/card@1
id: P-BKF10-4B
kind: problem
title: Determinant of the $6\times6$ matrix $(j^k)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 4B of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the row-factor reduction to a Vandermonde determinant and
    the resulting prime exponents.
---

::: {.problem}
Find the determinant of the $6\times6$ matrix whose entries are
$$
a_{j,k}=j^k,\qquad 1\le j,k\le6.
$$
You may give your answer as a product of powers of primes.
:::

::: {.solution}
Let
$$
A=(j^k)_{1\le j,k\le6}.
$$

::: pf

::: {.pf-step #s1}

Factoring $j$ from row $j$ gives
$$
\det A
=\left(\prod_{j=1}^6j\right)
\det\bigl(j^{k-1}\bigr)_{1\le j,k\le6}.
$$

::: pf-proof

Every entry in row $j$ has the form
$$
j^k=j\,j^{k-1}.
$$
Pulling the common factor $j$ out of each row multiplies the determinant
by the product of those six row factors.

:::

:::

::: {.pf-step #s2}

The remaining determinant is
$$
\det\bigl(j^{k-1}\bigr)_{1\le j,k\le6}
=\prod_{1\le i<j\le6}(j-i).
$$

::: pf-proof

The matrix $(j^{k-1})$ is the Vandermonde matrix for the ordered points
$1,2,3,4,5,6$. The Vandermonde determinant formula therefore gives
exactly the displayed product. Every factor $j-i$ is positive, so no
additional sign occurs.

:::

:::

::: {.pf-step #s3}

One has
$$
\prod_{1\le i<j\le6}(j-i)
=1^5\cdot2^4\cdot3^3\cdot4^2\cdot5.
$$

::: pf-proof

For each $d=1,\ldots,5$, the difference $j-i=d$ occurs for precisely
$6-d$ pairs $(i,j)$ with $1\le i<j\le6$. Multiplying by difference size
therefore gives
$$
\prod_{d=1}^5d^{6-d}
=1^5\cdot2^4\cdot3^3\cdot4^2\cdot5.
$$

:::

:::

::: {.pf-step #s4}

The determinant is
$$
\boxed{\det A=2^{12}3^5 5^2}.
$$

::: pf-proof

By steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref},
$$
\det A
=(1\cdot2\cdot3\cdot4\cdot5\cdot6)
 (1^5 2^4 3^3 4^2 5).
$$
Now
$$
1\cdot2\cdot3\cdot4\cdot5\cdot6=2^4 3^2 5,
$$
while
$$
1^5 2^4 3^3 4^2 5=2^8 3^3 5.
$$
Multiplying gives $2^{12}3^5 5^2$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the requested determinant.

:::

:::

:::
