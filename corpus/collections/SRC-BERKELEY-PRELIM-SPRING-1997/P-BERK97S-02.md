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

<1>1. For all $x,x'\in M$,
$$
f(x)\leq d(x,x')+f(x').
$$

::: {.proof}
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

<1>2. The function $f$ is $1$-Lipschitz:
$$
\abs{f(x)-f(x')}
\leq
d(x,x')
$$
for all $x,x'\in M$.

::: {.proof}
Step <1>1 gives
$$
f(x)-f(x')\leq d(x,x').
$$
Interchanging $x$ and $x'$ gives
$$
f(x')-f(x)\leq d(x,x').
$$
Combining these inequalities proves the claim.
:::

<1>3. The function $f:M\to\RR$ is continuous.

::: {.proof}
Every Lipschitz function is continuous, and step <1>2 gives a Lipschitz
constant equal to $1$.
:::

<1>4. If $x\in C$, then
$$
f(x)=0.
$$

::: {.proof}
Taking $y=x$ in the defining infimum gives $f(x)\leq0$. Since every
distance is nonnegative, $f(x)\geq0$. Thus $f(x)=0$.
:::

<1>5. If $f(x)=0$, then $x\in C$.

::: {.proof}
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

<1>6. Therefore
$$
\boxed{f(x)=0\iff x\in C}.
$$

::: {.proof}
Step <1>4 proves one implication and step <1>5 proves the other.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>3 proves continuity, and step <1>6 identifies the zero set.
:::
:::
