---
schema: qual/card@1
id: P-5JTV2
kind: problem
title: A covering with compact total space is finite-sheeted of degree $[\pi_1(Y):p_*\pi_1(X)]$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 3 of the official UGA Spring 2019 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified finiteness directly from compactness and local covering charts, and the cardinality formula from the transitive monodromy action and its stabilizer.
---

::: problem
Let
\[
p:X\longrightarrow Y
\]
be a covering space, where $X$ is compact, path connected, and locally path connected.
Prove that for each $x\in X$ the set
\[
p^{-1}(\{p(x)\})
\]
is finite, and has cardinality equal to the index of
\[
p_*\bigl(\pi_1(X,x)\bigr)
\]
in
\[
\pi_1(Y,p(x)).
\]
:::

::: {.solution}
Fix $x_0\in X$ and write
\[
y_0=p(x_0),
\qquad
F=p^{-1}(\{y_0\}).
\]

<1>1. Every point $z\in X$ has an open neighborhood $V_z$ containing at most one point of $F$.
::: {.proof}
Because $p$ is a covering map, there is an evenly covered open neighborhood
\[
U\subseteq Y
\]
of $p(z)$ and a sheet
\[
V_z\subseteq p^{-1}(U)
\]
containing $z$ such that
\[
p|_{V_z}:V_z\longrightarrow U
\]
is a homeomorphism.
In particular, $p|_{V_z}$ is injective.
All points of $F$ have the same image $y_0$, so $V_z$ can contain at most one point of $F$.
:::

<1>2. The fiber $F$ is finite.
::: {.proof}
The neighborhoods $V_z$ from <1>1 form an open cover of the compact space $X$.
Choose a finite subcover
\[
X=V_{z_1}\cup\cdots\cup V_{z_m}.
\]
Each $V_{z_i}$ contains at most one point of $F$.
Therefore
\[
|F|\le m,
\]
so $F$ is finite.
:::

<1>3. The group
\[
G=\pi_1(Y,y_0)
\]
acts on the fiber $F$ by monodromy.
::: {.proof}
For $z\in F$ and $[\gamma]\in G$, let
\[
\widetilde\gamma_z:[0,1]\longrightarrow X
\]
be the unique lift of $\gamma$ with
\[
\widetilde\gamma_z(0)=z.
\]
Since $\gamma(1)=y_0$, its endpoint also lies in $F$.
Define
\[
z\cdot[\gamma]=\widetilde\gamma_z(1).
\]
The homotopy lifting property shows that the endpoint depends only on the homotopy class $[\gamma]$, and uniqueness of path lifting gives the identity and composition laws.
Thus this is a right action of $G$ on $F$.
:::

<1>4. The monodromy action is transitive.
::: {.proof}
Let $z\in F$.
Since $X$ is path connected, choose a path
\[
\alpha:[0,1]\longrightarrow X
\]
from $x_0$ to $z$.
Then
\[
\gamma=p\circ\alpha
\]
is a loop at $y_0$.
The path $\alpha$ is the lift of $\gamma$ starting at $x_0$, so
\[
x_0\cdot[\gamma]=z.
\]
Hence every point of $F$ lies in the orbit of $x_0$.
:::

<1>5. The stabilizer of $x_0$ under this action is exactly
\[
H=p_*\bigl(\pi_1(X,x_0)\bigr).
\]
::: {.proof}
First let
\[
[\gamma]\in H.
\]
Then there is a loop $\alpha$ at $x_0$ such that
\[
[\gamma]=p_*[\alpha]=[p\circ\alpha].
\]
The lift of $p\circ\alpha$ beginning at $x_0$ is $\alpha$, which ends at $x_0$.
Homotopy lifting therefore gives
\[
x_0\cdot[\gamma]=x_0.
\]
Thus $H$ is contained in the stabilizer.

Conversely, suppose
\[
x_0\cdot[\gamma]=x_0.
\]
The lift $\widetilde\gamma_{x_0}$ is then a loop at $x_0$ and satisfies
\[
p\circ\widetilde\gamma_{x_0}=\gamma.
\]
Consequently
\[
[\gamma]
=p_*[\widetilde\gamma_{x_0}]
\in H.
\]
Thus the stabilizer is precisely $H$.
:::

<1>6. The fiber cardinality is the subgroup index:
\[
\bigl|p^{-1}(\{p(x_0)\})\bigr|
=
\left[
\pi_1(Y,p(x_0)):
 p_*\bigl(\pi_1(X,x_0)\bigr)
\right].
\]
::: {.proof}
For a transitive group action, the orbit of a point is in bijection with the cosets of its stabilizer.
By <1>4 the orbit of $x_0$ is all of $F$, and by <1>5 its stabilizer is
\[
p_*\bigl(\pi_1(X,x_0)\bigr).
\]
Hence orbit--stabilizer gives the displayed equality.
Together with <1>2, this index is finite.
Since $x_0$ was arbitrary, the statement holds for every $x\in X$.
:::
:::
