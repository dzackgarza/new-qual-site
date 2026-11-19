---
schema: qual/card@1
id: P-XEOMT
kind: problem
title: $[A_n,A_n]=A_n$ for $n\geq 5$
classification:
  areas:
  - algebra
  topics:
  - Commutators
  - Permutations
  - Simple Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. The prose's two assertions are now
    steps with their reasons: the commutator subgroup is characteristic, hence normal (an
    automorphism carries commutators to commutators), and it is nontrivial because two explicit
    3-cycles do not commute, the disagreement being computed on the point 2. Simplicity of A_n for
    n >= 5 is stated as a quoted theorem, with a step saying that it is not proved on the card,
    rather than presented as proved. The last step notes that perfection alone does not exclude
    A_n trivial, so the nonabelianity clause uses (123) in A_n. Statement unchanged; the card says
    the argument is its own.
---

::: {.problem}
Show that $[A_n, A_n] = A_n$ for $n\geq 5$, so $A_{n\geq 5}$ is nonabelian.
:::

::: {.solution}
$[A_n,A_n]$ is characteristic in $A_n$, hence normal, and it is nontrivial because $A_n$ is nonabelian; simplicity of $A_n$ for $n\ge5$ then forces it to be everything. Simplicity of $A_n$ is quoted, not proved here; what is proved is the nontriviality, by exhibiting two $3$-cycles that do not commute, and the consequence that $A_n$ is perfect and nonabelian. The argument is this card's own: no retained solution set covers this problem.

::: pf

::: {.pf-step #normal}
For $n\ge5$, the commutator subgroup $[A_n,A_n]$ is a normal subgroup of $A_n$.

::: pf-proof
The commutator subgroup is characteristic in any group: an automorphism carries a commutator $xyx^{-1}y^{-1}$ to the commutator of the images, so it maps $[G,G]$ into itself, and applying the same to the inverse automorphism gives equality. A characteristic subgroup is normal, since conjugation by an element is an automorphism. Hence $[A_n,A_n]$ is normal in $A_n$.
:::

:::


::: {.pf-step #nontrivial}
$[A_n,A_n]\ne1$ for $n\ge5$.

::: pf-proof
It is enough to exhibit two elements of $A_n$ that do not commute, since then their commutator is a nonidentity element of the commutator subgroup. Take the $3$-cycles $\sigma=(123)$ and $\tau=(345)$, both even and hence in $A_n$ for $n\ge5$. Compute on $2$, which both cycles move: $\tau(2)=2$ and $\sigma(2)=3$, so $\sigma\tau(2)=3$; while $\sigma(2)=3$ and $\tau(3)=4$, so $\tau\sigma(2)=4$. Hence $\sigma\tau\ne\tau\sigma$ and $[\sigma,\tau]\ne1$.
:::

:::


::: {.pf-step #simple}
$A_n$ is simple for $n\ge5$: its only normal subgroups are $1$ and $A_n$. This is quoted as the standard theorem of the theory of permutation groups and is not proved here.

::: pf-proof
The statement of the problem presupposes it; the proof is the long classification of normal subgroups of $A_n$ by cycle type, which is not reproduced on this card. What the argument below needs is only this: a normal subgroup of $A_n$ other than $1$ equals $A_n$.
:::

:::


::: {.pf-step #equality}
$[A_n,A_n]=A_n$ for $n\ge5$.

::: pf-proof
By steps [](#normal){.pf-ref} and [](#nontrivial){.pf-ref}, $[A_n,A_n]$ is a nontrivial normal subgroup of $A_n$; by step [](#simple){.pf-ref} it equals $A_n$.
:::

:::


::: {.pf-step #conclusion}
$A_n$ is perfect and nonabelian for $n\ge5$, and $[A_n,A_n]=A_n$.

::: pf-proof
$[A_n,A_n]=A_n$ is step [](#equality){.pf-ref}, which is exactly the assertion that $A_n$ is perfect. Perfect groups are nonabelian unless trivial, because an abelian group has trivial commutator subgroup; and $A_n\ne1$ for $n\ge5$, as $(123)\in A_n$. The conclusion $[A_n,A_n]=A_n$ does not by itself give nonabelianity without that last remark, and the nonabelianity is what the statement's final clause asserts.
:::

:::

:::
:::
