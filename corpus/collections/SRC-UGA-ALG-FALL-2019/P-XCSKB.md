---
schema: qual/card@1
id: P-XCSKB
kind: problem
title: Torsion elements form a submodule over an integral domain but not in general,
  and every module over a ring with zero-divisors has torsion
classification:
  areas:
  - algebra
  topics:
  - Torsion
  - Modules
  - Integral Domains
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card's proofs were label-steps with no justifications over
    nested one-sentence claims, ending in a pf-qed that only listed which step settles which
    part. Each part now carries the residue that belongs there: for (a) all four submodule
    conditions, including closure under addition with the product st of the two killing scalars
    — which is exactly where the domain hypothesis enters, and which the card had left as a
    listed bullet; for (b) the verification that 5 is a unit in Z/6 and hence not torsion,
    making the failure of closure explicit; for (c) the two-case argument on bm with the
    commutativity used in a(bm) = (ab)m. Answers unchanged. Not claimed: a retained solution
    set; the collection's provenance is the examination paper only.
---
::: {.problem}
Let $R$ be a commutative ring with identity $1 \ne 0$, and let $M$ be an $R$-module. Recall that the set of torsion elements of $M$ is defined by
$$
\operatorname{tor}(M) = \{m \in M \mid \exists r \in R \setminus \{0\} \text{ such that } r m = 0\}.
$$

(a) Prove that if $R$ is an integral domain, then $\operatorname{tor}(M)$ is an $R$-submodule of $M$.

(b) Give an example where $\operatorname{tor}(M)$ is not an $R$-submodule of $M$.

(c) If $R$ has zero-divisors, prove that every non-zero $R$-module $M \ne \{0\}$ contains at least one non-zero torsion element.
:::

::: {.solution}
Throughout $R$ is a commutative ring with $1 \ne 0$, $M$ is an $R$-module, and $\operatorname{tor}(M) \coloneqq \theset{m \in M \mid rm = 0 \text{ for some } r \in R \setminus\theset{0}}$. The collection's `provenance` is the Fall 2019 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #a}
(a) If $R$ is an integral domain then $\operatorname{tor}(M)$ is an $R$-submodule of $M$.

::: pf-proof
$0 \in \operatorname{tor}(M)$ because $1 \cdot 0 = 0$ and $1 \ne 0$. For closure under addition let $m, m' \in \operatorname{tor}(M)$, with $sm = 0$ and $tm' = 0$ for nonzero $s, t \in R$; then $st(m + m') = (st)m + (st)m' = t(sm) + s(tm') = 0$ by commutativity, and $st \ne 0$ because $R$ is a domain, so $m + m' \in \operatorname{tor}(M)$. For closure under negation, $(-s)m = -(sm) = 0$ with $-s \ne 0$. For scalar multiplication let $m \in \operatorname{tor}(M)$ and $r \in R$ with $sm = 0$, $s \ne 0$; then $s(rm) = r(sm) = 0$ by commutativity, so $rm \in \operatorname{tor}(M)$. These four facts are exactly the submodule conditions.

:::

:::

::: {.pf-step #b}
(b) For $R = \ZZ/6\ZZ$ and $M = R$ the set $\operatorname{tor}(M)$ is not closed under addition, so it is not a submodule.

::: pf-proof
Here $R = \ZZ/6\ZZ$ is not a domain: $\bar 2 \cdot \bar 3 = \bar 0$ with both factors nonzero. The element $\bar 2$ is torsion because $\bar 3 \cdot \bar 2 = \bar 0$ with $\bar 3 \ne \bar 0$, and $\bar 3$ is torsion because $\bar 2 \cdot \bar 3 = \bar 0$ with $\bar 2 \ne \bar 0$. Their sum is $\bar 5$, and $\bar 5$ is a unit, since $\bar 5 \cdot \bar 5 = \overline{25} = \bar 1$. If $r \bar 5 = \bar 0$ then $r = r\bar 5\bar 5 = \bar 0$, so no nonzero $r$ kills $\bar 5$ and $\bar 5 \notin \operatorname{tor}(M)$. Hence $\operatorname{tor}(M)$ contains $\bar 2$ and $\bar 3$ but not their sum.

:::

:::

::: {.pf-step #c}
(c) If $R$ has zero-divisors then every nonzero $R$-module $M$ has a nonzero torsion element.

::: pf-proof
Choose nonzero $a, b \in R$ with $ab = 0$, possible because $R$ is not a domain, and choose $0 \ne m \in M$. If $bm = 0$ then $m$ is a nonzero torsion element, killed by $b \ne 0$. If $bm \ne 0$, put $w \coloneqq bm$, which is nonzero, and compute $aw = a(bm) = (ab)m = 0 \cdot m = 0$; so $w$ is a nonzero torsion element, killed by $a \ne 0$. Either way $M$ has one.

:::

:::

::: {.pf-step #c-concl}
The three assertions hold: $\operatorname{tor}$ is a submodule over a domain, need not be one in general, and is nonzero for every nonzero module over a ring with zero-divisors.

::: pf-proof
Part (a) is step [](#a){.pf-ref}, part (b) step [](#b){.pf-ref} with the pair $\bar 2, \bar 3$, and part (c) step [](#c){.pf-ref} with its two cases.

:::

:::

:::
:::
