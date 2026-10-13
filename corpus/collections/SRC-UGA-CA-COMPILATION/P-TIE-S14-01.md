---
schema: qual/card@1
id: P-TIE-S14-01
kind: problem
title: $\int_\gamma z^n\,dz$ over circles centered at the origin without Cauchy's theorem
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2014, question 1.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the statement and recorded where parts 2 and 3 are carded, against Spring 2014, question 1, page 7 of Questions_from_Tie.pdf.
---

::: {.problem}
The question provides some insight into Cauchy's theorem. Solve the problem without using the Cauchy theorem.

Evaluate the integral $\int_\gamma z^n\,dz$ for all integers $n$. Here $\gamma$ is any circle centered at the origin with the positive (counterclockwise) orientation.
:::

::: {.remark}
This is part 1 of question 1 of the Spring 2014 list in the source.
Part 2 (the same integral over circles not containing the origin) and part 3 (the integral of $\frac{1}{(z-a)(z-b)}$ over $\abs{z} = r$ with $\abs{a} < r < \abs{b}$) are separate cards.
:::

::: {.solution}
Let the positively oriented circle be
$$
\gamma(t)=\rho e^{it},
\qquad
0\le t\le2\pi,
$$
with $\rho>0$.

<1>1. For every integer $n$,
$$
\int_\gamma z^n\,dz
=
i\rho^{n+1}
\int_0^{2\pi}e^{i(n+1)t}\,dt.
$$

::: {.proof}
Along the parametrization,
$$
z^n=\rho^ne^{int},
\qquad
dz=i\rho e^{it}\,dt.
$$
Therefore
$$
\int_\gamma z^n\,dz
=
\int_0^{2\pi}
\rho^ne^{int}
i\rho e^{it}\,dt
=
i\rho^{n+1}
\int_0^{2\pi}e^{i(n+1)t}\,dt.
$$
:::

<1>2. If $n\ne-1$, then
$$
\int_\gamma z^n\,dz=0.
$$

::: {.proof}
If $n\ne-1$, then $n+1$ is a nonzero integer, so
$$
\begin{aligned}
\int_0^{2\pi}e^{i(n+1)t}\,dt
&=
\left[
\frac{e^{i(n+1)t}}{i(n+1)}
\right]_{0}^{2\pi}\\
&=
\frac{e^{2\pi i(n+1)}-1}{i(n+1)}
=0.
\end{aligned}
$$
Step <1>1 then gives the stated value.
:::

<1>3. If $n=-1$, then
$$
\int_\gamma z^{-1}\,dz
=
\boxed{2\pi i}.
$$

::: {.proof}
When $n=-1$, the integrand in step <1>1 becomes $e^0=1$ and $\rho^{n+1}=1$. Hence
$$
\int_\gamma z^{-1}\,dz
=
i\int_0^{2\pi}1\,dt
=
2\pi i.
$$
:::

<1>4. Therefore, for every integer $n$,
$$
\boxed{
\int_\gamma z^n\,dz
=
\begin{cases}
2\pi i,&n=-1,\\
0,&n\ne-1.
\end{cases}
}
$$

::: {.proof}
This combines steps <1>2 and <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the value for every integer $n$ without using Cauchy's theorem.
:::
:::
