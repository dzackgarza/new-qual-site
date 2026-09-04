---
schema: qual/card@1
id: P-HZBSC
kind: problem
title: Fundamental group of two solid tori glued along the boundary by $\phi_n$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Corrected the swapped meridian/longitude action of phi_n; the group is Z/nZ, not Z for all n.
---

::: problem
Let 
$$
V = \DD^2 \times S^1 = \theset{ (z, e^{it}) \suchthat \norm z \leq 1,~~ 0 \leq t < 2\pi}
$$ 
be the "solid torus" with boundary given by the torus $T = S^1 \times S^1$ . 

For $n \in \ZZ$ define 
\begin{align*}
\phi_n : T &\to T \\
(e^{is} , e^{it} ) &\mapsto (e^{is} , e^{i(ns+t)})
.\end{align*}

Find the fundamental group of the identification space
$$
X_n = {V\disjoint V \over \sim_n}.
$$
where the equivalence relation $\sim_n$ identifies a point $x$ on the boundary $T$ of the first copy of $V$ with the point $\phi_n (x)$ on the boundary of the second copy of $V$.
:::

::: {.solution}
<1>1. Let
\[
\mu(s)=(e^{is},1),
\qquad
\lambda(t)=(1,e^{it})
\]
be the meridian and longitude of the boundary torus
\[
T=\partial(D^2\times S^1).
\]
Then
\[
\pi_1(T)\cong \mathbb Z\mu\oplus\mathbb Z\lambda.
\]
For either copy of the solid torus, the boundary inclusion kills \(\mu\) and sends \(\lambda\) to a generator of the fundamental group of the solid torus.
::: {.proof}
The solid torus \(V=D^2\times S^1\) deformation retracts onto its core \(\{0\}\times S^1\), so
\[
\pi_1(V)\cong\mathbb Z.
\]
The loop \(\mu\) bounds the disk \(D^2\times\{1\}\), while \(\lambda\) is homotopic to the core circle.
:::

<1>2. The gluing map acts on \(\pi_1(T)\) by
\[
\phi_{n*}(\mu)=\mu+n\lambda,
\qquad
\phi_{n*}(\lambda)=\lambda.
\]
::: {.proof}
Along the meridian,
\[
\phi_n(e^{is},1)=(e^{is},e^{ins}),
\]
so the image winds once in the meridian direction and \(n\) times in the longitude direction.
Along the longitude,
\[
\phi_n(1,e^{it})=(1,e^{it}),
\]
so \(\lambda\) is fixed.
:::

<1>3. Let \(a\) and \(b\) denote the core generators of the first and second copies of \(V\), respectively. Van Kampen gives
\[
\pi_1(X_n)
\cong
\left\langle a,b\ \middle|\
 i_{1*}(\mu)=i_{2*}\phi_{n*}(\mu),\
 i_{1*}(\lambda)=i_{2*}\phi_{n*}(\lambda)
\right\rangle.
\]
::: {.proof}
Use collar neighborhoods of the common boundary torus after gluing. They give an open cover whose two pieces deformation retract onto the two solid tori and whose intersection deformation retracts onto \(T\). The displayed presentation is the resulting pushout presentation from Seifert--van Kampen.
:::

<1>4. The meridian relation is
\[
1=b^n,
\]
and the longitude relation is
\[
a=b.
\]
::: {.proof}
By <1>1,
\[
i_{1*}(\mu)=1,
\qquad
 i_{1*}(\lambda)=a,
\]
and for the second solid torus
\[
i_{2*}(\mu)=1,
\qquad
 i_{2*}(\lambda)=b.
\]
Using <1>2,
\[
i_{2*}\phi_{n*}(\mu)
=i_{2*}(\mu+n\lambda)=b^n,
\]
while
\[
i_{2*}\phi_{n*}(\lambda)=b.
\]
Substitute these into <1>3.
:::

<1>5. Therefore
\[
\boxed{\pi_1(X_n)\cong \mathbb Z/n\mathbb Z}.
\]
Equivalently,
\[
\pi_1(X_n)\cong
\begin{cases}
\mathbb Z,&n=0,\\
\mathbb Z/|n|\mathbb Z,&n\ne0.
\end{cases}
\]
::: {.proof}
By <1>4,
\[
\pi_1(X_n)
\cong
\langle a,b\mid b^n=1,\ a=b\rangle
\cong
\langle a\mid a^n=1\rangle.
\]
For \(n=0\), the relation \(a^0=1\) is vacuous, giving \(\mathbb Z\). For \(n\ne0\), the relation has order \(|n|\), giving \(\mathbb Z/|n|\mathbb Z\).
:::
:::
