---
schema: qual/card@1
id: P-TOPS05G
kind: problem
title: 'An antipodal-preserving map of $S^{2k+1}$ has odd degree'
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

::: {.problem}
Let $f : S^{2k+1} \to S^{2k+1}$ satisfy $f(-x) = -f(x)$.
Prove the degree of $f$ is odd.
:::

::: {.solution}

::: pf

::: pf-step

The equivariant map descends to
$$
\bar f:\RP^{2k+1}\to\RP^{2k+1}.
$$

::: pf-proof

The identity $f(-x)=-f(x)$ sends antipodal orbits to antipodal orbits.

:::

:::

::: pf-step

The induced map on $\pi_1\cong\ZZ/2$ is the identity.

::: pf-proof

A generator lifts to a path from $x$ to $-x$; its image under $f$ is a path from $f(x)$ to $-f(x)$ and therefore projects to the nontrivial loop.

:::

:::

::: pf-step

Hence if $u\in H^1(\RP^{2k+1};\FF_2)$ is the generator, then
$$
\bar f^*u=u.
$$

::: pf-proof

The unique nonzero class in $H^1(-;\FF_2)$ corresponds to the nontrivial homomorphism $\pi_1\to\FF_2$.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\bar f^*(u^{2k+1})=u^{2k+1}\ne0.
$$

::: pf-proof

Pullback is multiplicative and
$$
H^*(\RP^{2k+1};\FF_2)=\FF_2[u]/(u^{2k+2}).
$$

:::

:::

::: {.pf-step #s5}

The integer degree of $\bar f$ is odd.

::: pf-proof

Because $2k+1$ is odd, $\RP^{2k+1}$ is orientable. By step [](#s4){.pf-ref}, $\bar f^*$ is nonzero on top cohomology with $\FF_2$ coefficients, so the mod-$2$ reduction of $\deg(\bar f)$ is $1$. Hence $\deg(\bar f)$ is odd.

:::

:::

::: {.pf-step #s6}

The sphere map $f$ has the same integer degree as $\bar f$.

::: pf-proof

Let $q:S^{2k+1}\to\RP^{2k+1}$ be the antipodal quotient. It is an oriented two-sheeted covering, hence $\deg q=2$. Equivariance gives
$$
q\circ f=\bar f\circ q.
$$
Taking degrees,
$$
2\deg f=\deg(q\circ f)=\deg(\bar f\circ q)=2\deg\bar f,
$$
so $\deg f=\deg\bar f$.

:::

:::

::: pf-step

Consequently
$$
\boxed{\deg f\text{ is odd}.}
$$

::: pf-proof

Combine steps [](#s5){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

:::

:::
