---
schema: qual/card@1
id: E-SMI-8000E-SY4
kind: problem
title: Normalizers of Sylow subgroups are self-normalizing
classification:
  areas:
  - algebra
  topics:
  - Sylow Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Smith 8000e Sylow problem 4."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Observed that P is the unique Sylow p-subgroup of its normalizer, then used conjugation by an element of N(N(P)) to force preservation of P."
---

::: {.exercise}
The "normalizer" $N(H)$ of a subgroup $H$ of $G$ is

$$
N(H) = \ts{g \in G : gHg^{-1} = H}.
$$

If $P$ is a Sylow subgroup of $G$, prove that $N(N(P)) = N(P)$.
:::

::: solution
Write
$$
N=N_G(P).
$$

<1>1. The subgroup $P$ is the unique Sylow $p$-subgroup of $N$.
::: proof
Because every element of $P$ normalizes $P$, one has
$$
P\le N.
$$
Since $P$ is a Sylow $p$-subgroup of $G$, no $p$-subgroup of the subgroup
$N\le G$ can have order larger than $|P|$. Thus $P$ is also a Sylow
$p$-subgroup of $N$.

By definition of $N=N_G(P)$, every element of $N$ conjugates $P$ to itself.
Hence
$$
P\trianglelefteq N.
$$
A normal Sylow subgroup is the unique Sylow subgroup of that prime-power
order. Therefore $P$ is the unique Sylow $p$-subgroup of $N$.
:::

<1>2. Every element normalizing $N$ also normalizes $P$.
::: proof
Let
$$
g\in N_G(N).
$$
Then
$$
gNg^{-1}=N.
$$
Since $P\le N$, it follows that
$$
gPg^{-1}\le N.
$$
Conjugation preserves order, so $gPg^{-1}$ has the same order as $P$ and is
therefore a Sylow $p$-subgroup of $N$. By uniqueness from step <1>1,
$$
gPg^{-1}=P.
$$
Thus
$$
g\in N_G(P)=N.
$$
Hence
$$
N_G(N)\subseteq N.
$$
:::

<1>3. Conclude equality.
::: proof
Every subgroup normalizes itself, so
$$
N\subseteq N_G(N).
$$
Combining this with step <1>2 gives
$$
\boxed{N_G(N_G(P))=N_G(P).}
$$
:::
:::
