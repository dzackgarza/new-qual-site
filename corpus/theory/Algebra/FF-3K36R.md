---
schema: qual/card@1
id: FF-3K36R
kind: fact
title: Krull's intersection theorem
prompts:
- What is Krull's intersection theorem?
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Commutative Algebra
  - Local Rings
relations: []
review: draft
---

::: {.fact}
Let $R$ be a commutative [[D-TZXBO|Noetherian]] ring and let $I\subseteq R$ be an [[D-GOFWL|ideal]] contained in the [[D-2IO6Q|Jacobson radical]] $J(R)$.
Then
$$
\bigcap_{n\ge0}I^n=0.
$$
In particular, $\bigcap_{n\ge0}\mfm^n=0$ for every Noetherian [[D-TGB4R|local ring]] $(R,\mfm)$.
:::

::: {.proof}
Let $N=\bigcap_{n\ge0}I^n$.
By the [[FF-CSABG|Artin--Rees lemma]] applied to $N\subseteq R$, there is $c\ge0$ with $I^n\cap N=I^{n-c}(I^c\cap N)$ for all $n\ge c$.
Since $N\subseteq I^n$ for every $n$, taking $n=c+1$ gives $N=I(I^c\cap N)=IN$.
The ideal $N$ is finitely generated because $R$ is Noetherian, so [[FF-NREXC|Nakayama's lemma]] with $I\subseteq J(R)$ gives $N=0$.
:::
