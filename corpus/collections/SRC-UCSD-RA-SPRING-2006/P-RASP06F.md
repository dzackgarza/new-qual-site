---
schema: qual/card@1
id: P-RASP06F
kind: problem
title: "Sobolev-type embedding via weighted L^p norms"
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
  note: Checked against Problem 6 of the official UCSD Spring 2006 real-analysis qualifying exam. The source quantifies C_t uniformly over every 1 <= r < p < infinity while also requiring C_t -> 0. That uniform statement is false as p approaches r; the card corrects the conclusion to fixed r,p, which is the estimate produced by the stated hint.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
For each $N \in \mathbb{R}$ define in $\mathbb{R}^n$ the measures $d\mu_N := (1 + |x|)^N\,dx$ and, for each $1 \leq p < \infty$, the norms
$$
\|f\|_{p,N} := \|f\|_{L^p(\mathbb{R}^n, d\mu_N)} = \left(\int_{\mathbb{R}^n} |f(x)|^p (1 + |x|)^N\,dx\right)^{1/p}.
$$

(a) Fix $1 \leq r < p < \infty$. Show that for every $t > 0$ there is a constant $C_{t,r,p}$ such that, with
$$
N_t := \frac{Np + n(p-r) + t(p-r)}{r}
$$
the estimate $\|f\|_{r,N} \leq C_{t,r,p} \|f\|_{p,N_t}$ holds.

(b) For fixed $r<p$, show that the constants can be chosen so that $C_{t,r,p} \to 0$ as $t \to \infty$.

Hint: For part (a), observe that $1 = (1 + |x|)^M / (1 + |x|)^M$.
:::

::: solution
<1>1. Apply Hölder with the weight split dictated by $N_t$.
::: proof
Fix $1\le r<p<\infty$ and set
\[
q=\frac p r,
\qquad
q'=\frac p{p-r}.
\]
Then
\[
\begin{aligned}
\|f\|_{r,N}^r
&=\int_{\mathbb R^n}|f(x)|^r(1+|x|)^N\,dx\\
&=\int_{\mathbb R^n}
\Bigl(|f(x)|^r(1+|x|)^{rN_t/p}\Bigr)
(1+|x|)^{N-rN_t/p}\,dx.
\end{aligned}
\]
Hölder's inequality with exponents $q$ and $q'$ gives
\[
\begin{aligned}
\|f\|_{r,N}^r
&\le
\left(\int |f|^p(1+|x|)^{N_t}\,dx\right)^{r/p}\\
&\qquad\cdot
\left(\int (1+|x|)^{(N-rN_t/p)p/(p-r)}\,dx\right)^{(p-r)/p}.
\end{aligned}
\]
By the definition of $N_t$,
\[
\frac p{p-r}\left(N-\frac{rN_t}{p}\right)=-(n+t).
\]
Hence, with
\[
I_t:=\int_{\mathbb R^n}(1+|x|)^{-n-t}\,dx<\infty,
\]
we obtain
\[
\|f\|_{r,N}^r
\le
\|f\|_{p,N_t}^r I_t^{(p-r)/p}.
\]
Taking $r$th roots gives
\[
\boxed{
\|f\|_{r,N}
\le C_{t,r,p}\|f\|_{p,N_t},
\qquad
C_{t,r,p}:=I_t^{1/r-1/p}.}
\]
:::

<1>2. Show that the constant tends to zero for fixed $r<p$.
::: proof
For $t\ge1$,
\[
0\le(1+|x|)^{-n-t}\le(1+|x|)^{-n-1},
\]
and the right-hand side is integrable on $\mathbb R^n$. Also
\[
(1+|x|)^{-n-t}\longrightarrow0
\]
for every $x\ne0$. By dominated convergence,
\[
I_t\longrightarrow0.
\]
Since
\[
\frac1r-\frac1p>0,
\]
it follows that
\[
\boxed{C_{t,r,p}=I_t^{1/r-1/p}\longrightarrow0.}
\]
:::

<1>3. Explain why the source's uniform quantifier cannot hold.
::: proof
The source asks for a single $C_t$ valid for every $1\le r<p<\infty$ and also satisfying $C_t\to0$. This cannot hold.

Indeed, fix $t>0$ and a bounded measurable set $E$ of positive finite measure. For fixed $r$ and $p\downarrow r$, one has
\[
N_t\longrightarrow N,
\]
and therefore, for $f=\mathbf1_E$,
\[
\frac{\|f\|_{r,N}}{\|f\|_{p,N_t}}\longrightarrow1.
\]
Thus any constant valid uniformly for all $r<p$ must satisfy $C_t\ge1$. Such constants cannot converge to $0$ as $t\to\infty$. The fixed-$(r,p)$ formulation proved above is therefore the valid statement.
:::
:::
