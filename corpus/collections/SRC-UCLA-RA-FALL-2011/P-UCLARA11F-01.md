---
schema: qual/card@1
id: P-UCLARA11F-01
kind: problem
title: Egorov theorem on almost-uniform convergence
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $(f_n)$ be measurable functions on $[0,1]$ converging almost everywhere to a measurable function $f$.
Prove that for every $\varepsilon>0$ there exists a measurable set $E\subseteq[0,1]$ with $\lambda(E)<\varepsilon$ such that $f_n\to f$ uniformly on $[0,1]\setminus E$.
:::

::: {.solution}
Fix
\[
\varepsilon>0.
\]

For each integer \(m\ge1\) and \(N\ge1\), define
\[
\boxed{
A_{m,N}
=
\bigcup_{n\ge N}
\left\{
x\in[0,1]:
|f_n(x)-f(x)|\ge\frac1m
\right\}.}
\]

<1>1. Each set \(A_{m,N}\) is measurable.

::: {.proof}
The functions \(f_n\) and \(f\) are measurable, so
\[
|f_n-f|
\]
is measurable. Hence each set
\[
\left\{|f_n-f|\ge\frac1m\right\}
\]
is measurable, and a countable union of measurable sets is measurable.
:::

<1>2. For fixed \(m\), the sets \(A_{m,N}\) decrease with \(N\):
\[
\boxed{
A_{m,N+1}\subseteq A_{m,N}}.
\]

::: {.proof}
The union defining \(A_{m,N+1}\) runs over the smaller index set
\[
\{n\ge N+1\}\subseteq\{n\ge N\}.
\]
:::

<1>3. For fixed \(m\),
\[
\bigcap_{N=1}^{\infty}A_{m,N}
\]
is contained in the set where \(f_n\) fails to converge to \(f\).

::: {.proof}
If
\[
x\in\bigcap_N A_{m,N},
\]
then for every \(N\) there exists \(n\ge N\) such that
\[
|f_n(x)-f(x)|\ge\frac1m.
\]
Thus the difference does not eventually stay below \(1/m\), so \(f_n(x)\not\to f(x)\).
:::

<1>4. Hence
\[
\boxed{
\lambda\left(
\bigcap_{N=1}^{\infty}A_{m,N}
\right)=0}.
\]

::: {.proof}
The sequence converges to \(f\) almost everywhere, so the failure set has Lebesgue measure zero. Apply step <1>3.
:::

<1>5. Because
\[
A_{m,1}\subseteq[0,1],
\]
one has
\[
\lambda(A_{m,1})\le1<\infty.
\]

::: {.proof}
Lebesgue measure of \([0,1]\) is \(1\).
:::

<1>6. By continuity from above of measure,
\[
\boxed{
\lambda(A_{m,N})\longrightarrow0
\qquad(N\to\infty)}
\]
for every fixed \(m\).

::: {.proof}
The sets decrease by step <1>2, the first has finite measure by step <1>5, and their intersection has measure zero by step <1>4.
:::

<1>7. For each \(m\ge1\), choose \(N_m\) such that
\[
\boxed{
\lambda(A_{m,N_m})
<
\frac{\varepsilon}{2^m}}.
\]

::: {.proof}
This is possible by step <1>6.
:::

<1>8. Define
\[
\boxed{
E
=
\bigcup_{m=1}^{\infty}
A_{m,N_m}}.
\]

::: {.proof}
This is a countable union of measurable sets, hence measurable.
:::

<1>9. The exceptional set satisfies
\[
\boxed{
\lambda(E)<\varepsilon}.
\]

::: {.proof}
By countable subadditivity and step <1>7,
\[
\lambda(E)
\le
\sum_{m=1}^{\infty}
\lambda(A_{m,N_m})
<
\sum_{m=1}^{\infty}
\frac{\varepsilon}{2^m}
=
\varepsilon.
\]
:::

Let
\[
F=[0,1]\setminus E.
\]

<1>10. For every \(m\ge1\), every \(x\in F\), and every \(n\ge N_m\),
\[
\boxed{
|f_n(x)-f(x)|<\frac1m}.
\]

::: {.proof}
Since
\[
x\notin E,
\]
one has
\[
x\notin A_{m,N_m}.
\]
By definition of \(A_{m,N_m}\), this means there is no \(n\ge N_m\) for which
\[
|f_n(x)-f(x)|\ge\frac1m.
\]
:::

<1>11. Let
\[
\delta>0.
\]
Choose \(m\) so large that
\[
\frac1m<\delta.
\]

::: {.proof}
The sequence \(1/m\) tends to \(0\).
:::

<1>12. Then for every
\[
n\ge N_m
\]
and every
\[
x\in F,
\]
\[
\boxed{
|f_n(x)-f(x)|<\delta}.
\]

::: {.proof}
By step <1>10,
\[
|f_n(x)-f(x)|<\frac1m<\delta.
\]
:::

<1>13. Therefore
\[
\boxed{
f_n\to f
\text{ uniformly on }
[0,1]\setminus E}.
\]

::: {.proof}
Step <1>12 is exactly the definition of uniform convergence on \(F\): for the given \(\delta>0\), the single index \(N_m\) works simultaneously for every \(x\in F\).
:::

<1>14. Thus for every \(\varepsilon>0\), there exists a measurable set \(E\subseteq[0,1]\) with
\[
\boxed{\lambda(E)<\varepsilon}
\]
such that \(f_n\to f\) uniformly on
\[
\boxed{[0,1]\setminus E}.
\]

::: {.proof}
The measure estimate is step <1>9 and uniform convergence is step <1>13.
:::

<1>15. Q.E.D.

::: {.proof}
Step <1>14 is the required conclusion.
:::
:::
