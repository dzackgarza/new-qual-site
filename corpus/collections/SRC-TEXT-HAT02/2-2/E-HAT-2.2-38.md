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
Show that a commutative diagram with the two sequences across the top and bottom exact, and every third vertical map an isomorphism, gives rise to an exact sequence $\cdots \to E_{n+1} \to B_n \to C_n \oplus D_n \to E_n \to B_{n-1} \to \cdots$ where the maps are obtained from those in the previous diagram in the obvious way, except that $B_n \to C_n \oplus D_n$ has a minus sign in one coordinate.
:::

::: {.solution}
The diagram in the exercise is the standard situation obtained by lining up two exact sequences and identifying every third vertical term.  A concise way to perform the required diagram chase is to package one three-term period into a mapping cone.

<1>1. After using each indicated vertical isomorphism to identify the corresponding top and bottom groups, one period of the diagram has the form
\[
B_n\xrightarrow{u_n}C_n\oplus D_n\xrightarrow{v_n}E_n\xrightarrow{w_n}B_{n-1}.
\]
The maps are the horizontal maps in the two rows, with
\[
u_n(b)=(u_n^C(b),-u_n^D(b)).
\]
::: {.proof}
The two exact rows commute with the vertical maps.  Transporting across the vertical isomorphisms therefore leaves only the four groups displayed above.  The sign in the second coordinate is forced by the usual difference map: it makes the two contributions through the commuting square cancel, hence $v_nu_n=0$.
:::

<1>2. The successive composites in the displayed sequence are zero.
::: {.proof}
For $v_nu_n$ this is the cancellation just noted.  The composite $w_nv_n$ is zero because each coordinate of $v_n$ lands, by commutativity, in the kernel of the next horizontal map in the appropriate exact row.  The same argument applies one degree later to $u_{n-1}w_n$.
:::

<1>3. The sequence is exact at $C_n\oplus D_n$.
::: {.proof}
Let $(c,d)\in\ker v_n$.  Equality of the two images in the common identified term says, by commutativity, that the discrepancy between $c$ and $d$ dies in the next group of each exact row.  Exactness of the rows therefore produces $b\in B_n$ whose two horizontal images are $c$ and $-d$.  Thus $(c,d)=u_n(b)$.  Conversely $\operatorname{im}u_n\subseteq\ker v_n$ by <1>2.
:::

<1>4. The sequence is exact at $E_n$.
::: {.proof}
If $e\in\ker w_n$, exactness of one row lifts $e$ to the preceding term.  Compare this lift with its image in the other row.  Their difference lies in the kernel of the next horizontal map, hence by exactness is corrected by an element of the preceding group.  After this correction the two lifts form a pair $(c,d)$ with $v_n(c,d)=e$.  Thus $e\in\operatorname{im}v_n$.  The reverse inclusion follows from <1>2.
:::

<1>5. The sequence is exact at $B_{n-1}$.
::: {.proof}
For $b\in\ker u_{n-1}$, its two horizontal images vanish after the sign convention.  Exactness in either row gives a preimage in the preceding common term.  Transporting that preimage through the vertical isomorphism and correcting by exactness in the other row gives $e\in E_n$ with $w_n(e)=b$.  Hence $\ker u_{n-1}=\operatorname{im}w_n$.
:::

<1>6. Repeating the argument in every degree gives the required long exact sequence
\[
\boxed{\cdots\longrightarrow E_{n+1}\longrightarrow B_n
\longrightarrow C_n\oplus D_n\longrightarrow E_n
\longrightarrow B_{n-1}\longrightarrow\cdots.}
\]
::: {.proof}
Steps <1>2--<1>5 prove exactness at each of the four types of consecutive terms.  Shifting $n$ repeats the same argument throughout the bi-infinite sequence.
:::
:::
