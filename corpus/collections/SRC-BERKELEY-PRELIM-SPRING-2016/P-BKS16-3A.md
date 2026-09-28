---
schema: qual/card@1
id: P-BKS16-3A
kind: problem
title: Convergence of $\int f_n^4$ from $\int f_n\to 0$ and $f_n^2\le g$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Checked the statement and counterexample against Problem 3A in the vendored Berkeley Spring 2016 solution packet.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked integrability, the pointwise domination f_n^2 <= g, the vanishing L1 integrals, and the constant fourth-power integrals.
---

::: {.problem}
Suppose $g$ and $f_n$ are nonnegative integrable functions such that
$$
\int f_n\,dx\to 0\qquad\text{as }n\to\infty
$$
and $f_n^2\le g$ for all $n$.
Prove or find a counterexample to the statement that
$$
\int f_n^4\,dx\to 0\qquad\text{as }n\to\infty.
$$
:::

::: {.solution}
The statement is false.

<1>1. On the measure space $(0,1)$ with Lebesgue measure, define
$$
g(x)=x^{-1/2}
$$
and
$$
f_n(x)
=
\begin{cases}
n^{1/4},&0<x\leq1/n,\\
0,&1/n<x<1.
\end{cases}
$$
Then $g$ and every $f_n$ are nonnegative and integrable.

::: {.proof}
Each $f_n$ is a bounded step function supported on an interval of finite measure. Also
$$
\int_0^1g(x)\,dx
=
\int_0^1x^{-1/2}\,dx
=
2.
$$
:::

<1>2. For every $n$ and every $x\in(0,1)$,
$$
f_n(x)^2\leq g(x).
$$

::: {.proof}
If $x>1/n$, then $f_n(x)=0$. If $0<x\leq1/n$, then
$$
f_n(x)^2=n^{1/2}
$$
while
$$
g(x)=x^{-1/2}\geq(1/n)^{-1/2}=n^{1/2}.
$$
:::

<1>3. One has
$$
\int_0^1f_n(x)\,dx
=
n^{-3/4}
\longrightarrow0.
$$

::: {.proof}
By definition,
$$
\int_0^1f_n(x)\,dx
=
n^{1/4}\frac1n
=
n^{-3/4}.
$$
:::

<1>4. Nevertheless,
$$
\int_0^1f_n(x)^4\,dx
=
1
$$
for every $n$.

::: {.proof}
On $(0,1/n]$ one has
$$
f_n(x)^4=n,
$$
and $f_n(x)^4=0$ elsewhere. Hence
$$
\int_0^1f_n(x)^4\,dx
=
n\frac1n
=
1.
$$
:::

<1>5. Thus the proposed conclusion
$$
\int f_n^4\,dx\longrightarrow0
$$
does not follow from the hypotheses.

::: {.proof}
Steps <1>1--<1>3 verify all hypotheses, while step <1>4 shows that the proposed conclusion fails.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 supplies the requested counterexample.
:::
:::
