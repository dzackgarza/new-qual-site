---
schema: qual/card@1
id: P-MMAQ-KGHDXFTO6Z
kind: problem
title: A finite field has irreducible polynomials of every positive degree
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 2 of the Algebra Preliminary Examination of September 8, 2008
    (University of Washington), printed p. 1 of the two-page paper retained at assets/attachments/UW-
    Algebra-Qual-2008.pdf, is the statement the card answers, and the paragraph at the head of the
    solution records that the paper prints no solutions, so the argument is the card's own. Checked: the
    statement against the paper's text layer at the page named; the solution read for the construction
    of the field of q^n elements as the fixed points of the n-th Frobenius power and the extraction of
    an element of each degree d dividing n; `qualc.authoring check` on the card, and `tmp/lam.sh` for
    the numbering and the QED. Not checked: no retained solution set exists for this paper to compare
    the argument with, and no other card of the collection in this pass.
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card opened with a step whose claim was a notation
    instruction ('Write |F| = q') followed by the n = 1 case with no proof, and its later steps
    asserted |E| = q^n and the existence of an element of each degree without argument. It is
    now five proved steps: the degree-1 case; E is a subfield containing F, keeping the card's
    Frobenius computation but stating the iterated Frobenius identity it uses; |E| = q^n from
    the q^n distinct roots of x^{q^n} - x, whose derivative -1 is nonzero; the existence of an
    element of degree exactly d for each d | n, through the cyclic structure of E^× and the fact
    that a finite field is not the union of its proper subfields; and the conclusion. The answer
    is unchanged. Not claimed: a retained solution set; the collection's provenance is the
    examination paper only.
---

::: {.problem}
Let $F$ be a finite field.
Show for any positive integer $n$ that there are irreducible polynomials of degree $n$ in $F[x]$.
:::

::: {.solution}

The problem is Problem 2 of the Algebra Preliminary Examination of September 8, 2008 (University of Washington), printed p. 1 of the two-page paper retained at `assets/attachments/UW-Algebra-Qual-2008.pdf`. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and what it supplies is the construction: the subfield $E=\{\alpha:\alpha^{q^n}=\alpha\}$ of $\overline{F}$ has $q^n$ elements, and for each $d\mid n$ an element of $E$ of degree $d$ over $F$ gives an irreducible polynomial of that degree
Throughout $F$ is a finite field with $\cardinality{F} = q$, $p \coloneqq \operatorname{char}F$ is prime and $q$ is a power of $p$, and $\overline{F}$ is an algebraic closure of $F$. The collection's `provenance` is the 2014 UW algebra examination, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #n1}
For $n = 1$ there is an irreducible polynomial of degree $1$ in $F[x]$.

::: pf-proof
Take any $a \in F$, which exists because a field is nonempty, and $x - a$. A polynomial of degree $1$ admits no factorization into two polynomials of positive degree, since degrees would add to $1 > 0 + 0$; hence $x - a$ is irreducible, and its root $a$ lies in $F$.

:::

:::

::: {.pf-step #E}
$E \coloneqq \theset{\alpha \in \overline{F} \mid \alpha^{q^{n}} = \alpha}$ is a subfield of $\overline{F}$ containing $F$.

::: pf-proof
For $a, b \in E$ the Frobenius identity $(a+b)^{q^{n}} = a^{q^{n}} + b^{q^{n}}$ in characteristic $p$, iterated $n$ times, gives $(a+b)^{q^{n}} = a + b$, and $(ab)^{q^{n}} = a^{q^{n}}b^{q^{n}} = ab$; also $0, 1 \in E$ and, for $a \ne 0$, $(a^{-1})^{q^{n}} = (a^{q^{n}})^{-1} = a^{-1}$. So $E$ is a subfield. For $a \in F$ one has $a^{q} = a$ because $F^{\times}$ has order $q-1$, hence $a^{q^{n}} = a$, so $F \subseteq E$.

:::

:::

::: {.pf-step #size}
$\cardinality{E} = q^{n}$.

::: pf-proof
$E$ is by definition the set of roots in $\overline{F}$ of the polynomial $x^{q^{n}} - x$, whose derivative is $q^{n}x^{q^{n}-1} - 1 = -1$ because $q^{n} = 0$ in characteristic $p$; a polynomial with nonzero constant derivative $-1$ has no repeated root, so $x^{q^{n}} - x$ has exactly $\deg = q^{n}$ distinct roots in $\overline{F}$, that is $\cardinality{E} = q^{n}$.

:::

:::

::: {.pf-step #degree-d}
For every divisor $d$ of $n$ there is $\alpha \in E$ with $[F(\alpha):F] = d$, hence an irreducible polynomial of degree $d$ over $F$.

::: pf-proof
$E$ is a finite field of order $q^{n}$, so $E^{\times}$ is cyclic of order $q^{n}-1$. If $d \mid n$ then $q^{d}-1 \mid q^{n}-1$, so $E^{\times}$ has a subgroup $H_{d}$ of order $q^{d}-1$, namely the unique subgroup of that order in a cyclic group; its fixed field inside $E$ is a subfield $E_{d}$ with $q^{d}$ elements, since the elements of $E_{d}$ are $0$ together with $H_{d}$. An element $\alpha \in E_{d}$ lying in no proper subfield of $E_{d}$ generates $E_{d}$ over $F$, because $F(\alpha) \subseteq E_{d}$ is a subfield containing $\alpha$ and the subfields of $E_{d}$ are its proper subfields; such an $\alpha$ exists since $E_{d}$ is not the union of its finitely many proper subfields. Then $[F(\alpha):F] = [E_{d}:F] = d$, and the minimal polynomial of $\alpha$ over $F$ is irreducible of degree $d$.

:::

:::

::: pf-step
For every positive integer $n$ there is an irreducible polynomial of degree $n$ in $F[x]$.

::: pf-proof
For $n = 1$ this is step [](#n1){.pf-ref}. For $n \ge 2$ apply step [](#degree-d){.pf-ref} with $d = n$: it produces $\alpha \in E$ of degree $n$ over $F$, and the minimal polynomial of $\alpha$ is a monic irreducible element of $F[x]$ of degree $n$.

:::

:::

:::
:::
