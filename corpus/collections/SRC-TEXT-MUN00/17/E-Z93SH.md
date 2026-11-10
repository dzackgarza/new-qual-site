---
schema: qual/card@1
id: E-Z93SH
kind: problem
title: Kuratowski's fourteen-set theorem
classification:
  areas:
  - topology
  topics:
  - Closure
  - Interior
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 21, printed p. 102; parts (a) and
    (b) are stored as printed, the starred exercise being the fourteen-set theorem.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 17.21, printed pp.
    175-178. His are the three identities, the reduction of a word in closure and complement
    to an alternating word, the two sequences of seven and the identity closing each, and
    the example of (b) with its two columns of seven sets. His chains of substitutions for
    the two identities icic = ic and cici = ci are replaced by their two-line proofs, which
    is what those chains verify, and the distinctness of the fourteen sets is checked
    against the table. (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Consider the collection of all subsets $A$ of the topological space $X$.
The operations of closure $A \to \overline{A}$ and complementation $A \to X - A$ are functions from this collection to itself.

(a) Show that starting with a given set $A$, one can form no more than 14 distinct sets by applying these two operations successively.

(b) Find a subset $A$ of $\RR$ (in its usual topology) for which the maximum of 14 is obtained.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 17.21, printed pp. 175--178** (`tmp/sources/munkres-solutions-whitman.pdf`); the list of identities, the enumeration of at most fourteen sets and the example of (b) are his. The proofs of his identities (h) and (i) are replaced below by their two-line arguments, which are what his chains of substitutions amount to. "positron0802", *Solutions to Topology, Chapter 2*, Exercise 17.21, PDF p. 10, proves (a) by the same route.

Write $c(A)=\overline{A}$, $i(A)=\operatorname{Int}A$ and $x(A)=X-A$; these are operations on subsets of $X$, and a word in $c$ and $x$ applied to $A$ means the successive application, so that $xcA=X-\overline{A}$.

**Lemma 1.** $\overline{A}=X-\operatorname{Int}(X-A)$ and $\operatorname{Int}A=X-\overline{X-A}$; equivalently $c=xix$ and $i=xcx$.

*Proof.* Both say the same thing: $X-\overline{X-A}$ is open (a complement of a closed set), lies in $A$, and contains every open set contained in $A$, since an open $U\subset A$ is disjoint from $X-A$ and hence from its closure. $\square$

**Lemma 2.** For all $A$: $ccA=cA$, $xxA=A$, and for $A\subset B$, $cA\subset cB$ and $iA\subset iB$; moreover
$$
cicA=cA \text{ is false in general},\quad\text{but}\quad icicA=icA\quad\text{and}\quad ciciA=ciA .
$$

*Proof.* $cA$ is closed, so $ccA=cA$; $xxA=A$ is set theory; monotonicity of $c$ is Exercise 17.6(a) and that of $i$ follows since $\operatorname{Int}A\subset A\subset B$. For the two non-trivial identities put $U=i(A)$. Then $icicA=i(cU)$, and since $U$ is open and $U\subset cU$ we get $U\subset i(cU)$, while $cU\subset c(cA)=cA$ gives $i(cU)\subset i(cA)=U$. Hence $i(cU)=U=icA$. Dually, with $V=c(iA)$: $ci(cV)=cV$ because $i(cV)\supset i(V)=V$ gives $cV\subset c(i(cV))$ and $c(i(cV))\subset c(cV)=cV$. Taking $V=c(iA)$ gives $c i c i A=c i A$. $\square$

(a) By Lemma 2 a word in $c$ and $x$ may be reduced to one with no repetition of a letter, that is, to an alternating word; and it is enough to list the sets obtained along the two alternating sequences, since any alternating word is a prefix of one of the two.

Applying $c$ first, from $A$:
$$
A,\quad cA,\quad xcA,\quad cxcA,\quad xcxcA,\quad cxcxcA,\quad xcxcxcA,\quad cxcxcxcA .
$$
The last is $cxcA$: using $i=xcx$ (Lemma 1), $cxcxcxc=c\,(xcx)\,(cxc)=c\,i\,(cix)=cicix=(cici)x=cix=cxc$, where $cix=cxc$ because $ci=c\,xcx=cxcx$ and $cxcx\,x=cxc$. So this sequence yields at most the seven sets $A$, $cA$, $xcA$, $cxcA$, $xcxcA$, $cxcxcA$, $xcxcxcA$.

Applying $x$ first, from $A$:
$$
xA,\quad cxA,\quad xcxA,\quad cxcxA,\quad xcxcxA,\quad cxcxcxA,\quad xcxcxcxA,\quad cxcxcxcxA .
$$
The last is $cxcxA$, because $cxcxcxcx=(cxcx)(cxcx)=(ci)(ci)=ci=cxcx$. So this sequence yields at most seven further sets.

Hence every word in $c$ and $x$ applied to $A$ gives one of at most $7+7=14$ sets, and no more than fourteen distinct sets can be formed.

(b) Take, in $\RR$ with the usual topology,
$$
A=(-3,-2)\cup(-2,-1)\cup\big([0,1]\cap\QQ\big)\cup\{2\}.
$$
The following fourteen sets are obtained, the first column from $A$ by the sequence beginning with $c$ and the second from $A$ by the sequence beginning with $x$:

| word | set | word | set |
| --- | --- | --- | --- |
| $A$ | $(-3,-2)\cup(-2,-1)\cup([0,1]\cap\QQ)\cup\{2\}$ | $xA$ | $(-\infty,-3]\cup\{-2\}\cup[-1,0)\cup((0,1)-\QQ)\cup(1,2)\cup(2,\infty)$ |
| $cA$ | $[-3,-1]\cup[0,1]\cup\{2\}$ | $cxA$ | $(-\infty,-3]\cup\{-2\}\cup[-1,\infty)$ |
| $xcA$ | $(-\infty,-3)\cup(-1,0)\cup(1,2)\cup(2,\infty)$ | $xcxA$ | $(-3,-2)\cup(-2,-1)$ |
| $cxcA$ | $(-\infty,-3]\cup[-1,0]\cup[1,\infty)$ | $cxcxA$ | $[-3,-1]$ |
| $xcxcA$ | $(-3,-1)\cup(0,1)$ | $xcxcxA$ | $(-\infty,-3)\cup(-1,\infty)$ |
| $cxcxcA$ | $[-3,-1]\cup[0,1]$ | $cxcxcxA$ | $(-\infty,-3]\cup[-1,\infty)$ |
| $xcxcxcA$ | $(-\infty,-3)\cup(-1,0)\cup(1,\infty)$ | $xcxcxcxA$ | $(-3,-1)$ |

Each row is obtained from the row above by taking the closure (column 1) or the complement (column 2): for instance $\overline{[0,1]\cap\QQ}=[0,1]$ and $\operatorname{Int}\big([0,1]\cap\QQ\big)=\varnothing$, since every interval meets both $\QQ$ and $\RR-\QQ$; and $\overline{(0,1)-\QQ}=[0,1]$ likewise. The two columns consist of fourteen sets no two of which are equal — they differ in their endpoints, in whether the isolated points $-2$ and $2$ are present, and in whether the rationals of $[0,1]$ or its irrationals are — so the bound of part (a) is attained in $\RR$.
:::
