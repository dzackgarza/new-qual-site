---
schema: qual/card@1
id: P-BKS83-1
kind: problem
title: A decreasing integrable positive function satisfies $xf(x)\to0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the monotonicity estimate on $[x/2,x]$ and the vanishing tail of the convergent improper integral.
---

::: {.problem}
Let $f:(0,\infty)\to(0,\infty)$ be monotone decreasing and suppose
\[
\int_0^\infty f(x)\,dx<\infty.
\]
Prove that
\[
\lim_{x\to\infty}x f(x)=0.
\]
:::

::: {.solution}
<1>1. For every $x>0$,
$$
\frac{x}{2}f(x)
\le
\int_{x/2}^{x}f(t)\,dt.
$$

::: {.proof}
If
$$
\frac x2\le t\le x,
$$
then monotonicity gives
$$
f(t)\ge f(x).
$$
Therefore
$$
\int_{x/2}^{x}f(t)\,dt
\ge
\int_{x/2}^{x}f(x)\,dt
=
\frac x2 f(x).
$$
:::

<1>2. For every $x>0$,
$$
0
\le
xf(x)
\le
2\int_{x/2}^{\infty}f(t)\,dt.
$$

::: {.proof}
Positivity of $f$ gives the lower bound. By step <1>1,
$$
xf(x)
\le
2\int_{x/2}^{x}f(t)\,dt
\le
2\int_{x/2}^{\infty}f(t)\,dt.
$$
:::

<1>3. One has
$$
\lim_{x\to\infty}
\int_{x/2}^{\infty}f(t)\,dt
=0.
$$

::: {.proof}
The improper integral
$$
\int_0^\infty f(t)\,dt
$$
converges. Hence its tails tend to zero:
$$
\lim_{R\to\infty}
\int_R^\infty f(t)\,dt
=0.
$$
Since $x/2\to\infty$ as $x\to\infty$, the displayed limit follows.
:::

<1>4. Therefore
$$
\boxed{
\lim_{x\to\infty}xf(x)=0
}.
$$

::: {.proof}
Combine steps <1>2 and <1>3 and apply the squeeze theorem.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required limit.
:::
:::
