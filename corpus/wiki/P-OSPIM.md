---
schema: qual/card@1
id: P-OSPIM
kind: problem
title: Measurability of $\inf_k f_k$ and $\sup_k f_k$, Fatou's lemma, and the monotone
  convergence theorem from Fatou
classification:
  areas:
  - real-analysis
  topics:
  - Fatou
  - Measure Theory
  - Convergence of Integrals
relations: []
review: draft
solved: true
---

::: problem
a. See \cref{equivalence_of_approximating_measures}

b. Let $f_k$ be a sequence of extended real-valued Lebesgue measurable function.

    i. Prove that $\inf_k f_k, \sup_k f_k$ are both Lebesgue measurable function.
    
        *Hint: argue that*
\[
\ts{x \st \inf_k f_k(x) < a} = \Union_k \ts{x \st f_k(x) < a}
.\]

    ii. Carefully state Fatou's Lemma and deduce the Monotone Converge Theorem from it.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. (b)i. For a sequence of extended-real measurable $f_k$: $\inf_k f_k$ and $\sup_k f_k$ are measurable.
    <2>1. $\sup_k f_k$ is measurable: for every $a$, $\{x : \sup_k f_k(x) \le a\} = \bigcap_k\{x : f_k(x) \le a\}$.
        Proof: $\sup_k f_k \le a$ iff $f_k \le a$ for every $k$; countable intersections of measurable sets are measurable.
    <2>2. $\inf_k f_k$ is measurable: for every $a$, $\{x : \inf_k f_k(x) < a\} = \bigcup_k\{x : f_k(x) < a\}$.
        Proof: the hint; $\inf_k f_k < a$ iff some $f_k < a$; countable unions of measurable sets are measurable.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2 (using the sublevel/superlevel-set characterization of measurability).

<1>2. (b)ii. Fatou's lemma: for measurable $f_n \ge 0$, $\int \liminf_n f_n \le \liminf_n \int f_n$.
    Proof: statement.

<1>3. Deduce MCT from Fatou: if $0 \le f_1 \le f_2 \le \cdots$ and $f_n \uparrow f$ pointwise, then $\int f_n \uparrow \int f$.
    <2>1. $\int f \ge \lim_n \int f_n$: by monotone convergence in the classical sense — but we must derive it from Fatou: $\int f = \int \liminf_n f_n \le \liminf_n \int f_n = \lim_n \int f_n$ (the last equality since $\int f_n$ is nondecreasing).
        Proof: Fatou applied to the nonnegative $f_n$; $\liminf = \lim$ for monotone sequences.
    <2>2. $\int f \le \lim_n \int f_n$: for each $m$, $f_m \le f$, so $\int f_m \le \int f$; hence $\lim_m \int f_m \le \int f$.
        Proof: monotonicity of the integral.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2 give $\lim_n \int f_n = \int f$; and $\int f_n \le \int f$ shows the convergence is monotone from below.

<1>4. Q.E.D.
    Proof: <1>1, <1>2, <1>3 settle (i) and (ii).
:::
