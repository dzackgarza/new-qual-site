---
schema: qual/card@1
id: E-HAT-3.3-32
kind: problem
title: Compact manifolds do not retract onto boundary
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 32; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 32; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument over $\ZZ_2$, where every manifold is orientable: a retraction makes $i_*$
    injective on $H_{n-1}$, while exactness together with $\delta[M,\partial M]=[\partial M]\ne0$
    makes $i_*[\partial M]=0$.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Added the published corroboration: Steven V. Sam, Solutions to Algebraic Topology (2008),
    SS3.3 Exercise 32, printed p.16, is the same argument, and this card matches it step for step
    except that Sam's own text slips in writing the retraction identity on M instead of on the
    boundary. Read against Hatcher: the ZZ_2 coefficient ring makes orientability automatic and
    Exercise 31 supplies the nonzero boundary class.
---

::: {.problem}
Show that a compact manifold does not retract onto its boundary.
:::

::: {.solution}
It is enough to use $R=\ZZ_2$, over which every manifold is orientable. Suppose there were a retraction
$$
r:M\to\partial M
$$
with inclusion $i:\partial M\hookrightarrow M$. Then
$$
r\circ i=\operatorname{id}_{\partial M},
$$
so on homology
$$
r_*i_*=\operatorname{id}.
$$
Thus
$$
i_*:H_{n-1}(\partial M;\ZZ_2)\to H_{n-1}(M;\ZZ_2)
$$
would be injective.

On the other hand, Exercise 31 says that the boundary homomorphism in the long exact sequence of the pair sends the relative fundamental class to the nonzero boundary fundamental class:
$$
\delta[M,\partial M]=[\partial M]\ne0.
$$
Exactness of
$$
H_n(M,\partial M)\xrightarrow{\delta}H_{n-1}(\partial M)
\xrightarrow{i_*}H_{n-1}(M)
$$
therefore gives
$$
i_*[\partial M]=0.
$$
This contradicts injectivity of $i_*$. Hence a compact manifold cannot retract onto its boundary.

The argument is the one in Steven V. Sam, *Solutions to Algebraic Topology* (2008), §3.3 Exercise 32, printed p.16: coefficients $\ZZ_2$ so that orientability is free, Exercise 31 to make the boundary map nonzero on the fundamental class, and exactness to make $i_*$ kill it. Sam's text prints "$r\circ i$ is the identity on $M$" where the composite is the identity on $\partial M$; the slip is not reproduced here.
:::
