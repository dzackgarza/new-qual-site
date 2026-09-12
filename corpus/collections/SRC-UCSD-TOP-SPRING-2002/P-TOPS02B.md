---
schema: qual/card@1
id: P-TOPS02B
kind: problem
title: "An even map from S^n to S^n has even degree"
classification:
  areas:
  - topology
  topics:
  - Degree
  - Spheres
relations: []
review: draft
---

::: problem
Let $f : S^n \to S^n$ be a continuous function such that $f(-x) = f(x)$.
Prove $\deg f$ is even.
:::

::: {.solution}
<1>1. Let $a:S^n\to S^n$ be the antipodal map. Since $f(-x)=f(x)$, we have $f\circ a=f$.
::: {.proof}
This is exactly the hypothesis.
:::

<1>2. If $n$ is even, then $\deg a=(-1)^{n+1}=-1$, hence
$$
\deg f=\deg(f\circ a)=\deg f\,\deg a=-\deg f.
$$
Thus $\deg f=0$.
::: {.proof}
Degree is multiplicative under composition, and the antipodal map on $S^n$ has degree $(-1)^{n+1}$.
:::

<1>3. If $n$ is odd, $f$ factors through the quotient $q:S^n\to\mathbb{RP}^n$:
$$
f=\bar f\circ q.
$$
::: {.proof}
The equality $f(x)=f(-x)$ says precisely that $f$ is constant on antipodal orbits, so it descends to the quotient.
:::

<1>4. For odd $n$, $\mathbb{RP}^n$ is orientable and $q$ has degree $2$, so
$$
\deg f=\deg \bar f\cdot \deg q=2\deg\bar f.
$$
::: {.proof}
The antipodal quotient is an orientation-preserving two-sheeted covering when $n$ is odd, hence has degree $2$.
:::

<1>5. Therefore $\deg f$ is even for every $n$.
::: {.proof}
For even $n$ it is $0$ by <1>2; for odd $n$ it is divisible by $2$ by <1>4.
:::
:::
