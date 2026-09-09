---
schema: qual/card@1
id: P-ALGS14B
kind: problem
title: Unique Sylow containing each $p$-subgroup; unique Sylow in $G/N$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $G$ be a finite group.
Suppose for any $p$-subgroup $Q$ of $G$, there is a unique Sylow $p$-subgroup $P$ which contains $Q$.
Moreover, assume $G$ has a normal subgroup $N$ such that $p \mid |N|$.

(a) Show that if $P_1$ and $P_2$ are two Sylow $p$-subgroups, then $nP_1 n^{-1} = P_2$ for some $n \in N$.
(Hint: Consider a Sylow $p$-subgroup of $N$.)

(b) Show that $G/N$ has a unique Sylow $p$-subgroup.
:::

::: {.solution}
<1>1. For every Sylow \(p\)-subgroup \(P\) of \(G\), the intersection \(P\cap N\) is a Sylow \(p\)-subgroup of \(N\).
::: {.proof}
Let \(R\) be a Sylow \(p\)-subgroup of \(N\). Since \(R\) is a \(p\)-subgroup of \(G\), it is contained in some Sylow \(p\)-subgroup \(S\) of \(G\). All Sylow \(p\)-subgroups of \(G\) are conjugate, so \(S=gPg^{-1}\) for some \(g\in G\). Because \(N\trianglelefteq G\),
\[
R\le S\cap N=g(P\cap N)g^{-1}.
\]
Thus \(|R|\le |P\cap N|\). The reverse inequality holds because \(P\cap N\) is itself a \(p\)-subgroup of \(N\). Hence equality holds and \(P\cap N\) is Sylow in \(N\).
:::

<1>2. Let \(P_1,P_2\) be Sylow \(p\)-subgroups of \(G\). Then there exists \(n\in N\) such that
\[
n(P_1\cap N)n^{-1}=P_2\cap N.
\]
::: {.proof}
By <1>1, both intersections are Sylow \(p\)-subgroups of \(N\), so Sylow conjugacy inside the group \(N\) gives such an \(n\in N\).
:::

<1>3. For this \(n\), we have \(nP_1n^{-1}=P_2\).
::: {.proof}
Both \(nP_1n^{-1}\) and \(P_2\) are Sylow \(p\)-subgroups of \(G\), and both contain the \(p\)-subgroup \(P_2\cap N\): indeed
\[
n(P_1\cap N)n^{-1}=P_2\cap N.
\]
By the hypothesis that every \(p\)-subgroup of \(G\) is contained in a unique Sylow \(p\)-subgroup, the two Sylow subgroups must be equal.
This proves part (a).
:::

<1>4. If \(P\) is a Sylow \(p\)-subgroup of \(G\), then \(PN/N\) is a Sylow \(p\)-subgroup of \(G/N\).
::: {.proof}
Write \(|G|_p\) and \(|N|_p\) for the \(p\)-parts of the two orders.
By <1>1, \(|P\cap N|=|N|_p\), while \(|P|=|G|_p\). Hence
\[
|PN/N|=|P/(P\cap N)|=\frac{|G|_p}{|N|_p}=|G/N|_p,
\]
so \(PN/N\) has the full \(p\)-part of \(|G/N|\).
:::

<1>5. Every Sylow \(p\)-subgroup of \(G/N\) is of the form \(PN/N\) for some Sylow \(p\)-subgroup \(P\le G\).
::: {.proof}
Let \(\overline Q\) be a Sylow \(p\)-subgroup of \(G/N\), and let \(H\) be its full inverse image in \(G\). Choose a Sylow \(p\)-subgroup \(P\) of \(H\). Since
\[
|H|=|N|\,|\overline Q|,
\]
the \(p\)-part of \(|H|\) is \(|N|_p|G/N|_p=|G|_p\). Thus \(P\) is also a Sylow \(p\)-subgroup of \(G\). The image \(PN/N\) is a Sylow \(p\)-subgroup of \(G/N\) by <1>4 and lies in \(\overline Q\); equality follows.
:::

<1>6. The quotient \(G/N\) has a unique Sylow \(p\)-subgroup.
::: {.proof}
Let \(P_1,P_2\) be Sylow \(p\)-subgroups of \(G\). By part (a), \(P_2=nP_1n^{-1}\) for some \(n\in N\). Therefore
\[
P_2N=nP_1n^{-1}N=P_1N,
\]
so \(P_1N/N=P_2N/N\). By <1>5 every Sylow \(p\)-subgroup of \(G/N\) arises this way, hence they are all equal.
:::
:::
