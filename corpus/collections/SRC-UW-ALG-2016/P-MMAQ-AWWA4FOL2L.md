---
schema: qual/card@1
id: P-MMAQ-AWWA4FOL2L
kind: problem
title: A finite simple group with all proper subgroups abelian is cyclic of prime
  order
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Subgroups
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $G$ be a finite simple group.
Assume that every proper subgroup of $G$ is abelian.
Prove that then $G$ is cyclic of prime order.
:::


::: {.solution}
<1>1. We first prove the special case of Burnside's normal \(p\)-complement theorem needed below: if \(H\) is finite, \(P\in\operatorname{Syl}_p(H)\), and
\[
P\subseteq Z(N_H(P)),
\]
then \(H\) has a normal subgroup \(K\trianglelefteq H\) of order prime to \(p\) such that \(H=KP\) and \(K\cap P=1\).
::: {.proof}
Because \(P\subseteq Z(N_H(P))\), the group \(P\) is abelian.

First we show that fusion in \(P\) is trivial: if \(x\in P\) and \(g x g^{-1}\in P\), then \(gxg^{-1}=x\). Let \(B=\langle x\rangle\) and \(C=gBg^{-1}\le P\). Since \(B\le Z(P)\), the Sylow \(p\)-subgroups \(P\) and \(gPg^{-1}\) both lie in \(C_H(C)\). Hence they are conjugate inside \(C_H(C)\): there is \(c\in C_H(C)\) such that
\[
cgPg^{-1}c^{-1}=P.
\]
Thus \(cg\in N_H(P)\). Since \(P\subseteq Z(N_H(P))\), conjugation by \(cg\) fixes \(x\). But \(c\) centralizes \(gxg^{-1}\in C\), so
\[
x=(cg)x(cg)^{-1}=g x g^{-1}.
\]

Now consider the transfer homomorphism
\[
V:H\longrightarrow P
\]
(the usual transfer takes values in \(P/[P,P]\), which is \(P\) here because \(P\) is abelian). Let \(m=[H:P]\). For \(u\in P\), decompose the right cosets of \(P\) into cycles under right multiplication by \(u\). A cycle of length \(r\), represented by the coset \(Pt\), contributes
\[
t u^r t^{-1}\in P
\]
to \(V(u)\). This element is conjugate in \(H\) to \(u^r\in P\), so trivial fusion makes it equal to \(u^r\). Multiplying over all cycles gives
\[
V(u)=u^m.
\]
Since \(m\) is prime to \(p\), the map \(u\mapsto u^m\) is an automorphism of the finite abelian \(p\)-group \(P\). Therefore \(V|_P\) is surjective, hence \(V\) is surjective. Put \(K=\ker V\). Then \(K\trianglelefteq H\) and
\[
[H:K]=|P|,
\]
so
\[
|K|=\frac{|H|}{|P|}
\]
is prime to \(p\). Hence \(K\cap P=1\), and \(|KP|=|H|\), so \(H=KP\). This proves the lemma.
:::

<1>2. Suppose, for contradiction, that \(G\) is nonabelian and simple. Then \(G\) is not a \(p\)-group for any prime \(p\).
::: {.proof}
A nontrivial finite \(p\)-group has nontrivial center. If \(G\) were a \(p\)-group, its center would be a nontrivial normal subgroup. Simplicity would force \(Z(G)=G\), making \(G\) abelian, contrary to the assumption.
:::

<1>3. Let \(p\mid |G|\) and let \(P\in\operatorname{Syl}_p(G)\). Then \(N_G(P)\) is a proper subgroup of \(G\), hence abelian, and therefore
\[
P\subseteq Z(N_G(P)).
\]
::: {.proof}
By <1>2, \(P\ne G\). If \(N_G(P)=G\), then \(P\trianglelefteq G\), contradicting simplicity because \(1<P<G\). Thus \(N_G(P)<G\). By hypothesis every proper subgroup of \(G\) is abelian, so \(N_G(P)\) is abelian. Since \(P\le N_G(P)\), every element of \(P\) commutes with every element of \(N_G(P)\), giving the claimed inclusion.
:::

<1>4. The assumption that \(G\) is nonabelian simple is impossible.
::: {.proof}
Apply <1>1 to the Sylow subgroup \(P\) from <1>3. We obtain a normal \(p\)-complement \(K\trianglelefteq G\) with
\[
|K|=\frac{|G|}{|P|}.
\]
Because \(P\ne G\), this order is greater than \(1\); because \(P\ne1\), it is strictly less than \(|G|\). Hence
\[
1<K<G,
\]
contradicting simplicity.
:::

<1>5. Therefore \(G\) is abelian.
:::

<1>6. A finite abelian simple group is cyclic of prime order.
::: {.proof}
Let \(1\ne g\in G\). The cyclic subgroup \(\langle g\rangle\) is normal because \(G\) is abelian. Simplicity forces \(\langle g\rangle=G\), so \(G\) is cyclic. If its order were composite, a cyclic group would have a proper nontrivial subgroup, again normal, contradicting simplicity. Hence \(|G|\) is prime.
:::

<1>7. Thus
\[
\boxed{G\cong C_p\text{ for some prime }p}.
\]
