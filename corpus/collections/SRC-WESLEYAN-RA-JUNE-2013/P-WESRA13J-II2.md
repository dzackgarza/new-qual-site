---
schema: qual/card@1
id: P-WESRA13J-II2
kind: problem
title: 'Positive-measure compact sets without intervals and everywhere-thick measurable sets'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. Flash renders the source interval delimiters as braces; they are normalized to $[0,1]$ from the stated Lebesgue-interval context.
---

::: {.problem}
(a) Give an example of a compact set $K\subset[0,1]$ with positive Lebesgue measure but containing no nonempty open interval.

(b) Prove that there exists $A\subset[0,1]$ such that every interval $I\subset[0,1]$ of positive measure satisfies
\[
0<m(A\cap I)<m(I).
\]
:::

::: {.solution}
<1>1. There exists a compact set $K\subseteq[0,1]$ with
$$
m(K)=\frac12
$$
and containing no nonempty open interval.

::: {.proof}
Start with $K_0=[0,1]$. At stage $n\geq1$, each of the $2^{n-1}$ closed interval components of $K_{n-1}$ has the same length. From the middle of each component remove an open interval of length $4^{-n}$, and let $K_n$ be the union of the remaining closed intervals. Define
$$
K=\bigcap_{n=0}^\infty K_n.
$$
Each $K_n$ is compact and the sequence is decreasing, so $K$ is compact.

At stage $n$, the total removed length is
$$
2^{n-1}4^{-n}=2^{-n-1}.
$$
The removed intervals are pairwise disjoint, so
$$
m(K)
=1-\sum_{n=1}^\infty2^{-n-1}
=1-\frac12
=\frac12.
$$

If $\ell_n$ denotes the common length of a component of $K_n$, then
$$
\ell_n=\frac{\ell_{n-1}-4^{-n}}2<\frac{\ell_{n-1}}2,
$$
and hence $\ell_n<2^{-n}$. Any interval contained in $K$ would be contained in one component of every $K_n$, but those component lengths tend to zero. Thus $K$ contains no nonempty open interval. This proves part (a).
:::

<1>2. Every nonempty open interval $J\subseteq[0,1]$ contains a compact nowhere-dense subset of positive measure.

::: {.proof}
Choose a closed interval $[a,b]\subset J$ with $a<b$. Let $K$ be the set from step <1>1 and let
$$
T(t)=a+(b-a)t.
$$
Then $T(K)\subseteq[a,b]\subset J$ is compact, has measure
$$
m(T(K))=(b-a)m(K)=\frac{b-a}{2}>0,
$$
and contains no nonempty open interval. Since it is closed with empty interior, it is nowhere dense.
:::

<1>3. Let $(J_n)_{n\geq1}$ enumerate all nonempty open intervals with rational endpoints whose closures lie in $(0,1)$. There exist compact sets
$$
K_n,L_n\subseteq J_n
$$
such that each has positive measure and the family
$$
K_1,L_1,K_2,L_2,\ldots
$$
is pairwise disjoint.

::: {.proof}
Construct the sets inductively. Suppose $K_j,L_j$ have been chosen for $j<n$. Their finite union
$$
F_{n-1}=\bigcup_{j<n}(K_j\cup L_j)
$$
is compact and nowhere dense, because it is a finite union of compact nowhere-dense sets. Therefore
$$
J_n\setminus F_{n-1}
$$
is a nonempty open set. It contains two disjoint nonempty open intervals $U_n$ and $V_n$. By step <1>2, choose a compact nowhere-dense set $K_n\subset U_n$ of positive measure and a compact nowhere-dense set $L_n\subset V_n$ of positive measure. They are disjoint from each other and from every previously chosen set. This completes the induction.
:::

<1>4. Define
$$
A=\bigcup_{n=1}^\infty K_n.
$$
Then $A$ is measurable, and every interval $I\subseteq[0,1]$ of positive length satisfies
$$
m(A\cap I)>0.
$$

::: {.proof}
The set $A$ is an $F_\sigma$ set, hence measurable. Let $I\subseteq[0,1]$ have positive length. Its interior contains an interval $J_n$ with rational endpoints and closure in $(0,1)$. By construction,
$$
K_n\subseteq J_n\subseteq I
$$
and $m(K_n)>0$. Since $K_n\subseteq A$,
$$
m(A\cap I)\geq m(K_n)>0.
$$
:::

<1>5. Every interval $I\subseteq[0,1]$ of positive length also satisfies
$$
m(I\setminus A)>0.
$$

::: {.proof}
Choose $J_n\subseteq I$ as in step <1>4. By step <1>3,
$$
L_n\subseteq J_n\subseteq I.
$$
The entire family $(K_j,L_j)$ is pairwise disjoint, while $A=\bigcup_jK_j$. Hence $L_n\cap A=\varnothing$, so
$$
L_n\subseteq I\setminus A.
$$
Since $m(L_n)>0$,
$$
m(I\setminus A)\geq m(L_n)>0.
$$
:::

<1>6. For every interval $I\subseteq[0,1]$ of positive measure,
$$
\boxed{0<m(A\cap I)<m(I)}.
$$

::: {.proof}
The first strict inequality is step <1>4. Since
$$
m(I)=m(A\cap I)+m(I\setminus A)
$$
and step <1>5 gives $m(I\setminus A)>0$, the second strict inequality follows. This proves part (b).
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>1 proves part (a), and step <1>6 proves part (b).
:::
:::
