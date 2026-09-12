---
schema: qual/card@1
id: E-HAT-1.1-10
kind: problem
title: Explicit homotopy for commuting loops in product spaces
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Product Spaces
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 10; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Gave an explicit square homotopy interpolating between the bottom-right and left-top edge paths.
---

From the isomorphism $\pi_1(X \times Y, (x_0, y_0)) \approx \pi_1(X, x_0) \times \pi_1(Y, y_0)$ it follows that loops in $X \times \{y_0\}$ and $\{x_0\} \times Y$ represent commuting elements of $\pi_1(X \times Y, (x_0, y_0))$.
Construct an explicit homotopy demonstrating this.

::: {.solution}
Let
\[
a:I\to X,
\qquad
b:I\to Y
\]
be loops based at $x_0$ and $y_0$, respectively.
Write
\[
\alpha(t)=(a(t),y_0),
\qquad
\beta(t)=(x_0,b(t)).
\]

<1>1. Define
\[
G:I^2\to X\times Y,
\qquad
G(u,v)=(a(u),b(v)).
\]
::: {.proof}
The map is continuous as the product of the two continuous coordinate maps.
Along the bottom and top edges it traces $\alpha$, while along the left and right edges it traces $\beta$, since $a(0)=a(1)=x_0$ and $b(0)=b(1)=y_0$.
:::

<1>2. Parameterize the bottom-then-right and left-then-top paths in the square by
\[
p_0(s)=
\begin{cases}
(2s,0),&0\le s\le\frac12,\\
(1,2s-1),&\frac12\le s\le1,
\end{cases}
\]
and
\[
p_1(s)=
\begin{cases}
(0,2s),&0\le s\le\frac12,\\
(2s-1,1),&\frac12\le s\le1.
\end{cases}
\]
::: {.proof}
Both are continuous paths from $(0,0)$ to $(1,1)$.
Under $G$, the first becomes the concatenation $\alpha\cdot\beta$, while the second becomes $\beta\cdot\alpha$.
:::

<1>3. For $t\in I$, set
\[
p_t(s)=(1-t)p_0(s)+t p_1(s).
\]
Then
\[
H(s,t)=G(p_t(s))
\]
is a homotopy relative to endpoints from $\alpha\cdot\beta$ to $\beta\cdot\alpha$.
::: {.proof}
The square $I^2$ is convex, so $p_t(s)\in I^2$ for all $(s,t)$.
The map $(s,t)\mapsto p_t(s)$ is continuous, hence so is $H$.
At $t=0$ and $t=1$ one has
\[
H(s,0)=G(p_0(s))=(\alpha\cdot\beta)(s),
\]
and
\[
H(s,1)=G(p_1(s))=(\beta\cdot\alpha)(s).
\]
Moreover,
\[
p_t(0)=(0,0),
\qquad
p_t(1)=(1,1)
\]
for every $t$, and both points map under $G$ to $(x_0,y_0)$.
Thus the endpoints remain fixed throughout the homotopy.
:::

<1>4. Therefore the classes of $\alpha$ and $\beta$ commute in $\pi_1(X\times Y,(x_0,y_0))$.
::: {.proof}
The based homotopy in <1>3 gives
\[
[\alpha][\beta]=[\alpha\cdot\beta]=[\beta\cdot\alpha]=[\beta][\alpha].
\]
:::
:::
