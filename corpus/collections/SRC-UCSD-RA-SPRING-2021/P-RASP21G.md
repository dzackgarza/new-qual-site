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
---

::: {.problem}
Let $\mu$ be a $\sigma$-finite Radon measure on an LCH space $X$, and $\varphi$ a positive continuous function on $X$.
Show that $\nu(E) := \int_E \varphi\,d\mu$ defines a Radon measure $\nu$ on $X$.

Hint: First consider the positive linear functional $I(f) := \int f\varphi\,d\mu$ on $C_c(X)$ and show that $\nu$ coincides with the Radon measure associated with this functional on open sets.
:::


::: {.solution}
Define
$$
I:C_c(X)\to\RR,
\qquad
I(f):=\int_X f\varphi\,d\mu.
$$
Because $\varphi\ge0$, the functional $I$ is positive. It is also well defined: if $f\in C_c(X)$ and $K=\operatorname{supp}f$, then $\varphi$ is bounded on $K$ and $\mu(K)<\infty$, so
$$
\int_X\abs{f}\varphi\,d\mu
\le \norm{f}_\infty\sup_K\varphi\,\mu(K)<\infty.
$$

By the Riesz--Markov representation theorem, there is a unique Radon measure $\lambda$ on $X$ such that
$$
I(f)=\int_X f\,d\lambda
\qquad(f\in C_c(X)).
$$
We show that $\lambda$ is precisely
$$
\nu(E):=\int_E\varphi\,d\mu.
$$

**Step 1: $\lambda=\nu$ on open sets.** Let $U\subseteq X$ be open and let
$$
\Phi_U:=\{f\in C_c(X):0\le f\le1,\ \operatorname{supp}f\subseteq U\}.
$$
For the Radon measure $\lambda$,
$$
\lambda(U)=\sup_{f\in\Phi_U}\int f\,d\lambda=\sup_{f\in\Phi_U}\int f\varphi\,d\mu.
$$
The family $\{f\varphi:f\in\Phi_U\}$ consists of nonnegative continuous functions, is directed upward (if $f,g\in\Phi_U$ then $\max(f,g)\in\Phi_U$), and its pointwise supremum is $\varphi\mathbf 1_U$, because for $x\in U$ Urysohn's lemma gives $f\in\Phi_U$ with $f(x)=1$. For a Radon measure $\mu$, the integral of the supremum of an upward-directed family of nonnegative lower semicontinuous functions is the supremum of the integrals (Folland, Proposition 7.12). Hence
$$
\lambda(U)=\int_U\varphi\,d\mu=\nu(U).
$$

**Step 2: $\nu\le\lambda$.** $\lambda$ is outer regular, so for every Borel $E$,
$$
\lambda(E)=\inf_{U\supseteq E\text{ open}}\lambda(U)=\inf_{U\supseteq E\text{ open}}\nu(U)\ge\nu(E).
$$

**Step 3: $\lambda\le\nu$.** Since $\mu$ is $\sigma$-finite, write $X=\bigcup_jF_j$ with $\mu(F_j)<\infty$, and set
$$
A_{j,k}:=F_j\cap\{k-1\le\varphi<k\}\qquad(j,k\ge1),
$$
countably many Borel sets of finite $\mu$-measure covering $X$; enumerate them as $A_1,A_2,\ldots$, with $\varphi<k_m$ on $A_m$. Let $E$ be Borel and $\varepsilon>0$. Since $\mu$ is outer regular and $\mu(E\cap A_m)<\infty$, there is an open $U_m\supseteq E\cap A_m$ with
$$
\mu\bigl(U_m\setminus(E\cap A_m)\bigr)<\frac{\varepsilon}{2^mk_m}.
$$
Replacing $U_m$ by the open set $U_m\cap\{\varphi<k_m\}$, which still contains $E\cap A_m$, gives
$$
\nu\bigl(U_m\setminus(E\cap A_m)\bigr)\le k_m\,\mu\bigl(U_m\setminus(E\cap A_m)\bigr)<\frac{\varepsilon}{2^m}.
$$
The open set $U:=\bigcup_mU_m$ contains $E$ and satisfies $U\setminus E\subseteq\bigcup_m\bigl(U_m\setminus(E\cap A_m)\bigr)$, so $\nu(U\setminus E)<\varepsilon$. By Step 1,
$$
\lambda(E)\le\lambda(U)=\nu(U)\le\nu(E)+\varepsilon.
$$
As $\varepsilon$ is arbitrary, $\lambda(E)\le\nu(E)$.

Steps 2 and 3 give $\lambda=\nu$ on all Borel sets. Since $\lambda$ is Radon, so is $\nu$:
$$
\boxed{\nu(E)=\int_E\varphi\,d\mu\text{ defines a Radon measure on }X.}
$$
:::
