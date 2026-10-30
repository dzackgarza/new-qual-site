---
schema: qual/card@1
id: P-BKS80-6
kind: problem
title: Coset action under a small-index factorial bound
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    The statement is false for G=C_2 and H={e}. Checked that this is the only
    exception: the coset action either has a nontrivial proper kernel or is an
    isomorphism onto S_k; in the latter case A_k gives the required normal
    subgroup for k>=3.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source printed the problem for any finite group of order n, which fails for G=C_2, H={e}. The statement now assumes n>2.
---

::: {.problem}
Let $G$ be a finite group of order $n>2$ and $H<G$ a proper subgroup of order $m$.
Assume
$$
(n/m)!<2n.
$$
Prove that $G$ has a proper nontrivial normal subgroup.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Put
$$
k\coloneqq[G:H]=\frac nm.
$$
The action of $G$ on the $k$ left cosets of $H$ gives a homomorphism
$$
\varphi:G\longrightarrow S_k
$$
whose kernel $K$ is a proper normal subgroup of $G$.

::: pf-proof

The kernel of any homomorphism is normal. Since $H$ is proper, $k\ge2$,
and the coset action is transitive on at least two points. Hence the action
is not trivial, so $K\ne G$. Thus $K\lhd G$ and $K$ is proper.

:::

:::

::: {.pf-step #s2}

If $K\ne\{e\}$, then $G$ has the required proper nontrivial normal
subgroup.

::: pf-proof

This is immediate from step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

Suppose $K=\{e\}$. Then
$$
G\cong S_k.
$$

::: pf-proof

If $K$ is trivial, then $\varphi$ is injective, so
$$
n=\cardinality{G}=\cardinality{\varphi(G)}
$$
divides $\cardinality{S_k}=k!$. Therefore
$$
[S_k:\varphi(G)]
=
\frac{k!}{n}.
$$
The hypothesis $k!<2n$ gives
$$
1\le\frac{k!}{n}<2.
$$
The index is an integer, so it equals $1$. Hence
$\varphi(G)=S_k$ and $G\cong S_k$.

:::

:::

::: {.pf-step #s4}

Under the hypothesis of step [](#s3){.pf-ref}, $G$ has a
proper nontrivial normal subgroup.

::: pf-proof

Since $k!=\cardinality{S_k}=n>2$, one has $k\ge3$. The alternating group
$$
A_k
$$
is a proper nontrivial normal subgroup of $S_k$. Transporting it through
the isomorphism in step [](#s3){.pf-ref} gives a proper nontrivial normal subgroup of
$G$.

:::

:::

::: pf-qed

If the kernel $K$ from step [](#s1){.pf-ref} is nontrivial, step [](#s2){.pf-ref} applies. If it is
trivial, step [](#s3){.pf-ref} identifies $G$ with $S_k$, and step [](#s4){.pf-ref} gives the
proper nontrivial normal subgroup.

:::

:::

:::
