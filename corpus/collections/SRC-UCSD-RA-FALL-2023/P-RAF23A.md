---
schema: qual/card@1
id: P-RAF23A
kind: problem
title: "Distributional derivative of a monotone function, and finite interval covers of countable subsets of $[0,1]$"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
TRUE or FALSE: Prove it if true and disprove it if false.

(i) Let $f(t)$ be a monotone non-increasing function on $\mathbb{R}$.
Then its distributional derivative is always a Radon measure.

(ii) Let $E \subset [0,1] \subset \mathbb{R}$ be a countable subset.
Then for any $\epsilon > 0$, there is a finite cover of $E$ by open intervals $\{I_k\}_{k=1}^{n}$ such that
$$
\sum_{k=1}^{n} m(I_k) < \epsilon.
$$
:::

::: {.solution}
<1>1. Statement (i) is true: $f'=-\mu$ for a positive Radon measure $\mu$ on $\mathbb R$.

<2>1. $f\in L^1_{\text{loc}}(\mathbb R)$, and its distributional derivative is $\langle f',\phi\rangle=-\int_{\mathbb R}f\phi'\,dt$ for $\phi\in C_c^\infty(\mathbb R)$.

::: {.proof}
A monotone function is bounded on every bounded interval and Borel measurable, so it is locally integrable. The formula is the definition of the distributional derivative.
:::

<2>2. $\int_{\mathbb R}f\phi'\,dt\ge0$ for every $\phi\in C_c^\infty(\mathbb R)$ with $\phi\ge0$.

::: {.proof}
Let $\eta\in C_c^\infty(\mathbb R)$ be nonnegative with $\int\eta=1$, put $\eta_\varepsilon(t)=\varepsilon^{-1}\eta(t/\varepsilon)$, and let $f_\varepsilon=f*\eta_\varepsilon$, a smooth function.
For $h>0$,
$$
f_\varepsilon(t+h)-f_\varepsilon(t)=\int_{\mathbb R}\bigl(f(t+h-s)-f(t-s)\bigr)\eta_\varepsilon(s)\,ds\le0,
$$
because $f$ is non-increasing; hence $f_\varepsilon'\le0$.
Integration by parts gives
$$
\int_{\mathbb R}f_\varepsilon\phi'\,dt=-\int_{\mathbb R}f_\varepsilon'\phi\,dt\ge0.
$$
Since $f_\varepsilon\to f$ in $L^1_{\text{loc}}(\mathbb R)$ and $\phi'$ is bounded with compact support, $\int f\phi'=\lim_{\varepsilon\to0^+}\int f_\varepsilon\phi'\ge0$.
:::

<2>3. Q.E.D.

::: {.proof}
By steps <2>1 and <2>2, $-f'$ is a positive distribution. A positive distribution on $\mathbb R$ is given by a unique positive Radon measure $\mu$, $\langle -f',\phi\rangle=\int\phi\,d\mu$ (Riesz–Markov–Kakutani representation theorem applied to $C_c(\mathbb R)$). Hence $f'=-\mu$ is a Radon measure.
:::

<1>2. Statement (ii) is false: for $E=\mathbb Q\cap[0,1]$, every finite cover of $E$ by open intervals $I_k=(a_k,b_k)$ has $\sum_k m(I_k)\ge1$.

::: {.proof}
The set $E$ is countable and contained in $[0,1]$.
If $E\subseteq\bigcup_{k=1}^n I_k$, taking closures gives
$$
[0,1]=\overline{E}\subseteq\overline{\bigcup_{k=1}^n I_k}=\bigcup_{k=1}^n[a_k,b_k],
$$
because a finite union of closed sets is closed.
By monotonicity and subadditivity of Lebesgue measure,
$$
1=m([0,1])\le\sum_{k=1}^n m([a_k,b_k])=\sum_{k=1}^n m(I_k).
$$
So no such cover has total length less than any $\epsilon\in(0,1)$.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 decide statements (i) and (ii).
:::
:::
