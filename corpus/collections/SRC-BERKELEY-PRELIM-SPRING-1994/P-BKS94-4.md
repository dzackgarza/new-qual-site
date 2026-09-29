---
schema: qual/card@1
id: P-BKS94-4
kind: problem
title: Finite-index subgroups contain finite-index normal subgroups
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 1994 preliminary examination.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used the action of G on the finite left-coset set G/A; its kernel is
    normal, finite-index, and contained in A.
---

::: {.problem}
Let G be a group having a subgroup A of finite index. Prove that there is a normal subgroup N of G contained in A such that N is of finite index in G.
:::

::: {.solution}
Let
$$
m\coloneqq[G:A]<\infty.
$$

::: pf

::: pf-step

Left multiplication defines a homomorphism
$$
\varphi:G\longrightarrow\operatorname{Sym}(G/A).
$$

::: pf-proof

For $g\in G$, define
$$
\varphi(g)(xA)=gxA.
$$
This is well defined on left cosets, is a permutation of the finite set
$G/A$, and satisfies
$$
\varphi(gh)=\varphi(g)\varphi(h).
$$
Thus $\varphi$ is a group homomorphism.

:::

:::

::: {.pf-step #s2}

Let
$$
N\coloneqq\ker\varphi.
$$
Then $N$ is normal in $G$ and has finite index.

::: pf-proof

Every kernel is normal. Moreover,
$$
G/N\cong\varphi(G),
$$
and $\varphi(G)$ is a subgroup of the finite group
$\operatorname{Sym}(G/A)\cong S_m$. Hence $G/N$ is finite, so
$[G:N]<\infty$.

:::

:::

::: {.pf-step #s3}

One has
$$
N\subseteq A.
$$

::: pf-proof

If $g\in N$, then $\varphi(g)$ fixes every left coset, in particular the
coset $A$. Thus
$$
gA=A,
$$
which is equivalent to $g\in A$.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} show that $N$ is normal in $G$, contained in $A$, and
of finite index in $G$.

:::

:::

:::
