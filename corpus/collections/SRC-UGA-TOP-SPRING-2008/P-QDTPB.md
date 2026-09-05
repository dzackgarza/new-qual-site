---
schema: qual/card@1
id: P-QDTPB
kind: problem
title: The twist $f(e^{i\theta},s)=(e^{i(\theta+2\pi s)},s)$ of $S^1\times[0,1]$ is
  homotopic to the identity relative to one boundary circle but not both
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement and hint against problem 7 of the official UGA Spring 2008 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    The explicit linear untwisting homotopy is stationary on the lower boundary.
    If a homotopy were stationary on both boundaries, applying it to a vertical
    spanning path would make that path homotopic rel endpoints to its image
    under the twist. Projection to S^1 would then homotope a degree-one loop to
    the constant loop, contradicting pi_1(S^1)=Z.
---

::: problem
Let $f$ be the map of $S^1 \times [0, 1]$ to itself defined by
\[
f(e^{i\theta},s)=(e^{i(\theta+2\pi s)},s),
\]
so that $f$ restricts to the identity on the two boundary circles of $S^1 \times [0, 1]$.

Show that $f$ is homotopic to the identity by a homotopy $f_t$ that is stationary on one of the boundary circles, but not by any homotopy that is stationary on both boundary circles.

> Hint: Consider what $f$ does to the path $s \mapsto (e^{i\theta_0} , s)$ for fixed $e^{i\theta_0} \in S^1$.
:::

::: {.solution}
Let
\[
A=S^1\times[0,1].
\]

<1>1. The map $f$ is homotopic to the identity through a homotopy stationary on the boundary circle $S^1\times\{0\}$.
::: {.proof}
Define
\[
H:A\times[0,1]\longrightarrow A
\]
by
\[
H_t(e^{i\theta},s)
=
\left(e^{i(\theta+2\pi(1-t)s)},s\right).
\]
At $t=0$ this is $f$, while at $t=1$ it is the identity.

If $s=0$, then for every $t$,
\[
H_t(e^{i\theta},0)
=
(e^{i\theta},0).
\]
Thus the homotopy is stationary on $S^1\times\{0\}$.
:::

<1>2. Let
\[
\alpha:[0,1]\longrightarrow A,
\qquad
\alpha(s)=(1,s).
\]
Then $\alpha$ and $f\circ\alpha$ are not homotopic relative to their endpoints.
::: {.proof}
Both paths run from
\[
p=(1,0)
\qquad\text{to}\qquad
q=(1,1).
\]
Let
\[
\operatorname{pr}_1:A\longrightarrow S^1
\]
be projection onto the first factor.
Then
\[
(\operatorname{pr}_1\circ\alpha)(s)=1,
\]
so $\operatorname{pr}_1\circ\alpha$ is the constant loop at $1$, whereas
\[
(\operatorname{pr}_1\circ f\circ\alpha)(s)
=
e^{2\pi i s},
\]
which traverses $S^1$ once.

If $\alpha$ and $f\circ\alpha$ were homotopic relative to endpoints in $A$, composing such a homotopy with $\operatorname{pr}_1$ would give a based homotopy in $S^1$ from the constant loop to the once-around loop.
But these represent respectively
\[
0
\qquad\text{and}\qquad
1
\]
in
\[
\pi_1(S^1,1)\cong\ZZ.
\]
Hence no such endpoint-fixed homotopy exists.
:::

<1>3. There is no homotopy from $f$ to the identity that is stationary on both boundary circles.
::: {.proof}
Suppose, for contradiction, that
\[
K:A\times[0,1]\longrightarrow A
\]
is a homotopy from $f$ to $\operatorname{id}_A$ such that
\[
K_t(x)=x
\]
for every
\[
x\in S^1\times\{0,1\}
\]
and every $t\in[0,1]$.

Apply this homotopy to the path $\alpha$ from <1>2. The map
\[
F:[0,1]\times[0,1]\longrightarrow A,
\qquad
F(s,t)=K_t(\alpha(s)),
\]
is a homotopy from
\[
F(s,0)=f(\alpha(s))
\]
to
\[
F(s,1)=\alpha(s).
\]
Because $\alpha(0)=p$ and $\alpha(1)=q$ lie on the two boundary circles and $K$ is stationary there,
\[
F(0,t)=p,
\qquad
F(1,t)=q
\]
for every $t$.
Thus $F$ is a homotopy relative to endpoints from $f\circ\alpha$ to $\alpha$, contradicting <1>2.

Therefore no homotopy from $f$ to the identity can be stationary on both boundary circles.
:::

Hence $f$ is homotopic to the identity relative to one boundary circle, but not relative to the full boundary $S^1\times\{0,1\}$.
:::
