---
schema: qual/card@1
id: P-BKS19-9B
kind: problem
title: Square roots in $S_6$ of elements of $A_6$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 counterexample $\sigma=(1\,2\,3\,4)(5\,6)$. The counterexample is correct; the solution below gives a shorter invariant-orbit proof using the fact that any square root commutes with its square.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified that the proposed element lies in $A_6$, that any square root would preserve the unique two-element $\sigma$-orbit, and that no permutation of two letters squares to the transposition.
---

::: {.problem}
Recall that $S_6$ and $A_6$ are the symmetric and alternating groups on six letters.
Prove or give a counterexample, with explanation: for every $\sigma\in A_6$ there is a $\tau\in S_6$ such that $\tau^2=\sigma$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The permutation
$$
\boxed{\sigma=(1\ 2\ 3\ 4)(5\ 6)}
$$
lies in $A_6$.


::: pf-proof

A $4$-cycle has sign $(-1)^{4-1}=-1$, and a transposition has sign $-1$. The two cycles are disjoint, so
$$
\operatorname{sgn}(\sigma)=(-1)(-1)=1.
$$
Hence $\sigma\in A_6$.

:::

:::

::: {.pf-step #s1-2}

If $\tau\in S_6$ satisfied $\tau^2=\sigma$, then $\tau$ would commute with $\sigma$.


::: pf-proof

Indeed,
$$
\tau\sigma=\tau\tau^2=\tau^3=\tau^2\tau=\sigma\tau.
$$

:::

:::

::: {.pf-step #s1-3}

Any permutation $\tau$ commuting with $\sigma$ must preserve the set $\{5,6\}$.


::: pf-proof

If $x\in\{1,\ldots,6\}$, commutation gives
$$
\tau(\sigma^k x)=\sigma^k(\tau x)
$$
for every integer $k$. Thus $\tau$ carries the $\langle\sigma\rangle$-orbit of $x$ bijectively onto the $\langle\sigma\rangle$-orbit of $\tau x$, preserving orbit cardinality.

The $\sigma$-orbits are
$$
\{1,2,3,4\}
\qquad\text{and}\qquad
\{5,6\},
$$
of respective sizes $4$ and $2$. Since the two-element orbit is unique, it must be preserved by $\tau$.

:::

:::

::: {.pf-step #s1-4}

No $\tau\in S_6$ can satisfy $\tau^2=\sigma$.


::: pf-proof

Suppose such a $\tau$ existed. By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}, its restriction to $\{5,6\}$ would be a permutation of that two-element set and would satisfy
$$
\left(\tau\restrict_{\{5,6\}}\right)^2=(5\ 6).
$$
But the only permutations of a two-element set are the identity and the transposition, and both have square equal to the identity. This is impossible.

:::

:::

::: {.pf-step #s1-5}

Therefore the proposed statement is false.


::: pf-proof

Step [](#s1-1){.pf-ref} gives an element $\sigma\in A_6$, while step [](#s1-4){.pf-ref} proves that it has no square root in $S_6$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} establishes the counterexample.

:::

:::

:::
