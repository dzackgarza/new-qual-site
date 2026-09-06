---
schema: qual/card@1
id: P-AMD-73FM5GNT
kind: problem
title: Nonsimplicity below order $60$ implies solvability
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Simple Groups
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 5, Exercise 5(a). The
    handout literally says to suppose that all groups of order less than 60 are
    not simple, which is false for cyclic groups of prime order. Restored the
    mathematically intended hypothesis: every nonabelian group of order less
    than 60 is not simple, and retained the source's requested implication to
    solvability.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Strong induction on the order reduces a nonabelian group to a nontrivial
    proper normal subgroup N and the quotient G/N. Both have smaller order and
    are solvable by induction. The extension step is proved directly with
    derived series: (G/N)^(r)=1 gives G^(r) <= N, and N^(s)=1 then gives
    G^(r+s)=1.
---

::: {.problem}
Assume that every nonabelian finite group $H$ with
\[
|H|<60
\]
is not simple.
Prove that every finite group $G$ with $|G|<60$ is solvable.

The handout states the hypothesis as ``all groups of order less than $60$ are not simple.'' Since every cyclic group of prime order is simple, the nonabelian restriction above is the mathematically necessary interpretation.
:::

::: {.solution}
<1>1. We prove by strong induction on $|G|$ that every finite group $G$ of order less than $60$ is solvable.
::: {.proof}
For $|G|=1$, the group is trivial and hence solvable.

Assume now that $1<|G|<60$ and that every group of smaller order is solvable.
:::

<1>2. If $G$ is abelian, then $G$ is solvable.
::: {.proof}
Indeed,
\[
G^{(1)}=[G,G]=1.
\]
:::

<1>3. Suppose that $G$ is nonabelian.
Then $G$ has a nontrivial proper normal subgroup
\[
1<N<G.
\]
::: {.proof}
By hypothesis, every nonabelian group of order less than $60$ is not simple.
Since $G$ is nonabelian and $|G|<60$, the group $G$ is not simple.
Therefore it has a normal subgroup $N$ satisfying
\[
1<N<G.
\]
:::

<1>4. Both $N$ and $G/N$ are solvable.
::: {.proof}
Because $N$ is nontrivial and proper,
\[
|N|<|G|
\qquad\text{and}\qquad
|G/N|<|G|.
\]
The induction hypothesis therefore applies to both $N$ and $G/N$.
:::

<1>5. If $N\trianglelefteq G$, and both $N$ and $G/N$ are solvable, then $G$ is solvable.
::: {.proof}
Choose integers $r,s\ge 0$ such that
\[
(G/N)^{(r)}=1
\qquad\text{and}\qquad
N^{(s)}=1.
\]
For the quotient map $\pi:G\to G/N$, derived subgroups commute with taking images, so
\[
\pi\bigl(G^{(r)}\bigr)=(G/N)^{(r)}=1.
\]
Hence
\[
G^{(r)}\le N.
\]
Taking $s$ further derived subgroups gives
\[
G^{(r+s)}=(G^{(r)})^{(s)}\le N^{(s)}=1.
\]
Thus $G$ is solvable.
:::

<1>6. Hence every finite group of order less than $60$ is solvable.
::: {.proof}
If $G$ is abelian, use <1>2. If $G$ is nonabelian, combine <1>3, <1>4, and <1>5. This completes the induction.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
