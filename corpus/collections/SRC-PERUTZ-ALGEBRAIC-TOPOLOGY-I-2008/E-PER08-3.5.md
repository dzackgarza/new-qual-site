---
schema: qual/card@1
id: E-PER08-3.5
kind: problem
title: Rectangular subdivision lemma for a homotopy
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 3.5 and Lemma 3.7 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the compact pullback-cover/Lebesgue-number argument and refinement of arbitrary prescribed endpoint subdivisions.
---

::: {.problem}
Suppose $X=U\cup V$, where $U$ and $V$ are open, and let
\[
\Gamma=\{\gamma_t\}_{t\in[0,1]}:I\times I\to X
\]
be a homotopy of based paths $(I,\partial I)\to(X,x)$.

Prove that there are increasing sequences
\[
0=t_0<t_1<\cdots<t_m=1,
\qquad
0=s_0<s_1<\cdots<s_n=1,
\]
such that $\Gamma$ maps every rectangle
\[
[t_i,t_{i+1}]\times[s_j,s_{j+1}]
\]
entirely into $U$ or entirely into $V$.
Moreover, show that the sequence $(s_j)$ can be chosen to refine prescribed subdivisions of $\gamma_0$ and $\gamma_1$.
:::

::: {.solution}
Regard $I\times I$ as the unit square with the Euclidean metric, with first coordinate $t$ and second coordinate $s$.

<1>1. Pull back the cover $X=U\cup V$ to an open cover of the square.
::: {.proof}
Since $\Gamma$ is continuous and $U,V\subseteq X$ are open,
\[
\Gamma^{-1}(U),
\qquad
\Gamma^{-1}(V)
\]
are open subsets of $I^2$. Because $U\cup V=X$,
\[
I^2=\Gamma^{-1}(U)\cup\Gamma^{-1}(V).
\]
Thus these two sets form an open cover of the compact metric space $I^2$.
:::

<1>2. Choose a Lebesgue number for this pullback cover.
::: {.proof}
By the Lebesgue-number lemma, there is a number
\[
\lambda>0
\]
such that every subset of $I^2$ of diameter less than $\lambda$ lies entirely in either $\Gamma^{-1}(U)$ or $\Gamma^{-1}(V)$.
:::

<1>3. Choose the horizontal subdivision so that it refines the prescribed endpoint subdivisions.
::: {.proof}
Let
\[
P_0:0=u_0<\cdots<u_r=1
\]
be a prescribed subdivision of $\gamma_0$, and let
\[
P_1:0=v_0<\cdots<v_q=1
\]
be a prescribed subdivision of $\gamma_1$. Take the finite ordered union of their subdivision points,
\[
P=P_0\cup P_1.
\]

Refine each interval between consecutive points of $P$ by inserting finitely many extra points until every resulting interval has length strictly less than
\[
\frac{\lambda}{\sqrt2}.
\]
Denote the resulting common refinement by
\[
0=s_0<s_1<\cdots<s_n=1.
\]
By construction, $(s_j)$ refines both prescribed subdivisions.
:::

<1>4. Choose the vertical subdivision with the same mesh bound.
::: {.proof}
Choose any finite subdivision
\[
0=t_0<t_1<\cdots<t_m=1
\]
whose mesh satisfies
\[
t_{i+1}-t_i<\frac{\lambda}{\sqrt2}
\]
for every $i$. For example, an equally spaced subdivision with sufficiently many pieces has this property.
:::

<1>5. Every resulting rectangle maps wholly into $U$ or wholly into $V$.
::: {.proof}
Fix $i,j$ and set
\[
R_{ij}=[t_i,t_{i+1}]\times[s_j,s_{j+1}].
\]
Its Euclidean diameter satisfies
\[
\operatorname{diam}(R_{ij})
=\sqrt{(t_{i+1}-t_i)^2+(s_{j+1}-s_j)^2}
<\sqrt{\frac{\lambda^2}{2}+\frac{\lambda^2}{2}}
=\lambda.
\]
By the defining property of the Lebesgue number, $R_{ij}$ lies entirely in one member of the pullback cover. Hence either
\[
R_{ij}\subseteq\Gamma^{-1}(U)
\]
or
\[
R_{ij}\subseteq\Gamma^{-1}(V).
\]
Equivalently,
\[
\Gamma(R_{ij})\subseteq U
\]
or
\[
\Gamma(R_{ij})\subseteq V.
\]
This holds for every rectangle.
:::

The sequences $(t_i)$ and $(s_j)$ therefore have the required property, and <1>3 proves the requested simultaneous refinement of the prescribed subdivisions of $\gamma_0$ and $\gamma_1$.
:::
