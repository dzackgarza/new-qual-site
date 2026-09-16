---
schema: qual/card@1
id: P-JHUMAY06AND
kind: problem
title: "Monotone harmonic functions converging to the constant one"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Harnack Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared the monotonicity, strict upper bound and central limit with May 2006 problem 4 on PDF page 40."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Derived the positive-harmonic bound directly from the Poisson kernel on an interior circle, and used a common radius to obtain convergence uniformly on each compact subset."
---

::: {.problem}
4. Let $f _ { n } : D \to ( - \infty , 1 ) , n = 1 , 2 , . . . ,$ be an increasing sequence of harmonic functions on the unit disk D such that $f _ { n } ( 0 ) \to 1$ as $n \to \infty$ . (I.e., $f _ { n } ( z ) \leq f _ { n + 1 } ( z ) < 1 , \forall n \geq 1 . )$ Prove that $f _ { n } ( z ) \to 1$ as $n \to \infty$ , for all $z \in D$
:::

::: {.solution}
Put $u_n=1-f_n$. Each $u_n$ is positive and harmonic on
$D=\{|z|<1\}$, and $u_n(0)\to0$.

<1>1. Values of a positive harmonic function on an interior disk are bounded by its central value.
::: {.proof}
Let $u>0$ be harmonic on $D$, and fix $0\leq r<R<1$.
The Poisson representation on the radius-$R$ disk gives,
for $|z|\leq r$,
$$
u(z)=\frac1{2\pi}\int_0^{2\pi}
\frac{R^2-|z|^2}{|Re^{it}-z|^2}u(Re^{it})\,dt
$$
[@SS03]. It applies since $u$ is harmonic on a neighborhood
of this closed disk. The kernel satisfies
$$
0<\frac{R^2-|z|^2}{|Re^{it}-z|^2}
\leq\frac{R+|z|}{R-|z|}\leq\frac{R+r}{R-r}.
$$
Using positivity of the boundary values and the mean-value
identity at zero therefore gives
$$
0<u(z)\leq\frac{R+r}{R-r}\frac1{2\pi}
\int_0^{2\pi}u(Re^{it})\,dt
=\frac{R+r}{R-r}u(0).
$$
:::

<1>2. Apply the common bound to the sequence.
::: {.proof}
For fixed $r<1$, choose any $R$ with $r<R<1$. Step
<1>1 applied separately to $u_n$ yields
$$
\sup_{|z|\leq r}|1-f_n(z)|
=\sup_{|z|\leq r}u_n(z)
\leq\frac{R+r}{R-r}u_n(0)\longrightarrow0.
$$
Every point of $D$ lies in such a disk. Hence
$f_n(z)\to1$ for every $z\in D$, as required; the
estimate also proves uniform convergence on compact
subsets. Monotonicity is compatible with the proof but
is not needed once positivity of $1-f_n$ and its central
limit are known.
:::
:::
