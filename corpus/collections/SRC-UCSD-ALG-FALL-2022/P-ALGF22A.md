---
schema: qual/card@1
id: P-ALGF22A
kind: problem
title: "Subgroup counts in the simple group of order 168"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 1 of the official UCSD Algebra Qualifying Exam, Fall 2022 source; all three requested subgroup orders agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the Sylow count, the normalizer bijection for order-21 subgroups, and the index-four action obstruction for order 42.
---

::: {.problem}
Let $G$ be a simple group of order $168 = (2^3)(3)(7)$.
For each $n$ below, calculate the number of subgroups of order $n$ inside $G$.
(For some $n$ the answer could be 0.)

(a) $n = 7$

(b) $n = 21$

(c) $n = 42$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The number of subgroups of order $7$ is $8$.

::: pf-proof

Such subgroups are exactly the Sylow $7$-subgroups of $G$.
If $n_7$ denotes their number, Sylow's theorem gives
\[
n_7\equiv1\pmod7,
\qquad
n_7\mid24.
\]
Among the divisors of $24$, the only possibilities congruent to $1$ modulo $7$ are $1$ and $8$.
If $n_7=1$, the unique Sylow $7$-subgroup would be normal in $G$, contradicting simplicity.
Hence
\[
n_7=8.
\]
This proves part (a).

:::

:::

::: {.pf-step #s2}

For every Sylow $7$-subgroup $P\le G$, its normalizer has order $21$.

::: pf-proof

Conjugation by $G$ acts transitively on the eight Sylow $7$-subgroups from step [](#s1){.pf-ref}.
The stabilizer of $P$ is $N_G(P)$, so orbit-stabilizer gives
\[
[G:N_G(P)]=8.
\]
Therefore
\[
|N_G(P)|=\frac{168}{8}=21.
\]

:::

:::

::: {.pf-step #s3}

Every subgroup $H\le G$ of order $21$ is the normalizer of its unique Sylow $7$-subgroup.

::: pf-proof

Let $P$ be a Sylow $7$-subgroup of $H$.
Inside $H$, Sylow's theorem gives
\[
n_7(H)\equiv1\pmod7,
\qquad
n_7(H)\mid3.
\]
Thus $n_7(H)=1$, so $P\trianglelefteq H$.
Hence
\[
H\le N_G(P).
\]
By step [](#s2){.pf-ref}, both groups have order $21$, so
\[
H=N_G(P).
\]

:::

:::

::: pf-step

The number of subgroups of order $21$ is $8$.

::: pf-proof

By step [](#s2){.pf-ref}, each of the eight Sylow $7$-subgroups $P$ gives an order-$21$ subgroup $N_G(P)$.
By step [](#s3){.pf-ref}, every order-$21$ subgroup arises this way.
Moreover, $N_G(P)$ has a unique Sylow $7$-subgroup, namely $P$, so distinct Sylow $7$-subgroups have distinct normalizers.
Thus there are exactly eight subgroups of order $21$.
This proves part (b).

:::

:::

::: pf-step

There is no subgroup of order $42$.

::: pf-proof

Suppose $H\le G$ has order $42$.
Then
\[
[G:H]=4.
\]
The action of $G$ on the four left cosets of $H$ gives a homomorphism
\[
\varphi:G\longrightarrow S_4.
\]
Its kernel is normal in the simple group $G$, so
\[
\ker\varphi=1
\quad\text{or}\quad
\ker\varphi=G.
\]
The action is not trivial: if every element fixed the coset $H$, then every element of $G$ would lie in $H$, contrary to $H\ne G$.
Hence $\ker\varphi\ne G$, so $\varphi$ is injective.
But an injection
\[
G\hookrightarrow S_4
\]
would imply
\[
168=|G|\le|S_4|=24,
\]
a contradiction.
Therefore no subgroup of order $42$ exists.
This proves part (c).

:::

:::

:::

:::
