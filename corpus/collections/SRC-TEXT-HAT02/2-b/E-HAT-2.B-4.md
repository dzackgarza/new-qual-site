---
schema: qual/card@1
id: E-HAT-2.B-4
kind: problem
title: "Linking numbers via Mayer--Vietoris"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the Alexander-duality and Mayer--Vietoris calculations and all degree shifts.
---

In the unit sphere $S^{p+q-1} \subset \mathbb{R}^{p+q}$ let $S^{p-1}$ and $S^{q-1}$ be the subspheres consisting of points whose last $q$ and first $p$ coordinates are zero, respectively.

(a) Show that $S^{p+q-1} - S^{p-1}$ deformation retracts onto $S^{q-1}$, and is in fact homeomorphic to $S^{q-1} \times \mathbb{R}^p$.

(b) Show that $S^{p-1}$ and $S^{q-1}$ are not the boundaries of any pair of disjointly embedded disks $D^p$ and $D^q$ in $D^{p+q}$.
[The preceding exercise may be useful.]

::: {.solution}
Write points of $S^{p+q-1}$ as $(x,y)\in\mathbb R^p\oplus\mathbb R^q$. Then
\[
S^{p-1}=\{(x,0):\|x\|=1\},
\qquad
S^{q-1}=\{(0,y):\|y\|=1\}.
\]

<1>1. There is a homeomorphism
\[
S^{p+q-1}-S^{p-1}\cong S^{q-1}\times\mathbb R^p.
\]
::: {.proof}
On the complement one has $y\ne0$. Define
\[
\Phi(x,y)=\left(\frac y{\|y\|},\frac x{\|y\|}\right).
\]
Its inverse is
\[
\Phi^{-1}(u,v)=\frac{(v,u)}{\sqrt{1+\|v\|^2}}.
\]
These formulas are continuous and inverse to one another.
:::

<1>2. Hence $S^{p+q-1}-S^{p-1}$ deformation retracts onto the coordinate sphere $S^{q-1}$.
::: {.proof}
Under the homeomorphism in <1>1, contract the $\mathbb R^p$ factor linearly to $0$. The subspace $S^{q-1}$ corresponds exactly to $S^{q-1}\times\{0\}$.
:::

<1>3. Suppose, for contradiction, that there are disjoint embedded disks
\[
D^p,D^q\subset D^{p+q}
\]
with boundaries the two coordinate spheres $S^{p-1}$ and $S^{q-1}$.
Then the class
\[
[S^{q-1}]\in H_{q-1}(S^{p+q-1}-S^{p-1})\cong\mathbb Z
\]
is a generator.
::: {.proof}
By <1>1--<1>2 the coordinate $S^{q-1}$ is a deformation retract of the complement, so its fundamental homology class generates $H_{q-1}$.
:::

<1>4. By Exercise 3, the inclusion
\[
S^{p+q-1}-S^{p-1}\hookrightarrow D^{p+q}-D^p
\]
induces an isomorphism on homology.
::: {.proof}
Apply Exercise 3 to the properly embedded pair $(D^p,S^{p-1})\subset(D^{p+q},S^{p+q-1})$.
:::

<1>5. But $[S^{q-1}]$ maps to zero in $H_{q-1}(D^{p+q}-D^p)$, a contradiction.
::: {.proof}
The disk $D^q$ is disjoint from $D^p$ by assumption, so it is a singular $q$-chain in $D^{p+q}-D^p$ whose boundary is $S^{q-1}$. Thus the image of $[S^{q-1}]$ is zero. This contradicts the injectivity in <1>4.
:::

Therefore the two coordinate spheres cannot bound disjoint embedded disks in $D^{p+q}$.
:::
