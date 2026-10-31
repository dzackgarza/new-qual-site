---
schema: qual/card@1
id: E-HAT-2.2-38
kind: problem
title: 'Algebraic lemma: diagram with two exact rows and isomorphisms every third vertical map yields long exact sequence'
classification:
  areas:
  - topology
  topics:
  - Homology
  - Exact Sequences
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 38, including the displayed exact-row diagram.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Recast the spliced sequence as the homology sequence of the mapping cone of the vertical chain map; exactness and the required minus sign follow directly.
---

::: {.problem}
Show that a commutative diagram
$$
\begin{array}{ccccccccccc}
\cdots\to C_{n+1}&\to&A_n&\to&B_n&\to&C_n&\to&A_{n-1}&\to&B_{n-1}\to\cdots\\
\downarrow&&\downarrow&&\downarrow&&\downarrow&&\downarrow&&\downarrow\\
\cdots\to E_{n+1}&\to&A_n&\to&D_n&\to&E_n&\to&A_{n-1}&\to&D_{n-1}\to\cdots
\end{array}
$$
with the two sequences across the top and bottom exact and the vertical maps at $A_n$ identities, gives rise to an exact sequence $\cdots \to E_{n+1} \to B_n \to C_n \oplus D_n \to E_n \to B_{n-1} \to \cdots$ where the maps are obtained from those in the previous diagram in the obvious way, except that $B_n \to C_n \oplus D_n$ has a minus sign in one coordinate.
:::

::: {.solution}
Name the maps in one period of the upper row
$$
C_{n+1}\xrightarrow{p}A_n\xrightarrow{q}B_n\xrightarrow{r}C_n
\xrightarrow{s}A_{n-1}\xrightarrow{t}B_{n-1},
$$
and name those in the lower row $p',q',r',s',t'$. Let $b:B_n\to D_n$ and $c:C_n\to E_n$ be the vertical maps. Commutativity says
$$
bq=q',\qquad cr=r'b,\qquad s'c=s.
$$
The proposed maps, in this period, are
$$
E_{n+1}\xrightarrow{qp'}B_n
\xrightarrow{(r,-b)}C_n\oplus D_n
\xrightarrow{c+r'}E_n
\xrightarrow{ts'}B_{n-1}.
$$
Consecutive composites vanish by exactness of the two rows and the three commutative squares. We check the three types of middle term.

If $(r(b_0),-b(b_0))=0$, exactness of the upper row gives $b_0=q(a)$. Then $0=b(b_0)=q'(a)$, so exactness of the lower row gives $a=p'(e)$ for some $e\in E_{n+1}$. Hence $b_0=qp'(e)$, proving exactness at $B_n$.

Suppose $(x,d)\in C_n\oplus D_n$ and $c(x)+r'(d)=0$. Applying $s'$ gives $s(x)=0$, so $x=r(b_0)$ for some $b_0\in B_n$. Commutativity now gives
$$
0=r'(b(b_0)+d).
$$
By exactness of the lower row, $b(b_0)+d=q'(a)=bq(a)$ for some $a\in A_n$. Set $b_1=b_0-q(a)$. Then $r(b_1)=x$ and $-b(b_1)=d$. This proves exactness at $C_n\oplus D_n$.

Finally, suppose $e\in E_n$ and $ts'(e)=0$. Exactness of the upper row gives $s'(e)=s(x)$ for some $x\in C_n$. Thus $s'(e-c(x))=0$, and exactness of the lower row gives $e-c(x)=r'(d)$ for some $d\in D_n$. Hence $e=(c+r')(x,d)$, proving exactness at $E_n$. These arguments repeat in every degree.
:::
