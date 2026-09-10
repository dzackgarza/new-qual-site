---
schema: qual/card@1
id: E-HAT-3.B-1
kind: problem
title: "Homology and cohomology of $\\mathbb{RP}^m \\times \\mathbb{RP}^n$"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.B, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Compute the groups $H_i(\mathbb{RP}^m \times \mathbb{RP}^n; G)$ and $H^i(\mathbb{RP}^m \times \mathbb{RP}^n; G)$ for $G = \mathbb{Z}$ and $\mathbb{Z}_2$ via the cellular chain and cochain complexes.
[See Example 3B.4.]

::: {.solution}
Give $\mathbb{RP}^r$ its standard CW structure with one cell $e_j$ in each dimension $0\le j\le r$. Its cellular chain complex over $\mathbb Z$ has
\[
\partial e_j=\begin{cases}
0,&j\text{ odd},\\
2e_{j-1},&j\text{ even}.
\end{cases}
\]
The product CW structure on $\mathbb{RP}^m\times\mathbb{RP}^n$ has one cell $e_p\times e_q$ for each $0\le p\le m$, $0\le q\le n$, and its cellular chain complex is the tensor product of the two cellular complexes, with
\[
\partial(e_p\otimes e_q)
=(\partial e_p)\otimes e_q+(-1)^p e_p\otimes(\partial e_q).
\]

For a compact notation define
\[
F_r=\{0\}\cup\bigl(\{r\}\text{ if $r$ is odd}\bigr),
\qquad
T_r=\{j:1\le j<r,\ j\text{ odd}\}.
\]
Thus the integral homology of $\mathbb{RP}^r$ is $\mathbb Z$ in degrees in $F_r$, $\mathbb Z_2$ in degrees in $T_r$, and zero otherwise.

The cellular tensor complex gives the integral Künneth decomposition
\[
H_i(\mathbb{RP}^m\times\mathbb{RP}^n;\mathbb Z)
\cong
\bigoplus_{p+q=i}H_p(\mathbb{RP}^m)\otimes H_q(\mathbb{RP}^n)
\oplus
\bigoplus_{p+q=i-1}\operatorname{Tor}(H_p(\mathbb{RP}^m),H_q(\mathbb{RP}^n)).
\]
Since the only torsion is $\mathbb Z_2$, this may be written explicitly as
\[
H_i\cong \mathbb Z^{f_i}\oplus(\mathbb Z_2)^{t_i},
\]
where
\[
f_i=\#\{(p,q)\in F_m\times F_n:p+q=i\},
\]
and
\[
\begin{aligned}
t_i={}&\#\{(p,q):p+q=i,\ (p,q)\in
(T_m\times F_n)\cup(F_m\times T_n)\cup(T_m\times T_n)\}\\
&+\#\{(p,q)\in T_m\times T_n:p+q+1=i\}.
\end{aligned}
\]
This is the complete integral homology calculation.

The integral cohomology follows from the universal coefficient theorem. Since $\operatorname{Hom}(\mathbb Z_2,\mathbb Z)=0$ and $\operatorname{Ext}(\mathbb Z_2,\mathbb Z)\cong\mathbb Z_2$,
\[
\boxed{H^i(\mathbb{RP}^m\times\mathbb{RP}^n;\mathbb Z)
\cong \mathbb Z^{f_i}\oplus(\mathbb Z_2)^{t_{i-1}}.}
\]

With $\mathbb Z_2$ coefficients every cellular differential is zero, since each nonzero integral differential is multiplication by $2$. Hence both cellular homology and cellular cohomology have one $\mathbb Z_2$ basis vector for each product cell of total dimension $i$. Therefore
\[
\boxed{H_i(-;\mathbb Z_2)\cong H^i(-;\mathbb Z_2)
\cong(\mathbb Z_2)^{N_i},}
\]
where
\[
N_i=\#\{(p,q):0\le p\le m,\ 0\le q\le n,\ p+q=i\}.
\]
Equivalently,
\[
N_i=\max\bigl(0,\min(m,i)-\max(0,i-n)+1\bigr).
\]
:::
