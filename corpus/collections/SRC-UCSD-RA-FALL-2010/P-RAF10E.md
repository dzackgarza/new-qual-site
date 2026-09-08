---
schema: qual/card@1
id: P-RAF10E
kind: problem
title: "Surjectivity of self-adjoint operators with lower bound"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Fall 2010 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Recall that a bounded linear operator $T : \mathcal{H} \to \mathcal{H}$ on a Hilbert space $\mathcal{H}$ is self-adjoint if $\langle Tv, w \rangle = \langle v, Tw \rangle$ for all vectors $v, w \in \mathcal{H}$.

(a) Suppose that $T$ is a bounded self-adjoint operator such that $\|v\| \leq \|Tv\|$ for all $v \in \mathcal{H}$.
Show that given any $y \in \mathcal{H}$, there exists $x \in \mathcal{H}$ such that $Tx = y$.

Hint: Prove first that the range of $T$ is a closed subspace of $\mathcal{H}$.

(b) Give an example of an injective bounded self-adjoint linear operator $T$ in a Hilbert space $\mathcal{H}$ for which the equation $Tx = y$ does not always have a solution.

(c) Can an example for (b) exist on a finite dimensional Hilbert space $\mathcal{H}$?
:::

::: solution
<1>1. Prove that the range of $T$ is closed.
::: proof
Suppose
\[
Tx_n\to y
\]
in $\mathcal H$. The lower bound
\[
\|v\|\le\|Tv\|
\]
gives
\[
\|x_n-x_m\|
\le \|T(x_n-x_m)\|
=\|Tx_n-Tx_m\|.
\]
Thus $(x_n)$ is Cauchy. Since $\mathcal H$ is complete, $x_n\to x$ for some $x\in\mathcal H$. Boundedness of $T$ then gives
\[
Tx_n\to Tx.
\]
Hence $y=Tx$, so $\operatorname{Ran}T$ is closed.
:::

<1>2. Show that the range is dense and conclude surjectivity.
::: proof
The lower bound implies
\[
Tv=0\quad\Longrightarrow\quad v=0,
\]
so
\[
\ker T=\{0\}.
\]
For any bounded operator on a Hilbert space,
\[
(\operatorname{Ran}T)^\perp=\ker T^*.
\]
Since $T$ is self-adjoint,
\[
\ker T^*=\ker T=\{0\}.
\]
Therefore
\[
(\operatorname{Ran}T)^\perp=\{0\},
\]
so $\operatorname{Ran}T$ is dense. By Step 1 it is also closed. Hence
\[
\operatorname{Ran}T=\mathcal H.
\]
Thus for every $y\in\mathcal H$ there exists $x\in\mathcal H$ with
\[
Tx=y.
\]
:::

<1>3. Give an injective self-adjoint operator that is not onto.
::: proof
Take
\[
\mathcal H=L^2([0,1])
\]
and define
\[
(Tf)(x)=x f(x).
\]
Then $T$ is bounded because
\[
\|Tf\|_2\le\|f\|_2,
\]
and it is self-adjoint because multiplication by the real-valued function $x$ is self-adjoint.

It is injective: if $xf(x)=0$ almost everywhere, then $f(x)=0$ for almost every $x>0$, hence $f=0$ in $L^2$.

However $T$ is not onto. If the constant function $1$ belonged to $\operatorname{Ran}T$, then we would have
\[
xf(x)=1
\]
almost everywhere, so
\[
f(x)=\frac1x
\]
almost everywhere on $(0,1]$. But
\[
\int_0^1\frac{dx}{x^2}=\infty,
\]
so $1/x\notin L^2([0,1])$. Thus $1\notin\operatorname{Ran}T$.
:::

<1>4. Explain why no finite-dimensional example exists.
::: proof
On a finite-dimensional vector space, every injective linear map from the space to itself is automatically surjective. Therefore an injective bounded self-adjoint operator on a finite-dimensional Hilbert space cannot fail to be onto.

Hence the answer to part (c) is
\[
\boxed{\text{No}.}
\]
:::
:::
