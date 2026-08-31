---
schema: qual/card@1
id: P-ALGS08G
kind: problem
title: "A simple ring with a minimal right ideal satisfies the minimum condition"
classification:
  areas:
  - algebra
  topics:
  - Ring Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $A$ be a simple ring with identity element.
Show that if $A$ has a minimal right ideal, then $A$ satisfies the minimum condition for right ideals.
:::

::: {.solution}
**Goal.** For a simple ring $A$ with identity and a minimal right ideal, show $A$ satisfies the descending chain condition (minimum condition) on right ideals.

<1>1. A minimal right ideal $I$ of $A$ is a simple right $A$-module.
::: {.proof}
a minimal right ideal has no nonzero proper submodule (submodule = right ideal contained in it).
:::

<1>2. $A$ is a direct sum of minimal right ideals.
<2>1. The sum of all right ideals isomorphic to $I$ is a two-sided ideal.
::: {.proof}
the sum of all right ideals isomorphic to a fixed simple module is a two-sided ideal (it is closed under left multiplication, since $aI \cong I$ for any $a \in A$).
:::
<2>2. This two-sided ideal is nonzero, hence equals $A$ (since $A$ is simple).
::: {.proof}
it contains $I \neq 0$, and $A$ is simple.
:::
<2>3. Hence $A$ is a sum of minimal right ideals, each isomorphic to $I$.
::: {.proof}
by <1>2.2, $A$ is the sum of right ideals isomorphic to $I$.
:::

<1>3. $A$ is a finite direct sum of minimal right ideals.
<2>1. The identity $1$ lies in a finite sum of these minimal right ideals.
::: {.proof}
$1 \in A = \sum_j I_j$, and $1$ is a finite sum of elements from finitely many $I_j$'s.
:::
<2>2. Hence $A = I_1 \oplus \cdots \oplus I_m$ for finitely many minimal right ideals $I_j$.
::: {.proof}
$1 \in I_1 + \cdots + I_m$ implies $A = A \cdot 1 \subseteq I_1 + \cdots + I_m \subseteq A$.
:::

<1>4. $A$ satisfies the minimum condition on right ideals.
<2>1. $A$ is a finite direct sum of simple right modules, hence is semisimple (Artinian).
::: {.proof}
a finite direct sum of simple modules is Artinian.
:::
<2>2. An Artinian module satisfies the descending chain condition on submodules.
::: {.proof}
this is the definition of Artinian.
:::
<2>3. Hence $A$ satisfies the minimum condition on right ideals.
::: {.proof}
right ideals of $A$ are exactly the submodules of the right $A$-module $A$.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.3 is the claim.
:::
:::
