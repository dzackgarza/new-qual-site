---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-10
kind: problem
title: A differential inequality with zero initial value
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Mean Value Theorem
relations: []
review: draft
---

::: {.problem}
(January 2005 #6) Suppose that $f:[0,1]\to\mathbb R$ is a differentiable function with $f(0)=0$ and that there exists some $K>0$ so that $|f'(x)|\le K|f(x)|$ for all $x\in[0,1]$.
Prove that $f(x)=0$ on $[0,1]$.

Note: See [Rud76, Chap 5, #26] for a significant hint.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. $f$ is bounded.
Proof: let $M = \sup_{[0,1]}|f(x)| < \infty$ ($f$ differentiable on a compact interval is continuous, hence bounded).
<1>2. Iterated Gronwall bound.
Proof: for $x \in [0,1]$, $f$ is differentiable with $|f'| \le K|f| \le KM$.
Integrating: \[|f(x)| = \left|\int_0^x f'(t)\,dt\right| \le \int_0^x |f'(t)|\,dt \le K\int_0^x |f(t)|\,dt \le K\int_0^x KM\,dt = MK^2 x.\] Iterating: substitute the improved bound $|f(t)| \le MK^2 t$ into the integral: \[|f(x)| \le K\int_0^x MK^2 t\,dt = MK^3\frac{x^2}{2},\] and by induction $|f(x)| \le MK^{n+1}\frac{x^n}{n!}$ for every $n \ge 0$.
<1>3. Conclude.
Proof: for fixed $x \in [0,1]$, $|f(x)| \le MK^{n+1}\frac{x^n}{n!} \le M K \frac{(Kx)^n}{n!} \to 0$ as $n \to \infty$ (for any fixed $Kx$, the factorial beats the exponential).
Hence $f(x) = 0$ for every $x \in [0,1]$.
<1>4. Q.E.D.
:::
