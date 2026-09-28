---
schema: qual/card@1
id: P-4HGM3
kind: problem
title: Groups of order 8
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Classify all groups of order 8.
:::

::: {.solution}
Let $G$ have order $8$.

If $G$ is abelian, the classification of finite abelian groups gives exactly
\[
\mathbb Z/8,\qquad \mathbb Z/4\times\mathbb Z/2,\qquad (\mathbb Z/2)^3.
\]

Assume $G$ is nonabelian. Then $G$ has an element $r$ of order $4$: if every nonidentity element had order $2$, then for all $x,y$,
\[
(xy)^{-1}=xy,
\]
while also $(xy)^{-1}=y^{-1}x^{-1}=yx$, so $xy=yx$.
Thus $H=\langle r\rangle$ has order $4$ and index $2$, hence is normal. Choose $s\notin H$. Then $G=H\sqcup sH$, and conjugation by $s$ induces an automorphism of $H\cong C_4$. Since $G$ is nonabelian, this automorphism is nontrivial, so
\[
srs^{-1}=r^{-1}.
\]
Also $s^2\in H$. Since $s$ commutes with its own square, $s^2$ cannot be $r$ or $r^3$: either equality would force $s$ to commute with $r$, contradicting $srs^{-1}=r^{-1}\ne r$. Hence
\[
s^2\in\{1,r^2\}.
\]

If $s^2=1$, then
\[
G\cong \langle r,s\mid r^4=s^2=1,\ srs^{-1}=r^{-1}\rangle,
\]
the dihedral group of order $8$.
If $s^2=r^2$, then
\[
G\cong \langle r,s\mid r^4=1,\ s^2=r^2,\ srs^{-1}=r^{-1}\rangle,
\]
which is $Q_8$.

Hence the five groups of order $8$ are
\[
\mathbb Z/8,\quad \mathbb Z/4\times\mathbb Z/2,\quad (\mathbb Z/2)^3,\quad D_8,\quad Q_8,
\]
where $D_8$ denotes the dihedral group of order $8$.
:::
