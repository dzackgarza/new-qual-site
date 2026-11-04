---
schema: qual/card@1
id: E-SS2.PR-5
kind: problem
title: A universal entire function under translation
classification:
  areas:
  - complex-analysis
  topics:
  - Runge
  - Entire Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 2, §5.5, exercise 5, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise, including parts (a) and (b) and their two hints, and the closing sentence about the
    derivative-universal function $G$. The print writes the first limit as $n\to\infty$ while the
    index is $k$; the card already records that in its remark and it was not changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Parts (a) and (b) are proved in full: the reduction from (17) to universality, and the
    construction of $F=\sum u_n$ with the parameters $c_n$, $M_n$ chosen inductively so that the
    three estimates hold. The closing sentence about $G$ is proved as well: the sets
    $V_n=\{G:\exists N\ge n,\ \sup_{|z|\le n}|D^NG-p_n|<1/n\}$ are open and dense in the complete
    space of entire functions (denseness by writing $G=G_0+\Psi$ with $\Psi$ an $N$-fold
    antiderivative of $p_n-D^NG_0$, whose size on a disc is controlled by Cauchy's estimates), and
    Baire's theorem then supplies $G$; the enumeration is taken with each polynomial occurring
    infinitely often. Nothing is left in outline and nothing is deferred.
---

::: {.exercise}
There exists an entire function $F$ with the following "universal" property: given any entire function $h$, there is an increasing sequence $\{N_k\}_{k=1}^\infty$ of positive integers, so that
$$
\lim_{k \to \infty} F(z + N_k) = h(z)
$$
uniformly on every compact subset of $\CC$.

(a) Let $p_1, p_2, \ldots$ denote an enumeration of the collection of polynomials whose coefficients have rational real and imaginary parts. Show that it suffices to find an entire function $F$ and an increasing sequence $\{M_n\}$ of positive integers, such that
$$
\abs{F(z) - p_n(z - M_n)} < \frac{1}{n} \quad \text{whenever } z \in D_n, \tag{17}
$$
where $D_n$ denotes the disc centered at $M_n$ and of radius $n$.
[Hint: Given $h$ entire, there exists a sequence $\{n_k\}$ such that $\lim_{k \to \infty} p_{n_k}(z) = h(z)$ uniformly on every compact subset of $\CC$.]

(b) Construct $F$ satisfying (17) as an infinite series
$$
F(z) = \sum_{n=1}^\infty u_n(z)
$$
where $u_n(z) = p_n(z - M_n) e^{-c_n (z - M_n)^2}$, and the quantities $c_n > 0$ and $M_n > 0$ are chosen appropriately with $c_n \to 0$ and $M_n \to \infty$.
[Hint: The function $e^{-z^2}$ vanishes rapidly as $\abs{z} \to \infty$ in the sectors $\{\abs{\arg z} < \pi/4 - \delta\}$ and $\{\abs{\pi - \arg z} < \pi/4 - \delta\}$.]

In the same spirit, there exists an alternate "universal" entire function $G$ with the following property: given any entire function $h$, there is an increasing sequence $\{N_k\}_{k=1}^\infty$ of positive integers, so that
$$
\lim_{k \to \infty} D^{N_k} G(z) = h(z)
$$
uniformly on every compact subset of $\CC$. Here $D^j G$ denotes the $j$th (complex) derivative of $G$.
:::

::: {.remark}
The book marks this problem with an asterisk. It writes the first limit as $n \to \infty$; the index of the sequence is $k$.
:::

::: {.solution}

Write $D_n=D(M_n,n)$ for the closed disc of centre $M_n$ and radius $n$.

::: pf

::: {.pf-step #s1}

Part (a): if $F$ is entire, $\{M_n\}$ is a strictly increasing sequence of positive integers, and (17) holds, then $F$ is universal.

::: pf-proof

Let $h$ be entire. The polynomials with rational real and imaginary parts are dense in the space of entire functions for uniform convergence on compact sets: the Taylor polynomials of $h$ converge to $h$ uniformly on every compact set, and each Taylor polynomial can be replaced by one with Gaussian rational coefficients arbitrarily close on that compact set. Hence there are indices $n_1<n_2<\cdots$ with
$$
\sup_{z\in K}\abs{p_{n_k}(z)-h(z)}\longrightarrow0
\qquad\text{for every compact }K .
$$
Put $N_k=M_{n_k}$, which is a strictly increasing sequence of positive integers because $\{M_n\}$ is and $n_k\to\infty$.

Let $K$ be compact and choose $R$ with $K\subseteq D(0,R)$. For $k$ large, $n_k>R$. For $z\in K$ the point $w=z+M_{n_k}$ satisfies
$$
\abs{w-M_{n_k}}=\abs{z}\le R<n_k,
$$
that is, $w\in D_{n_k}$; so (17) gives $\abs{F(z+M_{n_k})-p_{n_k}(z)}<1/n_k$. Therefore
$$
\sup_{z\in K}\abs{F(z+N_k)-h(z)}\le\frac{1}{n_k}+\sup_{z\in K}\abs{p_{n_k}(z)-h(z)}\longrightarrow0 .
$$

:::

:::

::: {.pf-step #s2}

Part (b): the parameters can be chosen. Let $d_n$ be the degree of $p_n$ and $C_n$ a bound for $\abs{p_n}$ on the closed disc of radius $n$; set
$$
c_n=\min\Bigl(1,\ \frac{1}{6n^3\max(C_n,1)}\Bigr)>0,
$$
so that $c_n\to0$ and $2C_nc_nn^2\le\frac1{3n}$ for every $n$. Suppose $M_1<\cdots<M_{n-1}$ and $u_1,\dots,u_{n-1}$ have been chosen. Then $M_n$ can be chosen so large that all of the following hold:
$$
\text{(A)}\quad \sup_{z\in D_n}\sum_{j<n}\abs{u_j(z)}<\frac1{4n},\qquad
\text{(B)}\quad \sup_{z\in D_j}\abs{u_n(z)}<\frac{2^{-n}}{4j}\ \ (j<n),\qquad
\text{(C)}\quad \sup_{\abs{z}\le M_n/4}\abs{u_n(z)}<2^{-n}.
$$

::: pf-proof

Everything rests on the decay of $e^{-c(z-M)^2}$ as $M\to+\infty$ away from the point $M$: for $z$ in a fixed compact set, $z-M\to-\infty$ along the real axis, so
$$
\operatorname{Re}\bigl((z-M)^2\bigr)=(M-\operatorname{Re}z)^2-(\operatorname{Im}z)^2\longrightarrow+\infty
$$
and $\bigl|e^{-c(z-M)^2}\bigr|=e^{-c\operatorname{Re}((z-M)^2)}\to0$ faster than any power of $M$, uniformly in $z$ in that compact set.

(A) Here $z$ ranges over $D_n$, which moves with $M_n$; but for $z\in D_n$ and $j<n$ one has $z-M_j=M_n-M_j+\zeta$ with $\abs{\zeta}\le n$, so
$$
\operatorname{Re}\bigl((z-M_j)^2\bigr)\ge (M_n-M_j-n)^2-2n^2\longrightarrow+\infty
$$
as $M_n\to\infty$, while $\abs{p_j(z-M_j)}$ grows only polynomially in $M_n$. Hence each $\sup_{z\in D_n}\abs{u_j(z)}$, $j<n$, tends to $0$, and a finite sum of them does too.

(B) For fixed $j<n$ the disc $D_j$ is compact, so by the observation above $\sup_{z\in D_j}\abs{u_n(z)}\to0$ as $M_n\to\infty$.

(C) If $\abs{z}\le M_n/4$ then $\abs{\operatorname{Re}z-M_n}\ge 3M_n/4$ and $\abs{\operatorname{Im}z}\le M_n/4$, so
$$
\operatorname{Re}\bigl((z-M_n)^2\bigr)=(\operatorname{Re}z-M_n)^2-(\operatorname{Im}z)^2\ge\frac{9M_n^2}{16}-\frac{M_n^2}{16}=\frac{M_n^2}{2},
$$
and $\abs{p_n(z-M_n)}\le C_n(1+5M_n/4)^{d_n}$. Thus the supremum in (C) is at most $C_n(1+5M_n/4)^{d_n}e^{-c_nM_n^2/2}$, which tends to $0$.

Each of (A), (B), (C) is therefore an inequality that holds for all sufficiently large $M_n$, and there are finitely many of them.

:::

:::

::: {.pf-step #s3}

With $u_n(z)=p_n(z-M_n)e^{-c_n(z-M_n)^2}$ and $M_n$ as in step [](#s2){.pf-ref}, the series $F=\sum_{n\ge1}u_n$ converges uniformly on every compact set, and its sum $F$ is entire.

::: pf-proof

Let $R>0$. If $M_n>4R$ then $D(0,R)\subseteq D(0,M_n/4)$, so by (C)
$$
\sup_{\abs{z}\le R}\abs{u_n(z)}\le 2^{-n}.
$$
Only finitely many $n$ have $M_n\le 4R$, because $M_n\to\infty$; on the disc $D(0,R)$ each of those finitely many $u_n$ is bounded. Hence $\sum_n\sup_{\abs{z}\le R}\abs{u_n(z)}<\infty$ and the series converges uniformly on $D(0,R)$ by the Weierstrass test. A locally uniform limit of entire functions is entire.

:::

:::

::: {.pf-step #s4}

This $F$ satisfies (17): $\abs{F(z)-p_n(z-M_n)}<1/n$ for $z\in D_n$.

::: pf-proof

Let $z\in D_n$. Then $\abs{z-M_n}\le n$, so $\abs{p_n(z-M_n)}\le C_n$ and
$$
\abs{u_n(z)-p_n(z-M_n)}\le C_n\bigl|e^{-c_n(z-M_n)^2}-1\bigr|\le C_n\bigl(e^{c_n n^2}-1\bigr)\le 2C_nc_nn^2\le\frac{1}{3n},
$$
where the last inequality is the choice of $c_n$ in step [](#s2){.pf-ref} and $e^t-1\le 2t$ for $0\le t\le1$. Splitting the series,
$$
\abs{F(z)-p_n(z-M_n)}\le\abs{u_n(z)-p_n(z-M_n)}+\sum_{j<n}\abs{u_j(z)}+\sum_{j>n}\abs{u_j(z)} .
$$
The first term is at most $1/(3n)$; the second is less than $1/(4n)$ by (A); and the third is less than
$$
\sum_{j>n}\frac{2^{-j}}{4n}<\frac{1}{4n}
$$
by (B), applied to this fixed $n$ and every $j>n$. The sum of the three bounds is $1/(3n)+1/(4n)+1/(4n)=5/(6n)<1/n$.

:::

:::

::: {.pf-step #s5}

Let $\mathcal E$ be the space of entire functions with the metric of uniform convergence on compact sets, and for $n\ge1$ put
$$
V_n=\Bigl\{G\in\mathcal E:\ \exists N\ge n\ \text{with}\ \sup_{\abs{z}\le n}\abs{D^NG(z)-p_n(z)}<\tfrac1n\Bigr\}.
$$
Each $V_n$ is open and dense in $\mathcal E$.

::: pf-proof

For fixed $N$ the condition $\sup_{\abs{z}\le n}\abs{D^NG-p_n}<1/n$ is the preimage under the continuous linear map $G\mapsto D^NG$ of an open ball of $\mathcal E$, hence open; and $V_n$ is the union of these sets over $N\ge n$.

For density, let $U=\{G\in\mathcal E:\sup_{\abs{z}\le R}\abs{G(z)-G_0(z)}<\delta\}$ be a basic neighbourhood. Fix $N\ge n$, put $\varphi=p_n-D^NG_0$, which is entire, and let $\Psi$ be the $N$-fold antiderivative of $\varphi$ vanishing to order $N$ at the origin:
$$
\Psi(z)=\frac{1}{(N-1)!}\int_0^z(z-w)^{N-1}\varphi(w)\,dw .
$$
Then $D^N\Psi=\varphi$, so for $G=G_0+\Psi$ one has $D^NG=D^NG_0+\varphi=p_n$ identically, and in particular $G\in V_n$.

It remains to see that $G\in U$ for $N$ large. Choose $\rho>2R$ and put $M_\rho=\sup_{\abs{z}\le\rho}\abs{G_0(z)}$, which is finite. For $\abs{z}\le R$,
$$
\abs{\Psi(z)}\le\frac{R^N}{N!}\sup_{\abs{w}\le R}\abs{\varphi(w)}
\le\frac{R^N}{N!}\sup_{\abs{w}\le R}\abs{p_n(w)}+\frac{R^N}{N!}\cdot\frac{N!\,M_\rho}{(\rho-R)^N},
$$
where Cauchy's estimate for the $N$-th derivative on the smaller disc was used for the second term. The first term tends to $0$ because $R^N/N!\to0$, and the second is $M_\rho\bigl(R/(\rho-R)\bigr)^N\to0$ because $R<\rho-R$. Hence $\sup_{\abs{z}\le R}\abs{\Psi}<\delta$ for all large $N$, and such a $G$ lies in $U\cap V_n$. Since the basic neighbourhoods generate the topology, $V_n$ is dense.

:::

:::

::: {.pf-step #s6}

Any $G\in\bigcap_{n\ge1}V_n$ has the required property, so such an entire function exists.

::: pf-proof

The space $\mathcal E$ is complete, so Baire's theorem applies to the countable family of open dense sets $V_n$, and $\bigcap_nV_n\ne\varnothing$; in fact it is dense.

Fix $G\in\bigcap_nV_n$. Take the enumeration with each polynomial occurring infinitely often, which is harmless for the conclusion. Let $h$ be entire and let $\varepsilon>0$ and a compact set $K$ be given. Choose a polynomial $q$ with rational real and imaginary parts such that $\sup_{K}\abs{q-h}<\varepsilon/2$, which is possible because the Taylor polynomials of $h$ converge uniformly on $K$ and their coefficients can be perturbed to Gaussian rationals. Since $q$ occurs infinitely often in the enumeration, there are arbitrarily large $n$ with $p_n=q$; fix such an $n$ with $K\subseteq D(0,n)$ and $1/n<\varepsilon/2$. Because $G\in V_n$, there is $N\ge n$ with
$$
\sup_{\abs{z}\le n}\abs{D^NG(z)-p_n(z)}<\tfrac1n .
$$
Then $\sup_K\abs{D^NG-h}<\frac1n+\frac{\varepsilon}{2}<\varepsilon$.

Repeating this with $K=D(0,k)$ and $\varepsilon=1/k$, and choosing at each step an index larger than the previous one — which is possible because the set of admissible $n$, hence of admissible $N$, is unbounded — produces a strictly increasing sequence $N_1<N_2<\cdots$ with $\sup_{\abs{z}\le k}\abs{D^{N_k}G-h}<1/k$. For a compact $K\subseteq D(0,k_0)$ and $k\ge k_0$ this gives $\sup_K\abs{D^{N_k}G-h}<1/k\to0$. Hence $D^{N_k}G\to h$ uniformly on every compact subset of $\CC$.

:::

:::

:::

:::
