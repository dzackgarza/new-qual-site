---
schema: qual/card@1
id: P-OMOPR
kind: problem
title: Every continuous map $\RP^2\to S^1$ is homotopic to a constant
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Homotopy
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked the statement and covering-space hint against problem 5 of the official UGA Fall 2014 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Verified the lifting-criterion proof using pi_1(RP^2)=Z/2, pi_1(S^1)=Z, and the universal cover R to S^1.
---

::: problem
Prove that every continuous map $f : \RP^2 \to S^1$ is homotopic to a constant.

> Hint: think about covering spaces.
:::

::: {.solution}
<1>1. The induced homomorphism
\[
f_*:\pi_1(\mathbb{RP}^2,x_0)\to\pi_1(S^1,f(x_0))
\]
is trivial.
::: {.proof}
The fundamental groups are
\[
\pi_1(\mathbb{RP}^2,x_0)\cong\mathbb Z/2
\qquad\text{and}\qquad
\pi_1(S^1,f(x_0))\cong\mathbb Z.
\]
Every group homomorphism
\[
\mathbb Z/2\to\mathbb Z
\]
is trivial: if the nonzero element of $\mathbb Z/2$ maps to $k\in\mathbb Z$, then
\[
2k=0,
\]
and torsion-freeness of $\mathbb Z$ gives $k=0$.
Hence $f_*=0$.
:::

<1>2. The map $f$ lifts to the universal covering
\[
p:\mathbb R\to S^1,
\qquad
p(t)=e^{2\pi i t}.
\]
::: {.proof}
Choose $\widetilde y_0\in\mathbb R$ with
\[
p(\widetilde y_0)=f(x_0).
\]
The covering-space lifting criterion says that a based map
\[
f:(\mathbb{RP}^2,x_0)\to(S^1,f(x_0))
\]
lifts to $(\mathbb R,\widetilde y_0)$ if and only if
\[
f_*\bigl(\pi_1(\mathbb{RP}^2,x_0)\bigr)
\subseteq
p_*\bigl(\pi_1(\mathbb R,\widetilde y_0)\bigr).
\]
By <1>1 the left-hand side is $0$.
Since $\mathbb R$ is simply connected, the right-hand side is also $0$.
Thus the criterion applies and gives a continuous lift
\[
\widetilde f:\mathbb{RP}^2\to\mathbb R
\]
such that
\[
p\circ\widetilde f=f.
\]
:::

<1>3. The lift $\widetilde f$ is homotopic to a constant map.
::: {.proof}
The real line is contractible.
For example, fixing $c=\widetilde f(x_0)$, define
\[
\widetilde H(x,t)=(1-t)\widetilde f(x)+tc.
\]
Then $\widetilde H$ is a homotopy from $\widetilde f$ to the constant map $x\mapsto c$.
:::

<1>4. Therefore $f$ is homotopic to a constant map.
::: {.proof}
Compose the homotopy in <1>3 with $p$:
\[
H=p\circ\widetilde H:\mathbb{RP}^2\times[0,1]\to S^1.
\]
At $t=0$,
\[
H(x,0)=p(\widetilde f(x))=f(x),
\]
while at $t=1$,
\[
H(x,1)=p(c),
\]
independent of $x$.
Thus
\[
\boxed{f\simeq\text{constant}}.
\]
:::
:::
