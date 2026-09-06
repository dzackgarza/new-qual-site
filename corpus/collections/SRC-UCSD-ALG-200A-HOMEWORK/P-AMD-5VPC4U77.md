---
schema: qual/card@1
id: P-AMD-5VPC4U77
kind: problem
title: Conjugating or precomposing a semidirect-product action preserves the semidirect product up to isomorphism
classification:
  areas:
  - algebra
  topics:
  - Semidirect Products
  - Automorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 5, Exercise 1. Restored
    the source hypothesis in part (b) that rho is an automorphism of K and
    separated the two modified actions unambiguously.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Conjugating the action by theta is transported by (h,k) -> (theta(h),k).
    Precomposing the action by rho is transported in the opposite direction by
    (h,k) -> (h,rho(k)). Both maps respect the defining semidirect-product
    multiplication and are bijective because theta and rho are automorphisms.
---

::: {.problem}
Let $H$ and $K$ be groups and let
\[
\psi:K\longrightarrow\operatorname{Aut}(H)
\]
be a homomorphism.

(a) Let $\theta\in\operatorname{Aut}(H)$ and define
\[
\phi_\theta:\operatorname{Aut}(H)\longrightarrow\operatorname{Aut}(H),
\qquad
\phi_\theta(\alpha)=\theta\alpha\theta^{-1}.
\]
Set
\[
\psi_\theta=\phi_\theta\circ\psi.
\]
Prove that
\[
H\rtimes_\psi K\cong H\rtimes_{\psi_\theta}K.
\]

(b) Let $\rho\in\operatorname{Aut}(K)$ and set
\[
\psi_\rho=\psi\circ\rho.
\]
Prove that
\[
H\rtimes_\psi K\cong H\rtimes_{\psi_\rho}K.
\]
:::

::: {.solution}
Recall that the multiplication in $H\rtimes_\psi K$ is
\[
(h_1,k_1)(h_2,k_2)
=\bigl(h_1\psi(k_1)(h_2),k_1k_2\bigr).
\]

<1>1. The map
\[
\Phi:H\rtimes_\psi K\longrightarrow H\rtimes_{\psi_\theta}K,
\qquad
\Phi(h,k)=(\theta(h),k),
\]
is a homomorphism.
::: {.proof}
For $(h_1,k_1),(h_2,k_2)\in H\rtimes_\psi K$,
\[
\begin{aligned}
\Phi\bigl((h_1,k_1)(h_2,k_2)\bigr)
&=\Phi\bigl(h_1\psi(k_1)(h_2),k_1k_2\bigr)\\
&=\bigl(\theta(h_1)\,\theta(\psi(k_1)(h_2)),k_1k_2\bigr).
\end{aligned}
\]
By definition of $\psi_\theta$,
\[
\psi_\theta(k_1)(\theta(h_2))
=(\theta\psi(k_1)\theta^{-1})(\theta(h_2))
=\theta(\psi(k_1)(h_2)).
\]
Therefore
\[
\Phi\bigl((h_1,k_1)(h_2,k_2)\bigr)
=\bigl(\theta(h_1),k_1\bigr)
 \bigl(\theta(h_2),k_2\bigr)
=\Phi(h_1,k_1)\Phi(h_2,k_2),
\]
where the product on the right is taken in $H\rtimes_{\psi_\theta}K$.
:::

<1>2. The map $\Phi$ is an isomorphism.
::: {.proof}
Since $\theta$ is an automorphism of $H$, the map
\[
(h,k)\longmapsto(\theta^{-1}(h),k)
\]
is an inverse to $\Phi$.
Thus $\Phi$ is bijective, and <1>1 shows it is a homomorphism.
Hence
\[
H\rtimes_\psi K\cong H\rtimes_{\psi_\theta}K.
\]
This proves part (a).
:::

<1>3. The map
\[
\Psi:H\rtimes_{\psi_\rho}K\longrightarrow H\rtimes_\psi K,
\qquad
\Psi(h,k)=(h,\rho(k)),
\]
is a homomorphism.
::: {.proof}
For $(h_1,k_1),(h_2,k_2)\in H\rtimes_{\psi_\rho}K$,
\[
\begin{aligned}
\Psi\bigl((h_1,k_1)(h_2,k_2)\bigr)
&=\Psi\bigl(h_1\psi_\rho(k_1)(h_2),k_1k_2\bigr)\\
&=\bigl(h_1\psi(\rho(k_1))(h_2),\rho(k_1k_2)\bigr)\\
&=\bigl(h_1\psi(\rho(k_1))(h_2),\rho(k_1)\rho(k_2)\bigr).
\end{aligned}
\]
The last expression is precisely
\[
(h_1,\rho(k_1))(h_2,\rho(k_2))
=\Psi(h_1,k_1)\Psi(h_2,k_2)
\]
in $H\rtimes_\psi K$.
:::

<1>4. The map $\Psi$ is an isomorphism.
::: {.proof}
Since $\rho$ is an automorphism of $K$, the map
\[
(h,k)\longmapsto(h,\rho^{-1}(k))
\]
is an inverse to $\Psi$.
Thus $\Psi$ is bijective, and <1>3 shows it is a homomorphism.
Hence
\[
H\rtimes_{\psi_\rho}K\cong H\rtimes_\psi K,
\]
and therefore
\[
H\rtimes_\psi K\cong H\rtimes_{\psi_\rho}K.
\]
This proves part (b).
:::
:::
