---
schema: qual/card@1
id: P-UCLAB18S-09
kind: problem
title: Riemann integrability of monotone functions
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2018, `assets/attachments/basic-18S.pdf`.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be non-decreasing, not necessarily continuous.
Prove that $f$ is Riemann integrable on every finite interval $(a,b)$.
If using Lebesgue integration theory, provide complete statements and proofs of all facts used.
:::

::: {.solution}
Fix a finite interval with $a<b$.

<1>1. The function $f$ is bounded on $[a,b]$.

::: {.proof}
Since $f$ is non-decreasing, every $x\in[a,b]$ satisfies
$$
f(a)\le f(x)\le f(b).
$$
Thus $f$ is bounded on $[a,b]$.
:::

<1>2. For the uniform partition
$$
P_N:\quad a=x_0<x_1<\cdots<x_N=b,
\qquad
x_j=a+j\frac{b-a}{N},
$$
one has
$$
U(f,P_N)-L(f,P_N)
=\frac{b-a}{N}\bigl(f(b)-f(a)\bigr).
$$

::: {.proof}
On each subinterval $[x_{j-1},x_j]$, monotonicity gives
$$
\inf_{[x_{j-1},x_j]}f=f(x_{j-1}),
\qquad
\sup_{[x_{j-1},x_j]}f=f(x_j).
$$
Since every subinterval has length $(b-a)/N$,
$$
\begin{aligned}
U(f,P_N)-L(f,P_N)
&=\frac{b-a}{N}\sum_{j=1}^N\bigl(f(x_j)-f(x_{j-1})\bigr)\\
&=\frac{b-a}{N}\bigl(f(b)-f(a)\bigr),
\end{aligned}
$$
where the sum telescopes.
:::

<1>3. For every $\varepsilon>0$, there is a partition $P$ of $[a,b]$ such that
$$
U(f,P)-L(f,P)<\varepsilon.
$$

::: {.proof}
If $f(b)=f(a)$, step <1>2 gives $U(f,P_N)-L(f,P_N)=0$ for every $N$. Otherwise choose
$$
N>\frac{(b-a)(f(b)-f(a))}{\varepsilon}.
$$
Then step <1>2 gives
$$
U(f,P_N)-L(f,P_N)
=\frac{(b-a)(f(b)-f(a))}{N}
<\varepsilon.
$$
:::

<1>4. The function $f$ is Riemann integrable on $[a,b]$, and hence on every finite interval.

::: {.proof}
The Darboux criterion states that a bounded function on a closed finite interval is Riemann integrable if and only if for every $\varepsilon>0$ there is a partition $P$ for which $U(f,P)-L(f,P)<\varepsilon$. Boundedness is step <1>1, and the required partitions are provided by step <1>3. Therefore $f$ is Riemann integrable on $[a,b]$.
:::

<1>5. Q.E.D.

::: {.proof}
The endpoints $a<b$ were arbitrary, so step <1>4 proves the claim for every finite interval.
:::
:::
