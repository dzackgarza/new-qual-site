---
schema: qual/card@1
id: P-AGH327CIRCLE
kind: problem
title: Derived functor cohomology of the circle
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Constant Sheaves
  - Topological Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both parts with the retained Hartshorne Chapter III section 2 transcription. The proof uses an injective resolution, a finite partition of unity applied only to continuous-function differences, and the real covering of the circle to compute the derived-functor group without a singular-cohomology comparison.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $S^1$ be the circle (with its usual topology), and let $\ZZ$ be the constant sheaf $\ZZ$.

(a) Show that $H^1(S^1, \ZZ) \cong \ZZ$, using our definition of cohomology.

(b) Now let $\mcr$ be the sheaf of germs of continuous real-valued functions on $S^1$.
Show that $H^1(S^1, \mcr)=0$.
:::

::: {.solution}
Put $X=S^1$ and identify it with $\RR/\ZZ$ through $t\mapsto e^{2\pi it}$.
The sections of $\mcr$ on an open set $U$ are the continuous functions $U\to\RR$.
Let $\mathcal T$ be the sheaf of continuous functions $U\to\RR/\ZZ$, with pointwise addition.
The notation $\ZZ$ denotes the sheaf of locally constant integer-valued functions, not the constant presheaf.

<1>1. If $0\to\mcr\to I\to Q\to0$ is a short exact sequence of abelian sheaves on $X$, then $\Gamma(X,I)\to\Gamma(X,Q)$ is surjective.

::: {.proof}
Take $q\in\Gamma(X,Q)$ and choose local lifts $t_i\in I(U_i)$.
Compactness gives finitely many such opens covering $X$.
After refining and allowing repetitions of the $U_i$, choose open sets $V_i$ still covering $X$ with $\overline{V_i}\subseteq U_i$.
This is possible by taking sufficiently small metric balls around each point and then a finite subcover.
There are continuous functions $\rho_i:X\to[0,1]$ with $\sum_i\rho_i=1$ and $\operatorname{supp}\rho_i\subseteq U_i$.
For an explicit construction, take $\phi_i(x)=\operatorname{dist}(x,X\setminus V_i)$, with $\phi_i=1$ when $V_i=X$, and put $\rho_i=\phi_i/\sum_h\phi_h$.
The denominator is everywhere positive and each support is contained in $\overline{V_i}$.

On $U_i\cap U_j$, the difference $c_{ij}=t_i-t_j$ is a section of $\mcr$.
On triple overlaps it satisfies $c_{ij}-c_{hj}=c_{ih}$.
Define on $U_i$ the continuous function
$$
b_i=\sum_j\rho_j c_{ij},
$$
where each product, initially defined on $U_i\cap U_j$, is extended by zero to $U_i$.
This extension is continuous, since $\operatorname{supp}\rho_j$ is a closed subset contained in $U_j$; near a point outside $U_j$ the product is identically zero.
On $U_i\cap U_h$, the cocycle identity and $\sum_j\rho_j=1$ give $b_i-b_h=c_{ih}$.
Thus $t_i-b_i$ agree and glue to a global section of $I$ lifting $q$.
Only the differences in $\mcr$ have been multiplied by continuous functions; the sheaf $I$ need not be a sheaf of $\mcr$-modules.
:::

<1>2. There is an exact sequence of sheaves
$$
0\longrightarrow\ZZ\longrightarrow\mcr
\xrightarrow{a\mapsto a\bmod\ZZ}\mathcal T\longrightarrow0,
$$
and the connecting map identifies $H^1(X,\ZZ)$ with the cokernel of $\Gamma(X,\mcr)\to\Gamma(X,\mathcal T)$.

::: {.proof}
The kernel consists of continuous integer-valued functions, which are locally constant.
Every continuous map into $\RR/\ZZ$ has a local real lift, since the covering $\RR\to\RR/\ZZ$ restricts to a homeomorphism on a sufficiently small interval around any chosen lift of a point.
Thus the last map is surjective on stalks and the sequence is exact.

Embed $\mcr$ into an injective abelian sheaf $I$ and let $Q=I/\mcr$.
The derived-functor long exact sequence gives
$$
\Gamma(X,I)\longrightarrow\Gamma(X,Q)\longrightarrow H^1(X,\mcr)\longrightarrow0,
$$
because an injective sheaf has zero higher derived functors.
Step <1>1 makes the first arrow surjective.
Therefore $H^1(X,\mcr)=0$.
The long exact sequence of the displayed lifting sequence now gives
$$
\Gamma(X,\mcr)\longrightarrow\Gamma(X,\mathcal T)
\longrightarrow H^1(X,\ZZ)\longrightarrow0
$$
[@Har10a, Chapter III, §§1 and 2].
This proves the asserted cokernel description using the derived-functor definition.
:::

<1>3. The cokernel in step <1>2 is $\ZZ$, proving $\boxed{H^1(S^1,\ZZ)\cong\ZZ}$ in (a).

::: {.proof}
Let $f:X\to\RR/\ZZ$ be continuous, and let $p:[0,1]\to X$ be $p(t)=t\bmod\ZZ$.
The composite $f\circ p$ has a continuous lift $a:[0,1]\to\RR$.
Indeed, its local lifts cover the compact interval; subdivide the interval into finitely many subintervals on each of which one lift is defined, and adjust consecutive lifts by integers to agree at their shared endpoints.
These finitely many lifts then glue.
Two such lifts differ by a continuous integer-valued function on the connected interval, hence by a constant integer.
Since $p(0)=p(1)$,
$$
\deg(f)\coloneqq a(1)-a(0)\in\ZZ
$$
is independent of the lift.
Adding lifts shows that this is a homomorphism from $\Gamma(X,\mathcal T)$ to $\ZZ$.
For every integer $m$, the function $f_m(t\bmod\ZZ)=mt\bmod\ZZ$ has degree $m$, so the homomorphism is surjective.

If $f$ is the reduction of a continuous real-valued function on $X$, its lift along $p$ has equal endpoint values, so $\deg(f)=0$.
Conversely, when $\deg(f)=0$, the lift $a$ has equal endpoint values and descends to a continuous function $X=[0,1]/(0\sim1)\to\RR$.
Its reduction is $f$.
Thus the kernel of degree is exactly the image of $\Gamma(X,\mcr)$.
The first isomorphism theorem and step <1>2 give the claimed group.
With the chosen orientation, the connecting class of $f_1$ is a generator.
:::

<1>4. In (b), $\boxed{H^1(S^1,\mcr)=0}$.

::: {.proof}
In step <1>2, the degree-one derived functor was identified with the cokernel of $\Gamma(X,I)\to\Gamma(X,I/\mcr)$ for an injective embedding $\mcr\hookrightarrow I$.
The explicit partition-of-unity correction in step <1>1 makes this cokernel zero, proving (b).
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>2--<1>3 compute the group in (a), using the lifting lemma of step <1>1; step <1>4 gives (b).
:::
:::
