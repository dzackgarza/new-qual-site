---
schema: qual/card@1
id: P-RASP21G
kind: problem
title: "Absolutely continuous measure via continuous density"
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
  date: 2026-09-09
  note: Checked against Problem 7 of the official UCSD Spring 2021 real-analysis qualifying exam. The card omitted the source hypothesis that phi is positive; that hypothesis is restored.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. Checked: the well-definedness of the functional (φ bounded on the compact support, μ locally finite), Riesz-Markov, the open-set identification through inner regularity of λ, Urysohn and the directed-family monotone convergence, and both inequalities on Borel sets. Two things the prose passed over are now steps: the epsilon-approximation of E cap A_m by an open set on which φ < k_m (which is what makes the bound ν <= k_m μ available), and the countable subadditivity covering U minus E by the sets U_m minus (E cap A_m), including the inclusion E cap A_m ⊆ E that makes it work. The card also states at the end what Radon means here (locally finite, outer regular, inner regular on open sets) rather than leaving "since λ is Radon, so is ν" to the reader. The citation of Folland, Proposition 7.12 for the directed-family monotone convergence is the card's own and is preserved. No statement repair; the proof is correct.
---

::: {.problem}
Let $\mu$ be a $\sigma$-finite Radon measure on an LCH space $X$, and $\varphi$ a positive continuous function on $X$.
Show that $\nu(E) := \int_E \varphi\,d\mu$ defines a Radon measure $\nu$ on $X$.

Hint: First consider the positive linear functional $I(f) := \int f\varphi\,d\mu$ on $C_c(X)$ and show that $\nu$ coincides with the Radon measure associated with this functional on open sets.
:::


::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own, following the hint and Folland's treatment (the monotone convergence step for lower semicontinuous functions is Folland, Proposition 7.12, as the card records).

Let $X$ be locally compact Hausdorff, $\mu$ a $\sigma$-finite Radon measure on $X$ and $\varphi:X\to(0,\infty)$ continuous; put $\nu(E)=\int_E\varphi\,d\mu$ for Borel $E$.

::: pf

::: {.pf-step #functional}
$I(f)=\int_Xf\varphi\,d\mu$ defines a positive linear functional on $C_c(X)$.

::: pf-proof
Linearity is linearity of the integral; positivity because $f\ge0$ and $\varphi>0$ give $f\varphi\ge0$. For $f\in C_c(X)$ with $K=\operatorname{supp}f$, the continuous $\varphi$ is bounded on the compact $K$ and $\mu(K)<\infty$ because $\mu$ is Radon (locally finite), so
$$
\int_X\abs f\,\varphi\,d\mu\le\norm f_\infty\Bigl(\sup_K\varphi\Bigr)\mu(K)<\infty,
$$
and $I(f)$ is a finite real number.
:::

:::

::: {.pf-step #riesz}
There is a Radon measure $\lambda$ on $X$ with $I(f)=\int_Xf\,d\lambda$ for every $f\in C_c(X)$.

::: pf-proof
$X$ is locally compact Hausdorff and $I$ is a positive linear functional on $C_c(X)$, so the Riesz–Markov representation theorem applies.
:::

:::

::: {.pf-step #open}
$\lambda(U)=\nu(U)$ for every open $U\subseteq X$.

::: pf-proof
Let $\Phi_U=\{f\in C_c(X):0\le f\le1,\ \operatorname{supp}f\subseteq U\}$. For a Radon measure, $\lambda(U)=\sup\{\lambda(K):K\subseteq U\ \text{compact}\}$, and Urysohn's lemma gives, for each such $K$, an $f\in\Phi_U$ with $f=1$ on $K$; conversely $\int f\,d\lambda\le\lambda(U)$ for $f\in\Phi_U$. Hence
$$
\lambda(U)=\sup_{f\in\Phi_U}\int_Xf\,d\lambda=\sup_{f\in\Phi_U}\int_Xf\varphi\,d\mu .
$$
The family $\{f\varphi:f\in\Phi_U\}$ consists of nonnegative continuous functions, is directed upward (as $\max(f,g)\in\Phi_U$), and has pointwise supremum $\varphi\mathbf 1_U$: the inequality $\le$ is clear, and for $x\in U$ Urysohn gives $f\in\Phi_U$ with $f(x)=1$. For a Radon measure, the integral of the supremum of an upward-directed family of nonnegative lower semicontinuous functions is the supremum of the integrals (Folland, Proposition 7.12), so
$$
\lambda(U)=\int_X\varphi\mathbf 1_U\,d\mu=\nu(U).
$$
:::

:::

::: {.pf-step #above}
$\lambda(E)\ge\nu(E)$ for every Borel $E$.

::: pf-proof
A Radon measure is outer regular on Borel sets, so
$$
\lambda(E)=\inf\{\lambda(U):U\supseteq E\ \text{open}\}=\inf\{\nu(U):U\supseteq E\ \text{open}\}\ge\nu(E),
$$
the middle equality by step [](#open){.pf-ref} and the last inequality because $E\subseteq U$ gives $\nu(E)\le\nu(U)$.
:::

:::

::: {.pf-step #below}
$\lambda(E)\le\nu(E)$ for every Borel $E$.

::: pf-proof
Since $\mu$ is $\sigma$-finite, $X=\bigcup_jF_j$ with $F_j$ Borel and $\mu(F_j)<\infty$. The countably many Borel sets $A_{j,k}=F_j\cap\{k-1\le\varphi<k\}$, $j,k\ge1$, cover $X$ and have $\mu(A_{j,k})<\infty$; enumerate them as $A_1,A_2,\dots$ and record $k_m\ge1$ with $\varphi<k_m$ on $A_m$.

::: {.pf-step #approx}
Fix a Borel $E$ and $\varepsilon>0$. There is an open $U_m\supseteq E\cap A_m$ with $\varphi<k_m$ on $U_m$ and $\nu\bigl(U_m\setminus(E\cap A_m)\bigr)<\varepsilon/2^m$.

::: pf-proof
$\mu$ is outer regular and $\mu(E\cap A_m)\le\mu(A_m)<\infty$, so there is an open $V_m\supseteq E\cap A_m$ with $\mu(V_m\setminus(E\cap A_m))<\varepsilon/(2^mk_m)$. Let $U_m=V_m\cap\{\varphi<k_m\}$, which is open because $\varphi$ is continuous and contains $E\cap A_m$ because $\varphi<k_m$ there. Then $U_m\setminus(E\cap A_m)\subseteq V_m\setminus(E\cap A_m)$ and $\varphi<k_m$ on $U_m$, so
$$
\nu\bigl(U_m\setminus(E\cap A_m)\bigr)=\int_{U_m\setminus(E\cap A_m)}\varphi\,d\mu\le k_m\,\mu\bigl(U_m\setminus(E\cap A_m)\bigr)<\frac{\varepsilon}{2^m}.
$$
:::

:::

::: {.pf-step #cover}
With $U=\bigcup_mU_m$: $U$ is open, contains $E$, and $\nu(U\setminus E)<\varepsilon$.

::: pf-proof
$U$ is open as a union of open sets and contains $E=\bigcup_m(E\cap A_m)$. If $x\in U\setminus E$ then $x\in U_m$ for some $m$ and $x\notin E$, hence $x\in U_m\setminus(E\cap A_m)$ because $E\cap A_m\subseteq E$; so $U\setminus E\subseteq\bigcup_m\bigl(U_m\setminus(E\cap A_m)\bigr)$ and by countable subadditivity
$$
\nu(U\setminus E)\le\sum_m\nu\bigl(U_m\setminus(E\cap A_m)\bigr)<\sum_m\frac{\varepsilon}{2^m}=\varepsilon .
$$
:::

:::

:::

:::

::: {.pf-step #equality}
$\lambda(E)=\nu(E)$ for every Borel $E$.

::: pf-proof
By steps [](#approx){.pf-ref} and [](#cover){.pf-ref} there is, for each $\varepsilon>0$, an open $U\supseteq E$ with $\nu(U\setminus E)<\varepsilon$; then
$$
\lambda(E)\le\lambda(U)=\nu(U)\le\nu(E)+\nu(U\setminus E)<\nu(E)+\varepsilon
$$
by step [](#open){.pf-ref} and additivity of $\nu$, and $\varepsilon$ is arbitrary, so $\lambda(E)\le\nu(E)$; with step [](#above){.pf-ref} this gives equality.
:::

:::

::: {.pf-step}
$\nu$ is a Radon measure on $X$.

::: pf-proof
$\nu(E)=\int_E\varphi\,d\mu$ is a measure on the Borel sets, being the integral of a nonnegative measurable density against $\mu$, and by step [](#equality){.pf-ref} it agrees there with the Radon measure $\lambda$ of step [](#riesz){.pf-ref}. Hence $\nu$ is locally finite ($\nu(K)=\lambda(K)<\infty$ on compact $K$), outer regular and inner regular on open sets, i.e. Radon.
:::

:::

:::
:::
