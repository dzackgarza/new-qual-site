---
schema: qual/card@1
id: P-JHUMAY09ANA
kind: problem
title: Meromorphic functions with a logarithmic bound divided by $|z|$
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Isolated Singularities
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the exact bound for every nonzero z and exhaustive formula request with May 2009 problem 1 in the retained JHU source; replaced the truncated title."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Excluded nonzero poles, extended zf across zero, checked vanishing of all positive Taylor coefficients and proved the exact allowed coefficient disk including its boundary."
---

::: {.problem}
1. Find all meromorphic functions f on C such that

$$
| f ( z ) | \leq { \frac { \log ( 2 + | z | ^ { 2 } ) } { | z | } } \qquad { \mathrm { f o r ~ a l l ~ } } z \neq 0 .
$$

Give explicit formulas for the functions and give a proof for your answer.
:::

::: solution
The functions are exactly
$$
\boxed{f(z)=\frac{a}{z},\qquad a\in\mathbb C,\quad |a|\leq\log2,}
$$
viewed as meromorphic functions; $a=0$ gives the identically
zero function.

<1>1. The function $g(z)=zf(z)$ extends to an entire function.
::: proof
At any nonzero point the given upper bound is locally
finite. A pole there would make $|f|$ unbounded in every
punctured neighborhood, contradicting the bound. Thus $f$
is holomorphic on $\mathbb C\setminus\{0\}$. On that set,
$$
|g(z)|\leq\log(2+|z|^2).
$$
This bounds $g$ near zero, so the removable-singularity
theorem gives an entire extension, still denoted $g$
[@SS03]. Continuity preserves the bound at zero as well.
:::

<1>2. The entire extension is constant.
::: proof
Write $g(z)=\sum_{n\geq0}b_nz^n$. For every $R>0$,
Cauchy's coefficient estimate gives
$$
|b_n|\leq \frac{\log(2+R^2)}{R^n}
$$
[@SS03]. For any integer $n\geq1$, the right-hand side
tends to zero as $R\to\infty$: for $R\geq1$ its numerator
is at most $\log3+2\log R$, and $(\log R)/R^n\to0$.
Hence $b_n=0$ for every $n\geq1$. Thus $g=a$ is constant,
and $f(z)=a/z$ on the punctured plane, determining $f$
as a meromorphic function.
:::

<1>3. The coefficient restriction is necessary and sufficient.
::: proof
The original inequality for $f=a/z$ is equivalent, after
multiplication by $|z|>0$, to
$$
|a|\leq\log(2+|z|^2)\qquad(z\ne0).
$$
Letting $|z|\downarrow0$ gives $|a|\leq\log2$.
Conversely, this last bound implies the displayed inequality
for every nonzero $z$, since the logarithm is increasing.
Every such $a/z$ is meromorphic on the plane, with at
most a simple pole at zero. Therefore every stated
coefficient is allowed, and no other function is allowed.
:::
:::
