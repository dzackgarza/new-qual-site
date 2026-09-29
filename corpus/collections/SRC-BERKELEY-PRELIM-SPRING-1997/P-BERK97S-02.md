---
schema: qual/card@1
id: P-BERK97S-02
kind: problem
title: Distance to a closed subset is continuous and detects membership
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
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $(M,d)$ be a metric space and let $C\subset M$ be nonempty and closed. Define
\[
f(x)=\inf\{d(x,y):y\in C\}.
\]
Show that $f:M\to\mathbb R$ is continuous and that
\[
f(x)=0\iff x\in C.
\]
:::

::: {.solution}
For $x\in M$, write
$$
f(x)=\inf_{y\in C}d(x,y).
$$

::: pf

::: {.pf-step #s1}

For all $x,x'\in M$,
$$
f(x)\leq d(x,x')+f(x').
$$

::: pf-proof

For every $y\in C$, the triangle inequality gives
$$
d(x,y)
\leq
d(x,x')+d(x',y).
$$
Taking the infimum over $y\in C$ yields
$$
f(x)
\leq
d(x,x')+f(x').
$$

:::

:::

::: {.pf-step #s2}

The function $f$ is $1$-Lipschitz:
$$
\abs{f(x)-f(x')}
\leq
d(x,x')
$$
for all $x,x'\in M$.

::: pf-proof

Step [](#s1){.pf-ref} gives
$$
f(x)-f(x')\leq d(x,x').
$$
Interchanging $x$ and $x'$ gives
$$
f(x')-f(x)\leq d(x,x').
$$
Combining these inequalities proves the claim.

:::

:::

::: {.pf-step #s3}

The function $f:M\to\RR$ is continuous.

::: pf-proof

Every Lipschitz function is continuous, and step [](#s2){.pf-ref} gives a Lipschitz
constant equal to $1$.

:::

:::

::: {.pf-step #s4}

If $x\in C$, then
$$
f(x)=0.
$$

::: pf-proof

Taking $y=x$ in the defining infimum gives $f(x)\leq0$. Since every
distance is nonnegative, $f(x)\geq0$. Thus $f(x)=0$.

:::

:::

::: {.pf-step #s5}

If $f(x)=0$, then $x\in C$.

::: pf-proof

Suppose instead that $x\notin C$. Since $C$ is closed, its complement is
open, so there exists $r>0$ such that
$$
B(x,r)\subseteq M\setminus C.
$$
Hence every $y\in C$ satisfies
$$
d(x,y)\geq r,
$$
and therefore
$$
f(x)\geq r>0,
$$
contradicting $f(x)=0$.

:::

:::

::: {.pf-step #s6}

Therefore
$$
\boxed{f(x)=0\iff x\in C}.
$$

::: pf-proof

Step [](#s4){.pf-ref} proves one implication and step [](#s5){.pf-ref} proves the other.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves continuity, and step [](#s6){.pf-ref} identifies the zero set.

:::

:::

:::
