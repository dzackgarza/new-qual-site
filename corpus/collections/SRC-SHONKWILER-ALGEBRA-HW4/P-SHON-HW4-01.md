---
schema: qual/card@1
id: P-SHON-HW4-01
kind: problem
title: A coprime-index normal subgroup is unique of its order
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against exercise 3.2.19 in the retained Algebra HW 4 solution packet.
---

::: {.problem}
Let $N\triangleleft G$ be a normal subgroup of a finite group $G$.
Assume
$$
\gcd(|N|,[G:N])=1.
$$
Prove that $N$ is the unique subgroup of $G$ of order $|N|$.
:::

::: {.solution}

Let
$$
H\le G
$$
be any subgroup with
$$
|H|=|N|.
$$

::: pf

::: pf-step

Since
$$
N\triangleleft G,
$$
the product
$$
HN
$$
is a subgroup of $G$.


::: pf-proof

If $N$ is normal, then for $h_1n_1,h_2n_2\in HN$,
$$
(h_1n_1)(h_2n_2)
=
h_1h_2(h_2^{-1}n_1h_2)n_2\in HN,
$$
and inverses are handled similarly. Thus $HN\le G$.

:::

:::

::: {.pf-step #s1-2}

The second isomorphism theorem gives
$$
\boxed{
HN/N\cong H/(H\cap N)}.
$$


::: pf-proof

For $H\le G$ and $N\triangleleft G$, the map
$$
H\to HN/N,
\qquad
h\mapsto hN,
$$
is surjective with kernel $H\cap N$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
|HN/N|
=
[H:H\cap N]}.
$$


::: pf-proof

Take orders in the finite-group isomorphism from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The integer
$$
|HN/N|
$$
divides
$$
[G:N].
$$


::: pf-proof

Since
$$
N\le HN\le G,
$$
the quotient $HN/N$ is a subgroup of $G/N$. By Lagrange's theorem,
$$
|HN/N|\mid|G/N|=[G:N].
$$

:::

:::

::: {.pf-step #s1-5}

The integer
$$
|HN/N|
$$
also divides $|H|$.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
|HN/N|=[H:H\cap N],
$$
and every subgroup index divides the group order in a finite group.

:::

:::

::: {.pf-step #s1-6}

Since
$$
|H|=|N|,
$$
one has
$$
\boxed{
|HN/N|\mid|N|}.
$$


::: pf-proof

Substitute the given equality into step [](#s1-5){.pf-ref}.

:::

:::

::: pf-step

By the coprimality hypothesis,
$$
\boxed{
|HN/N|=1}.
$$


::: pf-proof

Steps [](#s1-4){.pf-ref} and [](#s1-6){.pf-ref} show that $|HN/N|$ divides both
$$
[G:N]
$$
and
$$
|N|.
$$
Since
$$
\gcd(|N|,[G:N])=1,
$$
the only common positive divisor is $1$.

:::

:::

::: pf-step

Hence
$$
\boxed{HN=N}.
$$


::: pf-proof

The quotient $HN/N$ has one element exactly when $HN=N$.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\boxed{H\subseteq N}.
$$


::: pf-proof

Since
$$
H\subseteq HN=N.
$$

:::

:::

::: {.pf-step #s1-10}

Since
$$
|H|=|N|,
$$
the inclusion in step [](#s1-9){.pf-ref} is equality:
$$
\boxed{H=N}.
$$


::: pf-proof

A finite subgroup contained in another finite group of the same order must equal it.

:::

:::

::: {.pf-step #s1-11}

Thus $N$ is the unique subgroup of $G$ of order $|N|$.


::: pf-proof

The subgroup $H$ was arbitrary among subgroups with $|H|=|N|$, and step [](#s1-10){.pf-ref} shows every such $H$ equals $N$.

:::

:::

::: pf-qed

Step [](#s1-11){.pf-ref} is the required uniqueness statement.

:::

:::

:::
