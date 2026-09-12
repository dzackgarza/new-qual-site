---
schema: qual/card@1
id: P-ALGS15F
kind: problem
title: Characteristic subgroups and self-normalizing Sylow normalizers
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Centralizers and Normalizers
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
Recall that a subgroup $H$ of $K$ is characteristic in $K$, written $H\,\mathrm{char}\,K$, if for every automorphism $\sigma \in \mathrm{Aut}(K)$, we have $\sigma(H) = H$.
Recall also that the notation $K \trianglelefteq G$ means that $K$ is a normal subgroup of $G$.

(a) Prove that if $H\,\mathrm{char}\,K$ and $K \trianglelefteq G$, then $H \trianglelefteq G$.

(b) Prove that if $G$ is a finite group with Sylow-$p$ subgroup $P$ for some prime $p$, and $K = N_G(P)$ is the normalizer of $P$ in $G$, then $N_G(K) = K$.
:::

::: {.solution}
**Part (a).**

<1>1. If $H\,\mathrm{char}\,K$ and $K\trianglelefteq G$, then $H\trianglelefteq G$.
::: {.proof}
Let $g\in G$.
Since $K\trianglelefteq G$, conjugation by $g$ restricts to an automorphism
\[
c_g:K\longrightarrow K,\qquad k\longmapsto gkg^{-1}.
\]
Because $H$ is characteristic in $K$, every automorphism of $K$ preserves $H$.
Hence
\[
gHg^{-1}=c_g(H)=H.
\]
This holds for every $g\in G$, so $H\trianglelefteq G$.
:::

**Part (b).**

<1>2. The subgroup $P$ is the unique Sylow-$p$ subgroup of $K=N_G(P)$.
::: {.proof}
By definition of the normalizer, $P\trianglelefteq K$.
Also $P$ is a Sylow-$p$ subgroup of $K$: indeed $P\le K\le G$, and no $p$-subgroup of $K$ can have order larger than the Sylow-$p$ subgroup $P$ of $G$.
A normal Sylow subgroup is the unique Sylow subgroup of that prime order.
Thus $P$ is the unique Sylow-$p$ subgroup of $K$.
:::

<1>3. Hence $P$ is characteristic in $K$.
::: {.proof}
Every automorphism of $K$ sends a Sylow-$p$ subgroup to a Sylow-$p$ subgroup.
Since $P$ is the unique Sylow-$p$ subgroup of $K$ by <1>2, every automorphism of $K$ fixes $P$.
:::

<1>4. One has $K\trianglelefteq N_G(K)$.
::: {.proof}
This is immediate from the definition of the normalizer: every element of $N_G(K)$ conjugates $K$ to itself.
:::

<1>5. Therefore $P\trianglelefteq N_G(K)$.
::: {.proof}
Apply part (a) to $P\,\mathrm{char}\,K$ from <1>3 and $K\trianglelefteq N_G(K)$ from <1>4.
:::

<1>6. Hence $N_G(K)=K$.
::: {.proof}
If $g\in N_G(K)$, then <1>5 gives $gPg^{-1}=P$.
Thus $g\in N_G(P)=K$, so
\[
N_G(K)\subseteq K.
\]
The reverse inclusion $K\subseteq N_G(K)$ holds for every subgroup $K$ because each element of $K$ normalizes $K$.
Therefore $N_G(K)=K$.
:::
:::
