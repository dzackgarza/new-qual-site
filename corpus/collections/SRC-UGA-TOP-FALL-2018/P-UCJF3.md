---
schema: qual/card@1
id: P-UCJF3
kind: problem
title: 'van Kampen''s theorem: the surjection $\pi_1(A)*\pi_1(B)\to\pi_1(A\cup B)$'
classification:
  areas:
  - topology
  topics:
  - van Kampen
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked against problem 4 of the official UGA Fall 2018 topology exam and restored the omitted openness hypotheses on A, B, and A intersect B.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the Lebesgue-number subdivision, transition-point paths in A intersect B, and factorization of an arbitrary based loop.
---

::: problem
Prove the following portion of van Kampen's theorem.
If
\[
X=A\cup B
\]
and $A$, $B$, and $A\cap B$ are open and path connected, with $*\in A\cap B$, then there is a surjection
\[
\pi_1(A,*)*\pi_1(B,*)\longrightarrow\pi_1(X,*).
\]
:::

::: {.solution}
Let
\[
i_A:A\hookrightarrow X,
\qquad
i_B:B\hookrightarrow X
\]
be the inclusions.
By the universal property of the free product, the induced homomorphisms on fundamental groups determine a homomorphism
\[
\Phi:\pi_1(A,*)*\pi_1(B,*)\longrightarrow\pi_1(X,*).
\]
We prove that $\Phi$ is surjective.

<1>1. Every based loop in $X$ admits a finite subdivision whose subpaths lie alternately in $A$ or $B$.
::: {.proof}
Let
\[
\gamma:[0,1]\longrightarrow X
\]
be a loop based at $*$.
Since $A$ and $B$ are open and cover $X$, the sets
\[
\gamma^{-1}(A),
\qquad
\gamma^{-1}(B)
\]
form an open cover of the compact metric space $[0,1]$.
Choose a Lebesgue number $\delta>0$ for this cover and a partition
\[
0=t_0<t_1<\cdots<t_m=1
\]
whose subintervals have length less than $\delta$.
Then for each $j$ the image
\[
\gamma([t_{j-1},t_j])
\]
is contained entirely in $A$ or entirely in $B$.
Choose one such set and denote it by $L_j\in\{A,B\}$.
:::

<1>2. For every subdivision point $t_j$, one can choose a path
\[
\alpha_j:[0,1]\longrightarrow X
\]
from $*$ to $\gamma(t_j)$ that lies in every $L_r$ incident to that endpoint.
::: {.proof}
Take $\alpha_0$ and $\alpha_m$ to be the constant path at $*$.
For $0<j<m$, there are two cases.

If
\[
L_j=L_{j+1},
\]
then $\gamma(t_j)$ and $*$ both lie in the path-connected set $L_j$, so choose $\alpha_j$ inside $L_j$.
If
\[
L_j\neq L_{j+1},
\]
then
\[
\gamma(t_j)\in L_j\cap L_{j+1}=A\cap B.
\]
Since $A\cap B$ is path connected and contains $*$, choose $\alpha_j$ inside $A\cap B$.
Thus, for every $r$, both $\alpha_{r-1}$ and $\alpha_r$ lie in $L_r$.
:::

<1>3. The loop $\gamma$ is homotopic rel basepoint to a product of loops each lying entirely in $A$ or entirely in $B$.
::: {.proof}
Let
\[
\gamma_j=\gamma|_{[t_{j-1},t_j]}
\]
with the usual reparametrization to $[0,1]$, and define the based loop
\[
\sigma_j
=\alpha_{j-1}*\gamma_j*\overline{\alpha_j}.
\]
By <1>2, the entire loop $\sigma_j$ lies in $L_j$, hence in $A$ or in $B$.

In the concatenation
\[
\sigma_1*\cdots*\sigma_m,
\]
each adjacent pair
\[
\overline{\alpha_j}*\alpha_j
\]
is homotopic rel endpoints to the constant path at $\gamma(t_j)$.
Since $\alpha_0$ and $\alpha_m$ are constant at $*$, cancellation of these backtracking paths gives
\[
[\gamma]
=[\sigma_1]\cdots[\sigma_m]
\]
in $\pi_1(X,*)$.
:::

<1>4. The homomorphism $\Phi$ is surjective.
::: {.proof}
By <1>3, every element $[\gamma]\in\pi_1(X,*)$ is a product of classes $[\sigma_j]$, each represented by a loop wholly in $A$ or wholly in $B$.
Therefore every factor lies in the image of
\[
(i_A)_*:\pi_1(A,*)\to\pi_1(X,*)
\]
or of
\[
(i_B)_*:\pi_1(B,*)\to\pi_1(X,*).
\]
These two maps are precisely the restrictions of $\Phi$ to the two free factors.
Hence $[\gamma]\in\operatorname{im}\Phi$.
Since $[\gamma]$ was arbitrary, $\Phi$ is surjective.
:::
:::
