---
schema: qual/card@1
id: PR-Z5VSQ
kind: proposition
title: A homeomorphism can map a measurable set onto a non-measurable set
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Counterexamples
relations: []
review: draft
---

::: {.proposition}
There exist a homeomorphism $\psi\colon[0,1]\to[0,2]$ and a [[D-MDJII|Lebesgue measurable]] set $Z\subseteq[0,1]$ such that $\psi(Z)$ is not Lebesgue measurable.
:::

::: {.proof}
Let $C\subseteq[0,1]$ be the Cantor set and $c\colon[0,1]\to[0,1]$ the Cantor function, which is continuous, nondecreasing, and constant on each component interval of $[0,1]\setminus C$.
Put $\psi(x)\coloneqq x+c(x)$.
Then $\psi$ is continuous and strictly increasing with $\psi(0)=0$ and $\psi(1)=2$, so it is a homeomorphism $[0,1]\to[0,2]$.

On each component interval $I$ of $[0,1]\setminus C$ the function $c$ is constant, so $\psi(I)$ is an interval of the same length as $I$.
These image intervals are pairwise disjoint, so $m(\psi([0,1]\setminus C))=m([0,1]\setminus C)=1$, and therefore $m(\psi(C))=2-1=1$.

Every set of positive Lebesgue measure contains a subset that is not Lebesgue measurable (apply the Vitali construction inside it), so there is a non-measurable $A\subseteq\psi(C)$.
Let $Z\coloneqq\psi\inv(A)\subseteq C$.
Since $m(C)=0$, the set $Z$ has outer measure $0$ and is Lebesgue measurable, while $\psi(Z)=A$ is not.
:::
