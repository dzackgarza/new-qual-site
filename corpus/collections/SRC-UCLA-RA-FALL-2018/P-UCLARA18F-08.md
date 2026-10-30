---
schema: qual/card@1
id: P-UCLARA18F-08
kind: problem
title: Completeness and coefficient characterization of the Dirichlet space
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 8. Let $\mathcal D$ be the space of analytic functions $f(z)$ on the unit disc
$$
\DD=\{z:\abs{z}<1\}
$$
such that $f(0)=0$ and
$$
\int_{\DD}\abs{f'(z)}^2\,dx\,dy<\infty.
$$

(a) Prove that $\mathcal D$ is complete in the norm
$$
\norm{f}=\left(\int_{\DD}\abs{f'(z)}^2\,dx\,dy\right)^{1/2}.
$$

(b) Give a necessary and sufficient condition on the coefficients $a_n$ for the function
$$
f(z)=\sum_{n\ge1}a_nz^n
$$
to belong to $\mathcal D$.
:::

::: {.solution}

Write $dA=dx\,dy$.

::: pf

::: {.pf-step #s1-1}

For every $0<r<1$ there is a constant $C_r>0$ such that every holomorphic $h\in L^2(\DD,dA)$ satisfies
$$
\sup_{\abs{z}\le r}\abs{h(z)}\le C_r\norm{h}_{L^2(\DD)}.
$$


::: pf-proof

Put $\rho=(1-r)/2$. If $\abs{z}\le r$, then $B(z,\rho)\subset\DD$. The area mean-value formula for the holomorphic function $h$, followed by Cauchy--Schwarz, gives
$$
\begin{aligned}
\abs{h(z)}
&=\abs{\frac1{\pi\rho^2}\int_{B(z,\rho)}h(w)\,dA(w)}\\
&\le\frac1{\pi\rho^2}\bigl(\pi\rho^2\bigr)^{1/2}
\norm{h}_{L^2(\DD)}\\
&=\frac1{\sqrt\pi\rho}\norm{h}_{L^2(\DD)}.
\end{aligned}
$$
Thus one may take $C_r=1/(\sqrt\pi\rho)$.

:::

:::

::: {.pf-step #s1-2}

Let $(f_j)$ be Cauchy in $\mathcal D$. Then $(f_j')$ converges in $L^2(\DD)$ to some $g\in L^2(\DD)$, and it also converges locally uniformly on $\DD$ to a holomorphic function $h$.


::: pf-proof

By definition of the norm,
$$
\norm{f_j'-f_k'}_{L^2}=\norm{f_j-f_k}_{\mathcal D},
$$
so $(f_j')$ is Cauchy in the complete space $L^2(\DD)$ and hence converges there to some $g$.

Fix $0<r<1$. Applying step [](#s1-1){.pf-ref} to $h=f_j'-f_k'$ gives
$$
\sup_{\abs{z}\le r}\abs{f_j'(z)-f_k'(z)}
\le C_r\norm{f_j'-f_k'}_{L^2}\longrightarrow0.
$$
Thus $(f_j')$ is uniformly Cauchy on every closed disc $\{\abs{z}\le r\}$. It therefore has a locally uniform limit $h$, and a locally uniform limit of holomorphic functions is holomorphic.

:::

:::

::: {.pf-step #s1-3}

The functions $g$ and $h$ agree almost everywhere on $\DD$.


::: pf-proof

From $f_j'\to g$ in $L^2$, choose a subsequence $(f_{j_k}')$ converging to $g$ almost everywhere. The same subsequence converges pointwise everywhere to the locally uniform limit $h$. Hence $g=h$ almost everywhere.

:::

:::

::: {.pf-step #s1-4}

There is a unique holomorphic function $F$ on $\DD$ such that
$$
F(0)=0,
\qquad
F'=h,
$$
and $F\in\mathcal D$.


::: pf-proof

The unit disc is simply connected, so the holomorphic function $h$ has a primitive. Fix the additive constant by requiring $F(0)=0$. By step [](#s1-3){.pf-ref},
$$
\int_{\DD}\abs{F'}^2\,dA
=\int_{\DD}\abs{h}^2\,dA
=\int_{\DD}\abs{g}^2\,dA<\infty,
$$
so $F\in\mathcal D$. Uniqueness follows because two primitives with the same value at $0$ differ by the zero constant.

:::

:::

::: {.pf-step #s1-5}

One has $f_j\to F$ in $\mathcal D$. Consequently $\boxed{\mathcal D\text{ is complete}}$.


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref},
$$
\norm{f_j-F}_{\mathcal D}
=\norm{f_j'-F'}_{L^2}
=\norm{f_j'-g}_{L^2}\longrightarrow0.
$$
Thus every Cauchy sequence converges in $\mathcal D$.

:::

:::

::: {.pf-step #s1-6}

If
$$
f(z)=\sum_{n\ge1}a_nz^n
$$
is analytic on $\DD$, then for every $0<R<1$,
$$
\int_{\abs{z}<R}\abs{f'(z)}^2\,dA(z)
=\pi\sum_{n=1}^\infty n\abs{a_n}^2R^{2n}.
$$


::: pf-proof

On $\abs{z}\le R$, the differentiated power series
$$
f'(z)=\sum_{n=1}^\infty na_nz^{n-1}
$$
converges uniformly on every slightly larger closed disc. Writing $z=re^{i\theta}$, orthogonality of the exponentials gives
$$
\int_0^{2\pi}\abs{f'(re^{i\theta})}^2\,d\theta
=2\pi\sum_{n=1}^\infty n^2\abs{a_n}^2r^{2n-2}.
$$
Integrating in $r$ from $0$ to $R$ yields
$$
\begin{aligned}
\int_{\abs{z}<R}\abs{f'(z)}^2\,dA(z)
&=2\pi\sum_{n=1}^\infty n^2\abs{a_n}^2
\int_0^R r^{2n-1}\,dr\\
&=\pi\sum_{n=1}^\infty n\abs{a_n}^2R^{2n}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-7}

The exact norm identity is
$$
\norm{f}_{\mathcal D}^2
=\pi\sum_{n=1}^\infty n\abs{a_n}^2,
$$
with either side allowed to be $+\infty$.


::: pf-proof

Let $R\uparrow1$ in step [](#s1-6){.pf-ref}. The discs $\{\abs{z}<R\}$ increase to $\DD$, so monotone convergence gives convergence of the left side to $\int_{\DD}\abs{f'}^2dA$. On the right, each nonnegative term $n\abs{a_n}^2R^{2n}$ increases to $n\abs{a_n}^2$, so monotone convergence for series gives the displayed identity.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
f\in\mathcal D
\quad\Longleftrightarrow\quad
\sum_{n=1}^\infty n\abs{a_n}^2<\infty}.
$$


::: pf-proof

The function already has $f(0)=0$ because its power series starts at $n=1$. By step [](#s1-7){.pf-ref}, the defining integral for $\mathcal D$ is finite exactly when the displayed weighted square sum is finite.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves part (a), and step [](#s1-8){.pf-ref} proves part (b).

:::

:::

:::
