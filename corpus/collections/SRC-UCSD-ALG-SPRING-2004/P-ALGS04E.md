---
schema: qual/card@1
id: P-ALGS04E
kind: problem
title: "Every ideal in a commutative ring is contained in a maximal ideal"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
In a commutative ring with 1, prove that every ideal is contained in a maximal (proper) ideal.
:::

::: {.solution}
<1>1. Interpreted literally with the convention that the unit ideal is an ideal, the statement has the exception \(I=A\). The intended assertion is that every **proper** ideal \(I\subsetneq A\) is contained in a maximal ideal.
::: {.proof}
A maximal ideal is proper by definition, so no maximal ideal can contain the unit ideal \(A\). The standard existence theorem therefore concerns proper ideals.
:::

<1>2. Fix a proper ideal \(I\subsetneq A\), and let
\[
\mathcal P=\{J\triangleleft A: I\subseteq J\subsetneq A\},
\]
ordered by inclusion.
Then \(\mathcal P\) is nonempty.
::: {.proof}
The ideal \(I\) itself belongs to \(\mathcal P\).
:::

<1>3. Every chain \(\mathcal C\subseteq\mathcal P\) has an upper bound in \(\mathcal P\), namely
\[
U=\bigcup_{J\in\mathcal C}J.
\]
::: {.proof}
Because \(\mathcal C\) is totally ordered by inclusion, the union \(U\) is an ideal: if \(x,y\in U\), then \(x\in J_1\) and \(y\in J_2\) for some \(J_1,J_2\in\mathcal C\); one of these ideals contains the other, hence contains both \(x\) and \(y\), so \(x-y\in U\). Also \(ax\in U\) for every \(a\in A\).

Moreover \(I\subseteq U\). Finally, \(U\ne A\): if \(1\in U\), then \(1\in J\) for some \(J\in\mathcal C\), contradicting \(J\subsetneq A\). Thus \(U\in\mathcal P\).
:::

<1>4. By Zorn's lemma, \(\mathcal P\) has a maximal element \(M\).
::: {.proof}
By <1>3, every chain in \(\mathcal P\) has an upper bound in \(\mathcal P\). Zorn's lemma therefore applies.
:::

<1>5. The ideal \(M\) is a maximal ideal of \(A\), and \(I\subseteq M\).
::: {.proof}
By definition of \(\mathcal P\), \(I\subseteq M\subsetneq A\). Suppose
\[
M\subsetneq J\subsetneq A
\]
for an ideal \(J\). Then \(J\in\mathcal P\), contradicting maximality of \(M\) in \(\mathcal P\). Hence no proper ideal strictly contains \(M\), so \(M\) is maximal.
:::
:::
