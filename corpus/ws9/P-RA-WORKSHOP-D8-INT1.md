---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-INT1
kind: problem
title: 'A jump integrator evaluates a Riemann–Stieltjes integral at zero'
classification:
  areas:
  - real-analysis
  topics:
  - riemann-integrability
  - integrals
  - continuity
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(June 2014, 1) Define $\alpha:[-1,1]\to\mathbb R$ by
$$
\alpha(x):=
\begin{cases}
-1,&x\in[-1,0],\\
1,&x\in(0,1].
\end{cases}
$$
Let $f:[-1,1]\to\mathbb R$ be a function that is uniformly bounded on $[-1,1]$ and continuous at $x=0$, but not necessarily continuous for $x\ne0$.
Prove that $f$ is Riemann--Stieltjes integrable with respect to $\alpha$ over $[-1,1]$ and that
$$
\int_{-1}^{1}f(x)\,d\alpha(x)=2f(0).
$$
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Prove $f \in \mathcal R(\alpha)$ on $[-1,1]$ for the jump integrator $\alpha(x) = -1$ on $[-1,0]$, $1$ on $(0,1]$, given $f$ bounded and continuous at $0$; and $\int_{-1}^1 f\,d\alpha = 2f(0)$.

<1>1. The integrator increments vanish except across the jump at $0$: for any partition, $\Delta\alpha_i = \alpha(x_i) - \alpha(x_{i-1})$ is $2$ when $x_{i-1} \le 0 < x_i$ and $0$ otherwise.
Proof: $\alpha$ is constant $-1$ on $[-1,0]$ and constant $1$ on $(0,1]$, so consecutive values differ only when the interval straddles $0$, where the difference is $1 - (-1) = 2$.

<1>2. Every Stieltjes sum has exactly one nonzero term, and it is $2f(t)$ for a tag $t$ within the interval straddling $0$.
Proof: by <1>1, $S(P, f, \alpha) = \sum_i f(t_i)\Delta\alpha_i = f(t_j)\cdot 2$ where $j$ is the unique index with $x_{j-1} \le 0 < x_j$, and $t_j \in [x_{j-1}, x_j]$.

<1>3. As $\|P\| \to 0$, the straddling tag $t_j \to 0$, so $S(P) \to 2f(0)$.
Proof: $t_j \in [x_{j-1}, x_j]$ and $|x_j - x_{j-1}| \le \|P\| \to 0$ with $x_{j-1} \le 0 \le x_j$; hence $t_j \to 0$, and $f(t_j) \to f(0)$ by continuity of $f$ at $0$.

<1>4. $f \in \mathcal R(\alpha)$ on $[-1,1]$.
Proof: the Stieltjes sums converge to $2f(0)$ as the mesh tends to $0$ (by <1>2–<1>3), which is the definition of Riemann–Stieltjes integrability with integral $2f(0)$.
(Boundedness of $f$ is needed for the standard equivalence with the Darboux–Stieltjes formulation; here the sums converge directly.)

<1>5. Q.E.D. Proof: <1>4 gives integrability and $\int_{-1}^1 f\,d\alpha = \lim S(P) = 2f(0)$.
:::
