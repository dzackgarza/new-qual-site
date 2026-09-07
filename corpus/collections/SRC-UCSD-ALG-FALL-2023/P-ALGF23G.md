---
schema: qual/card@1
id: P-ALGF23G
kind: problem
title: "Splitting field with both α and α+1 as roots implies positive characteristic"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 7 of the official UCSD Algebra Qualifying Exam, Fall 2023 source; the irreducibility, splitting-field, and two-root hypotheses agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified that characteristic zero would give a finite Galois group containing an automorphism alpha maps to alpha+1, whose iterates force a nonzero integer to vanish.
---

::: problem
Suppose $F$ is a field, $f \in F[x]$ is irreducible, and $E$ is a splitting field of $f$ over $F$.
Suppose there exists $\alpha \in E$ such that $f(\alpha) = f(\alpha + 1) = 0$.
Prove that the characteristic of $F$ is positive.
:::

::: {.solution}
<1>1. Assume for contradiction that
\[
\operatorname{char}F=0.
\]
Then $E/F$ is a finite Galois extension.
::: {.proof}
In characteristic zero every irreducible polynomial is separable.
Thus $f$ is separable over $F$.
Since $E$ is the splitting field of $f$, the extension $E/F$ is finite, normal, and separable, hence Galois.
:::

<1>2. There exists
\[
\sigma\in\operatorname{Gal}(E/F)
\]
such that
\[
\sigma(\alpha)=\alpha+1.
\]
::: {.proof}
The elements $\alpha$ and $\alpha+1$ are both roots of the irreducible polynomial $f$.
Hence they have the same minimal polynomial over $F$, and the assignment
\[
\alpha\longmapsto\alpha+1
\]
defines an $F$-isomorphism
\[
F(\alpha)\longrightarrow F(\alpha+1)\subseteq E.
\]
Because $E/F$ is normal by <1>1, this $F$-embedding extends to an $F$-automorphism of $E$.
Call that automorphism $\sigma$.
:::

<1>3. For every integer $k\ge0$,
\[
\sigma^k(\alpha)=\alpha+k.
\]
::: {.proof}
The assertion is clear for $k=0$.
If it holds for $k$, then $\sigma$ fixes $F$, and in particular fixes the prime-field element $k\cdot1_F$.
Therefore
\[
\sigma^{k+1}(\alpha)
=\sigma(\alpha+k)
=\sigma(\alpha)+k
=\alpha+1+k
=\alpha+(k+1).
\]
Induction proves the formula.
:::

<1>4. The assumption $\operatorname{char}F=0$ is impossible.
::: {.proof}
By <1>1, the finite group $\operatorname{Gal}(E/F)$ contains $\sigma$.
Let $r\ge1$ be the order of $\sigma$.
Then
\[
\alpha=\sigma^r(\alpha).
\]
Using <1>3,
\[
\alpha=\alpha+r,
\]
so
\[
r\cdot1_F=0.
\]
This contradicts characteristic zero.
:::

<1>5. Therefore $F$ has positive characteristic.
::: {.proof}
Every field has characteristic either $0$ or a prime number.
By <1>4, characteristic zero is excluded, so $\operatorname{char}F>0$.
:::
:::
