---
schema: qual/card@1
id: P-KSRING17-137
kind: problem
title: The Jacobson radical of a right Artinian ring is nilpotent
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 137 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a ring satisfying the descending chain condition on right ideals.
If J(R) denotes the Jacobson radical of R, prove that J(R) is nilpotent.
:::

::: {.solution}
Write
$$
J
\coloneqq
J(R).
$$

<1>1. The descending chain
$$
J
\supseteq
J^2
\supseteq
J^3
\supseteq
\cdots
$$
stabilizes.

::: {.proof}
Each
$$
J^n
$$
is a right ideal of $R$.
By the descending chain condition on right ideals, there exists
$$
n\ge1
$$
such that
$$
J^n
=
J^{n+1}
=
J^{n+2}
=
\cdots.
$$
:::

<1>2. Set
$$
A
\coloneqq
J^n.
$$
Then
$$
A
=
AJ.
$$

::: {.proof}
By step <1>1,
$$
J^n
=
J^{n+1}.
$$
But
$$
J^{n+1}
=
J^nJ.
$$
Hence
$$
A=AJ.
$$
:::

<1>3. Suppose, for contradiction, that
$$
A\ne0.
$$
Then there exists a right ideal
$$
C
$$
minimal among the right ideals satisfying
$$
CA\ne0.
$$

::: {.proof}
The collection is nonempty because
$$
RA=A\ne0.
$$
The descending chain condition implies that every nonempty collection of right ideals has a minimal element under inclusion.
Choose such a minimal right ideal and call it $C$.
:::

<1>4. There exists
$$
c\in C
$$
such that
$$
cA\ne0.
$$

::: {.proof}
The condition
$$
CA\ne0
$$
means some finite sum of products
$$
ca
$$
with
$$
c\in C,
\qquad
a\in A
$$
is nonzero.
In particular, at least one such product is nonzero.
Choose $c$ with
$$
cA\ne0.
$$
:::

<1>5. The set
$$
cA
$$
is a nonzero right ideal contained in $C$.

::: {.proof}
Since $A$ is a two-sided ideal,
$$
cA
$$
is a right ideal:
for
$$
ca_1,ca_2\in cA,
$$
their difference is
$$
c(a_1-a_2)\in cA,
$$
and for
$$
r\in R,
$$
$$
(ca_1)r
=
c(a_1r)
\in
cA
$$
because
$$
a_1r\in A.
$$

Also
$$
cA\subseteq C
$$
because
$$
c\in C
$$
and $C$ is a right ideal.
It is nonzero by step <1>4.
:::

<1>6. One has
$$
(cA)A\ne0.
$$

::: {.proof}
By step <1>2,
$$
A=AJ.
$$
Multiplying on the left by $c$ gives
$$
cA
=
cAJ.
$$
Since
$$
cA\ne0,
$$
the right side is nonzero.
Because
$$
J^n=A
$$
and
$$
AJ=A,
$$
one also has
$$
A^2
=
J^{2n}
=
A
$$
after stabilization.
Hence
$$
(cA)A
=
cA^2
=
cA
\ne0.
$$
:::

<1>7. By minimality of $C$,
$$
cA=C.
$$

::: {.proof}
Step <1>5 gives a nonzero right ideal
$$
cA
\subseteq
C.
$$
Step <1>6 shows
$$
(cA)A\ne0.
$$
Thus $cA$ belongs to the collection of right ideals used in step <1>3.
Minimality of $C$ forces
$$
cA=C.
$$
:::

<1>8. Since
$$
c\in C=cA,
$$
there exists
$$
a\in A
$$
such that
$$
c=ca.
$$

::: {.proof}
Membership
$$
c\in cA
$$
means precisely that
$$
c=ca
$$
for some
$$
a\in A.
$$
:::

<1>9. The element
$$
1-a
$$
is a unit of $R$.

::: {.proof}
Since
$$
A=J^n
\subseteq
J,
$$
one has
$$
a\in J(R).
$$
A defining property of the Jacobson radical is that
$$
1-j
$$
is invertible for every
$$
j\in J(R).
$$
Therefore
$$
1-a
$$
is a unit.
:::

<1>10. The equality
$$
c=ca
$$
forces
$$
c=0.
$$

::: {.proof}
Rearranging step <1>8 gives
$$
c(1-a)=0.
$$
By step <1>9,
$$
1-a
$$
is invertible.
Multiplying on the right by
$$
(1-a)^{-1}
$$
gives
$$
c=0.
$$
:::

<1>11. This contradicts
$$
cA\ne0.
$$

::: {.proof}
If
$$
c=0,
$$
then
$$
cA=0,
$$
contrary to the choice of $c$ in step <1>4.
:::

<1>12. Therefore
$$
A=0.
$$

::: {.proof}
The assumption
$$
A\ne0
$$
leads to the contradiction in step <1>11.
Hence
$$
A=0.
$$
:::

<1>13. Consequently,
$$
\boxed{
J(R)^n=0
}
$$
for some
$$
n\ge1.
$$

::: {.proof}
By definition,
$$
A=J^n.
$$
Step <1>12 gives
$$
A=0.
$$
Thus
$$
J^n=0.
$$
This is exactly nilpotence of the Jacobson radical.
:::

<1>14. Q.E.D.

::: {.proof}
Step <1>13 is the required conclusion.
:::
:::
