---
schema: qual/card@1
id: P-ALGREV1-04
kind: problem
title: A homomorphism from Z8 to Z20
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared all three parts with Review1.md, open-ended question 4."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Solved for phi(1)=5, then computed image, kernel, and the two-element fiber over 5."
---
::: {.problem}
Suppose that $\phi:\ZZ_8\to\ZZ_{20}$ is a group homomorphism with $\phi(3)=15$.

1. Determine $\phi(x)$.
2. Determine the image and kernel of $\phi$.
3. Determine $\phi^{-1}(5)$.
:::

::: {.solution}
All groups are written additively.

::: pf

::: {.pf-step #s1}

Determine the homomorphism.

::: pf-proof

Every homomorphism from the cyclic group $\ZZ_8$ is determined by
$$
a=\phi(1)\in\ZZ_{20},
$$
with
$$
\phi(x)=xa.
$$
The hypothesis gives
$$
3a=15\pmod{20}.
$$
Since $3^{-1}=7$ modulo $20$,
$$
a=7\cdot15=105=5\pmod{20}.
$$
This value is compatible with the relation $8=0$ in $\ZZ_8$ because
$$
8a=40=0\pmod{20}.
$$
Therefore
$$
\boxed{\phi(x)=5x\pmod{20}.}
$$

:::

:::

::: {.pf-step #s2}

Compute the image and kernel.

::: pf-proof

As $x$ ranges through $\ZZ_8$, the multiples $5x$ modulo $20$ are
$$
0,5,10,15.
$$
Hence
$$
\boxed{\operatorname{im}\phi=\{0,5,10,15\}.}
$$

Also
$$
\phi(x)=0
\iff 5x\equiv0\pmod{20}
\iff x\equiv0\pmod4.
$$
Thus in $\ZZ_8$,
$$
\boxed{\ker\phi=\{0,4\}.}
$$

:::

:::

::: {.pf-step #s3}

Compute the fiber over $5$.

::: pf-proof

We have
$$
\phi(x)=5
\iff 5x\equiv5\pmod{20}
\iff x\equiv1\pmod4.
$$
The two such classes modulo $8$ are $1$ and $5$. Therefore
$$
\boxed{\phi^{-1}(5)=\{1,5\}.}
$$

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} determines $\phi$, step [](#s2){.pf-ref} gives its image and kernel, and step [](#s3){.pf-ref} gives the requested fiber.

:::

:::

:::
