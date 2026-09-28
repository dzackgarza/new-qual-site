---
schema: qual/card@1
id: P-BKS81-2
kind: problem
title: A nilpotent Jordan chain is linearly independent
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the minimal-index coefficient argument and the use of T^m x=0 to annihilate all higher terms.
---

::: {.problem}
Let $T:V\to V$ be linear. Suppose $x\in V$ satisfies
\[
T^m x=0,
\qquad
T^{m-1}x\ne0
\]
for some positive integer $m$.
Show that
\[
x,Tx,\ldots,T^{m-1}x
\]
are linearly independent.
:::

::: {.solution}
<1>1. Any relation
$$
a_0x+a_1Tx+\cdots+a_{m-1}T^{m-1}x=0
$$
has all coefficients equal to zero.

::: {.proof}
Suppose instead that some coefficient is nonzero, and let $r$ be the least
index such that $a_r\ne0$. Apply $T^{m-1-r}$ to the displayed relation.
All terms with index less than $r$ vanish because their coefficients are
zero. The term with index $r$ becomes
$$
a_rT^{m-1}x.
$$
For every $j>r$, the corresponding term becomes
$$
a_jT^{m-1-r+j}x,
$$
whose exponent is at least $m$; it vanishes because $T^m x=0$. Hence
$$
a_rT^{m-1}x=0.
$$
Since $a_r\ne0$ and the scalars form a field, this implies
$T^{m-1}x=0$, contrary to the hypothesis.
:::

<1>2. Therefore
$$
\boxed{x,Tx,\ldots,T^{m-1}x\text{ are linearly independent}.}
$$

::: {.proof}
By step <1>1, the only linear relation among these vectors is the trivial
one.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 is the required conclusion.
:::
:::
