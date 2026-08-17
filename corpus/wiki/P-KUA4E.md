---
schema: qual/card@1
id: P-KUA4E
kind: problem
title: $N(N(P))=N(P)$ for a Sylow $p$-subgroup
classification:
  areas:
  - algebra
  topics:
  - sylow-theory
  - centralizers-and-normalizers
  - normal-subgroups
relations: []
review: draft
solved: false
---

::: problem
We'll use the fact that $H \normal N(H)$ for any subgroup $H$ (following directly from the closure axioms for a subgroup), and thus 
$$
P \normal N(P) \quad \text{and}\quad N(P) \normal N^2(P).
$$
Since it is then clear that $N(P) \subseteq N^2(P)$, it remains to show that $N^2(P) \subseteq N(P)$.

So if we let $x \in N^2(P)$, so $x$ normalizes $N(P)$, we need to show that $x$ normalizes $P$ as well, i.e. $xPx\inv = P$.

However, supposing that $\abs G = p^k m$ where $(p, m) = 1$, we have 
$$
P \leq N(P) \leq G ~\implies ~p^k \divides \abs{N(P)} \divides p^km
,$$

so in fact $P \in \mathrm{Syl}(p, N(P))$ since it is a maximal $p\dash$subgroup. 

Then $P' \definedas xPx\inv \in \mathrm{Syl}(p, N(P))$ as well, since all conjugates of Sylow $p\dash$subgroups are also Sylow $p\dash$subgroups.

But since $P \normal N(P)$, there is only *one* Sylow $p\dash$ subgroup of $N(P)$, namely $P$.
This forces $P = P'$, i.e. $P = xPx\inv$, which says that $x \in N(P)$ as desired. $\qed$
:::
