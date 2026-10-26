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
\[
\gcd(|N|,[G:N])=1.
\]
Prove that $N$ is the unique subgroup of $G$ of order $|N|$.
:::

Let
\[
H\le G
\]
be any subgroup with
\[
|H|=|N|.
\]

::: pf

::: pf-step

Since
\[
N\triangleleft G,
\]
the product
\[
HN
\]
is a subgroup of \(G\).


::: pf-proof

If \(N\) is normal, then for \(h_1n_1,h_2n_2\in HN\),
\[
(h_1n_1)(h_2n_2)
=
h_1h_2(h_2^{-1}n_1h_2)n_2\in HN,
\]
and inverses are handled similarly. Thus \(HN\le G\).

:::

:::

::: pf-step

The second isomorphism theorem gives
\[
\boxed{
HN/N\cong H/(H\cap N)}.
\]


::: pf-proof

For \(H\le G\) and \(N\triangleleft G\), the map
\[
H\to HN/N,
\qquad
h\mapsto hN,
\]
is surjective with kernel \(H\cap N\).

:::

:::

::: pf-step

Therefore
\[
\boxed{
|HN/N|
=
[H:H\cap N]}.
\]


::: pf-proof

Take orders in the finite-group isomorphism from step <1>2.

:::

:::

::: pf-step

The integer
\[
|HN/N|
\]
divides
\[
[G:N].
\]


::: pf-proof

Since
\[
N\le HN\le G,
\]
the quotient \(HN/N\) is a subgroup of \(G/N\). By Lagrange's theorem,
\[
|HN/N|\mid|G/N|=[G:N].
\]

:::

:::

::: pf-step

The integer
\[
|HN/N|
\]
also divides \(|H|\).


::: pf-proof

By step <1>3,
\[
|HN/N|=[H:H\cap N],
\]
and every subgroup index divides the group order in a finite group.

:::

:::

::: pf-step

Since
\[
|H|=|N|,
\]
one has
\[
\boxed{
|HN/N|\mid|N|}.
\]


::: pf-proof

Substitute the given equality into step <1>5.

:::

:::

::: pf-step

By the coprimality hypothesis,
\[
\boxed{
|HN/N|=1}.
\]


::: pf-proof

Steps <1>4 and <1>6 show that \(|HN/N|\) divides both
\[
[G:N]
\]
and
\[
|N|.
\]
Since
\[
\gcd(|N|,[G:N])=1,
\]
the only common positive divisor is \(1\).

:::

:::

::: pf-step

Hence
\[
\boxed{HN=N}.
\]


::: pf-proof

The quotient \(HN/N\) has one element exactly when \(HN=N\).

:::

:::

::: pf-step

Therefore
\[
\boxed{H\subseteq N}.
\]


::: pf-proof

Since
\[
H\subseteq HN=N.
\]

:::

:::

::: pf-step

Since
\[
|H|=|N|,
\]
the inclusion in step <1>9 is equality:
\[
\boxed{H=N}.
\]


::: pf-proof

A finite subgroup contained in another finite group of the same order must equal it.

:::

:::

::: pf-step

Thus \(N\) is the unique subgroup of \(G\) of order \(|N|\).


::: pf-proof

The subgroup \(H\) was arbitrary among subgroups with \(|H|=|N|\), and step <1>10 shows every such \(H\) equals \(N\).

:::

:::

::: pf-qed

Step <1>11 is the required uniqueness statement.

:::

:::
