---
schema: qual/card@1
id: P-HGRO22
kind: problem
title: 'Center of a nonabelian group of order $p^3$'
classification:
  areas: [algebra]
  topics: [Group Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $p$ be prime, and let $G$ be a nonabelian group of order $p^3$.
Determine the order of the center of $G$.
:::

::: {.solution}
The center has order $p$.

::: pf

::: {.pf-step #s1}

The center $Z(G)$ is nontrivial.

::: pf-proof

Apply the class equation:
\[
|G|=|Z(G)|+\sum_i [G:C_G(x_i)],
\]
where the $x_i$ represent the noncentral conjugacy classes. Each noncentral
class size $[G:C_G(x_i)]$ is a power of $p$ greater than $1$, hence divisible by
$p$. Since $|G|=p^3$ is divisible by $p$, the class equation implies
$p\mid |Z(G)|$.

:::

:::

::: {.pf-step #s2}

The center cannot have order $p^2$ or $p^3$.

::: pf-proof

If $|Z(G)|=p^3$, then $Z(G)=G$, contradicting that $G$ is nonabelian.

If $|Z(G)|=p^2$, then $G/Z(G)$ has order $p$, hence is cyclic. But if
$G/Z(G)$ is cyclic, then $G$ is abelian: if $G/Z(G)=\langle gZ(G)\rangle$,
write $x=g^a z$ and $y=g^b w$ with $z,w\in Z(G)$; then $xy=yx$.
This again contradicts the hypothesis.

:::

:::

::: pf-step

Therefore $|Z(G)|=p$.

::: pf-proof

By step [](#s1){.pf-ref}, the order of the center is one of $p,p^2,p^3$, and step [](#s2){.pf-ref} excludes
the latter two possibilities.

:::

:::

:::

:::
