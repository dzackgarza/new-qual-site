---
schema: qual/card@1
id: P-JKJG3
kind: problem
title: Nonunique factorization of $6$ in $\ZZ[\sqrt{-5}]$ and the prime factorization of $(6)$
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Ideals
  - Prime Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Factor $6$ in two different ways in $R=\ZZ[\sqrt{-5}]$.
Explain the discrepancy using ideal factorization, and factor the principal ideal $(6)$ into prime ideals.
:::

::: {.solution}
There are two element factorizations
$$
6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5}).
$$
The norm $N(a+b\sqrt{-5})=a^2+5b^2$ takes the values $4,9,6,6$ on $2,3,1\pm\sqrt{-5}$ and never the values $2$ or $3$, so these four elements are irreducible, and $2$ is not associate to $1\pm\sqrt{-5}$. So the two factorizations are different factorizations into irreducibles, and $R$ is not a UFD.

Set
$$
\mathfrak p_2=(2,1+\sqrt{-5}),
\qquad
\mathfrak p_3=(3,1+\sqrt{-5}),
\qquad
\overline{\mathfrak p}_3=(3,1-\sqrt{-5}).
$$

::: pf

::: pf-step

These are prime ideals of norms $2,3,3$, respectively.

::: pf-proof

The quotient maps
$$
R\to\FF_2,
\qquad
a+b\sqrt{-5}\mapsto a-b\pmod2,
$$
and
$$
R\to\FF_3,
\qquad
a+b\sqrt{-5}\mapsto a-b\pmod3
$$
(or $a+b$ for the conjugate ideal) have kernels $\mathfrak p_2$, $\mathfrak p_3$, and $\overline{\mathfrak p}_3$. Hence the quotients are fields, so the ideals are maximal and prime. Their norms are the corresponding quotient sizes.

:::

:::

::: pf-step

The rational primes factor as
$$
(2)=\mathfrak p_2^2,
\qquad
(3)=\mathfrak p_3\overline{\mathfrak p}_3.
$$

::: pf-proof

Modulo $2$, the polynomial $x^2+5$ becomes
$$
x^2+1=(x+1)^2,
$$
so $2$ ramifies. Modulo $3$,
$$
x^2+5=x^2-1=(x-1)(x+1),
$$
so $3$ splits. The displayed prime ideals are exactly the ideals corresponding to these linear factors.

:::

:::

::: pf-step

Therefore
$$
(6)=\mathfrak p_2^2\mathfrak p_3\overline{\mathfrak p}_3.
$$

::: pf-proof

Multiply the factorizations of $(2)$ and $(3)$.

:::

:::

::: pf-step

The second element factorization produces the same prime-ideal factorization.

::: pf-proof

Since $1+\sqrt{-5}$ lies in both $\mathfrak p_2$ and $\mathfrak p_3$, we have
$$
(1+\sqrt{-5})\subseteq\mathfrak p_2\mathfrak p_3.
$$
Both ideals have norm $6$:
$$
\abs{N(1+\sqrt{-5})}=1^2+5\cdot1^2=6,
\qquad
N(\mathfrak p_2\mathfrak p_3)=2\cdot3=6.
$$
Hence
$$
(1+\sqrt{-5})=\mathfrak p_2\mathfrak p_3.
$$
By conjugation,
$$
(1-\sqrt{-5})=\mathfrak p_2\overline{\mathfrak p}_3.
$$
Multiplying gives again
$$
(6)=\mathfrak p_2^2\mathfrak p_3\overline{\mathfrak p}_3.
$$

:::

:::

:::

:::
