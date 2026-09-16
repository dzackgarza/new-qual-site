---
schema: qual/card@1
id: D-ALGSPACE
kind: definition
title: Étale equivalence relations and algebraic spaces
classification:
  areas:
  - algebraic-geometry
  topics:
  - Algebraic Spaces
  - Etale Topology
  - Quotients
relations:
- kind: uses
  target: D-ETFPPF
- kind: related-to
  target: D-ALGSTACK
review: draft
prompts:
- What is an étale equivalence relation?
- What is an algebraic space?
---

Let $S$ be a scheme, and regard $S$-schemes as sheaves on $(\Sch_{/S})_{\mathrm{et}}$ through their functors of points ([[D-ETFPPF]]).

::: {.definition title="Étale equivalence relation"}
Let $U$ be an $S$-scheme.
An \dfn{étale equivalence relation} on $U$ is an $S$-scheme $R$ with a monomorphism $(s, t) \colon R \to U \times_S U$ such that

1. for every $S$-scheme $T$, the subset $R(T) \subseteq U(T) \times U(T)$ is an equivalence relation on $U(T)$, and

2. the two projections $s, t \colon R \to U$ are étale.

Its \dfn{quotient} $U/R$ is the sheafification, on $(\Sch_{/S})_{\mathrm{et}}$, of the presheaf $T \mapsto U(T)/R(T)$.
:::

::: {.definition title="Algebraic space"}
An \dfn{algebraic space} over $S$ is a sheaf $X$ on $(\Sch_{/S})_{\mathrm{et}}$ such that

1. the diagonal $X \to X \times_S X$ is representable: for every $S$-scheme $T$ and every $T \to X \times_S X$, the fibre product $X \times_{X \times_S X} T$ is a scheme, and

2. there are a scheme $U$ and a morphism $U \to X$ that is étale and surjective, meaning that for every scheme $T \to X$ the base change $U \times_X T \to T$, a morphism of schemes by condition 1, is étale and surjective.

A morphism $U \to X$ as in condition 2 is an \dfn{étale atlas}.
:::

::: {.proposition}
If $U \to X$ is an étale atlas of an algebraic space, then $R = U \times_X U \to U \times_S U$ is an étale equivalence relation and $X \cong U/R$.
Conversely, the quotient $U/R$ of any étale equivalence relation on a scheme $U$ is an algebraic space, with étale atlas $U \to U/R$.
:::

::: {.example}
Every scheme $X$ is an algebraic space, with atlas $\id \colon X \to X$ and $R$ the diagonal.
If a finite group $G$ acts freely on an $S$-scheme $U$, then $R = U \times G \to U \times_S U$, $(u, g) \mapsto (u, ug)$, is an étale equivalence relation, and $U/R$ is an algebraic space, the quotient $U/G$; it is a scheme when, for instance, $U$ is quasiprojective over a field.
:::
