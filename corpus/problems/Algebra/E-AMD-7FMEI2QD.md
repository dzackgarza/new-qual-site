---
schema: qual/card@1
id: E-AMD-7FMEI2QD
kind: problem
title: A ring is local iff $x$ or $1-x$ is a unit for every $x$
classification:
  areas:
  - algebra
  topics:
  - Local Rings
  - Maximal Ideals
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The source does not say what kind of ring R is; the solution treats commutative rings with identity, and the zero ring satisfies the unit condition without being local, so the statement now assumes R nonzero, commutative, with identity.'
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; there is no retained solution set for this card and no numbered published solution to transcribe, so the card's own argument is given and the card says so. The statement is unchanged. Added: the fact that an element lies in a maximal ideal exactly when it is not a unit, used in both directions and assumed by the earlier prose, is now a step with both inclusions proved; the existence of a maximal ideal is separated from the uniqueness argument, so that "local" is established and not merely "at most one maximal ideal"; and the claim that n + (a) = R is justified by maximality of n.

---

::: {.exercise}
Let $R$ be a nonzero commutative ring with identity. Show that $R$ is a local ring iff for every $x\in R$, either $x$ or $1-x$ is a unit.

:::

::: {.solution}
There is no retained solution set for this card and it is not a textbook exercise with a numbered published solution; the argument is the card's own, from the standard facts that a proper ideal contains no unit and that every proper ideal of a nonzero commutative ring with identity is contained in a maximal ideal.

Throughout, $R$ is a nonzero commutative ring with identity, a unit is an element with a two-sided inverse, and $R$ is local when it has exactly one maximal ideal.

::: pf

::: {.pf-step #nonunits}
In a commutative ring with identity, an element lies in a maximal ideal if and only if it is not a unit.

::: pf-proof
If $x\in\mathfrak m$ with $\mathfrak m$ an ideal and $x$ were a unit, then $1=x^{-1}x\in\mathfrak m$, so $\mathfrak m=R$, contrary to maximality; hence elements of a proper ideal are nonunits. Conversely, if $x$ is not a unit then $(x)$ is a proper ideal, since $1\notin(x)$ would exhibit an inverse for $x$; a proper ideal is contained in a maximal ideal, so $x$ lies in a maximal ideal.

:::

:::

::: {.pf-step #forward}
If $R$ is local then for every $x\in R$, $x$ or $1-x$ is a unit.

::: pf-proof
Let $\mathfrak m$ be the unique maximal ideal. If neither $x$ nor $1-x$ were a unit, then by step [](#nonunits){.pf-ref} both would lie in $\mathfrak m$, since $\mathfrak m$ is the only maximal ideal; then $1=x+(1-x)\in\mathfrak m$ because $\mathfrak m$ is closed under addition, contradicting that $\mathfrak m$ is proper. So at least one of $x$, $1-x$ is a unit.

:::

:::

::: {.pf-step #at-most-one}
If every $x$ or $1-x$ is a unit, then $R$ has at most one maximal ideal.

::: pf-proof
Let $\mathfrak m,\mathfrak n$ be maximal ideals and suppose they are distinct. Then $\mathfrak m\not\subseteq\mathfrak n$, so choose $a\in\mathfrak m$ with $a\notin\mathfrak n$. The ideal $\mathfrak n+(a)$ strictly contains the maximal ideal $\mathfrak n$, hence equals $R$; so $1=b+ra$ for some $b\in\mathfrak n$ and $r\in R$. Put $x=ra$. Then $x\in\mathfrak m$ because $a\in\mathfrak m$, so $x$ is not a unit by step [](#nonunits){.pf-ref}; and $1-x=b\in\mathfrak n$, so $1-x$ is not a unit by the same step. Both $x$ and $1-x$ are then nonunits, contradicting the hypothesis. Hence $\mathfrak m=\mathfrak n$.

:::

:::

::: {.pf-step #existence}
$R$ has a maximal ideal.

::: pf-proof
$R\neq0$, so $(0)$ is a proper ideal of $R$ (it does not contain $1$), and a proper ideal of a nonzero commutative ring with identity is contained in a maximal ideal.

:::

:::

::: {.pf-step #reverse}
If for every $x\in R$ one of $x$, $1-x$ is a unit, then $R$ is local.

::: pf-proof
By step [](#at-most-one){.pf-ref} $R$ has at most one maximal ideal, and by step [](#existence){.pf-ref} it has at least one; so it has exactly one and is local.

:::

:::

::: {.pf-step #iff}
$R$ is local if and only if for every $x\in R$, $x$ or $1-x$ is a unit.

::: pf-proof
The two implications are steps [](#forward){.pf-ref} and [](#reverse){.pf-ref}.

:::

:::

:::

:::
