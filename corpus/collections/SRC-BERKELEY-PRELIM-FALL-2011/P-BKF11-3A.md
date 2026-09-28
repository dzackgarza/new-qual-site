---
schema: qual/card@1
id: P-BKF11-3A
kind: problem
title: Holomorphic logarithms of nonvanishing functions on simply connected regions
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 3A of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the primitive of f'/f, the constant quotient argument, and the
    final absorption of the nonzero constant into an exponential.
---

::: {.problem}
Let $U\subseteq\CC$ be a simply connected region, and let
$f:U\to\CC$ be analytic and never zero.
Show that there is an analytic function $g:U\to\CC$ such that $f=e^g$.
:::

::: {.solution}
<1>1. The function
$$
h\coloneqq\frac{f'}{f}
$$
is holomorphic on $U$ and has a holomorphic primitive
$k:U\to\CC$.

::: {.proof}
The function $f$ has no zeros, so $1/f$ is holomorphic on $U$.
Hence $h=f'/f$ is holomorphic. Since $U$ is simply connected, every
holomorphic function on $U$ has a holomorphic primitive. Therefore
there is a holomorphic $k$ with
$$
k'=h=\frac{f'}{f}.
$$
:::

<1>2. There is a constant $c\in\CC^\times$ such that
$$
f=ce^k
$$
on $U$.

::: {.proof}
Differentiate $fe^{-k}$:
$$
\begin{aligned}
(fe^{-k})'
&=f'e^{-k}-fk'e^{-k}\\
&=e^{-k}\left(f'-f\frac{f'}{f}\right)\\
&=0,
\end{aligned}
$$
where step <1>1 gives $k'=f'/f$. Because a region is connected,
$fe^{-k}$ is constant on $U$; write this constant as $c$. Since $f$
never vanishes and $e^{-k}$ never vanishes, $c\ne0$. Thus
$c\in\CC^\times$ and $f=ce^k$.
:::

<1>3. Choose $d\in\CC$ with $e^d=c$ and define
$$
\boxed{g\coloneqq k+d}.
$$
Then $g$ is holomorphic on $U$ and $f=e^g$.

::: {.proof}
Every nonzero complex number has a complex logarithm: writing
$c=re^{i\theta}$ with $r>0$, one may take
$$
d=\log r+i\theta.
$$
The function $g=k+d$ is holomorphic because $k$ is holomorphic and
$d$ is constant. By step <1>2,
$$
e^g=e^{k+d}=e^de^k=ce^k=f.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 constructs the required analytic function $g$.
:::
:::
