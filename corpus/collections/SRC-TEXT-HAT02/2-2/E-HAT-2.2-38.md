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
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Checked all three diagram chases: the composites vanish using the two exact rows and the three
    commutative squares, and exactness at $B_n$, at $C_n\oplus D_n$ and at $E_n$ follows by the
    stated decompositions, the minus sign on the second coordinate being what makes $cr-r'b$
    vanish.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement checked against the printed diagram, rendered from p. 159: the two rows and the six
    vertical arrows agree with the card, including the identity arrows at A_n and A_{n-1}, and the
    text matches as printed. The chase is correct at all three middle terms, and the two composite
    vanishings follow from rq = 0, q'p' = 0 and the commutativity bq = q', cr = r'b, s'c = s. What
    is not covered: the convergence of the sequence (that consecutive composite maps vanish) is
    asserted rather than computed term by term.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the diagram chase, which is what Queue D asks for on this card. The maps and the vanishing of consecutive composites are a step, and each of the three middle terms is then a step whose proof is the chase in both directions; the notation and the three commutation relations are declared before the proof, and the closing step says why the argument repeats in every degree rather than only in n. No retained set covers Hatcher §2.2 Exercise 38 (Poulsen's section-2.2 exercises are 2, 4, 7, 9, 13, 17, 20, 21, 22, 23, 32 and 36, and Li's list omits 38), so the card says the argument is its own; that is unchanged from the prose it replaces, and the card has said so since it was written. Statement re-read against Hatcher, Algebraic Topology (2002), §2.2 Exercise 38, printed p. 159, and the diagram is the printed one. No statement repair.
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
No retained solution set covers this exercise: the checkout's Hatcher sets reach §2.2 in Poulsen (exercises 2, 4, 7, 9, 13, 17, 20, 21, 22, 23, 32, 36) and Li (whose section-2.2 entries are the exercises printed as 2.2.1--2.2.9, 2.2.12, 2.2.14, 2.2.19--2.2.22, 2.2.24, 2.2.29, 2.2.32, 2.2.40 and 2.2.41), and neither holds exercise 38. The argument is therefore the card's own, written out below and checked against Hatcher, *Algebraic Topology* (2002), §2.2 Exercise 38: the only inputs are the exactness of the two printed rows and the commutativity of its six squares.

Name the maps in one period of the upper row
$$
C_{n+1}\xrightarrow{p}A_n\xrightarrow{q}B_n\xrightarrow{r}C_n
\xrightarrow{s}A_{n-1}\xrightarrow{t}B_{n-1},
$$
and those in the lower row $p',q',r',s',t'$; let $b:B_n\to D_n$ and $c:C_n\to E_n$ be the vertical maps. The vertical maps at $A_n$ and $A_{n-1}$ are identities, so commutativity of the three squares with a $B$ or $C$ corner says
$$
bq=q',\qquad r'b=cr,\qquad s'c=s .
$$

::: pf

::: {.pf-step #proposed-maps}
The maps
$$
E_{n+1}\xrightarrow{qp'}B_n\xrightarrow{(r,-b)}C_n\oplus D_n\xrightarrow{c+r'}E_n\xrightarrow{ts'}B_{n-1}
$$
are defined, and each composite of two consecutive ones is zero.

::: pf-proof
The composites are computed from exactness of the two rows and the three commutation relations. At $B_n$: $(r,-b)\bigl(qp'(e)\bigr)=\bigl(rq\,p'(e),-bq\,p'(e)\bigr)=(0,-q'p'(e))=(0,0)$, using $rq=0$ from exactness of the upper row at $B_n$ and $q'p'=0$ from exactness of the lower row at $A_n$. At $C_n\oplus D_n$: $(c+r')\bigl(r(b_0),-b(b_0)\bigr)=cr(b_0)-r'b(b_0)=0$ because $r'b=cr$. At $E_n$: $(ts')\bigl(c(x)+r'(d)\bigr)=ts'c(x)+ts'r'(d)=ts(x)+0=0$, using $s'c=s$ and $tr'=0$ from exactness of the lower row at $E_n$.
:::

:::

::: {.pf-step #exact-at-b}
The kernel of $(r,-b)$ is the image of $qp'$.

::: pf-proof
If $(r(b_0),-b(b_0))=(0,0)$ then $r(b_0)=0$, so exactness of the upper row at $B_n$ gives $b_0=q(a)$ for some $a\in A_n$. Then $b(b_0)=bq(a)=q'(a)$, and $b(b_0)=0$ by hypothesis, so $q'(a)=0$ and exactness of the lower row at $A_n$ gives $a=p'(e)$ for some $e\in E_{n+1}$. Hence $b_0=q(a)=qp'(e)$, and the reverse inclusion is the vanishing of step [](#proposed-maps){.pf-ref}.
:::

:::

::: {.pf-step #exact-at-sum}
The kernel of $c+r'$ is the image of $(r,-b)$.

::: pf-proof
Let $c(x)+r'(d)=0$ with $x\in C_n$, $d\in D_n$. Applying $s'$ gives $0=s'c(x)+s'r'(d)=s(x)$, the second term vanishing by exactness of the lower row at $E_n$; so exactness of the upper row at $C_n$ gives $x=r(b_0)$ for some $b_0\in B_n$. Then $r'(d)=-c(x)=-cr(b_0)=-r'b(b_0)$, that is $r'\bigl(b(b_0)+d\bigr)=0$, so exactness of the lower row at $D_n$ gives $b(b_0)+d=q'(a)=bq(a)$ for some $a\in A_n$. Put $b_1=b_0-q(a)$; then $r(b_1)=r(b_0)-rq(a)=x$ and $-b(b_1)=-b(b_0)+bq(a)=d$, so $(x,d)=(r,-b)(b_1)$ lies in the image. The reverse inclusion is again step [](#proposed-maps){.pf-ref}.
:::

:::

::: {.pf-step #exact-at-e}
The kernel of $ts'$ is the image of $c+r'$, and the same chase in every degree gives the exact sequence of the exercise.

::: pf-proof
Let $ts'(e)=0$ with $e\in E_n$. Then $s'(e)\in\ker t=\operatorname{im}s$ by exactness of the upper row at $A_{n-1}$, so $s'(e)=s(x)$ for some $x\in C_n$; hence $s'\bigl(e-c(x)\bigr)=s'(e)-s'c(x)=s(x)-s(x)=0$, and exactness of the lower row at $E_n$ gives $e-c(x)=r'(d)$ for some $d\in D_n$, that is $e=(c+r')(x,d)$. The reverse inclusion is step [](#proposed-maps){.pf-ref}. Together with steps [](#exact-at-b){.pf-ref} and [](#exact-at-sum){.pf-ref} this gives exactness at $B_n$, $C_n\oplus D_n$ and $E_n$; every map used in the argument is natural in $n$ and every hypothesis (the two exact rows, the six commuting squares, the two identity vertical maps) holds in each degree, so the same chase proves exactness at $B_{k}$, $C_k\oplus D_k$ and $E_k$ for every $k$, which is the exact sequence the exercise asserts.
:::

:::

:::
:::
