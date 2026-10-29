---
schema: qual/card@1
id: P-WESRA13J-II1
kind: problem
title: 'Borel–Cantelli first lemma'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $(X,\mathcal B,\mu)$ be a measure space and let $A_n\in\mathcal B$ satisfy
$$
\sum_{n=1}^\infty\mu(A_n)<\infty.
$$
Prove
$$
\mu\!\left(\bigcap_{n=1}^\infty\bigcup_{k=n}^\infty A_k\right)=0.
$$
:::

::: {.solution}

For $n\geq1$, set
$$
B_n=\bigcup_{k=n}^\infty A_k.
$$

::: pf

::: {.pf-step #s1-1}

For every $n$,
$$
\mu(B_n)\leq\sum_{k=n}^\infty\mu(A_k).
$$


::: pf-proof

This is countable subadditivity applied to the family $(A_k)_{k\geq n}$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\mu(B_n)\longrightarrow0.
$$


::: pf-proof

By hypothesis,
$$
\sum_{k=1}^\infty\mu(A_k)<\infty.
$$
Hence the tails
$$
\sum_{k=n}^\infty\mu(A_k)
$$
tend to zero. Step [](#s1-1){.pf-ref} then implies $0\leq\mu(B_n)$ is bounded above by a sequence tending to zero.

:::

:::

::: {.pf-step #s1-3}

The set
$$
L=\bigcap_{n=1}^\infty B_n
$$
has measure zero.


::: pf-proof

For every $n$, one has $L\subseteq B_n$, so monotonicity of measure gives
$$
0\leq\mu(L)\leq\mu(B_n).
$$
Letting $n\to\infty$ and using step [](#s1-2){.pf-ref} yields $\mu(L)=0$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{\mu\!\left(\bigcap_{n=1}^\infty\bigcup_{k=n}^\infty A_k\right)=0}.
$$


::: pf-proof

By definition, the set inside the measure is exactly $L$ from step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
