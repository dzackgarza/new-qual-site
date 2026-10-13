---
schema: qual/card@1
id: P-UNL872S14-PP-2
kind: problem
title: UNL Math 872 Spring 2014 assignment PP.2
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against assignment PP.2 on the retained UNL Math 872 Section 001 Spring 2014 problem-sets page PDF.
---

::: {.problem}
Let X be the space obtained from the solid cube I x I x I by gluing opposite square faces to one another with a 90-degree righthand twist (e.g., glue $\mathrm { ~ I ~ x ~ I ~ x ~ } \{ 0 \}$to$\operatorname { I } \mathrm { \mathrm { ~ x ~ I ~ x ~ } } \{ 1 \}$by identifying (x,y,0) with (y,1-x,1)). Describe a CW structure for X and compute a presentation for$\pi _ { 1 } ( \mathrm { X } )$ .
:::

::: {.solution}
Use the following cyclic-coordinate formulas for the three right-hand
quarter-turn identifications:
\[
\begin{aligned}
(0,y,z)&\sim(1,z,1-y),\\
(x,0,z)&\sim(1-z,1,x),\\
(x,y,0)&\sim(y,1-x,1).
\end{aligned}
\]
The last is the identification stated in the problem; the first two are its
cyclic analogues.

<1>1. The eight cube vertices fall into exactly two equivalence classes:
\[
\boxed{
A=\{000,011,101,110\},
\qquad
B=\{001,010,100,111\}}.
\]

::: {.proof}
Apply the three face identifications to the vertices. For example,
\[
000\sim101,\qquad
000\sim110,\qquad
000\sim011.
\]
Thus the four vertices listed in \(A\) are equivalent.

Similarly,
\[
001\sim111,\qquad
001\sim010,\qquad
001\sim100,
\]
so the four vertices listed in \(B\) are equivalent.

Each face identification preserves the parity class indicated by these two
sets, so no vertex of \(A\) is identified with a vertex of \(B\).
:::

<1>2. The twelve open cube edges fall into four equivalence classes.

::: {.proof}
Choose the following oriented representatives:
\[
\begin{aligned}
p&:000\longrightarrow100,\\
q&:000\longrightarrow010,\\
r&:001\longrightarrow101,\\
s&:010\longrightarrow110.
\end{aligned}
\]
Tracking the edges under the three quarter-turn face pairings gives the four
orbits
\[
\begin{aligned}
p:\quad&
[000,100],\ [001,011]^{-1},\ [110,111],\\
q:\quad&
[000,010],\ [100,101]^{-1},\ [011,111],\\
r:\quad&
[001,101],\ [100,110],\ [010,011],\\
s:\quad&
[010,110],\ [101,111]^{-1},\ [000,001]^{-1}.
\end{aligned}
\]
Every one of the twelve edges occurs exactly once in this list.
:::

<1>3. The quotient therefore has a CW structure with two \(0\)-cells
\[
A,B,
\]
four \(1\)-cells
\[
p,q,r,s,
\]
three \(2\)-cells, and one \(3\)-cell.

::: {.proof}
Step <1>1 gives the two vertex orbits and step <1>2 gives the four open-edge
orbits.

The six open faces are paired into three opposite-face pairs, so their
images give three open \(2\)-cells. The open cube interior is unaffected by
the boundary identifications and gives one open \(3\)-cell. These cells,
with the quotient characteristic maps inherited from the cube, form the
desired CW structure.
:::

<1>4. Taking the \(x=0\) face with boundary
\[
000\to010\to011\to001\to000,
\]
its attaching word is
\[
\boxed{q\,r\,p\,s}.
\]

::: {.proof}
The four successive boundary edges represent:
\[
000\to010=q,
\]
\[
010\to011=r,
\]
\[
011\to001=p,
\]
and
\[
001\to000=s.
\]
The last two equalities use the orientations recorded in step <1>2.
:::

<1>5. Taking the \(y=0\) face with boundary
\[
000\to001\to101\to100\to000,
\]
its attaching word is
\[
\boxed{s^{-1}rqp^{-1}}.
\]

::: {.proof}
Using step <1>2, the successive edges are
\[
000\to001=s^{-1},
\qquad
001\to101=r,
\]
\[
101\to100=q,
\qquad
100\to000=p^{-1}.
\]
:::

<1>6. Taking the \(z=0\) face with boundary
\[
000\to100\to110\to010\to000,
\]
its attaching word is
\[
\boxed{pr\,s^{-1}q^{-1}}.
\]

::: {.proof}
The four successive edges are
\[
p,\qquad r,\qquad s^{-1},\qquad q^{-1},
\]
again by the orbit orientations in step <1>2.
:::

<1>7. The \(1\)-cell \(p\) is a maximal tree in the \(1\)-skeleton.

::: {.proof}
There are exactly two vertices \(A\) and \(B\), and the edge \(p\) joins
them. Thus \(p\) is a connected tree containing every vertex.
:::

<1>8. Collapsing this maximal tree gives the presentation
\[
\boxed{
\pi_1(X)
\cong
\left\langle
q,r,s
\ \middle|\
qrs,\ s^{-1}rq,\ rs^{-1}q^{-1}
\right\rangle}.
\]

::: {.proof}
Collapsing a maximal tree in the \(1\)-skeleton does not change the
fundamental group. In the three attaching words from steps <1>4--<1>6, set
\[
p=1.
\]
This gives exactly the three displayed relators. The \(3\)-cell does not
affect the fundamental group.
:::

<1>9. The first relation gives
\[
\boxed{s=(qr)^{-1}=r^{-1}q^{-1}}.
\]

::: {.proof}
The relation
\[
qrs=1
\]
is equivalent to the displayed formula.
:::

<1>10. Eliminating \(s\), the second relation becomes
\[
\boxed{r^2=q^{-2}}.
\]

::: {.proof}
By step <1>9,
\[
s^{-1}=qr.
\]
Thus
\[
s^{-1}rq=1
\]
becomes
\[
qrrq=qr^2q=1.
\]
Multiplying by \(q^{-1}\) on both sides gives
\[
r^2=q^{-2}.
\]
:::

<1>11. Eliminating \(s\), the third relation becomes
\[
\boxed{q^{-1}rq=r^{-1}}.
\]

::: {.proof}
Again using
\[
s^{-1}=qr,
\]
the relation
\[
rs^{-1}q^{-1}=1
\]
becomes
\[
rqrq^{-1}=1.
\]
Equivalently,
\[
rqr=q.
\]
Multiplying on the left by \(q^{-1}\) and on the right by \(r^{-1}\) gives
\[
q^{-1}rq=r^{-1}.
\]
:::

<1>12. The relations in steps <1>10 and <1>11 imply
\[
\boxed{r^4=1}
\qquad\text{and}\qquad
\boxed{q^2=r^2}.
\]

::: {.proof}
Conjugate the equality
\[
r^2=q^{-2}
\]
by \(q^{-1}(-)q\). By step <1>11,
\[
q^{-1}r^2q=r^{-2},
\]
while
\[
q^{-1}q^{-2}q=q^{-2}.
\]
Hence
\[
r^{-2}=q^{-2}.
\]
Together with
\[
r^2=q^{-2},
\]
this gives
\[
r^2=r^{-2},
\]
so
\[
r^4=1.
\]
Then
\[
r^{-2}=r^2,
\]
and therefore
\[
q^2=r^2.
\]
:::

<1>13. Thus
\[
\pi_1(X)
\cong
\left\langle
r,q
\ \middle|\
r^4=1,\ q^2=r^2,\ q^{-1}rq=r^{-1}
\right\rangle.
\]

::: {.proof}
Steps <1>9--<1>12 eliminate \(s\) and rewrite the remaining relations in
the displayed standard form.
:::

<1>14. Every element of the group in step <1>13 can be written in the form
\[
\boxed{r^a q^b}
\]
with
\[
0\le a<4,
\qquad
b\in\{0,1\}.
\]

::: {.proof}
From
\[
q^{-1}rq=r^{-1}
\]
one obtains
\[
qr=r^{-1}q.
\]
Thus every \(q\) can be moved to the right of every \(r\). The relation
\[
q^2=r^2
\]
reduces every power of \(q\) to exponent \(0\) or \(1\), and
\[
r^4=1
\]
reduces the exponent of \(r\) modulo \(4\). Hence there are at most eight
elements.
:::

<1>15. The presentation in step <1>13 maps onto the quaternion group
\[
Q_8=\{\pm1,\pm i,\pm j,\pm k\}.
\]

::: {.proof}
Send
\[
r\longmapsto i,
\qquad
q\longmapsto j.
\]
In \(Q_8\),
\[
i^4=1,
\qquad
j^2=i^2=-1,
\]
and
\[
j^{-1}ij=i^{-1}.
\]
Thus the defining relations are satisfied. Since \(i\) and \(j\) generate
\(Q_8\), the resulting homomorphism is surjective.
:::

<1>16. Therefore
\[
\boxed{\pi_1(X)\cong Q_8}.
\]

::: {.proof}
Step <1>14 shows that the presented group has at most eight elements. Step
<1>15 gives a surjection onto \(Q_8\), which has exactly eight elements.
Hence the presented group has exactly eight elements and the surjection is
an isomorphism.
:::

<1>17. Q.E.D.

::: {.proof}
Step <1>3 gives the requested CW structure, step <1>8 gives a presentation
directly from the cell attachments, and step <1>16 identifies that
presentation with the quaternion group.
:::
:::
