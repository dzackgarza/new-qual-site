---
schema: qual/card@1
id: P-RAF20E
kind: problem
title: "A measure dominated by the L^2 norm has Holder-continuous density"
classification:
  areas:
  - real-analysis
  topics:
  - Radon-Nikodym
  - Holder Continuity
  - Borel Measures
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Fall 2020 real-analysis qualifying exam. The card had dropped the derivative from the source hypothesis; the source assumes |∫ f' dμ| ≤ ||f||_2 for every f∈C^1([0,1]).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $\mu$ be a (positive) Borel measure on $[0, 1]$ and denote by $m$ the Lebesgue measure.
Assume
$$
\left|\int_{[0,1]} f' \, d\mu\right| \leq \left(\int_{[0,1]} |f|^2 \, dm\right)^{1/2} \quad \forall f \in C^1([0, 1]).
$$

Prove the following:

(1) $\mu \ll m$;

(2) If $u = d\mu/dm \in L^1(m)$ is the Radon–Nikodym derivative of $\mu$ with respect to $m$, then
$$
|u(x) - u(y)| \leq |x - y|^{1/2} \quad \text{for a.e. } x, y \in [0, 1].
$$
:::

::: solution
<1>1. Represent the derivative functional on $L^2$.
::: proof
Define
\[
L(f):=\int_{[0,1]}f'\,d\mu,
\qquad f\in C^1([0,1]).
\]
The hypothesis gives
\[
|L(f)|\le\|f\|_2.
\]
Since $C^1([0,1])$ is dense in $L^2([0,1])$, $L$ extends uniquely to a bounded linear functional on $L^2$ with norm at most $1$. By the Riesz representation theorem, there exists $v\in L^2([0,1])$ with
\[
\|v\|_2\le1
\]
such that
\[
\int_{[0,1]}f'\,d\mu=\int_0^1 f(x)v(x)\,dx
\]
for every $f\in C^1([0,1])$.
:::

<1>2. Identify the measure on the open interval.
::: proof
Restrict the preceding identity to $f\in C_c^1((0,1))$. In the sense of distributions on $(0,1)$,
\[
D\mu=-v.
\]
Let
\[
V(x):=\int_0^x v(t)\,dt.
\]
Then $V\in H^1(0,1)$ and $DV=v$. Hence
\[
D(\mu+V\,m)=0
\]
as a distribution on the connected interval $(0,1)$. A distribution with zero derivative on an interval is constant, so there exists $c\in\mathbb R$ such that
\[
\mu|_{(0,1)}=(c-V)m.
\]
Thus $\mu$ is absolutely continuous with respect to Lebesgue measure on the open interval, with density
\[
u(x)=c-V(x)
\]
there.
:::

<1>3. Rule out endpoint atoms.
::: proof
Choose $\psi\in C_c^1([0,1))$ with $0\le\psi\le1$ and $\psi(0)=1$. For $\varepsilon>0$, define
\[
f_\varepsilon(x):=\int_0^x \psi(t/\varepsilon)\,dt.
\]
Then $f_\varepsilon'\to\mathbf1_{\{0\}}$ pointwise on $[0,1]$, with $|f_\varepsilon'|\le1$, while
\[
\|f_\varepsilon\|_2=O(\varepsilon).
\]
By dominated convergence with respect to the finite measure $\mu$,
\[
\int f_\varepsilon'\,d\mu\longrightarrow\mu(\{0\}).
\]
But the assumed estimate gives
\[
\left|\int f_\varepsilon'\,d\mu\right|
\le\|f_\varepsilon\|_2\longrightarrow0.
\]
Therefore $\mu(\{0\})=0$. Applying the same construction at $1$ gives $\mu(\{1\})=0$.

Consequently
\[
\boxed{\mu\ll m\text{ on }[0,1].}
\]
:::

<1>4. Prove the Hölder estimate for the Radon--Nikodym density.
::: proof
The density $u=c-V$ has an absolutely continuous representative satisfying
\[
u'(x)=-v(x)
\]
for almost every $x$. Hence for $x,y\in[0,1]$,
\[
u(x)-u(y)=-\int_y^x v(t)\,dt.
\]
Cauchy--Schwarz gives
\[
|u(x)-u(y)|
\le \|v\|_2\,|x-y|^{1/2}
\le |x-y|^{1/2}.
\]
Thus this representative satisfies the estimate for every $x,y$, and therefore the Radon--Nikodym derivative satisfies
\[
\boxed{|u(x)-u(y)|\le |x-y|^{1/2}}
\]
for almost every pair $(x,y)\in[0,1]^2$.
:::
:::
