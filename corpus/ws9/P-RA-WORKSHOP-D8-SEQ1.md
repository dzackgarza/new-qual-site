---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-SEQ1
kind: problem
title: Radii of convergence for sums and coefficientwise products of power series
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
relations: []
review: draft
---

::: {.problem title="?"}
(January 2006, 1) Let the power series series $\sum_{n=0}^{\infty}a_nx^n$ and $\sum_{n=0}^{\infty}b_nx^n$ have radii of convergence $R_1$ and $R_2$, respectively.

(a) If $R_1\ne R_2$, prove that the radius of convergence, $R$, of the power series $\sum_{n=0}^{\infty}(a_n+b_n)x^n$ is $\min\{R_1,R_2\}$.
What can be said about $R$ when $R_1=R_2$?

(b) Prove that the radius of convergence, $R$, of $\sum_{n=0}^{\infty}a_nb_nx^n$ satisfies $R\ge R_1R_2$.
Show by means of an example that this inequality can be strict.
:::

::: remark
The source page literally says “the power series series” in its opening sentence; that wording is preserved here.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** (a) If $\sum a_nx^n$ and $\sum b_nx^n$ have radii $R_1, R_2$ with $R_1 \neq R_2$, show $\sum(a_n+b_n)x^n$ has radius $\min\{R_1, R_2\}$; discuss $R_1 = R_2$.
> (b) Show $\sum a_nb_nx^n$ has radius $R \ge R_1R_2$, with a strict example.

<1>1. (a) $R_1 \neq R_2$: the radius of $\sum(a_n+b_n)x^n$ is $\min\{R_1, R_2\}$.
<2>1. Say $R_1 < R_2$.
For $|x| < R_1$, both series converge absolutely, so their sum converges absolutely: the radius $R$ of the sum satisfies $R \ge R_1$.
<2>2. For $R_1 < |x| < R_2$: $\sum(a_n+b_n)x^n$ diverges.
Proof: if it converged, then $\sum a_nx^n = \sum(a_n+b_n)x^n - \sum b_nx^n$ would converge (difference of two convergent series, since $\sum b_nx^n$ converges for $|x| < R_2$), contradicting the divergence of $\sum a_nx^n$ for $|x| > R_1$.
<2>3. $R = R_1 = \min\{R_1, R_2\}$.
Proof: <2>1 gives $R \ge R_1$ and <2>2 gives $R \le R_1$.
<2>4. If $R_1 = R_2 = R_0$, then $R \ge R_0$, and $R$ can be strictly larger.
Proof: $R \ge R_0$ since both series converge absolutely for $|x| < R_0$.
Strictness: $a_n = 1$, $b_n = -1$ gives $a_n + b_n = 0$, radius $\infty$; or $a_n = 1$, $b_n = -1 + 2^{-n}$ gives $a_n + b_n = 2^{-n}$, radius $2 > 1 = R_0$.
Nothing more can be said in general.
<2>5. Q.E.D. Proof: <2>3 and <2>4 answer (a).

<1>2. (b) The radius $R$ of $\sum a_nb_nx^n$ satisfies $R \ge R_1R_2$.
<2>1. Fix $|x| < R_1R_2$; choose $r_1 < R_1$, $r_2 < R_2$ with $|x| < r_1r_2$.
Proof: e.g. take $r_1, r_2$ close to $R_1, R_2$ with $r_1r_2 > |x|$, possible since $R_1R_2 > |x|$.
<2>2. $|a_n|r_1^n \to 0$ and $|b_n|r_2^n \to 0$.
Proof: $\sum a_nr_1^n$ and $\sum b_nr_2^n$ converge absolutely (inside the radius of convergence), so their terms tend to $0$; in particular they are bounded: $|a_n|r_1^n \le C_1$, $|b_n|r_2^n \le C_2$.
<2>3. $|a_nb_n||x|^n = (|a_n|r_1^n)(|b_n|r_2^n)\left(\frac{|x|}{r_1r_2}\right)^n \le C\rho^n$ with $\rho := |x|/(r_1r_2) < 1$.
Proof: <2>2 and $|x| < r_1r_2$.
<2>4. $\sum a_nb_nx^n$ converges absolutely for $|x| < R_1R_2$, so $R \ge R_1R_2$.
Proof: comparison with the convergent geometric series $\sum C\rho^n$ by <2>3. <2>5. Strictness example: $a_{2k} = 1$, $a_{2k+1} = 0$ and $b_{2k} = 0$, $b_{2k+1} = 1$.
Proof: $\sum a_nx^n = \sum_k x^{2k}$ has radius $R_1 = 1$ and $\sum b_nx^n = \sum_k x^{2k+1}$ has radius $R_2 = 1$; but $a_nb_n = 0$ for all $n$, so $\sum a_nb_nx^n = 0$ converges everywhere: $R = \infty > 1 = R_1R_2$.
<2>6. Q.E.D. Proof: <2>4 gives $R \ge R_1R_2$; <2>5 exhibits strictness.
:::
