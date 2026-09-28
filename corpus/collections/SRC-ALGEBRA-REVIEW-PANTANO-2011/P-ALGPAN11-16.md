---
schema: qual/card@1
id: P-ALGPAN11-16
kind: problem
title: Endomorphisms of the fourth roots of unity
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
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Statement transcribed from the retained scan problem-16.png (source question 46) in place of the embedded image.
---

::: {.problem}
Let $G$ be the group of complex numbers $\{1,i,-1,-i\}$ under multiplication.
Which of the following statements are true about the homomorphisms of $G$ into itself?

I. $z\mapsto\bar z$ defines one such homomorphism, where $\bar z$ denotes the complex conjugate of $z$.

II. $z\mapsto z^2$ defines one such homomorphism.

III. For every such homomorphism, there is an integer $k$ such that the homomorphism has the form $z\mapsto z^k$.

(A) None (B) II only (C) I and II only (D) II and III only (E) I, II, and III
:::

::: {.solution}
All three assertions are true, so the answer is $\boxed{\text{(E)}}$.

<1>1. Complex conjugation is an endomorphism of $G$.
::: {.proof}
For $z,w\in G$,
\[
\overline{zw}=\bar z\,\bar w,
\]
and conjugation preserves $G$.
Thus $z\mapsto\bar z$ is a homomorphism; on this group it is also $z\mapsto z^{-1}=z^3$.
:::

<1>2. Squaring is an endomorphism.
::: {.proof}
The group $G$ is abelian, so
\[
(zw)^2=z^2w^2.
\]
Hence $z\mapsto z^2$ is a homomorphism $G\to G$.
:::

<1>3. Every endomorphism has the form $z\mapsto z^k$.
::: {.proof}
$G=\langle i\rangle\cong C_4$.
An endomorphism is determined by the image of $i$, and that image may be any element $i^k$ of $G$.
The resulting homomorphism satisfies
\[
\varphi(i^m)=i^{km}=(i^m)^k,
\]
so $\varphi(z)=z^k$ for all $z\in G$.
:::
:::
