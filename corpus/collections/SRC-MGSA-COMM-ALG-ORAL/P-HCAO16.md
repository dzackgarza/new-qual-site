---
schema: qual/card@1
id: P-HCAO16
kind: problem
title: Definition of a Dedekind domain
classification:
  areas:
  - algebra
  topics:
  - Dedekind Domains
  - Noetherian Rings
  - Integral Closure
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Define a Dedekind domain.
:::

::: {.solution}

No retained solution set covers this question, and the card asks for a definition: the definition is recorded with the two remarks that make it usable, the equivalence with dimension one for non-fields being proved rather than asserted.

::: pf

::: {.pf-step #definition}
A Dedekind domain is an integral domain $R$ that is Noetherian, integrally closed in its fraction field, and such that every nonzero prime ideal of $R$ is maximal.

::: pf-proof
This is the definition (the three conditions are stated separately because all three are used: Noetherianness for finite generation of ideals, integral closedness for the valuation-theoretic behaviour of localisations, and the prime-maximal condition for the unique factorisation of ideals into primes).
:::

:::

::: {.pf-step #dimension}
For a Dedekind domain $R$ that is not a field, "every nonzero prime is maximal" is equivalent to $\dim R=1$.

::: pf-proof
$R$ is not a field, so $(0)$ is prime and not maximal, and $\dim R\ge1$. If every nonzero prime is maximal, a chain of primes $P_{0}\subsetneq P_{1}\subsetneq\cdots$ has $P_{0}=(0)$ and then $P_{1}$ already maximal, so no chain has length $2$ and $\dim R=1$. Conversely if $\dim R=1$ and $P\ne(0)$ is prime, then $P$ is contained in a maximal ideal $M$; the chain $P\subseteq M$ has length at most $1$ and $P\ne(0)$, so $P=M$ and $P$ is maximal.
:::

:::

::: {.pf-step #conventions}
A field is Noetherian and integrally closed and satisfies the third condition vacuously, so conventions differ on whether fields are Dedekind domains; those that exclude them require $\dim R=1$ exactly.

::: pf-proof
A field has no nonzero prime ideal, since every ideal of a field is $(0)$ or the whole ring, so the third condition holds vacuously; it is Noetherian (its only ideals are finitely generated) and integrally closed in itself. Its Krull dimension is $0$, so requiring $\dim R=1$ excludes exactly the fields.
:::

:::

::: {.pf-qed}
The definition is step [](#definition){.pf-ref}, with the dimension reformulation for non-fields in step [](#dimension){.pf-ref} and the status of fields in step [](#conventions){.pf-ref}.
:::

:::

:::
