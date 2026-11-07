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
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 4, printed page
    176, with the printed hint. (a) checked: Φ(x,y) = (y/|y|, x/|y|) is a
    homeomorphism S^{p+q−1} − S^{p−1} → S^{q−1} × R^p with inverse
    (v,u)/√(1+|v|²), and contracting the R^p factor gives the deformation retraction.
    (b) checked: [S^{q−1}] generates H̃_{q−1} of the complement of S^{p−1} (Exercise 3
    applied to (D^p,S^{p−1}) ⊂ (D^{p+q},S^{p+q−1}) makes the inclusion an
    isomorphism on H_{q−1}), yet a disjoint D^q is a chain there bounding it, so the
    class would vanish. No defect.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Examined the indexed answer to Math StackExchange question 666444, including its diagram;
    the direct page fetch presented a Cloudflare challenge. Its map f is zero for a reason that
    also destroys the proposed contradiction: with C=D^{p+q}-D^q and
    A=S^{p+q-1}-S^{q-1}, Exercise 3 makes A into C a homology isomorphism in every degree,
    so H_*(C,A)=0. Thus neither that diagram nor the suggested acyclic-pair shortcut supplies a
    complete published proof. Did not alter the checked bounding-chain proof; the complete
    published-solution obligation remains open.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Repaired a hypothesis gap in (b). The previous step applied Exercise 3 to the pair
    (D^p,S^{p-1}) inside (D^{p+q},S^{p+q-1}), but Exercise 3 requires D^p to meet the boundary
    sphere in exactly S^{p-1}, and the hypothesis of (b) does not give that: an embedded disk with
    boundary S^{p-1} can meet the boundary sphere in the interior of the disk, as the arc
    gamma(t) = (t, 1-t^2) in D^2 shows, with endpoints at (+-1,0) in S^1 and
    norm(gamma(t))^2 = t^4 - t^2 + 1 <= 1, equality exactly at t = 0 and t = +-1, so the arc is
    tangent to S^1 at (0,1). Checked replacement: radial contraction z -> z/norm(z) retracts
    D^{p+q} - S^{p-1} onto S^{p+q-1} - S^{p-1}, since a point (x,y) with y nonzero and
    norm <= 1 has last coordinates y((1-t) + t/norm(x,y)) with bracket >= 1 along the segment;
    that retraction is a homotopy equivalence, the inclusion into D^{p+q} - D^p factors it
    because S^{p-1} is contained in D^p, and a map with injective composite is injective. So the
    inclusion into D^{p+q} - D^p is injective on reduced H_{q-1}, which is all the contradiction
    needs, and no properness is used. Parts (a) and (b)'s bounding-chain argument are otherwise
    unchanged. What is not covered: no complete published solution to (a) has been located, so
    that source obligation stays open; no certificate.
---
---

::: {.problem}
In the unit sphere $S^{p+q-1} \subset \RR^{p+q}$ let $S^{p-1}$ and $S^{q-1}$ be the subspheres consisting of points whose last $q$ and first $p$ coordinates are zero, respectively.

(a) Show that $S^{p+q-1} - S^{p-1}$ deformation retracts onto $S^{q-1}$, and is in fact homeomorphic to $S^{q-1} \times \RR^p$.

(b) Show that $S^{p-1}$ and $S^{q-1}$ are not the boundaries of any pair of disjointly embedded disks $D^p$ and $D^q$ in $D^{p+q}$.
[The preceding exercise may be useful.]
:::

::: {.solution}
Write points of $S^{p+q-1}$ as $(x,y)\in\RR^p\oplus\RR^q$. Then
$$
S^{p-1}=\{(x,0):\norm{x}=1\},
\qquad
S^{q-1}=\{(0,y):\norm{y}=1\}.
$$

::: pf

::: {.pf-step #s1}

There is a homeomorphism
$$
S^{p+q-1}-S^{p-1}\cong S^{q-1}\times\RR^p.
$$

::: pf-proof

On the complement one has $y\ne0$. Define
$$
\Phi(x,y)=\left(\frac y{\norm{y}},\frac x{\norm{y}}\right).
$$
Its inverse is
$$
\Phi^{-1}(u,v)=\frac{(v,u)}{\sqrt{1+\norm{v}^2}}.
$$
These formulas are continuous and inverse to one another.

:::

:::

::: {.pf-step #s2}

Hence $S^{p+q-1}-S^{p-1}$ deformation retracts onto the coordinate sphere $S^{q-1}$.

::: pf-proof

Under the homeomorphism in step [](#s1){.pf-ref}, contract the $\RR^p$ factor linearly to $0$. The subspace $S^{q-1}$ corresponds exactly to $S^{q-1}\times\{0\}$.

:::

:::

::: pf-step

Suppose, for contradiction, that there are disjoint embedded disks
$$
D^p,D^q\subset D^{p+q}
$$
with boundaries the two coordinate spheres $S^{p-1}$ and $S^{q-1}$.
Then the class
$$
[S^{q-1}]\in \widetilde H_{q-1}(S^{p+q-1}-S^{p-1})\cong\ZZ
$$
is a generator.

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref} the coordinate $S^{q-1}$ is a deformation retract of the complement, so its fundamental reduced homology class generates $\widetilde H_{q-1}$. For $q=1$ this class is the difference of the two points of $S^0$.

:::

:::

::: {.pf-step #s4}

The inclusion
$$
S^{p+q-1}-S^{p-1}\hookrightarrow D^{p+q}-D^p
$$
induces an injection on $\widetilde H_{q-1}$, which is all the next step needs.

::: pf-proof

Radial contraction $r(z)=z/\norm{z}$ retracts $D^{p+q}-S^{p-1}$ onto $S^{p+q-1}-S^{p-1}$: a point $(x,y)$ of $D^{p+q}$ with $y\ne0$ has $\norm{(x,y)}\le1$, so on the segment to $r(x,y)$ the last $q$ coordinates are $y\bigl((1-t)+t/\norm{(x,y)}\bigr)$ with the bracket $\ge1$, hence nonzero throughout. So $S^{p+q-1}-S^{p-1}\subset D^{p+q}-S^{p-1}$ is a homotopy equivalence and induces an isomorphism on $\widetilde H_{q-1}$.

Since $S^{p-1}\subset D^p$, the inclusion $S^{p+q-1}-S^{p-1}\hookrightarrow D^{p+q}-D^p$ factors that homotopy equivalence. A map whose composite with another map is injective is itself injective, so the inclusion into $D^{p+q}-D^p$ is injective on $\widetilde H_{q-1}$, as claimed.

Exercise 3 is not used here, and cannot be applied as stated: its hypothesis is that the disk meets the boundary sphere in exactly its own boundary, which the hypothesis of (b) does not supply. An embedded disk with boundary $S^{p-1}$ can meet $\partial D^{p+q}$ in the interior of the disk --- already for $p=1$, $q=1$ the arc $\gamma(t)=(t,1-t^2)$ lies in $D^2$, has endpoints $(\pm1,0)\in S^1$, and meets $S^1$ at $\gamma(0)=(0,1)$, where $\norm{\gamma(t)}^2=t^4-t^2+1\le1$; that arc is tangent to $S^1$ at $(0,1)$, so Exercise 3 does not apply to it, while the factorization above does.

:::

:::

::: pf-step

But $[S^{q-1}]$ maps to zero in $\widetilde H_{q-1}(D^{p+q}-D^p)$, a contradiction.

::: pf-proof

The disk $D^q$ is disjoint from $D^p$ by assumption, so it is a singular $q$-chain in $D^{p+q}-D^p$ whose boundary is $S^{q-1}$. Thus the image of $[S^{q-1}]$ is zero. This contradicts the injectivity in step [](#s4){.pf-ref}.

:::

:::

:::

Therefore the two coordinate spheres cannot bound disjoint embedded disks in $D^{p+q}$.
:::
