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
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Searched outside the retained sets again on 2026-11-16 and read two further
    sources. Luis Fuentes and Manuel Pedreira, The Projective Theory of Ruled
    Surfaces, arXiv:math/0006204v3 (2002), downloaded whole to
    tmp/sources/projective-theory-ruled-surfaces.pdf: its Proposition 1.7, printed
    p. 5, builds the incidence variety of a linearly normal scroll and concludes
    that the scroll determines its ruled surface, which is uniqueness of the ruling
    of an embedded scroll and not the birational statement asked here, so it does
    not supply this exercise. Math StackExchange question 1715815, "Uniqueness of
    ruling for a ruled surface", asks exactly V.2.1 and has no answer: the page
    carries only Mohan's comment that a nonconstant map between curves of genus
    above one is an isomorphism by Hurwitz, with pointers to work of Ohm and
    Deveney. Chao Li's Columbia notes "Enriques classification of complex
    algebraic surfaces" were also read: their Theorem 7 and its proof show that
    every minimal model of C x P^1 for an irrational C is geometrically ruled
    over C, which recovers the base from a minimal model but never states or
    proves that C itself is determined by the birational class of X, so it is not
    an argument for this exercise either. No complete published argument for
    V.2.1 was located; steps s2 to s5 remain the card's own and were checked
    against the book in the note above.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the National Taiwan University set's Exercise 1 of section 2 in its
    text version on 2026-11-16 and made steps s2 and s4 its argument rather than
    a parallel one. Step s2 now evaluates on the fibres of p, as that set does:
    for all but finitely many x the restriction to {x} x P^1 gives a rational map
    P^1 to C', which extends to a morphism and is constant because C' is not
    P^1; the constants assemble into a morphism by comparison with the morphism
    C x {u} to C'. Step s4 is that set's last case, which the earlier notes
    called invalid: it is valid, since with C = P^1 and C' not P^1 the morphism
    f-tilde is constant, hence p' composed with the birational map is constant
    and its image lies in one fibre of p', a curve, which a dominant map from a
    surface cannot have. The other direction of s4 is the same argument applied
    to the inverse birational map. Also corrected: Math StackExchange question
    1715815 asks the isomorphism form, C_1 x P^1 isomorphic to C_2 x P^1, not
    this exercise's birational form. Not checked: whether that thread's
    question, being strictly weaker, follows from this exercise without a
    further argument; nothing on the card needs it.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Read Math StackExchange question 1715815, "Uniqueness of ruling for a ruled
    surface", whole through the Stack Exchange API on 2026-11-16: the question
    and all four of its comments are in
    tmp/sources/mse-1715815-hart77-v21-uniqueness-of-ruling.md, which the API
    returns as the question, an empty answer list and four comments. The
    comments are Mohan's 3502237 (assume C_1 and C_2 smooth projective; their
    genera agree because both are h^1 of C_i x P^1; genus zero makes both P^1;
    otherwise compose C_1 x {p} subset C_1 x P^1 = C_2 x P^1 with the
    projection to C_2, and show the composite nonconstant and hence an
    isomorphism, with the remark that g = 1 needs an extra argument), Xuqiang
    Qin's 3502350 asking whether that last step is Hurwitz's theorem, Mohan's
    3502398 answering that it is, and Takumi Murayama's 3502454 giving the
    field-theoretic route through Ohm following Nagata and Deveney and
    remarking that Mohan's argument also covers the birational case. Two
    earlier records are corrected here. The events of 2026-11-11 and of
    2026-11-16 above give the pointers to Ohm and Deveney to Mohan: they are
    Murayama's, and Mohan's comment cites neither paper. The event immediately
    above states that the saved page carries no answer and no comment: the file
    saved at that reading held the question alone, and the thread itself
    carries the four comments listed here, which the saved file now holds. What
    the thread gives is a sketch in a comment and not a published argument: it
    assumes the curves smooth and projective, treats genus zero and genus above
    one and leaves genus one to an extra argument, and it proves the
    isomorphism form of the statement, which steps s3 and s5 give here for C
    and C' not rational. The published argument for the exercise stays Exercise
    1 of section 2 of the National Taiwan University set, recorded in the
    remark below. Not checked: the contents of the three papers Murayama names,
    none of which is in tmp/sources.
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

If $C'\not\cong\PP^1$, then
$$
p'\circ\Phi=f\circ p
$$
for a morphism $f:C\to C'$, which is dominant.

::: pf-proof

Let $U\subseteq C\times\PP^1$ be a dense open set on which $\Phi$ is a
morphism. For $x\in C$ whose fibre
$\{x\}\times\PP^1$ meets $U$, the restriction is a rational map
$$
\PP^1\cong\{x\}\times\PP^1\longrightarrow C',
$$
and only finitely many $x$ fail this. Since $C'$ is a nonsingular projective
curve, that rational map extends to a morphism $\PP^1\to C'$, which is
constant by step [](#s1){.pf-ref} because $C'\not\cong\PP^1$. Write
$\widetilde f(x)$ for the constant value.

Fix $(x_0,u_0)\in U$ and let
$$
g:C\dashrightarrow C',\qquad
x\longmapsto p'\bigl(\Phi(x,u_0)\bigr)
$$
be the restriction of $p'\circ\Phi$ to the slice $C\times\{u_0\}$; it is a
rational map, a morphism on the open set of $x$ with $(x,u_0)\in U$. At a
point $x$ where both $g$ and $\widetilde f$ are defined, the value $\widetilde
f(x)$ is the value of the restriction of $p'\circ\Phi$ to $\{x\}\times\PP^1$,
which contains $(x,u_0)$ and is constant, so $\widetilde f(x)=g(x)$. Hence
$\widetilde f=g$ as rational maps. A rational map from the nonsingular curve $C$
to the projective curve $C'$ extends to a morphism, so
$$
f=\widetilde f:C\longrightarrow C'
$$
is a morphism with $p'\circ\Phi=f\circ p$. Since $\Phi$ and $p'$ are dominant
and $p$ is surjective, $f$ is dominant.

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

Suppose $C\cong\PP^1$ and assume for contradiction that $C'\not\cong\PP^1$. By
step [](#s2){.pf-ref},
$$
p'\circ\Phi=f\circ p
$$
with $f:C\to C'$ a morphism, and $C\cong\PP^1$ with $C'\not\cong\PP^1$ makes
$f$ constant by step [](#s1){.pf-ref}. Hence $p'\circ\Phi$ is constant, so the
image of the birational map $\Phi$ is contained in a single fibre
$$
\{c\}\times\PP^1
$$
of $p'$, which is a curve. A birational map is dominant, and the image of a
dominant map from a surface is dense, hence of dimension two. This is
impossible, so $C\cong\PP^1$ forces $C'\cong\PP^1$.

The same argument applied to the inverse birational map $\Psi$, whose target is
$C$, shows that $C'\cong\PP^1$ forces $C\cong\PP^1$. Hence either curve
rational implies both are.

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
Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework solutions, text version `tmp/sources/ntu-ag2-chapter5.md`, Exercise 1 of §2 (solution by Shuang-Yen Lee), printed p. 5 of that set, is the argument of steps [](#s2){.pf-ref} to [](#s4){.pf-ref}: assume $C'\not\cong\PP^1$, restrict the birational map to $\{x\}\times\PP^1$ and extend to a morphism $\PP^1\to C'$, which is constant because $C'\not\cong\PP^1$; the constants assemble into a morphism $C\to C'$; then "$C\not\cong\PP^1$, similarly we have a map $\widetilde g:C'\to C$", and with $f,g$ inverse so are $\widetilde f,\widetilde g$. Its last case reads "if $C=\PP^1$, then $\widetilde f$ is a constant, which means $f$ is a constant, a contradiction", and it is a valid contradiction: with $C\cong\PP^1$ and $C'\not\cong\PP^1$ the morphism $\widetilde f$ is constant by the same argument, so $p'\circ\Phi=\widetilde f\circ p$ is constant and the image of the birational map lies in one fibre $\{c\}\times\PP^1$ of $p'$, which is a curve. Its sentence names $f$, and $f$ is not constant, being the birational map and hence dominant; what the constancy argument gives is $\widetilde f=p'\circ f$, and that is all the contradiction needs. Step [](#s4){.pf-ref} sets that out and gets the other direction by applying it to $\Psi$. Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} are this set's argument, made explicit about the extension of the rational maps and about the inverse maps of the bases.

Yang Pi-Yeh, *Hartshorne Solutions*, text version `tmp/sources/lfwin-hartshorne-solutions.md`, exercise 5.2.1, printed p. 102, writes "$K(X)=L\otimes_kk(x)=L(x)$; then by corollary 6.12 in chapter I there exists a unique smooth projective curve $C$ such that $K(C)=L$, i.e. $C$ is unique one such that $X$ is birationally equivalent to $C\times\PP^1$". The uniqueness of the smooth projective model with a *given* function field is I.6.12, but the identity "$K(C)=L$" is not determined by $K(X)$ alone: that $L$ and $L'$ with $L(x)\cong L'(x)$ satisfy $L\cong L'$ is exactly what the exercise asks, so the argument assumes its conclusion.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise V.2.1: "Suppose that $C_0\times\PP^1\cong X\cong C_1\times\PP^1$. But two curves which are birational are isomorphic." That is the last sentence of step [](#s5){.pf-ref}; the birationality of $C_0$ and $C_1$ is asserted and not proved, and it is the content of the exercise.
:::
