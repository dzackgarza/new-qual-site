---
schema: qual/card@1
id: P-SW76H
kind: problem
title: The algebraic closure of $F$ in an algebraically closed extension $C$ is algebraically
  closed, and every algebraic $E/F$ embeds in $C$ over $F$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Fields
  - Zorn's Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $F\subset C$ be a field extension with $C$ algebraically closed.

a. Prove that the intermediate field $C_{\text{alg}} \subset C$ consisting of elements algebraic over $F$ is algebraically closed.

b. Prove that if $F\to E$ is an algebraic extension, there exists a homomorphism $E\to C$ that is the identity on $F$.
:::

::: solution
Let
\[
C_{\mathrm{alg}}=\{z\in C:z\text{ is algebraic over }F\}.
\]
It is a field, since sums, products, and inverses of elements algebraic over $F$ are again algebraic over $F$.

For (a), let
\[
g(x)=x^d+a_{d-1}x^{d-1}+\cdots+a_0\in C_{\mathrm{alg}}[x]
\]
be nonconstant. Because $C$ is algebraically closed, $g$ has a root $\alpha\in C$. The field
\[
L=F(a_0,\ldots,a_{d-1})
\]
is algebraic over $F$. Since $\alpha$ satisfies $g$, it is algebraic over $L$, and algebraicity is transitive; hence $\alpha$ is algebraic over $F$. Thus $\alpha\in C_{\mathrm{alg}}$. Every nonconstant polynomial over $C_{\mathrm{alg}}$ therefore has a root there, so $C_{\mathrm{alg}}$ is algebraically closed.

For (b), consider the set of pairs $(L,\varphi)$ where
\[
F\subseteq L\subseteq E
\]
and $\varphi:L\to C$ is an $F$-embedding. Order these pairs by extension. Every chain has an upper bound obtained by taking the union of its fields and compatible embeddings, so Zorn's lemma gives a maximal pair $(L,\varphi)$.

If $L\ne E$, choose $\alpha\in E\setminus L$. Because $E/F$ is algebraic, $\alpha$ is algebraic over $L$. Let $m_\alpha(x)\in L[x]$ be its minimal polynomial. Applying $\varphi$ to the coefficients gives a polynomial $\varphi(m_\alpha)\in C[x]$, which has a root $\beta\in C$ because $C$ is algebraically closed. The assignment $\alpha\mapsto\beta$ extends $\varphi$ to an $F$-embedding
\[
L(\alpha)\longrightarrow C,
\]
contradicting maximality. Hence $L=E$, and the maximal embedding gives the required homomorphism $E\to C$ fixing $F$.
:::
