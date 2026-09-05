---
schema: qual/card@1
id: P-6XN3Z
kind: problem
title: Whether the covering $S^2\to\RP^2$ is null-homotopic
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Homotopy
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 6 of the official UGA Spring 2006 topology exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Replaced the skeletal higher-homotopy argument by the covering-homotopy
    proof: a nullhomotopy would lift to a nullhomotopy of id_{S^2}, contradicting
    its action on H_2. Homotopy lifting is Hatcher, Algebraic Topology,
    Proposition 1.30.
---

::: problem
Let $S^2 \to \RP^2$ be the universal covering map.

Is this map null-homotopic?
Give a proof of your answer.
:::

::: {.solution}
<1>1. Suppose, for contradiction, that the universal covering map
\[
p:S^2\longrightarrow\RP^2
\]
is nullhomotopic.
Then there is a homotopy
\[
H:S^2\times I\longrightarrow\RP^2
\]
with
\[
H(x,0)=p(x)
\qquad\text{and}\qquad
H(x,1)=y_0
\]
for some $y_0\in\RP^2$.
::: {.proof}
This is the definition of nullhomotopy.
:::

<1>2. The homotopy $H$ lifts through $p$ to
\[
\widetilde H:S^2\times I\longrightarrow S^2
\]
with
\[
\widetilde H(x,0)=x
\qquad\text{and}\qquad
p\circ\widetilde H=H.
\]
::: {.proof}
At time $0$, the identity map $\id_{S^2}$ is a lift of $H(-,0)=p$, since
\[
p\circ\id_{S^2}=p.
\]
The homotopy lifting property for covering maps therefore gives the stated lift beginning at $\id_{S^2}$.
:::

<1>3. The terminal map
\[
\widetilde H_1:S^2\longrightarrow S^2
\]
is constant.
::: {.proof}
From <1>1--<1>2,
\[
p(\widetilde H(x,1))=H(x,1)=y_0
\]
for every $x\in S^2$.
Thus
\[
\widetilde H_1(S^2)\subseteq p^{-1}(y_0).
\]
The fiber of the double covering $p$ consists of two antipodal points and is therefore discrete.
Since $S^2$ is connected, its continuous image in a discrete space is a singleton.
Hence $\widetilde H_1$ is constant.
:::

<1>4. This contradicts the homology of $S^2$.
::: {.proof}
By <1>2--<1>3, the identity map of $S^2$ is homotopic to a constant map.
Homotopic maps induce the same map on integral homology.
But on
\[
H_2(S^2;\ZZ)\cong\ZZ,
\]
the identity induces the identity homomorphism, whereas a constant map factors through a point and therefore induces the zero homomorphism in degree $2$.
This is impossible.
:::

<1>5. Therefore
\[
\boxed{p:S^2\longrightarrow\RP^2\text{ is not nullhomotopic}.}
\]
::: {.proof}
The assumption in <1>1 led to the contradiction in <1>4.
:::
:::
