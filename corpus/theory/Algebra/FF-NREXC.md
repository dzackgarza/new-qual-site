---
schema: qual/card@1
id: FF-NREXC
kind: fact
title: Nakayama's lemma
prompts:
- What is Nakayama's lemma?
classification:
  areas:
  - algebra
  topics:
  - Nakayama's Lemma
  - Modules
  - Ideals
relations: []
review: draft
---

::: {.fact}
Let $R$ be a commutative ring, let $I\subseteq R$ be an [[D-GOFWL|ideal]], and let $M$ be a finitely generated $R$-module with $IM=M$.
Then there is $i\in I$ with $im=m$ for every $m\in M$.
In particular, if $I$ is contained in the [[D-2IO6Q|Jacobson radical]] $J(R)$, then $M=0$.

Let $(R,\mfm)$ be a [[D-TGB4R|local ring]], let $M$ and $N$ be $R$-modules with $N$ finitely generated, and let $\varphi\colon M\to N$ be $R$-linear.
Then $\varphi$ is surjective if and only if the induced map $M/\mfm M\to N/\mfm N$ of $R/\mfm$-vector spaces is surjective.
:::

::: {.proof}
Let $m_1,\ldots,m_n$ generate $M$.
Since $M=IM$, there are $a_{jk}\in I$ with $m_j=\sum_ka_{jk}m_k$, so the matrix $\mathrm{I}_n-A$, with $A=(a_{jk})$, kills the column vector $(m_1,\ldots,m_n)^t$.
Multiplying by the adjugate of $\mathrm{I}_n-A$ gives $\det(\mathrm{I}_n-A)\,m_j=0$ for every $j$.
Expanding the determinant, $\det(\mathrm{I}_n-A)=1-i$ with $i\in I$, so $m=im$ for every $m\in M$.
If $I\subseteq J(R)$, then $1-i$ is a unit by [[FF-QWCKR]], so $M=0$.

For the local statement, only the converse needs proof.
If $M/\mfm M\to N/\mfm N$ is surjective, then $N=\varphi(M)+\mfm N$, so the finitely generated module $C=N/\varphi(M)$ satisfies $\mfm C=C$, and $C=0$ by the first part with $I=\mfm=J(R)$.
:::
