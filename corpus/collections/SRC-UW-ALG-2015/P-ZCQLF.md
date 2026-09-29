---
schema: qual/card@1
id: P-ZCQLF
kind: problem
title: The number of intermediate fields of a degree-$4$ Galois extension, and of
  a degree-$4$ separable extension
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
- Let $L$ be a Galois extension of a field $K$ of degree 4. What is the minimum number of subfields there could be strictly between $K$ and $L$?
  What is the maximum number of such subfields?
  Give examples where these bounds are attained.

- How do these numbers change if we assume only that $L$ is separable (but not necessarily Galois) over $K$?
:::


::: {.solution}

::: pf

::: pf-step
If \(L/K\) is Galois of degree \(4\), then
\[
\operatorname{Gal}(L/K)\cong C_4
\quad\text{or}\quad
C_2\times C_2.
\]

:::

::: {.pf-step #s2}
In the cyclic case \(C_4\), there is exactly one field strictly between \(K\) and \(L\).

::: pf-proof
By the Galois correspondence, proper intermediate fields correspond to proper nontrivial subgroups of \(C_4\). A cyclic group of order \(4\) has exactly one such subgroup, namely its unique subgroup of order \(2\).
:::

:::

::: {.pf-step #s3}
In the Klein-four case \(C_2\times C_2\), there are exactly three fields strictly between \(K\) and \(L\).

::: pf-proof
The Klein four group has exactly three proper nontrivial subgroups, all of order \(2\). Galois correspondence therefore gives exactly three intermediate quadratic fields.
:::

:::

::: {.pf-step #s4}
Thus, among Galois quartic extensions, the minimum number of proper intermediate fields is \(1\) and the maximum is \(3\).

::: pf-proof
The bounds follow from step [](#s2){.pf-ref} and step [](#s3){.pf-ref}. They are attained, for example, by
\[
\mathbb Q(\zeta_5)/\mathbb Q,
\]
whose Galois group is \((\mathbb Z/5\mathbb Z)^\times\cong C_4\), and by
\[
\mathbb Q(\sqrt2,\sqrt3)/\mathbb Q,
\]
whose Galois group is \(C_2\times C_2\).
:::

:::

::: {.pf-step #s5}
For any separable extension \(L/K\) of degree \(4\), every proper intermediate field has degree \(2\) over \(K\).

::: pf-proof
If \(K\subsetneq F\subsetneq L\), then by the tower law
\[
4=[L:K]=[L:F][F:K].
\]
Both factors are integers greater than \(1\), so both equal \(2\).
:::

:::

::: {.pf-step #s6}
A separable quartic extension has at most three proper intermediate fields.

::: pf-proof
Suppose \(F_1
e F_2\) are two intermediate fields. By step [](#s5){.pf-ref} each is quadratic over \(K\), hence separable and therefore Galois over \(K\). Their compositum lies in \(L\), and since \(F_1\ne F_2\),
\[
[F_1F_2:K]=4.
\]
Thus \(F_1F_2=L\). A compositum of Galois extensions is Galois, so \(L/K\) is then Galois. By step [](#s3){.pf-ref}, a Galois quartic with more than one intermediate field has exactly three. Hence no separable quartic can have more than three.
:::

:::

::: {.pf-step #s7}
The minimum under the assumption “separable, not necessarily Galois” is \(0\).

::: pf-proof
Let \(\alpha\) be a root of
\[
f(x)=x^4-x-1\in\mathbb Q[x],
\]
and put \(L=\mathbb Q(\alpha)\). The reduction modulo \(2\) is \(x^4+x+1\), which is irreducible over \(\mathbb F_2\); hence \(f\) is irreducible over \(\mathbb Q\), so \([L:\mathbb Q]=4\).

Let \(N\) be the splitting field of \(f\). The factorization modulo \(2\) is irreducible, so the Galois group of \(N/\mathbb Q\) contains a \(4\)-cycle. Modulo \(7\),
\[
f(x)\equiv (x-3)(x^3+3x^2+2x-2),
\]
and the cubic factor has no root in \(\mathbb F_7\), so the group contains a \(3\)-cycle. Modulo \(17\),
\[
f(x)\equiv (x+2)(x+5)(x^2-7x+5),
\]
and the quadratic factor is irreducible because its discriminant \(29\equiv12\pmod{17}\) is not a square, so the group contains a transposition. A transitive subgroup of \(S_4\) containing a \(4\)-cycle, a \(3\)-cycle, and a transposition is \(S_4\). Hence
\[
\operatorname{Gal}(N/\mathbb Q)\cong S_4.
\]
The subgroup fixing \(\alpha\) is a point stabilizer \(S_3\), which is maximal in \(S_4\). By the Galois correspondence for \(N/\mathbb Q\), intermediate fields between \(\mathbb Q\) and \(L=N^{S_3}\) correspond to subgroups between \(S_3\) and \(S_4\). Since there are none, \(L/\mathbb Q\) has no proper intermediate fields.
:::

:::

::: pf-step
Therefore, among all separable quartic extensions, the minimum number of proper intermediate fields is \(0\) and the maximum is \(3\).

::: pf-proof
The upper bound is step [](#s6){.pf-ref}, the example in step [](#s7){.pf-ref} attains \(0\), and the biquadratic example in step [](#s4){.pf-ref} attains \(3\).

If one restricts specifically to separable quartic extensions that are not Galois, then step [](#s6){.pf-ref} shows there can be at most one intermediate field. Both possibilities occur: step [](#s7){.pf-ref} gives none, while \(\mathbb Q(\sqrt[4]{2})/\mathbb Q\) has the intermediate field \(\mathbb Q(\sqrt2)\), and cannot have a second one because two distinct quadratic intermediate fields would make the quartic extension Galois.
:::

:::

:::

:::
