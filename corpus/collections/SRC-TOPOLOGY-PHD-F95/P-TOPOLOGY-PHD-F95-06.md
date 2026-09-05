---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F95-06
kind: problem
title: Strong deformation retracts induce fundamental-group isomorphisms
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Fundamental Group
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section II, problem 1 of the 23 September 1995 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Used the endpoint retraction of the strong deformation and the induced maps
    on based fundamental groups; the fixed-point condition on Y makes the
    homotopy basepoint-preserving.
---

::: {.problem}
Define what it means for $Y$ to be a strong deformation retract of $X$, where $Y\subseteq X$ are topological spaces.
Prove that if $i:Y\to X$ is the inclusion map and $y\in Y$, then the induced homomorphism $i_*:\pi_1(Y,y)\to\pi_1(X,y)$ is an isomorphism.
:::

::: {.solution}
<1>1. Definition of strong deformation retract.
::: {.proof}
A subspace $Y\subseteq X$ is a **strong deformation retract** of $X$ if there is a continuous map
\[
H:X\times[0,1]\longrightarrow X
\]
such that
\[
H(x,0)=x\qquad(x\in X),
\]
\[
H(x,1)\in Y\qquad(x\in X),
\]
and
\[
H(y,t)=y\qquad(y\in Y,\;t\in[0,1]).
\]
Thus $H$ deforms the identity map of $X$ to a map with image in $Y$, while fixing every point of $Y$ throughout the deformation.
:::

<1>2. The endpoint map gives a retraction $r:X\to Y$ satisfying
\[
r\circ i=\id_Y.
\]
::: {.proof}
Define
\[
r(x)=H(x,1).
\]
The endpoint condition says $r(x)\in Y$, so $r$ may be regarded as a continuous map $X\to Y$.
If $y\in Y$, the strong deformation condition gives
\[
r(i(y))=H(y,1)=y.
\]
Hence
\[
r\circ i=\id_Y.
\]
:::

<1>3. The maps $i\circ r$ and $\id_X$ are homotopic through maps fixing the basepoint $y$.
::: {.proof}
Regarding $r$ as $X\to Y$ and $i$ as the inclusion, the composite $i\circ r:X\to X$ is simply
\[
x\longmapsto H(x,1).
\]
The given deformation $H$ satisfies
\[
H(-,0)=\id_X,
\qquad
H(-,1)=i\circ r.
\]
Thus it is a homotopy from $\id_X$ to $i\circ r$.
Because the chosen basepoint satisfies $y\in Y$, the strong condition gives
\[
H(y,t)=y
\qquad(0\le t\le1).
\]
Hence this homotopy is basepoint-preserving.
:::

<1>4. On fundamental groups,
\[
r_*\circ i_*=\id_{\pi_1(Y,y)}
\quad\text{and}\quad
 i_*\circ r_*=\id_{\pi_1(X,y)}.
\]
::: {.proof}
Functoriality of the induced homomorphism gives
\[
r_*\circ i_*=(r\circ i)_*.
\]
By <1>2, $r\circ i=\id_Y$, so
\[
r_*\circ i_*=(\id_Y)_*=\id_{\pi_1(Y,y)}.
\]

Likewise,
\[
i_*\circ r_*=(i\circ r)_*.
\]
By <1>3, $i\circ r$ is basepoint-preserving homotopic to $\id_X$.
Basepoint-preserving homotopic maps induce the same homomorphism on the fundamental group, hence
\[
(i\circ r)_*=(\id_X)_*=\id_{\pi_1(X,y)}.
\]
This proves both identities.
:::

<1>5. Therefore
\[
\boxed{i_*:\pi_1(Y,y)\longrightarrow\pi_1(X,y)\text{ is an isomorphism}.}
\]
::: {.proof}
By <1>4, $r_*$ is simultaneously a left and right inverse for $i_*$.
Therefore $i_*$ is an isomorphism with inverse $r_*$.
:::
:::
