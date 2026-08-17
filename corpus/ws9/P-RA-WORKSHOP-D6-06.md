---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-06
kind: problem
title: 'A bounded function with finitely many discontinuities is Riemann integrable'
classification:
  areas:
  - real-analysis
  topics:
  - riemann-integrability
  - continuity
relations: []
review: draft
---

::: {.problem title="?"}
(June 2005 #1b) Use the definition of the Riemann integral to prove that if $f$ is bounded on $[a,b]$ and is continuous everywhere except for finitely many points in $(a,b)$, then $f\in\mathcal R$ on $[a,b]$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Set up: let the discontinuities be $d_1, \ldots, d_m \in (a,b)$ and let $|f| \le M$.
    Proof: $f$ is bounded, say $|f(x)| \le M$ for all $x \in [a,b]$ (the endpoints are continuous by hypothesis).
<1>2. Cover the bad points by small intervals.
    Proof: fix $\epsilon > 0$. Cover each $d_j$ by an open interval $I_j$ of length $< \epsilon/(4mM)$ (with $I_j$ inside $(a,b)$, small enough not to reach the endpoints). The complement $K = [a,b] \setminus \bigcup_j I_j$ is a finite union of closed intervals on which $f$ is continuous, hence uniformly continuous.
<1>3. Control the oscillation on the good set.
    Proof: by uniform continuity of $f$ on $K$, there is $\delta > 0$ such that $|f(u) - f(v)| < \epsilon/(2(b-a))$ whenever $u, v \in K$ with $|u - v| < \delta$. Take a partition $P$ of $[a,b]$ refining both the $I_j$-boundaries and with mesh $< \delta$.
<1>4. Bound $U(P) - L(P)$.
    Proof: take a partition $P$ of $[a,b]$ containing the endpoints of each $I_j$ and with mesh $< \delta$ (so each $I_j$ is a union of subintervals of $P$). Subintervals lying entirely in $K$ have oscillation $< \epsilon/(2(b-a))$, contributing total $< \frac{\epsilon}{2(b-a)}(b-a) = \epsilon/2$. The subintervals inside the $I_j$'s have total length $\sum_j |I_j| < m\cdot\frac{\epsilon}{4mM} = \frac{\epsilon}{4M}$ and oscillation $\le 2M$ each, contributing $< 2M\cdot\frac{\epsilon}{4M} = \epsilon/2$. Hence $U(P) - L(P) < \epsilon$ (taking the mesh small enough that the $\delta$-condition on $K$ holds).
<1>5. Conclude.
    Proof: for every $\epsilon > 0$ there is a partition with $U(P) - L(P) < \epsilon$, so by the Riemann criterion $f \in \mathcal{R}$ on $[a,b]$.
<1>6. Q.E.D.
:::
