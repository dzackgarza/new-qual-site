---
title: Domains and factorization
order: 20
topics:
- Integral Domains
- Factorization
- Euclidean Domains
---

# Domains and factorization

Where the tower on [[algebra/rings-and-ideals/which-kind-of-ring|Which kind of ring is this?]] comes from.

## Elements

Factorization starts with divisibility modulo units.
Associates differ by a unit and therefore represent the same factor for uniqueness questions.
An irreducible element cannot be factored nontrivially; a prime element has the stronger divisibility property $p\mid ab\Rightarrow p\mid a$ or $p\mid b$.
The distinction is witnessed by irreducible nonprime elements in $\ZZ[\sqrt{-5}]$.

[[D-AVBIP]]

[[D-QQIQZ]]

[[D-TO3IY]]

[[FD-6LLJF]] [[FD-R4K7Z]]

[[D-AWSKI]]

[[FD-S52W7]]

[[D-R4H6F]]

::: {.remark title="Prime against irreducible"}
Prime implies irreducible in a domain, and the converse holds in a UFD. An irreducible nonprime element proves that a domain is not a UFD.
:::

## Types of ring

The first divide is whether zero divisors exist.
An integral domain has none, while a field goes further and makes every nonzero element a unit.
These hypotheses determine which cancellation and factorization arguments are legal before any stronger finiteness condition is invoked.

[[D-7O2CH]]

[[D-4I3SL]]

[[FD-S62UB]]

[[D-QJ3QL]]

[[FD-2A5XH]]

[[D-UI6CU]]

[[FD-SNOTW]]

[[E-HOJKE]]

### The big ones

The implication chain is
\[
\text{Euclidean domain}\Longrightarrow\text{PID}\Longrightarrow\text{UFD}
\Longrightarrow\text{integral domain}.
\]
A Euclidean function gives an algorithm for gcds, every ideal being principal turns ideal generation into element divisibility, and unique factorization is exactly the stage at which irreducible elements become prime.
None of the reverse implications is automatic, so examples separating adjacent classes are part of the standard toolkit.

[[D-D7VK2]]

[[D-HTIL5]]

[[E-KB4GA]]

[[D-INULL]]

[[FD-25SUQ]]

[[D-NKRGN]]

[[FD-GXXBV]]

### Others

The remaining properties concern ideal chains, nilpotents, maximal ideals, and dimension.
Noetherian means ascending chains of ideals stop; reduced means nilpotents vanish; local means there is a unique maximal ideal.
Valuation rings and DVRs organize divisibility locally, while Dedekind domains replace global element factorization by unique factorization of nonzero ideals.
Regularity is a local dimension/generator condition.

[[D-TZXBO]]

[[D-PQHHJ]]

[[FF-U4FHF]]

[[D-TGB4R]]

[[E-YYL5U]]

[[E-K4SU4]]

[[E-PQ3FR]]

[[D-WUGPG]]

[[E-M6J67]]

[[D-HWLVG]]

[[D-VK2KZ]]

[[D-JSZ77]]

[[FF-CQSNC]]

## Structure theorems

There is a second use of the word "simple" here, now for modules.
Semisimplicity means decomposition as a direct sum of simples, and Artin--Wedderburn classifies semisimple rings by matrix blocks over division rings.
This is structural decomposition rather than element factorization; it is included here because ring hypotheses are often translated immediately into statements about their module categories.

[[D-4KM4P]]

[[D-CYAJI]]

[[T-ZOTWN]]

[[T-GYVNQ]]
