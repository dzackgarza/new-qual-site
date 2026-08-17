---
schema: qual/card@1
id: P-JHWCH
kind: problem
title: "a. Prove that if $f, g\\in L^+(\\RR)$ then"
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - measure-theory
  - continuity-of-measure
relations: []
review: draft
---

::: problem
a. Prove that if $f, g\in L^+(\RR)$ then 
\[
\int(f +g) = \int f + \int g
.\]
  Extend this to establish that if $\ts{ f_k} \subseteq L^+(\RR^n)$ then
  \[
  \int \sum_k f_k = \sum_k \int f_k
  .\]


b. Let $\ts{E_j}_{j\in \NN} \subseteq \mathcal{M}(\RR^n)$ with $E_j \nearrow E$. 
  Use the countable additivity of $\mu_f$ on \( \mathcal{M}(\RR^n)  \) established above to show that
  \[
  \mu_f(E) = \lim_{j\to \infty } \mu_f(E_j)
  .\]
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. (a) For $f, g \in L^+(\RR)$: $\int (f + g) = \int f + \int g$.
    <2>1. For simple functions $s = \sum_i a_i \chi_{A_i}$, $t = \sum_j b_j \chi_{B_j}$ (with the $A_i$'s and $B_j$'s disjoint): $\int (s + t) = \sum_i a_i m(A_i) + \sum_j b_j m(B_j) = \int s + \int t$.
        Proof: refine the common refinement $A_i \cap B_j$: $s + t = \sum_{i,j}(a_i + b_j)\chi_{A_i \cap B_j}$, and the integral is the sum over the refinement.
    <2>2. General $f, g$: take simple $s_k \uparrow f$, $t_k \uparrow g$ (approximation by simple functions); then $s_k + t_k \uparrow f + g$ and $\int(f+g) = \lim_k \int(s_k + t_k) = \lim_k (\int s_k + \int t_k) = \int f + \int g$.
        Proof: monotone convergence and <2>1.

<1>2. Extension to countable sums: if $\ts{f_k} \subseteq L^+(\RR^n)$, then $\int \sum_k f_k = \sum_k \int f_k$.
    Proof: by induction, $\int\sum_{k=1}^N f_k = \sum_{k=1}^N\int f_k$ (<1>1, finite case); the partial sums $\sum_{k=1}^N f_k \uparrow \sum_k f_k$, so monotone convergence gives $\int\sum_k f_k = \lim_N \int\sum_{k=1}^N f_k = \lim_N \sum_{k=1}^N \int f_k = \sum_k \int f_k$.

<1>3. (b) If $E_j \nearrow E$ then $\mu_f(E_j) \to \mu_f(E)$, where $\mu_f(E) = \int_E f$.
    <2>1. $\chi_{E_j} \uparrow \chi_E$ pointwise.
        Proof: $E_j \nearrow E$ means $E_j \subseteq E_{j+1}$ and $\bigcup_j E_j = E$.
    <2>2. $\mu_f(E_j) = \int f\chi_{E_j} \uparrow \int f\chi_E = \mu_f(E)$.
        Proof: $f\chi_{E_j} \uparrow f\chi_E$ (as $f \ge 0$), monotone convergence.

<1>4. Q.E.D.
    Proof: <1>2 and <1>3 are the claims. (The "countable additivity of $\mu_f$" referenced in the card is exactly <1>2 with $f_k = f\chi_{E_k \setminus E_{k-1}}$.)
:::
