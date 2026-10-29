---
schema: qual/card@1
id: P-UCLAB11F-05
kind: problem
title: Riemann-integrable function with infinitely many discontinuities
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
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Problem 5. Give an example of a function $f$ on $[0,1]$ having infinitely many discontinuities but which is Riemann integrable.
Include a proof; do not merely quote a theorem.
:::

::: {.solution}

Define
$$
f(x)=
\begin{cases}
1,&x=1/n\text{ for some }n\in\NN,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf

::: {.pf-step #s1-1}

The function $f$ is discontinuous at every point
$$
\frac1n,
\qquad
n\in\NN.
$$


::: pf-proof

Fix $n$. One has
$$
f(1/n)=1.
$$
Every neighborhood of $1/n$ contains points that are not of the form $1/m$, because the set
$$
\{1/m:m\in\NN\}
$$
has empty interior. At each such nearby point, $f=0$. Therefore values of $f$ arbitrarily close to $1/n$ differ from $f(1/n)$ by $1$, so $f$ is not continuous at $1/n$.

:::

:::

::: {.pf-step #s1-2}

The function $f$ has infinitely many discontinuities.


::: pf-proof

The points
$$
1,\frac12,\frac13,\ldots
$$
are pairwise distinct, and step [](#s1-1){.pf-ref} shows that each is a discontinuity.

:::

:::

::: {.pf-step #s1-3}

Every lower Darboux sum of $f$ on $[0,1]$ is $0$.


::: pf-proof

Every nondegenerate subinterval of $[0,1]$ contains a point not equal to any $1/n$, and $f$ vanishes there. Since $f\ge0$, the infimum of $f$ on every subinterval is therefore $0$. Hence every lower Darboux sum equals $0$.

:::

:::

::: {.pf-step #s1-4}

For every $\varepsilon>0$, there is a partition $P$ such that
$$
U(f,P)<\varepsilon.
$$


::: pf-proof

Fix $\varepsilon>0$. Choose $N$ so large that
$$
\frac1N<\frac{\varepsilon}{2}.
$$
Then all points
$$
\frac1n,
\qquad
n\ge N,
$$
lie in
$$
\left[0,\frac1N\right],
$$
whose length is less than $\varepsilon/2$.

The remaining points
$$
1,\frac12,\ldots,\frac1{N-1}
$$
are finite in number. Choose pairwise disjoint intervals around them, contained in $(1/N,1]$, whose total length is less than $\varepsilon/2$. Form a partition containing all endpoints of these intervals together with $0,1/N,1$.

On every partition subinterval not lying in
$$
\left[0,\frac1N\right]
$$
or in one of the chosen small intervals, the function is identically zero, so its supremum is zero. On the exceptional intervals its supremum is at most $1$. Thus the upper Darboux sum is bounded by the total exceptional length, which is less than
$$
\frac{\varepsilon}{2}+\frac{\varepsilon}{2}
=
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-5}

The function $f$ is Riemann integrable and
$$
\boxed{\int_0^1f(x)\,dx=0}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, every lower sum is $0$, so the lower integral is $0$. By step [](#s1-4){.pf-ref}, upper sums can be made arbitrarily small and are nonnegative, so the upper integral is also $0$. Therefore the upper and lower integrals agree, and $f$ is Riemann integrable with integral $0$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives infinitely many discontinuities, and step [](#s1-5){.pf-ref} proves Riemann integrability directly from Darboux sums.

:::

:::

:::
