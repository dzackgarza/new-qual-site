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
\[
\sum_{n=1}^\infty\mu(A_n)<\infty.
\]
Prove
\[
\mu\!\left(\bigcap_{n=1}^\infty\bigcup_{k=n}^\infty A_k\right)=0.
\]
:::

::: {.solution}
For $n\geq1$, set
$$
B_n=\bigcup_{k=n}^\infty A_k.
$$

<1>1. For every $n$,
$$
\mu(B_n)\leq\sum_{k=n}^\infty\mu(A_k).
$$

::: {.proof}
This is countable subadditivity applied to the family $(A_k)_{k\geq n}$.
:::

<1>2. One has
$$
\mu(B_n)\longrightarrow0.
$$

::: {.proof}
By hypothesis,
$$
\sum_{k=1}^\infty\mu(A_k)<\infty.
$$
Hence the tails
$$
\sum_{k=n}^\infty\mu(A_k)
$$
tend to zero. Step <1>1 then implies $0\leq\mu(B_n)$ is bounded above by a sequence tending to zero.
:::

<1>3. The set
$$
L=\bigcap_{n=1}^\infty B_n
$$
has measure zero.

::: {.proof}
For every $n$, one has $L\subseteq B_n$, so monotonicity of measure gives
$$
0\leq\mu(L)\leq\mu(B_n).
$$
Letting $n\to\infty$ and using step <1>2 yields $\mu(L)=0$.
:::

<1>4. Therefore
$$
\boxed{\mu\!\left(\bigcap_{n=1}^\infty\bigcup_{k=n}^\infty A_k\right)=0}.
$$

::: {.proof}
By definition, the set inside the measure is exactly $L$ from step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
