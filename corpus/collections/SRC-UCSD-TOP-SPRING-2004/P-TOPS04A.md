---
schema: qual/card@1
id: P-TOPS04A
kind: problem
title: "Cohomology ring of a CW-complex from S^n with an (n+1)-cell attached by degree 4"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
Let $X$ be a CW-complex obtained from $S^n$, $n \geq 1$, by attaching a single $(n+1)$-cell by a map $\varphi : S^n \to S^n$ of degree $4$.
Compute the cohomology ring $H^*(X; \mathbb{Z}/2)$.
:::

::: {.solution}
<1>1. With $\mathbb F_2=\mathbb Z/2$ coefficients, the cellular boundary induced by the degree-$4$ attaching map is zero.
::: {.proof}
The cellular boundary $C_{n+1}(X;\mathbb Z)\to C_n(X;\mathbb Z)$ is multiplication by $4$. After reducing coefficients modulo $2$, it becomes zero.
:::

<1>2. Hence additively
$$
H^k(X;\mathbb F_2)\cong
\begin{cases}
\mathbb F_2,&k=0,n,n+1,\\
0,&\text{otherwise}.
\end{cases}
$$
::: {.proof}
The mod-$2$ cellular cochain complex has one copy of $\mathbb F_2$ in degrees $0,n,n+1$ and zero differential.
:::

<1>3. Let $u\in H^n(X;\mathbb F_2)$ and $v\in H^{n+1}(X;\mathbb F_2)$ be the nonzero classes. Then every product involving $v$ and every product of two positive-degree classes other than possibly $u^2$ vanishes for dimensional reasons.
::: {.proof}
The CW complex has dimension $n+1$, so cohomology vanishes above that degree.
:::

<1>4. If $n>1$, then $u^2=0$ since $2n>n+1$.
::: {.proof}
The square lies in $H^{2n}(X;\mathbb F_2)=0$.
:::

<1>5. If $n=1$, then again $u^2=0$.
::: {.proof}
Here $H_1(X;\mathbb Z)\cong\mathbb Z/4$. The class $u\in H^1(X;\mathbb F_2)=\operatorname{Hom}(\mathbb Z/4,\mathbb F_2)$ lifts to a class in $H^1(X;\mathbb Z/4)$ under reduction $\mathbb Z/4\to\mathbb F_2$. Hence its Bockstein for
$$
0\to\mathbb F_2\to\mathbb Z/4\to\mathbb F_2\to0
$$
vanishes. In degree one this Bockstein equals $Sq^1(u)=u^2$, so $u^2=0$.
:::

<1>6. Therefore the ring is the graded $\mathbb F_2$-vector space
$$
\boxed{H^*(X;\mathbb F_2)=\mathbb F_2\{1,u,v\},\quad |u|=n,\ |v|=n+1,}
$$
with all products of positive-degree elements equal to zero.
::: {.proof}
Combine <1>2--<1>5.
:::
:::
