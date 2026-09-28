---
schema: qual/card@1
id: P-ALGPAN11-02
kind: problem
title: Which listed subsets of the reals are subfields
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
---

::: {.problem}
Which of the following subsets $F_i$ of $\mathbb R$, $1\le i\le4$, are subfields of $\mathbb R$?

$F_1=\{a/b:a,b\in\mathbb Z\text{ and }b\text{ is odd}\}$,

$F_2=\{a+b\sqrt2:a,b\in\mathbb Z\}$,

$F_3=\{a+b\sqrt2:a,b\in\mathbb Q\}$,

$F_4=\{a+b\sqrt[4]2:a,b\in\mathbb Q\}$.

![Source scan for this review problem.](../../../assets/attachments/algebra-review-pantano-2011/problem-02.png)
:::

::: {.solution}
Only $F_3$ is a subfield of $\mathbb R$.

<1>1. $F_1$ is not a field.
::: {.proof}
The element $2=2/1$ belongs to $F_1$, but its inverse $1/2$ cannot be written with odd denominator after reduction.
Thus $F_1$ is not closed under inverses of nonzero elements.
:::

<1>2. $F_2$ is not a field.
::: {.proof}
The integer $2$ belongs to $F_2$, whereas $1/2$ does not, since an equality
\[
\frac12=a+b\sqrt2,
\qquad a,b\in\mathbb Z,
\]
would force $b=0$ and then $a=1/2\notin\mathbb Z$.
:::

<1>3. $F_3$ is a field.
::: {.proof}
It is $\mathbb Q(\sqrt2)$.
Addition and multiplication preserve the form $a+b\sqrt2$.
If $a+b\sqrt2\ne0$, then
\[
(a+b\sqrt2)^{-1}=\frac{a-b\sqrt2}{a^2-2b^2}.
\]
The denominator is nonzero (otherwise $a/b=\pm\sqrt2$ when $b\ne0$), and the coefficients of the displayed inverse are rational.
:::

<1>4. $F_4$ is not a field.
::: {.proof}
It contains $\alpha=\sqrt[4]{2}$, but closure under multiplication would require
\[
\alpha^2=\sqrt2=a+b\alpha
\]
for some $a,b\in\mathbb Q$.
This would give the nontrivial $\mathbb Q$-linear relation $\alpha^2-a-b\alpha=0$ among $1,\alpha,\alpha^2$.
But $T^4-2$ is irreducible over $\mathbb Q$ by Eisenstein at $2$, so $1,\alpha,\alpha^2,\alpha^3$ are linearly independent over $\mathbb Q$.
Hence $\sqrt2\notin\operatorname{span}_{\mathbb Q}\{1,\alpha\}$.
:::

Therefore the answer is $\boxed{F_3\text{ only}}$.
:::
