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

Hint: Is this true for $f(z)=z^n$, where $n\in\ZZ$?
:::

::: {.solution}

Let
\[
p:\RR\to S^1,
\qquad
p(t)=e^{2\pi it},
\]
be the universal covering map.

## Maps of equal degree are homotopic

::: pf

::: {.pf-step #s1-1}

Let
\[
f,g:S^1\to S^1
\]
have the same degree
\[
d\in\ZZ.
\]


::: pf-proof

This sets up the classification statement needed below.

:::

:::

::: {.pf-step #s1-2}

Choose lifts
\[
F,G:\RR\to\RR
\]
such that
\[
p\circ F=f\circ p
\]
and
\[
p\circ G=g\circ p.
\]


::: pf-proof

The domain \(\RR\) is simply connected, so both maps
\[
f\circ p,\qquad g\circ p
\]
lift through the covering \(p\).

:::

:::

::: {.pf-step #s1-3}

The common degree \(d\) is characterized by
\[
\boxed{
F(t+1)=F(t)+d}
\]
and
\[
\boxed{
G(t+1)=G(t)+d}.
\]


::: pf-proof

For a lift of a circle map, the difference
\[
F(t+1)-F(t)
\]
is integer-valued and continuous in \(t\), hence constant. That constant is the degree of the circle map. The same holds for \(G\).

:::

:::

::: {.pf-step #s1-4}

For
\[
s\in[0,1],
\]
define
\[
K_s(t)
=
(1-s)F(t)+sG(t).
\]


::: pf-proof

This is a continuous linear interpolation between the two lifts.

:::

:::

::: {.pf-step #s1-5}

One has
\[
\boxed{
K_s(t+1)=K_s(t)+d}.
\]


::: pf-proof

Using step [](#s1-3){.pf-ref},
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

:::

::: {.pf-step #s1-6}

Therefore the formula
\[
H(p(t),s)=p(K_s(t))
\]
is well defined.


::: pf-proof

If
\[
p(t)=p(t+k)
\]
for \(k\in\ZZ\), then repeated use of step [](#s1-5){.pf-ref} gives
\[
K_s(t+k)=K_s(t)+kd.
\]
Since \(kd\in\ZZ\),
\[
p(K_s(t+k))=p(K_s(t)).
\]
Thus the value depends only on the point \(p(t)\in S^1\).

:::

:::

::: {.pf-step #s1-7}

The map
\[
H:S^1\times[0,1]\to S^1
\]
is a homotopy from \(f\) to \(g\).


::: pf-proof

Continuity follows from the quotient property of \(p\). At \(s=0\),
\[
H(p(t),0)=p(F(t))=f(p(t)).
\]
At \(s=1\),
\[
H(p(t),1)=p(G(t))=g(p(t)).
\]

:::

:::

::: {.pf-step #s1-8}

Hence
\[
\boxed{
\deg f=\deg g
\Longrightarrow
f\simeq g}.
\]


::: pf-proof

This is the conclusion of steps [](#s1-1){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Degree is multiplicative under composition:
\[
\boxed{
\deg(\phi\circ\psi)=mn}.
\]


::: pf-proof

On fundamental groups,
\[
\phi_*:\ZZ\to\ZZ
\]
is multiplication by \(m\), and
\[
\psi_*:\ZZ\to\ZZ
\]
is multiplication by \(n\). Therefore
\[
(\phi\circ\psi)_*
=
\phi_*\circ\psi_*
\]
is multiplication by \(mn\).

:::

:::

::: pf-step

Likewise,
\[
\boxed{
\deg(\psi\circ\phi)=nm}.
\]


::: pf-proof

Reverse the order in step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Since integer multiplication is commutative,
\[
\boxed{
\deg(\phi\circ\psi)
=
\deg(\psi\circ\phi)}.
\]


::: pf-proof

\[
mn=nm.
\]

:::

:::

::: {.pf-step #s1-12}

Therefore
\[
\boxed{
\phi\circ\psi
\simeq
\psi\circ\phi}.
\]


::: pf-proof

Apply step [](#s1-8){.pf-ref} to the two maps whose degrees agree by step [](#s1-11){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-12){.pf-ref} is the required homotopy statement.

:::

:::

:::
