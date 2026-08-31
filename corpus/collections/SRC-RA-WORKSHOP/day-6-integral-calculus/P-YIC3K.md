---
schema: qual/card@1
id: P-YIC3K
kind: problem
title: $\int_0^1 x^4 f(x)\,dx=\frac15 f(\xi)$ for continuous $f$ on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Mean Value Theorem
  - Integrals
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

Let $f$ be a continuous real-valued function on $[0,1]$.
Prove that there exists at least one point $\xi\in[0,1]$ such that $\int_0^1 x^4 f(x)\,dx=\frac{1}{5}f(\xi)$.

::: {.proof}
*Proof.* Assume that $f$ is a continuous real-valued function on $[0,1]$.
Then, by the Intermediate Value Theorem we have that $f$ attains its maximum and minimum on $[0,1]$.
That is, for some $a,b\in[0,1]$,

$$f(a)=\min\limits_{[0,1]}f(x) \qquad \text{and} \qquad  f(b)=\max\limits_{[0,1]}f(x).$$

We now have $f(a)\leq f(x)\leq f(b)$ for all $x\in[0,1]$.
This gives $$f(a)\int_0^1 x^4dx\leq \int_0^1 x^4f(x)dx\leq f(b)\int_0^1 x^4dx.$$

By the Fundamental Theorem of Calculus we know that

$$\int_0^1x^4dx=\frac{1}{5}.$$

Thus, it follows that

$$\frac{1}{5}f(a)\leq\int_0^1 x^4f(x)dx\leq \frac{1}{5}f(b)$$ giving

$$f(a)\leq 5\int_0^1 x^4f(x)dx\leq f(b).$$

By the Intermediate Value Theorem, there exists $\xi\in[0,1]$ such that

$$f(\xi)=5\int_0^1 x^4f(x)dx.$$

Therefore, we have that there exists $\xi\in[0,1]$ such that $\int_0^1 x^4 f(x)dx=\frac{1}{5}f(\xi)$.
◻
:::
::: {.solution}
<1>1. Let $m = \min_{[0,1]} f$ and $M = \max_{[0,1]} f$.
::: {.proof}
$f$ is continuous on the compact set $[0,1]$, so it attains its extrema.
:::
<1>2. $m/5 \le \int_0^1 x^4 f(x)\,dx \le M/5$.
::: {.proof}
$m \le f(x) \le M$ for all $x$, and $x^4 \ge 0$, so $m x^4 \le x^4 f(x) \le M x^4$; integrating and using $\int_0^1 x^4\,dx = 1/5$ gives the claim.
:::
<1>3. $5\int_0^1 x^4 f \in [m, M] = f([0,1])$.
::: {.proof}
by <1>2, $5\int_0^1 x^4 f \in [m, M]$.
:::
Since $f$ is continuous, its image $f([0,1])$ is the interval $[m, M]$ (intermediate value theorem / connectedness).
<1>4. There is $\xi \in [0,1]$ with $\int_0^1 x^4 f(x)\,dx = \frac15 f(\xi)$.
::: {.proof}
by <1>3, $5\int_0^1 x^4f = f(\xi)$ for some $\xi \in [0,1]$.
:::
<1>5. Q.E.D.
:::
