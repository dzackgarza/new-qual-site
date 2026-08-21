---
schema: qual/card@1
id: P-FS6II
kind: problem
title: Tonelli's theorem and the layer-cake representation of a nonnegative measurable
  function
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Measure Theory
  - Integrals
relations: []
review: draft
solved: true
---

::: problem
a.
Carefully state Tonelli's theorem for a nonnegative function $F(x, t)$ on $\RR^n\cross \RR$.

b.
  Let $f:\RR^n\to [0, \infty]$ and define
\[
\mca \definedas \theset{(x, t) \in \RR^n\cross \RR \suchthat 0\leq t \leq f(x)}
.\]

  Prove the validity of the following two statements:

  1. $f$ is Lebesgue measurable on $\RR^{n} \iff \mca$ is a Lebesgue measurable subset of $\RR^{n+1}$.
  2. If $f$ is Lebesgue measurable on $\RR^n$ then
  \[
  m(\mathcal{A})=\int_{\mathbb{R}^{n}} f(x) d x=\int_{0}^{\infty} m\left(\left\{x \in \mathbb{R}^{n}\suchthat f(x) \geq t\right\}\right) d t
  .\]
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. (a) Tonelli's theorem (nonnegative case): let $F \ge 0$ be measurable on $\RR^n \times \RR$ (product of Lebesgue $\sigma$-algebras). Then $x \mapsto \int_\RR F(x, t)\,dt$ is measurable, $t \mapsto \int_{\RR^n} F(x, t)\,dx$ is measurable, and
    $$\int_{\RR^n \times \RR} F(x, t)\,d(x, t) = \int_{\RR^n}\left(\int_\RR F(x, t)\,dt\right)dx = \int_\RR\left(\int_{\RR^n} F(x, t)\,dx\right)dt,$$
    all possibly infinite.
    Proof: Tonelli: the iterated integrals equal the product integral for nonnegative measurable functions (no integrability or $\sigma$-finiteness issue beyond Lebesgue measure on $\RR^n \times \RR$).

<1>2. (b)1. For $\mca = \theset{(x, t) \in \RR^n \cross \RR \suchthat 0 \le t \le f(x)}$ (with $f \ge 0$): $f$ measurable $\iff$ $\mca$ measurable.
    <2>1. ($\Rightarrow$) $f$ measurable $\Rightarrow$ $\mca$ measurable.
        Proof: $\mca = \theset{(x,t) : t \ge 0} \cap \theset{(x,t) : f(x) - t \ge 0}$; the map $(x, t) \mapsto f(x) - t$ is measurable (composition of the measurable $f \circ \pi_x$ and subtraction), so $\mca$ is the intersection of two measurable sets.
    <2>2. ($\Leftarrow$) $\mca$ measurable $\Rightarrow$ $f$ measurable.
        Proof: the vertical section $\mca_x = \{t : (x, t) \in \mca\}$ is $[0, f(x)]$, so $f(x) = \sup\{t : (x, t) \in \mca\}$. For each $a$, $\{x : f(x) > a\} = \{x : \mca_x \cap (a, \infty) \ne \varnothing\} = \pi_x\big(\mca \cap \{(x, t) : t > a\}\big)$, the projection of a measurable set, which is measurable (projections of Borel sets in $\RR^{n+1}$ are analytic, hence Lebesgue measurable; on a complete space the projection of a measurable set is measurable).

<1>3. (b)2. Layer-cake: for measurable $f \ge 0$, $m(\mathcal A) = \int_{\RR^n} f(x)\,dx = \int_0^\infty m\{x : f(x) \ge t\}\,dt$.
    <2>1. $\chi_{\mca}(x, t) = \chi_{\{0 \le t \le f(x)\}}(x, t)$; for each fixed $x$, $\int_\RR \chi_{\mca}(x, t)\,dt = f(x)$ (length of $[0, f(x)]$).
        Proof: definition of $\mca$ and one-dimensional integration.
    <2>2. $m(\mathcal A) = \int_{\RR^{n+1}}\chi_{\mca} = \int_{\RR^n}\int_\RR \chi_{\mca}(x,t)\,dt\,dx = \int_{\RR^n} f(x)\,dx$.
        Proof: Tonelli (<1>1) applied to $F = \chi_\mca$.
    <2>3. For each fixed $t$, $\int_{\RR^n}\chi_{\mca}(x, t)\,dx = m\{x : f(x) \ge t\}$.
        Proof: $\chi_{\mca}(x, t) = \chi_{\{x : t \le f(x)\}}(x)$ for $t \ge 0$.
    <2>4. $m(\mathcal A) = \int_0^\infty m\{x : f(x) \ge t\}\,dt$.
        Proof: Tonelli applied the other way: $m(\mca) = \int_\RR \int_{\RR^n}\chi_\mca\,dx\,dt = \int_{-\infty}^0 m(\RR^n)\,dt + \int_0^\infty m\{f \ge t\}\,dt$ — the first term is infinite unless handled by noting $\chi_\mca(x,t) = 0$ for $t < 0$ (as $\mca$ requires $t \ge 0$), so it equals $\int_0^\infty m\{f \ge t\}\,dt$.

<1>4. Q.E.D.
    Proof: <1>2 and <1>3 establish (b)1 and (b)2.
:::
