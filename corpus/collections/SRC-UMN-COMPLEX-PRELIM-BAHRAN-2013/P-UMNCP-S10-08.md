---
schema: qual/card@1
id: P-UMNCP-S10-08
kind: problem
title: Iteration toward an attracting fixed point in the disk
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Spring 2010, 8 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Let \(f:\mathbb D\to\mathbb D\) be holomorphic.
Suppose \(c\in\mathbb D\) is a fixed point and \(|f'(c)|<1\). For any \(z_0\in\mathbb D\), define \(z_n=f(z_{n-1})\). Prove that \(z_n\to c\).
:::

::: {.solution}
Define the disk automorphism
$$
\phi(z)
\coloneqq
\frac{z-c}{1-\overline c z},
$$
so that
$$
\phi(c)=0.
$$
Set
$$
g
\coloneqq
\phi\circ f\circ\phi^{-1}.
$$

<1>1. The map
$$
g:\mathbb D\to\mathbb D
$$
is holomorphic, satisfies
$$
g(0)=0,
$$
and
$$
|g'(0)|=|f'(c)|<1.
$$

::: {.proof}
The map $\phi$ is a disk automorphism, so $g$ is a holomorphic self-map of the disk. Since $f(c)=c$,
$$
g(0)
=
\phi(f(c))
=
0.
$$

Also,
$$
\phi'(c)=\frac1{1-|c|^2},
$$
while
$$
(\phi^{-1})'(0)=1-|c|^2.
$$
The chain rule therefore gives
$$
g'(0)
=
\phi'(c)f'(c)(\phi^{-1})'(0)
=
f'(c).
$$
Hence the asserted derivative bound holds.
:::

<1>2. Schwarz's lemma gives
$$
|g(w)|\le|w|
$$
for every
$$
w\in\mathbb D.
$$

::: {.proof}
Step <1>1 gives a holomorphic self-map of the disk fixing $0$, so Schwarz's lemma applies.
:::

<1>3. The function
$$
h(w)=
\begin{cases}
g(w)/w,&w\ne0,\\
g'(0),&w=0
\end{cases}
$$
is holomorphic on $\mathbb D$ and satisfies
$$
\boxed{|h(w)|<1}
$$
for every $w\in\mathbb D$.

::: {.proof}
Since $g(0)=0$, the quotient has a removable singularity at $0$, with value $g'(0)$. Thus $h$ is holomorphic.

Step <1>2 gives
$$
|h(w)|\le1.
$$
If equality held at some point of the disk, the maximum-modulus principle would force $h$ to be a unimodular constant. But
$$
|h(0)|
=
|g'(0)|
<1
$$
by step <1>1. Therefore equality never occurs.
:::

<1>4. Let
$$
w_0=\phi(z_0),
\qquad
w_n=g(w_{n-1}).
$$
Then
$$
w_n=\phi(z_n)
$$
for every $n$.

::: {.proof}
For $n=0$ this is the definition. If
$$
w_{n-1}=\phi(z_{n-1}),
$$
then
$$
\begin{aligned}
w_n
&=
g(w_{n-1})\\
&=
\phi\!\left(
f(\phi^{-1}(\phi(z_{n-1})))
\right)\\
&=
\phi(f(z_{n-1}))\\
&=
\phi(z_n).
\end{aligned}
$$
Thus induction proves the identity.
:::

<1>5. The orbit satisfies
$$
|w_n|\le|w_0|
$$
for every $n$.

::: {.proof}
By step <1>2,
$$
|w_n|
=
|g(w_{n-1})|
\le
|w_{n-1}|.
$$
Iteration gives the claim.
:::

<1>6. If $w_0\ne0$, there exists
$$
q<1
$$
such that
$$
|w_{n+1}|\le q|w_n|
$$
for every $n$.

::: {.proof}
Let
$$
r=|w_0|<1.
$$
By step <1>3, the continuous function $|h|$ is strictly less than $1$ on the compact disk
$$
\{|w|\le r\}.
$$
Hence
$$
q
\coloneqq
\max_{|w|\le r}|h(w)|
<1.
$$
By step <1>5, every $w_n$ lies in this disk. Thus
$$
|w_{n+1}|
=
|g(w_n)|
=
|w_n||h(w_n)|
\le
q|w_n|.
$$
:::

<1>7. One has
$$
\boxed{w_n\to0}.
$$

::: {.proof}
If $w_0=0$, then $w_n=0$ for every $n$ because $g(0)=0$.

If $w_0\ne0$, step <1>6 gives
$$
|w_n|
\le
q^n|w_0|,
$$
and
$$
q^n\to0.
$$
Thus $w_n\to0$.
:::

<1>8. Therefore
$$
\boxed{z_n\to c}.
$$

::: {.proof}
By step <1>4,
$$
z_n=\phi^{-1}(w_n).
$$
Step <1>7 gives $w_n\to0$, and continuity of $\phi^{-1}$ gives
$$
z_n
\longrightarrow
\phi^{-1}(0)
=
c.
$$
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required convergence.
:::
:::
