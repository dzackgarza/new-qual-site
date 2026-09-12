---
schema: qual/card@1
id: P-ALGS24B
kind: problem
title: 'Sylow intersections and a bound on $[P : P \cap Q]$'
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
Suppose $G$ is a finite group.
Let $\operatorname{Syl}_p(G)$ be the set of Sylow $p$-subgroups of $G$ and $s_p$ the number of elements in $\operatorname{Syl}_p(G)$.

(a) Suppose $P, Q \in \operatorname{Syl}_p(G)$ are distinct.
Prove that
\[
P \cap N_G(Q) = P \cap Q.
\]

(b) Suppose $P \in \operatorname{Syl}_p(G)$ and consider the action of $P$ on $\operatorname{Syl}_p(G)$ by conjugation.
Prove that the $P$-orbit of $Q \in \operatorname{Syl}_p(G)$ has $[P : P \cap Q]$ many elements.

(c) Suppose $p^e \mid (s_p - 1)$ and $p^{e+1} \nmid (s_p - 1)$.
Prove that there are distinct $P, Q \in \operatorname{Syl}_p(G)$ such that
\[
[P : P \cap Q] \leq p^e.
\]
:::


::: {.solution}
**(a).**

<1>1. Set
\[
H=P\cap N_G(Q).
\]
Then \(H\) is a \(p\)-subgroup of \(N_G(Q)\), and \(H\) normalizes \(Q\).
::: {.proof}
The subgroup \(H\) lies in the \(p\)-group \(P\), so it is a \(p\)-group. By definition \(H\le N_G(Q)\), so every element of \(H\) normalizes \(Q\).
:::

<1>2. The product \(HQ\) is a \(p\)-subgroup of \(G\) containing \(Q\).
::: {.proof}
Because \(H\le N_G(Q)\), the subgroup \(Q\) is normal in \(HQ\), so \(HQ\) is a subgroup and
\[
|HQ|=\frac{|H||Q|}{|H\cap Q|},
\]
a power of \(p\). It contains \(Q\).
:::

<1>3. Hence \(HQ=Q\), so \(H\le Q\).
::: {.proof}
The subgroup \(Q\) is a Sylow \(p\)-subgroup of \(G\), hence maximal among \(p\)-subgroups. By <1>2, \(HQ\) is a \(p\)-subgroup containing \(Q\), so equality holds.
:::

<1>4. Therefore
\[
P\cap N_G(Q)=P\cap Q.
\]
::: {.proof}
By <1>3, \(H=P\cap N_G(Q)\le Q\), hence \(H\le P\cap Q\). Conversely, \(P\cap Q\le P\), and \(Q\le N_G(Q)\), so \(P\cap Q\le P\cap N_G(Q)=H\).
:::

**(b).**

<1>5. Under the conjugation action of \(P\) on \(\operatorname{Syl}_p(G)\), the stabilizer of \(Q\) is
\[
\operatorname{Stab}_P(Q)=P\cap N_G(Q)=P\cap Q.
\]
::: {.proof}
An element \(x\in P\) fixes \(Q\) exactly when \(xQx^{-1}=Q\), i.e. exactly when \(x\in N_G(Q)\). The second equality is part (a).
:::

<1>6. The \(P\)-orbit of \(Q\) has
\[
[P:P\cap Q]
\]
elements.
::: {.proof}
Orbit–stabilizer and <1>5 give
\[
|P\cdot Q|=[P:\operatorname{Stab}_P(Q)]=[P:P\cap Q].
\]
:::

**(c).**

<1>7. Fix \(P\in\operatorname{Syl}_p(G)\) and decompose \(\operatorname{Syl}_p(G)\) into orbits for the conjugation action of \(P\). The singleton \(\{P\}\) is one orbit, and every other orbit has size a positive power of \(p\).
::: {.proof}
The subgroup \(P\) is fixed by conjugation by its own elements. By <1>6, the orbit of any \(Q\ne P\) has size \([P:P\cap Q]\), which is a power of \(p\). Since \(Q\ne P\), the intersection is proper in \(P\), so the orbit size is greater than \(1\).
:::

<1>8. If every orbit other than \(\{P\}\) had size divisible by \(p^{e+1}\), then
\[
p^{e+1}\mid(s_p-1).
\]
::: {.proof}
The number \(s_p-1\) is the sum of the sizes of all nontrivial orbits. If each summand were divisible by \(p^{e+1}\), so would their sum.
:::

<1>9. Therefore some \(Q\ne P\) has orbit size at most \(p^e\), and hence
\[
[P:P\cap Q]\le p^e.
\]
::: {.proof}
The hypothesis says \(p^{e+1}\nmid(s_p-1)\), so by the contrapositive of <1>8 at least one nontrivial orbit has size not divisible by \(p^{e+1}\). By <1>7 its size is a power of \(p\), so it is at most \(p^e\). Apply <1>6 to that orbit.
:::
:::
