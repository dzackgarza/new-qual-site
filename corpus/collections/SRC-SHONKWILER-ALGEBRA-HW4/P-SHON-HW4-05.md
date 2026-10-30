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
$$
V_4=
\{1,(12)(34),(13)(24),(14)(23)\}
\subseteq A_4.
$$

::: pf

::: pf-step

The set $V_4$ is a subgroup of $A_4$.


::: pf-proof

Each nonidentity element has order $2$, and the product of any two distinct nonidentity double transpositions is the third. Thus $V_4$ is closed under multiplication and inverses.

:::

:::

::: {.pf-step #s1-2}

The subgroup $V_4$ is normal in $A_4$.


::: pf-proof

Conjugation preserves cycle type. The three nonidentity elements of $V_4$ are exactly the double transpositions in $A_4$, so conjugating any element of $V_4$ by an element of $A_4$ remains in $V_4$.

:::

:::

::: {.pf-step #s1-3}

Let
$$
H=\langle(12)(34)\rangle
=
\{1,(12)(34)\}.
$$
Then
$$
\boxed{H\triangleleft V_4}.
$$


::: pf-proof

The group $V_4$ is abelian, so every subgroup is normal.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
1\triangleleft H\triangleleft V_4\triangleleft A_4}
$$
is a subnormal series.


::: pf-proof

Normality of $H$ in $V_4$ is step [](#s1-3){.pf-ref}, and normality of $V_4$ in $A_4$ is step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

The first factor is
$$
\boxed{
H/1\cong C_2}.
$$


::: pf-proof

The group $H$ has order $2$.

:::

:::

::: {.pf-step #s1-6}

The second factor is
$$
\boxed{
V_4/H\cong C_2}.
$$


::: pf-proof

$$
\cardinality{V_4/H}
=
\frac4{2}
=
2.
$$
Every group of order $2$ is cyclic.

:::

:::

::: {.pf-step #s1-7}

The third factor is
$$
\boxed{
A_4/V_4\cong C_3}.
$$


::: pf-proof

$$
\cardinality{A_4/V_4}
=
\frac{12}{4}
=
3.
$$
Every group of prime order is cyclic.

:::

:::

::: {.pf-step #s1-8}

Each factor in steps [](#s1-5){.pf-ref} through [](#s1-7){.pf-ref} is simple.


::: pf-proof

Each has prime order.

:::

:::

::: {.pf-step #s1-9}

Hence
$$
\boxed{
1\triangleleft
\langle(12)(34)\rangle
\triangleleft
V_4
\triangleleft
A_4}
$$
is a composition series.


::: pf-proof

Step [](#s1-4){.pf-ref} gives a subnormal series, and step [](#s1-8){.pf-ref} shows all successive quotients are simple.

:::

:::

::: {.pf-step #s1-10}

All composition factors are abelian.


::: pf-proof

They are
$$
C_2,\ C_2,\ C_3
$$
by steps [](#s1-5){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
\boxed{A_4\text{ is solvable}}.
$$


::: pf-proof

A finite group is solvable if it has a subnormal series with abelian factors. The composition series in step [](#s1-9){.pf-ref} has abelian factors by step [](#s1-10){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} gives the requested composition series and step [](#s1-11){.pf-ref} gives solvability.

:::

:::

:::
