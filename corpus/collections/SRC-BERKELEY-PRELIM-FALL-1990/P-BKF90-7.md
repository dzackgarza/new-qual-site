---
schema: qual/card@1
id: P-BKF90-7
kind: problem
title: A normal maximal subgroup has finite prime index
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 in the deterministic MinerU Flash extraction assets/attachments/Fall90_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Passed to G/N, used the subgroup correspondence to show that every
    nonidentity element generates the quotient, and ruled out infinite or
    composite order by proper cyclic subgroups.
---

::: {.problem}
Let $N\trianglelefteq G$ with $N\ne G$.
Suppose there is no subgroup $H$ satisfying
\[
N\subsetneq H\subsetneq G.
\]
Prove that $[G:N]$ is finite and prime.
:::

::: {.solution}
Set
$$
Q\coloneqq G/N.
$$

<1>1. The group $Q$ has no nontrivial proper subgroup.

::: {.proof}
By the subgroup correspondence theorem, subgroups of $Q=G/N$ are in bijection with subgroups $H$ of $G$ satisfying
$$
N\subseteq H\subseteq G.
$$
The hypothesis rules out every strict intermediate subgroup, so the only subgroups of $Q$ are the trivial subgroup and $Q$ itself.
:::

<1>2. The group $Q$ is cyclic.

::: {.proof}
Since $N\ne G$, the quotient $Q$ is nontrivial. Choose $q\in Q$ with $q\ne e$. Then $\langle q\rangle$ is a nontrivial subgroup of $Q$, so step <1>1 forces
$$
\langle q\rangle=Q.
$$
:::

<1>3. The element $q$ has finite order.

::: {.proof}
If $q$ had infinite order, then
$$
\langle q^2\rangle
$$
would be a nontrivial proper subgroup of the infinite cyclic group $\langle q\rangle=Q$, contradicting step <1>1.
:::

<1>4. The order of $q$ is prime.

::: {.proof}
Let $m\coloneqq\operatorname{ord}(q)$, which is finite by step <1>3. If $m$ were composite, write
$$
m=rs
$$
with $1<r<m$. Then $q^r\ne e$, while
$$
(q^r)^s=q^m=e.
$$
Thus $\langle q^r\rangle$ would be a nontrivial proper subgroup of $Q=\langle q\rangle$, again contradicting step <1>1. Hence $m$ is prime.
:::

<1>5. The index $[G:N]$ is finite and prime.

::: {.proof}
By step <1>2, $Q=\langle q\rangle$, and by step <1>4 this cyclic group has prime finite order $m$. Therefore
$$
\boxed{[G:N]=\abs{G/N}=m},
$$
which is finite and prime.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
