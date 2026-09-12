---
schema: qual/card@1
id: P-TOPS05G
kind: problem
title: "Antipodal-preserving map of S^{2k+1} has odd degree"
classification:
  areas:
  - topology
  topics:
  - Degree
  - Antipodal Map
  - Spheres
relations: []
review: draft
---

::: problem
Let $f : S^{2k+1} \to S^{2k+1}$ satisfy $f(-x) = -f(x)$.
Prove the degree of $f$ is odd.
:::

::: {.solution}
<1>1. The equivariant map descends to
$$
\bar f:\mathbb{RP}^{2k+1}\to\mathbb{RP}^{2k+1}.
$$
::: {.proof}
The identity $f(-x)=-f(x)$ sends antipodal orbits to antipodal orbits.
:::

<1>2. The induced map on $\pi_1\cong\mathbb Z/2$ is the identity.
::: {.proof}
A generator lifts to a path from $x$ to $-x$; its image under $f$ is a path from $f(x)$ to $-f(x)$ and therefore projects to the nontrivial loop.
:::

<1>3. Hence if $u\in H^1(\mathbb{RP}^{2k+1};\mathbb F_2)$ is the generator, then
$$
\bar f^*u=u.
$$
::: {.proof}
The unique nonzero class in $H^1(-;\mathbb F_2)$ corresponds to the nontrivial homomorphism $\pi_1\to\mathbb F_2$.
:::

<1>4. Therefore
$$
\bar f^*(u^{2k+1})=u^{2k+1}\ne0.
$$
::: {.proof}
Pullback is multiplicative and
$$
H^*(\mathbb{RP}^{2k+1};\mathbb F_2)=\mathbb F_2[u]/(u^{2k+2}).
$$
:::

<1>5. The integer degree of $\bar f$ is odd.
::: {.proof}
Because $2k+1$ is odd, $\mathbb{RP}^{2k+1}$ is orientable. By <1>4, $\bar f^*$ is nonzero on top cohomology with $\mathbb F_2$ coefficients, so the mod-$2$ reduction of $\deg(\bar f)$ is $1$. Hence $\deg(\bar f)$ is odd.
:::

<1>6. The sphere map $f$ has the same integer degree as $\bar f$.
::: {.proof}
Let $q:S^{2k+1}\to\mathbb{RP}^{2k+1}$ be the antipodal quotient. It is an oriented two-sheeted covering, hence $\deg q=2$. Equivariance gives
$$
q\circ f=\bar f\circ q.
$$
Taking degrees,
$$
2\deg f=\deg(q\circ f)=\deg(\bar f\circ q)=2\deg\bar f,
$$
so $\deg f=\deg\bar f$.
:::

<1>7. Consequently
$$
\boxed{\deg f\text{ is odd}.}
$$
::: {.proof}
Combine <1>5 and <1>6.
:::
:::
