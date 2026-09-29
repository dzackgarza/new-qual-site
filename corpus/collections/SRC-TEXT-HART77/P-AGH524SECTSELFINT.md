---
schema: qual/card@1
id: P-AGH524SECTSELFINT
kind: problem
title: Possible self-intersection numbers of sections of $C \times \PP^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.2.4, the retained Egbert companion calculation, Exercise
    IV.6.8 as represented by the base-point-free nonspecial divisor card, and
    the local cards on gonality, hyperelliptic canonical systems, genus-three
    canonical models, and maps from pencils. A section of C x P^1 is the graph
    of a map u:C->P^1 and has normal bundle u^*T_{P^1}, so its square is twice
    deg(u). The genus-three cases are then proved directly: hyperelliptic curves
    have degree two but no base-point-free degree-three pencil, while a
    nonhyperelliptic genus-three curve is a plane quartic and projection from a
    point gives a degree-three pencil.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $C$ be a curve of genus $g$, and let $X$ be the ruled surface $C \times \PP^1$.
We consider the question, for what integers $s \in \ZZ$ does there exist a section $D$ of $X$ with $D^2=s$?
First show that $s$ is always an even integer, say $s=2 r$.

a. Show that $r=0$ and any $r \geqslant g+1$ are always possible.
Cf.
(V, Ex.
6.8).

b. If $g=3$, show that $r=1$ is not possible, and just one of the two values $r=2,3$ is possible, depending on whether $C$ is hyperelliptic or not.
:::

::: {.solution}
Let
$$
p_1:C\times\PP^1\longrightarrow C
$$
be the first projection.

::: pf

::: {.pf-step #s1}

Every section $D$ of $p_1$ is the graph $\Gamma_u$ of a unique morphism
$$
u:C\longrightarrow\PP^1.
$$

::: pf-proof

If
$$
\sigma:C\longrightarrow C\times\PP^1
$$
is a section, then
$$
p_1\circ\sigma=\id_C.
$$
Writing
$$
u=p_2\circ\sigma,
$$
one has
$$
\sigma(P)=(P,u(P)),
$$
so the image of $\sigma$ is the graph of $u$. Conversely every graph gives a
section. Uniqueness is immediate from the second projection.

:::

:::

::: {.pf-step #s2}

For $D=\Gamma_u$,
$$
\mcn_{D/(C\times\PP^1)}\cong u^*T_{\PP^1}.
$$

::: pf-proof

Restrict the tangent bundle of the product to the graph. Under the
identification $D\cong C$ this gives
$$
T_{C\times\PP^1}|_D
\cong
T_C\oplus u^*T_{\PP^1}.
$$
The differential of the graph embedding is
$$
T_C\longrightarrow T_C\oplus u^*T_{\PP^1},
\qquad
v\longmapsto(v,du(v)).
$$
The map
$$
T_C\oplus u^*T_{\PP^1}\longrightarrow u^*T_{\PP^1},
\qquad
(v,w)\longmapsto w-du(v)
$$
is surjective and has exactly this graph as its kernel. Hence the quotient in
the normal sequence is $u^*T_{\PP^1}$.

:::

:::

::: {.pf-step #s3}

Every section has even, nonnegative self-intersection, namely
$$
\boxed{D^2=2\deg u}.
$$

::: pf-proof

For a smooth curve on a smooth surface, self-intersection is the degree of the
normal bundle. By step [](#s2){.pf-ref},
$$
D^2
=
\deg u^*T_{\PP^1}.
$$
Since
$$
T_{\PP^1}\cong\OO_{\PP^1}(2),
$$
one obtains
$$
D^2=2\deg u.
$$
For a constant map set $\deg u=0$; for a nonconstant map the degree is a
positive integer. Thus every possible self-intersection is of the form
$s=2r$ with $r\ge0$.

:::

:::

::: {.pf-step #s4}

The value $r=0$ always occurs.

::: pf-proof

Take $u:C\to\PP^1$ to be constant. Its graph is the horizontal section
$$
C\times\{Q\},
$$
and step [](#s3){.pf-ref} gives self-intersection zero.

:::

:::

::: {.pf-step #s5}

For every integer
$$
r\ge g+1
$$
there is a morphism $u:C\to\PP^1$ of degree $r$.

::: pf-proof

Exercise IV.6.8, proved on [[P-AGH468BASEPOINTFREENONSPECIAL]], gives a
nonspecial line bundle $L$ of degree $r$ whose complete linear system is
base-point free. Riemann--Roch gives
$$
h^0(C,L)=r+1-g\ge2.
$$

Choose a nonzero section $s_0\in H^0(C,L)$. Its zero divisor has finite
support. For each point $P$ in that support, global generation says that the
subspace of sections vanishing at $P$ is a proper hyperplane in $H^0(C,L)$.
Because the ground field is infinite, a finite union of proper hyperplanes
cannot cover $H^0(C,L)$. Hence one can choose $s_1$ nonzero at every zero of
$s_0$. The two-dimensional space
$$
V=\langle s_0,s_1\rangle
$$
is therefore base-point free.

By the degree statement for pencil maps [[T-DIVMAPPN]], $V$ defines a finite
morphism
$$
u:C\longrightarrow\PP^1
$$
of degree
$$
\deg L=r.
$$

:::

:::

::: {.pf-step #s6}

The values
$$
\boxed{r=0\quad\text{and every }r\ge g+1}
$$
always occur.

::: pf-proof

Combine steps [](#s4){.pf-ref} and [](#s5){.pf-ref} with the graph construction in step [](#s1){.pf-ref} and the
self-intersection formula in step [](#s3){.pf-ref}. This proves part (a).

:::

:::

::: {.pf-step #s7}

Assume now $g=3$. The value $r=1$ is impossible.

::: pf-proof

If $r=1$ occurred, step [](#s3){.pf-ref} would give a degree-one morphism
$$
u:C\longrightarrow\PP^1.
$$
A finite degree-one morphism of nonsingular projective curves is birational,
so uniqueness of the smooth projective model [[T-CRVMINMOD]] would imply
$$
C\cong\PP^1,
$$
contradicting $g(C)=3$.

:::

:::

::: {.pf-step #s8}

If $C$ is hyperelliptic of genus three, then $r=2$ occurs.

::: pf-proof

By definition, a hyperelliptic curve has a degree-two morphism
$$
h:C\longrightarrow\PP^1
$$
[[D-CRVHYP]]. Its graph therefore has self-intersection four by step [](#s3){.pf-ref}, so
$r=2$ occurs.

:::

:::

::: {.pf-step #s9}

If $C$ is hyperelliptic of genus three, then $r=3$ does not occur.

::: pf-proof

Let $A$ denote the unique hyperelliptic $g^1_2$. Suppose for contradiction
that there were a degree-three morphism $u:C\to\PP^1$. Then
$$
L=u^*\OO_{\PP^1}(1)
$$
has degree three and is generated by the pulled-back two-dimensional space of
sections. In particular
$$
h^0(C,L)\ge2.
$$

Riemann--Roch on the genus-three curve gives
$$
h^0(C,L)-h^0(C,K_C\tensor L^{-1})=1.
$$
Hence $K_C\tensor L^{-1}$ has a nonzero section. It has degree one, so
$$
K_C\tensor L^{-1}\cong\OO_C(Q)
$$
for some point $Q\in C$. Therefore
$$
L\cong K_C(-Q).
$$

For a genus-three hyperelliptic curve, [[D-CRVHYP]] gives
$$
K_C\sim2A.
$$
Let $Q'$ be the residual point in the hyperelliptic fibre through $Q$, so
$$
Q+Q'\sim A
$$
(possibly $Q'=Q$ at a ramification point). Then
$$
L\sim2A-Q\sim A+Q'.
$$
Now $h^0(C,A)=2$. Since $K_C\tensor L^{-1}\cong\OO_C(Q)$ has exactly one
section on the nonrational curve $C$, Riemann--Roch gives
$$
h^0(C,L)=2.
$$
The natural inclusion
$$
H^0(C,A)\hookrightarrow H^0(C,A+Q')=H^0(C,L)
$$
is therefore an isomorphism. Every section of $L$ consequently vanishes at
the added point $Q'$, so $Q'$ is a base point of $|L|$. This contradicts the
fact that the two pulled-back sections from $\PP^1$ generate $L$. Thus no
degree-three morphism exists.

:::

:::

::: {.pf-step #s10}

If $C$ is nonhyperelliptic of genus three, then $r=2$ does not occur.

::: pf-proof

A degree-two morphism to $\PP^1$ is exactly a $g^1_2$, hence would make $C$
hyperelliptic by [[D-CRVHYP]]. Thus no such morphism exists.

:::

:::

::: {.pf-step #s11}

If $C$ is nonhyperelliptic of genus three, then $r=3$ occurs.

::: pf-proof

By the genus-three canonical model [[FE-CRVLOWG]], the canonical linear system
embeds $C$ as a smooth plane quartic
$$
C\hookrightarrow\PP^2.
$$
Fix a point $P\in C$ and consider the pencil of lines through $P$. On $C$ each
line cuts a canonical divisor of degree four containing $P$, so after removing
the fixed point $P$ the pencil has degree three.

It has no base point. For $Q\ne P$, choose a line through $P$ that does not
pass through $Q$. At $P$, choose a line through $P$ that is not tangent to the
smooth quartic; its intersection multiplicity with $C$ at $P$ is one, so after
subtracting the fixed copy of $P$ the residual divisor does not contain $P$.
Thus this is a base-point-free $g^1_3$, hence by [[T-DIVMAPPN]] it defines a
degree-three morphism
$$
C\longrightarrow\PP^1.
$$
Step [](#s3){.pf-ref} then gives a section of self-intersection six, so $r=3$ occurs.

:::

:::

::: {.pf-step #s12}

For genus three, exactly one of $r=2,3$ occurs:
$$
\boxed{
\begin{array}{c|cc}
&r=2&r=3\\ \hline
C\text{ hyperelliptic}&\text{yes}&\text{no}\\
C\text{ nonhyperelliptic}&\text{no}&\text{yes}
\end{array}}
$$

::: pf-proof

This is exactly the combination of steps [](#s8){.pf-ref}, [](#s9){.pf-ref}, [](#s10){.pf-ref} and [](#s11){.pf-ref}. Together with step
[](#s7){.pf-ref}, it proves part (b).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} identify possible self-intersections with twice the degrees of
maps to $\PP^1$; steps [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} prove part (a), and steps [](#s7){.pf-ref}, [](#s8){.pf-ref}, [](#s9){.pf-ref}, [](#s10){.pf-ref}, [](#s11){.pf-ref} and [](#s12){.pf-ref} prove
part (b).

:::

:::

:::
