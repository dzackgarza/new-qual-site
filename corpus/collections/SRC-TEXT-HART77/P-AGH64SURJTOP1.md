---
schema: qual/card@1
id: P-AGH64SURJTOP1
kind: problem
title: A nonconstant rational function on a projective curve gives a surjection onto $\PP^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nonsingular Curves
  - Morphisms
  - Function Fields
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.6.4 and Proposition I.6.8 in the Hartshorne source. The proof extends the rational function to a morphism into projective space, uses completeness to force a nonconstant image to be all of P^1, and proves each fibre finite as a proper closed subset of a curve.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $Y$ be a nonsingular projective curve.
Show that every nonconstant rational function $f$ on $Y$ defines a surjective morphism $\varphi: Y \to \PP^1$, and that for every $P \in \PP^1$ the fibre $\varphi^{-1}(P)$ is a finite set of points.
:::

::: {.solution}
Let $K=K(Y)$ and let $f\in K\setminus k$.

::: pf

::: {.pf-step #morphism-on-open-subset}
The rational function $f$ defines a morphism from a nonempty open subset of $Y$ to $\PP^1$.

::: pf-proof
There is a nonempty open subset $U\subseteq Y$ on which $f$ is regular.
On $U$ define
$$
\varphi_U:U\longrightarrow\PP^1,
\qquad
Q\longmapsto[f(Q):1].
$$
This is a morphism because its image lies in the standard affine chart $\AA^1\subseteq\PP^1$ and is represented there by the regular function $f\restrict_U$.
:::

:::

::: {.pf-step #morphism-extends-to-y}
The morphism $\varphi_U$ extends uniquely to a morphism $\varphi:Y\to\PP^1$.

::: pf-proof
The complement $Y\setminus U$ is a proper closed subset of the noetherian irreducible curve $Y$, hence is finite.
Write it as $\{P_1,\ldots,P_m\}$.
Proposition I.6.8 says that for an abstract nonsingular curve $X$, a point $P\in X$ and a projective variety $Z$, a morphism $X\setminus\{P\}\to Z$ extends uniquely over $P$.
A nonsingular quasi-projective curve is isomorphic to an abstract nonsingular curve by Proposition I.6.7, so the proposition applies to the curves below.

Starting with $U_0=U$, put $U_i=U\cup\{P_1,\ldots,P_i\}$.
The open subset $U_i$ of the nonsingular curve $Y$ is itself a nonsingular curve, and
$$
U_i\setminus\{P_i\}=U_{i-1}.
$$
Thus Proposition I.6.8 extends the morphism on $U_{i-1}$ uniquely to $U_i$.
At each stage the target is the projective variety $\PP^1$.
After finitely many steps we obtain a morphism
$$
\varphi:Y\longrightarrow\PP^1
$$
whose restriction to $U$ is $\varphi_U$.
Uniqueness at each extension step makes the final morphism unique.
:::

:::

::: {.pf-step #morphism-nonconstant-surjective}
The morphism $\varphi$ is nonconstant and surjective.

::: pf-proof
If $\varphi$ were constant, then its restriction to $U$ would be constant.
Since $\varphi_U$ is given in the affine chart by $f$, this would force $f$ to be constant in the function field, contrary to the hypothesis.

Because $Y$ is projective over $k$, it is complete, so the image $\varphi(Y)$ is closed in $\PP^1$.
The image of the irreducible space $Y$ is irreducible.
The only irreducible closed subsets of $\PP^1$ are points and $\PP^1$ itself.
The image is not a point because $\varphi$ is nonconstant.
Therefore
$$
\boxed{\varphi(Y)=\PP^1}.
$$
:::

:::

::: {.pf-step #fibres-finite}
Every fibre of $\varphi$ is finite.

::: pf-proof
Fix $P\in\PP^1$.
The fibre
$$
\varphi^{-1}(P)
$$
is closed in $Y$ because $P$ is closed.
It is a proper subset: if it were all of $Y$, then $\varphi$ would be constant with value $P$, contradicting step [](#morphism-nonconstant-surjective){.pf-ref}.

A proper closed subset of an irreducible noetherian curve has dimension zero.
Such a closed subset has only finitely many irreducible components, each of which is a closed point.
Hence $\varphi^{-1}(P)$ is a finite set of points.
:::

:::

::: pf-qed
Steps [](#morphism-on-open-subset){.pf-ref} and [](#morphism-extends-to-y){.pf-ref} construct the morphism associated to $f$, step [](#morphism-nonconstant-surjective){.pf-ref} proves that it is surjective, and step [](#fibres-finite){.pf-ref} proves that every fibre is finite.
:::

:::
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 6.4, PDF p. 8: a nonconstant rational map $Y\to\PP^1$ induces an injection $k(x)\to k(Y)$, "then every valuation ring of $k(x)$ can be extended to one of $k(Y)$, so every point of $\PP^1$ is the image of a point of $Y$"; and $\varphi^{-1}(P)$ is closed, while an infinite closed subset of the curve $Y$ is all of $Y$, which a nonconstant map does not have as a fibre. Surjectivity here rests on the extension of valuation rings, quoted and not proved.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), stops at §I.5 and gives no solution to 6.4.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.6.4, PDF p. 54: "$f$ induces a map $Y\to\AA^1$ by $x\mapsto f(x)$ and therefore $\varphi:Y\to\PP^1$; as $f$ is nonconstant and $Y$ irreducible, $\mathrm{im}(\varphi)=\PP^1$ and $\varphi$ is dominant, so induces $k(Y)\hookrightarrow k(\PP^1)$. If $P\in\PP^1$, then $\varphi^{-1}(P)$ is closed by continuity and finite since it's a proper subset of $Y$ with closure not $Y$ as $\varphi$ is nonconstant." The field map runs the wrong way round, and closedness plus properness of a subset is not finiteness.
Joe Cutrone and Nick Marshburn, *Algebraic Geometry by Robin Hartshorne: Solutions*, Exercise I.6.4, PDF pp. 24--25: the same construction, "since $Y$ is projective, the image must be closed in $\PP^1$; since $f$ is nonconstant and $Y$ irreducible, the image must be all of $\PP^1$", then finiteness through a finite module $k[V]$ over $k[\varphi(V)]$ from the theorem of finiteness of integral closure (I.3.9), with the two coordinate rings notated identically.
Steps [](#morphism-extends-to-y){.pf-ref} and [](#morphism-nonconstant-surjective){.pf-ref} obtain surjectivity from completeness, as Cutrone--Marshburn do, and finiteness from a proper closed subset of the curve rather than from a finiteness-of-integral-closure argument. Step [](#morphism-extends-to-y){.pf-ref} also names Proposition I.6.7, without which I.6.8 cannot be applied to a morphism on an open subset of a projective curve: I.6.8 is stated for abstract nonsingular curves. Matches.
:::
