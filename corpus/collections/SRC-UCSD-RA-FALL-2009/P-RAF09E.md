---
schema: qual/card@1
id: P-RAF09E
kind: problem
title: "Alternate proof of the Lebesgue-Radon-Nikodym theorem"
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
  note: Checked against Problem 5 of the official UCSD Fall 2009 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
The following provides steps to give an alternate proof of the Lebesgue-Radon-Nikodym theorem.
Suppose that $\mu$ and $\nu$ are positive finite measures on $(X, \mathcal{M})$ and let $\lambda = \mu + \nu$.

(a) The map $f \mapsto \int f\,d\nu$ is a bounded linear functional on $L^2(\lambda)$, so there exists $g \in L^2(\lambda)$ such that for any $f \in L^2(\lambda)$, $\int f(1-g)\,d\nu = \int fg\,d\mu$.

(b) $0 \leq g \leq 1$ $\lambda$-a.e., so we can assume that $0 \leq g \leq 1$ everywhere.

(c) Let $A = \{x : g(x) < 1\}$, $B = \{x : g(x) = 1\}$, and set $\nu_a(E) = \nu(A \cap E)$, $\nu_s(E) = \nu(B \cap E)$.
Then $\nu_a \ll \mu$ and $\nu_s \perp \mu$.

(d) Moreover $d\nu_a = g(1-g)^{-1}\,d\mu$.
:::

::: solution
<1>1. Prove part (a) by the Riesz representation theorem.
::: proof
Since $\nu\le\lambda$ and $\lambda(X)<\infty$, for $f\in L^2(\lambda)$,
\[
\left|\int_X f\,d\nu\right|
\le \nu(X)^{1/2}
\left(\int_X|f|^2\,d\nu\right)^{1/2}
\le \nu(X)^{1/2}\|f\|_{L^2(\lambda)}.
\]
Thus
\[
L(f):=\int_Xf\,d\nu
\]
is a bounded linear functional on the Hilbert space $L^2(\lambda)$. By the Riesz representation theorem, there is $g\in L^2(\lambda)$ such that
\[
\int_X f\,d\nu
=\int_X fg\,d\lambda
=\int_Xfg\,d\mu+\int_Xfg\,d\nu.
\]
Hence for every $f\in L^2(\lambda)$,
\[
\boxed{
\int_X f(1-g)\,d\nu
=\int_X fg\,d\mu.}
\]
:::

<1>2. Prove that $0\le g\le1$ almost everywhere.
::: proof
Because $\lambda$ is finite, indicators of measurable sets lie in $L^2(\lambda)$.

Let
\[
E_-:=\{g<0\}.
\]
Taking $f=\mathbf1_{E_-}$ in the identity from Step 1 gives
\[
\int_{E_-}(1-g)\,d\nu
=\int_{E_-}g\,d\mu.
\]
The left side is nonnegative and the right side is nonpositive. Hence both are zero. Since $1-g>0$ and $-g>0$ on $E_-$, this forces
\[
\nu(E_-)=\mu(E_-)=0.
\]

Similarly, on
\[
E_+:=\{g>1\},
\]
the left side is nonpositive and the right side nonnegative, so again both vanish, giving
\[
\nu(E_+)=\mu(E_+)=0.
\]
Thus
\[
0\le g\le1
\qquad\lambda\text{-a.e.}
\]
Changing $g$ on a $\lambda$-null set, we may assume this holds everywhere.
:::

<1>3. Prove the Lebesgue decomposition in part (c).
::: proof
Let
\[
A=\{g<1\},
\qquad
B=\{g=1\}.
\]
Taking $f=\mathbf1_B$ in Step 1 gives
\[
0=\int_Bg\,d\mu=\mu(B).
\]
Thus $\nu_s(E)=\nu(E\cap B)$ is supported on the $\mu$-null set $B$, so
\[
\nu_s\perp\mu.
\]

To prove $\nu_a\ll\mu$, let $E\in\mathcal M$ satisfy $\mu(E)=0$. Define
\[
A_n:=\left\{g\le1-\frac1n\right\}.
\]
Then $A_n\uparrow A$. Taking
\[
f=\mathbf1_{E\cap A_n}
\]
in Step 1 yields
\[
\int_{E\cap A_n}(1-g)\,d\nu=0.
\]
But $1-g\ge1/n$ on $A_n$, so
\[
\nu(E\cap A_n)=0.
\]
Letting $n\to\infty$ gives
\[
\nu(E\cap A)=0.
\]
Hence
\[
\nu_a\ll\mu.
\]
:::

<1>4. Identify the Radon--Nikodym density on $A$.
::: proof
Fix $E\in\mathcal M$ and again let
\[
A_n=\left\{g\le1-\frac1n\right\}.
\]
The function
\[
f_n:=\frac{\mathbf1_{E\cap A_n}}{1-g}
\]
is measurable and bounded by $n$, hence belongs to $L^2(\lambda)$. Applying Step 1 gives
\[
\nu(E\cap A_n)
=\int_{E\cap A_n}\frac{g}{1-g}\,d\mu.
\]
Since $A_n\uparrow A$, continuity from below on the left and monotone convergence on the right imply
\[
\nu(E\cap A)
=\int_{E\cap A}\frac{g}{1-g}\,d\mu.
\]
Therefore
\[
\boxed{
d\nu_a
=\frac{g}{1-g}\,d\mu,}
\]
where the density is understood on $A$; its value on the $\mu$-null set $B$ is irrelevant.
:::
:::
