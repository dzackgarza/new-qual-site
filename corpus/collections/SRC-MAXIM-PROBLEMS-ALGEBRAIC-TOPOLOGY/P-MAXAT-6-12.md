---
schema: qual/card@1
id: P-MAXAT-6-12
kind: problem
title: Maxim algebraic topology 6.12
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 12 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that if M is an oriented boundary, then all its Pontrjagin numbers are zero.
:::

Let $M^{4m}$ be a closed oriented manifold and suppose
\[
M=\partial W
\]
as oriented manifolds, where $W^{4m+1}$ is compact and oriented.

::: pf

::: pf-step

Along the boundary there is a stable tangent-bundle isomorphism
\[
TW|_M\cong TM\oplus\varepsilon^1.
\]


::: pf-proof

Choose an outward-pointing normal vector field along $\partial W$. It spans a trivial normal line bundle $\varepsilon^1$, and the tangent bundle of $W$ restricted to the boundary splits into the tangent bundle of the boundary plus this normal line.

:::

:::

::: pf-step

Hence, for the inclusion
\[
i:M\hookrightarrow W,
\]
one has
\[
p_j(TM)=i^*p_j(TW)
\qquad(j\geq1).
\]


::: pf-proof

Pontryagin classes are natural and stable. By step <1>1,
\[
p(TM)=p(TM\oplus\varepsilon^1)
=p(TW|_M)
=i^*p(TW).
\]
Comparing homogeneous components gives the formula.

:::

:::

::: pf-step

Let
\[
P=p_{i_1}\cdots p_{i_r}
\]
with
\[
i_1+\cdots+i_r=m.
\]
Then the corresponding Pontryagin number is
\[
\langle P(TM),[M]\rangle
=\langle i^*P(TW),[M]\rangle.
\]


::: pf-proof

The degree of $P$ is
\[
4(i_1+\cdots+i_r)=4m=\dim M,
\]
so it can be evaluated on the fundamental class. Multiplicativity of pullback and step <1>2 give
\[
P(TM)=i^*P(TW).
\]

:::

:::

::: pf-step

The boundary fundamental class satisfies
\[
[M]=\partial[W,M]
\]
in the long exact sequence of the pair $(W,M)$.


::: pf-proof

The relative fundamental class
\[
[W,M]\in H_{4m+1}(W,M;\mathbb Z)
\]
is characterized by the orientation of $W$. Under the connecting homomorphism
\[
\partial:H_{4m+1}(W,M)\to H_{4m}(M),
\]
it maps to the fundamental class of the oriented boundary, with the boundary orientation convention.

:::

:::

::: pf-step

If $u\in H^{4m}(W;\mathbb Z)$ is any absolute cohomology class, then
\[
\langle i^*u,[M]\rangle=0.
\]


::: pf-proof

Use step <1>4 and compatibility of the Kronecker pairing with the boundary and coboundary maps:
\[
\langle i^*u,\partial[W,M]\rangle
=\langle\delta(i^*u),[W,M]\rangle.
\]
In the cohomology long exact sequence of the pair, exactness gives
\[
\delta\circ i^*=0.
\]
Hence the right-hand side is zero.

:::

:::

::: pf-step

Applying step <1>5 to
\[
u=P(TW)
\]
gives
\[
\langle P(TM),[M]\rangle=0.
\]


::: pf-proof

Step <1>3 writes the Pontryagin number as
\[
\langle i^*P(TW),[M]\rangle,
\]
which vanishes by step <1>5.

:::

:::

::: pf-step

Therefore every Pontryagin number of $M$ is zero:
\[
\boxed{
\langle p_{i_1}(TM)\cdots p_{i_r}(TM),[M]\rangle=0
\quad\text{whenever }i_1+\cdots+i_r=m.}
\]


::: pf-proof

The monomial $P$ in step <1>3 was arbitrary among all Pontryagin monomials of total degree $4m$, and step <1>6 proves its characteristic number vanishes.

:::

:::

::: pf-qed

Step <1>7 is the required assertion.

:::

:::
