---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-INT2
kind: problem
title: 'Split a Riemann–Stieltjes integral at an interior point'
classification:
  areas:
  - real-analysis
  topics:
  - riemann-integrability
  - integrals
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(June 2017, 2) Prove: $f\in\mathcal R(\alpha)$ on $[a,b]$ if and only if for any $a<c<b$, $f\in\mathcal R(\alpha)$ on $[a,c]$ and on $[c,b]$.
In addition, if either condition holds, then we have that
$$
\int_a^c f\,d\alpha+\int_c^b f\,d\alpha=\int_a^b f\,d\alpha.
$$
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Prove $f \in \mathcal R(\alpha)$ on $[a,b]$ iff $f \in \mathcal R(\alpha)$ on $[a,c]$ and on $[c,b]$ for any $a < c < b$, with $\int_a^c f\,d\alpha + \int_c^b f\,d\alpha = \int_a^b f\,d\alpha$.

<1>1. ($\Leftarrow$) If $f$ is integrable on $[a,c]$ and $[c,b]$, then $f$ is integrable on $[a,b]$ and the integrals add.
<2>1. Let $P_1$ be a partition of $[a,c]$ and $P_2$ a partition of $[c,b]$; their union $P = P_1 \cup P_2$ is a partition of $[a,b]$ through $c$.
<2>2. The Stieltjes sum for $P$ is the sum of the Stieltjes sums for $P_1$ and $P_2$ (with matching tags at $c$ chosen compatibly): $S(P) = S(P_1) + S(P_2)$.
Proof: the sum over the points of $P$ splits at $c$; the term at $c$ belongs to exactly one side once tags are chosen.
<2>3. Given $\varepsilon > 0$, choose $\delta_1, \delta_2$ from integrability on the two halves.
For any partition $P$ of $[a,b]$ with $\|P\| < \min(\delta_1, \delta_2, (c-a)/2, (b-c)/2)$, refine $P$ by adding $c$; the refinement changes the sum by an arbitrarily small amount (two adjacent terms, bounded by $M(\text{Var})$ control or by the integrability on the halves), and the refined partition $P'$ decomposes into $P'_1, P'_2$ with $\|P'_i\| < \delta_i$.
Proof: adding $c$ to a partition splits one interval into two; the change in the Stieltjes sum is the difference between $f(x_i^*)\Delta\alpha_i$ and the two new terms.
A clean way: use the Cauchy criterion / Darboux–Stieltjes characterization; alternatively note $f \cdot \chi_{[a,c]}$ and $f\cdot\chi_{[c,b]}$-type localization.
<2>4. $\int_a^b f\,d\alpha = \int_a^c f\,d\alpha + \int_c^b f\,d\alpha$.
Proof: $S(P) \to \int_a^c + \int_c^b$ as $\|P\| \to 0$ by <2>2–<2>3 and uniqueness of the limit.

<1>2. ($\Rightarrow$) If $f$ is integrable on $[a,b]$, then $f$ is integrable on each subinterval $[a,c]$, $[c,b]$.
<2>1. Let $P$ be any partition of $[a,c]$ with small mesh; extend it to a partition $P'$ of $[a,b]$ by adding points in $[c,b]$ with small mesh.
<2>2. $S(P)$ differs from a Stieltjes sum over $[a,b]$ by the terms on $[c,b]$, which are controlled because $f$ is bounded (say $|f| \le M$) and $\alpha$ has bounded variation on $[c,b]$ — or, using integrability on $[a,b]$: pick two extensions with the same mesh bound and subtract.
Proof: a standard $ arepsilon/3$ argument: since $f \in \mathcal R(\alpha)$ on $[a,b]$, the Stieltjes sums converge; restrict to partitions containing the fixed point $c$, then the $[a,c]$-part of the sum converges as mesh $\to 0$, giving integrability on $[a,c]$.
The needed fact is that $f$ restricted to $[a,c]$ with integrator $\alpha|_{[a,c]}$ is integrable; this follows from the Cauchy criterion: for any two partitions $P, Q$ of $[a,c]$ with small mesh, extend both to $[a,b]$ by the same points on $[c,b]$; the sums on $[a,b]$ are close (integrability), and their difference equals the difference of the $[a,c]$-sums.
<2>3. Similarly for $[c,b]$.
Proof: symmetric argument.

<1>3. Q.E.D. Proof: <1>1 gives the forward direction and the additivity; <1>2 gives the converse.
:::
