---
schema: qual/card@1
id: P-TOP-WORKSHOP-QPH-03
kind: problem
title: Compositions of two self-maps of the circle are homotopic
classification:
  areas: [topology]
  topics: [Homotopy, Degree]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3, labeled Arizona Winter 2005, in assets/attachments/QualProblemsHomotopy_extracted.md.
---

::: {.problem}
Suppose $\phi:S^1\to S^1$ and $\psi:S^1\to S^1$ are continuous maps.
Show that the compositions $\phi\circ\psi$ and $\psi\circ\phi$ are homotopic.

Hint: Is this true for $f(z)=z^n$, where $n\in\mathbb Z$?
:::

::: {.solution}
Let
\[
p:\mathbb R\to S^1,
\qquad
p(t)=e^{2\pi it},
\]
be the universal covering map.

## Maps of equal degree are homotopic

<1>1. Let
\[
f,g:S^1\to S^1
\]
have the same degree
\[
d\in\mathbb Z.
\]

::: {.proof}
This sets up the classification statement needed below.
:::

<1>2. Choose lifts
\[
F,G:\mathbb R\to\mathbb R
\]
such that
\[
p\circ F=f\circ p
\]
and
\[
p\circ G=g\circ p.
\]

::: {.proof}
The domain \(\mathbb R\) is simply connected, so both maps
\[
f\circ p,\qquad g\circ p
\]
lift through the covering \(p\).
:::

<1>3. The common degree \(d\) is characterized by
\[
\boxed{
F(t+1)=F(t)+d}
\]
and
\[
\boxed{
G(t+1)=G(t)+d}.
\]

::: {.proof}
For a lift of a circle map, the difference
\[
F(t+1)-F(t)
\]
is integer-valued and continuous in \(t\), hence constant. That constant is the degree of the circle map. The same holds for \(G\).
:::

<1>4. For
\[
s\in[0,1],
\]
define
\[
K_s(t)
=
(1-s)F(t)+sG(t).
\]

::: {.proof}
This is a continuous linear interpolation between the two lifts.
:::

<1>5. One has
\[
\boxed{
K_s(t+1)=K_s(t)+d}.
\]

::: {.proof}
Using step <1>3,
\[
\begin{aligned}
K_s(t+1)
&=
(1-s)(F(t)+d)+s(G(t)+d)\\
&=
K_s(t)+d.
\end{aligned}
\]
:::

<1>6. Therefore the formula
\[
H(p(t),s)=p(K_s(t))
\]
is well defined.

::: {.proof}
If
\[
p(t)=p(t+k)
\]
for \(k\in\mathbb Z\), then repeated use of step <1>5 gives
\[
K_s(t+k)=K_s(t)+kd.
\]
Since \(kd\in\mathbb Z\),
\[
p(K_s(t+k))=p(K_s(t)).
\]
Thus the value depends only on the point \(p(t)\in S^1\).
:::

<1>7. The map
\[
H:S^1\times[0,1]\to S^1
\]
is a homotopy from \(f\) to \(g\).

::: {.proof}
Continuity follows from the quotient property of \(p\). At \(s=0\),
\[
H(p(t),0)=p(F(t))=f(p(t)).
\]
At \(s=1\),
\[
H(p(t),1)=p(G(t))=g(p(t)).
\]
:::

<1>8. Hence
\[
\boxed{
\deg f=\deg g
\Longrightarrow
f\simeq g}.
\]

::: {.proof}
This is the conclusion of steps <1>1--<1>7.
:::

## The two compositions

Let
\[
m=\deg\phi,
\qquad
n=\deg\psi.
\]

<1>9. Degree is multiplicative under composition:
\[
\boxed{
\deg(\phi\circ\psi)=mn}.
\]

::: {.proof}
On fundamental groups,
\[
\phi_*:\mathbb Z\to\mathbb Z
\]
is multiplication by \(m\), and
\[
\psi_*:\mathbb Z\to\mathbb Z
\]
is multiplication by \(n\). Therefore
\[
(\phi\circ\psi)_*
=
\phi_*\circ\psi_*
\]
is multiplication by \(mn\).
:::

<1>10. Likewise,
\[
\boxed{
\deg(\psi\circ\phi)=nm}.
\]

::: {.proof}
Reverse the order in step <1>9.
:::

<1>11. Since integer multiplication is commutative,
\[
\boxed{
\deg(\phi\circ\psi)
=
\deg(\psi\circ\phi)}.
\]

::: {.proof}
\[
mn=nm.
\]
:::

<1>12. Therefore
\[
\boxed{
\phi\circ\psi
\simeq
\psi\circ\phi}.
\]

::: {.proof}
Apply step <1>8 to the two maps whose degrees agree by step <1>11.
:::

<1>13. Q.E.D.

::: {.proof}
Step <1>12 is the required homotopy statement.
:::
:::
