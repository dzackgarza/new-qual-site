---
schema: qual/card@1
id: P-LARQ13
kind: problem
title: A cyclic module over a PID is a quotient
classification:
  areas: [algebra]
  topics: [Module Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the cyclic-module and PID hypotheses with Lerman practice problem 13."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Used the canonical surjection from R to a cyclic module, identified its kernel as a principal ideal, and applied the module first isomorphism theorem."
---

::: {.problem}
Let $M$ be a cyclic module over a principal ideal domain $R$.
Prove that $M\cong R/(a)$ as an $R$-module for some $a\in R$.
:::

::: {.solution}
<1>1. A chosen cyclic generator gives a surjective homomorphism from $R$.
::: {.proof}
Since $M$ is cyclic, choose $m\in M$ with
$$
M=Rm.
$$
Define
$$
\Phi:R\to M,
\qquad
\Phi(r)=rm.
$$
This is an $R$-module homomorphism. It is surjective because every element of $M$ has the form $rm$.
:::

<1>2. The kernel is principal, so the first isomorphism theorem gives the result.
::: {.proof}
The kernel
$$
\ker\Phi=\{r\in R:rm=0\}
$$
is an ideal of $R$. Since $R$ is a principal ideal domain, there exists $a\in R$ with
$$
\ker\Phi=(a).
$$
The first isomorphism theorem for modules therefore gives
$$
R/(a)=R/\ker\Phi\cong\operatorname{im}\Phi=M.
$$
This also covers the zero module: then one may take $a=1$.
:::
:::
