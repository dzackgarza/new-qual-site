---
schema: qual/card@1
id: E-HAT-3.A-3
kind: problem
title: "Rational and mod-$p$ cohomology determine integral homology"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.A, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that if $\tilde{H}^n(X; \mathbb{Q})$ and $\tilde{H}^n(X; \mathbb{Z}_p)$ are zero for all $n$ and all primes $p$, then $\tilde{H}_n(X; \mathbb{Z}) = 0$ for all $n$, and hence $\tilde{H}^n(X; G) = 0$ for all $G$ and $n$.
:::

::: {.solution}
For a field $F$, the singular chain complex $C_*(X;F)$ is a chain complex of vector spaces, so dualization is exact. Hence
\[
H^n(X;F)\cong \operatorname{Hom}_F(H_n(X;F),F).
\]
Thus the hypothesis implies
\[
\widetilde H_n(X;\mathbb Q)=0,
\qquad
\widetilde H_n(X;\mathbb Z_p)=0
\]
for every $n$ and every prime $p$.

By the homology universal coefficient theorem,
\[
0\to \widetilde H_n(X;\mathbb Z)\otimes\mathbb Z_p
\to \widetilde H_n(X;\mathbb Z_p)
\to \operatorname{Tor}(\widetilde H_{n-1}(X;\mathbb Z),\mathbb Z_p)
\to0.
\]
Since the middle group is zero for every prime $p$, one has for
\[
A_n=\widetilde H_n(X;\mathbb Z)
\]
both $A_n/pA_n=0$ and $A_n[p]=0$ for every prime $p$. Equivalently, multiplication by every prime is bijective on $A_n$, hence multiplication by every nonzero integer is bijective. Therefore each $A_n$ is naturally a vector space over $\mathbb Q$.

But
\[
0=\widetilde H_n(X;\mathbb Q)\cong A_n\otimes\mathbb Q.
\]
For a $\mathbb Q$-vector space $A_n$, the canonical map $A_n\to A_n\otimes\mathbb Q$ is an isomorphism, so $A_n=0$. Thus
\[
\widetilde H_n(X;\mathbb Z)=0
\]
for all $n$.

Finally the universal coefficient theorem for cohomology gives
\[
0\to \operatorname{Ext}(\widetilde H_{n-1}(X;\mathbb Z),G)
\to \widetilde H^n(X;G)
\to \operatorname{Hom}(\widetilde H_n(X;\mathbb Z),G)\to0,
\]
and both outer groups vanish. Hence
\[
\widetilde H^n(X;G)=0
\]
for every coefficient group $G$ and every $n$.
:::
