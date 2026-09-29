---
schema: qual/card@1
id: P-BERK83SU-03
kind: problem
title: Jordan form when $\chi=\mu\,(x-i)$ and $\mu^2=\chi\,(x^2+1)$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Cancelling the two polynomial identities gives
    mu=(x-i)^2(x+i) and chi=(x-i)^3(x+i). Thus i has algebraic
    multiplicity 3 and largest Jordan block size 2, forcing block sizes
    2 and 1, while -i has one block of size 1.
---

::: {.problem}
Let $A$ be an $n\times n$ complex matrix with characteristic polynomial $\chi$ and minimal polynomial $\mu$. Suppose
\[
\chi(x)=\mu(x)(x-i),
\qquad
\mu(x)^2=\chi(x)(x^2+1).
\]
Determine the Jordan canonical form of $A$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The minimal polynomial is
$$
\mu(x)=(x-i)^2(x+i).
$$

::: pf-proof

Substitute
$$
\chi(x)=\mu(x)(x-i)
$$
into the second hypothesis:
$$
\mu(x)^2
=
\mu(x)(x-i)(x^2+1).
$$
The minimal polynomial is nonzero, and $\CC[x]$ is an integral domain,
so cancellation gives
$$
\mu(x)
=
(x-i)(x^2+1).
$$
Since
$$
x^2+1=(x-i)(x+i),
$$
we obtain
$$
\mu(x)=(x-i)^2(x+i).
$$

:::

:::

::: {.pf-step #s2}

The characteristic polynomial is
$$
\chi(x)=(x-i)^3(x+i).
$$

::: pf-proof

Using the first hypothesis and step [](#s1){.pf-ref},
$$
\begin{aligned}
\chi(x)
&=
\mu(x)(x-i)\\
&=
(x-i)^3(x+i).
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

The Jordan blocks for the eigenvalue $i$ have sizes $2$ and $1$.

::: pf-proof

For an eigenvalue $\lambda$, its exponent in the characteristic
polynomial is the sum of the sizes of its Jordan blocks, while its
exponent in the minimal polynomial is the size of its largest Jordan
block. By step [](#s2){.pf-ref}, the total size of the $i$-blocks is $3$. By
step [](#s1){.pf-ref}, their largest size is $2$. The only partition of $3$ with
largest part exactly $2$ is
$$
3=2+1.
$$
Thus the $i$-blocks have sizes $2$ and $1$.

:::

:::

::: {.pf-step #s4}

The eigenvalue $-i$ has one Jordan block of size $1$.

::: pf-proof

Step [](#s2){.pf-ref} shows that $-i$ has algebraic multiplicity $1$. Hence its
Jordan blocks have total size $1$, so there is exactly one such block
and it has size $1$.

:::

:::

::: {.pf-step #s5}

Therefore the Jordan canonical form is
$$
\boxed{
\begin{pmatrix}
i&1&0&0\\
0&i&0&0\\
0&0&i&0\\
0&0&0&-i
\end{pmatrix}
}.
$$

::: pf-proof

Step [](#s3){.pf-ref} gives one block
$$
J_2(i)=
\begin{pmatrix}
i&1\\
0&i
\end{pmatrix}
$$
and one $1\times1$ block $(i)$. Step [](#s4){.pf-ref} gives one $1\times1$
block $(-i)$. Their direct sum is the displayed matrix, up to
permutation of Jordan blocks.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the requested Jordan canonical form.

:::

:::

:::
