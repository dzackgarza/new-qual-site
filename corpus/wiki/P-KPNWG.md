---
schema: qual/card@1
id: P-KPNWG
kind: problem
title: $\lim_{n\to\infty}\int_0^n\frac{\cos(x/n)}{x^2+\cos(x/n)}\,dx$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Calculate the following limit, justifying each step of your calculation:
\[
L \da \lim_{n\to \infty} \int_0^n { \cos\qty{x\over n} \over x^2 + \cos\qty{x\over n} }\dx
.\]
:::


:::{.solution}

- If interchanging a limit and integral is justified, we have
\[
L 
&\da \lim_{n\to \infty} \int_{(0, n)} {\cos\qty{x\over n} \over x^2 + \cos\qty{x\over n} } \dx \\
&= \lim_{n\to \infty} \int_{(0, \infty)} \chi_{(0, n)}(x) {\cos\qty{x\over n} \over x^2 + \cos\qty{x\over n} } \dx \\
&\equalsbecause{\text{DCT}} \int_{(0, \infty)} \lim_{n\to \infty} \chi_{(0, n)}(x) {\cos\qty{x\over n} \over x^2 + \cos\qty{x\over n} } \dx \\
&= \int_{(0, \infty)} \chi_{(0, \infty)}(x) \lim_{n\to \infty} {\cos\qty{x\over n} \over x^2 + \cos\qty{x\over n} } \dx \\
&= \int_{(0, \infty)} {\lim_{n\to \infty} \cos\qty{x\over n} \over \lim_{n\to \infty} x^2 + \cos\qty{x\over n} } \dx \\
&= \int_{(0, \infty)} {\cos\qty{\lim_{n\to \infty} {x\over n} } \over x^2 + \cos\qty{\lim_{n\to \infty} {x\over n} } } \dx \\
&= \int_{(0, \infty)} {1\over x^2 + 1}\dx \\
&= \arctan(x)\evalfrom_0^\infty \\
&= {\pi \over 2}
,\]
where we've used that $\cos(\theta)$ is continuous on $\RR$ to pass a limit inside, noting that $x$ is fixed in the integrand.

- Justifying the interchange: DCT.
  Write $f_n(x) \da \cos(x/n) / (x^2 + \cos(x/n))$.

- On $(\alpha, \infty)$ for any $\alpha > 1$:

  - We have
  \[
  \abs{f_n(x)} \leq 
  \abs{1\over x^2 + \cos(x/n)} \leq {1\over x^2-1}
  ,\]
  where we've used that $-1\leq \cos(x/n) \leq 1$ for every $x$, and so the denominator is minimized when $\cos(x/n) = -1$, and this maximizes the quantity.
  - Setting $g(x) \da 1/(x^2-1)$, we have $g\in L^1(\alpha, \infty)$ by the limit comparison test with $h(x) \da x^2$:
  \[
  {g(x) \over h(x) } \da {x^2 -1 \over x^2 } = 1 - {1\over x^2} \converges{x\to \infty}\too 1 < \infty
  ,\]
  and so $g, h$ either both converge or both diverge.
  But $\int_\alpha^\infty {1\over x^2}\dx < \infty$ by the $p\dash$test for integrals since $\alpha>1$.

- On $(0, \alpha)$:

  - Just use that $f_n(x)$ is bounded by a constant:
  \[
  \abs{f_n(x)} 
  = \abs{\cos(x/n) \over x^2 + \cos(x/n)}
  \leq \abs{\cos(x/n) \over \cos(x/n)} = 1
  ,\]
  where we've used that $x^2$ is positive, and removing it from the denominator only makes the quantity larger.
  - Then check that $\int_0^\alpha 1 \dx = \alpha < \infty$, so $1\in L^1(0, \alpha)$.
    
:::


