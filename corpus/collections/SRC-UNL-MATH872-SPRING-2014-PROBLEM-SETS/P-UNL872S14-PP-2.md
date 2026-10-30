---
schema: qual/card@1
id: P-UNL872S14-PP-2
kind: problem
title: CW structure and $\pi_1$ of the cube with opposite faces glued by a quarter twist
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
Let $X$ be the space obtained from the solid cube $I \times I \times I$ by gluing opposite square faces to one another with a $90$-degree righthand twist (e.g., glue $I \times I \times \{0\}$ to $I \times I \times \{1\}$ by identifying $(x, y, 0)$ with $(y, 1 - x, 1)$). Describe a CW structure for $X$ and compute a presentation for $\pi_{1}(X)$.
:::

::: {.solution}

Use the following cyclic-coordinate formulas for the three right-hand
quarter-turn identifications:
$$
\begin{aligned}
(0,y,z)&\sim(1,z,1-y),\\
(x,0,z)&\sim(1-z,1,x),\\
(x,y,0)&\sim(y,1-x,1).
\end{aligned}
$$
The last is the identification stated in the problem; the first two are its
cyclic analogues.

::: pf

::: {.pf-step #s1-1}

The eight cube vertices fall into exactly two equivalence classes:
$$
\boxed{
A=\{000,011,101,110\},
\qquad
B=\{001,010,100,111\}}.
$$


::: pf-proof

Apply the three face identifications to the vertices. For example,
$$
000\sim101,\qquad
000\sim110,\qquad
000\sim011.
$$
Thus the four vertices listed in $A$ are equivalent.

Similarly,
$$
001\sim111,\qquad
001\sim010,\qquad
001\sim100,
$$
so the four vertices listed in $B$ are equivalent.

Each face identification preserves the parity class indicated by these two
sets, so no vertex of $A$ is identified with a vertex of $B$.

:::

:::

::: {.pf-step #s1-2}

The twelve open cube edges fall into four equivalence classes.


::: pf-proof

Choose the following oriented representatives:
$$
\begin{aligned}
p&:000\longrightarrow100,\\
q&:000\longrightarrow010,\\
r&:001\longrightarrow101,\\
s&:010\longrightarrow110.
\end{aligned}
$$
Tracking the edges under the three quarter-turn face pairings gives the four
orbits
$$
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
$$
Every one of the twelve edges occurs exactly once in this list.

:::

:::

::: {.pf-step #s1-3}

The quotient therefore has a CW structure with two $0$-cells
$$
A,B,
$$
four $1$-cells
$$
p,q,r,s,
$$
three $2$-cells, and one $3$-cell.


::: pf-proof

Step [](#s1-1){.pf-ref} gives the two vertex orbits and step [](#s1-2){.pf-ref} gives the four open-edge
orbits.

The six open faces are paired into three opposite-face pairs, so their
images give three open $2$-cells. The open cube interior is unaffected by
the boundary identifications and gives one open $3$-cell. These cells,
with the quotient characteristic maps inherited from the cube, form the
desired CW structure.

:::

:::

::: {.pf-step #s1-4}

Taking the $x=0$ face with boundary
$$
000\to010\to011\to001\to000,
$$
its attaching word is
$$
\boxed{q\,r\,p\,s}.
$$


::: pf-proof

The four successive boundary edges represent:
$$
000\to010=q,
$$
$$
010\to011=r,
$$
$$
011\to001=p,
$$
and
$$
001\to000=s.
$$
The last two equalities use the orientations recorded in step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Taking the $y=0$ face with boundary
$$
000\to001\to101\to100\to000,
$$
its attaching word is
$$
\boxed{s^{-1}rqp^{-1}}.
$$


::: pf-proof

Using step [](#s1-2){.pf-ref}, the successive edges are
$$
000\to001=s^{-1},
\qquad
001\to101=r,
$$
$$
101\to100=q,
\qquad
100\to000=p^{-1}.
$$

:::

:::

::: {.pf-step #s1-6}

Taking the $z=0$ face with boundary
$$
000\to100\to110\to010\to000,
$$
its attaching word is
$$
\boxed{pr\,s^{-1}q^{-1}}.
$$


::: pf-proof

The four successive edges are
$$
p,\qquad r,\qquad s^{-1},\qquad q^{-1},
$$
again by the orbit orientations in step [](#s1-2){.pf-ref}.

:::

:::

::: pf-step

The $1$-cell $p$ is a maximal tree in the $1$-skeleton.


::: pf-proof

There are exactly two vertices $A$ and $B$, and the edge $p$ joins
them. Thus $p$ is a connected tree containing every vertex.

:::

:::

::: {.pf-step #s1-8}

Collapsing this maximal tree gives the presentation
$$
\boxed{
\pi_1(X)
\cong
\left\langle
q,r,s
\ \presentationbar\
qrs,\ s^{-1}rq,\ rs^{-1}q^{-1}
\right\rangle}.
$$


::: pf-proof

Collapsing a maximal tree in the $1$-skeleton does not change the
fundamental group. In the three attaching words from steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref}, set
$$
p=1.
$$
This gives exactly the three displayed relators. The $3$-cell does not
affect the fundamental group.

:::

:::

::: {.pf-step #s1-9}

The first relation gives
$$
\boxed{s=(qr)^{-1}=r^{-1}q^{-1}}.
$$


::: pf-proof

The relation
$$
qrs=1
$$
is equivalent to the displayed formula.

:::

:::

::: {.pf-step #s1-10}

Eliminating $s$, the second relation becomes
$$
\boxed{r^2=q^{-2}}.
$$


::: pf-proof

By step [](#s1-9){.pf-ref},
$$
s^{-1}=qr.
$$
Thus
$$
s^{-1}rq=1
$$
becomes
$$
qrrq=qr^2q=1.
$$
Multiplying by $q^{-1}$ on both sides gives
$$
r^2=q^{-2}.
$$

:::

:::

::: {.pf-step #s1-11}

Eliminating $s$, the third relation becomes
$$
\boxed{q^{-1}rq=r^{-1}}.
$$


::: pf-proof

Again using
$$
s^{-1}=qr,
$$
the relation
$$
rs^{-1}q^{-1}=1
$$
becomes
$$
rqrq^{-1}=1.
$$
Equivalently,
$$
rqr=q.
$$
Multiplying on the left by $q^{-1}$ and on the right by $r^{-1}$ gives
$$
q^{-1}rq=r^{-1}.
$$

:::

:::

::: {.pf-step #s1-12}

The relations in steps [](#s1-10){.pf-ref} and [](#s1-11){.pf-ref} imply
$$
\boxed{r^4=1}
\qquad\text{and}\qquad
\boxed{q^2=r^2}.
$$


::: pf-proof

Conjugate the equality
$$
r^2=q^{-2}
$$
by $q^{-1}(-)q$. By step [](#s1-11){.pf-ref},
$$
q^{-1}r^2q=r^{-2},
$$
while
$$
q^{-1}q^{-2}q=q^{-2}.
$$
Hence
$$
r^{-2}=q^{-2}.
$$
Together with
$$
r^2=q^{-2},
$$
this gives
$$
r^2=r^{-2},
$$
so
$$
r^4=1.
$$
Then
$$
r^{-2}=r^2,
$$
and therefore
$$
q^2=r^2.
$$

:::

:::

::: {.pf-step #s1-13}

Thus
$$
\pi_1(X)
\cong
\left\langle
r,q
\ \presentationbar\
r^4=1,\ q^2=r^2,\ q^{-1}rq=r^{-1}
\right\rangle.
$$


::: pf-proof

Steps [](#s1-9){.pf-ref} through [](#s1-12){.pf-ref} eliminate $s$ and rewrite the remaining relations in
the displayed standard form.

:::

:::

::: {.pf-step #s1-14}

Every element of the group in step [](#s1-13){.pf-ref} can be written in the form
$$
\boxed{r^a q^b}
$$
with
$$
0\le a<4,
\qquad
b\in\{0,1\}.
$$


::: pf-proof

From
$$
q^{-1}rq=r^{-1}
$$
one obtains
$$
qr=r^{-1}q.
$$
Thus every $q$ can be moved to the right of every $r$. The relation
$$
q^2=r^2
$$
reduces every power of $q$ to exponent $0$ or $1$, and
$$
r^4=1
$$
reduces the exponent of $r$ modulo $4$. Hence there are at most eight
elements.

:::

:::

::: {.pf-step #s1-15}

The presentation in step [](#s1-13){.pf-ref} maps onto the quaternion group
$$
Q_8=\{\pm1,\pm i,\pm j,\pm k\}.
$$


::: pf-proof

Send
$$
r\longmapsto i,
\qquad
q\longmapsto j.
$$
In $Q_8$,
$$
i^4=1,
\qquad
j^2=i^2=-1,
$$
and
$$
j^{-1}ij=i^{-1}.
$$
Thus the defining relations are satisfied. Since $i$ and $j$ generate
$Q_8$, the resulting homomorphism is surjective.

:::

:::

::: {.pf-step #s1-16}

Therefore
$$
\boxed{\pi_1(X)\cong Q_8}.
$$


::: pf-proof

Step [](#s1-14){.pf-ref} shows that the presented group has at most eight elements. Step
[](#s1-15){.pf-ref} gives a surjection onto $Q_8$, which has exactly eight elements.
Hence the presented group has exactly eight elements and the surjection is
an isomorphism.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested CW structure, step [](#s1-8){.pf-ref} gives a presentation
directly from the cell attachments, and step [](#s1-16){.pf-ref} identifies that
presentation with the quaternion group.

:::

:::

:::
