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

::: {.solution}
Let
\[
H\le G
\]
be any subgroup with
\[
|H|=|N|.
\]

<1>1. Since
\[
N\triangleleft G,
\]
the product
\[
HN
\]
is a subgroup of \(G\).

::: {.proof}
If \(N\) is normal, then for \(h_1n_1,h_2n_2\in HN\),
\[
(h_1n_1)(h_2n_2)
=
h_1h_2(h_2^{-1}n_1h_2)n_2\in HN,
\]
and inverses are handled similarly. Thus \(HN\le G\).
:::

<1>2. The second isomorphism theorem gives
\[
\boxed{
HN/N\cong H/(H\cap N)}.
\]

::: {.proof}
For \(H\le G\) and \(N\triangleleft G\), the map
\[
H\to HN/N,
\qquad
h\mapsto hN,
\]
is surjective with kernel \(H\cap N\).
:::

<1>3. Therefore
\[
\boxed{
|HN/N|
=
[H:H\cap N]}.
\]

::: {.proof}
Take orders in the finite-group isomorphism from step <1>2.
:::

<1>4. The integer
\[
|HN/N|
\]
divides
\[
[G:N].
\]

::: {.proof}
Since
\[
N\le HN\le G,
\]
the quotient \(HN/N\) is a subgroup of \(G/N\). By Lagrange's theorem,
\[
|HN/N|\mid|G/N|=[G:N].
\]
:::

<1>5. The integer
\[
|HN/N|
\]
also divides \(|H|\).

::: {.proof}
By step <1>3,
\[
|HN/N|=[H:H\cap N],
\]
and every subgroup index divides the group order in a finite group.
:::

<1>6. Since
\[
|H|=|N|,
\]
one has
\[
\boxed{
|HN/N|\mid|N|}.
\]

::: {.proof}
Substitute the given equality into step <1>5.
:::

<1>7. By the coprimality hypothesis,
\[
\boxed{
|HN/N|=1}.
\]

::: {.proof}
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

<1>8. Hence
\[
\boxed{HN=N}.
\]

::: {.proof}
The quotient \(HN/N\) has one element exactly when \(HN=N\).
:::

<1>9. Therefore
\[
\boxed{H\subseteq N}.
\]

::: {.proof}
Since
\[
H\subseteq HN=N.
\]
:::

<1>10. Since
\[
|H|=|N|,
\]
the inclusion in step <1>9 is equality:
\[
\boxed{H=N}.
\]

::: {.proof}
A finite subgroup contained in another finite group of the same order must equal it.
:::

<1>11. Thus \(N\) is the unique subgroup of \(G\) of order \(|N|\).

::: {.proof}
The subgroup \(H\) was arbitrary among subgroups with \(|H|=|N|\), and step <1>10 shows every such \(H\) equals \(N\).
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>11 is the required uniqueness statement.
:::
:::
