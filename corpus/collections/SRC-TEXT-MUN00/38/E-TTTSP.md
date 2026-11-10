---
schema: qual/card@1
id: E-TTTSP
kind: problem
title: Compactifications of the minimal uncountable well-ordered set
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Møller, "Solutions to exercises in Munkres", file S38.pdf,
    Exercise 38.5, page 1 of the file (tmp/sources/munkres-solutions-poulsen-S38.pdf; the sheet is dated
    2 April 2005 and its section-38 items name no author; Internet Archive snapshot 20181222125939 of
    web.math.ku.dk/~moller/e02/3gt/opg/S38.pdf). Checked against Munkres, Topology (2000), Section 38
    Exercise 5, printed p. 241, with Theorem 38.5 (the characterisation of beta(X) by extension of
    bounded real functions), Theorem 38.4 and the preceding exercise 38.4, and with the order topology of
    S_Omega = [0, Omega). What was corrected: on part (a) the card's earlier increasing-sequence argument
    chose pairs alpha_n < beta_n and then called the supremum of the beta_n a common limit of both
    sequences, which the choice of alpha_n does not give, and it then deduced |f(beta) - f(gamma)| < 1/n
    from two bounds of the form |f(beta) - f(alpha_n)| < 1/n, which only gives 2/n. The card's part (a) is
    here the sheet's argument: from the failure of the epsilon-bound one gets a single strictly increasing
    sequence gamma_n with |f(gamma_n) - f(gamma_{n-1})| >= epsilon, whose supremum lambda is a countable
    ordinal, hence below Omega, and continuity at lambda contradicts it; the 2/n is then taken correctly
    and f is constant on the tail. Parts (b) and (c) are the sheet's; (c) uses part (b) to see that
    beta(S_Omega) - S_Omega is a single point, hence so is Y - S_Omega for any compactification Y, and
    that a compactification adjoining one point to a locally compact Hausdorff space is its one-point
    compactification.
---

::: {.exercise}

(a) Show that every continuous real-valued function defined on $S_\Omega$ is "eventually constant."
[Hint: First prove that for each $\epsilon$, there is an element $\alpha$ of $S_\Omega$ such that $\abs{f(\beta) - f(\alpha)} < \epsilon$ for all $\beta > \alpha$. Then let $\epsilon = 1/n$ for $n \in \ZZ_+$ and consider the corresponding points $\alpha_n$.]

(b) Show that the one-point compactification of $S_\Omega$ and the Stone-Čech compactification are equivalent.

(c) Conclude that every compactification of $S_\Omega$ is equivalent to the one-point compactification.
:::

::: {.solution}
Write $S_\Omega=[0,\Omega)$, where $\Omega$ is the first uncountable ordinal.

(a) We prove first: for every $\varepsilon>0$ there is $\alpha<\Omega$ with
$$
\abs{f(\beta)-f(\alpha)}<\varepsilon\qquad(\beta>\alpha).
$$
Suppose not. Set $\gamma_0=0$ and choose recursively $\gamma_n>\gamma_{n-1}$ with
$\abs{f(\gamma_n)-f(\gamma_{n-1})}\ge\varepsilon$. The supremum
$$
\lambda=\sup_n\gamma_n
$$
is a countable ordinal, hence $\lambda<\Omega$, and $\gamma_n\to\lambda$ in the order topology, so by continuity $f(\gamma_n)\to f(\lambda)$ and $\abs{f(\gamma_n)-f(\gamma_{n-1})}<\varepsilon$ for $n$ large, a contradiction.

For each $n\ge1$ choose $\alpha_n<\Omega$ with $\abs{f(\beta)-f(\alpha_n)}<1/n$ for all $\beta>\alpha_n$, and let
$$
\alpha=\sup_n\alpha_n<\Omega,
$$
a countable supremum of countable ordinals. If $\beta,\gamma>\alpha$, then
$$
\abs{f(\beta)-f(\gamma)}\le\abs{f(\beta)-f(\alpha_n)}+\abs{f(\gamma)-f(\alpha_n)}<\frac2n
$$
for every $n$, hence $f(\beta)=f(\gamma)$: the function $f$ is constant on the tail $(\alpha,\Omega)$.

(b) Let $S_\Omega^*=S_\Omega\cup\{\Omega\}$ be the one-point compactification, which is the ordinal interval $[0,\Omega]$. Every bounded continuous real-valued function on $S_\Omega$ is eventually constant by (a), so it extends continuously to $\Omega$ by assigning that eventual constant value there. By the characterisation of the Stone--Čech compactification as the compactification to which every bounded continuous real-valued function extends (Theorems 38.2 and 38.5), $S_\Omega^*$ is equivalent to $\beta S_\Omega$.

(c) Let $Y$ be any compactification of $S_\Omega$. By maximality of the Stone--Čech compactification there is a continuous surjection
$$
q:\beta S_\Omega\longrightarrow Y
$$
that is the identity on $S_\Omega$. By (b), $\beta S_\Omega-S_\Omega$ consists of the single point $\Omega$. Since $q$ fixes every point of $S_\Omega$ and is onto, $Y-S_\Omega=q(\{\Omega\})$ has at most one point; it is nonempty because $S_\Omega$ is not compact. So $Y-S_\Omega=\{p\}$, and since $S_\Omega$ is locally compact and Hausdorff, the open sets of $Y$ meeting $Y-S_\Omega$ are the complements in $Y$ of the compact subsets of $S_\Omega$, which is the topology of the one-point compactification. Thus $Y$ is equivalent to $S_\Omega^*$.
:::
