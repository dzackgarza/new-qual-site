---
schema: qual/card@1
id: P-O4USN
kind: problem
title: $\nu\perp\mu$ and $\nu\ll|\mu|$ implies $\nu=0$
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - radon-nikodym
relations: []
review: draft
solved: true
---

::: problem
Let $\nu, \mu$ be signed measures, and show that
\[
\nu \perp \mu \text{ and } \nu \ll \abs{ \mu} \implies \nu = 0
.\]
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. $\nu \perp \mu$: there is a measurable $A$ with $|\mu|(A) = 0$ and $|\nu|(A^c) = 0$.
    Proof: definition of mutual singularity (equivalently $\nu \perp |\mu|$; singularity with $\mu$ is singularity with $|\mu|$ since $\mu$ and $|\mu|$ are mutually absolutely continuous).

<1>2. $\nu \ll |\mu|$: $|\mu|(E) = 0 \Rightarrow |\nu|(E) = 0$ (and hence $\nu(E) = 0$).
    Proof: definition of absolute continuity.

<1>3. $|\nu|(A^c) = 0$ by <1>1, and $|\nu|(A) = 0$ by <1>2 (since $|\mu|(A) = 0$).
    Proof: <1>2 applied with $E = A$.

<1>4. $|\nu|(X) = |\nu|(A) + |\nu|(A^c) = 0$.
    Proof: additivity over the partition $X = A \sqcup A^c$, using <1>3.

<1>5. Q.E.D.: $|\nu| \equiv 0$, so $\nu \equiv 0$.
    Proof: a signed measure with zero total variation is the zero measure (its positive and negative parts both vanish).
:::
