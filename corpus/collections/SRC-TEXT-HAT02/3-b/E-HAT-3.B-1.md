---
schema: qual/card@1
id: E-HAT-3.B-1
kind: problem
title: "Homology and cohomology of $\\RP^m \\times \\RP^n$"
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

::: {.problem}
Compute the groups $H_i(\RP^m \times \RP^n; G)$ and $H^i(\RP^m \times \RP^n; G)$ for $G = \ZZ$ and $\ZZ_2$ via the cellular chain and cochain complexes.
[See Example 3B.4.]
:::

::: {.solution}
Give $\RP^r$ its standard CW structure with one cell $e_j$ in each dimension $0\le j\le r$. Its cellular chain complex over $\ZZ$ has
$$
\partial e_j=\begin{cases}
0,&j\text{ odd},\\
2e_{j-1},&j\text{ even}.
\end{cases}
$$
The product CW structure on $\RP^m\times\RP^n$ has one cell $e_p\times e_q$ for each $0\le p\le m$, $0\le q\le n$, and its cellular chain complex is the tensor product of the two cellular complexes, with
$$
\partial(e_p\otimes e_q)
=(\partial e_p)\otimes e_q+(-1)^p e_p\otimes(\partial e_q).
$$

For a compact notation define
$$
F_r=\{0\}\cup\bigl(\{r\}\text{ if } r \text{ is odd}\bigr),
\qquad
T_r=\{j:1\le j<r,\ j\text{ odd}\}.
$$
Thus the integral homology of $\RP^r$ is $\ZZ$ in degrees in $F_r$, $\ZZ_2$ in degrees in $T_r$, and zero otherwise.

The cellular tensor complex gives the integral Künneth decomposition
$$
H_i(\RP^m\times\RP^n;\ZZ)
\cong
\bigoplus_{p+q=i}H_p(\RP^m)\otimes H_q(\RP^n)
\oplus
\bigoplus_{p+q=i-1}\operatorname{Tor}(H_p(\RP^m),H_q(\RP^n)).
$$
Since the only torsion is $\ZZ_2$, this may be written explicitly as
$$
H_i\cong \ZZ^{f_i}\oplus(\ZZ_2)^{t_i},
$$
where
$$
f_i=\#\{(p,q)\in F_m\times F_n:p+q=i\},
$$
and
$$
\begin{aligned}
t_i={}&\#\{(p,q):p+q=i,\ (p,q)\in
(T_m\times F_n)\cup(F_m\times T_n)\cup(T_m\times T_n)\}\\
&+\#\{(p,q)\in T_m\times T_n:p+q+1=i\}.
\end{aligned}
$$
This is the complete integral homology calculation.

The integral cohomology follows from the universal coefficient theorem. Since $\operatorname{Hom}(\ZZ_2,\ZZ)=0$ and $\operatorname{Ext}(\ZZ_2,\ZZ)\cong\ZZ_2$,
$$
\boxed{H^i(\RP^m\times\RP^n;\ZZ)
\cong \ZZ^{f_i}\oplus(\ZZ_2)^{t_{i-1}}.}
$$

With $\ZZ_2$ coefficients every cellular differential is zero, since each nonzero integral differential is multiplication by $2$. Hence both cellular homology and cellular cohomology have one $\ZZ_2$ basis vector for each product cell of total dimension $i$. Therefore
$$
\boxed{H_i(-;\ZZ_2)\cong H^i(-;\ZZ_2)
\cong(\ZZ_2)^{N_i},}
$$
where
$$
N_i=\#\{(p,q):0\le p\le m,\ 0\le q\le n,\ p+q=i\}.
$$
Equivalently,
$$
N_i=\max\bigl(0,\min(m,i)-\max(0,i-n)+1\bigr).
$$
:::
