---
schema: qual/card@1
id: E-AMD-BKDDOBZG
kind: exercise
title: An ideal containing a unit is the whole ring
classification:
  areas:
  - algebra
  topics:
  - ideals
  - rings
relations: []
review: draft
solved: true
---

::: {.exercise}
Show that if an ideal $I\normal R$ contains a unit then $I = R$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $R$ be a ring with identity $1 \neq 0$, and let $I \trianglelefteq R$ be an ideal (left, right, or two-sided).
Suppose $I$ contains a unit $u \in R^\times$.
Prove that $I = R$.

<1>1. Definitions: <2>1. A unit in $R$ is an element $u \in R$ for which there exists an element $u^{-1} \in R$ such that $u u^{-1} = u^{-1} u = 1$.
Proof: Standard definition of a unit in a ring with unity.
<2>2. A left (resp.
right, two-sided) ideal $I$ of $R$ satisfies $r x \in I$ (resp.
$x r \in I$) for all $x \in I$ and all $r \in R$.
Proof: Standard definition of an ideal.

<1>2. Proof that $1 \in I$: <2>1. By hypothesis, there exists $u \in I$ such that $u \in R^\times$.
Proof: Hypothesis.
<2>2. Since $u \in R^\times$, there exists $u^{-1} \in R$.
Proof: By <1>1.<2>1. <2>3. Since $u \in I$ and $u^{-1} \in R$, by the absorption property of ideals, $1 = u^{-1} u \in I$ (for left ideals) and $1 = u u^{-1} \in I$ (for right ideals).
Proof: By <1>1.<2>2 with $x = u \in I$ and $r = u^{-1} \in R$.

<1>3. Proof that $I = R$: <2>1. Since $I$ is an ideal of $R$, by definition $I \subseteq R$.
Proof: An ideal is by definition a subset of $R$.
<2>2. Let $r \in R$ be an arbitrary element.
Proof: Setting an element to prove $R \subseteq I$.
<2>3. Since $1 \in I$ (<1>2.<2>3), by absorption $r = r \cdot 1 \in I$.
Proof: By <1>1.<2>2 with $x = 1 \in I$ and ring element $r \in R$.
<2>4. Thus $R \subseteq I$.
Proof: Since $r \in I$ for every $r \in R$.
<2>5. Since $I \subseteq R$ and $R \subseteq I$, we have $I = R$.
Proof: Mutual subset inclusion.

<1>4. Conclusion: Any ideal containing a unit is the entire ring.
Proof: By <1>3.
:::
