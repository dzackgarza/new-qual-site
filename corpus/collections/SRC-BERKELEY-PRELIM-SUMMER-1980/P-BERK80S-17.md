---
schema: qual/card@1
id: P-BERK80S-17
kind: problem
title: Fixed point of a monotone real function
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 17 of the vendored Berkeley Preliminary Exam, Summer 1980; restored the lost arrow in $f:\mathbb R\to\mathbb R$ and the OCR-split endpoint $100$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: "Verified the supremum argument without assuming continuity: monotonicity alone forces the supremum of the subfixed set to be fixed."
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be monotonically increasing, perhaps discontinuous.
Suppose $0<f(0)$ and $f(100)<100$.
Prove that $f(x)=x$ for some $x$.
:::

::: {.solution}
Set
$$
A=\{x\in[0,100]:x\le f(x)\}.
$$

<1>1. The set $A$ is nonempty and bounded above, so $c=\sup A$ exists and
lies in $[0,100]$.

::: {.proof}
Since $0<f(0)$, one has $0\in A$. By definition $A\subseteq[0,100]$.
:::

<1>2. One has $c\le f(c)$.

::: {.proof}
For every $x\in A$, one has $x\le c$. Because $f$ is monotonically
increasing,
$$
f(x)\le f(c).
$$
But $x\in A$ also gives $x\le f(x)$. Thus
$$
x\le f(c)
\qquad\text{for every }x\in A,
$$
so $f(c)$ is an upper bound for $A$. Since $c$ is the least upper bound,
$c\le f(c)$.
:::

<1>3. One has $c<100$.

::: {.proof}
If $c=100$, then step <1>2 would give $100\le f(100)$, contrary to the
hypothesis $f(100)<100$.
:::

<1>4. One has $f(c)\le c$.

::: {.proof}
Suppose for contradiction that
$$
c<f(c).
$$
Monotonicity gives
$$
f(c)\le f(f(c)).
$$
Since $c<100$ by step <1>3, monotonicity also gives
$$
f(c)\le f(100)<100,
$$
and $f(c)>c\ge0$. Hence $f(c)\in[0,100]$ and $f(c)\le f(f(c))$, so
$f(c)\in A$. But $f(c)>c=\sup A$, a contradiction.
:::

<1>5. $f(c)=c$.

::: {.proof}
Steps <1>2 and <1>4 give $c\le f(c)\le c$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the fixed point $x=c$.
:::
:::
