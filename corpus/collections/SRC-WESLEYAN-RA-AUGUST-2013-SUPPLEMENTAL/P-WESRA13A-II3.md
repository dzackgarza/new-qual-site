---
schema: qual/card@1
id: P-WESRA13A-II3
kind: problem
title: 'Vanishing integrals over compact subsets'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. Flash garbles the integral typography, but the compact-set quantifier and zero integral are unambiguous in the deterministic text.
---

::: {.problem}
Let $A\subset\mathbb R$ be Lebesgue measurable and let $f:A\to\mathbb R$ be measurable.
Suppose
\[
\int_K f\,dm=0
\]
for every compact $K\subset A$.
Must $f=0$ almost everywhere?
Prove the conclusion or give a counterexample.
:::

::: {.solution}
Yes. The hypotheses force
$$
f=0
$$
almost everywhere on $A$.

<1>1. If
$$
m(\{x\in A:f(x)>0\})>0,
$$
then there exists $r\in\NN$ such that
$$
E_r=\{x\in A:f(x)\ge1/r\}
$$
has positive measure.

::: {.proof}
Because $f$ is real-valued,
$$
\{f>0\}
=
\bigcup_{r=1}^{\infty}\{f\ge1/r\}.
$$
If every set on the right had measure zero, then their countable union would also have measure zero. Therefore positive measure of $\{f>0\}$ forces positive measure of some $E_r$.
:::

<1>2. If $m(E_r)>0$, then there is a compact set
$$
K\subset E_r
$$
with $m(K)>0$.

::: {.proof}
Choose $N$ so large that
$$
m(E_r\cap[-N,N])>0;
$$
such an $N$ exists because
$$
E_r=\bigcup_{N=1}^{\infty}(E_r\cap[-N,N]).
$$
The set $E_r\cap[-N,N]$ is measurable and has finite measure. By inner regularity of Lebesgue measure, for
$$
0<\varepsilon<m(E_r\cap[-N,N])
$$
there exists a compact set
$$
K\subset E_r\cap[-N,N]
$$
with
$$
m(K)>m(E_r\cap[-N,N])-\varepsilon>0.
$$
:::

<1>3. The set $\{f>0\}$ has measure zero.

::: {.proof}
Suppose it had positive measure. By steps <1>1--<1>2, there would be some $r$ and a compact set $K\subset E_r\subset A$ with $m(K)>0$. On $K$,
$$
f\ge\frac1r.
$$
Hence
$$
\int_K f\,dm
\ge
\frac1r m(K)
>0,
$$
contradicting the hypothesis that the integral is zero for every compact $K\subset A$.
:::

<1>4. The set $\{f<0\}$ also has measure zero.

::: {.proof}
Apply step <1>3 to the measurable function $-f$. For every compact $K\subset A$,
$$
\int_K(-f)\,dm
=-\int_K f\,dm
=0.
$$
Therefore
$$
m(\{-f>0\})=0,
$$
which is exactly
$$
m(\{f<0\})=0.
$$
:::

<1>5. Therefore
$$
\boxed{f=0\text{ almost everywhere on }A}.
$$

::: {.proof}
The set where $f\ne0$ is
$$
\{f>0\}\cup\{f<0\}.
$$
Both sets have measure zero by steps <1>3--<1>4, so their union has measure zero.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
