---
schema: qual/card@1
id: P-BERK92S-06
kind: problem
title: Quadratic factors of $x^4+1$ over $\mathbb F_p$ for $p\equiv3\pmod4$
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $p$ be prime with
\[
p\equiv3\pmod4.
\]
Suppose
\[
x^4+1=g(x)h(x)
\]
in $\mathbb F_p[x]$, where $g,h$ are quadratic. Prove that both $g$ and $h$ are irreducible over $\mathbb F_p$.
:::

::: {.solution}
<1>1. The polynomial $x^4+1$ has no root in $\FF_p$.

::: {.proof}
Suppose $a\in\FF_p$ satisfied $a^4+1=0$. Then $a\ne0$ and
$$
(a^2)^2=-1.
$$
Thus $-1$ would be a square in $\FF_p$. But by Euler's criterion,
$$
(-1)^{(p-1)/2}=-1
$$
because $p\equiv3\pmod4$, whereas every nonzero square $u^2$ satisfies
$$
(u^2)^{(p-1)/2}=u^{p-1}=1.
$$
This contradiction proves the claim.
:::

<1>2. Both $g$ and $h$ are irreducible over $\FF_p$.

::: {.proof}
A reducible quadratic over a field has a linear factor and therefore
a root in that field. If, say, $g$ were reducible, there would be
$a\in\FF_p$ with $g(a)=0$. Since
$$
x^4+1=g(x)h(x),
$$
this would give $a^4+1=0$, contradicting step <1>1. Hence $g$ is
irreducible. The same argument applies to $h$.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 proves both required irreducibility statements.
:::
:::
