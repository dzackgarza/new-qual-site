---
schema: qual/card@1
id: P-AGH511EULERCHAR
kind: problem
title: Intersection number as an alternating sum of Euler characteristics
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Intersection Theory
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.1.1, the retained Egbert companion proof, the surface
    intersection-pairing definition, the degree formula for line bundles on
    curves, and II.7.5 on very ample twists. The source statement needs no
    correction. The companion proof treats transverse effective curves and
    leaves the extension to arbitrary divisors implicit. The proof below
    avoids surface Riemann--Roch and proves the full statement by computing
    the change in the four-term Euler expression when one smooth curve is
    added, then writing an arbitrary divisor as a difference of two smooth
    very ample divisors.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $C, D$ be any two divisors on a surface $X$, and let the corresponding invertible sheaves be $\mathcal{L}, \mathcal{M}$.
Show that
\[
C . D=\chi\left(\mathcal{O}_X\right)-\chi\left(\mathcal{L}^{-1}\right)-\chi\left(\mathcal{M}^{-1}\right)+\chi\left(\mathcal{L}^{-1} \otimes \mathcal{M}^{-1}\right) .
\]
:::

::: {.solution}
For divisors $A,D$ on $X$, put
$$
\Phi(A,D)
=
\chi(\OO_X)
-\chi(\OO_X(-A))
-\chi(\OO_X(-D))
+\chi(\OO_X(-A-D)).
$$
The required identity is
$$
\Phi(C,D)=C\cdot D.
$$

<1>1. Let $E\subseteq X$ be a nonsingular irreducible curve.  For arbitrary
divisors $A,D$ on $X$,
$$
\Phi(A+E,D)-\Phi(A,D)=E\cdot D.
$$

::: {.proof}
Since $E$ is an effective Cartier divisor on the nonsingular surface $X$,
there are exact sequences
$$
0
\longrightarrow
\OO_X(-A-E)
\longrightarrow
\OO_X(-A)
\longrightarrow
\OO_E(-A)
\longrightarrow0
$$
and
$$
0
\longrightarrow
\OO_X(-A-D-E)
\longrightarrow
\OO_X(-A-D)
\longrightarrow
\OO_E(-A-D)
\longrightarrow0.
$$
Additivity of Euler characteristic gives
$$
\begin{aligned}
\Phi(A+E,D)-\Phi(A,D)
&=
\chi(\OO_E(-A))
-\chi(\OO_E(-A-D)).
\end{aligned}
$$

For a line bundle $N$ on the nonsingular projective curve $E$,
[[D-CRVDEGREES]] gives
$$
\chi(E,N)=\chi(E,\OO_E)+\deg_E N.
$$
Applying this to
$$
N=\OO_E(-A)
$$
and
$$
N\tensor\OO_E(-D)=\OO_E(-A-D)
$$
yields
$$
\chi(\OO_E(-A))-
\chi(\OO_E(-A-D))
=
\deg_E\OO_E(D).
$$
By the definition of the surface intersection pairing [[D-SRFINT]],
$$
\deg_E\OO_E(D)=E\cdot D.
$$
This proves the claim.
:::

<1>2. Every divisor $C$ is linearly equivalent to
$$
P-Q
$$
for nonsingular irreducible effective divisors $P,Q$.

::: {.proof}
Choose a very ample divisor $H$ on $X$.  By the ample/very-ample properties
of [[P-AGH275AMPLEPROPS|Exercise II.7.5]], the sheaf
$$
\OO_X(C+(n-1)H)
$$
is globally generated for all sufficiently large $n$: this is the defining
large-twist property of the ample sheaf $\OO_X(H)$.  Since $\OO_X(H)$ is
very ample, part (d) of that exercise makes
$$
\OO_X(C+nH)
=
\OO_X(H)\tensor\OO_X(C+(n-1)H)
$$
very ample.  Also $\OO_X((n-1)H)$ is globally generated for every $n\ge1$,
so the same part (d) makes $\OO_X(nH)$ very ample.  Thus, for all
sufficiently large $n$, both divisor classes
$$
C+nH
\qquad\text{and}\qquad
nH
$$
are very ample.

Choose general members
$$
P\in\abs{C+nH},
\qquad
Q\in\abs{nH}.
$$
Each complete linear system is the hyperplane system of its very ample
embedding.  Bertini's hyperplane theorem [[T-BERTINI]] therefore makes a
general member nonsingular; because $X$ is irreducible of dimension $2$, the
same theorem makes the general hyperplane section connected.  A nonsingular
curve is regular, so its distinct irreducible components are disjoint and
open-and-closed.  Connectedness therefore forces only one component.
Thus $P$ and $Q$ are nonsingular irreducible effective divisors, and
$$
P-Q\sim C.
$$
:::

<1>3. For the divisor $Q$ of step <1>2,
$$
\Phi(-Q,D)=-Q\cdot D.
$$

::: {.proof}
Apply step <1>1 with
$$
A=-Q,
\qquad
E=Q.
$$
It gives
$$
\Phi(0,D)-\Phi(-Q,D)=Q\cdot D.
$$
Directly from the definition,
$$
\Phi(0,D)=0.
$$
Hence
$$
\Phi(-Q,D)=-Q\cdot D.
$$
:::

<1>4. For arbitrary divisors $C,D$,
$$
\Phi(C,D)=C\cdot D.
$$

::: {.proof}
Choose $P,Q$ as in step <1>2, so
$$
C\sim P-Q.
$$
The expression $\Phi(C,D)$ depends only on the invertible sheaves associated
to the divisor classes, and the intersection pairing depends only on linear
equivalence.  Thus it is enough to compute with $P-Q$.

Apply step <1>1 with
$$
A=-Q,
\qquad
E=P.
$$
Then
$$
\Phi(P-Q,D)-\Phi(-Q,D)=P\cdot D.
$$
Using step <1>3,
$$
\Phi(P-Q,D)
=
P\cdot D-Q\cdot D
=
(P-Q)\cdot D
=
C\cdot D.
$$
:::

<1>5. Q.E.D.

::: {.proof}
For the line bundles
$$
\mathcal L=\OO_X(C),
\qquad
\mathcal M=\OO_X(D),
$$
step <1>4 reads
$$
C\cdot D
=
\chi(\OO_X)
-\chi(\mathcal L^{-1})
-\chi(\mathcal M^{-1})
+\chi(\mathcal L^{-1}\tensor\mathcal M^{-1}),
$$
which is exactly the desired formula.
:::
:::
