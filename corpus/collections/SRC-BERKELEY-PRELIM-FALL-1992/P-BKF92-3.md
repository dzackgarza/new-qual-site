---
schema: qual/card@1
id: P-BKF92-3
kind: problem
title: Roots of $2z^5+4z^2+1$ in the unit disk and on the real axis
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Used Rouche's theorem with 4z^2 on the unit circle, then analyzed the two
    real critical points to show the polynomial crosses the real axis exactly once.
---

::: {.problem}
Let
\[
p(z)=2z^5+4z^2+1.
\]

1. How many roots does $p$ have in the disk $|z|<1$?
2. How many roots does $p$ have on the real axis?
:::

::: {.solution}
<1>1. On the unit circle,
$$
\abs{2z^5+1}<\abs{4z^2}.
$$

::: {.proof}
If $\abs z=1$, then
$$
\abs{2z^5+1}
\le2\abs z^5+1
=3
<4
=\abs{4z^2}.
$$
:::

<1>2. The polynomial $p$ has exactly
$$
\boxed{2}
$$
zeros in $\abs z<1$, counted with multiplicity.

::: {.proof}
By step <1>1 and Rouché's theorem, $p(z)=4z^2+(2z^5+1)$ and $4z^2$ have the same number of zeros in the unit disk. The polynomial $4z^2$ has exactly two zeros there, counted with multiplicity.
:::

<1>3. Put
$$
a\coloneqq\left(\frac45\right)^{1/3}.
$$
The real critical points of $p$ are $-a$ and $0$.

::: {.proof}
For real $x$,
$$
p'(x)=10x^4+8x=2x(5x^3+4).
$$
Thus $p'(x)=0$ exactly when $x=0$ or $x^3=-4/5$, namely $x=-a$.
:::

<1>4. The function $p$ is strictly increasing on $(-\infty,-a)$, strictly decreasing on $(-a,0)$, and strictly increasing on $(0,\infty)$.

::: {.proof}
For $x<-a$, both factors $x$ and $5x^3+4$ are negative, so $p'(x)>0$. For $-a<x<0$, the first factor is negative and the second positive, so $p'(x)<0$. For $x>0$, both are positive, so $p'(x)>0$.
:::

<1>5. Both critical values are positive:
$$
p(-a)>0,
\qquad
p(0)>0.
$$

::: {.proof}
Clearly $p(0)=1$. Since $a^3=4/5$,
$$
\begin{aligned}
p(-a)
&=-2a^5+4a^2+1\\
&=-2a^2a^3+4a^2+1\\
&=-\frac85a^2+4a^2+1\\
&=\frac{12}{5}a^2+1>0.
\end{aligned}
$$
:::

<1>6. The polynomial $p$ has exactly
$$
\boxed{1}
$$
real zero.

::: {.proof}
Since the leading term is $2x^5$,
$$
p(x)\longrightarrow-\infty
\qquad\text{as }x\to-\infty.
$$
By step <1>4, $p$ is strictly increasing on $(-\infty,-a)$, and by step <1>5 it ends that interval at the positive value $p(-a)$. The intermediate value theorem therefore gives exactly one zero on $(-\infty,-a)$.

On $[-a,0]$, step <1>4 shows that $p$ decreases from the positive value $p(-a)$ to the positive value $p(0)$, so it has no zero there. On $(0,\infty)$ it increases from $p(0)>0$, so it has no zero there either.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 answers part 1, and step <1>6 answers part 2.
:::
:::
