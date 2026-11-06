---
schema: qual/card@1
id: P-HIRWW
kind: problem
title: Conjugation action of $G/A$ on a normal abelian subgroup
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Automorphisms
  - Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against an independent reproduction of Hungerford II.4.1.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section II.4,
    exercise 1, book page 91: "Let G be a group and A a normal abelian subgroup.
    Show that G/A operates on A by conjugation and obtain a homomorphism
    G/A → Aut A." The card states exactly this. The solution was checked as a
    proof: normality puts gag^{-1} in A; for gA = hA, writing g = hb with b in A
    gives gag^{-1} = h(bab^{-1})h^{-1} = hah^{-1} because A is abelian, which is
    the only place abelianness is used and is used correctly; the left-action
    axiom holds since (gh)a(gh)^{-1} = g(hah^{-1})g^{-1}; and conjugation by g
    restricted to A is an automorphism with inverse conjugation by g^{-1}, so
    the map into Aut(A) and its multiplicativity are immediate. Complete; no
    defect. The card does not claim that the action is by inner automorphisms
    of G or that the map is injective, and the exercise does not ask for
    either.
---

::: {.problem}
Let $G$ be a group and $A \trianglelefteq G$ be a normal abelian subgroup.
Show that $G/A$ acts on $A$ by conjugation and construct a homomorphism $\varphi: G/A \to \Aut(A)$.
:::

::: {.solution}
For $gA\in G/A$ and $a\in A$, define
$$
(gA)\cdot a=gag^{-1}.
$$

::: pf

::: {.pf-step #s1}

The formula is well-defined and takes values in $A$.

::: pf-proof

Normality of $A$ gives $gag^{-1}\in A$. Suppose $gA=hA$. Then
$h^{-1}g\in A$, so write $g=hb$ with $b\in A$. Since $A$ is abelian,
$bab^{-1}=a$, and therefore
$$
gag^{-1}=h(bab^{-1})h^{-1}=hah^{-1}.
$$
Thus the value depends only on the coset $gA$.

:::

:::

::: pf-step

This formula defines a left action of $G/A$ on $A$.

::: pf-proof

The identity coset satisfies
$$
A\cdot a=a.
$$
For $g,h\in G$,
$$
((gA)(hA))\cdot a=(gh)a(gh)^{-1}
=g(hah^{-1})g^{-1}
=(gA)\cdot((hA)\cdot a).
$$
Hence the action axioms hold.

:::

:::

::: {.pf-step #s3}

For each $gA\in G/A$, conjugation by $g$ restricts to an automorphism
of $A$.

::: pf-proof

Normality shows that conjugation by $g$ maps $A$ to itself. Its inverse on $A$
is conjugation by $g^{-1}$, so the restriction is an automorphism.

:::

:::

::: pf-step

The map
$$
\varphi:G/A\longrightarrow\operatorname{Aut}(A),\qquad
\varphi(gA)(a)=gag^{-1},
$$
is a group homomorphism.

::: pf-proof

Well-definedness follows from step [](#s1){.pf-ref} and the codomain assertion from step [](#s3){.pf-ref}. For
$g,h\in G$ and $a\in A$,
$$
\varphi((gA)(hA))(a)
=(gh)a(gh)^{-1}
=\varphi(gA)(\varphi(hA)(a)).
$$
Thus $\varphi((gA)(hA))=\varphi(gA)\varphi(hA)$.

:::

:::

:::

:::
