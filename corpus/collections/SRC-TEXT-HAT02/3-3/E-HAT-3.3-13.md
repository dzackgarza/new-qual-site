---
schema: qual/card@1
id: E-HAT-3.3-13
kind: problem
title: No retraction onto subsurface of high genus
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Rechecked the statement against Hatcher and repaired the existing solution.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Replaced the invalid homological argument with a correct proof.
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 13; it matches the printed text. The printed bracketed hint "[Apply the previous problem ...]" was missing and is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: $r^*$ is injective on $H^1$ and lands in an isotropic subspace because $H^2$
    of a surface with boundary vanishes; the cup-product form on $H^1(M_g;F)$ is nondegenerate and
    alternating, so isotropy bounds the dimension by $g$ and $2h\le g$.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Two repairs. The solution called the cup-product form "skew-symmetric" over an arbitrary field,
    which says nothing in characteristic 2; the alternating property is now derived from the
    symplectic basis, where the matrix is a sum of hyperbolic blocks, which holds in every
    characteristic. And the printed hint's route through Exercise 12 is recorded at the end, since
    the solution takes a different one; that route is not written out in full.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, and one
    citation repaired: the symplectic-basis computation the prose attributed to "Exercise 1
    p. 228" is now attributed to the symplectic basis of §3.3 on printed p. 249, with
    nondegeneracy traced to Poincaré duality, Theorem 3.30 on printed p. 250, and the
    alternating property proved integrally ($u\smile u=0$ in the torsion-free
    $H^2(M_g;\ZZ)=\ZZ$) so that it does not depend on the characteristic. Added: the
    deformation retraction of the one-boundary surface onto a wedge of $2h$ circles, and the
    block-by-block bound on an isotropic subspace. The exercise's printed hint (Exercise 12)
    is recorded as an alternative and not used. Statement re-read at §3.3 Exercise 13,
    printed p. 258. Not claimed: a retained solution set — Li stops at Exercise 11 and Sam has
    Exercises 8, 17, 32 — so the argument is the card's own.
---

::: {.problem}
Let $M_h' \subset M_g$ be a compact subsurface of genus $h$ with one boundary circle, so $M_h'$ is homeomorphic to $M_h$ with an open disk removed.
Show there is no retraction $M_g \to M_h'$ if $h > g/2$.
[Apply the previous problem, using the fact that $M_g - M_h'$ has genus $g - h$.]
:::

::: {.solution}
The statement is Hatcher, *Algebraic Topology* (2002), §3.3 Exercise 13, with the exercise's own hint. No retained solution set covers it — Guanyu Li's set stops at §3.3 Exercise 11 and Steven V. Sam's contains Exercise 8, 17 and 32 of that section — and the argument below is the card's own: it replaces the printed hint by the cup-product bound and records that the hint also works.

Throughout $F$ is a field, $M_g$ is the closed orientable surface of genus $g$, and $M_h'\subset M_g$ is a compact genus-$h$ subsurface with one boundary circle, so that $M_h'$ is $M_h$ with an open disk removed.

::: pf

::: {.pf-step #injective}
If $r:M_g\to M_h'$ is a retraction and $i:M_h'\hookrightarrow M_g$ the inclusion, then $r^*:H^1(M_h';F)\to H^1(M_g;F)$ is injective.

::: pf-proof
$r\circ i=\operatorname{id}$ gives $i^*\circ r^*=\operatorname{id}$ on $H^1(M_h';F)$, since cohomology is a functor. A map with a left inverse is injective.

:::

:::

::: {.pf-step #boundary-surface}
$\dim_F H^1(M_h';F)=2h$ and $H^2(M_h';F)=0$.

::: pf-proof
$M_h'$ is a compact surface with one boundary circle, so it is homotopy equivalent to a wedge of $2h$ circles: collapsing the complement of $2h$ arcs cutting $M_h$ into a disk gives a deformation retraction onto such a wedge (§1.1, or Exercise 1.2.4's picture). Hence $H_1(M_h';\ZZ)\cong\ZZ^{2h}$ and $H_i(M_h';\ZZ)=0$ for $i\ge2$; over the field $F$, $H^1(M_h';F)\cong\operatorname{Hom}(H_1,F)$ has dimension $2h$ by the universal coefficient theorem, and $H^2(M_h';F)=0$.

:::

:::

::: {.pf-step #isotropic}
$V=r^*H^1(M_h';F)$ is a $2h$-dimensional subspace of $H^1(M_g;F)$ on which the cup product vanishes identically.

::: pf-proof
$\dim V=2h$ since $r^*$ is injective by step [](#injective){.pf-ref}. For $u,v\in H^1(M_h';F)$, naturality of the cup product gives $r^*u\smile r^*v=r^*(u\smile v)$, and $u\smile v\in H^2(M_h';F)=0$ by step [](#boundary-surface){.pf-ref}. So every product of two elements of $V$ is zero, which is isotropy for the cup-product pairing.

:::

:::

::: {.pf-step #form}
The cup product pairing $H^1(M_g;F)\times H^1(M_g;F)\to H^2(M_g;F)\cong F$ is a nondegenerate alternating bilinear form.

::: pf-proof
Bilinearity is the bilinearity of $\smile$; nondegeneracy is Poincaré duality: for $0\ne u\in H^1(M_g;F)$ there is $v$ with $u\smile v\ne0$, because cap product with the fundamental class is an isomorphism $H^1(M_g;F)\cong H_{2-1}(M_g;F)=H_1(M_g;F)$ and the Kronecker pairing is nondegenerate (Theorem 3.30). Alternating: $u\smile u=0$ for every $u\in H^1$, since $u\smile u=-u\smile u$ by graded commutativity in odd degree, so $2(u\smile u)=0$ in the torsion-free group $H^2(M_g;\ZZ)\cong\ZZ$; this holds integrally and hence after tensoring with any field, and in particular in characteristic $2$, where a symmetric form with zero diagonal is alternating.

:::

:::

::: {.pf-step #bound}
An isotropic subspace of a nondegenerate alternating form on a space of dimension $2g$ has dimension at most $g$.

::: pf-proof
The form has a symplectic basis $e_1,f_1,\dots,e_g,f_g$, obtained by choosing $e_1\ne0$, finding $f_1$ with $e_1\cdot f_1\ne0$ by nondegeneracy, and restricting to the orthogonal complement of the span, which has dimension $2g-2$ and again carries a nondegenerate alternating form; this is the usual induction, and the resulting basis is the symplectic basis of §3.3. In such a basis the form is a direct sum of $\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ blocks, and an isotropic subspace $W$ meets the span of each block in at most one dimension: if $W$ contained two independent elements of $\langle e_i,f_i\rangle$ it would contain a vector pairing nontrivially with an element of $W$. Hence $\dim W\le g$.

:::

:::

::: {.pf-step #conclusion}
There is no retraction $M_g\to M_h'$ when $h>g/2$.

::: pf-proof
By step [](#isotropic){.pf-ref} the subspace $V$ is isotropic of dimension $2h$ in $H^1(M_g;F)$, which has dimension $2g$ by the same computation as step [](#boundary-surface){.pf-ref} applied to the closed surface. Step [](#bound) then gives $2h\le g$. Consequently $h>g/2$ is incompatible with the existence of a retraction.

:::

:::

:::
:::
