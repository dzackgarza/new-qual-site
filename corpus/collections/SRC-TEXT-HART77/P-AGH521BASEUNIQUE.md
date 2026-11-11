---
schema: qual/card@1
id: P-AGH521BASEUNIQUE
kind: problem
title: Uniqueness of the base curve of a birationally ruled surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.2.1, the retained Egbert note, and the local uniqueness
    theorem for smooth projective models of curves. The retained note jumps
    directly from birationality of C x P^1 and C' x P^1 to birationality of C
    and C'. The proof below supplies the missing descent: a rational map to a
    nonrational curve is constant on the general P^1-fibre, hence factors
    rationally through the base; applying this to a birational map and its
    inverse produces inverse birational maps of the base curves. The rational
    base case is treated separately.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.2,
    exercise 2.1, printed page 383 (PDF page 398 of the extraction), and the
    chapter's definition of birationally ruled in Remark 2.2.1, printed page
    370. Checked the card's steps: a rational map from a nonsingular curve
    extends to a morphism (I.6.8) and a birational map of nonsingular projective
    curves is an isomorphism (I.6.12), both printed page 45; Luroth is what makes
    a rational map P^1 to a nonrational curve constant. Searched outside the
    twelve retained sets and read two further published treatments. Algebraic
    Geometry II, National Taiwan University, 2020 Spring, Chapter V homework,
    Exercise 1 of section 2, PDF p. 5 (tmp/sources/ntu-ag2-chapter5.pdf): the
    argument is the card's, except that its last case reads "if C = P^1 then
    f-tilde is a constant, which means f is a constant, a contradiction", and
    f-tilde is dominant by construction; step s4 states the unirationality that
    case needs. Yang Pi-Yeh, Hartshorne Solutions, exercise 5.2.1, printed p.
    102 (tmp/sources/lfwin-hartshorne-solutions.pdf), passes from K(X) = L(x) to
    "the unique curve C with K(C) = L", which assumes that L is determined by
    K(X), the content of the exercise. Not checked: the argument was not
    re-examined over a non-algebraically-closed base field.
---

::: {.problem}
If $X$ is a birationally ruled surface, show that the curve $C$, such that $X$ is birationally equivalent to $C \times \PP^1$, is unique (up to isomorphism).
:::

::: {.solution}
Suppose
$$
C\times\PP^1\dashrightarrow C'\times\PP^1
$$
is a birational map $\Phi$, with inverse $\Psi$. Let
$$
p:C\times\PP^1\to C,
\qquad
p':C'\times\PP^1\to C'
$$
be the projections.

::: pf

::: {.pf-step #s1}

If $B$ is a nonsingular projective curve not isomorphic to $\PP^1$, then
every rational map
$$
\PP^1\dashrightarrow B
$$
is constant.

::: pf-proof

A rational map from the nonsingular curve $\PP^1$ to the projective curve $B$
extends to a morphism. If it were nonconstant, it would be dominant and would
give an inclusion of function fields
$$
k(B)\hookrightarrow k(t).
$$
By Lüroth's theorem, every intermediate field of transcendence degree one in
$k(t)/k$ is rational. Thus $k(B)\cong k(u)$, so $B$ is birational to
$\PP^1$. Since both curves are nonsingular and projective, the uniqueness of
smooth projective models [[T-CRVMINMOD]] would give
$$
B\cong\PP^1,
$$
contrary to the hypothesis. Hence the map is constant.

:::

:::

::: {.pf-step #s2}

If $C'\not\cong\PP^1$, then the rational map
$$
p'\circ\Phi:C\times\PP^1\dashrightarrow C'
$$
factors uniquely as
$$
C\times\PP^1\dashrightarrow C\dashrightarrow C',
$$
that is,
$$
p'\circ\Phi=f\circ p
$$
for a dominant rational map $f:C\dashrightarrow C'$.

::: pf-proof

Restrict $p'\circ\Phi$ to the generic fibre of $p$. After extending the
ground field from $k$ to $k(C)$, this is a rational map
$$
\PP^1_{k(C)}\dashrightarrow C'_{k(C)}.
$$
If it were nonconstant, after passage to an algebraic closure of $k(C)$ it
would give a nonconstant rational map from $\PP^1$ to the base change of
$C'$. Step [](#s1){.pf-ref} would force that base-changed curve, and hence $C'$, to have
genus zero, so $C'\cong\PP^1$. This contradicts the hypothesis. Thus the map
is constant on the generic $p$-fibre.

Equivalently on function fields, the pullback
$$
k(C')\longrightarrow k(C)(t)
$$
has image in the subfield $k(C)$. It therefore defines a rational map
$$
f:C\dashrightarrow C'
$$
with $p'\circ\Phi=f\circ p$. Since both $\Phi$ and $p'$ are dominant, so is
$f$.

:::

:::

::: {.pf-step #s3}

If neither $C$ nor $C'$ is isomorphic to $\PP^1$, then $C$ and $C'$ are
birational.

::: pf-proof

By step [](#s2){.pf-ref},
$$
p'\circ\Phi=f\circ p
$$
for a dominant rational map $f:C\dashrightarrow C'$. Applying the same
argument to the inverse birational map $\Psi$ gives a dominant rational map
$g:C'\dashrightarrow C$ with
$$
p\circ\Psi=g\circ p'.
$$
On the common dense open set where the birational compositions are defined,
$$
\begin{aligned}
p
&=p\circ\Psi\circ\Phi\\
&=g\circ p'\circ\Phi\\
&=g\circ f\circ p.
\end{aligned}
$$
Since $p$ is dominant,
$$
g\circ f=\id_C
$$
as rational maps. Similarly,
$$
f\circ g=\id_{C'}.
$$
Thus $f$ and $g$ are inverse birational maps.

:::

:::

::: {.pf-step #s4}

If one of $C,C'$ is isomorphic to $\PP^1$, then so is the other.

::: pf-proof

Suppose, for example, that $C'\cong\PP^1$ and assume for contradiction that
$C\not\cong\PP^1$. Apply the argument of step [](#s2){.pf-ref} to the composite
$$
p\circ\Psi:C'\times\PP^1\dashrightarrow C.
$$
Because the target $C$ is nonrational, this composite factors through the
first projection and produces a dominant rational map
$$
C'\dashrightarrow C.
$$
But $C'\cong\PP^1$, contradicting step [](#s1){.pf-ref}. Hence $C\cong\PP^1$. The other
direction is symmetric.

:::

:::

::: {.pf-step #s5}

The base curve of a birationally ruled surface is unique up to
isomorphism:
$$
\boxed{C\cong C'.}
$$

::: pf-proof

If one curve is rational, step [](#s4){.pf-ref} shows both are $\PP^1$. Otherwise step
[](#s3){.pf-ref} shows that $C$ and $C'$ are birational. Nonsingular projective curves have
unique smooth projective models by [[T-CRVMINMOD]], so birationality implies
isomorphism.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove the required uniqueness of the base curve.

:::

:::

:::

::: {.remark title="Published solution"}
Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework solutions, Exercise 1 of §2 (solution by Shuang-Yen Lee), PDF p. 5, argues as steps [](#s2){.pf-ref} to [](#s4){.pf-ref}: assume $C'\not\cong\PP^1$, restrict the birational map to $\{x\}\times\PP^1$ and extend to a morphism $\PP^1\to C'$, which is constant because $C'\not\cong\PP^1$; the constants assemble into a morphism $C\to C'$; then "$C\not\cong\PP^1$, similarly we have a map $\widetilde g:C'\to C$", and with $f,g$ inverse so are $\widetilde f,\widetilde g$. Its last case reads "if $C=\PP^1$, then $\widetilde f$ is a constant, which means $f$ is a constant, a contradiction", which is not what the construction gives: $\widetilde f$ is dominant, being induced by a dominant map. What the case needs is that a dominant rational map $\PP^1\dashrightarrow C'$ makes $C'$ unirational, hence isomorphic to $\PP^1$; that is step [](#s4){.pf-ref}.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.2.1, printed p. 102, writes "$K(X)=L\otimes_kk(x)=L(x)$; then by corollary 6.12 in chapter I there exists a unique smooth projective curve $C$ such that $K(C)=L$, i.e. $C$ is unique one such that $X$ is birationally equivalent to $C\times\PP^1$". The uniqueness of the smooth projective model with a *given* function field is I.6.12, but the identity "$K(C)=L$" is not determined by $K(X)$ alone: that $L$ and $L'$ with $L(x)\cong L'(x)$ satisfy $L\cong L'$ is exactly what the exercise asks, so the argument assumes its conclusion.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.2.1, PDF p. 261: "Suppose that $C_0\times\PP^1\cong X\cong C_1\times\PP^1$. But two curves which are birational are isomorphic." That is the last sentence of step [](#s5){.pf-ref}; the birationality of $C_0$ and $C_1$ is asserted and not proved, and it is the content of the exercise.
:::
