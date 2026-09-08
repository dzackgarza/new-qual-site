---
schema: qual/card@1
id: P-RAF04G
kind: problem
title: "Polynomials in a continuous injective function are dense in L^1([-1,1])"
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - L1 Spaces
  - Stone-Weierstrass
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 7 of the official UCSD Fall 2004 real-analysis qualifying exam, including the source's note about the possible zero of h.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $h \in C([-1, 1], \mathbb{R})$ be a one-to-one function and let $Z$ denote the space of functions of the form $p(h) := \sum_{k=1}^n a_k h^k$ for some $n \in \mathbb{N}$ and $a_k \in \mathbb{R}$.
Show $Z$ is a dense subspace of $L^1([-1, 1], \mathcal{B}_{[-1,1]}, m)$.
:::

::: solution
<1>1. Transfer the problem to the compact range of $h$.
::: proof
Because $h$ is continuous and injective on the compact interval $[-1,1]$, it is a homeomorphism from $[-1,1]$ onto the compact interval
\[
K:=h([-1,1]).
\]
Let $\nu=h_*m$ be the pushforward of Lebesgue measure. Then for every measurable $\Phi:K\to\mathbb C$,
\[
\int_{-1}^1 |\Phi(h(x))|\,dx
=\int_K|\Phi(t)|\,d\nu(t).
\]
Thus it is enough to show that the polynomials
\[
p(t)=\sum_{k=1}^n a_kt^k,
\]
with zero constant term, are dense in $L^1(K,\nu)$.

If $0\in K$, then $h^{-1}(\{0\})$ is a singleton because $h$ is injective. Hence
\[
\nu(\{0\})=m(h^{-1}(\{0\}))=0.
\]
If $0\notin K$, the same conclusion is vacuous.
:::

<1>2. Approximate continuous functions by zero-constant polynomials in $L^1(K,\nu)$.
::: proof
Fix $\varphi\in C(K)$ and $\varepsilon>0$. Since $\nu(\{0\})=0$, choose an open neighborhood $U$ of $0$ in $K$ so small that
\[
\int_U |\varphi|\,d\nu<\frac\varepsilon2.
\]
Choose a continuous cutoff $\chi:K\to[0,1]$ such that $\chi=0$ on a neighborhood of $0$ and $\chi=1$ on $K\setminus U$. Then
\[
\|\varphi-\chi\varphi\|_{L^1(\nu)}<\frac\varepsilon2.
\]

Define
\[
\psi(t)=
\begin{cases}
\chi(t)\varphi(t)/t,&t\ne0,\\
0,&t=0.
\end{cases}
\]
Because $\chi$ vanishes on a neighborhood of $0$, $\psi\in C(K)$. By the Weierstrass approximation theorem, there is a polynomial $q$ such that
\[
\|q-\psi\|_{\infty}<
\frac{\varepsilon}{2\nu(K)\max(1,\sup_{t\in K}|t|)}.
\]
Then $p(t):=tq(t)$ has zero constant term and
\[
\begin{aligned}
\|p-\chi\varphi\|_{L^1(\nu)}
&=\int_K |t|\,|q(t)-\psi(t)|\,d\nu(t)\\
&<\frac\varepsilon2.
\end{aligned}
\]
Therefore
\[
\|p-\varphi\|_{L^1(\nu)}<\varepsilon.
\]
So zero-constant polynomials are dense in $C(K)$ with respect to the $L^1(\nu)$ norm.
:::

<1>3. Pass from continuous functions to all of $L^1$.
::: proof
Continuous functions are dense in $L^1(K,\nu)$ because $\nu$ is a finite Borel measure on the compact metric space $K$. Step 2 therefore shows that zero-constant polynomials are dense in $L^1(K,\nu)$. Pulling them back by $h$ gives precisely the functions in $Z$. Hence
\[
\boxed{\overline Z^{\,L^1([-1,1])}=L^1([-1,1]).}
\]
:::
:::
