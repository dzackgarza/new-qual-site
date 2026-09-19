---
schema: qual/card@1
id: P-AGH5217CONORMALSPLIT
kind: problem
title: Splitting type of the conormal bundle of rational space curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ruled Surfaces
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.2.17* and the retained Egbert companion, which marks the
    exercise starred but supplies no solution. The proof below puts both
    parametrized curves on the smooth quadric x_0 x_3-x_1 x_2=0. They are
    graphs of the degree-n power map for n=2 and n=3. A direct two-chart
    calculation of the conormal sequence shows that its extension class is
    (n-1) times the generator of H^1(O_{P^1}(-2)); this is always nonzero for
    n=2, while for n=3 it vanishes exactly in characteristic 2. Birkhoff--
    Grothendieck then gives the requested splitting types.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
a. Let $\varphi: \PP_k^1 \rightarrow \PP_k^3$ be the 3-uple embedding (I, Ex. 2.12). Let $\mathcal{I}$ be the sheaf of ideals of the twisted cubic curve $C$ which is the image of $\varphi$. Then $\mathcal{I} / \mathcal{I}^2$ is a locally free sheaf of rank 2 on $C$, so $\varphi^*\left(\mathcal{I} / \mathcal{I}^2\right)$ is a locally free sheaf of rank 2 on $\PP^1$.
  By (2.14), therefore,
  \[
\varphi^*\left(\mathcal{I} / \mathcal{I}^2\right) \cong \mathcal{O}(l) \oplus \mathcal{O}(m)
  .\]
  for some $l, m \in \ZZ$. Determine $l$ and $m$.

b. Repeat part (a) for the embedding $\varphi: \PP^1 \rightarrow \PP^3$ given by $x_0=t^4$, $x_1=t^3 u$, $x_2=t u^3$, $x_3=u^4$, whose image is a nonsingular rational quartic curve.

  Answer: If $\operatorname{char} k \neq 2$, then $l=m=-7$; if $\operatorname{char} k=2$, then $l, m=-6,-8$.
:::

::: {.solution}
For $n\ge2$, consider the parametrized rational curve
$$
\varphi_n:\PP^1\longrightarrow\PP^3,
\qquad
[t:u]\longmapsto
[t^{n+1}:t^nu:tu^n:u^{n+1}].
$$
Thus $n=2$ is the twisted cubic of part (a), and $n=3$ is the quartic of
part (b).

<1>1. The image $C_n$ lies on the smooth quadric
$$
Q=V(x_0x_3-x_1x_2)\subseteq\PP^3,
$$
and under
$$
Q\cong\PP^1\times\PP^1
$$
it is the graph of the power map
$$
[t:u]\longmapsto[t^n:u^n].
$$

::: {.proof}
The parametrization satisfies
$$
x_0x_3-x_1x_2
=
t^{n+1}u^{n+1}-t^nu\,tu^n
=0.
$$
The quadric is smooth because the four partial derivatives of its equation
are
$$
x_3,\qquad -x_2,\qquad -x_1,\qquad x_0,
$$
which have no common projective zero.

Using the Segre coordinates
$$
[a:b]\times[c:d]
\longmapsto
[ac:ad:bc:bd],
$$
the curve is obtained by
$$
[a:b]=[t^n:u^n],
\qquad
[c:d]=[t:u].
$$
The second projection therefore identifies $C_n$ with $\PP^1$, even when
the first power map is inseparable.
:::

<1>2. Let
$$
E_n=\varphi_n^*(\mathcal I_{C_n}/\mathcal I_{C_n}^2).
$$
There is an exact sequence
$$
\boxed{
0\longrightarrow\OO_{\PP^1}(-2n-2)
\longrightarrow E_n
\longrightarrow\OO_{\PP^1}(-2n)
\longrightarrow0.}
$$

::: {.proof}
For the regular immersions
$$
C_n\subset Q\subset\PP^3,
$$
the conormal sequence is
$$
0
\longrightarrow
\mathcal I_Q/\mathcal I_Q^2|_{C_n}
\longrightarrow
\mathcal I_{C_n}/\mathcal I_{C_n}^2
\longrightarrow
\mathcal I_{C_n/Q}/\mathcal I_{C_n/Q}^2
\longrightarrow0.
$$

The quadric is a hypersurface of degree $2$, so
$$
\mathcal I_Q/\mathcal I_Q^2|_{C_n}
\cong
\OO_{C_n}(-2).
$$
Since
$$
\varphi_n^*\OO_{\PP^3}(1)=\OO_{\PP^1}(n+1),
$$
its pullback is
$$
\OO_{\PP^1}(-2n-2).
$$

As a divisor on $Q\cong\PP^1\times\PP^1$, the graph $C_n$ has type
$(1,n)$, hence
$$
C_n^2=2n.
$$
Therefore
$$
\mathcal I_{C_n/Q}/\mathcal I_{C_n/Q}^2
\cong
\OO_{C_n}(-C_n)
\cong
\OO_{\PP^1}(-2n).
$$
Pulling the conormal sequence back along the isomorphism
$\varphi_n:\PP^1\xrightarrow{\sim}C_n$ gives the displayed sequence.
:::

<1>3. The extension class of step <1>2 is
$$
\boxed{(n-1)\eta}
$$
where
$$
0\ne\eta\in H^1(\PP^1,\OO_{\PP^1}(-2))
$$
is a generator.

::: {.proof}
Use the affine chart $x_0\ne0$ with coordinates
$$
a=\frac{x_1}{x_0},
\qquad
b=\frac{x_2}{x_0},
\qquad
c=\frac{x_3}{x_0}.
$$
Put
$$
q=c-ab,
\qquad
h=b-a^n.
$$
Then $q,h$ generate the ideal of $C_n$ on this chart. Along the
parametrization, with
$$
s=\frac ut,
$$
one has
$$
a=s,
\qquad
b=s^n,
\qquad
c=s^{n+1}.
$$

On the chart $x_3\ne0$, put
$$
\alpha=\frac{x_1}{x_3},
\qquad
\beta=\frac{x_2}{x_3},
\qquad
\gamma=\frac{x_0}{x_3},
$$
and take generators
$$
q'=\gamma-\alpha\beta,
\qquad
h'=\alpha-\beta^n.
$$
On the overlap,
$$
\alpha=\frac a c,
\qquad
\beta=\frac b c,
\qquad
\gamma=\frac1c.
$$
Thus, modulo the square of the ideal $(q,h)$,
$$
q'=\frac{q}{c^2}
\equiv
s^{-2n-2}q.
$$

For the second generator,
$$
h'
=
\frac{a c^{n-1}-b^n}{c^n}.
$$
Substitute
$$
b=a^n+h,
\qquad
c=ab+q=a^{n+1}+ah+q
$$
and retain only terms linear in $q,h$. The numerator becomes
$$
-a^{n^2-n}h
+
(n-1)a^{n^2-n-1}q
\pmod{(q,h)^2}.
$$
Since $c^n\equiv a^{n^2+n}$ to zeroth order, one gets
$$
h'
\equiv
-s^{-2n}h
+
(n-1)s^{-2n-1}q
\pmod{(q,h)^2}.
$$

The diagonal factors
$$
s^{-2n-2},
\qquad
s^{-2n}
$$
are precisely the transition functions of the two line bundles in step
<1>2. After factoring them out, the off-diagonal term is represented by
$$
(n-1)s^{-1}.
$$
On the standard two-chart cover of $\PP^1$, $s^{-1}$ represents a generator
of
$$
H^1(\PP^1,\OO(-2)).
$$
Hence the extension class is $(n-1)\eta$.
:::

<1>4. If the extension class in step <1>3 is zero, then
$$
E_n
\cong
\OO(-2n)\oplus\OO(-2n-2).
$$
If it is nonzero, then
$$
\boxed{E_n\cong\OO(-2n-1)\oplus\OO(-2n-1).}
$$

::: {.proof}
The zero-class assertion is exactly the definition of a split extension.

Assume the class is nonzero and twist the exact sequence of step <1>2 by
$\OO(2n)$:
$$
0
\longrightarrow
\OO(-2)
\longrightarrow
E_n(2n)
\longrightarrow
\OO
\longrightarrow0.
$$
Its connecting map
$$
H^0(\OO)\longrightarrow H^1(\OO(-2))
$$
is the nonzero extension class. Both spaces are one-dimensional, so this map
is an isomorphism. Consequently
$$
H^0(E_n(2n))=0.
$$

By Birkhoff--Grothendieck, write
$$
E_n\cong\OO(l)\oplus\OO(m),
\qquad
l\ge m.
$$
Step <1>2 gives
$$
l+m=-4n-2.
$$
The vanishing of $H^0(E_n(2n))$ implies
$$
l+2n<0,
$$
so
$$
l\le-2n-1.
$$
But $l$ is at least the average $(l+m)/2=-2n-1$. Hence
$$
l=m=-2n-1.
$$
:::

<1>5. For the twisted cubic,
$$
\boxed{l=m=-5.}
$$

::: {.proof}
Here $n=2$. By step <1>3 the extension class is
$$
(2-1)\eta=\eta\ne0
$$
over every field. Step <1>4 therefore gives
$$
E_2\cong\OO(-5)\oplus\OO(-5).
$$
This proves part (a).
:::

<1>6. For the rational quartic,
$$
\boxed{
E_3\cong
\begin{cases}
\OO(-7)\oplus\OO(-7),&\operatorname{char}k\ne2,\\
\OO(-6)\oplus\OO(-8),&\operatorname{char}k=2.
\end{cases}}
$$

::: {.proof}
Here $n=3$. Step <1>3 gives extension class
$$
2\eta.
$$
If $\operatorname{char}k\ne2$, this is nonzero, and step <1>4 gives
$$
E_3\cong\OO(-7)\oplus\OO(-7).
$$
If $\operatorname{char}k=2$, the class vanishes, so the sequence splits:
$$
E_3
\cong
\OO(-6)\oplus\OO(-8).
$$
This is exactly the answer stated in part (b).
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>5 proves part (a), and step <1>6 proves part (b).
:::
:::
