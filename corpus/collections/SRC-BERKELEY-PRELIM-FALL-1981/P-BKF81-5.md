---
schema: qual/card@1
id: P-BKF81-5
kind: problem
title: Ratio limit for Fibonacci numbers
classification:
  areas:
  - prelim
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Solved the recurrence using its two characteristic roots and took the ratio limit from the exponentially smaller second root."
---

::: problem
Let $f_1=1$, $f_2=2$, and $f_{n+1}=f_n+f_{n-1}$. Show that
\[
\lim_{n\to\infty}\frac{f_{n+1}}{f_n}
\]
exists and evaluate it.
:::

::: solution
The characteristic equation of
$$
f_{n+1}=f_n+f_{n-1}
$$
is
$$
r^2-r-1=0.
$$
Its roots are
$$
\phi=\frac{1+\sqrt5}{2},
\qquad
\psi=\frac{1-\sqrt5}{2}.
$$

<1>1. Write an explicit formula for $f_n$.
::: proof
The sequence
$$
f_n=\frac{\phi^{n+1}-\psi^{n+1}}{\sqrt5}
$$
satisfies the recurrence because both $\phi$ and $\psi$ satisfy
$r^2=r+1$. It also gives
$$
f_1=\frac{\phi^2-\psi^2}{\sqrt5}=1,
$$
and
$$
f_2=\frac{\phi^3-\psi^3}{\sqrt5}=2.
$$
By uniqueness for a second-order recurrence with prescribed first two terms,
this is the given sequence.
:::

<1>2. Compute the ratio limit.
::: proof
Since
$$
|\psi|<1<\phi,
$$
we have
$$
\left|\frac\psi\phi\right|<1.
$$
Therefore
$$
\begin{aligned}
\frac{f_{n+1}}{f_n}
&=\frac{\phi^{n+2}-\psi^{n+2}}
{\phi^{n+1}-\psi^{n+1}}\\
&=\phi\,
\frac{1-(\psi/\phi)^{n+2}}
{1-(\psi/\phi)^{n+1}}
\longrightarrow\phi.
\end{aligned}
$$
Hence the limit exists and equals
$$
\boxed{\frac{1+\sqrt5}{2}.}
$$
:::
:::
