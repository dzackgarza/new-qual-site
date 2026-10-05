---
schema: qual/card@1
id: P-TRIV-PR12
kind: problem
title: Poisson arrivals at a counter with dead time
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 12, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains one or more nonprinting control bytes at this source position; they were removed from the authored card as nonsemantic extraction artifacts.
---

::: {.problem}
In nuclear physics, the intensity of a particle source is measured with Geiger-Muller counters.
A particle entering the counter generates a discharge in it that lasts time τ , during which the counter does not record any particles entering the counter.
Find the probability that the counter will count all particles entering it during time t if the following conditions are fulfilled:

(a) the particles enter the counter independently;

(b) the probability that during the time interval from t to $t + \Delta t .$ , k particles entered the counter is given by

$$
p _ { k } ( t , t + \Delta t ) = \frac { ( a \Delta t ) ^ { k } e ^ { - a \Delta t } } { k ! } ,\tag{43}
$$

where a is the rate.
:::

::: {.solution}
The arrival process is Poisson with rate $a$. The counter records every particle during $[0,t]$ exactly when no two arrival times in that interval differ by less than $\tau$.

<1>1. Conditional on exactly $n$ arrivals during $[0,t]$, their ordered arrival times
\[
0<T_1<\cdots<T_n<t
\]
are uniformly distributed on the simplex of volume $t^n/n!$.

::: {.proof}
For a homogeneous Poisson process, conditional on $N(t)=n$, the unordered arrival times are independent uniform points on $[0,t]$. Ordering them restricts to the simplex $0<T_1<\cdots<T_n<t$, on which the joint density is constant $n!/t^n$.
:::

<1>2. For fixed $n\geq1$, all particles are counted exactly when
\[
T_{i+1}-T_i\geq\tau
\qquad(1\leq i<n).
\]

::: {.proof}
After each recorded arrival the counter is dead for time $\tau$. Thus the next arrival is recorded exactly when it occurs at least $\tau$ later. Applying this successively gives the stated inequalities.
:::

<1>3. Set
\[
S_i=T_i-(i-1)\tau.
\]
Then the inequalities in step <1>2 are equivalent to
\[
0<S_1<\cdots<S_n<t-(n-1)\tau.
\]

::: {.proof}
One has
\[
S_{i+1}-S_i=T_{i+1}-T_i-\tau.
\]
Thus the separation inequalities are equivalent to $S_{i+1}\geq S_i$; equality occurs on a measure-zero boundary and does not affect probability. The upper bound follows from $T_n<t$.
:::

<1>4. Hence, provided $(n-1)\tau<t$,
\[
P(\text{all counted}\mid N(t)=n)
=\left(1-\frac{(n-1)\tau}{t}\right)^n,
\]
and this conditional probability is zero when $(n-1)\tau\geq t$, except for the measure-zero endpoint case.

::: {.proof}
The translation in step <1>3 has Jacobian $1$. The admissible simplex therefore has volume
\[
\frac{(t-(n-1)\tau)^n}{n!}.
\]
Divide by the full conditional simplex volume $t^n/n!$ from step <1>1.
:::

<1>5. Since
\[
P(N(t)=n)=e^{-at}\frac{(at)^n}{n!},
\]
the required probability is
\[
\boxed{
P(\text{all counted})
=e^{-at}\sum_{n\geq0}
\frac{a^n}{n!}
\bigl(t-(n-1)\tau\bigr)_+^n,}
\]
where the $n=0$ term is $1$ and $x_+=\max(x,0)$.

::: {.proof}
Condition on $N(t)=n$ and multiply the Poisson probability by the conditional probability in step <1>4:
\[
e^{-at}\frac{(at)^n}{n!}
\frac{(t-(n-1)\tau)^n}{t^n}
=e^{-at}\frac{a^n(t-(n-1)\tau)^n}{n!}.
\]
Summing over all feasible $n$ gives the formula; the positive-part notation makes the sum finite automatically.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the probability that no particle arrives during the dead time caused by any preceding particle, which is exactly the event that every entering particle is counted.
:::
:::
