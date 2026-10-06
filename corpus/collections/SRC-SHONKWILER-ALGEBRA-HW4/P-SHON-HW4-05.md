---
schema: qual/card@1
id: P-SHON-HW4-05
kind: problem
title: A composition series for $A_4$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against exercise 3.5.10 in the retained Algebra HW 4 solution packet.
---

::: {.problem}
Find a composition series for $A_4$.
Deduce that $A_4$ is solvable.
:::

::: {.solution}
Let
\[
V_4=
\{1,(12)(34),(13)(24),(14)(23)\}
\subseteq A_4.
\]

<1>1. The set \(V_4\) is a subgroup of \(A_4\).

::: {.proof}
Each nonidentity element has order \(2\), and the product of any two distinct nonidentity double transpositions is the third. Thus \(V_4\) is closed under multiplication and inverses.
:::

<1>2. The subgroup \(V_4\) is normal in \(A_4\).

::: {.proof}
Conjugation preserves cycle type. The three nonidentity elements of \(V_4\) are exactly the double transpositions in \(A_4\), so conjugating any element of \(V_4\) by an element of \(A_4\) remains in \(V_4\).
:::

<1>3. Let
\[
H=\langle(12)(34)\rangle
=
\{1,(12)(34)\}.
\]
Then
\[
\boxed{H\triangleleft V_4}.
\]

::: {.proof}
The group \(V_4\) is abelian, so every subgroup is normal.
:::

<1>4. Therefore
\[
\boxed{
1\triangleleft H\triangleleft V_4\triangleleft A_4}
\]
is a subnormal series.

::: {.proof}
Normality of \(H\) in \(V_4\) is step <1>3, and normality of \(V_4\) in \(A_4\) is step <1>2.
:::

<1>5. The first factor is
\[
\boxed{
H/1\cong C_2}.
\]

::: {.proof}
The group \(H\) has order \(2\).
:::

<1>6. The second factor is
\[
\boxed{
V_4/H\cong C_2}.
\]

::: {.proof}
\[
|V_4/H|
=
\frac4{2}
=
2.
\]
Every group of order \(2\) is cyclic.
:::

<1>7. The third factor is
\[
\boxed{
A_4/V_4\cong C_3}.
\]

::: {.proof}
\[
|A_4/V_4|
=
\frac{12}{4}
=
3.
\]
Every group of prime order is cyclic.
:::

<1>8. Each factor in steps <1>5--<1>7 is simple.

::: {.proof}
Each has prime order.
:::

<1>9. Hence
\[
\boxed{
1\triangleleft
\langle(12)(34)\rangle
\triangleleft
V_4
\triangleleft
A_4}
\]
is a composition series.

::: {.proof}
Step <1>4 gives a subnormal series, and step <1>8 shows all successive quotients are simple.
:::

<1>10. All composition factors are abelian.

::: {.proof}
They are
\[
C_2,\ C_2,\ C_3
\]
by steps <1>5--<1>7.
:::

<1>11. Therefore
\[
\boxed{A_4\text{ is solvable}}.
\]

::: {.proof}
A finite group is solvable if it has a subnormal series with abelian factors. The composition series in step <1>9 has abelian factors by step <1>10.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>9 gives the requested composition series and step <1>11 gives solvability.
:::
:::
