---
schema: qual/card@1
id: P-RAF22F
kind: problem
title: "Adding an L^1 density to a Radon measure stays Radon"
classification:
  areas:
  - real-analysis
  topics:
  - Radon Measures
  - L1 Functions
  - Locally Compact Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the official UCSD Fall 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Suppose that $\mu$ is a Radon measure on $X$ (a locally compact Hausdorff space).
Assume $\varphi \in L^1(\mu)$ and $\varphi \geq 0$.
Prove that $\nu(E) = \int_E \varphi \, d\mu$ is a Radon measure.
:::

::: solution
<1>1. The measure $\nu$ is finite, hence locally finite.
::: proof
Since $\varphi\ge0$ and $\varphi\in L^1(\mu)$,
\[
\nu(X)=\int_X\varphi\,d\mu<\infty.
\]
Thus $\nu$ is a finite positive Borel measure, in particular finite on every compact set.
:::

<1>2. Prove inner regularity.
::: proof
Fix a Borel set $E\subset X$ and $\varepsilon>0$. Since
\[
\{\varphi>0\}=\bigcup_{m,n\ge1}
\left\{\frac1m\le\varphi\le n\right\},
\]
monotone convergence allows us to choose $m,n$ so that, with
\[
A:=E\cap\left\{\frac1m\le\varphi\le n\right\},
\]
we have
\[
\nu(E\setminus A)<\frac\varepsilon2.
\]

Moreover,
\[
\frac1m\mu(A)
\le\int_A\varphi\,d\mu
\le\nu(X)<\infty,
\]
so $\mu(A)<\infty$.

Because $\mu$ is Radon, there exists a compact set $K\subset A$ such that
\[
\mu(A\setminus K)<\frac{\varepsilon}{2n}.
\]
On $A$ we have $\varphi\le n$, hence
\[
\nu(A\setminus K)
=\int_{A\setminus K}\varphi\,d\mu
\le n\mu(A\setminus K)
<\frac\varepsilon2.
\]
Therefore
\[
\nu(E\setminus K)
\le \nu(E\setminus A)+\nu(A\setminus K)
<\varepsilon.
\]
Thus
\[
\nu(E)=\sup\{\nu(K):K\subset E,\ K\text{ compact}\},
\]
so $\nu$ is inner regular.
:::

<1>3. Deduce outer regularity.
::: proof
Let $E$ be Borel and let $\varepsilon>0$. By Step 2 applied to $X\setminus E$, choose compact
\[
K\subset X\setminus E
\]
such that
\[
\nu((X\setminus E)\setminus K)<\varepsilon.
\]
Set
\[
U:=X\setminus K.
\]
Then $U$ is open and contains $E$, while
\[
\nu(U\setminus E)
=\nu((X\setminus E)\setminus K)
<\varepsilon.
\]
Hence
\[
\nu(E)=\inf\{\nu(U):E\subset U,\ U\text{ open}\}.
\]

Thus $\nu$ is locally finite, inner regular, and outer regular; therefore it is a Radon measure.
:::
:::
