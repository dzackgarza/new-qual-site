---
schema: qual/card@1
id: P-RAF25C
kind: problem
title: "Pointwise and weak-star dual characterizations of the constraint u >= f"
classification:
  areas:
  - real-analysis
  topics:
  - L-infinity Spaces
  - Weak* Topology
  - Duality
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Fall 2025 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $\Omega \subset \mathbb{R}^n$ be a Lebesgue measurable set, $f : \Omega \to \mathbb{R}$ measurable and define
$$
X := \{u \in L^\infty(\Omega) : u \geq f \text{ a.e. in } \Omega\}, \quad Y := \left\{u \in L^\infty(\Omega) : \int_\Omega u\varphi \, dx \geq \int_\Omega f\varphi \, dx \; \forall \varphi \in W\right\},
$$
where $W := \{\varphi \in L^1(\Omega) : \varphi f \in L^1(\Omega), \varphi \geq 0 \text{ a.e. in } \Omega\}$.

(1) Prove that if $f \in L^\infty(\Omega)$, then $X = Y$.

(2) Prove that (1) holds when $f$ is just measurable.

(3) Prove that $X$ is sequentially closed in the weak*-topology in $L^\infty(\Omega)$.
:::

::: solution
<1>1. Prove $X\subseteq Y$ for arbitrary measurable $f$.
::: proof
Let $u\in X$ and let $\varphi\in W$. Then
\[
u-f\ge0
\qquad\text{a.e.},
\qquad
\varphi\ge0
\qquad\text{a.e.}
\]
Moreover $u\varphi\in L^1$ because $u\in L^\infty$ and $\varphi\in L^1$, while $f\varphi\in L^1$ by the definition of $W$. Therefore
\[
\int_\Omega u\varphi-\int_\Omega f\varphi
=\int_\Omega (u-f)\varphi\ge0.
\]
Hence $u\in Y$, so
\[
X\subseteq Y.
\]
:::

<1>2. If $f\in L^\infty$, prove $Y\subseteq X$.
::: proof
Assume $f\in L^\infty$ and let $u\in Y$. Suppose $u\notin X$. Then
\[
A:=\{x:u(x)<f(x)\}
\]
has positive measure. Since
\[
A=\bigcup_{m=1}^\infty\{f-u\ge1/m\},
\]
there exists $m$ such that
\[
m(\{f-u\ge1/m\})>0.
\]
Because Lebesgue measure is $\sigma$-finite, for some radius $R$ the set
\[
E:=\{f-u\ge1/m\}\cap B_R
\]
has finite positive measure. Put
\[
\varphi:=\mathbf1_E.
\]
Since $f\in L^\infty$, we have $\varphi\in W$. But
\[
\int u\varphi
\le \int f\varphi-\frac1m m(E)
<\int f\varphi,
\]
contradicting $u\in Y$. Thus $u\in X$, and therefore
\[
X=Y
\]
when $f\in L^\infty$.
:::

<1>3. Prove $Y\subseteq X$ for arbitrary measurable $f$.
::: proof
Let $u\in Y$ and suppose again that
\[
A:=\{u<f\}
\]
has positive measure. Since $f$ is finite-valued and measurable,
\[
A
=\bigcup_{m,k,R\ge1}
\left(
\{f-u\ge1/m\}\cap\{|f|\le k\}\cap B_R
\right).
\]
Hence for some $m,k,R$ the set
\[
E:=\{f-u\ge1/m\}\cap\{|f|\le k\}\cap B_R
\]
has finite positive measure.

Set $\varphi=\mathbf1_E$. Then $\varphi\in L^1$, $\varphi\ge0$, and
\[
|f\varphi|\le k\mathbf1_E\in L^1,
\]
so $\varphi\in W$. But again
\[
\int u\varphi
\le \int f\varphi-\frac1m m(E)
<\int f\varphi,
\]
contradicting $u\in Y$. Thus $u\ge f$ almost everywhere, so
\[
\boxed{X=Y}
\]
for arbitrary measurable $f$.
:::

<1>4. Prove weak* sequential closedness.
::: proof
Let $(u_j)\subset X$ and suppose
\[
u_j\overset{*}{\rightharpoonup}u
\qquad\text{in }L^\infty(\Omega).
\]
Fix $\varphi\in W\subset L^1(\Omega)$. Since $u_j\in X=Y$,
\[
\int_\Omega u_j\varphi\,dx
\ge \int_\Omega f\varphi\,dx
\qquad\text{for every }j.
\]
Weak* convergence gives
\[
\int_\Omega u_j\varphi\,dx
\longrightarrow
\int_\Omega u\varphi\,dx.
\]
Passing to the limit yields
\[
\int_\Omega u\varphi\,dx
\ge \int_\Omega f\varphi\,dx.
\]
Since this holds for every $\varphi\in W$, we have $u\in Y=X$. Hence $X$ is sequentially weak* closed.
:::
:::
