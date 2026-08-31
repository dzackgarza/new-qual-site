---
schema: qual/card@1
id: P-P2UWB
kind: problem
title: Approximation of measurable sets by elementary sets, and $\lim_{n\to\infty}\int_E\sin(nt)\,dt=0$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Convergence of Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Recall that a set $E \subset \mathbb{R}^{d}$ is measurable if for every $c>0$ there is an open set $U \subseteq \RR^d$ such that $m^{*}(U \sm E)<\epsilon$.

a.
Prove that if $E$ is measurable then for all $\epsilon>0$ there exists an elementary $\operatorname{set} F$, such that $m(E \Delta F)<\epsilon$. 

  Here $m(E)$ denotes the Lebesgue measure of $E$, a set $F$ is called elementary if it is a finite union of rectangles and $E \Delta F$ denotes the symmetric difference of the sets $E$ and $F$.

b.
Let $E \subset \mathbb{R}$ be a measurable set, such that $0<m(E)<\infty$. Use part (a) to show that
\[
\lim _{n \rightarrow \infty} \int_{E} \sin (n t) d t=0
\]
:::
::: {.solution}
<1>1. (a) If $E$ is measurable then for every $\eps > 0$ there is an elementary set $F$ (finite union of rectangles) with $m(E \Delta F) < \eps$.
    <2>1. By measurability, choose open $U \supseteq E$ with $m(U \setminus E) < \eps/2$.
        ::: {.proof}
        the definition of measurability given in the card (the definition uses $m^*$ and open approximation; also $m(U \setminus E) = m^*(U\setminus E)$ for measurable $E$).
        :::
    <2>2. $U$ is a countable union of almost disjoint cubes/rectangles $Q_j$: $U = \bigcup_j Q_j$ with $m(U) = \sum_j m(Q_j)$.
        ::: {.proof}
        dyadic-cube decomposition of an open set; or cover by intervals and refine.
        :::
    <2>3. Choose $N$ with $\sum_{j > N} m(Q_j) < \eps/2$. (If $m(U) = \infty$, first replace $U$ by $U_R = U \cap B(0,R)$ with $m(U_R \setminus E) < \eps/2$ — possible by continuity of measure — and work with $U_R$, which has finite measure.)
        ::: {.proof}
        tails of a convergent series; the truncation handles infinite measure.
        :::
    <2>4. $F = \bigcup_{j \le N} Q_j$ is elementary and $m(E \Delta F) < \eps$.
        ::: {.proof}
        $E \setminus F \subseteq U \setminus F = \bigcup_{j > N}Q_j$ (as $E \subseteq U$) and $F \setminus E \subseteq U \setminus E$; hence $m(E\Delta F) \le m(U\setminus F) + m(U\setminus E) < \eps/2 + \eps/2 = \eps$.
        :::

<1>2. (b) For measurable $E$ with $0 < m(E) < \infty$: $\lim_n \int_E \sin(nt)\,dt = 0$.
    <2>1. For an interval $I = [a,b]$: $\left|\int_I \sin(nt)\,dt\right| = \left|\frac{\cos(na) - \cos(nb)}{n}\right| \le \frac{2}{n} \to 0$.
        ::: {.proof}
        compute the integral.
        :::
    <2>2. For an elementary set $F = \bigcup_i I_i$ (disjoint intervals): $\left|\int_F \sin(nt)\right| \le \sum_i \frac{2}{n} \to 0$.
        ::: {.proof}
        <2>1 summed over finitely many intervals.
        :::
    <2>3. Given $\eps > 0$, by (a) choose elementary $F$ with $m(E \Delta F) < \eps/(2\cdot 1)$: then $\left|\int_E \sin(nt) - \int_F \sin(nt)\right| \le \int_{E \Delta F}|\sin(nt)| \le m(E \Delta F) < \eps/2$.
        ::: {.proof}
        $|\sin| \le 1$; the integrals differ only on $E \Delta F$.
        :::
    <2>4. Q.E.D.
        ::: {.proof}
        $\limsup_n |\int_E \sin(nt)| \le \limsup_n |\int_F \sin(nt)| + \eps/2 = \eps/2$; $\eps$ arbitrary.
        :::

<1>3. Q.E.D.
    ::: {.proof}
    <1>1 and <1>2 establish (a) and (b).
    :::
:::
