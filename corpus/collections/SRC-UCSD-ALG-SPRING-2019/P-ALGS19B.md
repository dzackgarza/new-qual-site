---
schema: qual/card@1
id: P-ALGS19B
kind: problem
title: "Frattini subgroup, Sylow subgroups, and nilpotence"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Suppose $G$ is a finite group, and $\Phi(G)$ is its Frattini subgroup (the intersection
of all maximal subgroups of $G$). Suppose $G/\Phi(G)$ is nilpotent.

(a) Let $P$ be a Sylow $p$-subgroup of $G$. Prove that $P\Phi(G)$ is a normal subgroup
of $G$.

(b) Prove that $P \trianglelefteq G$.

Hint: $P$ is a Sylow $p$-subgroup of $P\Phi(G)$; use Frattini's argument.

(c) Prove that $G$ is nilpotent.
:::

::: {.solution}
<1>1. Put \(\Phi=\Phi(G)\), and let \(P\) be a Sylow \(p\)-subgroup of \(G\). Then
\(P\cap\Phi\) is a Sylow \(p\)-subgroup of \(\Phi\).
::: {.proof}
The Frattini subgroup \(\Phi\) is characteristic, hence normal, in \(G\). For a normal
subgroup \(N\trianglelefteq G\) and a Sylow \(p\)-subgroup \(P\) of \(G\), the
intersection \(P\cap N\) is a Sylow \(p\)-subgroup of \(N\). Apply this with \(N=\Phi\).
:::

<1>2. The subgroup \(P\Phi/\Phi\) is a Sylow \(p\)-subgroup of \(G/\Phi\).
::: {.proof}
By the second isomorphism theorem,
\[
P\Phi/\Phi\cong P/(P\cap\Phi).
\]
Hence
\[
|P\Phi/\Phi|=\frac{|P|}{|P\cap\Phi|}.
\]
By <1>1, the denominator is the full \(p\)-part of \(|\Phi|\), so this quotient has
exactly the full \(p\)-part of \(|G/\Phi|\).
:::

<1>3. Therefore \(P\Phi\trianglelefteq G\).
::: {.proof}
By hypothesis \(G/\Phi\) is finite nilpotent. Every Sylow subgroup of a finite nilpotent
group is normal, so <1>2 gives
\[
P\Phi/\Phi\trianglelefteq G/\Phi.
\]
Taking the inverse image under \(G\to G/\Phi\) yields \(P\Phi\trianglelefteq G\).
:::

<1>4. The subgroup \(P\) is a Sylow \(p\)-subgroup of \(P\Phi\).
::: {.proof}
The \(p\)-part of
\[
|P\Phi|=\frac{|P|\,|\Phi|}{|P\cap\Phi|}
\]
is \(|P|\), because <1>1 says that \(|P\cap\Phi|\) is the full \(p\)-part of \(|\Phi|\).
:::

<1>5. By Frattini's argument,
\[
G=(P\Phi)N_G(P)=\Phi N_G(P).
\]
::: {.proof}
By <1>3, \(P\Phi\trianglelefteq G\), and by <1>4, \(P\) is Sylow in \(P\Phi\).
Frattini's argument therefore gives
\[
G=(P\Phi)N_G(P).
\]
Since \(P\le N_G(P)\), the right side equals \(\Phi N_G(P)\).
:::

<1>6. One has \(N_G(P)=G\), hence \(P\trianglelefteq G\).
::: {.proof}
A basic property of the Frattini subgroup is: if \(H\le G\) and \(H\Phi(G)=G\), then
\(H=G\). Indeed, if \(H<G\), choose a maximal subgroup \(M\) containing \(H\); since
\(\Phi(G)\le M\), one gets \(H\Phi(G)\le M<G\), a contradiction. Apply this to
\(H=N_G(P)\) using <1>5. Thus \(N_G(P)=G\), so \(P\trianglelefteq G\).
:::

<1>7. Every Sylow subgroup of \(G\) is normal; therefore \(G\) is nilpotent.
::: {.proof}
The prime \(p\) was arbitrary, so <1>6 applies to every Sylow subgroup of \(G\). A
finite group is nilpotent if and only if all its Sylow subgroups are normal;
equivalently, it is the internal direct product of its Sylow subgroups. Hence \(G\) is
nilpotent.
:::
:::
