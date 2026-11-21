---
schema: qual/card@1
id: T-CJCKL
kind: theorem
title: Rouché's theorem
slogan: 'If $\abs{m}<\abs{M}$ on $\gamma$, then $M\circ\gamma$ and $(M+m)\circ\gamma$ have the same winding number about $0$, so $M$ and $M+m$ have the same number of zeros minus poles inside $\gamma$.'
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Winding Number
  - Meromorphic Functions
relations: []
review: draft
---

::: {.theorem ref="Rouche"}
Let $\Omega\subseteq\CC$ be open, let $M$ and $m$ be [[D-7DFVJ|meromorphic]] on $\Omega$, and let $\gamma$ be a piecewise smooth [[D-YKB3V|toy contour]] in $\Omega$ whose interior $\Omega_\gamma$ satisfies $\overline{\Omega_\gamma}\subseteq\Omega$.
Assume that $M$ and $m$ have no poles on $\gamma$ and that
$$
\abs{m(z)}<\abs{M(z)}\quad\text{for all } z\in\gamma.
$$
For a meromorphic function $h$, write $Z_h$ and $P_h$ for the numbers of [[D-65VIK|zeros]] and [[D-AUD6K|poles]] of $h$ in $\Omega_\gamma$, counted with multiplicity.
Then the [[D-PJ7JM|winding numbers]] of $M\circ\gamma$ and $(M+m)\circ\gamma$ about $0$ agree, and
$$
Z_M-P_M=Z_{M+m}-P_{M+m}.
$$
In particular, if $M$ and $m$ are [[D-E7A5W|holomorphic]] on $\Omega$, then $M$ and $M+m$ have the same number of zeros in $\Omega_\gamma$.
:::

::: {.remark title="From the circle to a toy contour"}
For a circle $C$ and holomorphic $f,g$ with $\abs{f}>\abs{g}$ on $C$, this is [@SS03, Theorem 4.3].
The toy-contour form follows by applying [[T-JXDQT|the argument principle]] to $M_t\coloneqq M+tm$: the hypothesis $\abs{m}<\abs{M}$ on $\gamma$ makes every $M_t$ nonvanishing on $\gamma$, so $Z_{M_t}-P_{M_t}$ depends continuously on $t\in[0,1]$ and is integer valued, hence constant.
:::

::: {.proposition}
Let $f,g,M,m$ be holomorphic on a neighbourhood of the closed region bounded by $\gamma$, and write $Z_h$ for the number of zeros of $h$ inside $\gamma$. Each of the following is an instance of the theorem above, with the decomposition named:

(i) if $f = M+m$ and $\abs{m}<\abs{M}$ on $\gamma$, then $Z_f = Z_M$;

(ii) under the same hypothesis each of $\pm(M\pm m)$ has $Z_M$ zeros, since $\abs{\pm m}<\abs{M}$ and a function has the zeros of its negative;

(iii) if $\abs{f-g}<\abs{f}$ on $\gamma$, then $Z_f = Z_g$, the decomposition being $M = f$, $m = g-f$;

(iv) if $\abs{f-g}<1$ on $\gamma$ and $\abs f\ge1$ or $\abs g\ge1$ there, then $Z_f = Z_g$, which is (iii) after replacing the larger of $\abs f,\abs g$ by the bound $1$;

(v) if $\abs f\ge L$ and $\abs{f-f_n}\le U$ on $\gamma$ with $U<L$, then $Z_f = Z_{f_n}$, which is (iii) with $g = f_n$.
:::
